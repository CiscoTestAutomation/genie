January 2026
==========

 - Genie v26.1 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v26.1 
    ``genie.libs.health``, v26.1 
    ``genie.libs.clean``, v26.1 
    ``genie.libs.conf``, v26.1 
    ``genie.libs.filetransferutils``, v26.1 
    ``genie.libs.ops``, v26.1 
    ``genie.libs.parser``, v26.1 
    ``genie.libs.robot``, v26.1 
    ``genie.libs.sdk``, v26.1 
    ``genie.telemetry``, v26.1 
    ``genie.trafficgen``, v26.1 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* harness
    * Added --exclude-trigger-uids and --exclude-verification-uids arguments
        * New CLI arguments to exclude specific triggers and verifications from execution
        * Excluded triggers/verifications are filtered during discovery phase



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean/stages/deletefiles
    * Added timeout parameter to delete_files method to specify timeout for delete operation.

* iosxe
    * RommonBoot Stage
        * Added retry functionality for TFTP boot with configurable tftp_boot_max_attempts and tftp_boot_sleep_interval parameters
        * Default 3 attempts with 30 second intervals between retries
        * Applies to iosxe, cat9k, and ie3k platforms

* iosxe/cat9k/stackwise_virtual
    * New stage for StackWise Virtual configuration

* clean-pkg
    * Added image handler for RommonBoot stage to set image in rommon_boot section
    * iosxe/cat9k
        * updated the schema to make image as Optional parameter in RommonBoot stage


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean-pkg
    * Added support for new flag overwrite_if_size_different to allow conditional overwriting only when the existing file’s size differs.

* iosxe
    * RommonBoot Stage
        * Improved ROMMON TFTP logging to report each ROMMON variable as it is set, making ROMMON boot failures easier to debug.

* clean/iosxe/test_connect_device_rommon
    * Removed the extra comma in the FIND_BOOT_IMAGE setting to fix the UT.

* installimage stage
    * N9k
        * Added check_reload logic to detect if device auto reloads after image install and wait for device to reload.

* clean
    * IOSXE - ResetConfiguration
        * Re-initialize init commands after rollback in case they were removed

* clean/recovery/recovery
    * Added a check to verify the boot manual recovery process.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added
        * Added support for Dynamic Load Balancing (DLB)
        * Covers all possible configurations currently supported for feature dlb on NXOS



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* fileutils
    * Added retry mechanism on 'Permission denied' error during file transfer
        * When a file transfer fails due to permission issues, the utility now



genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health
    * Added functionality to move to enable mode before running health checks



genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_execute_set_memory_debug_incremental_starting_time
        * test_api_clear_cts_counters_ipv4
        * test_api_clear_cts_counters_ipv6
        * test_api_configure_cts_aaa_methods
        * test_api_configure_interface_cts_role_based_sgt_map
        * test_api_debug_platform_software_fed_switch_active_punt_packet_capture
        * test_api_debug_software_cpm_switch_pcap
        * test_api_debug_vdsl_controller_slot_dump_internal
        * test_api_disable_debug
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_cdp
        * test_api_unconfigure_cdp_holdtime
        * test_api_enable_cpp_system_default_on_device
        * test_api_execute_clear_control_plane
        * test_api_configure_device_sensor_filter_list_lldp
        * test_api_configure_hw_module_switch_number_usbflash
        * test_api_configure_service_private_config_encryption
        * test_api_cry_key_generate_rsa_encryption
        * test_api_hw_module_switch_num_usbflash_security_password
        * test_api_snmp_server_engine_id_local
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * cat9k/c9500/rev1/platform.py
        * Fix KeyError when merging standby RP redundancy data during platform learning

