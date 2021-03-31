March 2021
==========

March 30h - Genie v21.3
-----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.3                          |
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

**genie**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* testbed conversion
    * Fixed bug with non pyATS/Genie interface classes
    * Fixed bug with non pyATS/Genie device classes

* Fixed trafficgen argument
    * Fixed bug that `--tgn-traffic-streams-data` was not properly handled from CLI

* Genie Conf Interface
    * Added `alias` to Genie Conf Interface object

* Device settings in topology
    * Moved Genie default error pattern implementation to Unicon
    * Moved device custom timeout attributes implementation to Unicon


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* Genie schemaengine
    * Add ListOf to schema validation

* Genie make_json
    * Sort tokens



**genie.libs.clean**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* genie.conf
    * Modified Interface class, updated ipv6 type to ipv6_or_list_of_ipv6

* IOSXE
    * Modified clean stage 'install_image' directory lookup

* Junos
    * Modified verify_chassis_environment_component_present
        * Enhanced code to return proper result
    * Modified verify_log_exists
        * Enhanced code to return correct response

* UTILS
    * Modified validate_clean to do linting on the clean yaml


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* IOSXE
    * Modified apply_configuration clean stage
        * Added option to copy config directly to startup
    * Added ping API

* IOS
    * Added delete_local_file API
    * Added get_config_from_file API
    * Added start_packet_capture API
    * Added stop_packet_capture API
    * Added export_packet_capture API
    * Added clear_packet_buffer API
    * Added ping_interface_success_rate API
    * Added change_hostname API
    * Added save_running_config_configuration API
    * Added set_clock API
    * Added scp API
    * Added delete_files API
    * Added verity_ping API
    * Added get_md5_hash_of_file
    * Added ping API

* IOSXR
    * Added ping API

* NXOS
    * Added ping API


**genie.libs.conf**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* NXOS
    * Added in bgp conf
        * disable-peer-as-check
    * Added in bgp conf
        * nbr_af_rewrite_mvpn_rt_asn


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* Utils
    * Changed "from fractions import gcd" to "from math import gcd" due to deprecation in Python 3.9

* Device object
    * Removed 'role' attribute

* NXOS
    * Modified Interface Conf
        * Fixed a bug which unconfig doesn't work with attributes



**genie.libs.sdk**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* JUNOS
    * Modified Get_Firewall_Counter
    * Removed Duplicate Verify_Bgp_Peer_Address
    * Modified Get_Interface_Snmp_Index
        * Removed .Split('.')[0] From Command Parsing
    * Modified Verify_File_Details_Exists
    * Modified Verify_Services_Accounting_Flow
    * Modified Get_Route_Table_First_Label
    * Modified Get_Route_Push_Value
    * Modified Verify_Services_Accounting_Aggregation
    * Modified Verify_Task_Replication

* ABSTRACTED_LIBS
    * Modified Post_Execute_Command Processor
        * Made The `Valid_Section_Results` Argument Work As Intended

* IOSXE
    * Modified Triggerissu To Set The 'Device.Filetranser_Attributes' Attribute If Run Through Run_Genie_Sdk
    * Modified Verify_Chassis_Alarm_Output
        * Fixed Broken Functionality
    * Modified Write_Erase_Reload_Device
        * Moved Error Pattern Settings To Unicon
    * Modified Execute_Install_Package
        * To Ensure The Device Is In The Enable State After Reload
    * Modified Verify_Ping

* BLITZ
    * If Parent Keys Are Not Returned In Get-Config Of Empty Nested List Pass Test.
    * Preventing Possible Exception Of Not Saving A Value
    * Auto-Validation Failed For Edit-Config Of Multiple List Entries In One Rpc.
    * "Parent Keys Are Not Returned" Fix Broke Deleted Leaf Logic.

* NXOS
    * Modified Get_Interfaces_Status

* MAPLE_BLITZ
    * Replacing Xr()Xr Cases In Show Commands

* UTILS
    * Modified Stop Method In Tcpdump
        * To Use Actual Server Name For Searching In Server Block In Testbed Yaml

* GENERAL
    * Moved Reconnect Error Pattern Handling To Unicon


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* IOSXR
    * Added Verify_Interface_State_Down
        * Verify Interface State Is Down And Line Protocol Is Down
    * Asr9K
        * Added Verify_Current_Image
        * Added Get_Software_Version
    * Ncs5K
        * Added Verify_Current_Image
        * Added Get_Software_Version

* Linux
    * Added topic search API which can be used with the decoded output file

* NXOS
    * Added Get_Software_Version

* IOSXE
    * Cat9K
        * Added Verify_Boot_Variable

* COM
    * Added Get_Structure_Output
        * Generate Structure Data From Output Based On Spaces


