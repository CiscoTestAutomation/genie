May 2025
==========

 - Genie v25.5 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.5 
    ``genie.libs.health``, v25.5 
    ``genie.libs.clean``, v25.5 
    ``genie.libs.conf``, v25.5 
    ``genie.libs.filetransferutils``, v25.5 
    ``genie.libs.ops``, v25.5 
    ``genie.libs.parser``, v25.5 
    ``genie.libs.robot``, v25.5 
    ``genie.libs.sdk``, v25.5 
    ``genie.telemetry``, v25.5 
    ``genie.trafficgen``, v25.5 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* harness/discovery
    * Updated exception for trigger load.



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean
    * recovery
        * update the recovery process to use state machine for bringing device to enable state
    * iosxe/connect
        * Password Recovery did not kick in if the fallback credential did not work.
    * recovery/iosxe
        * update the recovery process to update grub_boot_image if there is grub activity pattern
    * iosxe/stages
        * Handled the variable total_size when the size of the filedata returns
    * recovery
        * update the recovery process to use multi threading and handling grub menu for device recovery

* iosxe
    * Added new dialog to handle reload patterns


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added exception handler for enable authentication failure to trigger recovery.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* conf
    * NXOS
        * Added ParsedInterfaceName class to handle interface name parsing


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified neighbor.py
        * Added new class IfNeighbor to configure interface as neighbor in bgp
    * Modified bgp.py
        * Added new managed attribute interface_neighbors to support interface neighbor configuration
    * Modified interface.py
        * Added support to configure mac address under port-channel interfaces
    * Modified test_interface.py and test_bgp.py
        * Added new unittest for new support



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* filetransferutils
    * moved the base fileutils logic to filetransferutils pkg in genielibs.



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * cat9k/c9500/rev1
        * Fixed DevX importer issue for C9500 stackable platforms.
            * Added rp_pid leaf in show inventory to correctly extract and map PID.



genie.libs.robot
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genierobot
    * Modified
        * Several GenieRobot keywords no longer call robot's pass_execution or fail



genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* updated api unit tests
    * IOSXE
        * Updated the following API unit tests with the latest unit testing methodology
            * configure_aaa_accounting_connection_default_start_stop_group_tacacs_group
            * configure_aaa_accounting_identity_default_start_stop_group
            * configure_aaa_accounting_system_default_start_stop_group_tacacs_group
            * configure_aaa_authentication_enable_default_group_enable
            * configure_aaa_authentication_login_default_group_local
    * IOSXE
        * Updated unittests to new testing method
            * configure_mac_acl
            * configure_scale_ipv6_accesslist_config
            * configure_standard_acl
            * configure_type_access_list_action
            * delete_configure_ip_acl
            * delete_configure_ipv6_acl
            * delete_mac_acl
            * remove_acl_from_interface
            * unconfig_extended_acl_with_evaluate
            * unconfig_extended_acl_with_reflect
            * unconfig_ip_tcp_mss
            * unconfig_refacl_global_timeout
        * Removed the mock yaml under 'unconfigure_access_list_deny' as we do not have any API for it.
    * IOSXE
        * Updated the following API unit tests with the latest unit testing methodology
            * configure_SVI_Autostate
            * configure_SVI_Unnumbered
            * unconfigure_static_ip_route_all
            * configure_aaa_accounting_connection_default_start_stop_group_tacacs_group
            * configure_boot_manual
    * IOSXE
        * Updated the following API unit tests with the latest unit testing methodology
            * configure_radius_attribute_policy_name_globally
            * configure_radius_attribute_policy_name_under_server
            * configure_radius_interface
            * unconfigure_aaa_accounting_dot1x_default_start_stop_group
        * unconfigure_aaa_accounting_network_default_start_stop_group
    * IOSXE
        * Updated the following API unit tests with the latest unit testing methodology
            * configure_aaa_accounting_connection_default_start_stop_group_tacacs_group
            * configure_aaa_authorization_config_commands
            * configure_aaa_authorization_exec_default_group_if_authenticated
            * configure_aaa_authorization_network_default_group
            * configure_mab_eap_on_switchport_mode_access_interface
    * IOSXE
        * Updated unittests to new testing method
            * configure_as_path_acl
            * configure_extended_acl
            * configure_filter_vlan_list
            * configure_interface_ipv6_acl
        * Removed the mock yaml under 'configure_extended_acl_deny' as we do not have any API for it.

