.. _health:

pyATS Health Check
==================
By using pyATS Health Check, it is possible to check the CPU load, memory usage, detection of specific log messages, whether or not a process-level core file was generated on crash, and whether or not IOS XE crashinfo files exist on the device filesystem.

pyATS Health Check currently supports the following 5 checks by default.

.. list-table::
   :header-rows: 1

   * - health check
     - description
   * - cpu
     - CPU load check. Compares the higher of ``show processes cpu sorted`` and ``show processes cpu platform sorted`` against a threshold (default 90%). Uses the 5-second average (``five_sec_cpu``).
   * - memory
     - Memory usage check. First checks total processor-pool usage against a threshold (default 90%). Only runs the full per-process parse when the threshold is exceeded, keeping overhead low.
   * - logging
     - Keyword search in ``show logging`` output. Default keywords: ``traceback``, ``Traceback``, ``TRACEBACK``. Tracks log count across testcases so only *new* messages since the last check are reported. Use ``--health-clear-logging`` to clear the log buffer before each check.
   * - core
     - Checks for process-level ``.core.gz`` / ``.tar.gz`` files in ``bootflash:/core/`` (and ``harddisk:/core/``). Supports HA (also checks ``stby-bootflash:/core/``) and stack (checks ``flash-{id}:/core/``). Use ``--health-remote-device`` to copy files to a remote server. Files are only deleted from the device after a successful copy.
   * - crashinfo
     - Checks for IOS XE crashinfo files in ``crashinfo:`` (written on full OS crash/reload). **IOS XE only.** Supports HA (also checks ``stby-crashinfo:``) and stack (checks ``crashinfo-{id}:``). Copies discovered files automatically to ``<runinfo>/crashinfo/`` — no remote server needed. Optionally deletes files from the device after copy.

.. note:

    `cpu`, `memory`, `logging`, `core` and `crashinfo` checks are pre-defined in /path/to/genielibs/pkgs/health-pkg/src/genie/libs/health/health_yamls/pyats_health.yaml. `--health-checks` uses this default pyats health file.

Using pyATS Health Check is very easy. Just list the above heath check names by adding `--health-checks` to the current pyats command.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core crashinfo

If you want to check only specific checks, list only those names after `--health-checks`. **The pyATS Health Check specified by `--health-checks` runs as a post-processor after each test case.**

For ``core``, only detection occurs by default. To copy the file to a remote server for TAC analysis or archival, provide ``--health-remote-device``. Files are deleted from the device only after a successful copy.

For ``crashinfo``, files are copied automatically to the ``crashinfo/`` subdirectory of the pyATS run directory (no remote server needed). The check also establishes a pre-run baseline so only files that appear *during* the run are flagged as failures.

The command example in that case is as follows.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-remote-device name:myserver path:/tmp/ protocol:http --health-mgmt-vrf iosxe:None

Note that in order to run the above example you need to have the server `myserver` in testbed yaml as below.

.. code-block:: yaml

    testbed:
      name: general_xe_xr_nx
      servers:
        myserver:
          dynamic: true
          protocol: http
          subnet: 192.168.255.0/24
          path: /tmp
          credentials:
            default:
              username: pyats
              password: "<password>"

.. note::

    The above example uses `Embedded pyATS File Transfer Server <https://pubhub.devnetcloud.com/media/pyats/docs/utilities/file_transfer_server.html>`_.

You can find more examples in our `Github repo <https://github.com/CiscoTestAutomation/examples/tree/master/health>`_. Any contributions for pyATS Health Check examples are encouraged!

FAQ
---

**1. What kind of protocols are supported for core file transfer? And how to adjust to my remote server info?**

`http`, `scp`, `tftp` and `ftp` are supported. It depends on what is supported by `Multiprotocol File Transfer Utilities <https://pubhub.devnetcloud.com/media/pyats/docs/utilities/file_transfer_utilities.html>`_. 

If VRF for transfer needs to be changed from common default ones (`Mgmt-intf`, `management`), please change via `--health-mgmt-vrf` argument. for default VRF, needs to specify `None` like `iosxe:None`.

