May 2019
========

May 27th- Genie v19.5.0
-----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.5.0                        |
+-----------------------------------+-------------------------------+
| ``unicon``                        | 19.5.0                        |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.examples genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

**Genie.Harness**

* Local processor overwrite Global processor argument
* Adding error patterns to Genie infra (device actions)
* New processors "save_running_config" and "restore_running_config" added for XE/NX/XR
* New processors "start_traffic" and "stop_traffic" added
* Per-stream traffic check added to "initialize_traffic" subsection and "check_traffic_loss" processor
* Enhance traffic loss checks in "initialize_traffic" subsection and "check_traffic_loss" processor
* Enhance traffic profile comparison checks in "profile_traffic" subsection and "compare_traffic_profile" processor
* Uids now set the Trigger order
* Uids now support list instead of Logic syntax
* Number of element to perform action on can now be modified with the trigger datafile


**Genie.Utils**

* Function Question mark now support state parameters, default is enable
* "unpickle_stream_data" to read Ixia yaml with outage info added


**Genie.Conf**

* Genie infra - Enhancement for device.learn to accept attributes


**Genie.Libs.Parser**

* Over 50 new IOSXE, NXOS & IOSXR Parsers!
    * IOSXE: 13
    * IOSXR: 9
    * NXOS: 36
* Changelog can be checked :parserchangelog19:`here <MAY>`


**Genie.Libs.Ops**

New Genie Ops structures;

* IOSXR
    * `RIP`
    * `MLD`

* IOSXE
    * `MSDP`

* NXOS
    * `LLDP`

* Changelog can be checked :opschangelog19:`here <MAY>`


**Genie.Libs.Sdk**

* Supported trigger count during execution!
* New IOSXE Triggers and enhancements!
* Changelog can be checked :sdkchangelog19:`here <MAY>`


**Parsergen**

* Enhanced package as per the support needed for python versions 3.6 & 3.7!


**Genie.Libs.Filetransferutils**

* Removed old pyATS plugin entry points!


**Genie.Trafficgen**

* Start and stop traffic per stream support added
* Per stream traffic loss check support added for genie common_setup and processors
* Expand traffic loss/outage checking for outage, loss % and rate loss
* Expand traffic profile comaprison checks for frame rate and loss %
* Add support for automatically enabling "traffic item" in flow groups (if disabled in user config)
* Add documentation for new features, traffic checks and profile comaprison


**Unicon**

* Enhance following iosxr patterns to support different versions of iosxr:
  run_prompt, admin_prompt, admin_conf_prompt, admin_run_prompt
* Update user guide to remove prompt argument from bash_console service
* Added ASA plugin error pattern.
* Fixed admin_attach_console on iosxr plugin, it now exits correctly.
* The generic switchover service now respects the timeout parameter.
* Enhance RawSpawn expect, add argument "log_timeout" to control
  whether log Timeout info
* Introducing iosxe/sdwan plugin with config commit support.
* Fix the problem that iosxr admin_attach_console does not exit correctly.
* Added retries option to the generic HA config service.

May 3rd
-------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.5.1                        |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

Features
^^^^^^^^

* Simplified loading the Testbed yaml file!

.. code-block:: bash

    from genie import testbed
    genie_tb = testbed.load('testbed.yaml')