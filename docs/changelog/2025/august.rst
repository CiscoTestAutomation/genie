August 2025
==========

September 30 - Genie v25.8 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.8 
    ``genie.libs.health``, v25.8 
    ``genie.libs.clean``, v25.8 
    ``genie.libs.conf``, v25.8 
    ``genie.libs.filetransferutils``, v25.8 
    ``genie.libs.ops``, v25.8 
    ``genie.libs.parser``, v25.8 
    ``genie.libs.robot``, v25.8 
    ``genie.libs.sdk``, v25.8 
    ``genie.telemetry``, v25.8 
    ``genie.trafficgen``, v25.8 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie
    * Added retry functionality to the harness connect method with parameters
        * retry Boolean flag to enable retry functionality
        * retry_max_time Maximum time in seconds to retry connection (default 300)
        * retry_interval Time interval in seconds between retries (default 30)
    * Fix tgn-disable-regenerate-traffic argument default value from True to False



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe/copy_to_device
    * Added md5 verification before copying the image to the device.

* stages
    * Install image reloads to Press Enter key add a statement to handle return key after the image reloads.

* iosxe
    * Modified clean connect to handle exhaused credentials error and trigger password recovery

* clean-pkg
    * Added delay after applying configuration to the device
    * iosxe
        * Updated the logic to work for ha/stack device in install image and install SMU stages
        * Increased the timeout to 3 minutes since by default the image take time to be applied.

* iosxe/connect
    * Removed duplicate configure rommon variable in connect stage.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified Service-Acceleration
        * Added service vlan keys to service-acceleration conf model



genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""

genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_pvlan_for_input_service_policy
        * API to Configures private VLAN settings on an input interface.
    * Added configure_pvlan_for_output_service_policy
        * API to Configures private VLAN settings on an output interface.
    * Added configure_extended_acl_with_dscp
    * Added configure_rep_segment_auto
        * API to configure_rep_segment_auto
    * Added configure_fastrep_segment_auto
        * API to configure_fastrep_segment_auto
    * Added unconfigure_call_home_profile_destination_transport_method
        * API to unconfigure_call_home_profile_destination_transport_method
    * Added config API configure_crypto_isakmp_profile
    * Added config API unconfigure_crypto_isakmp_profile
    * cat9kv
        * Added API get_boot_variables and get_config_register
    * ISA
        * API to clear crypto isakmp
    * Added configure_ipv6_prefix_list_with_permit_deny
        * API to Configures ipv6 prefix list on Device
    * Added unconfigure_ipv6_prefix_list_with_permit_deny
        * API to unconfigures ipv6 prefix list on Device
    * Added config API configure_crypto_pki_http_max_buffer_size
    * Added config API unconfigure_crypto_pki_http_max_buffer_size
    * Added configure_ip_nat_switchover_http and unconfigure_ip_nat_switchover_http
        * API to configure_ip_nat_switchover_http and unconfigure_ip_nat_switchover_http
    * Added config API configure_crypto_pki_crl_request
    * Added config API unconfigure_crypto_pki_crl_request
    * Added execute API clear_crypto_pki
    * Added new API to configure ipv4 access list on line vty
        * API to configure ipv4 access list on line vty
    * Added new API to unconfigure ipv4 access list on line vty
        * API to unconfigure ipv4 access list on line vty
    * Added new API to configure ipv6 access list on line vty
        * API to configure ipv6 access list on line vty
    * Added new API to unconfigure ipv6 access list on line vty
        * API to unconfigure ipv6 access list on line vty
    * Added API to configure facility alarm temperature primary
        * Added support for configuring the primary temperature threshold for facility alarms.
        * The API allows setting the temperature threshold to 'high' and specifying the value.
    * Added API to unconfigure facility alarm temperature primary
        * Added support for unconfiguring the primary temperature threshold for facility alarms.
        * The API allows removing the temperature threshold configuration.
        * Added support for configuring and unconfiguring notifications for primary temperature alarms.
        * Added support for configuring and unconfiguring relay settings for primary temperature alarms.
        * Added support for configuring and unconfiguring syslog settings for primary temperature alarms.
    * Added API to configure facility alarm temperature secondary
    * Added API to unconfigure facility alarm temperature secondary
        * Added support for unconfiguring the secondary temperature threshold for facility alarms.
        * The API allows removing the temperature threshold configuration.
        * Added support for configuring and unconfiguring notifications for secondary temperature alarms.
        * Added support for configuring and unconfiguring relay settings for secondary temperature alarms.
        * Added support for configuring and unconfiguring syslog settings for secondary temperature alarms.
    * Added API to configure logging alarm
    * Added API to unconfigure logging alarm

* api to configure extended access-list with dscp configure.

