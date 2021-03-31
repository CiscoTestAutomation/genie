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

If you have pyATS installed, you can use:

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



**genie.libs.parser**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* NXOS
    * Modified Showversion
        * Show Version
    * Modified Showforwardingipv4
        * Updated Regex Patterns P3 And, P3_1 To Accommodate Various Outputs.
    * Modified Showrunningconfignvoverlay
        * Fixed Regex To Support More Output
    * Modified Showbgppolicystatisticsparser
        * Change Xml.Getchildren To List(Item) Because Of Python 3.9 Deprecation
    * Modified Showvrf
        * Update Regex To Accommodate Reason That Are More Than One Word.
        * Added New Folder Based Unittests.
    * Modified Showlldpneighborsdetail
        * Update Regex P5 And P6 To Handle Spaces In System_Name And System_Description For 'Show Lldp Neighbors Detail' Command.
        * Converted Unittestss To New Folder Based Unittests And Add New Unittests.
    * Removed Showsysteminternall2Fwdermac Class
        * Removed For Duplicated
    * Modified Showiproute
        * Updated Regex Pattern <Next_Hop> To Accommodate Various Outputs.
    * Modified Showinterfacebrief
        * To Support Only Port-Channel Interfaces In The Output
    * Updated Showcdpneighborsdetail
        * Support Various Outputs
    * Modified Showinterface
        * Handling For "(Sfp Checksum Error)" And "(No Operational Members)"

* IOSXE
    * Modified Showspanningtreedetail
        * Optional Interface Issue For Spanning Tree Output
    * Modified Showiproute
        * Updated Src_Protocol_Dict To Contain New Key Codes Including '+', '%', 'P', '&' For Static, Connected, Bgp, Ospf, Eigrp Routes
        * Modified Regex Pattern P3 For Both Ipv4 And Ipv6 Tables To Include Above Symbols When Parsing
        * Modified Regex Pattern P3 To Include Next Hop Vrf. Before Vrf Was In Brackets And Was Being Treated As An Outgoing Interface Which Was Incorrect
        * Added Vrf Field For Next Hop In Output Dictionary Of Show Ip Route.
    * Added Parser For Show Flow Monitor Sdwan_Flow_Monitor Statistics Command
    * Patch Showmplsldpdiscovery
    * Updated Showaccesslists
        * Added `Acl_Type` To Distinguish Standard, Extended Or Ipv6
    * Modified Ping
        * Added Arguments For Ping Api
        * Updated Regex To Support Various Outputs
    * Updated Showinterfaces
        * Made Several Keys Optional
    * Modified Showbootvar
        * To Make 'Configuration_Register' Optional
    * Modified Showauthenticationsessions
        * Show Authentication Sessions - Allow N/A As Method
    * Modified Showbgp
        * Update Cli_Command To Accept 'Show Bgp {Address_Family} Unicast'.
        * Add Folder Based Unittests.
    * Modified Showplatform
        * Enhanced Regex And Logic To Parse Various Outputs.
    * Modified Showbgpsummarysuperparser
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Showsdwanbfdhistory
        * Added Parser For Show Sdwan Bfd History Command
    * Added Class Showipeigrpinterfaces
        * Added Parser For "Show Ip Eigrp Interfaces"
    * Added Class Showipeigrpinterfacesschema
        * Added Schema For Showipeigrpinterfaces Class ("Show Ip Eigrp Interfaces")
    * Modified Showenvironmentall
        * Handling For Tab Characters In Output
    * Modified Showiproute
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showipv6Route
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showiprouteword
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showipv6Routeword
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showswitchstackportssummary
        * 'Show Switch Stack-Ports Summary'
    * Modified Showswitchstackportssummary
    * Changed Neighbor, Link_Changes_Count From Schema To Int (Was String).
    * Added Cli/Empty/Empty_Output_Ouput.Txt
    * Updated Cli/Equal/Golden_Output1_Output.* For Integer Change Above

