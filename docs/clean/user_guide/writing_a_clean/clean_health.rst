.. _clean_doc_health:

Clean Health
============

Clean checks for new crash artifacts after each clean stage, including after
device recovery. The current implementation supports IOS XE crashinfo, system
reports, and core files, including stack member and standby filesystems.
Devices without a supported implementation are skipped.

For each accessible filesystem, Clean records the files present when it first
scans that filesystem. Files already present at that time are left on the
device. This includes files created before the first successful connection or
during the stage that first makes the filesystem accessible.

New files found after the baseline are copied to the ``clean_health`` directory
in the job's runinfo archive. By default, Clean deletes a device file only after
its copy has been verified. If a scan or transfer fails, the file is left on
the device and the clean stage result is unchanged.

Configuration
-------------

Clean health is enabled by default. To keep files on the device after copying
them, set ``delete_files`` to ``false`` for the device in the Clean YAML file:

.. code-block:: yaml

    cleaners:
      PyatsDeviceClean:
        module: genie.libs.clean
        devices: [PE1]

    devices:
      PE1:
        clean_health:
          delete_files: false
        connect:
        order:
          - connect

To disable the checks for a device, set ``clean_health`` to ``false``:

.. code-block:: yaml

    devices:
      PE1:
        clean_health: false
        connect:
        order:
          - connect