* iosxe/health/health_core
    * Update the api to collect core files for stack devices.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_route_map_permit to add few arguments
        * Added global_nhop for default recursive global next hop
        * Added default_recursive for default recursive next hop
        * Added default_nhop_ip for default recursive next hop address
    * Modified unconfigure_route_map_permit to add few arguments
        * Added vrf for default recursive vrf next hop
        * Added global_nhop for default recursive global next hop
        * Added default_recursive for default recursive next hop
        * Added default_nhop_ip for default recursive next hop address
    * Updated password_recovery API, added init_connection to initialize connection
    * Removed
        * unconfigure_crypto_pki_server

* iosxe/platform/get
    * Refactored get_platform_model_number to reliably return chassis PID as a string.
    * Added fallback logic to gather PIDs from inventory slots if chassis PID is missing.
    * Normalized show version parsing to ensure consistent comparison with inventory PIDs.

* iosxe/rommon/utils
    * Updated device_rommon_boot api to use correct tftp boot command.
    * Updated device_rommon_boot api
        * Reordered the execution of execute_rommon_reset, execute_set_config_register

* iosxe/platform
    * Updated logic to handle standby scenario.

* iosxe/asr1k
    * Updated logic to handle standby scenario.

* sdk/utils
    * Modified password_recovery api
        * Moved init_connection to step 5 to handle the syslogs.

* iosxe/sdk-pkg
    * Added an api get_recovery_details to get recovery details.
    * Updated the device_rommon_boot to use the api to get details.

* nxos
    * Modified
        * Added flag to handle 'minimally-disruptive' mode for ISSU trigger in NXOS


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe/routing/configure
    * Added configure_ip_route_cache_on_interface API

* iosxe/platform
    * added 'show platform hardware qfp active feature alg statistics sip clear' api.


