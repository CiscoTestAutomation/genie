March 2023
==========

March 28 - Genie v23.3 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.3                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.3                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

If you have pyATS installed, you can use:

.. code-block:: bash

    pyats version update




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* harness
    * Modified Verifications
        * Fixed parallel verifications results rollup
    * Modified Base
        * Fixed parallel verification attribute error



genie.libs.clean
""""""""""""""""

genie.libs.conf
"""""""""""""""

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
    * Added configure_evpn_instance_vlan_based_flood_suppression
        * API for to configure evpn instance vlan based flood suppression
    * Added unconfigure_evpn_instance_vlan_based_flood_suppression
        * API to unconfigure evpn instance vlan based flood suppression
    * Added configure_authentication_control_direction
        * added api to configure authentication control-direction
    * Added unconfigure_authentication_control_direction
        * added api to unconfigure authentication control-direction
    * Added configure_authentication_open
        * added api to configure authentication open
    * Added unconfigure_authentication_open
        * added api to unconfigure authentication open
    * Add a get API to retrieve the whole MPLS forwarding-table.
    * Added configure_interface_switchport
        * API for to configure switchport on interface
    * Added configure_ptp_vlan
        * API for to configure ptp vlan on interface
    * Added unconfigure_ptp_vlan
        * API for to unconfigure ptp vlan on interface
    * modified API  unconfigure_source_template_global
        * modified api unconfigure_source_template_global to address duplicate names
    * Added configure_ipv6_traffic_filter_acl
        * API to configure ipv6 traffic-filter {acl} {direction} on vlan interface range
    * Added unconfigure_ipv6_traffic_filter_acl
        * API to unconfigure ipv6 traffic-filter {acl} {direction} on vlan interface range
    * Added configure_ip_dhcp_restrict_next_hop
        * added api to configure ip dhcp restrict-next-hop on interface
    * Added unconfigure_ip_dhcp_restrict_next_hop
        * added api to unconfigure ip dhcp restrict-next-hop on interface
    * Added configure_aaa_accounting_exec_default_start_stop_group
        * API to configure aaa accounting exec default start-stop group
    * Added unconfigure_aaa_accounting_exec_default_start_stop_group
        * API to unconfigure aaa accounting exec default start-stop group
    * Added configure_local_span_filter
        * New API to configure local span filter
    * Added unconfigure_local_span_filter
        * New API to unconfigure local span filter
    * Added configure_policy_map_with_dscp_table
        * New API to configure policy map with dscp table
    * Added configure_policy_map_with_percent
        * New API to configure policy map with percentage value
    * Added configure_policy_map_with_no_set_dscp
        * New API to configure policy map with no set dscp value
    * Added configure_service_policy_with_queueing_name
        * API to configure service policy map with queueing type
    * Added unconfigure_policy_map_with_type_queue
        * API to unconfigure policy map with queue type
    * Added configure_policy_map_with_dscp_police
        * API to configure policy map with dscp
    * Added configure_table_map
        * API to configure table map from value to to value
    * Added unconfigure_table_map
        * API to unconfigure table map from value to to value
    * Added configure_interface_monitor_session_shutdown
        * API to configure monitor session on interface by shuttingdown
    * Added configure_ip_dhcp_snooping_limit
        * New API to configure ip dhcp snooping limit rate on interface
    * Added clear_ip_bgp_ipv6_unicast
        * API for clear ip bgp ipv6 unicast {route}
    * Added configure_ip_dlep
        * added api to configure ip dlep
    * Added unconfigure_ip_dlep
        * updated api to unconfigure ip dlep
    * Added configure_physical_interface_vmi
        * added api to configure vmi interface pppoe-rar mode
    * Added config_interface_ospfv3
        * updated api to configure network, hello_interval
    * Added configure_virtual_template
        * updated api to configure authentication, load_delay, mss, mtu
    * Added execute_switch_clear_stack_mode API
        * API to execute clear stack-mode for a switch
    * Added execute_switch_role API
        * API to switch role mode for a switch
    * Added unconfigure_ipv6_pim_bsr_candidate_bsr
        * added api to unconfigure ipv6 pim bsr candidate bsr
    * Added unconfigure_ipv6_pim_bsr_candidate_rp
        * added api to unconfigure ipv6 pim bsr candidate rp
    * Added configure config_pim_acl
        * added api to configure ipv6 pim accept-register lis acl_name
    * Added unconfigure unconfig_pim_acl
        * added api to unconfigure ipv6 pim accept-register lis acl_name
    * Added configure_ipv6_mld_join_group_acl
        * added api to configure ipv6 mld join-group saddress source-lis acl_name
    * Added unconfigure_interface_datalink_flow_monitor
        * API for unconfigure datalink flow monitor
    * Added execute_clear_ip_nat_translation
        * API for clearing ip nat translation
    * Fixed configure_bgp_neighbor_filter_description
        * Fix a conditional statement
    * Added unconfigure_static_ip_route_all API
        * API to unconfigure static ip route
    * Added configure_diagnostic_monitor_syslog
        * API to enable configure diagnostic monitor syslog
    * Added unconfigure_diagnostic_monitor_syslog
        * API to disable configure diagnostic monitor syslog
    * Added unconfigure_device_classifier_command
        * API to unconfigure device classifier command
    * Added unconfigure_device_classifier_profile_command
        * API to unconfigure device classifier profile command
    * Added configure_device_classifier_command
        * API to configure device classifier command
    * Added unconfigure_device_classifier_profile
        * API to unconfigure device classifier profile
    * Added unconfigure_device_classifier_operator
        * API to unconfigure device classifier operator
    * Added configure_dscp_global
        * API to configure global dscp values
    * Added unconfigure_dscp_global
        * API to remove configuration of global dscp values
    * Added configure_flow_monitor_on_vlan_configuration API
        * API to Configure Flow Monitor on vlan configuration
    * Added unconfigure_flow_monitor_on_vlan_configuration API
        * API to Unconfigure Flow Monitor on vlan configuration
    * Added execute_license_smart_save_usage_all_file
        * API to excute license smart save usage all file
    * Added execute_more_file_count
        * API to execute more file <filepath> | count <regex>
    * Added execute_license_smart_save_usage_unreported_file
        * API to execute license smart save usage unreported file
    * Added unconfigure_dscp_radius_server
        * New API to unconfigure dscp authentication and accounting values in radius server configuration
    * Added unconfigure_dscp_radius_server_group
        * New API to unconfigure dscp authentication and accounting values in radius server group configuration
    * Added configure_mdt_auto_discovery_vxlan
        * New API to configure mdt auto discovery vxlan under vrf definition
    * Added configure_ip_dhcp_exclude_vrf
        * New API to configure ip dhcp exclude vrf on device
    * Added configure_ipv6_mld_access_group
        * New API to configure ipv6 mld access group
    * Added unconfigure_ipv6_mld_access_group
        * New API to unconfigure ipv6 mld access group
    * Added configure_ptp_announce_transmit
        * API for to configure ptp announce transmit on interface
    * Added unconfigure_ptp_announce_transmit
        * API for to unconfigure ptp announce transmit on interface
    * Added configure_ipv6_route_nexthop_vrf API
        * API to configure ipv6 route nexthop vrf
    * Added unconfigure_ipv6_route_nexthop_vrf API
        * API to unconfigure ipv6 route nexthop vrf
    * Added unconfigure_system_mtu API
        * API to unconfigure system mtu
    * Added clear_ip_eigrp_neighbor
        * API to clear ip eigrp neighbor
    * Added configure_eigrp_passive_interface API
        * API to configure passive interface in eigrp ipv4
    * Added unconfigure_eigrp_passive_interface API
        * API to unconfigure passive interface in eigrp ipv4
    * Added configure_eigrp_passive_interface_v6 API
        * API to configure passive interface in eigrp ipv6
    * Added unconfigure_eigrp_passive_interface_v6 API
        * API to unconfigure passive interface in eigrp ipv6
    * modified  configure_hsrp_interface API
        * Modification done including the HSRP ipv6 configuration under the interface
    * Added get_policy_map_interface_queue_output
        * API to get policy map queuing interfaces
    * Added
        * config_interface_ospfv3_network_type
        * unconfig_interface_ospfv3_network_type
        * config_interface_ospfv3_flood_reduction
        * unconfig_interface_ospfv3_flood_reduction
    * Added configure_ipv6_mld_snooping_enhance and uconfigure_ipv6_mld_snooping_enhance
        * API to configure mld snooping, unconfig
    * Added configure_ip_pim_ssm and unconfigure_ip_pim_ssm
        * API to configure ip pim ssm , unconfigure
    * Added unconfigure_ip_igmp_snooping_vlan_mrouter_interface
        * API to unconfigure ip igmp snooping vlan
    * Added configure_route_map_permit and unconfigure_route_map_permit
        * API to configure route map, unconfig
    * Added configure_ipv6_ospf_router_id
        * New API to configure ipv6 ospf router id
    * Added configure_macro_auto_processing_on_interface
        * New API to configure macro auto processing on device interface
    * Added unconfigure_macro_auto_processing_on_interface
        * New API to unconfigure macro auto processing on device interface
    * Added configure_switchport_trunk_pruning_vlan_except
        * New API to configure switchport trunk pruning vlan except vlan numbers
    * Added configure_vtp_trunk_interface
        * New API to configure vtp trunk interface
    * Added execute_config_confirm
        * New API to execute the config confirm
    * Added execute_device_dir_path
        * New API to execute the device dir flash for total bytes
    * Added execute_archive_config
        * New API to execute archive config on device
    * Added restore_running_config_file
        * Modified API restore running config file

