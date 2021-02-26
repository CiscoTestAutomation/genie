February 2021
=============

February 23rd - Genie v21.2
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.2                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.2                          |
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

**genie**

* harness
    * Updated discovery
        * avoid %VARIABLE to pick up device for Blitz testcase
    * Modfied configuration datafile
        * enhanced code to allow for jinja2 templates
* device
    * Fixed backward compatiblity of `platform` with `series` for Unicon
    * return result of connect to caller
* cli
    * Changed command shell to use pyats testbed loader


--------

**genie.libs.clean**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* APIC
    * Modified Clean_Schema In Stages To Support Controller_Reconnect Timeout

* MODIFIED VALIDATE_CLEAN TO SUPPORT THE 'CLEAN_DEVICES' KEY

* NXOS
    * Modified
        * Changed The P2 Pattern In The Ping_Stage To Accomodate Mds Platform
    * N7K
        * Modified The Imagehandler Class
            * To Fix An Issue With Using The Kickstart Image For Both Boot Variables

* COM
    * Modified Verify_Running_Image Stage
        * To Verify The Running Image Using Either The Image Name (Original Method) Or The Image Hashes (New Method)

--------

**genie.libs.conf**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* IOSXR
    * Modified
        * Modified Loopbackinterface So That It Will Actually Work With The `Loopback` Type

* NXOS
    * Modified Nxos Device Object
        * Removed Unexpected 'Logging Logfile Messages' Config



--------

**genie.libs.filetransferutils**

--------

**genie.libs.ops**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* IOSXE
    * Modified Isis Ops
        * Fixed A Bug When No Isis Config

* NX
    * Modified Import Statement
        * Fixed Showsysteminternall2Fwdermac

* IOSXR
    * Modified Learn Eigrp
        * Captures Default Vrfs Now



--------

**genie.libs.parser**

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* IOSXR
    * Added Showbfdsessiondestination
        * Show Bfd Session Destination {Ip_Address}
        * Show Bfd Ipv6 Session Destination {Ip_Address}
    * Added Showmplsldpdiscovery
        * Show Mpls Ldp Discovery
        * Show Mpls Ldp Discovery Detail
        * Show Mpls Ldp Afi-All Discovery
        * Show Mpls Ldp Discovery <Ldp>
        * Show Mpls Ldp Vrf <Vrf> Discovery
        * Show Mpls Ldp Vrf <Vrf> Discovery Detail
    * Added Showmribevpnbucketdb
        * Parser For Show Mrib Evpn Bucket-Db
    * Modified Show_Pim.Py
        * Added Show Pim Topology Summary
        * Added Show Pim Vrf <Vrf> Topology Summary
    * Added Showrouteallsummary
        * Show Route Afi-All Safi-All Summary
        * Show Route Vrf All Afi-All Safi-All Summary
        * Show Route Vrf <Vrf> Afi-All Safi-All Summary

* IOSXE
    * Added 'Show Track' Parser
        * Added Schema And Parser To Iosxe/Show_Track.Py
        * Added Test Files In Iosxe/Tests/Showtrack Test Directory
    * Added Showipslasummary
        * Show Ip Sla Summary
    * Added Class Showipeigrpinterfaces
        * Added Parser For "Show Ip Eigrp Interfaces"
    * Added Class Showipeigrpinterfacesschema
        * Added Schema For Showipeigrpinterfaces Class ("Show Ip Eigrp Interfaces")
    * Added Parser For Show Flow Monitor Sdwan_Flow_Monitor Statistics Command
    * Showsdwanbfdhistory
        * Added Parser For Show Sdwan Bfd History Command
    * Added Parser For Show Sdwan Appqoe Aoim-Statistics
        * Showsdwanappqoeaoimstatistics
    * Added Showswitchstackportssummary
        * 'Show Switch Stack-Ports Summary'

* IRONWARE
    * Initial Creation Of Ironware Parsers
    * Added Parsers
        * Show Interfaces Brief
        * Show Ip Interfaces
        * Show Media <Interface>
        * Show Mpls Lsp
        * Show Mpls Vll <Vll>
        * Show Mpls Vll-Local <Vll>
        * Show Mpls Ldp Neighbor
        * Show Optic <Slot>
        * Show Ip Ospf Neighbor
        * Show Ip Ospf Interface Brief
        * Show Ip Route
        * Show Ip Route Summary

* NXOS
    * Added Showeigrptopologyschema
    * Added Showeigrptopologysuperparser
    * Added Showipv4Eigrptopology
    * Added Showipv6Eigrptopology
        * For 'Show Ip Eigrp Topology'
        * For 'Show Ipv6 Eigrp Topology'

