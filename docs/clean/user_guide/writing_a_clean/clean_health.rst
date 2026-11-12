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
        health_checks:
          delete_files: false
        connect:
        order:
          - connect

To disable the checks for a device, set ``health_checks`` to ``false``:

.. code-block:: yaml

    devices:
      PE1:
        health_checks: false
        connect:
        order:
          - connect

Select artifact types and configure core directories by operating system with
``checks`` and ``core_default_dir``. A directory override replaces the default
core directories for the matching operating system. Crashinfo directories are
unaffected.

.. code-block:: yaml

    devices:
      PE1:
        health_checks:
          checks:
            core: true
            crashinfo: false
          core_default_dir:
            iosxe:
              - bootflash:/core/
        connect:
        order:
          - connect

Use ``health_tc_sections`` to select stage names or section types, and
``health_tc_uids`` to select a stage or its parent testcase by UID. Names and
UIDs accept regular expressions. When both filters are set, a stage must match
both. Baselines are still taken before stages; new files created in a stage
outside the filter can be collected after a later matching stage.

.. code-block:: yaml

    devices:
      PE1:
        health_checks:
          health_tc_sections:
            - "connect.*"
          health_tc_uids:
            - "CleanTestcase"
        connect:
        order:
          - connect