* JUNOS
    * Modified Showroutetable
        * Made Keys Optional
        * Fixed Regex
    * Modified Showchassisenvironmentfpc
        * Updated P_Power Regex Pattern
        * Made Voltage Key Optional
    * Modified Showchassispower
        * Changed Some Keys To Optional.
        * Added Regex To Capture Wider Variety Of Device Output
    * Modified Showipv6Neighborsschema
        * Made Key Optional
    * Modified Showinterfaces
        * Added Optional Key Ifff-User-Mtu
    * Modified Showinterfacesdescriptions
        * Update Regex P2 - Description - To Accommodate Spaces For 'Show Interfaces Descriptions'.
        * Add Folder Based Unittests.
    * Modified Showddosprotectionprotocol
        * Accounted For Fpc Slots
    * Modified Pingmplsrsvp
        * Updated Code To Sopport Different Output
    * Updated Showinterfaces
        * Updated P2 Regex. Added ? To `(, +Generation +\S+)`
        * Added P32_1. Checks For `Addresses`
    * Modified Showchassispower
        * Changed Some Keys To Optional.
        * Added Regex To Capture Wider Variety Of Device Output
    * Modified Filelistdetailschema
    * Modified Pingschema
    * Modified Showarpnoresolveschema
    * Modified Showarpschema
    * Modified Showbgpgroupbriefschema
    * Modified Showbgpsummaryschema
    * Modified Showchassisalarmsschema
    * Modified Showchassisenvironmentcomponentschema
    * Modified Showchassisenvironmentfpcschema
    * Modified Showchassisfabricplaneschema
    * Modified Showchassisfabricsummaryschema
    * Modified Showchassisfirmwareschema
    * Modified Showchassisfpcpicstatusschema
    * Modified Showchassisfpcschema
    * Modified Showchassishardwaredetailschema
    * Modified Showchassishardwareextensiveschema
    * Modified Showchassishardwareschema
    * Modified Showchassispicfpcslotpicslotschema
    * Modified Showchassisroutingengineschema
    * Modified Showconfigurationprotocolsmplspathschema
    * Modified Showddosprotectionprotocolschema
    * Modified Showfirewalllogschema
    * Modified Showinterfacesdescriptionsschema
    * Modified Showinterfacesdiagnosticsopticsschema
    * Modified Showinterfacespolicersinterfaceschema
    * Modified Showinterfacesqueueschema
    * Modified Showinterfacesschema
    * Modified Showinterfacesstatisticsschema
    * Modified Showipv6Neighborsschema
    * Modified Showkrtqueueschema
    * Modified Showlacpinterfacesinterfaceschema
    * Modified Showlacpstatisticsinterfacesinterfaceschema
    * Modified Showldpdatabasesessionipaddressschema
    * Modified Showldpneighborschema
    * Modified Showospf3Databaseextensiveschema
    * Modified Showospf3Databaseexternalextensiveschema
    * Modified Showospf3Databaselinkadvertisingrouterschema
    * Modified Showospf3Databasenetworkdetailschema
    * Modified Showospf3Databaseschema
    * Modified Showospf3Interfaceextensiveschema
    * Modified Showospf3Interfaceschema
    * Modified Showospf3Neighborextensiveschema
    * Modified Showospf3Neighborinstanceallschema
    * Modified Showospf3Neighborschema
    * Modified Showospf3Routenetworkextensiveschema
    * Modified Showospf3Routerouteschema
    * Modified Showospfdatabaseadvertisingrouterselfdetailschema
    * Modified Showospfdatabaseextensiveschema
    * Modified Showospfdatabaseexternalextensiveschema
    * Modified Showospfdatabasenetworklsaiddetailschema
    * Modified Showospfdatabaseopaqueareaschema
    * Modified Showospfdatabaseschema
    * Modified Showospfdatabasesummaryschema
    * Modified Showospfinterfaceextensiveschema
    * Modified Showospfneighborextensiveschema
    * Modified Showospfneighborinstanceallschema
    * Modified Showospfneighborschema
    * Modified Showospfroutebriefschema
    * Modified Showospfroutenetworkextensiveschema
    * Modified Showospfrouteprefixschema
    * Modified Showospfstatisticsschema
    * Modified Showppmtransmissionsprotocolbfddetailschema
    * Modified Showpferoutesummaryschema
    * Modified Showrsvpneighbordetailschema
    * Modified Showrsvpsessionschema
    * Modified Showrouteadvertisingprotocoldetailschema
    * Modified Showrouteadvertisingprotocolschema
    * Modified Showrouteforwardingtablelabelschema
    * Modified Showrouteforwardingtablesummaryschema
    * Modified Showrouteinstancedetailschema
    * Modified Showrouteinstancenameschema
    * Modified Showrouteprotocolextensiveschema
    * Modified Showroutereceiveprotocolextensiveschema
    * Modified Showroutereceiveprotocolpeeraddressextensiveschema
    * Modified Showroutereceiveprotocolschema
    * Modified Showrouteschema
    * Modified Showroutesummaryschema
    * Modified Showroutetablelabelswitchednameschema
    * Modified Showservicesaccountingaggregationtemplateschema
    * Modified Showservicesaccountingerrorsschema
    * Modified Showservicesaccountingflowschema
    * Modified Showservicesaccountingmemoryschema
    * Modified Showservicesaccountingstatusschema
    * Modified Showservicesaccountingusageschema
    * Modified Showsnmpconfigurationschema
    * Modified Showsnmpstatisticsschema
    * Modified Showsystemcommitschema
    * Modified Showsystemconnectionsschema
    * Modified Showsystemcoredumpsschema
    * Modified Showsystemqueuesschema
    * Modified Showsystemstatisticsschema
    * Modified Showsystemstorageschema
    * Modified Showsystemusersschema
    * Modified Showteddatabaseipaddressschema
    * Modified Showversiondetailschema
    * Modified Showversioninvokeonallroutingenginesschema
    * Modified Showversionschema
    * Modified Traceroutenoresolveschema
        * Using Listof Instead Of Use
    * Modified Showservicesaccountingaggregationtemplate
        * Allowed For Multiple Entries
    * Updated Showospf3Interfaceextensive
        * Updated Regex To Capture Capture Bdr Addr
    * Modified Showinterfaces
        * Made Key Cos-Queue-Configuration Optional
    * Modified Showchassispicfpcslotpicslot
        * Fixed Uptime Regex
            * Accounted For Seconds And Second
            * Accounted For Lack Of Hours
    * Updated Showospf3Interfaceextensive
        * Updated Regex To Capture Capture Bdr Addr
    * Updated Showospf3Interfaceextensive
        * Updated Regex P4 To Captured Varied Output
    * Modified Showchassispicfpcslotpicslot
        * Fixed Uptime Regex
            * Accounted For Seconds And Second
            * Accounted For Lack Of Hours
    * Updated Showtaskreplication
        * To Support Various Outputs
    * Modified Showchassisenvironmentfpc
        * Updated P_Power Regex Pattern
        * Made Voltage Key Optional