* IOS
    * Added Showinventory For Asr901
        * To Support Asr901 Output


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* IOSXE
    * Modified Showspanningtreedetail
        * Optional Interface Issue For Spanning Tree Output
    * Modified Showenvironmentall
        * Handling For Tab Characters In Output
    * Modified Showplatform
        * Enhanced Regex And Logic To Parse Various Outputs.
    * Updated Showinterfaces
        * Made Several Keys Optional
    * Modified Showauthenticationsessions
        * Show Authentication Sessions - Allow N/A As Method
    * Modified Showbgpsummarysuperparser
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Modified Showbootvar
        * To Make 'Configuration_Register' Optional
    * Patch Showmplsldpdiscovery
    * Updated Showaccesslists
        * Added `Acl_Type` To Distinguish Standard, Extended Or Ipv6
    * Modified Showswitchstackportssummary
        * 'Show Switch Stack-Ports Summary'
    * Modified Showswitchstackportssummary
    * Changed Neighbor, Link_Changes_Count From Schema To Int (Was String).
    * Added Cli/Empty/Empty_Output_Ouput.Txt
    * Updated Cli/Equal/Golden_Output1_Output.* For Integer Change Above

* NXOS
    * Modified Showinterface
        * Handling For "(Sfp Checksum Error)" And "(No Operational Members)"
    * Modify Showipinterfacevrfall
        * Fix Regex
    * Modified Showrunningconfignvoverlay
        * Fixed Regex To Support More Output
    * Removed Showsysteminternall2Fwdermac Class
        * Removed For Duplicated
    * Updated Showcdpneighborsdetail
        * Support Various Outputs

* JUNOS
    * Modified Showipv6Neighborsschema
        * Made Key Optional
    * Modified Showroutetable
        * Made Keys Optional
        * Fixed Regex
    * Modified Showinterfaces
        * Added Optional Key Ifff-User-Mtu
    * Modified Showinterfaces
        * Made Key Cos-Queue-Configuration Optional
    * Modified Pingmplsrsvp
        * Updated Code To Sopport Different Output
    * Updated Showospf3Interfaceextensive
        * Updated Regex P4 To Captured Varied Output
    * Updated Showospf3Interfaceextensive
        * Updated Regex To Capture Capture Bdr Addr
    * Updated Showtaskreplication
        * To Support Various Outputs
    * Updated Showlogfilename
        * Removed Unneeded Output As Logging Lines
    * Updated Showlogfilenamematchexcept
        * Removed Unneeded Output As Logging Lines

* IOS
    * Modified Showinventory
        * Enhanced Logic To Parse Various Outputs.

* IOSXR
    * Modify Showarpdetail
        * Change Regex To Capture Bundle-Ether Interfaces
    * Modified Showrunningconfigbgp
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Modified Showbgpinstancesummary
        * Update Regex To Support Vrf Name In Lowercase
    * Update Showplatform
        * Fixed To Run Unittests Successfully
    * Updated Showlogging
        * Fixed To Collect Logs With Include Option



--------

**genie.libs.robot**

--------

**genie.libs.sdk**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* JUNOS
    * Modified Get_Route_Table_Output_Interface
        * Added Exception Handling For Show Command Execution
    * Modified Get_Route_Table_Output_Label
        * Added Exception Handling For Show Command Execution
    * Fixed Verify_Bgp_All_Peer_State
    * Modified Verify_Traffic_Statistics_Data
        * Added Arguments Invert And Ipv4
    * Modified Get_Diagnostics_Optics_Stats
        * Fixed If-Condition To Support Lane Number Is 0
    * Modified Get_Services_Accounting_Aggregation_Template_Field
        * Make Source/Destination Arguments As Optional
    * Modified Verify_Task_Replication
        * Fixed Logic To Return Proper Result
    * Modified Verify_Bgp_Peer_Address
        * Support Another 'Establ' Output
    * Modified Verify_Ping
        * Added Interface Option
    * Modified Get_Task_Memory_Information
        * Updated Kwargs
    * Modified Verify_Bfd_Session_Destination_Detail
        * Added Ipv6 Flag
    * Modified Verify_Bfd_Session_Destination_Detail_No_Output
        * Added Ipv6 Flag
    * Modified Get_Route_Push_Value
        * Removed Subnet
    * Modified Verify_Services_Accounting_Aggregation
        * Fixed Code Logic
    * Modified Get_Route_Push_Value
        * Fixed Code Logic
    * Modified Verify_Routing_Ip_Exist
        * Verification If Rt_Destination Doesn'T Exist
    * Modified Verify_No_Log_Output
        * Returned True If Schemaparserempty Exception Comes Up
    * Modified Get_Interface_Traffic_Input_Pps
        * Modified Code To Get Parsed Output
    * Modified Verify_Bfd_Session_Detail
        * Modified Code To Get Parsed Output
    * Modified Get_Chassis_Cpu_Util_Alternative
        * Added Check To See If Log Output Exists
    * Modified Get_Chassis_Cpu_Util_Alternative
        * Updated Code Flow
        
* COMMON
    * Verification Of A Single Value From Multiple List Entries In Rpc-Reply Was Failing.
    * Return Value Still Being Processed Even Though "Selected" Is Set To False In Yaml.
    * Modified Yang Pause Handling When Auto-Validating Is Enabled
        * Pause Between Edit-Config And Auto-Validate Get-Config.

