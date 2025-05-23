June 2023
=========

June 27 - Genie v23.6
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.6                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.6                          |
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

* genie.harness
    * Fixed discovery for datafiles that are using non-pickable values



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe/cat9k
    * Fixed the rommon boot clean stage by adding optional ether_port arg.

* generic
    * Modified copy_to_linux clean stage
        * Fix copy operation when local filesystem is used
    * Modified copy_to_device clean stage
        * Support dynamic http file server copy
            * Use dynamic http file server if origin.hostname is not specified
            * Add connection_alias for use with dynamic http file copy
    * Modified connect clean stage
        * Added `alias` option to specify connection alias to use



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
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* genie.libs.robot
    * Modified execution logic to ensure processors are executed



genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* nxos
    * Modified TriggerIssuLxc and TriggerIssuNative
        * modified args to handle `,` in case of multiple images
        * fixed `filetransfer` variable to be initialzed outside of if loop in case `self.device` already has the necessary `filetransfer_attributes`

* iosxe
    * Modified configure_ipv6_multicast_routing
        * Added vrf support to config api
    * Modified unconfigure_ipv6_multicast_routing
        * Added vrf support to unconfig api
    * Updated configure_pppoe_enable_interface
        * updated api to configure_pppoe_enable_interface
    * Updated configure_virtual_template
        * updated api to configure_virtual_template
    * Added configure_dialer_interface
        * added api to configure_dialer_interface
    * Modified config_vlan_range
        * API for config_vlan_range
    * Modified unconfig_vlan_range
        * API for unconfig_vlan_range
    * Modified configure_flow_monitor_cache_entry
        * Added option to configure exporter {exporter_name}
    * Modified configure_policy_map
        * added priority_level, bandwidth_percent, bandwidth_remaining_percent, police_cir_percent options
    * Modified configure_no_keepalive_intf
        * added optional variables 'keepalive_period' and 'no_switchport'
    * Modified configure_interface_ipv6_verify_unicast_source
        * added optional variables 'no_switchport'
    * Modified configure_ipv6_multicast_routing and unconfigure_ipv6_multicast_routing
        * added 'vrf_name' optional variable
    * Modified configure_ospf_internal_external_routes_into_bgp
        * added 'metric' optional variable to support metric configuration
    * Added unconfigure_port_channel_ip api
        * API to unconfigure interface Port-channel cli
    * Added execute_debug_ip and execute_no_debug_ip api
        * API to execute debug ip protocol
    * Added configure_ip_ssh_version and unconfigure_ip_ssh_version api
        * API to configure and unconfigure ip ssh version
    * Modified execute_format api
        * API modified to handle format file system type
    * Modified get_traceroute_ipv6 api
        * API modified command parser
    * Modified configure_ldra_interface API
        * Modified the if conditions to configure policy and interface_id over interface with or without vlan_id
    * Modified configure_ospf_networks
        * added optional variable 'vrf_name' to handle vrf
    * Modified configure_shape_map
        * added optional variables 'shape_average_percent', 'random_detect_type', discard_class_value'
    * Modified configure_stack_power_switch_power_priority  and unconfigure_stack_power_switch_power_priority
        * Fixed the API to handle power priority with default vlaues.
    * Modified configure_stackpower_stack_switch_standalone and unconfigure_stackpower_stack_switch_standalone
        * Fixed the API to handle stack config and standalone config based on inputs.
    * Deleted configure_stack_power_switch_standalone and configure_stack_power_switch_no_standalone
        * Deleted APIs which functionality is handled by other APIs.
    * Modified exclude_ip_dhcp
        * added optional 'high_ip' variable to configure high end ip range
    * Modified configure_ospfv3
        * Added if condition and no functionality change
    * Modified `get_bgp_rt5_community_paths_label` API
        * Removed continue statement from determining if prefix is same as ip

* blitz
    * Added possibility to create custom verifiers and encoders when using GNMI
    * Made some of the dictionaries like 'returns' into Objects to make work with it easier
    * Simplified GNMI Subscription verification code
    * Added static types to functions to make work with it easier
    * Got rid of eval() function in opt_fields verification
    * Fix to handle leaf list return values for GNMI auto validation.

