.. _clean_doc_health:

Clean Health
============

Clean runs pyATS Health checks around its stages using the same Health
processors as test scripts. Pre actions run before the Clean stage. Post
actions run after the stage and, when configured, after device recovery.
Custom Health datafiles retain their configured pre/post phases.
Health results appear in the Clean report and in a per-device
``clean_health/<device>/health_results.json`` file in the run archive.
The archive also contains ``pyats_clean_health.yaml``. Its ``devices`` mapping
preserves each device's prepared Health source, settings, reconnect options,
sections, and configured filters, including the translated Clean selectors.
Each Clean worker scopes the Health ``devices`` settings to its own device,
including when a custom datafile lists multiple devices. A stage's existing
processors continue to run alongside Health and device recovery.

Health is disabled by default. A device's ``health_checks`` configuration
selects built-in checks or a custom Health datafile. Health failures are
included in the Clean stage result. Later stages follow the Clean
configuration's failure handling. Reports show the Health checks that ran;
empty processor phases and setup helpers such as ``get_testcase_name`` are
hidden.

Built-in checks
---------------

The built-in checks are ``cpu``, ``memory``, ``logging``, ``core``, and
``crashinfo``. Clean calls device APIs through abstraction and skips unsupported
APIs. CPU, memory, and logging availability follows the
platform's pyATS Health implementation. Verified artifact collection is
available through the IOS XE core and crashinfo Health APIs, including system
reports. Existing core checks on other platforms run without copying or
deleting files when their APIs do not provide verified collection.

.. code-block:: yaml

    cleaners:
      PyatsDeviceClean:
        module: genie.libs.clean
        devices: [PE1]

    devices:
      PE1:
        health_checks:
          checks: [cpu, memory, logging, core, crashinfo]
          health_settings:
            threshold:
              cpu: 90
              memory: 90
            show_logging_keywords:
              iosxe: [traceback, Traceback, TRACEBACK]
            clear_logging: false
        connect:
        order:
          - connect

``checks`` also accepts a mapping of check names to boolean values.
``health_settings`` uses the settings from the pyATS Health datafile, including
thresholds, logging keywords, and core directories. For example:

.. code-block:: yaml

    devices:
      PE1:
        health_checks:
          checks:
            core: true
            crashinfo: true
          health_settings:
            core_default_dir:
              iosxe: [flash:/core/]
            crashinfo_default_dir:
              iosxe: ["crashinfo:"]

Artifact collection
-------------------

Each filesystem's first successful scan records the existing files as its
baseline. These files are left on the device. A filesystem that becomes
accessible later receives its own baseline; a failed scan does not establish
an empty baseline.

Verified collection uses HTTP and the proxy configured in the device testbed.
New artifacts found after the baseline are copied into per-device directories
under ``clean_health`` in the run archive. Each source path has a separate
archive directory, including when active, standby, or stack filesystems contain
identical filenames. Clean deletes a source file only after the copy API
confirms a verified transfer. Each copied file's ``archive_path`` in the Health
results identifies its destination file, including the filename selected by
the transfer API. Failed scans and transfers leave source files in
place; later checks retry unsuccessful collections. Setting
``health_settings.delete_files: false`` retains source files after verified
copies as well.

Custom Health datafiles
-----------------------

``health_file`` loads a pyATS Health datafile. Its actions, settings, and
``processor: pre`` or ``processor: post`` timing are preserved. Test-script
section types are translated to Clean selectors as described below.
``health_settings`` overrides settings from that file. An optional ``checks``
list selects named sections from it.

.. code-block:: yaml

    devices:
      PE1:
        health_checks:
          health_file: health.yaml
        connect:
        order:
          - connect

For example, ``health.yaml`` can execute an additional command after selected
Clean stages:

.. code-block:: yaml

    pyats_health_processors:
      source:
        pkg: genie.libs.health
        class: health.Health
      test_sections:
        - version:
            - execute:
                device: PE1
                command: show version
                health_tc_sections: ["Connect.*"]
                processor: post

Stage filters
-------------

``health_tc_sections``, ``health_tc_uids``, and ``health_tc_groups`` use the
pyATS Health filtering rules. Stage report names and UIDs accept regular expressions.
``health_tc_sections`` also accepts ``type:TestSection`` for Clean stages.
In both built-in and custom datafiles, ``type:TestCase`` is translated to
``type:TestSection``, while ``type:CommonSetup`` selects only the ``Connect``
stage, including repeated Connect stages. Other section expressions are
preserved. These translations are logged and saved in
``pyats_clean_health.yaml``.

.. code-block:: yaml

    devices:
      PE1:
        health_checks:
          checks: [cpu, memory]
          health_tc_sections: ["Connect.*", "ConfigureManagement.*"]
          health_tc_uids: ["CleanTestcase"]

To disable Health explicitly for a device, set ``health_checks: false``.