--------------------------------------------------------------------------------
                                    Fix/Add                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_flow_record_match_datalink
        * Added nested if statement to account for 'match datalink {field_type} vlan {direction}' command.
    * Modified configure_fnf_flow_record_match_flow
        * Added else clause to if statement block for 'match flow {flow_name}' command.
    * Added configure_flow_record_transport API
        * Added new API to configure flow record transport fields match/collect source-port/destination-port/tcp flags.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added acm merge parser
        * Added Acm merge
        * Added Acm replcae]
        * Added Acm rollback
    * Added ShowPlatformMrpMappings
        * Added  schema and parser for 'show platform mrp mappings' command.
    * Added Parser for parsers for below commands
        * Added show mrp ring <ring-id>statistics all
    * Added Parser for parsers for below commands
        * show platform software fed switch {switch_num} wdavc flows
        * show platform software fed switch {switch_num} wdavc function wdavc_ft_show_all_flows_seg_ui
    * Added ShowPlatformHardwareFedActiveQosQueueConfigInternalPortTypeRecyclePortPortNumAllAsic parser
        * Added schema and parser for 'show platform hardware fed {state} qos queue config internal port_type recycle-port port_num all asic {asic_number}''
    * Added below parser for c9550 by inheriting from c9350
        * ShowPlatformTcamUtilization
        * ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
        * ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * ShowPlatformHardwareFedQosSchedulerSdkInterface
    * Added Parser for below command
        * show tcp brief numeric
    * Modified ShowInventory
        * Added logic support if name is a digit
    * Added ShowSubsysNameIpfib
        * show subsys name ipfib
    * Added ShowIpv6VirtualReassemblyFeatures parser
        * Added schema and parser for 'show ipv6 virtual-reassembly features'
    * Added ShowPlatformStatus schema in iosxe/ie3k
        * Added parser for show platform status in iosxe/ie3k
    * Added ShowFlowMonitorCacheSortOrderSuperParser
        * show flow monitor {name} cache sort counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort counter bytes long top {value} format table
        * show flow monitor {name} cache sort counter packets long top {value} format table
        * show flow monitor {name} cache sort flow direction top {value} format table
        * show flow monitor {name} cache sort timestamp absolute {time} top {value} format table
        * show flow monitor {name} cache sort datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort datalink ethertype top {value} format table
        * show flow monitor {name} cache sort datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort datalink vlan {direction} top {value} format table
        * show flow monitor {name} cache sort ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort ipv4 tos top {value} format table
        * show flow monitor {name} cache sort ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort ipv4 version top {value} format table
        * show flow monitor {name} cache sort ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort ipv6 version top {value} format table
        * show flow monitor {name} cache sort transport tcp flags top {value} format table
        * show flow monitor {name} cache sort transport {port} top {value} format table
        * show flow monitor {name} cache sort {order} counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort {order} counter bytes long top {value} format table
        * show flow monitor {name} cache sort {order} counter packets long top {value} format table
        * show flow monitor {name} cache sort {order} flow direction top {value} format table
        * show flow monitor {name} cache sort {order} timestamp absolute {time} top {value} format table
        * show flow monitor {name} cache sort {order} datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort {order} datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink ethertype top {value} format table
        * show flow monitor {name} cache sort {order} datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink vlan {direction} top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 tos top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 version top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 version top {value} format table
        * show flow monitor {name} cache sort {order} transport tcp flags top {value} format table
        * show flow monitor {name} cache sort {order} transport {port} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderCounter
        * show flow monitor {name} cache sort {order} counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort {order} counter bytes long top {value} format table
        * show flow monitor {name} cache sort {order} counter packets long top {value} format table
        * show flow monitor {name} cache sort counter bytes long top {value} format table
        * show flow monitor {name} cache sort counter bytes layer2 long top {value} format table
        * show flow monitor {name} cache sort counter packets long top {value} format table
    * Added ShowFlowMonitorCacheSortOrderFlow
        * show flow monitor {name} cache sort {order} flow direction top {value} format table
        * show flow monitor {name} cache sort flow direction top {value} format table
    * Added ShowFlowMonitorCacheSortOrderTimestamp
        * show flow monitor {name} cache sort {order} timestamp absolute {time} top {value} format table
        * show flow monitor {name} cache sort timestamp absolute {time} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderTransport
        * show flow monitor {name} cache sort {order} transport tcp flags top {value} format table
        * show flow monitor {name} cache sort {order} transport {port} top {value} format table
        * show flow monitor {name} cache sort transport tcp flags top {value} format table
        * show flow monitor {name} cache sort transport {port} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderDatalink
        * show flow monitor {name} cache sort {order} datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort {order} datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink ethertype top {value} format table
        * show flow monitor {name} cache sort {order} datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort {order} datalink vlan {direction} top {value} format table
        * show flow monitor {name} cache sort datalink dot1q priority top {value} format table
        * show flow monitor {name} cache sort datalink dot1q vlan {direction} top {value} format table
        * show flow monitor {name} cache sort datalink ethertype top {value} format table
        * show flow monitor {name} cache sort datalink mac {destination} address {direction} top {value} format table
        * show flow monitor {name} cache sort datalink vlan {direction} top {value} format table
    * Added ShowFlowMonitorCacheSortOrderIPv4
        * show flow monitor {name} cache sort {order} ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 tos top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort {order} ipv4 version top {value} format table
        * show flow monitor {name} cache sort ipv4 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv4 protocol top {value} format table
        * show flow monitor {name} cache sort ipv4 tos top {value} format table
        * show flow monitor {name} cache sort ipv4 ttl top {value} format table
        * show flow monitor {name} cache sort ipv4 version top {value} format table
    * Added ShowFlowMonitorCacheSortOrderIPv6
        * show flow monitor {name} cache sort {order} ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort {order} ipv6 version top {value} format table
        * show flow monitor {name} cache sort ipv6 {destination} address top {value} format table
        * show flow monitor {name} cache sort ipv6 protocol top {value} format table
        * show flow monitor {name} cache sort ipv6 hop-limit top {value} format table
        * show flow monitor {name} cache sort ipv6 traffic-class top {value} format table
        * show flow monitor {name} cache sort ipv6 version top {value} format table
    * Added Parser for parsers for below commands
        * 'show flow monitor {monitor_name} cache sort application name top {top_count}',
        * 'show flow monitor {monitor_name} cache sort connection {connetion_type} counter bytes network long top {top_count}'
    * Added
        * Added schema and parser for show ip ospf neighbor summary
        * Added schema and parser for show ipv6 ospf neighbor summary
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableStatistics parser
        * Added schema and parser for cli "show platform hardware fed {state} fwd-asic insight acl-table statistics"
    * Modified ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetail parser
        * Added optional keys in schema and p15 regex for "show platform software fed {state} switch active acl info sdk detail"
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightSanetAccsecClientTable parser.
        * Added parser for cli 'show platform hardware fed switch {switch} fwd-asic insight sanet_accsec_client_table()'.
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightAccsecClientClassificationEnablement parser.
        * Added parser for cli 'show platform hardware fed switch {switch_id} fwd-asic insight accsec_client_classification_enablement()'.
    * Added Parser for show platform hardware fed {mode} qos queue stats internal port_type recycle-port port_num {port_num} asic {asic}
        * Added a new schema and parser for the show platform hardware fed {mode} qos queue stats internal port_type recycle-port port_num {port_num} asic {asic} command.
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2SwitchAttachmentCircuit parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status({sys_port_gid}).
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_switch_attachment_circuits({l2_ac_gid}).
    * Modified ShowPlatformSoftwareObjectManagerFpActiveStatistics
        * Added new cli in parser for show platform software object manager
    * Modified ShowClock
        * Added new time format parser for show clock
    * ShowConnection
        * show connection name 1.
    * ShowControllerT1
        * show controller T1
    * Modified ShowIpNatBpa
        * show ip nat bpa
    * Modified ShowIpOspfDatabaseNssa
        * show ip ospf database nssa.
    * Added ShowPlatformSoftwareFirewallRPActiveZones
        * sh ipv6 mfib FF03111 count
        * sh ipv6 mfib FF03111 1011200 count
    * Added ShowIsdnStatusSerial parser in show_isdn.py
    * Added schema and parser for cli 'show isdn status serial {interface}'
    * Added ShowMonitorEventTraceCryptoIkev2EventAll parser in show_monitor.py
    * Added schema and parser for cli 'show monitor event-trace crypto ikev2 event all'
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbDetail
        * show platform hardware qfp active feature firewall datapath scb any any any any any all any detail
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathEdm
    * 'show platform hardware qfp active feature nat datapath edm'
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathPor parser in show_platform.py
        * Added schema and parser for cli 'Schema for show platform hardware qfp active feature nat datapath port'
    * Added howPlatformHardwareQfpActiveFeatureNatDatapathMap parser in show_platform.py
        * Added schema and parser for cli 'Parser for show platform hardware qfp active feature nat datapath map'
    * Added ShowPlatformSoftwareFirewallRPActiveZones
        * show platform software firewall RP active zones
        * show platform software firewall FP active zones
    * Added ShowPlatformSoftwareWccpWebCacheCounters parser in show_platform.py
    * Added schema and parser for cli 'show platform software wccp web-cache counters'
    * ShowPolicyMapTypeInspectPmap
        * show policy-map type inspect pmap
    * Added class ShowSubsysName parser in show_subsys.py
        * Added schema and parser for cli 'show subsys name {name}'
    * Added ShowSubsysNamePgen parser in show_subsys.py
        * Added schema and parser for cli 'show subsys name pgen'
    * Modified ShowVpdnTunnelPptpAll
        * show vpdn tunnel pptp all
    * Added class ShowXdrLinecard parser in show_platform.py
        * Added schema and parser for cli 'show xdr linecard'
    * Added class ShowZonePairSecurity parser in show_paltform.py
        * Added schema and parser for cli 'show zone-pair security'

