May 2023
==========

May 30 - Genie v23.5 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.5                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.5                          |
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

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* generic
    * Added configure_management clean stage


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean
    * Updated VerifyRunningImage clean stage to allow user to ignore flash directories
    * Added clean stage for cat9k to ignore flash directories by default

* iosxe
    * Modified the logic to pick the golden_image if the clean fails with a crash image.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified TunnelInterface class
        * Updated logic to support any tunnel mode



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* filetransferutils.server
    * Modified fileserver to log IP, port and path

* filetransferutils.fileserver.http
    * Modified HTTP fileserver to log sending/receiving files at debug level



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified Interface class, using CLI commands for parsers instead of hardcoded classes



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_monitor_erspan_source_interface
        * API to configure monitor erspan source on interface
    * Added unconfigure_monitor_erspan_source_interface
        * API to unconfigure monitor erspan source on interface
    * Added execute_install_application_bootflash
        * added api to install application from bootflash
    * Added
        * verify_igmp_group_exists
        * verify_igmp_group_not_exists
        * verify_mld_group_exists
        * verify_mld_group_not_exists
        * unconfigure_default_vxlan
        * unconfigure_mdt_auto_discovery_vxlan
    * Added clear_ipv6_rip
        * API for to clear ipv6 rip process on device
    * Added configure_sdm_prefer
        * added api to configure sdm prefer
    * Added configure_default_spanning_tree_mode
        * added api to configure default spanning-tree mode
    * Added unconfigure_logging_monitor_debugging
        * added api to unconfigure logging monitor debugging
    * Added unconfigure_ip_on_interface
        * New API to unconfigure IP on an interface
    * Added configure_extended_acl
        * API to configure extended acl on device
    * Added configure_eigrp_redistribute_bgp
        * API to configure redistribute bgp routes into eigrp
    * Added configure_router_isis
        * API to configure router isis with parameters on device
    * modified  configure_sks_client API
        * Modification for sks-client as skip-client as per IOS behavior change.
    * modified  unconfigure_sks_client API
        * Modification for sks-client as skip-client as per IOS behavior change.
    * Added unconfigure_interface_switchport_port_security
        * added api to unconfigure interface switchport port-security
    * Added configure_switchport_protected
        * added api to configure interface switchport protected
    * Added unconfigure_switchport_protected
        * added api to unconfigure interface switchport protected
    * Added configure_interface_keepalive
        * added api to configure interface keepalive
    * Added configure_interface_l2protocol_tunnel
        * added api to configure interface l2protocol tunnel
    * Added unconfigure_interface_l2protocol_tunnel
        * added api to unconfigure interface l2protocol tunnel
    * Added configure_app_hosting_appid_trunk_port
        * API to configure app-hosting appid
    * Added configure_app_hosting_appid_docker
        * API to configure app-hosting appid resource docker
    * Added configure_app_hosting_resource_profile
        * API to configure app-hosting appid resource custom profile
    * Added execute_guestshell_enable
        * API to enable guestshell
    * Added execute_test_platform_hardware_fantray
    * Added execute_app_hosting_appid
        * API to configure app-hosting appid
    * Added unconfigure_app_hosting_appid
        * API to unconfigure app-hosting appid
    * Added configure_interface_ip_wccp
        * API to configure interface ip wccp
    * Added configure_static_nat_route_map_no_alias_rule and unconfigure_static_nat_route_map_no_alias_rule
        * API to configure and unconfigure static NAT route-map rule
    * Added configure_access_session_macmove_deny
        * New API to configure access-session mac-move deny
    * Added unconfigure_access_session_macmove_deny
        * New API to unconfigure access-session mac-move deny
    * Added configure_access_session_macmove_deny_uncontrolled
        * New API to configure access-session mac-move deny uncontrolled
    * Added unconfigure_access_session_macmove_deny_uncontrolled
        * New API to unconfigure access-session mac-move deny uncontolled
    * Added configure_mac_address_table_aging
        * API to configure mac address table aging
    * Added unconfigure_mac_address_table_aging
        * API to unconfigure mac address table aging
    * Added unconfigure_interface_duplex_mode
        * API to unconfigure interface duplex mode
    * Added configure_boot_system_image_file
        * API to configure boot system image file
    * Added unconfig_cns_agent_password
        * New un configure cns agent password
    * Added config_ip_domain_lookup
        * New API to configure ip domain lookup
    * Added unconfig_ip_domain_lookup
        * New API to configure ip domain lookup
    * Added configure_default_vtp_version
        * API to configure default vtp version
    * Added def configure_vlan_name
        * API to configure vlan name
    * Added configure_flow_monitor_sampler_fnf_sampler
        * API to configure {protocol_type} flow monitor {name} sampler fnf_sampler {flow}
    * Added unconfigure_mac_access_group_mac_acl_in_out
        * API for unconfigure the mac access group acl name on interface
    * Added configure_ip_acl
        * API for configre the ip acl details
    * Added delete_configure_ip_acl
        * API for delete the ip acl details
    * Added delete_configure_ipv6_acl
        * API for delete the ipv6 acl details
    * Added configure_spanning_tree_portfast_on_interface
        * API for configure spanning tree portfast on interface
    * Added unconfigure_access_map_match_ip_address_action_forward
        * API for unconfigure access map for vacl
    * Added unconfigure_filter_vlan_list
        * API for delete the filter vlan list
    * Added unconfigure_interface_switchport_trunk_allowed_vlan API
        * API to unconfigure switchport mode trunk allowed vlan to the interface
    * Added configure_access_session_acl_default_passthrough api
        * Api to configure access-session acl default passthrough
    * Added unconfigure_access_session_acl_default_passthrough api
        * Api to unconfigure access-session acl default passthrough
    * Added configure_ipv6_flow_monitor
        * New API to configure ipv6 flow monitor
    * Added unconfigure_ipv6_flow_monitor
        * New API to unconfigure ipv6 flow monitor
    * Added configure_bgp_vpn_import
        * API to configure vpn import under router bgp
    * Added configure_isis_metric_style
        * API to configure IS-IS metric-style and passive-interface
    * Added configure_mdt_auto_discovery_inter_as
        * API to configure mdt auto-discovery inter-as
    * Added clear_lne_ftpse_all
        * API to clear lne ftpse all
    * Added configure_route_map_match_length
        * API to configure route-map match length on device
    * Added unconfigure_snmp_server_engineid
        * API to unconfigure the snmp server engineID
    * Added unconfigure_license_smart_usage_interval
        * API to unconfigure license smart usage interval
    * Added unconfigure_smart_transport_url
        * API to unconfigure smart transport url
    * Added config_smart_transport_url
        * API to configure smart transport url
    * Added configure_snmp_if_index_on_ospfv3_process_id
        * API to configure snmp if index on ospf process
    * Added configure_interface_ospfv3_ipsec_ah API
        * API to configure ospfv3 ipsec authentication on interface
    * Added configure_interface_ospfv3_ipsec_esp API
        * API to configure ospfv3 ipsec encryption  on interface
    * Added configure_ospfv3_ipsec_esp API
        * API to configure ospfv3 ipsec authentencryption
    * Added configure_ospfv3_ipsec_ah
        * API to configure ospfv3 ipsec authentication
    * Added configure_arp_access_list_permit_ip_host
        * API to configure arp access-list with ip host
    * Delete API configure_ip_igmp_static_group
        * Deleted API configure_ip_igmp_static_group from /iosxe/multicast/configure.py file
        * The same API is present under /iosxe/interface/configure.py file
    * Added shutdown_ipv6_eigrp_instance
        * API to shutdown EIGRP IPv6 router
    * Added unshutdown_ipv6_eigrp_instance
        * API to unshutdown EIGRP IPv6 router
    * Added configure_ip_multicast_routing_distributed
        * API to configure distributed multicast routing
    * Added unconfigure_ip_multicast_routing_distributed
        * API to unconfigure distributed multicast routing
    * Added configure_ospfv3_address_family
        * API to configure address-framily on OSPFv3 router
    * Added clear_policy_map_counters
        * API to clear counters of policy-map
    * Added configure_ip_forward_protocol_nd
        * API for configure_ip_forward_protocol_nd
    * Added unconfigure_ip_forward_protocol_nd
        * API for unconfigure_ip_forward_protocol_nd
    * Added clear_ipv6_traffic
        * API to clear ipv6 traffic
    * modified  configure_isis_network_type API
        * Added nsf and metric-style for isis router.
    * modified  configure_isis_with_router_name_network_entity API
        * Added bfd,adjacency,nsf and metric-style for isis router name.
    * Added execute_set_platform_hardware_fed_qos
        * API to set platform hardware feq qos
    * Added configure_flow_exporter
        * API to configure flow exporter parameters
    * Added unconfigure_outside_static_nat_rule
        * API to unconfigure static NAT rule
    * Added unconfigure_nat_pool_address
        * API to unconfigure NAT pool address
    * Added configure_mac_address_change_interval
        * API to configure_mac_address_change_interval
    * Added unconfigure_mac_address_change_interval
        * API to unconfigure_mac_address_change_interval
    * Added unconfigure_mac_address_table_aging_time_vlan
        * API to unconfigure_mac_address_table_aging_time_vlan
    * Added configure_interface_default_snmp
        * API to configure_interface_default_snmp
    * Added configure_license_smart_transport_callhome
        * added API for configure smart transport callhome
    * Added configure_netconf_yang
        * added API for configure_netconf_yang
    * Added unconfigure_netconf_yang
        * added API for unconfigure_netconf_yang
    * Added configure_telemetry_ietf_subscription
        * added API for configure_telemetry_ietf_subscription
    * Added unconfigure_telemetry_ietf_subscription
        * added API for unconfigure_telemetry_ietf_subscription
    * Added verify_flood_suppress
        * API to verify the flood suppress for the given evi
    * Added clear_controllers_ethernet_controller
        * API to clear controllers ethernet-controller
    * Added configure_logging
        * added api to configures logging {mode}
    * Added unconfigure_logging
        * added api to unconfigures logging {mode}
    * Added configure_interface_authentication_violation
        * added api to configures authentication violation
    * Added unconfigure_interface_authentication_violation
        * added api to unconfigures authentication violation
    * Added configure_thousandEyes_application
        * API to configure thousandEyes application on device