* iosxr
    * Modified Platform
        * Added full_slot to platform ops model


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* platform/nxos/rev2/platform.py
    * Added Rev2 platform support for transceiver slot parsing, Fan, and fixed logic for rp and lc



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_dhcp_snooping_verify_no_relay_agent_address
        * test_api_configure_interface_ip_dhcp_relay_information_option_vpn_id
        * test_api_configure_interface_ip_dhcp_relay_source_interface_intf_id
        * test_api_configure_interface_range_dhcp_channel_group_mode
        * test_api_configure_ip_dhcp_client
        * test_api_configure_ip_dhcp_client_vendor_class
        * test_api_configure_ip_dhcp_exclude_vrf
        * test_api_configure_ip_dhcp_pool
        * test_api_configure_ip_dhcp_pool_address
        * test_api_configure_ip_dhcp_restrict_next_hop
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified collect_install_log
        * Added timeout parameter (600s) to prevent timeout issues when collecting install failure logs
    * Modified collect_install_log (cat9k/c9300)
        * Added timeout parameter (600s) to prevent timeout issues when collecting install failure logs
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_cdp_interface
        * test_api_unconfigure_cdp_neighbors
        * test_api_unconfigure_cdp_timer
        * test_api_configure_ipv6_traffic_filter_acl
        * test_api_unconfigure_ipv6_traffic_filter_acl
        * test_api_clear_ip_bgp_ipv6_unicast
        * test_api_clear_ip_eigrp_neighbor
        * test_api_clear_ip_eigrp_traffic
        * test_api_configure_mpls_mtu
        * test_api_configure_switchport_vlan_mapping
        * test_api_unconfigure_switchport_vlan_mapping
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_device_policy_tracking
        * test_api_configure_device_tracking_logging
        * test_api_configure_source_tracking_on_interface
        * test_api_unconfigure_device_tracking_logging
        * test_api_configure_cts_manual
        * test_api_configure_dhcp_channel_group_mode
        * test_api_configure_dhcp_option43
        * test_api_configure_dhcp_pool
        * test_api_configure_dhcp_relay_short_lease
        * test_api_configure_dhcp_snooping_track_server_dhcp_acks
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * configure_bgp_neighbor_remote_as_fall_over_as_with_peergroup
        * configure_bgp_redistribute_internal
        * configure_bgp_redistribute_static
        * configure_bgp_refresh_max_eor_time
        * configure_bgp_route_reflector_client
        * configure_bgp_router_id_interface
        * configure_bgp_router_id_neighbor_ip_peergroup_neighbor
        * configure_bgp_router_id_peergroup_neighbor
        * configure_bgp_sso_route_refresh_enable
        * configure_bgp_update_delay
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * pki
        * Added more parameters to the configure_trustpool_policy api
    * ike
    * rommon/utils
        * Revert the change made in PR 3844 since it was breaking device recovery
    * routing
        * Fixed the cli in unconfigure_routing_static_route
    * Modified copy_file_with_scp to fix a Dialog case
        * Modified the copy file with scp method to handle file paths with spaces correctly
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_clear_controllers_ethernet_controller
        * test_api_unconfigure_hw_module_switch_number_usbflash
        * test_api_unconfigure_service_private_config_encryption (csdl)
        * test_api_disable_debug_pdm
        * test_api_set_platform_soft_trace_ptp_debug
        * test_api_configure_device_sensor_filter_list
        * test_api_configure_device_sensor_filter_spec
        * test_api_configure_device_sensor_notify
        * test_api_configure_radius_server_vsa
        * test_api_unconfigure_device_sensor_filter_list
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified configure_interface_ip_tcp_adjust_mss
        * Added no switchport as optional command before configuring tcp mss on routed interfaces
    * Modified configure_interface_ipv6_tcp_adjust_mss
        * Added no switchport as optional command before configuring tcp mss on routed interfaces
    * Modifying API execute_locate_switch in iosxe/ie3k.
        * Fixed issue where the API did not correctly locate the switch in certain scenarios.
    * Added API execute_stop_locate_switch in iosxe/ie3k.
        * New API to stop the locate switch process.
    * pki/configure
        * Delete the Trustpoint when it is in use, the function will handle the error and retry the import.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_ip_dhcp_snooping_database
        * test_api_configure_ip_dhcp_snooping_information_option
        * test_api_configure_ip_dhcp_snooping_information_option_allow_untrusted
        * test_api_configure_ip_dhcp_snooping_information_option_allow_untrusted_global
        * test_api_configure_ip_dhcp_snooping_limit
        * test_api_configure_ip_dhcp_snooping_verify_mac_address
        * test_api_configure_pnp_startup_vlan
        * test_api_configure_service_dhcp
        * test_api_create_dhcp_pool_withoutrouter
        * test_api_disable_dhcp_compatibility_suboption
    * Removed mock_data.yaml files for the above tests as they are no longer needed

