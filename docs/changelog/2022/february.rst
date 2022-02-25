February 2022
=============

February 24 - Genie v22.2 
-------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.2                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.2                          |
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
    * Modified _get_triggers_verifications_via_callable()
        * added logic to ignore 'data' and 'variables' fields in trigger files
    * updated connect_device() in utils
        * Fix a bug with 'pool_size' via mapping datafile

* genie.harness
    * Allow module load failures to propagate exception


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* conf/utils
    * Updated converter
        * pyATS Device will not be converted to Genie Device if pyATS Device class is given in testbed yaml



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Modified clean infrastructure
        * To properly log exceptions generated in the parent process
    * Modified stage schema validation
        * To support the 'source' key

* clean recovery
    * Removed exception when connecting to device in rommon

* generic
    * Modified 'reload' clean stage, fixed check_modules logic

* iosxe
    * Fixed iosxe clean abstraction issue

* iosxr
    * Added
        * verify_running_image



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Modified filetransferutils
        * removed 'protocol identification string lack carriage return' error pattern
    * Modified filetransferutils
        * Added 'No such file or directory' error pattern



genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated pyATS Health Check default yaml
        * Added 'threshold' to 'memory' check



genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * routing.py
        * Fixed the routing issue caused by default vrf



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added 'configure_ip_mtu' API
        * configure mtu value under interface
    * Added 'unconfigure_ip_mtu' API
        * unconfigure mtu value under interface
    * Added 'configure_interface_reg_segment' API
        * configure rep segment under interface
    * Added 'unconfigure_interface_reg_segment' API
        * unconfigure rep segment under interface
    * Added 'configure_interface_reg_segment_timer' API
        * configure rep segment timer under interface
    * Added 'unconfigure_interface_reg_segment_timer' API
        * unconfigure rep segment timer under interface
    * Added 'configure_switchport_nonegotiate' API
        * configure switchport nonegotiate under interface
    * Added 'unconfigure_switchport_nonegotiate' API
        * unconfigure switchport nonegotiate under interface
    * Added configure_shap_map API
        * API for configuring policy with shape map for service-policy.
    * Added clear_ikev2_sa API
        * API for clearing ikev2 sa.
    * Added clear_ip_nhrp API
        * API for clearing NHRP.
    * Added clear_dmvpn API
        * API for clearing dmvpn sessions.
    * Added clear_dmvpn_statistics API
        * API for clearing dmvpn statistics.
    * Added configure_ikev2_proposal API
        * API for configuring ike proposal.
    * Added configure_ikev2_policy API
        * API for configure ike policy.
    * Added configure_ikev2_authorization_policy API
        * API for configuring ikev2 authorization policy.
    * Added configure_ikev2_profile_advanced API
        * API for ikev2 profile advanced.
    * Added configure_ipsec_transform_set API
        * API for IPSec transform set.
    * Added configure_ipsec_profile API
        * API for IPSec profile
    * Added configure_dynamic_nat_route_map_rule API
        * API for configuring a dynamic NAT route-map rule.
    * Added unconfigure_dynamic_nat_route_map_rule API
        * API for unconfiguring a dynamic NAT route-map rule.
    * Added configure_dynamic_nat_pool_overload_route_map_rule API
        * API for configuring a dynamic NAT pool overload route-map pool rule.
    * Added unconfigure_dynamic_nat_pool_overload_route_map_rule API
        * API for unconfiguring a dynamic NAT pool overload route-map pool rule.
    * Added configure_dynamic_nat_interface_overload_route_map_rule API
        * API for configuring a dynamic NAT interface overload route-map rule.
    * Added unconfigure_dynamic_nat_interface_overload_route_map_rule API
        * API for unconfiguring a dynamic NAT interface overload route-map rule.
    * Added configure_standard_access_list API
        * API for configuring standard access-list.
    * Added unconfigure_standard_access_list API
        * API for unconfiguring standard access-list.
    * Added configure_enable_nat_scale API
        * API for configure enable nat scale.
    * Added configure_dynamic_nat_rule API
        * API for configuring dynamic NAT rule.
    * Added unconfigure_dynamic_nat_rule API
        * API for unconfiguring dynamic NAT rule.
    * Added configure_static_nat_rule API
        * API for configuring a static NAT rule.
    * Added unconfigure_static_nat_rule API
        * API for unconfiguring a static NAT rule.
    * Added configure_static_nat_outside_rule
        * API for configuring static NAT outside rule.
    * Added unconfigure_static_nat_outside_rule
        * API for unconfiguring static NAT outside rule.
    * Added configure_subinterface API
        * API for configuring subinterface
    * Added unconfigure_aaa_new_model API
        * API for unconfiguring aaa new-model.
    * added remove_ipv6_dhcp_guard_policy API
    * added remove_ipv6_nd_suppress_policy API
    * added remove_single_device_tracking_policy API
    * added remove_ipv6_source_guard_policy API
    * added clear_device_tracking_database API
    * added clear_device_tracking_counters API
    * Added configure_ptp_8275_local_priority API
        * configure ptp 8275 local priority
    * Added unconfigure_ptp_8275_local_priority API
        * unconfigure ptp 8275 local priority
    * Added configure_ptp_role_primary API
        * configure ptp role primary
    * Added unconfigure_ptp_role_primary API
        * unconfigure ptp role primary
    * Added configure_ptp_8275_holdover_spec_duration API
        * configure holdover spec duration
    * Added unconfigure_ptp_8275_holdover_spec_duration API
        * unconfigure holdover spec duration
    * Added execute_clear_ipdhcp_snooping_database_statistics API
        * clear ip dhcp snooping database statistics
    * Added configure_ip_arp_inspection_vlan API
        * config ip arp inspection vlan on device
    * Added unconfigure_ip_arp_inspection_vlan API
        * unconfig ip arp inspection vlan on device
    * Added configure_ip_arp_inspection_validateip API
        * config ip arp inspection validate ip  on device
    * Added unconfigure_ip_arp_inspection_validateip API
        * unconfig ip arp inspection validate ip  on device
    * Added configure_ip_dhcp_snooping_database API
        * configuring ip dhcp snooping database on device
    * Added unconfigure_ip_dhcp_snooping_database API
        * unconfiguring ip dhcp snooping database on device
    * Added create_dhcp_pool_withoutrouter API
        * create dhcp pool  on device
    * Added VerifyApMode
        * Added new clean stage called VerifyApMode
    * Added VerifyApAssociation
        * Added new clean stage called VerifyApAssociation
    * Added
        * configure_eigrp_networks
        * configure_interface_eigrp_v6
        * unconfigure_interface_eigrp_v6
        * enable_ipv6_eigrp_router
        * unconfigure_ipv6_eigrp_router
        * unconfigure_eigrp_router
    * Added
        * configure_crypto_transform_set
        * unconfigure_crypto_transform_set
        * unconfigure_ipsec_profile
        * configure_crypto_ikev2_keyring
        * unconfigure_crypto_ikev2_keyring
        * configure_ikev2_profile_pre_share
    * Added
        * configure_ipv6_multicast_routing
        * unconfigure_ipv6_multicast_routing
    * Added
        * unconfigure_ipv6_unicast_routing
    * Added configure_nat_pool API
        * API for configuring a NAT pool.
    * Added unconfigure_nat_pool API
        * API for unconfiguring a NAT pool.
    * Added configure_static_nat_route_map_rule API
        * API for configuring a static NAT route-map rule.
    * Added unconfigure_static_nat_route_map_rule API
        * API for unconfiguring a static NAT route-map rule.
    * Added configure_nat_port_route_map_rule API
        * API for configuring a NAT port route-map rule.
    * Added unconfigure_nat_port_route_map_rule API
        * API for unconfiguring a NAT port route-map rule.
    * Added execute_clear_platform_software_fed_switch_active_cpu_interface API
        * API for clearing active cpu-interface.
    * Added configure_default_gateway API
        * Configures default gateway
    * Added configure_dot1x_pae API
        * Configures DOT1x pae both on device
    * Added unconfigure_dot1x_pae API
        * Unconfigures DOT1x pae both on device
    * Added configure_aaa_auth_proxy API
        * Configures AAA auth proxy on device
    * Added unconfigure_aaa_auth_proxy API
        * Unconfigures AAA auth proxy on device
    * Added configure_wired_radius_attribute API
        * Configures wired radius attribute on device
    * Added unconfigure_wired_radius_attribute API
        * Unconfigures wired radius attribute on device
    * Added configure_radius_server_dead_criteria API
        * Configures Radius Server dead criteria on device
    * Added unconfigure_radius_server_dead_criteria API
        * Unconfigures Radius Server dead criteria on device
    * Added configure_radius_server_deadtime API
        * Configures Radius Server deadtime on device
    * Added unconfigure_radius_server_deadtime API
        * Unconfigures Radius Server deadtime on device
    * Added configure_aaa_session_id API
        * Configures AAA session ID on device
    * Added unconfigure_aaa_session_id API
        * Unconfigures AAA session ID on device
    * Added verify_bgp_evi_rt2_mac_localhost
        * Method verifies bgp host for routetype 2 in show ip bgp
    * Added config_interface_subinterface API
    * Added configure_ipv6_acl API
        * configures ipv6 acl
    * Added unconfigure_ipv6_acl_ace API
        * unconfigures ace in ipv6 acl
    * Added execute_clear_platform_software_fed_switch_mode_acl_stats API
        * executes execute_clear_platform_software_fed_switch_mode_acl_stats
    * Added verify_cef_uid_on_active_standby API
        * verifies cef id on both active and standby device
    * Added verify_cef_path_sets_summary API
        * verifies cef path sets summary on active and standby device
    * Added verify_mpls_rlist_summary_vefore_and_after_sso API
        * verifies wether rlist summary is same before and after sso on both active and standby device
    * Added verify_etherchannel_counter API
        * verifies packet flow on port-channel interface
    * Added interface_counter_check API
        * verifies packet flow on interface
    * Added verify_igmp_groups_under_vrf API
        * verifies igmp groups
    * Added verify_mpls_mldp_count
        * verifies  mpls mldp count
    * Added unconfig_ip_on_vlan API
        * unconfigures Ipv4/Ipv6 address from vlan
    * Added transceiver API
        * API for getting transceiver input current,output current and laserbiased current
    * Added transceiver_interval API
        * API for getting the default interval "30" for the transceiver
    * Added get_ap_state
        * Added new api to get state of the access point
    * Added get_ap_country
        * Added new api to get country of the access point
    * Added get_ap_mode
        * Added new api to get ap mode of the access point