* blitz
    * Made that gnmi tests are not aborted in case of an error, but are always executed until max_stream/polls_number is reached
    * Added decimal_64 type handling
    * Combined sample_interval and polls_number into single parameter named sample_poll
    * Added support for "any" operator for returned value verification.
        * If datatype is correct the test passes regardless of value.


--------------------------------------------------------------------------------
                                       ~                                        
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modify configure_nat64_prefix_stateful API
        * Modified the API by adding vrf_name parameter
    * Modify unconfigure_nat64_prefix_stateful API
        * Modified the API by adding vrf_name parameter
    * Modify configure_nat64_v6v4_static API
        * Modified the API by adding vrf_name and match_in_vrf parameters
    * Modify unconfigure_nat64_v6v4_static API
        * Modified the API by adding vrf_name and match_in_vrf parameters
    * Modify configure_nat64_v4_list_pool API
        * Modified the API by adding vrf_name and match_in_vrf parameters
    * Modify unconfigure_nat64_v4_list_pool API
        * Modified the API by adding vrf_name and match_in_vrf parameters
    * Modify configure_nat64_v4_list_pool_overload API
        * Modified the API by adding vrf_name and match_in_vrf parameters
    * Modiy uconfigure_nat64_v4_list_pool_overload API
        * Modified the API by adding vrf_name and match_in_vrf parameters
    * Modified configure_isis_with_router_name_network_entity
        * Modified api configure isis with router name network_entity, vrf and redistribute bgp
    * Modified unconfig_interface_ospfv3
        * Modified unconfig_interface_ospfv3 to add option for unconfiguring network
    * Modified configure_ip_igmp_join_group_source
        * Modified api name in configure ip igmp join group source
    * Modified unconfigure_ip_igmp_join_group_source
        * Modified api name in unconfigure ip igmp join group source
    * Modified perform_telnet
        * Fixed the API perform_telnet to handle the prompt 'Password' after sending the CLI 'enable' while performing telnet
    * Uplifted configure_radius_server
        * Uplifted the API to accommodate dscp authentication and accounting values in radius server configuration
    * Uplifted configure_radius_group
        * Uplifted the API to accommodate dscp authentication and accounting values in radius group configuration
    * Modified configure_vrf_ipv6_eigrp_named_networks
        * Modified vrf ipv6 eigrp
    * Modified perform_ssh API
        * Added hmac field in the API