* updated api unit tests
    * IOSXE
        * Updated unittests to new testing method
    * IOSXE
        * Updated unittests to new testing method
            * configure_aaa_accounting_network_default_start_stop_group
            * configure_masked_unmasked_credentials
            * configure_radius_attribute_policy_name_under_servergroup
            * unconfigure_mab_on_switchport_mode_access_interface
            * unconfigure_radius_attribute_policy_name_under_server
            * unconfigure_radius_attribute_policy_name_globally
            * unconfigure_radius_attribute_policy_name_under_servergroup
            * unconfigure_radius_interface
            * clear_ip_reflexive_list
            * config_extended_acl_with_evaluate
    * Removed mock_data.yaml files for config_extended_acl and the above files as they are not required as they are updated to new testing method.
    * Added __init__.py files to
        * configure_masked_unmasked_credentials
        * clear_ip_reflexive_list
        * config_extended_acl_with_evaluate
    * IOSXE
        * Updated unittests to new testing method
    * IOSXE
        * Updated unittests to new testing method
            * configure_bgp_vpn_import
            * configure_fall_over_bfd_on_bgp_neighbor
            * get_running_config_section_dict
            * unconfigure_route_map_route_map_to_bgp_neighbor
            * configure_mac_address_table_notification_change
            * configure_call_home_aaa_authorization
            * configure_call_home_mail_server
            * configure_call_home_profile_active
            * configure_call_home_profile_anonymous_reporting_only
            * configure_call_home_profile_destination_address
    * IOSXE
        * Updated unittests to new testing method
            * config_extended_acl_with_reflect
            * configure_bgp_eigrp_redistribution
            * configure_bgp_isis_redistribution
            * configure_bgp_l2vpn_evpn_rewrite_evpn_rt_asn
            * configure_bgp_l2vpn_route_map
            * configure_bgp_l2vpn_route_reflector_client
            * configure_bgp_log_neighbor_changes
            * configure_bgp_neighbor
            * configure_bgp_neighbor_advertisement_interval
            * configure_bgp_neighbor_filter_description

* nxos
    * SDK
        * libs/abstracted_libs/nxos/ha.py
            * Modified _perform_issu() to check switch syslog for non-disruptive ISSU completion
    * Added Advertise labelled local route support
        * A requirement for mpls to disable local labelled routes

* management
    * configure
        * Added support for switchport and vlan configuration in 'configure_management' API.

* sdk/triggers
    * blitz
        * Fixed negative configure test handling when expected_failure=True and configuration succeeds

* rommon/utils
    * Updated the boot_cmd to ENTER for C8KV grub mode to ensure proper booting

* fixed api configure_ikev2_proposal
    * ipsec

* fixed api configure_ipsec_profile

* utils
    * Updated `copy_to_device`, `copy_from_device` and `get_server_certificate_pem`
    * Added api get_proxy to get proxy information from device connections.