* utils
    * Fix copy_from_device.
        * Passing local_ip to get_mgmt_ip_and_mgmt_src_ip_addresses
    * Fix get_mgmt_ip_and_mgmt_src_ip_addresses.
        * Return the mgmt_ip based on mgmt_src_ip optional argument


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added configure_pim_register_source
        * configures specified interface as source interface for pim messages
    * Added unconfigure_pim_register_source
        * unconfigures specified interface as source interface for pim messages
    * Added configure_interface_monitor_session_shutdown_erspan_dest
        * added api to configure monitor session on device by doing shut of the erspan destination interface
    * Added configure_interface_monitor_session_mtu
        * added api to configure monitor session on device by setting destination mtu
    * Added configure_interface_monitor_session_no_mtu
        * added api to configure monitor session on device by setting destination no mtu
    * Added configure_call_home_profile
        * added api to configure call home profile
    * Added remove_static_route_all
        * API for remove_static_route_all
    * Added configure_interface_isis_network
        * API to configure interface isis network type
    * Added configure_ip_msdp_peer
        * API to configure ip msdp peer
    * Added configure_ip_msdp_cache_sa_state
        * API to configures ip msdp cache-sa-state
    * Added configure_interface_tunnel_mode_ipsec and unconfigure_interface_tunnel_mode_ipsec
        * API to configure and unconfigure tunnel mode ipsec
    * Added configure_evpn_ethernet_segment
        * API to configure l2vpn evpn ethernet segment
    * Added enable_dhcp_compatibility_suboption and disable_dhcp_compatibility_suboption
        * API to configure and unconfigure DHCP compatibility suboption
    * Added configure_interface_evpn_ethernet_segment
        * API to configure interface evpn ethernet-segment
    * Added configure_isis_nsf_xfsu
        * added api to configure isis nsf xfsu
    * Added execute_reload_fast
        * added api to configure configure reload fast and enhanced
    * Added configure_ip_arp_inspection_filter
        * New API to configure ip arp inspection filter
    * Added unconfigure_ip_arp_inspection_filter
        * New API to unconfigure ip arp inspection filter
    * Added unconfigure_arp_access_list
        * New API to unconfigure arp access-list
    * Modified configure_hqos_policer_map
        * New API to configure hqos policer-map to include policy cir value
    * Added clear ppp all API
        * API to clear ppp all
    * Added configure_portchannel_dpi_algorithm API
        * API to configure port channel portchannel dpi algorithm
    * Added unconfigure_portchannel_dpi_algorithm API
        * API to unconfigure port channel portchannel dpi algorithm
    * Added execute_set_fnf_debug
        * API to set platform software trace fed switch active fnf debug
    * Added execute_set_fnf_verbose
        * API to set platform software trace fed switch active fnf verbose
    * Added redistribute_route_metric_vrf_green API
        * API to redistribute route metric vrf green
    * Added configure_mld_version
        * API to configure mld version
    * Added configure_ipsec_ike_sa_strength_enforcement
        * Api to configure ipsec ike sa strength enforcement
    * Added unconfigure_ipsec_ike_sa_strength_enforcement
        * Api to unconfigure ipsec ike sa strength enforcement
    * Added configure_policy_map_class_parameters
        * added api to configure policy-map with police command
    * Added unconfigure_policy_map_class_parameters
        * added api to unconfigure police and set commands under policy-map
    * Added unconfigure_policy_map_class
        * added api to unconfigure police map class under policy-map
    * Added unconfigure_ospf_from_interface
        * API to unconfigure ospf from interface
    * Added hw_module_switch_usbflash_security_password
        * API to execute hw-module switch {switch_number} usbflash1 security {action} password {pwd}
    * Added configure_acl_with_ip_any
        * API to configure access-list {acl_name} {action} ip any any
    * Added configure_netconf_yang_intelligent_sync and unconfigure_netconf_yang_intelligent_sync
        * API to configure and unconfigure netconf-yang cisco-ia intelligent-sync
    * Added configure_enable_cisp
        * API to configure enable cisp
    * Added unconfigure_enable_cisp
        * API to unconfigure_enable_cisp
    * Added unconfigure_pvlan_primary API
        * API to unconfigure private vlan primary and private vlan association
    * Added unconfigure_pvlan_type API
        * API to unconfigure private vlan community and isolated
    * Added set_platform_soft_trace_debug
        * added api to execute set platform software trace aaa-acct debug
    * Added configure_queue_sub_interface
        * added api to configure queue sub_interface propagation
    * Added clear_authentication_session
        * New API to clear all authenticated sessions
    * Added configure_banner
        * New API to Config Day banner
    * Added enable_ietf_standard_snmp_link_traps
        * New API to Enable ietf standard snmp link traps
    * Added disable_ietf_standard_snmp_link_traps
        * New API to Disable ietf standard snmp link traps
    * Added configure_graceful_reload_interval
        * API for graceful-reload interval {value}
    * Added  monitor_event_trace
        * API for monitor event-trace {trace_type} {category} clear
    * Added debug_lfd_label_statistics
        * API to configure debug lfd label statistics
    * Added new API configure_radius_server_vsa
    * Added new API configure_device_sensor_notify
    * Added new API configure_device_sensor_filter_spec
    * Added configure_bgp_eigrp_redistribution
        * API to configure redistribute eigrp under bgp
    * Added configure_dhcp_pool_dns_server
        * API to configure dns-server under dhcp pool
    * Added configure_crypto_logging_ikev2
        * API to enable crypto logging ikev2
    * Added unconfigure_crypto_logging_ikev2
        * API to disable crypto logging ikev2
    * Added configure_mtc API
        * API to configure management traffic control
    * Added unconfigure_mtc_parameters API
        * API to unconfigure mtc parameters
    * Added unconfigure_mtc
        * API to unconfigure mtc
    * Added configure_ospf_redistribute_in_bgp
        * API to configure bgp with ospf redistribuiton
    * Added configure_authentication_event_server
        * API to configure_authentication_event_server
    * Added unconfigure_authentication_event_server
        * API to unconfigure_authentication_event_server
    * Added configure_stackpower_stack  and unconfigure_stackpower_stack
        * Added new API to configure stack-power stack.
    * Added configure_dhcp_pool and unconfigure_dhcp_pool
        * API to configure and unconfigure dhcp pool
    * Added configure_service_dhcp and unconfigure_service_dhcp
        * API to configure and unconfigure service dhcp
    * Added unconfigure_exclude_ip_dhcp
        * API to unconfigure exclude ip dhcp
    * Added configure_pvlan_loadbalancing_ethernetsegment_l2vpn_evpn
        * New API to configure per vlan load balncing between PEs on ethernet segment
    * Added unconfigure_mdt_config_on vrf
        * New API to unconfigure mdt bgp autodiscovery or mdt default group or mdt overlay protocol on VRF
    * Added config_cns_agent_passwd
        * New API to configure cns agent password
    * Modified `save_running_config` API
        * Added timeout argument
    * Added `configure_generate_self_certificate` API
        * New API to generate self certificate on device
    * Added configure_nat_translation_max_entries
        * API to configure ip nat translation max-entries
    * Added configure_static_nat_source_list_rule
        * API to configure static NAT source list rule
    * Added execute_license_smart_save_usage_rum_id_file
        * API to configure license smart save usage rum-Id {rum_id} file {path}
    * Added unconfigure_propagate_sgt
        * API to unconfigure propagate sgt
    * Added unconfigure_cts_role_based_sgt_map_vlan_list
        * API to unconfigure cts role based sgt map vlan list
    * New unconfigure_ip_local_pool
        * Added api unconfigure_ip_local_pool
    * Added configure_app_hosting_appid_iperf_from_vlan
        * API to configure app hosting appid iperf from vlan
    * Added configure_line_vty_needs_enhancement
        * Api to configure line vty needs enhancement
    * Added execute_change_installed_application_state
        * API to change the state of currently installed Application
    * Added unconfigure_nat_translation_max_entries
        * API to unconfigure nat translation max-entries
    * Modified configure_static_nat_rule
        * API modified to handle vrf and no-alias
    * Added generate_crypto_key_execute
        * API for Generate Crypto keys
    * Added configure_arp_acl
        * API for Configuring ARP ACL
    * Added configure_rd_address_family_vrf
        * API for configure rd and address family on vrf
    * Added redistribute_bgp_on_ospfv3
        * API for redistribute bgp on ospfv3
    * Added configure_console_default_privilege_level
        * added api to configure console privilege level
    * Added configure_print_timestamp_for_show_command
        * added api to Configure print timestamp for show command
    * Added config_smart_authorisation_request
        * added api to configure smart authorisation request
    * Added config_smart_save_license_usage
        * added api to configure smart save license usage
    * Added clear_dlep_client API
        * API to clear dlep client on interface
    * Added clear_dlep_neighbor API
        * API to clear dlep neighbor on interface
    * Added unconfigure_switchport_private_vlan_mode
        * API to unconfigure switchport private vlan mode on device interface
    * Added unconfigure_service_policy_with_queueing_name
        * New API to unconfigure service policy with queueing_name
    * Added unconfigure_snmp_mib_bulkstat
        * New API to unconfigure snmp_mib bulkstat profile

