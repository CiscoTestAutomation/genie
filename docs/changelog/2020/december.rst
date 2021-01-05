December 2020
=============

December 15th - Genie v20.12
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.12                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.12                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

Note that this will leave older v19.12 packages around in pip list, but it will
not impact anything (visual only).  An update command can be used to clean up
these packages

.. code-block:: bash

   pyats version update

Features:
^^^^^^^^^

* End of Support for genie.telemetry starting January - migrate to `pyATS Health Check
<https://pubhub.devnetcloud.com/media/genie-docs/docs/health/index.html>`_.
* End of Support for Python3.5 starting January - upgrade to Python3.6/3.7/3.8

**genie**

* Enhanced mapping datafile to pass netconf_poolsize as argument for NetConf connections.
* Enhancement to Standalone to support non UUT testbed
* Updated genie device error pattern to propagate into device settings 
* Enhanced mapping datafile to pass netconf_poolsize as argument for NetConf connections.
* Fixed API abstraction for platform specific APIs
* Fixed an issue using run_genie_sdk with only a/b connections defined for a device

--------

**genie.libs.clean**

* CLEAN
    * At The End Of Clean All Connection Will Be Destroyed

* COM
    * Added Power_Cycle Stage
    * Modified Apply_Configuration
        * To Add Argument 'Skip_Copy_Run_Start'

* IOSXE
    * Added Grub Menu Booting During Device Recovery

* JUNOS
    * Added Get_Task_Memory_Information
    * Added Verify_Chassis_Routing_Engine
    * Added Verify_Chassis_Environment_Status
    * Added Verify_Chassis_Alarm_No_Output
    * Added Verify_Chassis_Alarm_Output
    * Added Verify_Chassis_Slot_Missing
    * Added Verify_Log_Multiple_Attributes
    * Added Verify_No_Log_Output
    * Added Get_Chassis_Cpu_Util_Alternative
    * Added Verify_Traffic_Statistics_Data

* NXOS
    * Aci
        * Added Fabric_Upgrade Stage
        * Added Fabric_Clean Stage
        * Added Node_Registration Stage
    * Added Support For N3K
        * Support N3K For Genie Clean

--------

**genie.libs.health**

* PYATS HEALTH CHECK
    * Modified Logic To Run Post-Processor With Exception In Section
    * Fixed Processor Key Issue In Health Yaml
    * Fixed Logic To Handle Health Args In Health Yaml

--------

**genie.libs.conf**

* No change

--------

**genie.libs.filetransferutils**

* New FTP/TFTP dynamic FileServer for running on execution host
* Improved file copying for IOS/IOSXE/IOSXR/NXOS to include FTP server
  credentials
* File copying configuration for IOSE/IOSXE/IOSXR/NXOS devices that have
  default_gateway and file_transfer_interface defined as custom values

--------

**genie.libs.ops**

* IOSXE
    * Added Platform Ops For C8200

--------

**genie.libs.parser**

* 62 new IOSXE, IOS, NXOS, IOSXE and Junos Parsers!
* Grand total of 2740 Parsers
* Changelog can be checked :parserchangelog20:`here <december>`

--------

**genie.libs.robot**

* No change

--------

**genie.libs.sdk**

* 79 new apis to use on your devices!
* Grand total of 1101 APIs
* Changelog can be checked :sdkchangelog20:`here <december>`
--------

**genie.telemetry**

* No change

--------

**genie.trafficgen**

* ixianative.py
    * Modified create_traffic_streams_table:
        * enhanced code so it could work with different config types

--------

**genie.utils**

* Removed python sorted method in genie diff in instances where tuple could have different types