* cleaning api ut's
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's
            * configure_ipv6_subnet_to_sgt_mapping
            * configure_ipv6_to_sgt_mapping
            * configure_sap_pmk_on_cts
            * disable_cts_enforcement_vlan_list
            * enable_cts_enforcement_vlan_list
    * Iosxe
        * Updated with latest UT method to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's
            * remove_default_ipv6_sgacl
            * unconfigure_cts_aaa_methods
            * unconfigure_cts_enforcement_interface
            * unconfigure_cts_enforcement_logging
            * unconfigure_cts_manual
            * unconfigure_cts_role_based_monitor
            * unconfigure_cts_role_based_permission
            * unconfigure_cts_role_based_permission_default
            * unconfigure_host_ip_to_sgt_mapping
            * unconfigure_interface_cts_role_based_sgt_map
            * unconfigure_ip_role_based_acl
            * unconfigure_ip_role_based_acl
            * unconfigure_ip_subnet_to_sgt_mapping_vrf
            * unconfigure_ip_to_sgt_mapping_vrf
            * unconfigure_ipv6_subnet_to_sgt_mapping
    * Iosxe
        * ACL
            * Updated with latest UT mathod to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT method to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's

* iosxe/rommon
    * Utils
        * update the send break boot to handle login creds

* updated unittests
    * IOSXE
        * Updated below API unit tests with the latest unit testing methodology
            * configure_router_bgp_synchronization
            * unconfigure_bgp_auto_summary
            * unconfigure_bgp_log_neighbor_changes
            * unconfigure_bgp_redistribute_internal
            * unconfigure_bgp_redistribute_static
    * IOSXE
        * Updated below API unit tests with the latest unit testing methodology
            * unconfigure_redestribute_ospf_metric_in_bgp
            * unconfigure_router_bgp_maximum_paths
            * unconfigure_router_bgp_network_mask
            * unconfigure_router_bgp_synchronization
            * configure_datalink_flow_monitor
    * IOSXE
        * Updated below API unit tests with the latest unit testing methodology
            * unconfigure_datalink_flow_monitor
            * unconfigure_mac_address_table_notification_change
            * enable_http_server
            * set_clock_calendar
            * configure_call_home_alert_group

* iosxe
    * Modified verify_pattern_in_show_logging
        * Modified the API to search pattern from entire show logging output.
    * Added Support for Destination username pattern for copy_file_with_scp
    * Modified configure_route_map_permit to add vrf argument
        * Added Vrf for set vrf clause
    * Modified API unconfigure_ipv6_pim_bsr_candidate_rp
        * Added support for priority in the unconfiguration command.
        * Included CLI commands
    * Modified API `unconfigure_ipv6_pim_bsr_candidate_bsr`
        * Added support for `priority` in the unconfiguration command.
        * Included CLI commands
            * `no ipv6 pim bsr candidate bsr 20002 priority 254`
            * `no ipv6 pim bsr candidate bsr 20001`
            * `no ipv6 pim bsr candidate bsr 30001`
    * Modified configure_tacacs_server
        * Modified the API to use hostname instead of IP address as host for tacacs server configuration
        * Added support for TLS (Transport Layer Security) configuration options
            * TLS port number
            * TLS idle timeout
            * TLS connection timeout
            * TLS retries
            * TLS client and server trustpoints
            * IPv4 and IPv6 source interfaces for TLS
            * IPv4 and IPv6 VRF forwarding for TLS
            * TLS server identity matching for DNS-ID, IP address, and SRV-ID

* sdk-pkg
    * rommon/util
        * Added prompt recovery to support the state transition.

* linux
    * Modified scp API in linux
        * Handled first-time SSH connection prompt
        * Added support for 'Are you sure you want to continue connecting' dialog

* wsim
    * sdk-pkg
        * Removed execute and added sendline/expect because vsta_app would