* nxos
    * Added API 'verify_boot_mode_lxc_config'
        * verify LXC config on device
    * Added API 'verify_boot_mode_lxc_unconfig'
        * verify LXC config is not present in the device
    * Added API 'verify_incompatibility_status'
        * verify ISSU incompatibility status

* blitz
    * advanced_actions.py
        * Added if, elif and else conditions support for run_condition action.

* {address_family} evi {evi} route-type 2 0 {mac} *
    * Added verify_bgp_evi_mac_ipprefix

* method verifies for bgp ip prefix specific to mac in

* show ip bgp {address-family} evi {evi} detail
    * Added  get_l2route_mac_route_flags

* gets mac related flags in show l2route evpn default-gateway
    * Added verify_l2route_mac_route_flag

* method verifies for particular flag and also flag

* specific to mac if given
    * Added get_mac_table_from_address_family

* gets mac table from address_family in show {address_family} mac
    * Added  verify_mac_from_address_family
        * Verify mac from particular address family in show l2vpn evpn mac

* also for the particular evi if given
    * Added get_routing_ipv6_routes

* executes 'show ipv6 route vrf <vrf>' and retrieve the routes
    * Added verify_route_vrf_nexthop_with_source_protocol

* verify route target is present with specific l3 protocol in
    * show <address_family> route vrf <vrf>