* added unconfigure_static_nat_source_list_rule
    * API to unconfigure ip nat {translation} source list

* modified unconfigure_static_nat_rule
    * API modified to handle vrf and no-alias



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * Added ShowDiagnosticContentModule
        * show diagnostic content module {mod_num}
    * Added ShowDiagnosticResultModuleTestDetail
        * show diagnostic result module {mod_num} test {include} detail

* iosxe
    * Added ShowPlatformSoftwareFedQosInterfaceEgressNpdDetailed
        * parser for show platform software fed {switch} {mode} qos interface {interface} egress npd detailed
    * Added ShowInterfacesVlanMapping
        * show interface {interface} vlan mapping
    * Added ShowLoggingProcessSmdReverse
        * parser for show logging process smd reverse
        * show logging process smd {switch} {mode} reverse
    * Added ShowPolicyMapTypeQueueingPolicyname
        * parser for show policy-map type queueing {policy_name}
    * Added ShowEeeCapabilitiesInterface
        * show eee capabilities interface <interface-id>
    * Added ShowEeeStatusInterface
        * show eee status interface <interface-id>
    * Added ShowIpv6cefExactRoute Parser
        * parser for show ipv6 cef exact route
    * Added ShowConsistencyCheckerMcastStartAll
        * "show consistency-checker mcast {layer} start all"
        * "show consistency-checker mcast {layer} start {address} {source}"
        * "show consistency-checker mcast {layer} start vrf {instance_name} {address} {source}"
        * "show consistency-checker mcast {layer} start vlan {vlan_id} {address}"
    * Added ShowConsistencyCheckerRunIdDetail
        * "show consistency-checker run-id {id} detail"
    * Added ShowConsistencyCheckerRunId
        * "show consistency-checker run-id {id}"
    * Added SnmpGetIfIndex Parser
        * Parser for "snmp get v{version} {ip} {community_str} oid {mibifindex}"
    * Added ShowPlatformSoftwareCefIpVrf Parser
        * Parser for show platform software cef {protocol} vrf {option} {ip} {mask} feature-all
    * Added ShowOspfv3RibRedistribution
        * added parser for show ospfv3 rib redistribution
    * Added ShowPlatform
        * updated regex for p6 to capture state
    * Modified ShowPlatformHardwareAuthenticationStatus
        * Added Line card 4 authentication status for 9400 switch.
    * Added ShowControllersEthernetController
        * parser for show controllers ethernet-controller
    * Added ShowPlatformHardwareFedQosQueueStatsOqMulticast
        * parser for show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id}
    * Added ShowPlatformHardwareFedQosQueueStatsOqMulticastOqId
        * parser for show platform hardware fed {switch} {mode} qos queue stats oq multicast interface {interface} oq_id {oq_id} clear-on-read
    * Added ShowL2routeEvpnMulticastSmet
        * show l2route evpn multicast smet
        * show l2route evpn multicast smet topology <evi>
        * show l2route evpn multicast smet topology <evi> group <group>
        * show l2route evpn multicast smet topology <evi> group <group> local
        * show l2route evpn multicast smet topology <evi> group <group> local interface <interface>
        * show l2route evpn multicast smet topology <evi> group <group> local interface <interface> service-instance <serviceInstance>
        * show l2route evpn multicast smet topology <evi> group <group> remote
        * show l2route evpn multicast smet topology <evi> group <group> remote originator <originator-addr>
        * show l2route evpn multicast smet topology <evietag>
        * show l2route evpn multicast smet topology <evietag> group <group>
        * show l2route evpn multicast smet topology <evietag> group <group> local
        * show l2route evpn multicast smet topology <evietag> group <group> local interface <interface>
        * show l2route evpn multicast smet topology <evietag> group <group> local interface <interface> service-instance <serviceInstance>
        * show l2route evpn multicast smet topology <evietag> group <group> remote
        * show l2route evpn multicast smet topology <evietag> group <group> remote originator <originator-addr>
    * Added ShowL2routeEvpnMulticastRoute
        * show l2route evpn multicast route
        * show l2route evpn multicast route topology <evi>
        * show l2route evpn multicast route topology <evi> group <group>
        * show l2route evpn multicast route topology <evi> group <group> source <source>
        * show l2route evpn multicast route topology <evietag>
        * show l2route evpn multicast route topology <evietag> group <group>
        * show l2route evpn multicast route topology <evietag> group <group> source <source>
    * Added ShowL2routeEvpnImet
        * show l2route evpn imet
        * show l2route evpn imet topology <evi>
        * show l2route evpn imet topology <evi> producer <producer>
        * show l2route evpn imet topology <evi> producer <producer> origin-rtr <originator-addr>
    * Added ShowPlatformSoftwareFedPuntEntries Parser
        * Parser for show platform software fed {switch} {mode} punt entries
    * Added ShowPlatformHardwareFedQosSchedulerSdkInterface Parser
        * parser for 'show platform hardware fed {mode} qos scheduler sdk interface {interface}'
        * 'show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}'
    * Added ShowLoggingOnboardSwitchMessageDetail
        * for 'show logging onboard rp {switch_type} message detail'
    * Added ShowLoggingOnboardSwitchEnvironmentDetail
        * for 'show logging onboard rp {switch_type} environment detail'
    * Added ShowLoggingOnboardSwitchCounterDetail
        * show logging onboard rp {switch_type} counter detail'
    * Added ShowLoggingOnboardSwitchClilogDetail
        * for 'show logging onboard rp {switch_type} clilog detail'
    * Added ShowFileSys
        * parser for show {filesystem} filesys
    * Added ShowInterfaceCounterErrors Parser
        * Parser for show interfaces {interface} counters errors
    * Added ShowSdwanTenantOmpRoutes Parser
        * Parser for show sdwan tenant {tenant} omp routes
    * Added ShowSdwanTenantOmpPeers Parser
        * Parser for show sdwan tenant {tenant} omp peers
    * Added ShowSdwanTenantSumary Parser
        * Parser for show sdwan tenant-summary
    * Added ShowL2fibBdTableMulticast
        * show l2fib bridge-domain {id} table multicast
    * Added ShowL2fibBdAddressMulticast
        * show l2fib bridge-domain {id} address multicast {address/prefix}
    * Added ShowL2fibBdTableUnicast
        * show l2fib bridge-domain {id} table unicast
    * Modified ShowL2fibBridgeDomainDetail
        * Added missing fields back, added missing Optionals
    * Modified ShowCryptoIkev2Stats
        * show crypto ikev2 stats
    * Added ShowInterfaceFlowControl
        * show show interface flowcontrol
    * Added ShowDot1xInterfaceStatistics Parser
        * Parser for "show dot1x interface {interface} statistics"
    * Added ShowFlowMonitorCacheFilterInterface
        * parser for show flow monitor {name} cache filter {int_type} {direction} {interface_name} sort highest {int_type} {direction} {top}
    * Added ShowIpOspfDatabaseOpaqueAreaTypeTrafficEngineeringSelfOriginate Parser
        * Parser for "show ip ospf database opaque-area type traffic-engineering self-originate"
    * Added new parser 'show ipv6 dhcp relay binding'
    * Added ShowPlatformHardwareCryptoDeviceUtilization Parser
        * Parser for show platform hardware crypto-device utilization
    * Added ShowPlatformHardwareQfpActiveClassificationFeatureTcamUsage Parser
        * Parser for show platform hardware qfp active classification feature tcam-usage
    * Added ShowSdwanServiceChainStats parser
        * Parser for "show platform hardware qfp active feature sdwan datapath service-chain stats"
    * Added ShowSdwanPolicyDataPolicyFilter parser
        * Parser for "show sdwan policy data-policy-filter"
    * Added ShowSdwanMulticastRemoteNodes Parser
        * Parser for "show platform software sdwan multicast remote-nodes vrf {vrf ID}"
    * Added ShowSdwanMulticastReplicators Parser
        * Parser for "show platform software sdwan multicast replicators vrf {vrf_ID}"
    * Added  ShowMgmtTrafficControlIpv4 parser
        * Parser for "show mgmt-traffic control ipv4"
    * Added ShowPlatformSoftwareFedSwitchQosPolicyTargetStatus
        * show platform software fed switch {switch} qos policy target status
    * Added ShowDhcpLease Parser
        * Parser for "show dhcp lease"
    * Added ShowPerformanceMeasurementInterfaces
        * show performance-measurement interfaces
        * show performance-measurement interfaces detail
        * show performance-measurement interfaces private
        * show performance-measurement interfaces {multiple}
        * show performance-measurement interfaces name <name>
        * show performance-measurement interfaces name <name> {multiple}

