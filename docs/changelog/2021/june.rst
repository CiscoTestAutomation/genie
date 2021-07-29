June 2021
==========

June 29th - Genie v21.6
-----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.6                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.6                          |
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
                                      New
--------------------------------------------------------------------------------

* harness
    * Added ability to provide section specific parameters to sections in trigger datafile
    * Updated utils
        * Modified connect_device
            * Added support for new context schema for multiple connections
    * Updated script
        * Modified organize_testbed
            * Added context for new schema
    * Updated schema
        * Added support for new context schema

* conf
    * Updated Device
        * Modified parse
            * Added context parameter and made cli as default context
        * Modified _get_parser_output
            * Added context parameter and made cli as default for context and alias

* dq
    * Added sum_value_operator
        * Sum up values and evaluate operator against the total value

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* harness
    * Modified GenieStandalones
        * To initialize max_time/interval in case no value is given

* conf
    * Modified testbed loading logic to fix conversion bug

* dq
    * Modified query_validator
        * Method did not consider functions with no arguments as valid.
    * Modified str_to_dq_query
        * Method did not consider functions with no arguments as valid.
    * Modified value_operator
        * Use float instead of integer

* run_genie_sdk(): Workaround default device alias='uut' requirement

    Users can now give the device parameter with arbitrary alias without requiring to override the internal device parameter value. The change saves the original device alias temporarily and sets the current alias to 'uut' to allow the Genie harness to operate smoothly then revert back to the original alias once the trigger execution is complete.

**genie.libs.clean**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified get_bgp_neighbors_in_state API, fixed regex expression

* com
    * Updated clean stage 'delete_files_from_server'
        * updated docstring to mention supporting only ftp and sftp and schema

* iosxe
    * Modified device recovery
        * To properly match rommon prompts
        * When the 'Press RETURN to get started' prompt is seen, wait until the buffer is settled to send RETURN.


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* com
    * Modified 'connect' clean stage to include 'via' argument

* apic
    * Add `apply_configuration` clean stage for REST interactions

**genie.libs.conf**

No changes

**genie.libs.filetransferutils**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* common
    * Modified send_cli_to_device
        * Changed to return output after execution of cli command

* nxos
    * Modified copyfile
        * check both source and destination for server name
        * add check if server name is just number (module number)

**genie.libs.health**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* health
    * Enhanced device connectivity check
        * Updated logic with pcall for speed up
    * Added pyats_health default template 'health_yamls/pyats_health.yaml'
        * default template is used with '--health-checks'
    * Added 'force_all_connected' as health_settings
        * pyATS Health Check requires that all devices are connected by default. It can be disabled by this setting.
    * Modified internal functions
        * To support 'hide_processor' which you can hide specific processor from log

* health plugin
    * Added '--health-webex' argument
        * Added webex notification feature with notification template
    * Added '--health-remote-device' argument
        * Specify remote device information for copy files to remote
    * Added '--health-mgmt-vrf' argument
        * Specify Mgmt Vrf which is reachable to remote device
    * Added '--health-threshold' argument
        * Specify threshold for cpu, memory and etc
    * Added '--health-show-logging-keywords' argument
        * Specify show logging keywords to search
    * Added '--health-core-default-dir' argument
        * Specify directories where searching core file or etc
    * Added '--health-tc-sections' argument
        * same with '--health-sections' and `--health-sections` is now deprecated
    * Added '--health-tc-uids' argument
        * same with '--health-tc-uids' and `--health-uids` is now deprecated
    * Added '--health-tc-groups' argument
        * same with '--health-tc-groups' and `--health-groups` is now deprecated


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* health
    * pyats_health default template
        * Added save variable name 'health_value' for webex notification
    * Fixed internal logic to remove redundant run
        * Fixed a bug which causes redundant run with multiple health args

* health plugin
    * Modified saving health data
        * Save health result data to health_results.json in post_task
    * Added support multiple values to arguments
        * each health argument if applicable supports multiple values by delimiter ' '(space)

**genie.libs.ops**

No changes

**genie.libs.robot**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* robot
    * Modify GenieRobot
        * fix robot.libdoc generation for GenieRobot library


**genie.libs.sdk**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* blitz
    * blitz.py
        * Fixed bug that caused regex filtered variables not to be saved
    * updated 'save_variable'
        * changed logging message from info to debug.
    * Modified decorator 'add_result_as_extra'
        * Fixed a bug which was missing validation of return from action
    * Enhanced logging for Dq filter via include/exclude
        * Show Dq Filtered result and update message to be clearer
    * Updated Blitz class
        * Allow pyATS Health Check action to save variable inside of action
    * Modified add_result_as_extra for pyATS Health Check
        * Save health data to runtime variable instead of saving to file
        * Added webex notification support
        * Save variable which can be used in pyATS Health Check webex notification
    * Modified save_variable function
        * logging massage is changed from info to debug
    * Modified internal func '_find_saved_variable'
        * add handling for API which has argument 'section'

