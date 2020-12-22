October 2018
============

October 10th - Genie v3.1.0
---------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 3.1.0                         |
+-----------------------------------+-------------------------------+

+-----------------------------------+-------------------------------+
| Module (Libs)                     | Versions                      |
+===================================+===============================+
| ``genie.libs.conf``               | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 3.1.0                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 3.1.0                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie
    pip install --upgrade genie.conf
    pip install --upgrade genie.examples
    pip install --upgrade genie.harness
    pip install --upgrade genie.ops
    pip install --upgrade genie.utils
    pip install --upgrade genie.abstract
    pip install --upgrade genie.telemetry
    pip install --upgrade genie.parsergen
    pip install --upgrade genie.predcore
    pip install --upgrade genie.metaparser
    pip install --upgrade genie.libs.conf
    pip install --upgrade genie.libs.ops
    pip install --upgrade genie.libs.sdk
    pip install --upgrade genie.libs.robot
    pip install --upgrade genie.libs.filetransferutils
    pip install --upgrade genie.libs.parser
    pip install --upgrade genie.libs.telemetry

Features:
^^^^^^^^^

**Genie.Harness**

* Added Summary table to all CommonSetup/CommonCleanup sections (log summary)
* Genie now supports Pcall, do actions in parallel on the devices (saving run time)
* Added a fix for running the same processor with different arguments
* Timeout fix (Always run triggers for up to maxtime and when time is up trigger will fail)
* `common_setup` and `common_cleanup` can now have processors added dynamically with the subsection datafile
* `Trigger` section can now have processors added dynamically with the trigger datafile
* Fixed bug with adding the same processor with the different arguments
* Datafiles are now smart. Trigger, verification, subsection and PTS datafile will find their corresponding files if not provided
* Triggers and verification will only execute the one requested with uids or groups, old behavior was to run all triggers in datafile, unless uids/groups provided
* Added 'rest' to context list
* Genie harness now supports pyATS connection pool feature
* Added check after applying configurations to device to make sure device is alive
* Disabled 'show version' execution after connection to device
* Added an enhancement to terminate run upon failure of any CommonSetup section
* Fixed the corner case of skipping config section and try to use device.filetransfer later in the run either in ha actions or telemetry
* Handled the case when user provide filetransfer_protocol and forgot to add server info to the testbed yaml file
* Enhancement of the log messages 
* Improvement of the log for Common Setup and Common Cleanup
* Fix an issue with config_snapshot 
* Providing custom/abstraction is now optional. Only needed if anything else
  than OS
* All Triggers argument can now be provided in the trigger datafile, instead of
  being learn dynamically

**Genie.Conf**

* Removal of interfaces.find_links, as interfaces only have 1 link. (Following pyATS model)

**Genie.Ops**

* Enhancement for `Maker`, can now provide `attributes` longer than the smallest dest of the ops

**Genie.Libs.Robot**

* Changelog can be checked :robotchangelog:`here <OCTOBER>`

**Genie.Libs.Ops**

* Changelog can be checked :opschangelog:`here <OCTOBER>`

**Genie.Libs.Conf**

* Changelog can be checked :confchangelog:`here <OCTOBER>`

**Genie.Libs.Sdk**

* Changelog can be checked :sdkchangelog:`here <OCTOBER>`

**Genie.Telemetry**

* Data wrapping, syntax stacking, syntax formatting
* Added supported os and version to genietelemetry
* Testbed yaml custom abstraction check

**Genie.Libs.Parser**

* Changelog can be checked :parserchangelog:`here <OCTOBER>`

**Genie.Libs.FileTransferUtils**

* Enhanced setup.py file and the unittests with pyAts backward compatibility.


October 25th
------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.ops``                     | 3.1.1                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.ops

Features:
^^^^^^^^^

* Fixed Genie objects Conf/Ops mapping (Converting learnt Ops dictionary to Conf Object)