--------------------------------------------------------------------------------
                          Unconfigure_Exclude_Ip_Dhcp                           
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
         Unconfigure_Interface_Ip_Dhcp_Relay_Information_Option_Vpn_Id          
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
          Unconfigure_Interface_Ip_Dhcp_Relay_Source_Interface_Intf_Id          
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
              Unconfigure_Interface_Range_Dhcp_Channel_Group_Mode               
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                    Unconfigure_Ip_Dhcp_Client_Vendor_Class                     
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                            Unconfigure_Ip_Dhcp_Pool                            
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added unconfigure_flow_exporter_from_monitor
        * API for unconfigure_flow_exporter_from_monitor
    * Added configure_spanning_tree_extend_system_id
        * API to configure spanning-tree extend system id
    * Added API execute_diagnostic_start_module_port
        * Added API to execute_diagnostic_start_module_port
    * Added configure_app_hosting_docker_with_run_opts
        * API to configure app hosting docker with run opts
    * Added verify_backplane_optical_port_interface_config_media_type
        * API to verify backplane/optical port on 10G interface.
    * Added configure_app_hosting_docker
        * API to configure app hosting docker
    * Added API default_policy_map to deafult a policy-map on the device
    * ie3k
        * Added new api execute_copy_verify
    * Added configure_logging_host_ipv6
        * API to configure logging host ipv6
        * API to unconfigure logging host ipv6
    * Added configure_rep_preempt_and_block
        * API to configure rep preempt and block
    * Added API configure_file_verify_auto
        * API to configure file verify auto
    * Added API unconfigure_file_verify_auto
        * API to unconfigure file verify auto
    * Added ip pim send-rp-announce Loopback0 scope 10
    * Added configure_app_hosting_custom_profile
        * API to configure app hosting custom profile
    * Added API configure_sd
        * API to configure sdflash
    * Added API unconfigure_sd
        * API to unconfigure sdflash
    * Added API get_logging_message_time
        * Added API to get_logging_message_time
    * Added configure_app_hosting_vlan
        * API to configure app hosting vlan
    * Added configure_app_hosting
        * API to configure app hosting
    * Added enable_app_hosting_verification
        * API to enable app hosting verification
    * Added API default_attribute_service_map
        * API to default parameter-map type on the device
    * Added  API configure_ipv6_logging_with_discriminator
        * API to Configure IPv6 logging with discriminator on the device.
    * Added API configure_ipv6_pim_on_interface

* api
    * NXOS
        * Added breakout_interface_names

* iosxe/c9200cx
    * Added configure_management_ip
        * New API to configure management IP

* nxos
    * Added
        * verify_ping API that validates Ping at given device to given address


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* * iosxe
    * cat9k
        * c9500
            * C9500-24Y4C
                * Inherited API's to configure and unconfigure the ignore startup config

* iosxe
    * ie3k
        * configure
            * Added 'configure and unconfigure ignore startup config' API under ie3k platform
        * Verify
            * Added 'verify_current_image' and 'verify_ignore_startup_config' Api's


--------------------------------------------------------------------------------
                         Configure_Dhcp_Pool_Dns_Server                         
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                      Configure_Dhcp_Pool_Ipv6_Domain_Name                      
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                    Configure_Ipv6_Dhcp_Client_Vendor_Class                     
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                 Configure/Configure_Ipv6_Dhcp_Relay_Option_Vpn                 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
               Configure_Ipv6_Dhcp_Relay_Destination_Ipv6Address                
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
               Configure_Ipv6_Dhcp_Relay_Source_Interface_Intf_Id               
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                Configure_Ip_Acl                                
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                           Configure_Ip_Acl_With_Any                            
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                               Configure_Ip_Sgacl                               
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                               Configure_Ipv6_Acl                               
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                   Configure_Mac_Access_Group_Mac_Acl_In_Out                    
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                         Unconfigure_Ip_Dhcp_Pool_Host                          
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                     Unconfigure_Ip_Dhcp_Restrict_Next_Hop                      
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                     Unconfigure_Ip_Dhcp_Snooping_Database                      
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                Unconfigure_Ip_Dhcp_Snooping_Information_Option                 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
        Unconfigure_Ip_Dhcp_Snooping_Information_Option_Allow_Untrusted         
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
     Unconfigure_Ip_Dhcp_Snooping_Information_Option_Allow_Untrusted_Global     
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                           Clear_Dhcpv4_Server_Stats                            
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                             Clear_Ip_Dhcp_Binding                              
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                         Clear_Ip_Dhcp_Snooping_Binding                         
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                       Clear_Ip_Dhcp_Snooping_Statistics                        
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                      Clear_Ip_Dhcp_Snooping_Track_Server                       
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                            Clear_Ipv6_Dhcp_Binding                             
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                   Configure_Access_Map_Match_Ip_Mac_Address                    
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                          Configure_Acl_Protocol_Port                           
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                           Configure_Acl_With_Ip_Any                            
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                         Configure_Acl_With_Src_Dsc_Net                         
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                               Configure_Arp_Acl                                
--------------------------------------------------------------------------------



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowProcesses
        * Added support for the option 'location'
    * Modified ShowL2vpnXconnectDetail
        * Added support for parsing the line "Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=1,Rx=1)"
    * Modified ShowIpSourceBinding
        * Modified regex pattern to support lease if infinite

