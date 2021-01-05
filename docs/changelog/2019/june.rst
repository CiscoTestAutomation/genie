June 2019
=========

June 25th- Genie v19.6.0
------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.6.0                        |
+-----------------------------------+-------------------------------+
| ``unicon``                        | 19.6.0                        |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.examples genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

**Genie**

* genie parse --raw - Can be used to collect device output without parsing them
* Genie Cli does not modify the state of the device anymore


**Infrastructure**

* Support for duplicate triggers
* New Processors
* run_genie_sdk new arguments, support for trigger and verification datafile
* Ops Schema
* New get_exclude API for OPS and Parser
* New Import for Genie testbed - from genie import testbed


**Genie.Libs.Parser**

* Over 40 new IOSXE, IOS & NXOS Parsers!
    * IOSXE: 12
    * IOS: 2
    * NXOS: 22
    * ASA: 7
* Changelog can be checked :parserchangelog19:`here <JUNE>`


**Genie.Libs.Ops**

* Genie learn beacame more time efficient!
    * Now it can learn custom arguments (Ex:Ethernet1/1/1)
    * It can learn for specific parsers
* Changelog can be checked :opschangelog19:`here <JUNE>`


**Genie.Libs.Sdk**

* Updates on HA/Reload triggers!
* New NXOS TriggerMplsEncsp Trigger!
* Changelog can be checked :sdkchangelog19:`here <JUNE>`


**Genie.Trafficgen**

* Get stats from "Flow Statistics" view
* Generate traffic streams after config change
* Enable/disable "flow tracking" filter per traffic stream
* Export Ixia QuickTest PDF report
* Generate Ixia QuickTest PDF report
* Execute Ixia QuickTest on IxNetwork
* Get entire traffic configuration attributes
* Get traffic stream attributes
* Get flow group attributes
* Get quick flow group attributes
* Configure packet size per traffic stream
* Configure packet rate per flow group
* Configure packet rate per traffic stream
* Configure layer2 bit rate per flow group
* Configure layer2 bit rate per traffic stream
* Configure line rate per flow group
* Configure line rate per traffic stream
* Bugfix pull multi-page stats for custom "GENIE" view
* Check traffic loss per flow group
* Start/stop traffic per flow group
* Start/stop traffic per Quick Flow Group
* Flags to add/remove columns in custom "GENIE" view
* Enhance check traffic to check only L3L3 traffic streams
* Enhance check_traffic_loss to iterate internally


**Unicon**

* iosxr plugin

    * Now handling "Enter secret:" and "Enter secret again:" correctly.
    * iosxr/spitfire regex fixes, added init config commands with timeout.
    * spitfire plugin now accepts username and enable password.

* nxos plugin

    * Added guestshell service.
    * Config lock fix
    * add utils method retry_state_machine_go_to
    * add arguments in generic Configure and HaConfigure service for retrying go_to config sate
    * add retry go_to config sate in nxos Reload and HANxosReloadService
    * fix nxos configuration locked problem after reload
    * add nxos n9k plugin whose reload service supports image_to_boot argument

* generic plugin

    * Fix reload service that was hanging when mgmt connection was attempted.
    * Updated execute() service to allow override of default service dialogs by
      passing `service_dialog`
    * improve ping extd_ping judgement and fix endless ping dialog on erroneous
      value
    * Copy service now correctly detects "Could not resolve hostname" as an error

* asa plugin

    * update to handle --more-- prompt.

* ios plugin

    * add iol plugin including switchover support for dIOL devices.

* core

    * modifed `unicon_record`, `unicon_replay`, `unicon_speed` environment
      variables to `UNICON_RECORD`, `UNICON_REPLAY`, and `UNICON_REPLAY_SPEED`.
    * Disconnect timers may now be updated via Settings object
    * Dialogs are now documented using autogenerated documentation for connect()
      and execute() services.
    * Mock device updates:
      Updated code that replaces the string ESC in prompt with \1xb.
      Print the command that was deemed invalid.
      Added ASA mock device to test more prompt handling.
    * The 'init_exec_commands' and 'init_config_commands' options can now be
      passed via the connection block in the yaml topology file.
    * use SimpleDialogProcessor instead of AlarmBasedDialogProcessor

* Remove hard ``asyncssh`` package dependency.

    * Now users requiring SSH mocks must manually install the ``asyncssh`` package.