* IOS/CAT6K, IOS/C7600, IOSXE/CAT4K, NXOS
    * Modified Showmoduleschema Class
        * Add 'Slot' Key
    * Modified Showmodule
        * Add Slot Value To Leaf

* UTILS
    * Turn The Unittest Code Into A Standalone Importable
    * Modified Common()
        * Change Xml.Getchildren To List(Item) Because Of Python 3.9 Deprecation
    * Turn The Unittest Code Into A Standalone Importable

* IOSXR
    * Modified Ping
        * Added Arguments For Ping Api
        * Updated Regex To Support Various Outputs
    * Update Showplatform
        * Fixed To Run Unittests Successfully
    * Modified Showinterfacesdescription
        * Update Regex P2 - Description - To Accommodate Spaces For 'Show Interfaces Description'.
    * Modified Showethernettags
        * Removed Cli_Command From Showethernettags In 'Show_Ethernet.Py'
        * Migrated Unitest For 'Show Ethernet Tags' To New Style Unittests 'Showethernettags' Folder
        * Removed 'Src/Genie/Libs/Parser/Iosxr/Tests/Test_Show_Ethernet_Yang.Py'
        * Removed 'Src/Genie/Libs/Parser/Iosxr/Tests/Test_Show_Interface.Py' Since All Unittests In This File Have Been Migrated To New Unittests Folder
    * Modified Showlldpentry
        * Update Regex P2 To Handle Spaces In Chassis_Id For 'Show Lldp Neighbors Detail' Command.
        * Add Folder Based Unittests.
    * Modified Showrunningconfigbgp
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Modified Showbfdsession
        * Changed <Async_Msec> And <Echo_Msec> From Schema To Optional.
        * Changed Showbfdsession Folder Tests To Reflect This Change
        * Removed Showbfdsession From Parser Unittest Ignore List
    * Modified Showbgpinstancesummary
        * Update Parser To Accept Numbers And Dotted Numbers For Remote_As In P17_2.
    * Modify Showarpdetail
        * Change Regex To Capture Bundle-Ether Interfaces
    * Modified Showbgpinstancesummary
        * Update Regex To Support Vrf Name In Lowercase
    * Updated Showlogging
        * Fixed To Collect Logs With Include Option