* iosxe/support/tech_support
    * Fixed the api to log the full traceback


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added iosxe interface API support for the CLI command
        * New API support for 'hardware_sublot_module_interface_statistics' CLI command to execute hardware sublot module interface statistics on IOSXE devices.
        * New API support for 'hardware_qfp_active_datapath_infrastructure_sw_cio' CLI command to hardware qfp active datapath infrastructure sw-cio on IOSXE devices.
        * New API support for 'hardware_qfp_active_datapath_utilization' CLI command to hardware qfp active datapath utilization on IOSXE devices.
        * New API support for 'execute_setup' CLI command to execute setup on IOSXE devices.
    * Update device_rommon_boot to support ignore_startup_config during device recovery
    * c9400
        * Updated the configure and unconfigure ignore_startup api to work for H/A devices.
    * Modified configure_ip_ssh_stricthostkeycheck API to support accept-new option
        * Enhanced API to support 'ip ssh stricthostkeycheck accept-new' CLI command with new accept_new parameter.
    * Modified unconfigure_ip_ssh_stricthostkeycheck API to support accept-new option
        * Enhanced API to support 'no ip ssh stricthostkeycheck accept-new' CLI command with new accept_new parameter.
    * Added API configure_interfaces_fcs to configure FCS on interfaces.
    * cat9kv
        * Added configure_bgp_aggregate_address api
        * Added clear_bgp_ipv6_dampening api
    * Added iosxe ipv6 API support for the CLI command
        * New API support for 'configure_ipv6_nd_reachable_time' CLI command to configure ipv6 nd reachable time on IOSXE devices.
        * New API support for 'unconfigure_ipv6_nd_reachable_time' CLI command to unconfigure ipv6 nd reachable time on IOSXE devices.
    * Added API get_active_rp_info to get the active route processor information
    * clear_cts_pac_all
        * Added support for 'clear cts pac all' command in IOSXE devices.
    * Added
        * configure_eap_profile_advanced
            * API to configure_eap_profile_advanced
        * configure_dot1x_eap_profile_on_interface
            * API to configure_dot1x_eap_profile_on_interface
        * unconfigure_dot1x_eap_profile_on_interface
            * API to unconfigure_dot1x_eap_profile_on_interface
        * configure_access_session_pqc_type
            * API to configure_access_session_pqc_type
        * unconfigure_access_session_pqc_type
            * API to unconfigure_access_session_pqc_type
    * Added api for configure_cts_sxp_connection_peer
        * Added new api configure_cts_sxp_connection_peer .
    * Added api for configure_cts_sxp_list_option
        * Added new api configure_cts_sxp_list_option .
    * Added api for unconfigure_cts_sxp_list_option
        * Added new api unconfigure_cts_sxp_list_option .
    * Added api for configure_cts_sxp_export_import_group_option
        * Added new api configure_cts_sxp_export_import_group_option .
    * Add configure_cdp_advertise_v2 API
        * New API to configure 'cdp advertise-v2' on device.
    * Add unconfigure_cdp_advertise_v2 API
        * New API to unconfigure 'no cdp advertise-v2' on device.
    * Add configure_interface_cdp_enable API
        * New API to configure 'cdp enable' on specified interface.
    * Add unconfigure_interface_cdp_enable API
        * New API to unconfigure 'no cdp enable' on specified interface.
    * Add get_cdp_neighbors_output API
        * New API to retrieve the output of 'show cdp neighbors' command.
    * Add get_cdp_neighbors_intf_detail_output API
        * New API to retrieve the output of 'show cdp neighbors <interface> detail' command.
    * Add configure_cdp_log_mismatch_duplex API
        * New API to configure 'cdp log mismatch duplex' on device.
    * Add unconfigure_cdp_log_mismatch_duplex API
        * New API to unconfigure 'no cdp log mismatch duplex' on device.
    * Add get_get_interface_switchport_output API
        * New API to retrieve the output of 'show interfaces <interface> switchport' command.
    * Add get_interface_controller_output API
        * New API to retrieve the output of 'show interface <interface> controller' command.
    * Added test_pppoe to platform-execute.py
        * New API support for 'test pppoe <session> <max> <addr>
    * Added iosxe interface API support for the CLI command
        * New API support for 'unconfigure_interface_media_type' CLI command to unconfigure interface media type on IOSXE devices.
        * New API support for 'verify_subslot_state' CLI command to verify subslot state on IOSXE devices.
        * New API support for 'get_interface_speed_config_range' CLI command to get interface speed config range on IOSXE devices.
    * Added API configure_mpls_static_binding_ipv4
    * Added API unconfigure_mpls_static_binding_ipv4
    * Added new api for execute_ingress_ping_sweep
    * Added API configure_mpls_ldp_label
    * Added API unconfigure_mpls_ldp_label
    * cat9kv
        * Added configure_autoboot api
        * Added configure_boot_manual api
        * Added configure_no_boot_manual api
    * Health
        * health_core
            * Updated the logic where health - core file check should ignore filesystem path.
    * Added new api for configure_trustpool_import_terminal
    * IR1K
        * IR1100
            * Added "get_recovery_details" API in rommon module to fetch recovery related information.
    * Added iosxe subslot oir API support for the CLI command
        * New API support for 'configure_hw_module_sub_slot_shutdown' CLI command to configure hw_module sub slot shutdown on IOSXE devices.
        * New API support for 'unconfigure_hw_module_sub_slot_shutdown' CLI command to unconfigure hw module sub slot shutdown on IOSXE devices.
        * New API support for 'hw_module_sub_slot_stop' CLI command to hw module sub slot stop on IOSXE devices.
        * New API support for 'hw_module_sub_slot_start' CLI command to hw module sub slot start on IOSXE devices.
        * New API support for 'hw_module_sub_slot_oir_power_cycle' CLI command to hw module sub slot oir power cycle on IOSXE devices.

