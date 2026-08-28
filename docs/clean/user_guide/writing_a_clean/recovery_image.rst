.. _clean_doc_recovery_image:

Recovery Images
===============

The ``recovery_image`` stage keeps one or more stable image files on a device
for later device recovery. It compares each remote recovery image with its
local target, copies images that are missing or do not satisfy the requested
verification, verifies the result, and publishes the local paths under
``device.clean.device_recovery.golden_image``.

Recovery images are separate from the images used to install or upgrade the
device. See `Recovery Images and Image Management`_ for the distinction.

Source and Target Paths
-----------------------

The stage uses two different path types:

* ``recovery_image.images`` contains canonical paths to files on the recovery
  server. A canonical path is the normal, stable filesystem path produced by
  image discovery. Do not replace it in the Clean YAML with a temporary URL,
  cache path, or transport-specific shortened path. A platform-specific stage
  may adapt the path immediately before copying it without changing the public
  Clean contract.
* ``recovery_image.golden_image`` contains stable local paths on the device.
  These are the paths that subsequent recovery code can boot.

``images`` and ``golden_image`` are paired by position, and their list lengths
must match. ``golden_image`` may also be written as a string when there is only
one target.

When ``golden_image`` is omitted, the stage first uses an existing
``device_recovery.golden_image`` value. If that is also absent and ``images``
is present, the stage uses the platform default directory and creates the
following target names:

* ``golden_image.bin`` for one source image.
* ``golden_image_1.bin``, ``golden_image_2.bin``, and so on for multiple source
  images.

Set ``destination.directory`` when the recovery files must be stored on a
specific filesystem. ``destination.standby_directory`` and
``destination.stack_directory`` request equivalent copies on additional
destinations.

If only a local ``golden_image`` is configured, the stage verifies that it
exists and publishes it without copying. It fails if the local file is
missing. If neither a recovery source nor a golden-image target is configured,
the stage skips. This makes it safe for a shared Clean template to include the
stage for devices that do not have recovery-image data.

YAML Example
------------

The following Clean YAML uses one image for the normal install workflow and a
different, explicitly configured image for device recovery:

.. code-block:: yaml
    :linenos:

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1]

    devices:
        PE1:
            # Used by ImageHandler and normal install-image stages.
            images:
            - /srv/images/releases/system-image.bin

            connect:

            recovery_image:
                # Canonical recovery-server path, not a temporary copy path.
                images:
                - /srv/recovery/builds/recovery-image.bin
                # Stable local path used by later device recovery.
                golden_image:
                - bootflash:golden_image.bin
                recovery_server: recovery-server
                protocol: https
                recovery_server_port: 8443
                verify_size: true
                verify_md5: false
                timeout: 1800
                copy_attempts: 2
                copy_attempts_sleep: 30
                protected_files:
                - startup-config
                min_free_space_percent: 5

            copy_to_device:
                destination:
                    directory: 'bootflash:'

            order:
            - connect
            - recovery_image
            - copy_to_device

The referenced testbed can define the recovery server as follows. Because
``/srv/recovery`` is the server root, the stage retains the canonical source
for validation and passes ``/builds/recovery-image.bin`` to the transfer
service.

.. code-block:: yaml

    testbed:
        servers:
            recovery-server:
                address: 192.0.2.10
                path: /srv/recovery
                services:
                    https:
                        type: file_transfer
                        protocol: https
                        port: 8443
                        order: 10

After the stage passes, later recovery logic can read the following runtime
value without the Clean YAML having to duplicate it under ``device_recovery``:

.. code-block:: yaml

    device_recovery:
        golden_image:
        - bootflash:golden_image.bin

Recovery Images and Image Management
------------------------------------

The top-level device ``images`` key belongs to Clean Image Management and its
platform-specific ImageHandler. ImageHandler passes those images between the
normal copy, boot-variable, install, reload, and running-image verification
stages. It may also replace image values configured directly under those
stages, depending on ``image_management.override_stage_images``.

The ``recovery_image`` stage is deliberately independent:

* ImageHandler does not populate or replace ``recovery_image.images``.
* The stage does not fall back to top-level ``images``.
* ``image_management.override_stage_images`` does not change this behavior.
* The stage does not write its local golden image back to top-level ``images``.

Therefore, supply recovery sources under ``recovery_image.images`` explicitly,
or use tooling that generates that stage argument. If the same file is used
for both installation and recovery, list the canonical source in both places;
the two keys still have different ownership and lifecycle.

Server and Protocol Selection
-----------------------------

``protocol`` defaults to ``https``. ``recovery_server`` may identify a testbed
server by name or provide its address directly.

When ``recovery_server`` is omitted, the stage examines testbed servers for a
``file_transfer`` service whose protocol matches ``protocol``. Services with a
numeric ``order`` take precedence; otherwise, testbed server and service order
is preserved. The stage fails with a clear message when no matching service is
available.

The port is resolved in this order:

#. ``recovery_server_port`` in the stage.
#. The selected matching file-transfer service's ``port``.
#. The standard port for the selected protocol.

The configured server ``path`` is treated as its transfer root and is removed
from canonical image paths only when preparing server-relative copy and
metadata requests. Address, credentials, proxy, and other transfer behavior
remain owned by pyATS FileUtils and the platform copy implementation.

Size metadata can be read over FTP, HTTP, HTTPS, or SFTP. When URL metadata is
unavailable, the stage can fall back to an SSH connection to the configured
recovery server. The selected copy protocol does not change during that
fallback.

Verification and Copy Decisions
-------------------------------

By default, the stage checks only whether the expected filename exists at the
local target. Use one or both verification options when an existing file must
also be compared with the source:

``verify_size`` (default: ``false``)
    Compare the source and target byte counts before deciding whether to copy,
    and verify the size again after a copy. This is normally much faster than
    MD5. It detects a changed image only when its size also changes; two
    different images with the same byte count are treated as equal.

``verify_md5`` (default: ``false``)
    Compare source and target MD5 digests before deciding whether to copy, and
    verify the digest again after a copy. This is an exact content comparison,
    but calculating a digest for a large image can take considerably longer.

Both options require ``recovery_image.images`` because the stage needs a
remote source from which to obtain the expected metadata. When both are true,
the existing target must satisfy both checks. A target that is absent or fails
an enabled check is copied; a target that passes is skipped.

For a remote source, size verification requires either supported URL metadata
or SSH access to the recovery server. MD5 verification requires the source to
be readable by the Clean runner or through an SSH-accessible recovery server.

Disk-Space Cleanup
------------------

Automatic cleanup is performed only when a copy is required and
``verify_size: true`` has supplied the number of bytes needed. Before copying,
the stage asks the platform ``free_up_disk_space`` API to create enough space
on each target filesystem.

``protected_files`` (default: none)
    Additional filenames or patterns that cleanup must preserve. Clean history
    references to golden configurations and golden images, along with the
    other recovery targets in this stage, are also protected where applicable.

``skip_deletion`` (default: ``false``)
    Prevent cleanup from deleting files. The stage still checks the available
    space and fails if the image cannot fit.

``min_free_space_percent`` (default: none)
    Ask cleanup to retain at least this percentage of the filesystem as free
    space in addition to the space required for the recovery image.

When ``verify_size`` is false, the stage cannot calculate the required space,
so automatic cleanup is skipped and the copy operation reports any
insufficient-space error.

Publishing to Device Recovery
-----------------------------

After every local target passes verification, the stage sets:

.. code-block:: python

    device.clean.setdefault("device_recovery", {})["golden_image"] = [
        "bootflash:golden_image.bin"
    ]

This preserves other ``device_recovery`` settings and exposes the local path,
not the remote canonical source, to later recovery operations. Set
``update_device_recovery: false`` to verify or copy the image without publishing
the paths.

Stage Arguments
---------------

``images`` (list, optional)
    Canonical remote recovery-image paths. Paired positionally with
    ``golden_image``.

``golden_image`` (string or list, optional)
    Stable local device paths for recovery. Existing
    ``device_recovery.golden_image`` or platform defaults are used when this is
    omitted, as described in `Source and Target Paths`_.

``recovery_server`` (string, optional)
    Testbed server name or server address. A matching server is selected from
    the testbed when omitted.

``recovery_server_port`` (integer, optional)
    File-transfer service port. The selected service or protocol default is
    used when omitted.

``protocol`` (string, optional)
    Copy protocol. Defaults to ``https``.

``destination`` (mapping, optional)
    May contain ``directory``, ``standby_directory``, and a list named
    ``stack_directory``.

``connection_alias`` (string, optional)
    Device connection alias used by the stage. Defaults to ``default``.

``vrf`` (string, optional)
    VRF passed to the device copy API. Defaults to an empty string.

``timeout`` (integer, optional)
    Transfer and remote-metadata timeout in seconds. Defaults to ``300``.

``copy_attempts`` (integer, optional)
    Number of copy attempts. Defaults to ``1``.

``copy_attempts_sleep`` (integer, optional)
    Seconds between copy attempts. Defaults to ``30``.

``verify_size`` (boolean, optional)
    Enable source-to-target size verification and disk-space calculation.
    Defaults to ``false``.

``verify_md5`` (boolean, optional)
    Enable source-to-target MD5 verification. Defaults to ``false``.

``protected_files`` (list, optional)
    Additional filenames or patterns that disk cleanup must preserve.

``skip_deletion`` (boolean, optional)
    Disable deletion during disk-space cleanup. Defaults to ``false``.

``min_free_space_percent`` (integer, optional)
    Minimum free-space percentage requested during cleanup.

``prompt_recovery`` (boolean, optional)
    Enable copy prompt recovery in the platform copy API. Defaults to
    ``false``.

``update_device_recovery`` (boolean, optional)
    Publish verified local paths to ``device_recovery.golden_image``. Defaults
    to ``true``.