* api to execute test platform hardware chassis fantray

* added unconfigure_interface_ospfv3_ipsec_ah api
    * API to unconfigure ospfv3 ipsec authentication on interface

* added unconfigure_interface_ospfv3_ipsec_esp api
    * API to unconfigure ospfv3 ipsec encryption  on interface

* added unconfigure_ospfv3_ipsec_esp api
    * API to unconfigure ospfv3 ipsec authentencryption

* added unconfigure_ospfv3_ipsec_ah
    * API to unconfigure ospfv3 ipsec authentication

* added clear_ospfv3_process_all api
    * API to clear ospv3 process for all process

* added unconfigure_ospfv3_authentication_null
    * API to unconfigure ospfv3 authentication null command from interface

* nxos
    * Updated _prepare_issu
        * Added use_kstack option to filetransfer for ISSU image copy
    * Updated _perform_issu
        * Updated ISSU impact only check to prevent disruptive ISSU when non-disruptive is set
            * Improved upgrade_will_be_disruptive regex
    * Updated TriggerIssu
        * Added step validation to testcases in TriggerIssu


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* blitz
    * Fix rpcverify to handle key values with forward slash.
    * Set GNMI autovalidate to False by default.
    * Fixed ntp_server verification for GNMI STREAM

* iosxe
    * Modified unconfigure_crypto_key
        * Fixed the pattern in Dialog section of the API
    * Modify unconfigure_logging_buffered
        * added log_type optional variable
    * Modify configure_datalink_flow_monitor
        * added flow_name, direction variables
    * Modified configure_nat_pool and unconfigure_nat_pool
        * API to configure extended acl on device
    * Added configure_ptp_priority
        * made 'priority1' and 'priority2' as optional variables
    * Modified get_neighbor_count
        * API for get the neighbor count value
    * Fixed get_firmware_version API
        * Replaced 'fw' with 'fw_version' for key in output from 'show firmware version all'
    * Modify configure_policy_map_on_device
        * Add if condition for set {match_mode} {match_packets_precedence}
    * Modify clear_flow_monitor_statistics API
        * Modified the API by adding monitor_name as argument and switch as optional
    * Modified execute_clear_ip_nat_translation
        * Added conditional statements to cover more commands
    * Modified configure_dhcpv6_guard_policy
        * Added device_role more options to condition statement
    * Fix configure_hqos_policer_map
        * Add if condition for police cir percent {policer_percent_val} conform-action transmit
    * Modified configure_control_policies
        * Fixed the API configure_control_policies to configure only event and match options and only action and action number
    * Added `configure_management_credentials` and `configure_management_vrf` APIs
    * Added option to configure hostname for `configure_management` API
    * Modify configure_system_disable_password_recovery_switch_all API
        * Modified the API by adding switch and switch_number as an optional argument
    * Modify unconfigure_system_disable_password_recovery_switch_all API
        * Modified the API by adding switch and switch_number as an optional argument
    * Modify configure_system_ignore_startupconfig_switch_all API
        * Modified the API by adding switch and switch_number as an optional argument
    * Modify uconfigure_system_ignore_startupconfig_switch_all API
        * Modified the API by adding switch and switch_number as an optional argument
    * Modified configure_eigrp_networks
        * Added option to configure passive interfaces
    * Modified enable_ipv6_eigrp_router
        * Added option to configure router ID
    * Modified configure_ip_unnumbered_on_interface
        * Added support for IPv6
    * Modified configure_bandwidth_remaining_policy_map
        * Added option to configure percentage of bandwidth
    * Modified config_interface_ospfv3_network_type
        * Added support for ip_version 'both'
    * Modified unconfig_interface_ospfv3_network_type
        * Added support for ip_version 'both'
    * Modified configure_physical_interface_vmi
        * Made 'mode_op' argument optional
    * Fix restore_running_config
        * Add handling for delete_after parameter and fix behavior change
    * Modify configure_nat_overload_rule
        * added overload optional variable
    * Modify configure_static_nat_outside_rule
        * added more optional variables to support l4 configuration
    * configure_nat_pool
        * added more optional variables to support netmask, prefix-length
    * Modified unconfigure_mac_global_address_table_notification_change
        * API modified to execute command based on size and interval input
    * Modified configure_default_mac_global_address_table_notification_change
        * API modified to execute command based on size and interval input
    * Updated configure_license_smart_transport_smart
        * updated API for configure smart transport smart
    * Modified configure_shape_map
        * Fixed the API by making "queue_name" argument optional and add new optional argument as "policy_name"
    * Modified configure_interface_interfaces_on_port_channel
        * Fixed the API configure_interface_interfaces_on_port_channel for if condition where list lenght was against 2 for index 3