* nxos
    * Added retry mechanism to nxapi_method_nxapi_rest
    * Modified health_core API
        * Added FileUtils support to copy core file to remote device

* iosxe, isoxr, nxos, apic
    * Update copy_from_device and copy_to_device APIs to support HTTP transport incuding proxy support
    * Removed copy_to_script_host API (use copy_from_device instead)

* iosxe
    * Modified default_interface
        * Fixed docstring
    * Modified health_memory API
        * Fixed calculation in case pid is same
    * Modified health_core API
        * Added FileUtils support to copy core file to remote device
    * enhanced API 'health_cpu'
        * updated logic for speed up
    * enhanced API 'health_memory'
        * updated logic for speed up
    * enhanced API 'config_ip_on_interface'
        * Add argument for ipv6 address and configure if it is passed
    * updated 'get_ospf_interfaces'
        * added new argument 'ospf_process_id'. But keep 'bgp_as' for backward compatibility

* api utils
    * Modified API `verify_pcap_packet`
        * Added support to check the fragmented captured packet.
    * Modified API `verify_pcap_dscp_bit`
        * To verify the Expected destination IP address.
        * To verify the Expected protocol message type.
    * Modified API `verify_pcap_mpls_packet`
        * To verify the Expected source port number.
        * To verify the Expected destination port number.
        * To verify the Expected protocol message type.
        * To handle the port_and_or operation.
    * Modified API `web_interaction`
        * To handle the result status when time limit exceeded.

* utils
    * Modified copy_from_device
        * return output from FileUtils copyfile

* iosxr
    * Modified health_core API
        * Added FileUtils support to copy core file to remote device

* utils
    * added 'only_connected' to API 'get_devices'
        * check if device is connected and return only connected ones
    * added 'with_os' to API 'get_devices'
        * return dict with device name and os as key/value pair


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* blitz
    * 'execute' action
        * Added `result_status' to support result change only for `passed` based on user input.
    * markup.py
        * Added apply_regex_findall to search for patterns in a string
    * blitz.py
        * Modified _filter_and_save_action_output to expect regex_findall
    * Support attachment for pyATS Health Check webex notification
    * actions.py
        * Added `result_status' to support result change only for `passed` based on user input
    * actions_helper.py
        * Added `result_status' to support result change only for `passed` based on user input
    * advanced_actions.py
        * Modified custom_substep_message in loop to support the use of %VARIABLES{}
    * markup.py
        * Added save_output_to_file to save the output of an action to a specified file
    * blitz.py
        * Modified _filter_and_save_action_output to expect file_name and append arguments
    * add webex notification support for pyATS Healtch Check
    * 'execute' action
        * Added `connection_alias' to support different connections
    * 'parse' action
        * Added `connection_alias' to support different connections
        * Added `context' to use different context
    * 'configure' action
        * Added `connection_alias' to support different connections
    * 'configure_dual' action
        * Added `connection_alias' to support different connections

* api utils
    * Added API `web_interaction`
        * To return result of user choice for manual steps. same capability with WebInteraction.
    * Added API `verify_pcap_ldp_packet`
        * To verify the LDPHello and LDPKeepAlive packet

* utils
    * add 'verify_device_connection'
        * check device connectivity and return Boolean. have reconnect feature

* nxos/n9k
    * add 'health_core' for N9K
        * copy_from_device with default timeout 600 secs and use-kstack

* iosxe
    * API Utils
        * Added API `verify_device_tracking_policies`
        * Added API `verify_ip_mac_binding_in_network`
        * Added API `verify_ip_mac_binding_not_in_network`
        * Added API `verify_ip_mac_binding_count`