* iosxr
    * Added ShowIsisInterfaceBrief Parser
        * Parser for "show isis interface brief"
    * Added ShowIpBgp
        * Parser for cli 'show ip bgp {route}'
    * Added ShowIsisDatabase
        * Parser for cli 'show isis databse'


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLicenseRumIdDetail
        * The schema is changed to make the 'feature_name' and 'metric_value'
    * Modified ShowCtsRoleBasedPermissions Parser
        * Fix parser issue with p1, p2 and formatted to new parser format.
    * Modified ShowRunInterface
        * added addtional optional keys to schema
    * Modified ShowSpanningTree
        * Fix p10 reg ex
    * Modified ShowArp
        * Fix p1 reg ex and added optional variable private_vlan
    * Modified ShowL2vpnEvpnMac
        * added local and remote optional variables to consider local and remote commands
    * Modify ShowIpv6MldSnoopingMrouterVlan
        * show ipv6 mld snooping mrouter vlan {vlanid}
    * Modified ShowCispRegistrations Parser
        * Added support to extract dot1x value
    * Modified ShowCdpEntry Parser
        * Made native_vlan as optional
    * Modified ShowInterfacesSwitchport
        * Fixed the schema by making 'switchport_mode' key optional
    * Modified ShowTelemetryIETFSubscriptionAllReceivers
        * fixed parser issue when "explanation" field is empty
    * Modified ShowIsisRib
        * Modified parser to handle subinterfaces
    * Modified ShowPolicyMapTypeSuperParser
        * Fix p11_2 and p41
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Modified regex p1 and p7_1
    * Modified ShowLispSiteSuperParser
        * Added support for 2-line display of registration when ETR address is too long
    * Modified ShowLispSiteDetailSuperParser
        * Added support for parsing 'any-mac' as EID-prefix
    * Modified ShowCryptoCallAdmissionStatistics
        * Modified schema to support new values for SA Strength Enforcement Rejects
    * Added ShowLispIpv4Publisher
        * Updated regex pattern p2 for ipv4 publisher output with ems type
    * Added ShowLispIpv6Publisher
        * Updated regex pattern p2 for ipv6 publisher output with ems type
    * Added ShowLispEthernetPublisher
        * Updated regex pattern p2 for ethernet publisher output with ems type
    * Modified ShowPlatformSoftwareWiredClientSwitchR0
        * fix p1 regular expression
    * Modified ShowCdpNeighborsDetail Parser
        * Added support for show cdp neighbors {interface} detail
    * Modified ShowIpv6Mfib Parser
        * Fix p8 regex
        * added optional variables 'egress_vxlan_vni' and 'egress_vxlan_nxthop'
    * Added parames as optional for few keys.
        * Made fail_close_revert, pfs_rekey_received, anti_replay_count are optional.
        * Fixed regexp more generic to match G-IKEv2 syntax.
    * Updated ShowRomvar Parser to support new keys real_mgmte_dev, sr_mgmt_vrf,

* iosxr
    * Modified ShowCefDetail
        * Added support for cli 'show cef vrf {vrf_name} {ip_type} {prefix} detail' in ShowCefDetail
    * Modified ShowIsisProtocol
        * Modified 'level' parameter as optional parameter in schema
    * Modified show_static_routing and show rpl route-policy
        * Updated pattren <p2> for show_static_routing to accommodate with other outputs
        * Updated regex pattern <route-type> for show rpl route-policy to accommodate various outputs.
    * Modified ShowOspfInterface
        * Added <p30> pattern to match 'LDP Sync Enabled, Sync Status Achieved'
        * Modified <p3> pattern to support 'GigabitEthernet0/0/0/2 is administratively down, line protocol is down'

* ios/iosxe
    * Modified ShowVersion
        * Updated regex pattern p1_1 to accommodate legacy platform


--------------------------------------------------------------------------------
                                     Modify
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface
        * added support for 'show platform software fed active ptp interface'



genie.telemetry
"""""""""""""""""