* iosxe
    * Modified ShowLispInstanceIdService
        * Modified regex pattern to support a variant of the output
    * Fixed parser ShowIpv6PimBsrElection
        * Added support for parsing "This system is the Bootstrap Router (BSR)"
        * Updated schema to include 'bsr_system' under 'bsr' for Bootstrap Router detection
        * Enhanced parser to capture and store the 'bsr_system' information
    * Modified parser ShowIpMroute
        * Updated regex pattern p3_1 to accomodate various outputs
        * Added optional key 'iif_mdt_ip' to schema
    * Modified ShowDeviceTrackingDatabaseMacMacDetails parser
        * Modified entries regex pattern
    * Modified ShowDeviceTrackingDatabaseMac parser
        * Modified parser and schema to support device tracking database mac for different vlans
    * Fix parser ShowDeviceTrackingDatabaseMacDetails
        * New revision handles handles extracting primary vlan
    * Fixed ShowPlatformSoftwareFedSwitchActiveSecurityFedSisfStatistics parser
        * Added support command should work for all the platforms.
        * Added clear command support for 'show platform software fed switch {active} security-fed sisf statistics {clear}'.
    * Modified ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel
        * Added new cli command 'show platform software fed switch active ifm interfaces virtualportgroup'
        * Added new cli command 'show platform software fed active ifm interfaces virtualportgroup'
        * Added new cli command 'show platform software fed switch {mode} ifm interfaces ethernet'
        * Added new cli command 'show platform software fed active ifm interfaces ethernet'
        * Added new cli command 'show platform software fed switch active ifm interfaces loopback'
        * Added new cli command 'show platform software fed active ifm interfaces loopback'
    * Modified ShowPlatformSoftwareFedSwitchActiveIFMMappingsEtherchannel
        * Added command parameter to support new way of assiging the variables to the command
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel
        * show command "show platform software fed switch active ifm interfaces detail" was hitting this parser
    * Modified Parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfPorts
        * Supported CLIs
            * `show platform hardware fed {switch} {state} fwd-asic insight vrf_ports_detail`
            * `show platform hardware fed {switch} {state} fwd-asic insight vrf_ports`
        * Introduced `state` as a variable for flexibility.
    * Modified Parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfRouteTable
        * Supported CLI
            * `show platform hardware fed {switch} {state} fwd-asic insight vrf_route_table`
        * Introduced `state` as a variable for flexibility.
    * Modified ShowPowerInlineModule
        * Modified the regex pattern
    * Modified ShowLicenseAll
        * Enhanced the parser code to handle the trust_code_installed field more effectively
    * Modified ShowVersion
        * Added handling for merged boot line on c9500x
    * Fixed parser ShowLispMapCacheSuperParser
        * Added support for parsing more date and time formats
    * Modified ShowPolicyMapTypeInspectZonePair
    * Added show policy-map type inspect zone-pair in-self cli
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandErspan parser
        * Modified parser for CLI
            * 'show platform hardware fed switch {switch_type} fwd-asic insight l2_mirror_command_erspan({mirror_gid})',
            * 'show platform hardware fed {switch} {switch_type} fwd-asic insight l2_mirror_command_erspan({mirror_gid})'
    * Added  ShowPlatformHardwareQfpActiveFeatureBfdDatapathSession parser
        * Added schema and parser for 'show platform hardware qfp active feature bfd datapath session'
    * Fixed parser ShowPlatformSoftwareFedMatmMacTable parser
        * Modified the parser to handle the output of the command "show platform software fed switch {switch_var} mac address-table" correctly.
        * Modified schema and parser to handle the output of the command "show platform software fed switch {switch_var} mac address-table" correctly.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveSecurityFedArpIf parser
        * Added schema and regex pattern p9 and p10 to match the output of the command.
    * Fixed parser ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id
        * Added "show platform software fed switch {switch_num} ifm if-id {if_id}" to the command
    * Fixed  ShowPlatformHardwareFedSwitchActiveFwdAsicInsightRoutes parser
        * Fixed parser to work on any switch id
    * Fixed  ShowPlatformSoftwareFedSwitchActiveOifsetUrid parser
        * made the switch_id optional and made optional in schema
    * Fixed  ShowPlatformSoftwareFedSwitchActiveOifset parser
        * Fixed parser to work on any switch id
    * Fixed ShowPlatformSoftwareFedSwitchActiveIpMfibVrf parser
        * Fixed schema and added regex to match output for any number of asics
    * Modified ShowLicenseTechSupport
        * Modified the regex pattern
    * Fixed ShowPlatformSoftwareFedQosInterfaceSuperParser parser
        * Added new way of parsing cli with command option
    * Added  ShowPlatformHardwareQfpActiveFeatureAlgStatistics parser
        * Added schema and parser for 'show platform hardware qfp active feature alg statistics'
    * Modified ShowXfsuStatus
        * Added optional argument 'xfsu_platform_status' to capture "xFSU PLATFORM Status Stack reloaded, all nodes connected"
        * Made other variables optional to avoid KeyError
    * cat9k
        * fixed parser ShowL2ProtocolTunnelSummary - initialised port_dict
    * Modified ShowIpDhcpSnooping
        * Modified the regex pattern
    * Modified ShowPlatformSoftwareFedActiveMonitor
        * Made "encap" optional
    * Fix parser ShowCtsPolicyServerDetails
        * Modified regex pattern
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjects parser
        * Added support cli to work on all platforms
    * Modified ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObject parser
        * Added support cli to work on all platforms