**genie.libs.parser**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMroute
        * add lisp_mcast_source/lisp_mcast_group to outgoing interface ip mroute schema.
        * add '-' as additional possible character in "state"
        * Modified regex pattern to accomodate state with lowercase letters
    * Modified ShowAuthenticationSessionsInterfaceDetails
        * Added optional key unauth_timeout to schema.
            * Added regex pattern p13 to accept all type of inputs for restart_timeout.
            * Added regex pattern p14 for unauth_timeout key.
            * Added keys unauth_timeout into the schema.
    * Modified ShowAuthenticationSessionsInterfaceDetails
        * Removed session_timeout from known_list on p1 to fix incorrect match
    * Added ShowInterfaceTransceiver for
        * show interfaces {interface} transceiver
    * Modified ShowInterfaceTransceiverDetail to
        * Parse transceiver information
    * Modified ShowVrfDetailSuperParser
        * Added keys <import_route_map> and <export_route_map> to schema.
        * Added regex patterns <p7_2> and <p8_2> to accommodate various outputs.
    * Modified ShowIpStaticRoute
        * Fixed line stripping issue that broke Ops unittests.
    * Modified
        * Modified show_device_tracking.py to fix a bug in show_device_tracking
        * Now able to match entries with time left
    * Modified ShowUsers
        * Bug workaround to capture location data when it's forced onto a newline.
    * Modified ShowPolicyMapTypeSuperParser
        * Changed <pattern> from schema to Optional.
        * Updated regex patterns <p0> and <p12> to accommodate various outputs.
        * Added regex patterns <p3_1>, <p8_0>, <p9_0> to accommodate various outputs.
    * Modified ShowPlatformSoftwareMemoryBacktraceSchema
        * Changed type for callsite from int to str
    * Modified ShowIpStaticRoute
        * Added support for dashes in names
    * Modified ShowIpv6StaticDetail
        * Added support for dashes in names
    * Modified ShowPlatformResourcesSchema
        * Made 'esp' optional
    * Modified ShowLogging
        * Fixed patterns to support show logging parser when monitor logging is disabled
        * Fixed pattern p11 to recognize vrf information
    * Modified ShowLoggingSchema
        * Made monitoring keys (level, message_logged, xml and filtering) optional
    * Modified ShowVersion
        * only accepted digits for Motherboard Revision Number now accept all characters.
    * Added Parser for ShowRedundancyApplicationGroup
        * show redundancy application group {group_id}
    * Modified ShowIpEigrpInterfaces
        * Adjusting p1 regex to support IPv6 too
        * Offloading parser to a SuperParser class
        * Support eigrp named mode
        * Added Optional keys to ShowIpEigrpInterfacesSchema schema to support `show ip eigrp interfaces detail parser`
    * Modified ShowInterfaces
        * Updated regex pattern p11 to accomodate media types with a period (ex 2.5G)

* nxos
    * Modified ShowRunningConfigNvOverlay
        * Added key <ingress_replication_protocol_bgp> to schema
        * Added regex pattern <p17> and related code
    * Modified ShowInterface
        * Modified regex pattern <p1> to accomodate different link states
        * Added regex pattern <p4_1> to process various VLAN description outputs
        * Added unit test to support changes
    * Modified ShowInterfaceTransceiverDetails
        * Added regex pattern <p37_1> as a catch-all for when <p37> doesn't match.
    * Modified ShowIpRoute
        * Added key <asymmetric> to schema
        * Added regex pattern <p3> and related code
    * Modified ShowIpInterfaceBriefVrfAll
        * Added in workaround for vrf information not being output
    * Modified ShowInterface
        * Added regex pattern p3_1 to process MAC address and type for VLAN.
    * Modified ShowIpInterfaceBriefVrfAll
        * Changed Schema to record vrf info
        * Changed parser to capture vrf info
    * Modified ShowCdpNeighbors
        * Added regex patterns p6 and p7 to accept Linux interface names
        * Added unittest
        * Added folder based unittest
    * Modified ShowInterface
        * Fixed issue where incoming storm supression being measured in bytes would cause in_jumbo_packets to not be parsed.
    * Modified ShowInterfaceBrief
        * Fixed issue with parser when speed for 'mgmt0' wasn't a digit

* iosxr
    * Modified ShowL2vpnBridgeDomainDetail
        * Fixed variable referenced before assignment error
        * Added support for outputs where MPLS data wants to be inside the LSP dict
        * Added support for more keys in the schema to match sample output
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetail
        * changed 'state' to return lowercase instead of the default uppercase.

* ios
    * Added ShowInterfaceTransceiver for
        * show interface {interface} transceiver

* added showinterfacetransceiverdetail for
    * show interface {interface} transceiver detail

* unittest
    * Modified SuperFileBasedTesting
        * Added check to skip classes that do not contain a cli_command. This serves to skip outdated tcl based parsers.

* iosxe
    * Modified ShowVrrp
        * Added schema key <address family> to handle new device output
        * Added <master_advertisement_expiration_secs> key to schema
        * Added <state_duration> key to schema
    * Modified ShowPolicyMapTypeSuperParser
        * Updated regex pattern p3 to make bytes optional
    * Modified ShowDeviceTrackingDatabase
        * Update regex to capture output related to 'time left' for 'show device-tracking database'
    * Added ShowPolicyMapTypeControlSubscriberBindingPolicyName
        * show policy-map type control subscriber binding {policy_map_name}

* nxos
    * Modified ShowIsisAdjacency
        * Fixed p2 regex to match lines with SNPA N/A and level 1-2
    * Modified ShowNveInterfaceDetailSchema
        * Added anycast_if key to the schema