* nxos
    * SDK
        * libs/abstracted_libs/nxos/ha.py
            * Allow _prepare_issu() to accept a local NXOS image path (e.g. bootflashnxos64-cs.10.4.6.M.bin)

* api utils
    * Added API support in api utils
        * New API support for 'get_interface_type_name' to get interface type name.

* sdk-pkg
    * iosxe/isr4k
        * Added new api 'execute_rommon_reset' to perform a rommon reset on the device

* iosxe/utils
    * password_recovery
        * Updated the api to include steps to reset the device in rommon mode during password recovery process.

* utils
    * Added new API `check_config_options` to check available configuration options for a given device model.

* iosxe/mcast/rev1
    * Added new rev1 directory and new logic to consolidate below APIs.
        * configure_pim_autorp_listener and configure_pim_auto_rp_listener consolidated to configure_pim_auto_rp_listener in rev1.
        * unconfigure_pim_autorp_listener and unconfigure_pim_auto_rp_listener consolidated to unconfigure_pim_auto_rp_listener in rev1.
    * Added Check duplicate logic to CI Pipeline to detect duplicate APIs.


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe/verify
    * Added a new API verify_no_boot_manual to verify the boot manual recovery process.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathPool schema and parser
        * Added schema and parser for show platform hardware cpp active feature nat datapath pool
    * Added ShowIpv6VirtualReassembly parser
        * 'show ipv6 virtual-reassembly'
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathTime parser.
        * Added parser for cli 'show platform hardware cpp active feature nat datapath time'.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfIdDetail
        * Added parser for 'show platform software fed switch security fed ipsg if-id {if-id} detail' command.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgIfId
        * Added parser for 'show platform software fed switch security fed security-fed ipv6sg if-id {if-id}' command.
    * Added ShowPlatformHardwareQfpActiveClassificationCceInterfaceBrief
        * Added show platform hardware qfp active classification cce interface brief parser and tests
    * Fixed parsing issue in ShowPlatformSoftwareAdjacencyNexthopIpfrr
        * Adj-ID field now supports hexadecimal values to prevent nexthop parsing failures
    * Added ShowIpOspfFast-reroutePrefix-summary
        * Added show ip ospf fast-reroute prefix-summary parser and tests
    * Added ShowCryptoAutovpnSession
        * Added schema and parser for show crypto autovpn session command.
    * Added ShowCryptoAutovpnSessionPeerno
        * Added schema and parser for show crypto autovpn session peerno {peerno} command.
    * Added ShowPlatformSoftwareNatFpActiveTranslation
        * 'show platform software nat fp active translation'
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpv6sgClear
        * Added parser for 'show platform software fed switch security fed ipv6sg clear' command.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpsgClear
        * Added parser for 'show platform software fed switch security fed ipsg clear' command.
    * Added ShowLoggingProcessFedInternalStartLastClearSwitchActive
        * Added schema and parser for show logging process fed internal start last clear switch active command.
    * Added ShowLoggingProcessFedInternalStartLastClearSwitchActive
        * Added schema and parser for show logging process fed internal start last clear switch active command.
    * Added ShowPolicyFirewallSessionsPlatformV6SourceAddress
        * show policy-firewall sessions platform v6-source-address {address}
    * Parser Updates
        * show running-config | section alarm
        * Added support for parsing 'show running-config | section alarm' command output.
    * Added Parser for parsers for below commands
        * 'show processes cpu platform profile DP'
        * 'show processes cpu platform profile CP'
        * 'show processes cpu platform profile SP'
    * Added ShowPlatformSoftwareAdjacencyNexthop-ipfrr
        * Added show platform software adjacency nexthop-ipfrr parser and tests
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathMap
        * 'show platform hardware cpp active feature nat datapath map'
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathStats parser.
        * Added parser for cli 'show platform hardware cpp active feature nat datapath stats'.
    * Fixed parsing of external OSPF routes in show ip ospf rib
        * Added support for Ext/NSSA routes with forward cost and tag fields
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathSessDump parser
        * 'show platform hardware cpp active feature nat datapath sess-dump'
    * Added ShowAccessListFqdnClient
        * Added parser for 'show access-list fqdn client' command.
    * Added ShowFQDNDatabaseFqdn
        * Added parser for 'show fqdn database fqdn' command.
    * Added ShowFQDNDebugStatistics
        * Added parser for 'show fqdn debug statistics' command.
    * Added ShowPlatformHardwareFedSwitchFwdAsicAbstractionPrintResourceHandle
        * Added parser for 'show platform hardware fed switch fwd asic abstraction print resource handle' command.
    * Solve parsing of repair path entries in show isis rib
        * Improved handling of repair path attributes to support both single and multiple flags (e.g. DS,DS,SR)
    * Added ShowCtsSxpExportImportGroupDetailed parser.
        * Added parser for cli 'show cts sxp export-import-group {role} detailed'.
    * Enchanced ShowCtsSxpConnections parser.
        * Enchanced parser for cli'show cts sxp connections'.
    * Added ShowPolicyFirewallSessionsPlatformDestinationPort
        * show policy-firewall sessions platform destination-port {port}
    * Added ShowPlatformHardwareCppActiveFeatureNatDatapathBind schema and parser
        * Added schema and parser for show platform hardware cpp active feature nat datapath bind
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAcl parser
        * Added rv1 parser for 'show platform hardware fed switch 1 fwd-asic insight ip_source_guard_acl' command.
    * Added ShowPlatformSoftwareIpFpActiveCefSummary
        * Added show platform software ip FP active cef summary parser and tests