* added verify_bgp_neighbor_state
    * Verifies bgp neighbor state in show ip bgp l2vpn evpn summary or
    * state for particular neighbor if given

* added verify_bgp_neighbor_route_zero_prefixes

* added poe_p3 api
    * API for getting power_class and power_used for poe interfaces


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* fixes to existing apis
    * Added configure_ptp_modes API
        * configure ptp modes
    * Added unconfigure_ptp_modes API
        * unconfigure ptp modes

* api utils
    * Modified api_unittest_generator
        * Fixed bug when default test arguments are not provided

* generic
    * Modified copy_from_device API, avoid stripping of /

* ios
    * Modified write_erase_reload_device_without_reconfig
        * Added sleep_after_reload argument to be used instead of reload_timeout for post reload sleep.

* iosxe
    * Modified write_erase_reload_device_without_reconfig
        * Added sleep_after_reload argument to be used instead of reload_timeout for post reload sleep.
    * Modified
        * configure_ipsec_profile
    * Modified
        * configure_ip_on_tunnel_interface
    * Modified write_erase_reload_device
        * Added api to device  and remove the extra argument from  calling the
    * Modified configure_pki_enroll_certificate API
        * Modified to return the output
    * Modified configure_radius_server_dead_criteria
        * Changed the variable time to server_time
    * Modified configure_radius_server_deadtime
        * Changed the variable time to server_time
    * Modified unconfigure_radius_server_dead_criteria
        * Changed the variable time to server_time
    * Modified unconfigure_radius_server_deadtime
        * Changed the variable time to server_time
    * Modified configure_aaa_local_auth API
        * Added few commands to this API
    * Modified unconfigure_aaa_local_auth API
        * Added few commands to this API
    * Added configure_dot1x_cred_int API
        * Configures Dot1x credential on interface
    * Added unconfigure_dot1x_cred_int API
        * Unconfigures Dot1x credential on interface
    * Fixed 'write_erase_reload_device_without_reconfig' API
        * Fixed init_config_commands issue
    * Fixed 'write_erase_reload_device' API
        * Fixed init_config_commands issue
    * Modified API clear_access_session
        * added attributes Interface, as options to the configuration
    * Modified API configure_interface_switchport_trunk
        * added attributes Operation, as options to the configuration
    * Modified API configure_ip_prefix_list
        * added attributes SubnetId, as options to the configuration
    * Modified API unconfigure_ip_prefix_list
        * added attributes SubnetId, as options to the configuration
    * Modified API configure_coa
        * added attributes vrf, as options to the configuration
    * Added API unconfigure_coa
        * added unconfiguration API for dynamic-author
    * Updated configure_control_policies
        * added attributes priority, dot1x_type, retries, retry_time, auth_rest_timer, and template_name as options to the configuration
    * Modified config_ip_on_interface
        * Added Support for ip adddress dhcp
    * Modified verify_mpls_forwarding_table_gid_counter API
    * Modified verify_mpls_forwarding_table_vrf_mdt API
    * Modified verify_mfib_vrf_hardware_rate API
        * Modified it to support verification of multiple group ips hardware rate, by passing grp_ip which contains group ip with traffic sent pps and number of joins
    * Modified 'health_cpu' API
        * Updated command to have 'exclude 0.00%' filter by default
    * Modified 'health_memory' API
        * Updated command to have 'section | ^Processor' by default
        * added 'threshold' argument
        * check only total usage first, then check detail only when threshold exceeds