* nxos
    * Added ShowInterfaceCountersTable
        * Added  schema and parser for 'show interface counters table' command.


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowMrpPorts
        * Updated  regex pattern in ShowMrpPorts.
    * Modified show flow monitor {name} cache parser
        * added one more type of output with connection_initiator, connection_server_nw_bytes_counter, connection_client_nw_bytes_counter parameter
    * Updated ShowMerakiConnect parser
        * Added support for "VRF" field in meraki_tunnel_interface section

* nxos
    * Modified ShowInterface
        * Updated  regex pattern in ShowInterface.
        * Updated  regex pattern in ShowCdpNeighbors and ShowCdpNeighborsDetail.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Show Intrface parser
        * Added regex to match port channel.
    * Modified Show ip mroute vrf all and show ipv6 mroute vrf all
        * Added <router_id> option.

* iosxe
    * Modified ShowFlowMonitor parser
        * Modified parser for CLI
            * 'show flow monitor {name} cache format table'
    * Modified regex pattern P1 for the given ie3k output
    * Added few fields to 'show env temperature' command output to support 'Inlet Temp Sensor' and 'HotSpot Temp Sensor' temperature readings.
    * Fixed parsing of temperature thresholds to handle spaces and units correctly.
    * Updated regex patterns to ensure accurate matching of temperature readings and thresholds.
    * Modified ShowLispInstanceIdServiceStatistics
        * Made itr_map_resolvers and etr_map_servers optional in schema.
    * Modified ShowPlatformPacketTracePacket
    * 'show platform packet-trace packet all'
    * Modified ShowBgpSummarySuperParser
        * Supported more variant output
    * Modified Dir
        * Added p2_2 regex to support dir drec0 command for c9200 devices.

* viptela/show_control
    * Updated ShowControlLocalPropertiesSchema
        * Made the port_hopped key optional to accommodate various outputs

* iosxr
    * Modified ShowControllersOpticsDb
        * Fix Parser for 'show controllers optics *' to extract multi-word Vendor Name

* parser
    * Modified Show Processes Memory Doc Value ()
        * Updated doc value for "show processes memory" to match this, instead of "show switch detail"



genie.telemetry
"""""""""""""""