* IOSXE
    * Modified Yangexec To Handle Commit Failures
    * Fixed Rpcbuilder Test Cases
    * Modified Configure_Interfaces_Unshutdown
        * Fixed Logic Error
    * Modified Configure_Interfaces_Shutdown
        * Fixed Logic Error
    * Modified Get_Running_Image Api
        * To Get The Real Boot Image If The Boot Image Is Configured To Packages.Conf

* BLITZ
    * List Entry With Only Key Fails Auto-Validation
        * A Get-Config On A List Entry Returns At Least The Keys If Nothing Else.
    * Multiple List Entries With Same Values Are Not Validated
        * Keys Cannot Be Determined On Rpc-Reply And User Was Only Interested In
        * Values, So In This Case We Just Had A Bucket Of Values And Each Entry
        * Matched The First In The Bucket So We Ended Up With
        *  
        * Compare
        * Field-1, Id-1, Xpath-/A/B/C, Value-1234
        * Field-2, Id-2, Xpath-/A/B/C, Value-1234
        * Field-3, Id-3, Xpath-/A/B/C, Value-1234
        *  
        * Found
        * Field-1, Id-1, Xpath-/A/B/C, Value-1234
        * Field-1, Id-1, Xpath-/A/B/C, Value-1234
        * Field-1, Id-1, Xpath-/A/B/C, Value-1234
        *  
        * Only Interested In Xpath/Value And Id Does Not Matter But With Id Included
        * In Match It Was Failing.
        *  
        * User Could Make More Targeted Tests, One For Each Key, But This Test Setup
        * Should Not Fail.

* UTILS
    * Modified Verify_Pcap_Mpls_Packet
        * Handled Crash When Ip Packet Is None

* IOSXR
    * Modified Configure_Interfaces_Unshutdown
        * Fixed Logic Error
    * Modified Configure_Interfaces_Shutdown
        * Fixed Logic Error

* NXOS
    * Modified Configure_Interfaces_Unshutdown
        * Fixed Logic Error
    * Modified Configure_Interfaces_Shutdown
        * Fixed Logic Error


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* JUNOS
    * Added Verify_Ospf_Neighbor_Instance_State_All
    * Added Verify_Ospf3_Neighbor_Instance_State_All
    * Added Verify_Route_Instance_Type
    * Added Verify_Route_Instance_Exists
    * Added Verify_Route_Table_Route_Exists
    * Added Quick_Configure_By_Jinja2
    * Added Verify_Services_Accounting_Flow_Active
    * Added Get_Services_Accounting_Flow_Exported
    * Added Get_Services_Accounting_Flow_Active
    * Added Get_Services_Accounting_Flow_Expired
    * Added Get_Services_Accounting_Usage_Five_Second_Load
    * Added Verify_Bgp_Summary_Instance_Peers_State
    * Added Get_Interface_Ipv4_Address
    * Added Get_Ipv6_Interface_Ip_Address
    * Added Verify_Arp_Interface_Exists
    * Added Verify_Chassis_Fpc_Slot_Port
    * Added Verify_Ipv6_Neighbor_State
    * Modified Get_Bgp_Summary_Neighbor_State_Count
    * Modified Get_Chassis_Fpc_Cpu_Util
        * Fixed Redundant Method
    * Added Verify_Interface_Mtu
        * Verify Mtu Status Via Show Lacp Interfaces {Interface}

* IOSXE
    * Added Verify_Interface_Errors
    * Added Verify_Interface_State_Admin_Up
    * Added Verify_Ping
    * Added Get_Interfaces_Status
    * Modified Api Get_Platform_Core
        * Updated Not To Raise Exception
    * Added Get_Md5_Hash_Of_File
        * To Generate The Md5 Hash Of A File

* IOSXR
    * Added Verify_Interface_State_Up
    * Added Verify_Interface_Errors
    * Added Verify_Interface_State_Admin_Down
    * Added Verify_Interface_State_Admin_Up
    * Added Verify_Ping
    * Added Get_Interfaces_Status
    * Modified Api Get_Platform_Core
        * Added Arguments To Copy Core File To Remote Servers
    * Added Api Scp
    * Added Api Get_Platform_Logging
    * Added Get_Md5_Hash_Of_File
        * To Generate The Md5 Hash Of A File

* NXOS
    * Added Get_Interfaces_Status
    * Modified Api Scp
        * Updated Not To Raise Exception
    * Modified Api Get_Platform_Core
        * Added Arguments And Support More Features
    * Added Api Get_Platform_Logging
    * Added Api Scp
    * Added Get_Md5_Hash_Of_File
        * To Generate The Md5 Hash Of A File

* BLITZ
    * Executing Loop Iterations In Parallel
    * Updating Blitz To Save Variables Globally And Make Them Reusable In Testscript Level
    * All The Step Log Messages In Blitz Are Now Customizable
    * Updated Run_Condition To Work Without Specifying A Function
    * Updated Testbed Handling For Pyats Health Check

* LINUX
    * Added Get_Md5_Hash_Of_File
        * To Generate The Md5 Hash Of A File



--------

**genie.telemetry**

--------

**genie.trafficgen**

--------

**genie.utils**