* nxos
    * Modified write_erase_reload_device_without_reconfig
        * Added sleep_after_reload argument to be used instead of reload_timeout for post reload sleep.
    * Fixed 'write_erase_reload_device_without_reconfig' API
        * Fixed init_config_commands issue
    * Fixed 'health_cpu' API
        * Fixed to get proper cpu usage for total

* jinja2
    * Modified load_jinja_template
        * Added arguments to remove empty newline characters and leading whitespace
            * Defaults to True
    * Modified get_jinja_template
        * Added arguments to remove empty newline characters and leading whitespace
            * Defaults to True

* apis
    * Modified creating the remote path so the files with more than one suffixes



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                     Added                                      
--------------------------------------------------------------------------------

* iosxe
    * Added ShowLispInstanceIdServiceStatistics
        * show lisp instance-id {instance_id} {service} statistics
        * show lisp {lisp_id} {instance_id} {service} statistics
        * show lisp locator-table {locator_table} instance-id {instance_id} {service} statisticsNo backward compatibility


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowFirmwareVersionAll
        * show firmware version all
    * Added ShowIpv6RouteSummary parser
        * Parser for 'show ipv6 route summary' and 'show ipv6 route vrf {vrf} summary'
    * Modified ShowIpRouteSummary parser
        * Modified parser to grep v6 protocols
    * Added ShowLispInstanceIdIpv4MapCache
        * show lisp instance-id {instance_id} ipv4 map-cache
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache
        * show lisp eid-table vrf {vrf} ipv4 map-cache
        * show lisp eid-table {eid_table} ipv4 map-caches
    * Added ShowLispInstanceIdIpv6MapCache
        * show lisp instance-id {instance_id} ipv6 map-cache
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache
        * show lisp eid-table vrf {vrf} ipv6 map-cache
        * show lisp eid-table {eid_table} ipv6 map-caches
    * Deleted ShowLispEidTableVrfUserIpv4MapCache existing class because this command is covered by new parser (ShowLispInstanceIdIpv4MapCache). Modified Schema and updated code.No backward compatibility
    * Added ShowLisp
        * 'show lisp'
        * 'show lisp {lisp_id}'
    * Added ShowLoggingOnboardRpActiveTemperatureDetail
        * show logging onboard rp active temperature detail
        * show logging onboard rp active voltage detail
        * show logging onboard rp standby temperature detail
        * show logging onboard rp standby voltage detail
    * Added ShowPlatformSoftwareFedSwitchActiveQosPolicyTarget parser
        * show platform software fed switch active qos policy target brief
    * Added ShowPlatformSoftwareObjectManagerFpActiveStatistics parser
        * show platform software object-manager FP active statistics
    * Added ShowPolicyMapTypeQueueingSuperParser
    * Added ShowPolicyMapTypeQueueingInterfaceOutput
        * show policy-map type queueing interface {interface} output class {class_name}
        * show policy-map type queueing interface {interface} output
    * Added ShowRunningConfigFlowRecord
        * show running-config flow record
    * Added ShowTelemetryIETFSubscriptionSummary
        * show telemetry ietf subscription summary
    * Added ShowLispInstanceIdService
        * 'show lisp instance-id {instance_id} {service}',
        * 'show lisp {lisp_id} instance-id {instance_id} {service}',
        * 'show lisp locator-table {locator_table} instance-id {instance_id} {service}
    * Added ShowLispSiteSummary
        * 'show lisp site summary',
        * 'show lisp {lisp_id} site summary',
        * 'show lisp site summary instance-id {instance_id}',
        * 'show lisp site summary eid-table vrf {vrf}',
        * 'show lisp site summary eid-table {eid_table}'
    * Added ShowInstallState parser
        * show install <state>
    * Added ShowParserStatistics parser
        * show parser statistics
    * Added ShowVersionRunning parser
        * show version running
    * Added ShowStackwiseLink parser
        * show stackwise-virtual switch <number> link
    * Added ShowInstallRollback parser
        * show install rollback
    * Added ShowInstallRollbackId parser
        * show install rollback id <rollback_id>
    * Added ShowPlatformSoftwareInstallManagerSwitchActiveR0OperationHistorySummary parser
        * show platform software install-manager switch active r0 operation history summary
    * Added ShowPlatformSoftwareInstallManagerRpActiveOperationHistorySummary parser
        * show platform software install-manager RP active operation history summary
    * Added show install package SMU parser
        * show install package SMU
    * c9400
        * Added ShowBoot parser
            * show boot
    * Added ShowIpv6DhcpPool
        * Parser for show ipv6 dhcp pool
    * Added ShowIpv6OspfNeighbor
        * Parser for show ipv6 ospf neighbor
    * Added ShowPlatformSoftwareFedActiveAclInfoSummary
        * Parser for Show Platform Software Fed Active Acl Info Summary
    * Added ShowPlatformFedActiveIfmMapping
        * Parser for show platform software fed active ifm mappings
    * Added ShowPlatformFedActiveTcamUtilization
        * Parser for show platform hardware fed active fwd-asic resource tcam utilization
    * Added ShowLispInstanceIdIpv4Server
        * show lisp instance-id {instance_id} ipv4 server
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server
        * show lisp eid-table vrf {vrf} ipv4 server
        * show lisp eid-table {eid_table} ipv4 server
    * Added ShowLispInstanceIdIpv6Server
        * show lisp instance-id {instance_id} ipv6 server
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server
        * show lisp eid-table vrf {vrf} ipv6 server
        * show lisp eid-table {eid_table} ipv6 server
    * Added ShowCryptoIkev2Session
        * show crypto ikev2 session
    * Added ShowCryptoIkev2SessionDetail
        * show crypto ikev2 session detail
    * Added ShowCryptoIsakmpSa
        * show crypto isakmp sa
    * Added ShowCryptoIsakmpSaDetail
        * show crypto isakmp sa detail
    * Added ShowCryptoMibIpsecFlowmibEndpoint
        * Parser for show crypto mib ipsec flowmib endpoint
    * Added ShowCryptoMibIpsecFlowmibTunnel
        * Parser for show crypto mib ipsec flowmib tunnel
    * Added ShowCryptoSessionLocalDetail
        * Parser for show crypto session local {ip_address} detail
    * Added ShowCryptoSessionLocal
        * Parser for show crypto session local {ip_address}
    * Added ShowCryptoIpsecSaCount
        * Parser for show crypto ipsec sa count
    * Added ShowCryptoIkev2SaDetail
        * Parser for show crypto ikev2 sa detail
    * Added ShowCryptoIkev2SaLocalDetail
        * Parser for show crypto ikev2 sa local {ip_address} detail
    * Added ShowCryptoIkev2SaLocal
        * Parser for show crypto ikev2 sa local {ip_address}
    * Added ShowIpMrib
        * show ip mrib route
        * show ip mrib route {group}
        * show ip mrib route {group} {source}
        * show ip mrib vrf {vrf} route
        * show ip mrib vrf {vrf} route {group}
        * show ip mrib vrf {vrf} route {group} {source}
    * Added ShowIpMrib
        * added the new parser for cli "show ip mrib route"
        * show ip mrib route
        * show ip mrib route {group}
        * show ip mrib route {group} {source}
        * show ip mrib vrf {vrf} route
        * show ip mrib vrf {vrf} route {group}
        * show ip mrib vrf {vrf} route {group} {source}
    * Added ShowIpMroute
        * added the new argument verbose and supported additonal
        * combinations in parser for cli "show ip mroute" and "show ipv6 mroute"
        * show ip mroute verbose
        * show ip mroute {group} verbose
        * show ip mroute {group} {source} verbose
        * show ip mroute vrf {vrf}
        * show ip mroute vrf {vrf} {group}
        * show ip mroute vrf {vrf} {group} {source}
        * show ip mroute vrf {vrf} verbose
        * show ip mroute vrf {vrf} {group} verbose
        * show ip mroute vrf {vrf} {group} {source} verbose
        * show ipv6 mroute {group}
        * show ipv6 mroute {group} {source}
        * show ipv6 mroute verbose
        * show ipv6 mroute {group} verbose
        * show ipv6 mroute {group} {source} verbose
        * show ipv6 mroute vrf {vrf} {group}
        * show ipv6 mroute vrf {vrf} {group} {source}
        * show ipv6 mroute vrf {vrf} verbose
        * show ipv6 mroute vrf {vrf} {group} verbose
        * show ipv6 mroute vrf {vrf} {group} {source} verbose
    * Modified class ShowLispSite
        * show lisp site
        * show lisp {lisp_id} site
        * show lisp site instance-id {instance_id}
        * show lisp {lisp_id} site instance-id {instance_id}
        * show lisp site eid-table {eid_table}
        * show lisp {lisp_id} site eid-table {eid_table}
        * show lisp site eid-table vrf {vrf}
        * show lisp {lisp_id} site eid-table vrf {vrf}
    * Modified ShowLispInstanceIdEthernetServer
        * show lisp instance-id {instance_id} ethernet server
        * show lisp {lisp_id} instance-id {instance_id} ethernet server
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server
        * show lisp eid-table vlan {vlan} ethernet server
    * Added ShowLispIpv4ServerExtranetPolicy
        * show lisp instance-id {instance_id} ipv4 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy
        * show lisp eid-table {eid_table} ipv4 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy
    * Added ShowLispIpv6ServerExtranetPolicy
        * show lisp instance-id {instance_id} ipv6 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy
        * show lisp eid-table {eid_table} ipv6 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy
    * Added ShowCallAdmissionStatistics parser
        * show call admission statistics
    * Added ShowCallAdmissionStatisticsDetailed parser
        * show call admission statistics detailed
    * Added ShowPlatformSoftwareFedSwitchActivePuntCpuq
        * show platform software fed switch active punt cpuq {cpu_q_id}
    * Added ShowPlatformTcamPbr
        * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowPlatformNatTranslationsStatistics
        * show platform nat translations active statistics
    * Added ShowPlatformNatTranslations
        * show platform nat translations active
    * Added ShowPlatformTcamAcl
        * show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}
    * Added ShowStackwiseVirtualLink
        * show stackwise-virtual link
    * Added ShowPlatSwObjectManagerF0Statistics
        * show platform software object-manager {switch} {switch_type} F0 statistics
    * Added ShowPlatSwObjectManagerF0ErrorObject
        * show platform software object-manager {switch} {switch_type} F0 error-object
    * Added ShowAAAMethodList
        * Added the parser for cli 'show aaa method-list {type}'
    * Added ShowRunningConfigAAA
        * Added the parser for cli 'show running-config aaa'
    * Modified class ShowLispServiceDatabase
        * The existing schema does not properly represent the output of the show command So fixed all the schema so that it represents the output properly and updated code accordingly
    * Modified class ShowLispEidTableServiceDatabase
        * The existing schema does not properly represent the output of the show command So fixed all the schema so that it represents the output properly and updated code accordingly
    * Modified class ShowLispEthernetDatabase
        * The existing schema does not properly represent the output of the show command So fixed all the schema so that it represents the output properly and updated code accordingly
    * Below are the new parsers added for pdm
        * Added show pdm steering policy
        * Added show pdm steering policy {steering_policy} detail
        * Added show pdm steering service
        * Added show pdm steering service {steering_service} detail
        * Added show pdm steering policy | count {service}
    * Added ShowRepTopologySegment
        * 'show rep topology segment {no}'
    * Added ShowPlatformSoftwareFedSwitchSecurityfedDhcpsnoopVlanVlanid
        * 'show platform software fed switch {switch_no} security-fed dhcp-snoop vlan vlan-id {vlan_id}'
    * Added ShowInterfacesEtherchannelCounters
        * show interfaces {interface} counter etherchannel
    * Modified ShowIpMroute
        * show ip mroute vrf {vrf} {grpip} {sourceip}
        * show ip mroute vrf {vrf} {grpip}
        * Added Optional schema keys <upstream_interface>, <rpf_nbr>, and <state>
    * Modified ShowBgpAllDetail
        * show bgp {address_family} {route}
    * Added ShowIpMrib command with options
    * Added ShowIpSlaStatistics
        * 'show ip sla statistics'
        * 'show ip sla statistics {probe_id}'
    * Added ShowIpSlaStatisticsDetails
        * 'show ip sla statistics details'
        * 'show ip sla statistics {probe_id} details'
    * Added ShowIpSlaStatisticsAggregated
        * 'show ip sla statistics aggregated'
        * 'show ip sla statistics aggregated {probe_id}'