* modify unconfigure_datalink_flow_monitor
    * added flow_name, direction variables

* genric
    * Updated verify_current_image with new argument to ignore flash directories

* iosxe/cat9k
    * Added verify_current_image API, ignoring flash directories by default



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowIpIgmpSnooping
        * Added 'ip_address' and 'state' as Optional parameter to schema
        * Modified pattern <p10> to match 'Switch-querier enabled, address XXX.XXX.XXX.XXX, currently running'
    * Modified ShowEnvironment
        * Updated regex pattern <p6> to accommodate various outputs.
    * Modified ShowModule
        * Updated p4 regex pattern to handle slot in case the serial number doesnt start with letters.

* iosxe
    * Modified ShowAAACacheGroup
        * fixed username regex pattern to handle special characters
    * Modified ShowCispInterface
        * Added support for parsing Auth State
    * Modified ShowFipsStatus
        * made sesa_ready as optional and added reg ex pattern to match switch and stack fips status
    * Modified ShowRunInterface
        * added switchport_trunk_native_vlan optional key
    * Modified ShowVersion
        * Update schema for show version to support older IOS devices
            * 'gigabit_ethernet' interfaces is now an optional key
    * Modified ShowCtsRoleBasedSgtMapAll
        * Added optional parameters 'total_l3if' and 'total_vlan'.
    * Enhanced ShowDeviceTrackingDatabaseDetails
        * Updated optional keys 'creating' and 'tentative' in schema
    * Added ShowLispServiceDatabase
        * Fix for "UnboundLocalError local variable 'lisp_id_dict' referenced before assignment"
    * Added ShowClnsTraffic
        * Fix for "UnboundLocalError local variable 'isis_dict' referenced before assignment"
    * Modified ShowPlatformSoftwareFedSwitchActivePtpDomain
        * Added few schema kesy to grep optional information.
    * Modified ShowPlatformSoftwareAuditSummary
        * Modified schema to support standalone output
    * Modified ShowStandbyBrief
        * Modified this PARSER to capture all the ipv6 entry from the output of command "show standby brief"
        * Saparate the ipv4 and ipv6 dictionary by "interface" and "ipv6_interface" name
        * change the schema for interface as "Any()"
    * Modified ShowOspfv3vrfNeighbor
        * changed vrf ID to be string instead of  integer
        * change regexp pattern
        * vrf_id was not sent as argument
    * Modified ShowBgpDetailSuperParser
        * Fix regex pattern for Extended Community to match dot
    * Modified ShowCdpInterface
        * Fix p0 regex pattern
    * Modified ShowInventoryRaw
        * Updated regex pattern <p1> to accommodate plus sign
    * Modified ShowOspfv3Neighbor
        * Updated regex pattern p2 to accommodate various outputs
    * Modified ShowOspfv3InterfaceSchema
        * Changed state, transmit_delay, retransmit, state, dead, hello, priority to optional
        * Added optional keys cost_hysteresis and neighbor_cost
    * Modified ShowOspfv3Interface
        * Modified regex patterns p1_1, p1_3, p1_4 and p1_15 to accommodate various outputs
        * Added parsing for cost_hysteresis and neighbor_cost
    * Modified ShowDlepNeighborsSchema
        * Made dlep_server, sid optional
        * Added dlep_local optional key
    * Modified ShowDlepNeighbors
        * Modified regex patterns to accommodate various inputs
    * Modified ShowDlepClientsSchema
        * Made dlep_server key optional
        * Modified dlep_client key
    * Modified ShowDlepClients
        * Updated regex patterns to accommodate various inputs
    * Modified ShowCispSummary
        * modified parser to handle cisp enabled, running state
    * Modified ShowL2vpnEvpnDefaultGatewayDetailSchema
        * Made eth_tag as optional parameter to support ShowL2vpnEvpnDefaultGateway
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Modified parser to match sub interfaces and unit test added
    * Modified ShowL2vpnEvpnEviDetail
        * Made 'mac_routes' and 'mac_ip_routes' as optional. Added unit test.
    * Modified ShowTemplateBindingTarget
        * Fixed regular expression and unit test added
    * Modified ShowIdpromInterface
        * parsing more information from the output
    * Modified ShowL2fibBridgeDomainDetail Parser
        * Fixed p10 regex pattern
    * Modified ShowDerivedConfigInterface
        * Added some more parsing capabilities
    * Modified ShowIpNatTranslations
        * Fixed parser to hadle sigle table entry for show ip nat translations
    * Modified ShowIpHttpServerAll
        * Fix p21_3, p21_5, p21_9 regex
    * Modified ShowPlatformSudiCertificateNonce
        * Updated pattren <p5> to accommodate other outputs
    * Modified ShowPolicyMap
        * Added rate key under policy and added unit test.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Fix regex pattern to match sub interface
    * Modified ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * Fix regex pattern to match sub interface
    * Modified ShowBgp
        * Added support for parser show bgp {address_family} evi {evi}
    * Modified ShowDeviceSensor
        * Fixed Regex patterns p1 and p2
    * Modified ShowDeviceTrackingCountersInterface
        * Added optional key "reason"
    * Modified ShowDeviceTrackingCountersVlan
        * Added optional key "reason"
    * Modified ShowPlatformSoftwareFedActiveAclInfoSummary
        * added 'feature' key as Optional and added unit test. New change in 17.12
    * Modified ShowControllerEthernetController
        * Modified cli as show controllers ethernet-controller {interface} previously it is like show controller ethernet-controller {interface}. Due to controller getting error as ambiguous command.
    * Modified ShowIpDhcpSnoopingBinding
        * added 'show ip dhcp snooping binding interface {interface}'
        * added 'show ip dhcp snooping binding {mac}'
        * added 'total_bindings' key to parser total number of bindings
    * Modified ShowPlatformSoftwareWiredClientSwitchR0.
    * modified the parser file show_platform.py.
    * Modified ShowAccessSession.
    * modified the parser file show_access_session.py.
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesAdjkey
        * Added "show platform software fed active matm adjacencies adjkey {adj_key}"
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmAdjacenciesVlan
        * Added "show platform software fed active matm adjacencies vlan {vlan_id}"
    * Modified ShowIdpromTanSchema and ShowIdpromTanParser
        * Modified schema class to change revision_num type from int to str
        * Modified parser class to store revision_num as str
        * Modified parser class p3 regex pattern for revision_num to accept hex values with '\w+'.