* nx-os
    * Modified ShowLldpNeighborsDetail
        * If an NX-OS device is connected to an IOS-XR device the interface formats will be processed

* utils
    * Modified Common.py - Common.convert_intf_name
        * Dictionary containing interface conversions is now nested.
        * Created *generic* key as a catchall for previous code.
        * Edited logic to check if a specific operating system is mentions in the os= argument

* iosxr
    * Modified ShowIpInterfaceBrief class
        * Updated regex to make VRF optional
        * IOSXE
            * Modified ShowClassMap
                * Added missing quotes to cli_command


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added ShowMabAllDetails
        * show mab all details
    * Added ShowIpDhcpDatabase
        * show ip dhcp database
    * Added ShowMeraki
        * show meraki
        * show meraki switch {switch}
    * Added ShowIpBgpL2VPNEVPN
        * Added parser for "show ip bgp l2vpn evpn detail"
        * Added parser for "show ip bgp {address_family} evi {evi}
        * Added parser for "show ip bgp {address_family} route-type {rt}"
        * Added parser for "show ip bgp {address_family} evi {evi} route-type {rt}"
        * Added nlri_data object under prefixes in "ShowBgpAllDetailSchema"
        * Added pmsi_data object under prefixes in "ShowBgpAllDetailSchema"
        * Added igmpmld object under prefixes in "ShowBgpAllDetailSchema"
        * Added 4 regexp in ShowBgpDetailSuperParser
            * p3_3 to handle all EVPN route-types
            * p8_6 to handle PMSI attribute Flags
            * p19 to handle IGMP/MLD filter
        * Modified 3 regexp in ShowBgpDetailSuperParser
            * p11 to handle local IRB vxlan vtep
            * p12 to handle core bdi
            * p13 to handle evpn l3-vni
        * Added folder based unittests
    * Added ShowPortSecurity
        * show port-security
        * show port-security interface <interface>
    * Added ShowPlatformSoftware
        * for 'show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics'
    * Added ShowIpv6EigrpInterfaces
        * show ipv6 eigrp interfaces
    * Added ShowIpEigrpInterfacesDetail
        * show ip eigrp interfaces detail
    * Added ShowIpv6EigrpInterfacesDetail
        * show ipv6 eigrp interfaces detail
    * Added ShowKeyChain
        * show key chain
    * Added ShowIpv6Protocols
        * show ipv6 protocols
        * show ipv6 protocols vrf {vrf}
    * Added ShowInterfacesLink
        * show interfaces link
        * show interfaces {interface} link

* iosxr
    * Added ShowOspfInterface
        * show ospf interface
        * show ospf interface <interface_name>
        * show ospf <process_name> interface
        * show ospf <process_name> interface <interface_name>
    * Added ShowOspfv3VrfAllInclusiveDatabasePrefix
        * show ospfv3 vrf all-inclusive database prefix
    * Added ShowOspfv3VrfAllInclusiveDatabaseRouter
        * show ospfv3 vrf all-inclusive database router
    * Added ShowOspfNeighbor
        * show ospf neighbor
        * show ospf {process_name} neighbor
        * show ospf vrf all-inclusive neighbor

* nxos
    * Added RunBashTop
        * Added 'top -n 1' command under 'run bash' mode
    * Added ShowSystemInternalProcessesMemory
        * 'show system internal processes memory'

* ios-xr
    * Added ShowOspfDatabaseRouter
        * show ospf database {process-id} router
        * show ospf database all-inclusive router

* ios
    * Added ShowLldpNeighbors
        * show lldp neighbors
    * Added ShowIpv6EigrpInterfaces
        * show ipv6 eigrp interfaces
    * Added ShowIpEigrpInterfacesDetail
        * show ip eigrp interfaces detail
    * Added ShowIpv6EigrpInterfacesDetail
        * show ipv6 eigrp interfaces detail
    * Added ShowKeyChain
        * show key chain
    * Added ShowIpv6Protocols
        * show ipv6 protocols
        * show ipv6 protocols vrf {vrf}

* iosxe
    * Added ShowDeviceTrackingPolicies
        * add show command 'show device-tracking policies'

* asa
    * Added ShowCryptoIkev2Sa
        * show crypto ikev2 sa
    * Added ShowNameif
        * show nameif
    * Added ShowFailover
        * show failover
    * Added ShowFailoverInterface
        * show failover interface

**genie.telemetry**

No changes

**genie.trafficgen**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* ixiarestpy
    * Added ixiarestpy based on ixnetwork_restpy

* genie.trafficgen
    * Implemented abstraction
        * Use `os ixianative|ixiarestpy|trex` to select connection type


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* ixianative
    * Enhanced exception message in check_traffic_loss
        * only 1 traffic item is not supported. error clearly mentions.


**genie.webdriver**

No changes