example when using tftp and vrf `mgmt` for both iosxe and nxos

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core crashinfo --health-remote-device name:myserver path:/tmp/ protocol:scp --health-mgmt-vrf iosxe:mgmt nxos:mgmt

**2. How to change threshold for cpu load/memory usage?**

It can be done via `--health-threshold` argument. The same threshold applies to both CPU and memory checks independently.

example when specifying thresholds, cpu 75% and memory 80%

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core crashinfo --health-threshold cpu:75 memory:80

**3. How can I change which logging keywords I want to detect?**

By default, `logging` check detects only `traceback`, `Traceback` and `TRACEBACK`. The keywords can be overwritten via `--health-show-logging-keywords`.

example when changing to `Crash` and `CRASH` for both iosxr and nxos.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core crashinfo --health-show-logging-keywords "iosxr:['Crash', 'CRASH']" "nxos:['Crash', 'CRASH']"

.. note::

    Use ``--health-clear-logging`` (flag, no value needed) to clear the device log buffer before each check. This prevents previously seen messages from being re-counted.

**4. I want to change the location of where core files are searched for**

by default, it's pre-defined for each platform (iosxe, iosxr, nxos). If you want to look somewhere else, the location can be overwritten via `--health-core-default-dir`.

example to change to `harddisk0:/core` for iosxe.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core crashinfo --health-core-default-dir "iosxe:['harddisk0:/core']"

.. note::

    ``--health-core-default-dir`` applies only to the ``core`` check. For HA devices the standby filesystem (``stby-bootflash:/core/``) is checked automatically. For stack devices ``flash-{switch_id}:/core/`` is checked per member.

**5. How to run pyATS Health check against only certain devices?**

All checks will run against all connected devices in testbed yaml by default. To run checks against only specific devices, please use `--health-devices`.

example to run against only `R1_xe` device.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core crashinfo --health-devices R1_xe

**6. Is it possible to send a webex notification?**

Yes. There is `--health-webex` argument to send a webex notification. The webex notification will be sent out only when health checks fail.
Webex token and space id or email need to be given via pyats.conf or webex arguments `--webex-token`, `--webex-space`, `--webex-email`.

example to send Webex notification to webex space by using webex arguments

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core crashinfo --health-notify-webex --webex-token <webex token> --webex-space <webex space id>

.. note::

    ``--health-webex`` is deprecated. Use ``--health-notify-webex`` instead.

.. note::

    Webex notification is done by pyATS Webex Plugin in `pyats.contrib` package. Please refer to `Webex Plugin README <https://github.com/CiscoTestAutomation/pyats.contrib/tree/master/src/pyats/contrib/plugins/webex_plugin>`_ for more detail.

**7. How do I tune the crashinfo check? (default directory, filename filter, delete behaviour)**

The ``crashinfo`` check supports three tunable arguments via a custom health YAML (``--health-file``):

* ``default_dir`` — filesystem(s) to inspect. Default: ``['crashinfo:']``. For non-standard setups (e.g. ``flash:/crashinfo/``) pass a list. HA and stack overrides are applied automatically.
* ``keyword`` — filename substrings to match. Default: ``['crashinfo']``. Matches both Cat9K style (``<host>_crashinfo_1_RP_...``) and ASR1K style (``crashinfo_RP_...tar.gz``).
* ``delete_crashinfo`` — delete files from the device after a successful copy. Default: ``True``. Set to ``False`` to keep files on device.

example custom health YAML with non-default crashinfo directory and delete disabled:

.. code-block:: yaml

    pyats_health_processors:
      source:
        pkg: genie.libs.health
        class: health.Health
      test_sections:
        - crashinfo:
            - api:
                device: my_device
                function: health_crashinfo
                arguments:
                  default_dir:
                    - flash:/crashinfo/
                  delete_crashinfo: false
                include:
                  - value_operator('num_of_crashfiles', '==', 0)
                processor: post

++++

The above are all the easy ways to use pyATS Health Check. Also, please be aware that each of the above arguments can be used in combination. If you want to use custom pyATS Health Checks, please check the design chapter.

.. toctree::
   :maxdepth: 2

   health_design/design
   health_usage/usage