* common
    * Modified interface conversion method
        * Added `ignore_case` option to match interface name case insensitive

* iosxr
    * Modified ShowIsisInterface
        * Added <r63> pattern to match 'Measured Delay           Min- Avg- Max- usec'
        * Added <r63> pattern to match 'Normalized Delay         Min- Avg- Max- usec'
        * Added 'measured_delay' parameter as optional parameter to schema
        * Added 'normalized_delay' parameter as optional parameter to schema
    * Modified ShowIsisDatabaseDetail
        * Added 'mt_srv6_locator' as Optional parameter to schema
        * Added 'locator_prefix', 'locator_prefix_length', 'd_flag', 'metric', and 'algorithm' parameters inside 'mt_srv6_locator' in schema
        * Added <r25> pattern to match 'SRv6 Locator   MT (IPv6 Unicast) fc00c0001001/48 D0 Metric 0 Algorithm 0'
    * Added ShowMkaPolicy
        * Added parser for show mka policy
    * Modified ShowRouteIpv6
        * Added behaviour as Optional parameter to schema.
        * Modified pattern <p2> to match 'L    fc00c0001001/64, SRv6 Endpoint uN (PSP/USD)'
        * Modified pattern <p3> to match '[0/0] via ffff0.0.0.0 (nexthop in vrf SRV6_L3VPN_BE), 230919'