* blitz
    * Fixed transaction_time for gnmi subscribe SAMPLE



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowDerivedConfigInterface
        * added couple of optional parameters.
    * Added ShowControllerEthernetController
        * show controller ethernet-controller {interface}
    * Added ShowCallHomeAlertGroup
        * show call-home alert-group
    * Added ShowCallHomeDiagnosticSignature
        * show call-home diagnostic-signature
    * Added ShowCallHomeEvents
        * show call-home events
    * Added ShowCallHomeDetail
        * show call-home detail
    * Added ShowAccessSessionInterface
        * show access-session interface {interface}
    * Added ShowIpv6MldSnoopingQuerier
        * show ipv6 mld snooping querier
    * Added show platform software fed switch {active} vp key {if_id} {vlan_id}
        * Parsre for "show platform software fed switch {active} vp key {if_id} {vlan_id}
    * Added ShowDiagnosticResultSwitchTestDetail parser
        * Parser for "show diagnostic result {switch_number} test {include} detail"
    * Added ShowPlatformSoftwareFedSwitchMatmStats Parser
        * Parser for "show platform software fed switch {mode} matm stats"
    * Added ShowAlarmProfile parser
        * parser for show alarm profile in the device
    * Added ShowAlarmSettings parser
        * parser for show alarm settings in the device
    * Added ShowFacilityAlarmStatus parser
        * parser for show facility-alarm status in the device
    * Added ShowPlatformSoftwareFedActiveVtHardwareIfId
        * show platform software fed active vt hardware if-id {if_id}
    * Added Parser ShowPlatformSoftwareInstallManagerChassisActiveR0OperationHistorySummary
        * 'show platform software install-manager chassis active r0 operation history summary'
    * Added ShowCryptoPkiTrustpoints parser
        * Parser for "show crypto pki trustpoints"
    * Modified ShowIpDhcpServerStatistics Parser
        * Parser lines added for the drop counters
    * Added ShowL2fibBridgeDomainDetail Parser
        * Parser for show l2fib bridge-domain {bd_id} detail
    * Added ShowTemplateInterfaceSourceUser
        * show template interface source user {user}
    * Added ShowTemplateServiceSourceUser
        * show template service source user {user}
    * Added ShowAutoConfigurationTemplateBuiltIn
        * show auto configuration template builtin
    * Added ShowFlowMonitor
        * "show flow monitor" for 9500 devices
    * Added ShowPlatformSoftwareFedSwitchQosPolicyTargetStatus
        * show platform software fed switch {switch} qos policy target status
    * Added ShowBgpL2vpnEvpnEviRouteType
        * show bgp l2vpn evpn evi {evi_id} route-type {route_type}
    * Added ShowPlatformSoftwareFedSwitchActiveVpSummaryInterfaceIfId
        * show platform software fed switch active vp summary interface if_id {if_id}
    * Added ShowPlatformSoftwareFedIfmInterfaces Parser
        * Parser for "show platform software fed {switch} active ifm interfaces vlan"
        * Parser for "show platform software fed active ifm interfaces vlan"
    * Added ShowL2fibOutputList Parser
        * Parser for "show l2fib output-list"
    * Added ShowL2fibOutputListId Parser
        * Parser for "show l2fib output-list {output_id}"
    * Added ShowVRFIPv6
        * show vrf ipv6 {vrf}
        * To verify the IPv6 configuration on device
    * Added ShowPlatformSoftwareFedActiveQosPolicySummary
        * Parser for show platform software fed active qos policy summary