* <nxos>
    * Modified ShowBgpSessions
    * Updated regex pattern <p6_1> to accommodate port-channel neighbors

* nxos
    * Modified the DPU name and model in show module
        * DPU name has changed from SAM to DPU.
        * DPU module has changed from Service Accelerator Module to DPU.
    * Show module values are taken from non rv1/show_platform.py
        * Updated the rv1/show_platform.py and show_platform.py same for 'show module'
    * Fixed the 'show inventory' slot for FAN
        * FAN slot is returning as None as the definition there twice.

* viptela
    * Modified ShowSystemStatus parser to cast engineering_signed to boolean.
    * Added logic to safely convert string true/false values to Python bool.
    * Ensures schema validation passes for engineering_signed field.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareFedSwitchL2SwitchMacTable parser.
        * Added parser for cli show platform hardware fed switch {switch_no} fwd-asic insight l2_switch_mac_table({vlan_or_switch_gid}).
    * Added Parser 'ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfHostRoute'
        * 'show platform hardware fed {switch} {state} fwd-asic insight vrf_host_routes'
    * Added Parser 'ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfForUsRoute'
        * 'show platform hardware fed {switch} {state} fwd-asic insight vrf_for_us_routes'
    * Added Parser 'ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfNextHop'
        * 'show platform hardware fed {switch} {state} fwd-asic insight vrf_next_hops'
    * Added ShowPlatformSoftwareMplsFpActiveEos
        * Added schema and parser for 'show platform software mpls fp active eos'
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSmtp
        * show platform hardware qfp active feature alg statistics smtp
        * show platform hardware qfp active feature alg statistics smtp {clear}
    * Added ShowEthernetCFMEFDMeps parser
        * Added schema and parser for 'show ethernet cfm efd meps'
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedDhcpSnoopVlanDetail parser
        * Added schema and parser for 'show platform software fed switch {active} security-fed dhcp-snoop vlan {vlan} detail' command.
    * Added ShowPlatformDhcpSnoopingClientStats parser
        * Added schema and parser for 'show platform dhcp snooping client stats' command.
    * Added ShowIpv6PimNeighborIntf
        * Added schema and parser for 'Parser for show ipv6 pim neighbor {interface}'
    * Added 'show crypto pki crls' parser.
    * Added parser for cli 'show crypto pki crls'.
    * Added 'show crypto pki crls download' parser.
    * Added parser for cli 'show crypto pki crls download'.
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathStats
        * Added schema and parser for 'show platform hardware qfp active feature nat datapath stats'
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallMemory
        * Added schema and parser for 'show platform hardware qfp active feature firewall memory'
    * Added ShowIpNatTranslationUdpTotal
        * show ip nat translation udp total
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfProperties
        * Added schema and parser for'show platform hardware fed switch active fwd asic insight vrf properties'
    * Added ShowPlatformHardwareQfpActiveInterfaceIfName
        * Added schema and parser for 'show platform hardware qfp active interface if-name Port-channel1'
    * Added ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroup
        * Added schema and parser for
            * 'show platform software fed {switch} {state} ipv6 mld snooping group'
    * Added show loggging count
    * Added ShowPlatformSoftwareNatFpActiveQfpStats parser
        * Added schema and parser for 'show platform software nat fp active qfp-stats'
    * Added ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage parser
        * Added rv1 schema and parser for 'show platform software access-security table usage'
    * Added ShowPlatformHostAccessTableIntf parser
        * Added rv1 schema and parser for 'show platform host access-table <interface>'
    * Added ShowIpVirtualReassemblyInterface parser
        * Added schema and parser for the command 'show ip virtual-reassembly {interface}'
    * Added ShowPlatformSoftwareFedSwitchActiveIpTypeMfibVrfDetail parser
        * Added schema and parser for cli 'show platform software fed {switch} {active} {ip_type} mfib vrf {vrf_name} {group} {source} detail'
    * Added ShowIpDhcpSnoopingBinding parser
        * Added latest ShowIpDhcpSnoopingBinding parser in rv1 and reverted the changes in original file.
    * Added ShowMerakiConfigMonitor parser
        * Added schema and parser for cli 'show meraki config monitor'
    * Added ShowMerakiConfigUpdater parser
        * Added schema and parser for cli 'show meraki config updater'
    * Added ShowMerakiMigration parser
        * Added schema and parser for cli 'show meraki migration'
    * Added ShowRunningConfigFlowMonitorExpand parser
        * Added schema and parser for 'show running-config flow monitor {monitor_name} expand' command.
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSunrpc
        * show platform hardware qfp active feature alg statistics sunrpc
        * show platform hardware qfp active feature alg statistics sunrpc {clear}
    * Added ShowPlatformSoftwareNatFpActiveInterface
    * 'show platform software nat fp active interface'
    * Added ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadBalanceMacAddr parser
        * Added schema and parser for CLI commands
            * 'show platform software fed {switch} {switch_type} etherchannel {eth_channel_id} load-balance mac-addr {src} {dst}'
            * 'show platform software fed {switch_type} etherchannel {eth_channel_id} load-balance mac-addr {src} {dst}'
    * Added ShowPlatformHardwareQfpActiveFeatureNatDataStats
        * Added 'show platform hardware qfp active feature nat data stats' command and schema for the command.
    * Added ShowPlatformSoftwareFedSwitchIpv6MldSnoopingGroupsVlan
        * Added schema and parser for
            * 'show platform software fed {switch} {state} ipv6 mld snooping groups vlan {vlan_id}'
    * Added ShowPlatformSoftwareMemoryDatabaseForwardingManager
    * 'show platform software memory database forwarding-manager {slot} active brief | include {options}'
    * Added ShowPlatformSoftwareFedOifsetL2m parser
        * Added schema and parser for CLI
            * 'show platform software fed {switch} {module} oifset l2m'
            * 'show platform software fed {switch} {module} oifset l2m hash {hash_data}'
    * Added  ShowPlatformHardwareFedSwitchActiveFwdAsicInsightAclEthPortSpecialLkupOrder
        * Added schema and parser for cli "show platform hardware fed switch active fwd-asic insight acl_eth_port_special_lkup_order()
    * Added ShowPlatformSoftwareFedActiveSdmFeature parser
        * Added schema and parser for 'show platform software fed active sdm feature'
    * Fixed ShowSdmPreferred parser
        * Added schema and parser for 'show sdm preferred' to handle qos_acl_in and qos_acl_out as optional fields
    * Added  ShowPlatformHardwareFedSwitchFwdAsicInsightL3mGroups parser
        * Added schema and parser for cli "show platform software fed switch {swith_id} fwd-asic insight l3m-groups"
    * Added ShowPlatformSoftwareFedSecurityArpSnoopVlan parser
        * Added schema and parser for 'show platform software fed switch security-fed arp-snoop vlan {vlan}'
    * Added ShowPlatformSoftwareFedSecurityArpSnoopStats parser
        * Added schema and parser for 'show platform software fed switch security-fed arp-snoop statistics'
    * Added ShowApphostingUtil parser
        * Added schema and parser for 'show app-hosting utilization appid {appid}' command.
    * Added ShowHwModuleSubslotAllOir
    * show hw-module subslot all oir
    * Added ShowIpSlaConfiguration parser
        * Added schema and parser for cli 'show ip sla configuration'
    * Added ShowIpNatTranslationFilterRange
    * show ip nat translation filter range inside global 5.1.1.2 5.1.1.2 total
    * Added ShowIpSubscriberMac parser
        * Added schema and parser for 'show ip subscriber mac {mac_address}'
    * Added  ShowParameterMapTypeSubscriberAttributeToService parser
        * Added schema and parser for cli "show parameter-map type subscriber attribute-to-service name {template_name}"
    * Added ShowFlowInterface parser
        * Added schema and parser for 'show flow interface' command.
    * Added ShowPlatformSoftwareFedSwitchFnfProfileMapsDump parser
        * Added schema and parser for cli 'show platform software fed switch {switch_num} fnf profile-maps-dump'
    * Added show platform software fed switch acl man key profile egress all
    * Added ShowSoftwareAuthenticityKeys schema and parser
        * Added schema and parser for show software authenticity keys
    * Added ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailedAsicAll parser
        * Added parser for cli "show platform software fed {switch} {mode} qos interface {interface} ingress sdk detailed asic {asic}"
        * Added parser for cli "show platform software fed {mode} qos interface {interface} ingress sdk detailed asic {asic}"
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroupMembers
        * Added schema and parser for
            * 'show platform hardware fed switch active fwd-asic insight l3m_group_members'
            * 'show platform hardware fed switch active fwd-asic insight l2m_group_members'
    * Added ShowPlatformSoftwareInterfaceFpActive
        * Added schema and parser for 'show platform software interface fp active name Port-channel32'
    * Added ShowIpv6MfibVrfSummary parser
        * added schema and parser for cli 'show ipv6 mfib vrf {vrf_name} summary'
    * Added show platform software fed switch acl man key profile ingress all
    * Added ShowPlatformSoftwareMulticastStats parser
        * Added schema and parser for 'show platform software multicast stats'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2mGroupMembers parser
        * Added schema and parser for cli "show platform hardware fed {switch} {module} fwd-asic insight l2m_group_members"
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL3mGroupMembers parser
        * Added schema and parser for cli "show platform hardware fed {switch} {module} fwd-asic insight l3m_group_members"
    * Added ShowPlatformHardwareQfpActiveFeatureIpsecState
        * Added schema and parser for 'show platform hardware qfp active feature ipsec state'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitL2 parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_l2({sys_port_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitL2Detail parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_l2_detail({l2_ac_gid}).

* iosxr
    * Added ShowControllersOpticsDb
        * show controllers optics {port} db
    * Added ShowProcessesBlocked
        * show processes blocked
    * Added ShowInventoryRaw
        * show inventory raw
    * Added ShowControllersOpticsFecThresholds
        * show controllers optics {port} fec-thresholds
    * Added ShowControllersOpticsBreakoutDetails
        * show controllers optics {port} breakout-details
    * Added ShowControllersOpticsDwdmCarrierMap
        * show controllers optics {port} dwdm-carrier-map

* linux
    * Added CurlMinusV parser class
        * Parse "curl -V"



genie.telemetry
"""""""""""""""