* modified the showplatformsoftwarewiredclientswitchr0 regex pattern to proper output.

* modified the showaccesssession to match when there is no session exist.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPerformanceMeasurementResponderCounters
        * show performance-measurement responder counters interface
        * show performance-measurement responder counters interfaces name {name}
    * Added ShowPerformanceMeasurementResponderInterfaces
        * show performance-measurement responder interfaces
        * show performance-measurement responder interfaces name {name}
    * Added ShowPerformanceMeasurementResponderSummary
        * show performance-measurement responder summary
    * Added ShowInterfacesCapabilities
        * parser for show interfaces {interface} capabilities
    * Added ShowPlatformSoftwareIgmpSnoopingGroupsCount
        * parser for ShowPlatformSoftwareIgmpSnoopingGroupsCount
    * Added ShowPlatformSoftwareMldSnoopingGroupsCount
        * parser for ShowPlatformSoftwareMldSnoopingGroupsCount
    * Added ShowVlanBrief
        * show vlan brief
    * Added ShowCryptoMap
        * parser for show crypto map
    * Added ShowAccessSessionMacDetails
        * parser for show access-session mac {mac} details
        * show access-session mac {mac} details switch {mode} {rp_slot}
        * show access-session interface {interface} details switch {mode} {rp_slot}
    * Added ShowIpHttpServerAll
        * parser for show ip http server all
    * Added ShowIpHttpServerSecureStatus
        * parser for show ip http server secure status
    * Modified ShPlatformSoftwareFedActiveVpSummaryInterfaceIf_id
        * Added 'switch' and 'mode' input variables to support switch command
    * Modified ShowFlowMonitorCache
        * Added 'ip_tos' optional key to grep ip tos
    * Added  ShowPlatformSoftwareBpCrimsonStatistics Parser
        * Parser for "show platform software bp crimson statistics"
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Local Parser
        * Parser for "show platform software node cluster-manager switch {mode} B0 local"
    * Added ShowSdwanServiceChainDatabase parser
        * Parser for "show platform software sdwan service-chain database"
    * Added ShowIdpromTan for 9500X
    * Added ShowIpv6NdRoutingProxy  parser
        * Parser for "show ipv6 nd routing-proxy"
    * Added ShowBgpL2vpnEvpnSummary
        * parser for show bgp l2vpn evpn summary
    * Added ShowIpVerifySource for c9300
        * parser for show ip verify source
    * Added ShowVersionMode
        * parser for show version {mode}
        * parser for show version {switch} {sw_number} {route_processor} {mode}
    * Added ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed Parser
        * Parser for show platform software fed {switch} {mode} qos interface {interface} ingress npi detailed
    * Added ShowPlatformSoftwareFedSecurityFedIpsgIfId
        * show platform software fed {switch} {mode} security-fed ipsg if-id {if_id}
        * show platform software fed {mode} security-fed ipsg if-id {if_id}
    * Added ShowIpv6EigrpTopologyEntrySchema
        * show ipv6 eigrp topology {ipv6_subnet}
    * Added ShowPlatformHardwareQfpStatisticsDropClear
        * show platform hardware qfp {status} statistics drop clear
    * Added ShowPlatformSoftwareAuditSummary
        * added parser for show platform software audit summary
    * Added ShowL2vpnEvpnDefaultGateway
        * parser for show l2vpn evpn default-gateway
    * Added ShowHardwareLedPortMode Parser
        * Parser for show hardware led port {port} {mode}
    * Added ShowCispRegistrations Parser
        * Parser for "show cisp registrations"
    * Added ShowLldpNeighborsInterfaceDetail
        * show lldp neighbors {interface} detail
    * Added ShowAdjacencyInterfaceDetail
        * show adjacency interface detail
        * show adjacency interface <interface> id <id> detail
        * show adjacency interface <interface> id <id> prefix <prefix> detail
    * Added ShowAdjacencyVlanLinkDetail
        * show adjacency vlan <id> detail
        * show adjacency vlan <id> prefix <prefix> detail'
        * show adjacency vlan <id> prefix <prefix> link protocol <protocol> detail
    * Added ShowAppHostingDetailAppid
        * parser for show app-hosting detail appid {appid}
    * Added ShowMplsTrafficEngTopology
        * parser for show mpls traffic-eng topology
    * Added ShowIpIgmpSnoopingVlan Parser
        * Parser for "show ip igmp snooping vlan {vlan}"
    * Added ShowPlatHardFedActiveQosQueueStatsOqMulticastAttach
        * show platform hardware fed active qos queue stats oq multicast attach
    * Modified ShowCryptoIkev2SaDetail parser
        * IOS Change in output syntax "Quantum-Safe Encryption using PPK is enabled" insted "Quantum Resistance Enabled"
    * Added ShowPost
        * 9300 parser for 'show post'
    * Added ShowXfsuStatus
        * parser for show xfsu status
    * Added ShowGracefulReload
        * parser for show graceful-reload
    * Added ShowFlowMonitorCheck
        * show flow monitor
    * Added ShowCryptoIpsecSaInterface Parser
        * Parser for show crypto ipsec sa interface {interface}
    * Added new parser 'show device-sensor details'
    * Added ShowBeaconAll
        * Parser for show beacon all to check the beacon status.
    * Added ShowAppHostingResource
        * parser for show app-hosting resource
    * Added ShowSpanningTreeSummaryTotals
        * parser for show spanning-tree summary totals

* iosxr
    * Added ShowFrequencySynchronizationInterfaces
        * Added new parser for cli show frequency synchronization interfaces
        * Added new parser for cli show frequency synchronization interfaces {interface}
    * Added ShowRunSectionMacAddress
        * Parser for cli 'show running-config | section mac address'
    * Added ShowBgpVrfAfPrefix Parser
        * Parser for "show bgp vrf {vrf_name} {address_family} {prefix}"
        * Parser for "show bgp {address_family} vrf {vrf_name} {prefix}"
    * Added ShowBgpVrfAfPrefixDetail Parser
        * Parser for "show bgp vrf {vrf_name} {address_family} {prefix} detail"


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMfib
        * show ip mfib vrf {vrf}
            * Add if condition to handle the 'NA' as output
    * Modified ShowPlatformSoftwareFedSwitchMatmStats
        * added support for 'show platform software fed active matm stats'


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowDiagnosticPost parser
        * added parser for show diagnostic post



genie.telemetry
"""""""""""""""""