* iosxr
    * Added ShowDhcpIpv4ProxyBinding
        * Parser for cli 'show dhcp ipv4 proxy binding'
        * Parser for cli 'show dhcp ipv4 proxy binding interface {interface_name}'
    * Added ShowDhcpIpv4ServerBinding
        * Parser for cli 'show dhcp ipv4 server binding'
        * Parser for cli 'show dhcp ipv4 server binding interface {interface_name}'
    * Added ShowPtpPlatformServo
        * added new parser for cli 'show ptp platform servo'
    * Added ShowPlatformHwFedActiveQosQStatsInternalCpuPolicer
        * added new parser for cli 'show platform hardware fed switch active qos queue stats internal cpu policer'
    * Modified ShowIsisNeighbors
        * Parser for 'show isis instance {process_id} neighbors'

* added showplatformsoftwarefedswitchactivematmadjacenciesadjkey
    * show platform software fed switch active matm adjacencies adjkey {adj_key}


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowIpIgmpSnoopingGroupsVlanHosts
        * show ip igmp snooping groups vlan <vlan> <group> hosts
    * Added ShowIpIgmpSnoopingGroupsVlanSources
        * show ip igmp snooping groups vlan <vlan> <group> sources
    * Added
        * show platform hardware fed switch {switch} fwd-asic resource utilization
    * Added ShowL2vpnEvpnEviDetail
        * show l2vpn evpn evi detail
        * show l2vpn evpn evi <evi> detail
    * Added ShowL2vpnEvpnSummary
        * show l2vpn evpn summary
    * Added ShowIsisTeapp
    * Added ShowIsisTeappPolicy


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added
        * show stack-power load-shedding
        * show switch stack-mode
    * Modified ShowCryptoIke2SaDetail
        * Updated regex pattern <r8> to support not just IP addresses for Remote id
    * Modified ShowL2vpnServiceAll
        * Updated schema to allow for incomplete configuration with no interface
    * Modified ShowIpRoute
        * Updated regex patterns to allow next_hop vrf to contains '-' in vrf name
    * Modified ShowNetconfYangStatus
        * Updated schema to accommodate the latest release output.
        * Updated parser for latest release output
    * Fix ShowL2vpnServiceAll
        * CLI output was modified
        * show l2vpn service all
        * show l2vpn service interface {interface}
        * show l2vpn service name {name}
        * show l2vpn service xconnect all
        * show l2vpn service xconnect interface {interface}
        * show l2vpn service xconnect name {name}
    * Modified ShowPowerInlineDetail
        * Fixed 'operational_status' regular expression and added unit test
    * Modified ShowPowerInlineUpoePlus
        * Fixed regular expression and added unit test
    * Modified ShowIpVerifySource
        * Added mac_address optional key, fixed regex and unit test
    * Modified ShowBgpNeighbor
        * Update parsing to support VRF in bgp neighbors cli command instead of always setting 'default' VRF (parser p2_3)
    * Modified ShowFlowMonitorCache
        * Modified code to match protocol entires
    * Modified ShowMonitorCaptureBuffer
        * Modified code to match ipv4 and ipv6 protocol entires
    * Modified ShowPlatformHardwareFedSwitchQosDscpcosCounters
        * Modified code to get parse output for HA and standlone devices
    * Modified ShowRunningConfigNve
        * Updated the SVI schema for DHCP related data
        * Added regex <p3_16> and <p3_17>
    * Modified ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface
        * Updated command to match previous implementation for c9600 and fix fuzzy command search
    * Modified ShowLispService
        * Added ipv6 regex
    * Modified ShowLispSiteDetail
        * Added ipv6 regex
    * Modified ShowLispIpv6Publication
        * Added ipv6 regex
    * Modified ShowLispPublisherSuperParser
        * Added ipv6 regex
    * Modified ShowLispPublicationPrefixSuperParser
        * Added ipv6 regex
    * Modified ShowLispSubscriberSuperParser
        * Added ipv6 regex
    * Modified ShowLispIpv4PublisherRloc
        * Added ipv6 regex
    * Modified ShowLispInstanceIdService
        * Added ipv6 regex
    * Added ShowLispIpv6PublisherRloc
        * Added ShowLispIpv6PublisherRloc parser
    * Modified ShowParserStatistics
        * Changed date, time_with_seconds, time_zone from schema to Optional.
        * Updated regex pattern p7 to accommodate various outputs.