* iosxr
    * NCS5K
        * Added platform folder
    * Added ShowInterfaceSummary Parser
        * show interface summary


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInventoryRaw
        * Updated regex <p1> and <p2> and modified code to not to add keywords with empty value
    * Modified ShowEnvironment
        * Updated regex pattern <P4> to accommodate various outputs
    * Modified ShowModule parser
        * Updated ShowModule parser to include missing keys
    * Added ShowVpdnSuperParser
        * show vpdn
        * show vpdn tunnel
    * Modified ShowVpdn
        * Moved logic into ShowVpdnSuperParser
    * Added ShowVpdnTunnel
        * show vpdn tunnel
    * Modified ShowIsisLspLog
        * Added an initial tag value "default"
    * Modified ShowRunInterface
        * Added stackwise_virtual_link and dual_active_detection as new Optional keys.
    * Modified ShowVersion
        * Added two new keys <copyright_years> and <location> to parser schema, updated regex <p3> and <p4>
    * Modified ShowModule
        * Updated regex <p3> and <p4> and modified code so it works with multiple modules
        * Changed keys <redundancy_role>, <operating_redundancy_mode>, and <configured_redundancy_mode> to optional
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * Added missing process states (Init, Failed, Invalid)
    * Modified ShowVlan
        * Added regex <p0> for handling situations where line wrapping is causing breakages
    * Modified ShowPlatform
        * Fix incorrect logic for <p6> slot type. C83 now included in matches for types 'lc' and 'rp'. Fix is NOT BACKWARDS COMPATIBLE
    * Modified ShowBgpAllNeighborsRoutesSuperParser
        * Added p8 to parse the "Total number of prefixes" in the for "show bgp neighbor routes"
    * Modified ShowPlatformSoftwareFedactiveAclCountersHardwareSchema
        * Added Optional Schema keys <ingress_ipv4_ipclients_cpu>, <ingress_ipv6_ipclients_cpu>, <ingress_ipv4_ipclients_drop>, and <ingress_ipv6_ipclients_drop>
    * Modified ShowIpMrouteSchema
        * Changed schema key <rpf_nbr> to Optional
    * Modified ShowProcessCpuSorted
        * Added 'include'/'exclude' support
    * Modified ShowProcessesMemory
        * Added 'exclude'/'section' support
    * Modified ShowSslproxyStatusSchema
        * Added "Dual-Side Optimization" key support.
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * added try/catch for unconditional command execution "show bgp all neighbors | i BGP neighbor"
    * Modified ShowMkaSessions Parser
        * changed the 'ckn' variable to match decimal/hexa decimal
    * Modified ShowLispService
        * Modified Schema and updated code.No backward compatibility

* ios
    * Modified ShowCdpNeighborsDetail
        * Changed port_id from schema to Optional.
        * Rearranged software version and advertisement version patterns to accommodate various outputs.

* iosxr
    * Modified ShowPolicyMapInterface
        * Updated regex patterns <p2> and <p4> to accommodate various outputs
        * Added optional schema keys <queue_conform_packets>, <queue_conform_bytes>, <queue_conform_rate>, <red_random_drops_packets>, and <red_random_drops_bytes>
    * Modified ShowBgpInstanceNeighborsAdvertisedRoutes
        * Added new pattern and logic to handle when device output was split into multiple lines

* generic
    * Modified ShowVersion
        * Adjusted iosxe/ios logic to ignore platforms that contain "x86_64_linux"

* nxos
    * Modified ShowInterface
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowEigrpTopology
        * Removed cli_commands, af and vrf
    * Added ShowIpEigrpTopology
        * show ip eigrp topology
        * show ip eigrp topology vrf {vrf}
    * Added ShowIpv6EigrpTopology
        * show ipv6 eigrp topology
        * show ipv6 eigrp topology vrf {vrf}