* iosxe/rv1
    * Added ShowInterfacesTransceiver
        * Added show interfaces transceiver parser in rv1 for new device output format.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLoggingOnboardRpActiveUptime
    * Added regex pattern to accept chassis type
    * Modified ShowPlatformHardwareModuleInterfaceStatus
        * Schema supports both Optional l2_network and Optional l3_network keys
    * Modified ShowPlatformHardwareQfpActiveInterfaceIfName
        * 'show platform hardware qfp active interface if-name {interface}'
    * Modified ShowCableDiagnosticsTdrInt
        * Modified parser ShowCableDiagnosticsTdrInt in iosxe for show cable diagnostics tdr interface <interface name>
    * Modified ShowPlatformHardwareModuleInterfaceStatus
        * Schema supports both Optional vlan_mode and Optional native_vlan keys
    * Modified ShowMkaSessionDetail
        * 'show mka session detail'
    * Add ShowConnectionName parser
        * Added schema and parser for show connection name command.
    * Modified ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbDetail
        * 'show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'
    * Modified ShowInterfacesTrunk
        * Parser supports show interfaces <interface> trunk command.
    * Modified ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Added the keys stp_state_hw, gid, mac_learn in schema
        * Added the regexp p1_1 and the corresponding code.
    * Modified ShowMacsecStatusInterface
        * 'show macsec status interface {interface}'
    * Fixed parsing issue in 'show environment power all' command for IE9k devices
    * Modified ShowPolicyMapTypeInspectZonePairSession
    * Added regex pattern to match the ipv6 support for zonepair session
    * Modified ShowPlatformSoftwareInterfaceFpActive
        * 'show platform software interface fp active name {interface}'
    * ShowRomvar
        * Updated the variable random_num to optional
    * ShowCryptoIkev2SaDetail
    * Modified ShowCdp
    * Modified regex pattern to match the cdpv2 for "show cdp" command
    * Modified ShowCryptoSessionRemoteSchema
        * Modified parser ShowCryptoSessionRemoteSchema in iosxe for show crypto session remote <remote-ip>
    * Modified ShowNat64Statistics
        * 'show nat64 statistics interface {interface_name}'

* iosxe ie3k
    * Modified ShowEnvironmentAll
        * Fixed ShowEnvironmentAll parser in IOSXE IE3K platform.

* fixed parser to work with new funtionality changes
    * ShowCryptoIkev2Session

* fixed parser to work with new funtionality changes
    * ShowCryptoIpsecSaDetail

* fixed parser to work with new funtionality changes
    * ShowCryptoIpsecProfile
        * Fixed parser to work with new funtionality changes
    * ShowCryptoIkev2Proposal
        * Fixed parser to work with new funtionality changes
    * ShowCryptoIkev2Sa
        * Fixed parser to work with new funtionality changes
    * ShowCryptoIpsecSaIpv6Detailed
        * Fixed parser to work with new funtionality changes


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPolicyMapTypeSuperParser parser in show_policy_map.py
        * Add support for 'match' criteria and 'match_stats' under each class in policy map



genie.telemetry
"""""""""""""""