* iosxr
    * Modified ShowVrfAllDetail
        * Updated regex pattern p1 to allow '' in vrf name
    * Modified ShowOspfv3Neighbor
        * Modified up_time as Optional parameter in schema.
    * Modified ShowPolicyMapInterface
        * Added Optional parameter queue_exceed_packets to schema
        * Added Optional parameter queue_exceed_bytes to schema
        * Added Optional parameter queue_exceed_rate to schema
        * Added Optional parameter policing_statistics section to schema
        * Added Optional parameter policed_confirm to schema
        * Added Optional parameter policed_exceed to schema
        * Added Optional parameter policed_violate to schema
        * Added Optional parameter policed_and_dropped to schema
        * Added Optional parameter wred_profile section to schema
        * Added Optional parameter red_transmitted to schema
        * Added Optional parameter red_random_drops_packets to schema
        * Added Optional parameter red_random_drops_bytes to schema
        * Added Optional parameter red_maxthreshold_drops to schema
        * Added Optional parameter red_ecn_marked_transmitted to schema
        * Modified P2 pattern to support the format 'Bundle-Ether203 input SERVICE-BPS'
        * Modified P5 pattern to support the format 'Class IPV4-PACKET-IS-00'
    * Modified ShowBfdSession
        * Added <p5> pattern to match 'Gi0/0/0/1.10        192.168.1.2     0s               10s(2s*5)        INIT'
    * Modified ShowMplsLdpDiscovery
        * Added code to support 'passive' and 'active/passive' state
        * Added 'targeted_hellos' section as optional parameter to schema under 'local_ldp_identifier'.
        * Added 'xmit' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'recv' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'active' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'passive' as optional parameter under 'targeted_hellos' section to schema.
        * Added 'active/passive' as optional parameter under 'targeted_hellos' section to schema.


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPolicyMapInterface parser
        * Added new keys 'burst_bytes' and 'rate_bps'


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified show cts interface
        * show cts interface {interface} added.


--------------------------------------------------------------------------------
                                       ~                                        
--------------------------------------------------------------------------------


