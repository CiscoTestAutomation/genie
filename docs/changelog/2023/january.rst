January 2023
==========

January 31 - Genie v23.1 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.1                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.1                          |
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
                                New
--------------------------------------------------------------------------------
* genie.harness
    * Allow Trigger data order to specify trigger data using dictionary

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* genie.json
    * Removed the ignore directory from MAkeApi    

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_switch_provision_model
        * API unset switch provision
    * Added configure_snmp_server_manager
        * API set snmp server manager
    * Added unconfigure_event_manager_applet
        * API to unset event manager applet
    * Added configure_event_manager_applet
        * API to set event manager applet
    * Added configure_power_inline_auto_max
        * API to power inline auto max
    * Added
        * New clean stage Verify HA state under c9800


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Added `mgt_itf`` in NOT_A_STAGE
    * Updated 'apply_configuration' clean stage
        * added `error_pattern` argument to pass it to device.configure()

* cheetah
    * Modified
        * Increase sleep timeout in EraseApConfiguration since certain AP MODELS take extra time to reload.

* iosxe
    * Modified
        * Changed trustpoint name to device.hostname since sometimes hostname differs from name.




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

* nxos
    * Added to trigger required data settings (Which key to exclude for Platform Ops comparison)
        * Added <disk_total_space> and <installed_packages> to excluded keys
    * Updated _prepare_issu
        * Increased the timeout_seconds for filetransfer to 900 seconds
    * Updated _perform_issu
        * Added parameters <allow_disruptive> and <config_ver_exclude>
        * Added ISSU impact only check to prevent disruptive ISSU when non-disruptive is set
            * If <disrupt_flag> is False, checks if ISSU will be disruptive and fails if <allow_disruptive> is False
        * Added argument <config_ver_exclude> to compare_config_dicts
            * <config_ver_exclude> is a list of regex item to exclude from step Compare post-trigger config with pre trigger config snapshot
        * Resolved pre/post ISSU snapshot timeout when cfg_transfer is not set, using the cfg_timeout parameter.
    * Increased timer for <show install all time-stats detail>

* iosxe
    * Added unconfigure_profile_on_tunnel_interface API
        * API to unconfig profile alone under Tunnel interface.
    * Added terminal_no_monitor
        * API to execute terminal no monitor
    * Added license_smart_sync_all
        * API to license smart sync all
    * Added request_platform_software_cflow_copy
        * API to request platform software cflow copy
    * Added configure_stack_power_switch
    * Added configure_default_spanning_tree
    * Added configure_service_template
    * Added configure_interface_flow_control
        * API for configuring flow control on a interface
    * Added unconfigure_interface_flow_control
        * API for unconfiguring flow control on a interface
    * Added configure_replace
        * API forperforming configure replace on a switch
    * Added configure_udld_aggressive
        * API to configure udld aggressive
    * Added configure_udld_message_time
        * API to configure udld message time
    * Added unconfigure_interface_vlan
        * API to unconfigure interface vlan
    * Added configure_udld_port_aggressive
        * API to configure udld port aggressive on an interface
    * Added unconfigure_interface_port_channel
        * API to unconfigure interface port-channel number
    * Added configure_ipv6_pim_bsr_candidate_bsr api
        * Api to configure ipv6 pim candidate bsr
    * Added configure_ipv6_pim_bsr_candidate_rp api
        * Api to configure ipv6 pim candidate rp
    * Added configure_hsrp_version_on_interface
        * API for configure the hsrp version on interface
    * Added configure_ipv6_address_on_hsrp_interface
        * API for configure the ipv6 address on hdrp interface with timers
    * Modified configure_hsrp_interface
        * API for configure the ipv4 address on interface with timers
    * Added command to configure spanning-tree portfast default
        * spanning-tree portfast default
    * Added configure_policy_map_control api
        * Api to configure policy-map type control
    * Added clear_bgp_l2vpn_evpn
        * API for to clear bgp l2vpn evpn sessions from the device
    * Added clear_isis
        * API for clearing the isis sessions from the device
    * Added var check in configure_ipsec_transform_set
        * API to config ah value to ''.
    * Added configure_system_disable_password_recovery_switch_all
        * API to configure system disable password recovery switch all
    * Added unconfigure_system_disable_password_recovery_switch_all
        * API to unconfigure system disable password recovery switch all
    * Added configure_system_ignore_startupconfig_switch_all
        * API to onfigure system ignore startupconfig switch all
    * Added unconfigure_system_ignore_startupconfig_switch_all
        * API to unonfigure system ignore startupconfig switch all
    * Added configure_service_template_with_absolute_timer
        * API for configure service template with absolute timer
    * Added configure_service_template_with_description
        * API for configure service template with description
    * Added configure_service_template_with_inactivity_timer
        * API for configure service template with inactive timer
    * Added configure_service_template_with_redirect_url
        * API for configure service template with url redirect
    * Added configure_service_template_with_sgt
        * API for configure service template with sgt revision number
    * Added configure_service_template_with_tag
        * API for configure service template with tag
    * Added configure_mac_address_table_learning
        * API for configure mac address-table learning
    * Added unconfigure_mac_address_table_learning
        * API for unconfigure mac address-table learning
    * Added configure_mac_address_table_aging_default
        * API for configure default mac address-table aging
    * Modified unconfigure_routing_static_route
        * API for unconfigure static routes
    * Modified configure_local_span_source
        * API for configure span source
    * Added unconfigure_local_span_source
        * API for unconfigure span source
    * Added unconfigure_local_span_destination_interface
        * API for configure span destination interface
    * Added configure_spanning_tree_bpdufilter_disable
        * API for configure spanning-tree bpdufilter disable
    * Added configure_spanning_tree_bpdugaurd
        * API for configure spanning-tree bpdugaurd enable/disable
    * Added configure_spanning_tree_mst_configuration_name
        * API for configure mst configuration name
    * Added configure_spanning_tree_mst_configuration_revision
        * API for configure mst configuration revision number
    * Added configure_ospf_network_non_broadcast
        * API to configure ip ospf network non broadcast
    * Added unconfigure_ospf_network_non_broadcast
        * API to unconfigure ip ospf network non broadcast
    * Added configure_neighbor_under_ospf
        * API to configure neighbor ip address under ospf process id
    * Added unconfigure_neighbor_under_ospf
        * API to unconfigure neighbor ip address under ospf process id
    * Added configure_ip_igmp_snooping_vlan_vlanid API
        * API for ip igmp snooping vlan {vlan_id} cli
    * Added unconfigure_ip_igmp_snooping_vlan_vlanid API
        * API for no ip igmp snooping vlan {vlan_id} cli
    * Added configure_service_performance
        * API for configure service performance on device
    * Added unconfigure_interface_switchport_block_address
        * API for unconfigure service performance on device
    * Added configure_key_config_key_password_encrypt
        * API for configure key config key password encrypt
    * Added unconfigure_key_config_key_password_encrypt
        * API for unconfigure key config key password encrypt
    * Added enable_ip_igmp_snooping_report_suppression api
        * Api to enable report-suppression
    * Added disable_ip_igmp_snooping_report_suppression api
        * Api to disable the report-suppression
    * Added unconfigure_global_source_template api
        * Api to unconfigure source template globally
    * Added configure_policy_map_type_service api
        * Api to configure policy map for pppoe service
    * Modified configure_ikev2_keyring
        * modified API to have Optional args
    * Added unconfigure_ppk_on_keyring
        * API to  unconfigure unconfigure_ppk_on_keyring
    * Added configure_modify_ikev2_profile
        * API to Configure and Modify configure_modify_ikev2_profile
    * Added unconfigure_modify_ikev2_profile
        * API to unonfigure and Modify configure_modify_ikev2_profile
    * Added configure_interface_lacp_fast_switchover
        * API for configure interface port channel lacp fast switchover
    * Added unconfigure_interface_lacp_fast_switchover
        * API for unconfigure interface port channel lacp fast switchover
    * Added configure_interface_lacp_max_bundle
        * API for configure interface port channel lacp max bundle
    * Added unconfigure_interface_lacp_max_bundle
        * API for unconfigure interface port channel lacp max bundle
    * Added configure_interface_snmp_trap_mac_notification_change
        * API for configure interface snmp trap mac-notification change
    * Added unconfigure_interface_snmp_trap_mac_notification_change
        * API for unconfigure interface snmp trap mac-notification change
    * Added configure_interface_default_snmp_trap_mac_notification_change
        * API for configure interface default snmp trap mac-notification change
    * Added configure_port_channel_persistent
        * API for configure port-channel persistent
    * Added configure_eigrp_router_configs
        * API for configure eigrp router configurations
    * Added unconfigure_eigrp_router_configs
        * API for unconfigure eigrp router configurations
    * Added configure_isis_router_configs
        * API for configure isis router configs
    * Added unconfigure_isis_router_configs
        * API for unconfigure isis router configs
    * Modified configure_eigrp_named_networks
        * API modified to handle eigrp router-id configuration
    * Added clear_ip_ospf_process
        * API to clear ip ospf process
    * Added configure_archive_default
        * API for configure archive default
    * Added configure_archive_path
        * API for configure archive path
    * Added unconfigure_archive_path
        * API for unconfigure archive path
    * Added configure_archive_maximum
        * API for configure archive maximum
    * Added unconfigure_archive_maximum
        * API for unconfigure archive maximum
    * Added configure_archive_rollback
        * API for configure archive rollback
    * Added unconfigure_archive_rollback
        * API for unconfigure archive rollback
    * Added configure_archive_time_period
        * API for configure archive time period
    * Added unconfigure_archive_time_period
        * API for unconfigure archive time period
    * Added configure_archive_write_memory
        * API for configure archive write memory
    * Added unconfigure_archive_write_memory
        * API for unconfigure archive write memory
    * Added API configure_ipv6_eigrp_named_networks
        * API to configure eigrp in address family ipv6
    * Added API configure_udld_aggressive_port
        * API to Configure udld port aggressive
    * Added configure_udld_enable
        * API to enable udle global configs
    * Added configure_vrf_ipv6_eigrp_named_networks
        * API to configure ipv6 eigrp with vrf
    * Added unconfigure_udld_enable
        * API to disable udle global configs
    * Added unconfigure_udld_port_aggressive API
        * API to unconfigure udld aggressive on interface
    * Added clear_macro_auto_configs
        * API for configuring clear macro auto configuration
    * Added configure_software_auto_upgrade
        * API for configure software auto-upgrade
    * Added unconfigure_software_auto_upgrade
        * API for unconfigure software auto-upgrade
    * Added power_supply_on_off
        * API for performing on/off on power supply slot on as switch
    * Added configure_bgp_redistribute_internal
        * API for configure bgp redistribute internal
    * Added unconfigure_bgp_redistribute_internal
        * API for unconfigure bgp redistribute internal
    * Added configure_redestribute_ospf_metric_in_bgp
        * API for configure bgp redistribute ospf metric
    * Added unconfigure_redestribute_ospf_metric_in_bgp
        * API for unconfigure bgp redistribute ospf metric
    * Added configure_interface_ip_tcp_adjust_mss
        * API for configure interface ip tcp adjust mss
    * Added unconfigure_interface_ip_tcp_adjust_mss
        * API for unconfigure interface ip tcp adjust mss
    * Added configure_interface_ipv6_tcp_adjust_mss
        * API for configure interface ipv6 tcp adjust mss
    * Added unconfigure_interface_ipv6_tcp_adjust_mss
        * API for unconfigure interface ipv6 tcp adjust mss
    * Modified configure_routing_static_route
        * Added check to configure dhcp default gateway for a route
    * Added configure_switch_priority
        * API to configure priority for a switch on stack
    * Added get_dir_byte_total
        * API to get the total and free bytes for directory
    * Added configure_logging_monitor_debugging
        * New API to configure logging monitor debugging
    * Added configure_logging_buffered_debugging
        * New API to configure logging buffered debugging
    * Added enable_debug_ilpower_event
        * New API to enabling the debug ilpower event
    * Added configure_ospfv3_max_lsa_limit
        * API for configure the ospfv3 max lsa limit
    * Added configure_ospf_max_lsa_limit
        * API for configure the ospf max lsa limit
    * configure_bgp_neighbor_remote_as_fall_over_as_with_peergroup
        * API for configure the bgp neighbor remote value with peergroup and fallover
    * Added
        * configure_macro_global_apply
        * configure_ip_igmp_snooping_vlan_static
        * unconfigure_ip_igmp_snooping_vlan_static
        * configure_snmp_server_manager
        * unconfigure_snmp_server_manager
    * Added configure_policy_map_with_pps
        * API for configure policymap and classname and policerate with pps
    * Added configure_igmp_snooping_tcn_flood API
        * API to configure ip igmp snooping tcn flood
    * Added unconfigure_igmp_snooping_tcn_flood API
        * API to unconfigure ip igmp snoopint tcn flood
    * Added configure_ipv6_mld_snooping_tcn_flood API
        * API to configure ipv6 mld snooping tcn flood
    * Added unconfigure_ipv6_mld_snooping_tcn_flood API
        * API to unconfigure ipv6 mld snooping tcn flood
    * Added configure_switchport_trunk_allowed_vlan_remove
    * Added configure_switchport_trunk_allowed_vlan_except
    * Added configure_tunnel_with_ipsec
        * Api to configure tunnel_protection under tunnel interface
    * Added verify_tunnel_protection
        * API to verify if tunnel is configured with tunnel protection
    * Added verify_ipsec_tunnel_status
        * API to verify ipsec tunnel status
    * Added get_crypto_ipsec_tunnel_counter
        * API returns counters for show crypto interface tunnel details
    * Modified configure_ospf_networks
        * API for configure the ospf network with bfd details
    * Added configure_ospfv3_redistributed_connected
        * API for ospfv3 redistribute connected interfaces
    * Added unconfigure_router_bgp api
        * Api to unconfigure router bgp
    * Added unconfigure_udld_agressive api
        * Api to unconfigure udld aggressive
    * Added unconfigure_udld_message_time api
        * Api to unconfigure udld message time
    * Added unconfigure_router_ospf api
        * Api to unconfigure router ospf
    * Added configure_ip_igmp_ssm_map_query_dns api
        * Api to configure ip igmp ssm map query dns
    * Added unconfigure_ip_igmp_ssm_map_query_dns api
        * Api to unconfigure ip igmp ssm map query dns
    * Added API for configure_acl_with_src_dsc_net
        * API to config source and destination networks
    * Added API for unconfigure_acl_with_src_dsc_net
        * API to unconfig source and destination networks
    * Modified config_interface_isis
        * API for configure the isis interface with mtu value
    * Added configure_isis_network_type
        * API for configure the isis network type
    * Added configure_isis_redistributed_connected
        * API for isis redistribute the connected interfaces
    * Added configure_lisp_enhanced_forwarding
        * API for configuring enhanced forwarding under lisp
    * Added unconfigure_lisp_enhanced_forwarding
        * API for unconfiguring enhanced forwarding under lisp
    * Added configure_lisp_l2_flooding
        * API for configuring l2 flooding under lisp
    * Added uconfigure_lisp_l2_flooding
        * API for unconfiguring l2 flooding under lisp
    * dhcp
        * unconfigure_ip_dhcp_snooping_trust
    * multicast
        * Added configure_ip_igmp_ssmmap_static
    * Added configure_boot_level_licence api
        * Api to configure boot level license
    * Added configure_ipv6_nd_raguard_on_interface API
        * API for configuring ipv6 nd raguard on interface
    * Added unconfigure_ipv6_nd_raguard_on_interface API
        * API for unconfiguring ipv6 nd raguard on interface
    * Added configure_device_tracking_on_interface API
        * API for configuring device-tracking on interface
    * Added unconfigure_device_tracking_on_interface API
        * API for unconfiguring device-tracking on interface
    * Added configure_ipv6_dhcp_guard_on_interface API
        * API for configuring ipv6 dhcp guard on interface
    * Added unconfigure_ipv6_dhcp_guard_on_interface API
        * API for unconfiguring ipv6 dhcp guard on interface
    * Added configure_interface_template_with_default_ipv6_nd_raguard_policy API
        * API for configuring ipv6 nd raguard on template
    * Added configure_interface_template_with_default_device_tracking_policy API
        * API for configuring device-tracking on template
    * Added verify_show_template API
        * API for verifying template name and bound interface
    * Added verify_show_template_empty API
        * API for verifying template is empty
    * Added enable_license_smart_authorization_return
        * API to enable license smart authorization return
    * Added enable_license_smart_clear_eventlog
        * API to enable license smart clear eventlog
    * Added execute_stack_power
        * APIs execute_stack_power to enable stack power
    * Added execute_diagnostic_start_switch_test
        * APIs execute_diagnostic_start_switch_test to nable diagnositc start
    * Added configure_enable_secret_password and unconfigure_enable_secret_password
        * APIs to enable and disable the enable mode login
    * Added configure_line_vty and unconfigure_line_vty
        * APIs to enable and disable line vty specific to vty modes
    * Added configure_diagnostic_monitor_switch and unconfigure_diagnostic_monitor_switch
        * APIs to configure diagnostic monitor sessions in switch
    * Added configure_diagnostic_schedule_switch and unconfigure_diagnostic_schedule_switch
        * APIs to configure the scheduled diagnostic enablement
    * Added configure_pae
        * API for configure product analytics
    * Added unconfigure_pae
        * API for unconfigure product analytics
    * Added configure_license_smart_transport_smart
        * API for configure smart transport smart
    * Added unconfigure_license_smart_transport
        * API for unconfigure smart transport
    * Added execute_test_platform_sw_product_analytics_report
        * API for generating product analytics report
    * Added execute_test_platform_sw_product_analytics_send
        * API for pushing product analytics report to smart agent for generating rum report
    * Added execute_test_license_smart_telemetry_show
        * API for show rum report which contains analytics report
    * Added execute_license_smart_sync_all
        * API for sending rum report to cloud server
    * Added execute_test_telemetry_show_logging
        * API for show logging output without parsing
    * Added execute_test_license_smart_dev_cert_enable
        * API for enable dev certification
    * Added execute_show_license_boot_level_config
        * API for show license boot level config
    * Added execute_show_license_dev_cert
        * API for show license certification if dev is enabled
    * Added execute_show_license_rum_id_telemetry
        * API for show telemetry entries only in show license rum id all
    * Added get_actv_switch
        * API for getting the current active switch
    * Added get_system_redundancy_states
        * API for getting the system redundancy state
    * Added get_the_number_of_telemetry_report_in_system
        * API for getting the number of telemetry report and report list
    * Added get_kpi_value_in_show_kpi_report_id
        * API for getting kpi value given report id and kpi name
    * Added verify_telemetry_enabled
        * API to verify if telemetry/pae is enabled
    * Added verify_telemetry_report_in_show_summary
        * API to verify telemetry report id is in show summary
    * Added verify_telemetry_report_kpi_in_show_kpi_summary
        * API to verify telemetry report and kpi name are in show kpi summary
    * Added verify_smart_account_is_activated
        * API to verify smart account is activated
    * Added verify_license_usage
        * API to verify at least 1 license is in use
    * Added verify_license_boot_level_configured
        * API to verify license boot level is configured
    * Added verify_license_smart_transport_configured
        * API to verify license smart transport smart is configured
    * Added verify_mpls_summary_label
        * API to check stack label id value and label value
    * Added verify_mpls_summary_lspa
        * API to check mpls lspa value and bgp value
    * Clear crypto ikev2 stats
        * API for "clear crypto ikev2 stats"
    * Added configure_vrrp_version_on_device
        * API for configure the vrrp version
    * Added configure_vrrp_on_interface
        * API for configure the vrrp configuration on interface
    * Added config_link_local_ip_on_interface
        * API for config the link local ipv6 address
    * Added unconfigure_ipv6_acl api
        * Removes complete ACL config for the acl specified
    * Added mopdify_pbr_route_map
        * Modifies existing route-map by removing ACL or action sepcified.
    * Added configure_ip_prefix_list_deny_permit
        * API for configure ip prefix list permit/deny
    * Added unconfigure_ip_prefix_list_deny_permit
        * API for unconfigure ip prefix list permit/deny
    * Added configure_ip_prefix_list_description
        * API for configure ip prefix list description
    * Added unconfigure_ip_prefix_list_description
        * API for unconfigure ip prefix list description
    * Added configure_ip_prefix_list_seq
        * API for configure ip prefix list sequence
    * Added unconfigure_ip_prefix_list_seq
        * API for unconfigure ip prefix list sequence
    * Added configure_distribute_prefix_list_under_ospf
        * API for configure distribute prefix list under ospf
    * Added unconfigure_distribute_prefix_list_under_ospf
        * API for unconfigure distribute prefix list under ospf
    * Added redistribute_bgp_metric_route_map_under_ospf
        * API for redistribute bgp metric route-map under ospf
    * Added API configure_parameter_map_subscriber
    * Added API 'configure_nve_interface_group_based_policy' in evpn
    * Added API 'unconfigure_nve_interface_group_based_policy' in evpn
    * Modified configure_eigrp_networks
        * API for configure the eigrp network with bfd value
    * Added configure_eigrp_redistributed_connected
        * API for eigrp redistributed the connected interfaces
    * Added configure_eigrp_named_networks_with_af_interface
        * API for configure the eigrp named network with af interface
    * Added configure_mac_global_address_table_static
        * API for configure global mac address-table static
    * Added unconfigure_mac_global_address_table_static
        * API for unconfigure globle mac address-table static
    * Added configure_mac_global_address_table_notification_change
        * API for configure mac global address-table notification change
    * Added unconfigure_mac_global_address_table_notification_change
        * API for unconfigure mac global address-table notification change
    * Added configure_mac_address_table_notification_change
        * API for configure mac address-table notification change
    * Added unconfigure_mac_address_table_notification_change
        * API for unconfigure mac address-table notification change
    * Added configure_default_mac_global_address_table_notification_change
        * API for configure default mac global address-table notification change
    * Added configure_sdm_prefer_custom_fib and configure_sdm_prefer_core API
        * API for configuring sdm prefer custom fib and sdm prefer core cli
    * Added unconfigure_bfd_value_on_interface
        * API for unconfigure the bfd value on interface
    * Added enable_bfd_on_isis_ipv6_address
        * API for enable the bfd for isis ipv6 address
    * Added disable_bfd_on_isis_ipv6_address
        * API for disable the bfd for isis ipv6 address
    * Added configure_pim_ssm_default
        * API to configure pim ssm default
    * Added unconfigure_pim_ssm_default API
        * API to unconfigure pim ssm default
    * Added unconfigure_license_smart_reservation
        * API to unconfigure license smart reservation
    * Added configure_license_smart_transport_off
        * API to configure license smart transport off
    * Added configure_ip_domain_timeout
        * API to configure ip domain timeout
    * Added configure_platform_shell
        * API to platform shell
    * Added configure_ip_http_authentication_local
        * API to ip http authentication local
    * Added configure_ip_domain_name
        * API to ip domain name
    * Added configure_ip_domain_name_vrf_mgmt_vrf
        * API to ip domain name vrf mgmt-vrf
    * Added configure_ip_name_server_vrf_mgmt_vrf
        * API to ip name-server vrf mgmt-vrf
    * Added configure_ip_http_client_source_interface_vlan_domain_lookup
        * API to ip http client source-interface vlan domain lookup
    * Added unconfigure_service_internal
        * API to unonfigure service imternal
    * Added configure_ip_http_client_source_interface
        * API to ip http client source-interface
    * Added configure_ip_http_client_source_interface_vlan_domain_lookup_name_server_vrf_mgmt_vrf
        * API to ip http client source-interface vlan domain lookup
    * Added configure_subscriber_template
        * added to configure subscriber template
    * Added configure_call_home_reporting
        * API to configure call home reporting
    * Added API verify_ipv6_intf_ip_address_notexist to verify if given IPv6 address not exist on given interface
    * Added configure_monitor_capture_without_match API
        * API for configuring monitor capture {capture_name} interface {interface} {direction} cli
    * Added configure_monitor_capture_buffer_size API
        * API for configuring monitor capture {capture_name} buffer size {size} cli
    * Added configure_monitor_capture_limit_packet_len API
        * API for configuring monitor capture {capture_name} limit packet-len {length} pps {pps} cli
    * Added unconfigure_monitor_capture_without_match API
        * API for unconfiguring monitor capture {capture_name} interface {interface} {direction} cli
    * Added unconfigure_monitor_capture_buffer_size API
        * API for unconfiguring monitor capture {capture_name} buffer size cli
    * Added unconfigure_monitor_capture_limit_packet_len API
        * API for unconfiguring monitor capture {capture_name} limit packet-len cli
    * Added configure_monitor_capture_match API
        * API for configuring monitor capture {capture_name} ipv4 any any cli
    * Added configure_event_manager_applet_event_none api
        * Api to configure event none to specific event manager applet
    * Added configure_action_syslog_msg api
        * Api to configure action syslog message on event manager applet
    * Added configure_action_force_switchover api
        * Api to configure action force-switchover on event manager applet
    * Added configure_label_mode_all_explicit_null
        * API to configure label mode all explicit null

* added execute_switch_priority
    * API to execute the switch priority

* blitz
    * Class GnmiNotification has been broken down into 3 classes with each class being responsible for 1 of the 3 modes (ONCE, POLL, STREAM). So now we have
        * GnmiSubscribe - base class for main 3
        * GnmiSubscribeOnce(GnmiSubscribe)
        * GnmiSubscribePoll(GnmiSubscribe)
        * GnmiSubscribeStream(GnmiSubscribe)
    * Added transaction_time option that can be passed via format. Option specifies required time in seconds between sending request and getting response. If not set, check will not be performed.
    * Added GNMI POLL request implementation
        * Added polls_number option that indicates number of POLL requests to send. Default to (stream_max // sample_interval) - 1. Only used in POLL mode.
    * Added updates_only option to Gnmi, which is a boolean that causes the server to send only updates to the current state in sbuscrbition.

* sdk/powercycler
    * Added cli powercycler to support custom cli powercycle commands.
    * Modified raritan-px2_v3 to raritan-px2 and changed the connection_type to snmpv3.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* sdk/terminal_server
    * Fixed the terminal_server port values to allow to use either str, int or a list.

* iosxe
    * Modify configure_ip_igmp_static_group API
        * Modify the interface and vlan argument
    * Modify configure_ip_igmp_join_group API
        * Modify the interface and vlan argument
    * Modified API fix_verify_ipv6_intf_ip_address
        * Fixed verification when ipv6 is not configured to address traceback that was raised in such scenario
    * Modified configure_bba_group API
        * Modified configure_bba_group API to configure service profile for virtual template
    * Updated the power inline API
        * Added four-pair power inline mode in the existed API by passing that in an if-condition
    * Added check condition in configure_ipsec_transform_set
        * API to config transform_auth is none and when auth bit is not None.
    * Added reverse route to ip sec profile
        * Added check to config reverse route command.
    * Modified configure_ospfv3 api
        * Modified configure_ospfv3 API to configure additional address family changes
    * Fix broken tests
        * Modified tests for `configure_archive_time_period`,
    * Modified configure_bgp_address_advertisement
        * Updated address_family to suppport ipv6
    * Modified configure_router_bgp_maximum_paths
        * updated api to support address_family
    * Fixed iosxe switchover function
    * Modified verification api verify_tunnel_protection
        * Added check for tunnel status
    * Modified configure interface monitor session to include ipv4, vlan, origin ipv6 and ipv6 address.
    * Fixed  configure_ospfv3 api
        * Fixed  address family command to configure ospfv3 configuration
    * Modified configure_pbr_route_map api
        * Introduced support for configuring ipv6 parameters for route-map
    * Modified configure_lldp_interface to make lldp transmit and lld receive as optional configurations.
    * Modified unconfigure_lldp_interface to make lldp transmit and lld receive as optional unconfigurations.
    * Modified API verify_ipv6_intf_ip_address
        * Added functionality to retry verification in a given time interval and given frequency

* blitz
    * ON_CHANGE Subscription support for multiple paths.
    * Added
        * In order to fix the issue that some left over containers and/or list instances are not removed after a test case, two new Blitz actions, 'yang_snapshot' and 'yang_snapshot_restore' are added.
    * STREAM Subscribe fix.
    * Poll Subscribe Infinite Loop fix.
    * Returns Handling optimised.
    * Modified device name detection
        * Failed ON_CHANGE active subscriptions not being reported.
    * Make returns optional for GNMI Subscribe and Get operation

* iosxe/platfrom
    * Added unconfigure_system_ignore_startupconfig_switch_all
    * Added configure_virtual_service_vnic_gateway_guest_ip_address
    * Added configure_snmp_mib_bulkstat
    * Added configure_bulkstat_profile
    * Added unconfigure_bulkstat_profile

* iosxe/acl
    * Added configure_mac_access_group_mac_acl_in_out

* sdk
    * Added missing init file

* api
    * Fixed UT for below APIs relating to config error pattern update
        * configure_icmp_ip_reachable
        * config_ip_on_interface


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_identity_ibns API
        * Added template_name and other few parameters
    * Modified configure_service_policy API
        * Modified the name to configure_dot1x_service_policy as it was overlapping with another API




genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCableRpd
        * show cable rpd
        * show cable rpd {rpd_mac_or_ip}
    * Added ShowControllersEthernetControllerPortAsicStatisticsExceptionsSwitchAsicInRpf parser
        * for 'show controllers ethernet-controller port-asic statistics exceptions switch 1 asic 1 | in RPF'
    * Added ShowIpArpInspectionInterfaces
        * show ip arp inspection interfaces {interface}
    * Added Parser as below
        * ShowCispInterface
        * ShowCispSummary
        * ShowDeviceClassifierAttachedInterface
        * ShowDeviceClassifierAttachedMacAddress
        * ShowPlatformSoftwareFedSwitchActiveVpSummaryVlan
        * ShowPlatformSoftwareWiredClientSwitchActiveFo
        * ShowCispClients
    * Modified parser
        * ShowDeviceSensor to include 2 more commands with same output
    * Added ShowIsisMicroloopAvoidance
        * show isis microloop-avoidance flex-algo
    * Added ShowCdp Parser
        * Parser for "show cdp"
    * Added ShowMacAddressTableNotificationChange parser
        * show mac address-table notification change
    * Added ShowMacAddressTableNotificationChangeInterface parser
        * show mac address-table notification change interface {interface}
    * Added ShowPlatformPmInterfaceNumbers
        * 'show platform pm interface-numbers'
    * Added ShowLoggingOnboardSwitchDetail parser
        * for 'Show logging onboard switch {switch_num} {feature} detail'
    * Added ShowLoggingOnboardSwitchMessageDetail parser
        * for 'Show logging onboard switch {switch_num} Message detail'
    * Added ShowIpIgmpSnoopingDetail
        * show ip igmp snooping detail
    * Added ShPlatformSoftwareFedActiveVpSummaryInterfaceIf_id
        * show platform software fed active vp summary interface if_id {interface_id}
    * Added ShSoftwareFed
        * 'show platform software fed switch active ifm if-id'
    * Added parser ShowDeviceClassifierAttachedInterfaceDetail
        * show device classifier attached interface {interface} detail
    * Added ShowEtherChannelDetail Parser
        * Parser for "show etherchannel {channel_group} detail"
    * Added ShowIpIgmpVrfSnoopingGroups Parser
        * Parser for "show ip igmp vrf {vrf} snooping groups"
    * Added PingIpv6 Parser
        * Parser for "ping ipv6 {addr}"
    * Added ShowCallHome
        * show call-home parser
    * Added ShowInstallUncommitted
        * show install uncommitted
    * Added ShowVtemplate parser
        * Parser for "show vtemplate"
    * Added ShowProductAnalyticsKpiSummary
        * show product-analytics kpi summary
    * Added ShowProductAnalyticsReportSummary
        * show product-analytics report summary
    * Added ShowProductAnalyticsKpiReportId
        * show product-analytics kpi report {report}
    * Added ShowL2fibOlist
        * show l2fib output-list {id}
    * Added ShowLoggingOnboardSwitchEnvironmentContinuous Parser
        * Parser for "show logging onboard switch {switch_num} environment continuous"
    * Added ShowIpDhcpExcludedAddresses Parser
        * show ip dhcp excluded-addresses all
        * show ip dhcp excluded-addresses vrf {vrf}
        * show ip dhcp excluded-addresses pool {pool}
    * Added ShowLoggingOnboardSwitch Parser
        * Parser for "show logging onboard switch {switch_num} {feature}"
    * Added ShowLicenseAuthorization Parser
        * Parser for "ShowLicenseAuthorization"
        * Parser for "ShowDiagnosticStatus"
        * Parser for "ShowPlatformHardwareFedSwitchActiveFwdAsicResourceAsicAllCppVbinAll"
    * Added ShowPlatformUsbStatus Parser
        * Parser for "show platform usb status"
    * Added ShowHwModuleUsbflash1Security Parser
        * Parser for "show hw-module usbflash1 security status"
    * Added ShowVmiNeighborsDetail parser
        * Parser for "show vmi neighbors detail"
    * Added ShowPlatformSoftwareFedSwitchActiveAcl
        * show platform software fed switch active acl counters hardware | include Ingress IPv4 Forward
    * Added ShowPlatformSoftwareBpCrimsonStatistics
        * show platform software bp crimson statistics
    * Added parser
        * Added ShowInterfacesCountersErrors
    * Added ShowCableRpd
        * show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities
    * Added ShowCallHomeStatistics
        * show call-home statistics
    * Added ShowTemplateTemplate
        * show template {template}
    * Added ShowIpv6MldSnoopingMrouter vlan
        * Added parser for "show ipv6 mld snooping mrouter vlan {vlan id}"
    * Added ShowInstallCommitted
        * show install committed
    * Added ShowLoggingOnboardRpActiveUptimeDetail parser
        * show logging onboard Rp active uptime detail
    * Added ShowSdmPreferCustom
        * added new parser for cli 'show sdm prefer custom'
    * Added ShowMonitorCaptureBufferDetailed
        * added new parser for cli 'show monitor capture {capture_name} buffer detailed'
    * Added ShowCableRpdIpv6
        * show cable rpd ipv6
        * show cable rpd {rpd_mac} ipv6
        * show cable rpd {rpd_ip} ipv6
        * show cable rpd {tengig_core_interface} ipv6
        * show cable rpd slot {lc_slot_number}  ipv6
    * Added ShowCefInterface Parser
        * Parser for "show ipv6 mld groups summary"
    * Added ShowControllersPowerInlineModule
        * show controllers power inline module <module_number>
    * Added ShowEigrpAddressFamilyIpv6VrfNeighbors Parser
        * Parser for "show eigrp address-family ipv6 vrf {vrf} {num} neighbors {interface}"
    * Added  ShowInstallInactive
        * show install inactive
    * Added ShowIpOspfNeighbor
        * Added parser support for 'show ip ospf <proccess_id> neighbor'
        * Added parser support for 'show ip ospf <proccess_id> neighbor {interface}'
    * Added ShowPppAll parser
        * Parser for "show ppp all"
    * Added ShowEtherchannelPortChannel
        * Parsre for "show etherchannel <number> port-channel"
    * Added ShowEtherchannelProtocol
        * Parser for "show etherchannel protocol"
    * Added ShowPortSecurityInterfacesAddressVlan
        * show port-security interfaces {interface} address vlan
    * Added ShowMemoryDebugIncrementalLeaks Parser
        * Parser for "show memory debug incremental leaks"
    * Added ShowPlatformSoftwareMonitorSession
        * Added parser for "show platform software monitor session {session}"
    * Added ShowVlanPrivate-Vlan
        * Added parser for "Show Vlan Private-Vlan"
        * Added parser for "Show Vlan Private-Vlan Type"
    * Added ShowIpMfibSummary
        * Added parser for "Show Ip Mfib Summary"

* added showiparpinspectionlog
    * show ip arp inspection log

* iosxr
    * Added ShowCdp
        * added new parser for cli 'show cdp'

* rpd
    * Added new os type RPD
    * Added parser
        * Added ShowBcmRegisterWbfftConfig

* added showpowerinlinemodule
    * Parser for "show power inline module {module}"

* added show device classifier profile type custom
    * Added parser for "show device classifier profile type custom"


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpIgmpSnoopingGroups
        * Fixed reg ex pattern match and added a unit test
    * Added
    * Modified ShowIpMroute
        * Modified p5 to support ipv6 address too
    * Modified ShowCdpNeighbors
        * Added total_entries parameter.
    * Modified ShowPlatformSoftwareFactoryResetSecureLog
        * Added Optional parameter status to schema
    * Modified ShowChassis where redun_port_type is made optional key.
    * Modified ShowEtherchannelPortChannel
        * Changed one of the pattern to match port_channel properly
        * Made 'gc' key as optional
    * Modified ShowEtherChannelDetail
        * Made 'last_port_bundled' and 'last_port_unbundled' keys as optional
    * Modified ShowL2vpnEvpnEthernetSegmentDetail
        * Handle case where RD is shown as "Not set"
    * Modified ShowCryptoIkev2Stats Added Quantum resistance line to parser.
    * Modified ShowBgpSuperParser
        * Modified regexp to consider statuscode with astrick followed by m so that it will take other routes and rds
    * Modified ShowIpRoute
        * Updated source_protocol_dict to support nat dia routes with type "n" and "Nd"
    * Modified ShowCryptoIkev2SaDetail Added Quantum resistance line of code to parser.
    * Modified ShowIsisRib
        * updated regex to accept alphanumberic as isis level
    * Modified ShowL2fibBridgedomainAddressUnicast
        * Support Adjacency and PD_Adjacency with multiple PL (have trailing " ...")
    * Modified ShowPlatformResources
        * Added control Processor and rp/esp as optional
    * Modified ShowPlatformSoftwareCpmSwitchB0ControlInfo
        * Added regular expression p1_2 to accomodate the change in the ouput.
    * Modified ShowLoggingOnboardSwitchActiveStatus
        * modified code to match code for not having switch_num
    * Modified ShowLoggingOnboardSwitchActiveUptimeDetail
        * modified code to match code for not having switch_num
    * Modified ShowSpanningTreeInterfaceDetail
        * Fix the parser issue. Add additional key.
    * Modified ShowPlatformResources
        * updated to print full interface name instead of short form
    * Modified ShowPlatformSoftwareMonitorSession
        * Fixing optional keys and value format
    * Modified ShowArchive
        * Added total_entries parameter.
    * Modified ShowVrrpBrief
        * Parser for show vrrp brief
    * Added
        * show template
        * show service-template
        * show redundancy config-sync failures mcl
    * Modified ShowBgpDetailSuperParser
        * Fixed regex pattern p6_3 to accommodate 3 update-groups.
        * Added new golden output txt and expected.py with 3 update-groups.
        * Fixed golden output 4 with the right route info and update-groups.
        * Added update groups item to ShowIpBgpAllDetail and ShowIpBgpDetail expected outputs.
    * Modified ShowCallHomeMailServerStatus
        * Included exception in Show call-home mail-server status
    * Modified ShowWirelessClientMacDetail
        * added inital support for fabric-enabled clients
    * 9600
        * Modified ShowPlatformSwitchStandbyTcamUtilization
            * Modified switch to a dynamic variable to avoid conflicts
    * Modified ShowIdpromInterface.
    * Added the parser in the proper file show_idprom.py.
    * Modified ShowLicenseTechSupport as per the output change in latest polaris version.
    * Added the keys device_telemetry_report_summary, data_channel, reports_on_disk in schema.
    * Added  the regular  expression p14.
    * Implemented a nonbackwards compatible change in order to fix the ShowIsisDatabase parser
        * Fixed ShowIsisDatabase parser to handle multiple interfaces under a single device
        * Modified the Schema to store interfaces in a list instead of a dict ('is_dict' --> 'is_list')
        * Updated all ShowISISDatabaseVerbose, ShowIsisDatabaseDetail, and ShowIsisDatabase tests to verify output with multiple interfaces under a single device

* show romvar switch <switch_number>

* deleted the duplicate parser under iosxe/show_platform.py and iosxe/c9300/show_platform.py.


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInterfacesSwitchport parser
        * Corrected the ethertype section