* ASA
    * Modified Showinterfaceipbrief
        * Updated Regex Patterns <Method> And <Link_Status> To Properly Capture Device Output

* IOS
    * Modified Showinventory
        * Enhanced Logic To Parse Various Outputs.
    * Added Class Showipeigrpinterfaces
        * Added Parser For "Show Ip Eigrp Interfaces"

* IOSXE AND IOSXE/C9500
    * Modified Showversion
        * Added Label And Build_Label Keys To Schema
        * Added Xe_Version Key To Show Version Schema
        * Updated Regex Patterns P0 To Catch Xe_Version
        * Updated Regex P1/P3 To Catch Label And Build_Label
        * Update Version_Short To Match Major.Minor For Xe/9500

* IOS-XR
    * Modified Showcdpneighborsdetail
        * Updated Regex Pattern <Platform> To Accommodate Various Outputs.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* IOSXR
    * Added Following Commands For Dir
        * Dir Location {Location}
        * Dir {Directory} Location {Location}
    * Added Showusers
        * Show User

* IOSXE
    * Added Showsdwanzbfwstatistics
        * Show Sdwan Zbfw Zonepair-Statistics
    * Added Parser For Show Sdwan Appqoe Aoim-Statistics
        * Showsdwanappqoeaoimstatistics
    * Added Showipslasummary
        * Show Ip Sla Summary
    * Added Showsdwanzbfwstatistics
        * Show Sdwan Zbfw Zonepair-Statistics
    * Modified Showvrrp
        * Changed Schema To Allow Track_Group To Optionally Be Nested Level With Most Other Key/Value Pairs.
            * Added Regex Pattern <Track> To Accommodate Various Outputs.
            * Added Key <Flags> Into The Schema.
    * Added Parser Capabilities And A New 'Show Vrrp All' Parser To Handle The Following Commands
        * Show Vrrp All
        * Show Vrrp Interface {Interface}
        * Show Vrrp Interface {Interface} All
        * Show Vrrp Interface {Interface} Group {Group}
        * Show Vrrp Interface {Interface} Group {Group} All
    * Added Showipnbarclassificationsocket
        * Show Ip Nbar Classification Socket-Cache <Number_Of_Sockets>

* NXOS
    * Added Showusers
        * Show User
    * Added Ping
        * Ping {Addr}
        * Ping {Addr} Source {Source} Count {Count}
    * Modified Showinterfacebrief
        * Modified Parser To Accommodate Nve Related Config.
        * `Show Interface Brief Nve 1`
    * Added Showenvironment
        * For 'Show Environment'
    * Added Showenvironmentfan
        * For 'Show Environment Fan'
    * Added Showenvironmentfandetail
        * For 'Show Environment Fan Detail'
    * Added Showenvironmentpower
        * For 'Show Environment Power'
    * Added Showenvironmentpowerdetail
        * For 'Show Environment Power Detail'
    * Added Showenvironmenttemperature
        * For 'Show Environment Temperature'
        * For 'Show Environment Temperature Module {Module}'
    * Added Showinterfacecapabilities
        * For 'Show Interface Capabilities'
        * For  'Show Interface {Interface} Capabilities'
    * Added Showinterfacetransceiver
        * For 'Show Interface Transceiver'
        * For 'Show Interface {Interface} Transceiver'
    * Added Showinterfacetransceiverdetails
        * For 'Show Interface Transceiver Details'
        * For 'Show Interface {Interface} Transceiver Details'
    * Added Showinterfacefec
        * For 'Show Interface Fec'
    * Added Showinterfacehardwaremap
        * For 'Show Interface Hardware-Mappings'

* IOS
    * Added Ping
        * Ping {Addr}
        * Ping {Addr} Source {Source} Repeat {Count}
    * Added Showinventory For Asr901
        * To Support Asr901 Output

* Added new VRRP tests
    * IOSXE/tests/ShowVrrp
    * IOSXE/tests/ShowVrrpAll
    * IOSXE/tests/ShowVrrpBrief
    * IOSXE/tests/ShowVrrpBriefAll

**genie.trafficgen**

* ixianative.py
    * Modified save_packet_capture_file
        * Fixed so that it returns `directory` variable instead of static value
