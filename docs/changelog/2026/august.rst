August 2026
==========

August 25 - Genie v26.8
-----------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v26.8
    ``genie.lamp``, v26.8
    ``genie.libs.health``, v26.8
    ``genie.libs.clean``, v26.8
    ``genie.libs.conf``, v26.8
    ``genie.libs.filetransferutils``, v26.8
    ``genie.libs.ops``, v26.8
    ``genie.libs.parser``, v26.8
    ``genie.libs.robot``, v26.8
    ``genie.libs.sdk``, v26.8
    ``genie.telemetry``, v26.8
    ``genie.trafficgen``, v26.8




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie.conf.utils
    * Modified Converter.convert_tb
        * Snapshot source links once instead of repeatedly deriving target links during conversion.
        * Preserve private topology state owned by the converted testbed.

* ci
    * Added release-matrix builds for cythonized public alpha packages to pull request validation.

* genie.tests.json.test_make_json
    * Modified get_package_location editable-location test
        * Compare canonical paths so the test supports the macOS /var to /private/var symlink.
    * Modified get_package_location tests
        * Use unittest-compatible test cases so runAll discovers and executes the PEP 660 editable-package-location coverage.

* genie.json.make_json
    * Modified get_package_location
        * Resolve PEP 660 editable package source roots from direct_url.json before falling back to distribution locations.

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added the generic ``RecoveryImage`` clean stage.
        * Resolves recovery images from paths supplied by clean configuration.
        * Supports fast, optional file-size verification with the boolean ``verify_size`` option and exact MD5 verification with ``verify_md5``.
        * Supports protocol-aware server ports and clear copy-operation output.
        * Accepts optional pre-resolved transfer paths while retaining the original filesystem paths for size or MD5 verification.
        * Skips safely when a shared clean template invokes the stage for a device without recovery-image inputs or a golden-image target.
        * Discovers protocol-matching file-transfer servers and ports, supports multiple images and verify-only operation, copies images to golden-image targets, verifies target presence and optional size or MD5, and updates device recovery data.
        * Supports recovery from devices that boot through ROMMON.

* clean
    * Retry a complete Clean workflow for a device when configured device recovery restores the device after a stage failure.
    * Keep the failed or errored attempt visible as superseded, record recovery as a separate passed processor result, and let the retry attempt determine the final Clean result.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated InstallImage clean stage
        * Added ``verify_install_space`` step to ensure free space of ``install_space_factor`` (default 1.25) times the image size before running ``install add``.
    * Modified clean template
        * Increased the default ``install_remove_inactive`` timeout from 180 to 300 seconds.
    * Updated InstallRemoveInactive clean stage
        * Fail the step when install remove inactive times out instead of reporting it as passed.
    * Updated InstallImage clean stage
        * Recognize IE3K insufficient-space and install-add failure output.
        * Avoid collecting install logs before recoverable space and ISSU retries so device configuration remains unchanged for the retry.
        * Fail the step when space retries are exhausted instead of falling through silently.
    * Updated InstallImage clean stage
        * Call ``device.api.collect_install_log(reconnect=True)`` so the connection/state-machine resynchronization required after an install timeout is handled by the API instead of the clean stage.
        * Preserve the original install error when diagnostic recovery or log collection also fails.
    * Modified SetControllerMode clean stage
        * Fixed SetControllerMode so IOS XE devices that stop at ``grub>`` during ``controller-mode disable`` recover and continue booting instead of timing out.

* iosxe ie3k, cat9k, cat3k
    * Updated InstallImage clean stage
        * Added ``verify_install_space`` to ``exec_order``.

* clean
    * Preserve failed and errored Connect stage results when device recovery is enabled, so an unsuccessful recovery cannot hide the triggering failure.
    * Modified recovery_processor
        * Added separate reachability and recovery steps to device recovery processor reporting.

* generic clean stages
    * Use the ApplyConfiguration max_time value as the command timeout when copying running-config to startup-config, preserving the separate configuration timeout.

* linux
    * Modified run_configure to handle True or False return values
    * Modified simulate_ap_container to handle True or False return values

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* filetransferutils
    * Prevented credentials embedded in authenticated file-transfer URLs from being exposed in logs and error messages.

genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health
    * Moved device enable transitions to the parent process after parallel connectivity checks so Unicon state remains synchronized for subsequent health actions.

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* sdk
    * Added optional server-port support to ``copy_to_device`` and ``copy_from_device`` for HTTP(S) transfers.

* sdk-pkg
    * Added SDK API support for
        * `find_server_route_for_device_ip` - return structured server route metadata using the existing server route-selection policy for IPv4 and IPv6, with design-aligned fields and compatibility aliases, while skipping malformed routes and unusable interfaces.
        * `probe_tcp_host` and `probe_tcp_hosts` - probe local TCP endpoints with a stable structured reachability-result schema.
        * `probe_tcp_from_server` - probe endpoints from a Linux server using validated targets, structured command diagnostics, and an IPv4/IPv6- aware nmap-to-nc fallback policy.
    * Added unit test coverage for the new connectivity APIs.

* iosxe
    * Added configure_bfd_template_multi_hop
        * added api configure_bfd_template_multi_hop
    * Added unconfigure_bfd_template_multi_hop
        * added api unconfigure_bfd_template_multi_hop
    * Added configure_bfd_map
        * added api configure_bfd_map
    * Added unconfigure_bfd_map
        * added api unconfigure_bfd_map
    * Added vlan configure APIs for IOSXE.
        * API to configure_default_vtp_mode.
        * API to configure_vlan_state.
    * Added unit test coverage for the new API.
    * Added SDK API support for
        * get_show_spanning_tree_output
        * get_show_spanning_tree_interface_detail_output
        * get_spanning_tree_interface_cost
        * get_interface_spanning_tree_portfast_output
        * get_configure_spanning_tree_guard_root_output
        * get_configure_spanning_tree_mst_instance_output
        * get_spanning_tree_interfaces
    * Added unit test coverage for spanning-tree get APIs.
    * Added configure_policy_map_type_inspect
        * policy-map type inspect {policy_map_name}
        * class type inspect {class_map_name}
        * no inspect
        * no pass
        * no drop
        * {action} {log_param}
    * Added unconfigure_policy_map_type_inspect
        * no class type inspect {class_map_name}
        * no policy-map type inspect {policy_map_name}
    * Added unit test coverage for the new APIs.
    * Added configure_ip_vrf
        * added api configure_ip_vrf
    * Added startup-config verify APIs for IOSXE.
        * API to verify_show_startup_config_section.
    * Added unit test coverage for the new API.
    * Added cloud_mgmt verify APIs for Meraki/cloud management (show cloud-mgmt compatibility/migration, show romvar)
        * verify_cloud_monitoring_compatibility
        * verify_cloud_mgmt_compatibility
        * verify_cloud_mgmt_migration_details
        * verify_rommon_boot_device_mode
    * Added interface verify APIs for IOSXE.
        * API to verify_interfaces_trunk.
        * API to verify_show_interfaces_switchport.
    * Added unit test coverage for the new API.
    * Added configure_ipv6_mld_version
        * API to configure the IPv6 MLD version on an interface
    * Added unconfigure_ipv6_mld_version
        * API to unconfigure the IPv6 MLD version on an interface
    * Added configure_pim_spt_threshold
        * API to configure the PIM SPT threshold on a device
    * Added unconfigure_pim_spt_threshold
        * API to unconfigure the PIM SPT threshold on a device
    * Modified configure_ipv6_mld_join_group
        * Added optional source support when configuring an IPv6 MLD join group
    * Added unconfigure_ipv6_mld_join_group
        * API to unconfigure an IPv6 MLD join group with optional source support
    * Added configure_parameter_map_type_inspect
        * parameter-map type inspect {name}
        * log dropped-packets
    * Added unconfigure_parameter_map_type_inspect
        * no log dropped-packets
        * no parameter-map type inspect {name}
    * Added unit test coverage for the new APIs.
    * Added configure_zone_security
        * zone security {zone_name}
    * Added unconfigure_zone_security
        * no zone security {zone_name}
    * Added configure_zone_pair_security
        * zone-pair security {zone_pair_name} source {source_zone} destination {destination_zone}
        * service-policy type inspect {service_policy}
    * Added unconfigure_zone_pair_security
        * no service-policy type inspect {service_policy}
        * no zone-pair security {zone_pair_name} source {source_zone} destination {destination_zone}
    * Added configure_zone_member_security
        * zone-member security {zone_name}
    * Added unconfigure_zone_member_security
        * no zone-member security {zone_name}
    * Added unit test coverage for the new APIs.
    * Added configure_class_map_type_control_isg
        * class-map type control match-any SECURE_REM
        * match vlan 130
        * match vlan 140
    * Added configure_redirect_server_group_without_port
        * redirect server-group SMTP_REDIRECT_GROUP
        * server ip 10.1.1.1
    * Added configure_policy_map_type_service_secure_dhcp_class
        * policy-map type service SECURE_DHCP_CLASS
        * classname orange_secure
    * Added configure_policy_map_type_service_opengarden
        * policy-map type service OPENGARDEN_SERVICE
        * 10 class type traffic OPENGARDEN_TC
        * class type traffic default input
        * drop
    * Added configure_policy_map_type_service_https_l4r_redirect
        * policy-map type service HTTPS_L4R_REDIRECT_SERVICE
        * 25 class type traffic HTTPS_L4R_REDIRECT_TC
        * redirect to group HTTPS_L4R_REDIRECT_GROUP
    * Added configure_policy_map_type_service_smtp_redirect
        * policy-map type service SMTP_REDIRECT_SERVICE
        * 15 class type traffic SMTP_REDIRECT_TC
        * redirect to group SMTP_REDIRECT_GROUP
    * Added configure_policy_map_type_service_web_proxy_redirect
        * policy-map type service WEB_PROXY_REDIRECT_SERVICE
        * 10 class type traffic WEB_PROXY_REDIRECT_TC
        * redirect to group WEB_PROXY_REDIRECT_GROUP
    * Added configure_policy_map_type_service_arp_keepalive
        * policy-map type service ARP_KEEPALIVE
        * keepalive idle 35 attempts 10 interval 20 protocol ARP
    * Added unit test coverage for the new APIs.
    * Added cloud_mgmt verify APIs for Meraki/cloud management (show cloud-mgmt connect)
        * verify_cloud_mgmt_connect_status
        * verify_cloud_mgmt_device_registration
        * verify_cloud_mgmt_tunnel_state
        * verify_cloud_mgmt_tunnel_interface_status
        * verify_cloud_mgmt_tunnel_config
    * Added execute API execute_cloud_mgmt_reset_level
        * Execute 'test platform software cloud-mgmt reset level <1-3>' on IIoT Meraki devices
        * For Level 1, verify cloud management is enabled, configuration fetch succeeds, and the tunnels transition down and recover. Verify that TLS-VIF2 disappears or transitions down, then returns up
        * For Level 2, verify a new reset/recovery event is logged and the tunnels and TLS-VIF2 transition down and recover. Verify config fetch recovers and fail if a new configuration updater error is logged
        * For Level 3, wait up to 600 seconds for the factory reset to finish and the device console to return
    * Added configure_platform_inspect_match_statistics_per_filter
        * platform inspect match-statistics per-filter
    * Added unconfigure_platform_inspect_match_statistics_per_filter
        * no platform inspect match-statistics per-filter
    * Added configure_platform_inspect_disable_all
        * platform inspect disable-all
    * Added unconfigure_platform_inspect_disable_all
        * no platform inspect disable-all
    * Added unit test coverage for the new APIs.
    * Added ``recover_device_to_enable_state`` API
        * Recovers the connection and brings the device to enable mode after a long running or disruptive operation (image install, reload, upgrade, etc.) when the device state can no longer be assumed.
        * Disconnects and reconnects when the session is down, resynchronizes the unicon state machine, completes authentication, and transitions the device to enable mode.
        * Raises if the device is in ROMMON or enable mode could not be reached, so callers can preserve/log the failure without masking the original error.
    * Added configure_segment_routing
        * added api configure_segment_routing
    * Added unconfigure_segment_routing
        * added api unconfigure_segment_routing
    * Added verify_logging apis
        * API to verify logging on the device
    * Added configure_class_map_type_inspect
        * class-map type inspect {match_type} {class_map_name}
        * match access-group name {acl}
        * match access-group {acl}
        * match protocol {protocol}
        * match class-map {child}
    * Added unconfigure_class_map_type_inspect
        * class-map type inspect {match_type} {class_map_name}
        * no match access-group name {acl}
        * no match access-group {acl}
        * no match protocol {protocol}
        * no match class-map {child}
        * no class-map type inspect {match_type} {class_map_name}
    * Added unit test coverage for the new APIs.
    * CAT9K
        * Added API ``execute_clear_platform_software_fed_switch_punt_entries`` to clear FED punt entry counters for a specified stack switch.
    * Added configure_policy_map_type_service_default_l4r_redirect
        * policy-map type service DEFAULT_L4R_REDIRECT_SERVICE
        * 15 class type traffic DEFAULT_L4R_REDIRECT_TC
        * redirect to group DEFAULT_L4R_REDIRECT_GROUP
    * Added unit test coverage for the new API.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_static_nat_network_rule
        * Added optional vrf argument
        * ip nat inside source static network {inside_local_ip} {inside_global_ip} {mask} vrf {vrf}
    * Modified unconfigure_static_nat_network_rule
        * Added optional vrf argument
        * no ip nat inside source static network {inside_local_ip} {inside_global_ip} {mask} vrf {vrf}
    * Modified ``configure_rommon_tftp`` and ``configure_rommon_tftp_ha``
        * Selects recovery TFTP servers from clean data or dynamically injected testbed services.
        * Prefers the TFTP service with the lowest order and retains legacy testbed compatibility.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_mac_global_address_table_notification_change
        * test_api_unconfigure_mac_global_address_table_static
        * test_api_unconfigure_mac_loopback
        * test_api_config_macsec_should_secure
        * test_api_config_mka_keychain_on_interface
        * test_api_config_mka_policy
        * test_api_configure_disable_sci_dot1q_clear
        * test_api_configure_mka_macsec
        * test_api_configure_mka_policy
        * test_api_configure_mka_policy_delay_protection
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Fixed configure_flow_exporter
        * Added dest_vrf to config destination with vrf
    * Modified configure_management API to enable the physical management interface when switchport access or trunk mode is configured.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_logging_monitor_debugging
        * test_api_configure_default_mac_global_address_table_notification_change
        * test_api_configure_interface_default_snmp
        * test_api_configure_mac_address_change_interval
        * test_api_configure_mac_address_table_aging
        * test_api_configure_mac_address_table_aging_default
        * test_api_configure_mac_address_table_control_packet_learn
        * test_api_configure_mac_address_table_learning
        * test_api_configure_mac_address_table_notification_change
        * test_api_configure_mac_address_table_static
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Updated C9200-48P ROMMON recovery APIs to use C9200 APIs, which provide the same functionality, while retaining direct-import compatibility.
    * Fixed C9200 ROMMON recovery with explicit TFTP boot details to skip optional drec0 golden-image discovery.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_management_telnet
        * test_api_configure_management_tftp
        * test_api_configure_management_vty_lines
        * test_api_configure_mtc
        * test_api_configure_netconf_yang_intelligent_sync
        * test_api_configure_ssh_certificate_profile
        * test_api_configure_ssh_server_algorithm
        * test_api_unconfigure_ip_ssh_version
        * test_api_unconfigure_management_netconf
        * test_api_unconfigure_mtc
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Increased the management SSH RSA key generation timeout to support slower IIOT platforms.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_license_smart_transport_smart
        * test_api_configure_netconf_yang
        * test_api_configure_telemetry_ietf_parameters
        * test_api_configure_telemetry_ietf_subscription
        * test_api_unconfigure_license_smart_transport
        * test_api_unconfigure_netconf_yang
        * test_api_unconfigure_telemetry_ietf_subscription
        * test_api_configure_l2_traceroute
        * test_api_unconfigure_l2_traceroute
        * test_api_configure_interface_udld_port
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_lisp_enhanced_forwarding
        * test_api_configure_lisp_l2_flooding
        * test_api_unconfigure_lisp_l2_flooding
        * test_api_clear_lldp_counters
        * test_api_clear_lldp_table
        * test_api_configure_lldp_holdtime
        * test_api_configure_lldp_interface
        * test_api_configure_lldp_reinit
        * test_api_configure_lldp_timer
        * test_api_configure_lldp_tlv_select
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * vrf
        * Modified Unit Tests
            * test_api_configure_default_vxlan
            * test_api_configure_ip_vrf_forwarding_interface
            * test_api_configure_mdt_auto_discovery_inter_as
            * test_api_configure_mdt_auto_discovery_inter_as_mdt_type
            * test_api_configure_mdt_auto_discovery_mldp
            * test_api_configure_mdt_auto_discovery_vxlan
            * test_api_configure_mdt_data_mpls_mldp
            * test_api_configure_mdt_data_threshold
            * test_api_configure_mdt_data_vxlan
            * test_api_configure_mdt_default
        * Removed mock_data.yaml files for refactored unit tests.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_mtc_parameters
        * test_api_unconfigure_netconf_yang_intelligent_sync
        * test_api_unconfigure_netconf_yang_polling
        * test_api_unconfigure_ssh_certificate_profile
        * test_api_unconfigure_ssh_server_algorithm
        * test_api_configure_interface_pim
        * test_api_configure_ip_multicast_routing
        * test_api_configure_ip_multicast_routing_distributed
        * test_api_configure_ip_multicast_vrf_routing
        * test_api_configure_ip_pim_vrf_ssm_range
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_logging_facility
        * test_api_configure_logging_host_transport_tcp_port
        * test_api_configure_login_log
        * test_api_configure_terminal_exec_prompt_timestamp
        * test_api_configure_terminal_length
        * test_api_configure_terminal_width
        * test_api_unconfigure_logging
        * test_api_unconfigure_logging_buffered
        * test_api_unconfigure_logging_buffered_errors
        * test_api_unconfigure_logging_console_errors
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * vlan
        * Modified Unit Tests
            * test_api_configure_shutdown_vlan_interface_range
            * test_api_configure_switchport_trunk_allowed_vlan_except
            * test_api_configure_switchport_trunk_allowed_vlan_remove
            * test_api_configure_switchport_trunk_pruning_vlan
            * test_api_configure_switchport_trunk_pruning_vlan_except
            * test_api_configure_vlan_group_list
            * test_api_configure_vlan_name
            * test_api_configure_vlan_shutdown
            * test_api_configure_vlan_state_active
            * test_api_configure_vlan_state_suspend
        * Removed mock_data.yaml files for refactored unit tests.
    * vrf
        * Modified Unit Tests
            * test_api_configure_vrf_forwarding_interface
            * test_api_configure_vrf_rd_value
            * test_api_create_ip_vrf
            * test_api_delete_ip_vrf
            * test_api_unconfigure_default_vxlan
            * test_api_unconfigure_ip_vrf_forwarding_interface
            * test_api_unconfigure_mdt_auto_discovery_mldp
            * test_api_unconfigure_mdt_auto_discovery_vxlan
            * test_api_unconfigure_mdt_data_threshold
            * test_api_unconfigure_mdt_data_vxlan
        * Removed mock_data.yaml files for refactored unit tests.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_mdns_active_response_timer
        * test_api_configure_mdns_boot_level_license
        * test_api_configure_mdns_controller_service_list
        * test_api_configure_mdns_global_service_buffer
        * test_api_configure_mdns_query_response_mode
        * test_api_configure_mdns_remote_cache_enable
        * test_api_configure_mdns_remote_cache_max_limit
        * test_api_configure_mdns_remote_purge_timer
        * test_api_configure_mdns_sd_service_peer
        * test_api_configure_mdns_service_list
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_default_switchport_trunk_vlan
        * test_api_configure_default_vtp_version
        * test_api_configure_ethernet_vlan_unlimited
        * test_api_configure_flow_monitor_vlan_configuration
        * test_api_configure_interface_port_channel
        * test_api_configure_interface_vlan_priority
        * test_api_configure_interface_vlan_range_priority
        * test_api_configure_interface_vtp
        * test_api_configure_no_shutdown_vlan_interface_range
        * test_api_configure_private_vlan_on_vlan
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_lldp_holdtime
        * test_api_unconfigure_lldp_interface
        * test_api_unconfigure_lldp_reinit
        * test_api_unconfigure_lldp_timer
        * test_api_unconfigure_lldp_tlv_select
        * test_api_configure_lineconsole_exectimeout
        * test_api_configure_logging
        * test_api_configure_logging_buffer_size
        * test_api_configure_logging_buffered_errors
        * test_api_configure_logging_console_errors
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_udld_alert_mode
        * test_api_configure_udld_message_time
        * test_api_configure_udld_recovery
        * test_api_unconfigure_interface_udld_port
        * test_api_unconfigure_udld
        * test_api_unconfigure_udld_message_time
        * test_api_unconfigure_udld_recovery
        * test_api_configure_controller_shutdown
        * test_api_config_ip_on_vlan
        * test_api_configure_access_vlan
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_ip_ssh_client_algorithm_mac
        * test_api_configure_ip_ssh_server_algorithm_encryption
        * test_api_configure_ip_ssh_server_algorithm_hostkey
        * test_api_configure_ip_ssh_server_algorithm_kex
        * test_api_configure_ip_ssh_server_algorithm_mac
        * test_api_configure_line_vty_needs_enhancement
        * test_api_configure_management_gateway
        * test_api_configure_management_ip
        * test_api_configure_management_ntp
        * test_api_configure_management_routes
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_clear_mdns_cache
        * test_api_clear_mdns_cache_remote
        * test_api_clear_mdns_controller_statistics
        * test_api_clear_mdns_statistics_all
        * test_api_clear_mdns_statistics_servicepeer
        * test_api_clear_mdns_statistics_sp_sdg
        * test_api_configure_controller_policy
        * test_api_configure_controller_service_policy
        * test_api_configure_default_mdns_controller
        * test_api_configure_mdns
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_pim_ssm_default
        * test_api_configure_pim_vrf_ssm_default
        * test_api_configure_scale_ip_multicast_vrf_distribute_tftp
        * test_api_unconfigure_interface_pim
        * test_api_unconfigure_ip_multicast_routing
        * test_api_unconfigure_ip_multicast_routing_distributed
        * test_api_unconfigure_ip_multicast_vrf_routing
        * test_api_unconfigure_ip_pim_vrf_ssm_range
        * test_api_unconfigure_pim_ssm_default
        * test_api_unconfigure_pim_vrf_ssm_default
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified configure_ip_on_tunnel_interface
        * modified configure_ip_on_tunnel_interface
    * Updated ``collect_install_log`` API (base, c9300, c9200, c9800)
        * Added a ``reconnect`` argument. When ``True``, the API calls ``recover_device_to_enable_state`` so the device is in enable mode before the diagnostic commands are run.
        * Added a ``reconnect_timeout`` argument so callers can use their own timeout (e.g. an install timeout) for the recovery independently of the ``timeout`` used for the diagnostic commands.
    * vrf
        * Modified Unit Tests
            * test_api_unconfigure_mdt_overlay_use_bgp
            * test_api_unconfigure_vrf_definition_stitching
            * test_api_unconfigure_vrf_forwarding_interface
        * Removed mock_data.yaml files for refactored unit tests.
    * snmp
        * Modified Unit Tests
            * test_api_unconfigure_snmp_server_engineid
            * test_api_unconfigure_snmp_server_group
            * test_api_unconfigure_snmp_server_host
            * test_api_unconfigure_snmp_server_manager
            * test_api_unconfigure_snmp_server_trap
            * test_api_unconfigure_snmp_server_user
            * test_api_unconfigure_snmp_server_view
        * Removed mock_data.yaml files for refactored unit tests.
    * vlan
        * Modified Unit Tests
            * test_api_unconfigure_vlan_state_suspend
            * test_api_unconfigure_vtp_mode
            * test_api_unconfigure_vtp_password
            * test_api_unconfigure_vtp_pruning
            * test_api_unconfigure_vtp_version
            * test_api_unconfig_vlan_range
            * test_api_unconfig_vlan_tag_native
        * Removed mock_data.yaml files for refactored unit tests.
    * vpdn
        * Modified Unit Tests
            * test_api_configure_vpdn_group
            * test_api_unconfigure_vpdn_group
        * Removed mock_data.yaml files for refactored unit tests.
    * vrf
        * Modified Unit Tests
            * test_api_configure_default_mpls_mldp
        * Removed mock_data.yaml files for refactored unit tests.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_mdns_service_peer_group
        * test_api_configure_mdns_service_policy
        * test_api_configure_mdns_service_query_timer_periodicity
        * test_api_configure_mdns_service_receiver_purge_timer
        * test_api_configure_mdns_service_record_ttl
        * test_api_unconfigure_controller_policy_service_export
        * test_api_unconfigure_controller_service_policy_service_export
        * test_api_unconfigure_match_service_type_mdns_controller_service_list
        * test_api_unconfigure_match_service_type_mdns_service_list
        * test_api_unconfigure_mdns_active_response_timer
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_pki_trustpoint
        * test_api_unconfig_macsec_should_secure
        * test_api_unconfig_mka_policy
        * test_api_unconfigure_disable_sci_dot1q_clear
        * test_api_unconfigure_mka_keychain_on_interface
        * test_api_unconfigure_mka_macsec
        * test_api_unconfigure_mka_policy
        * test_api_unconfigure_mka_policy_delay_protection
        * test_api_configure_ip_ssh_client_algorithm_encryption
        * test_api_configure_ip_ssh_client_algorithm_kex
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified configure_bgp_neighbor_remote_as_fall_over_as_with_peergroup
        * modified configure_bgp_neighbor_remote_as_fall_over_as_with_peergroup
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_smartpower_name
        * test_api_unconfigure_smartpower_role
        * test_api_configure_smartpower_activitycheck
        * test_api_configure_smartpower_interface_domain_default
        * test_api_configure_smartpower_interface_endpoint_default
        * test_api_configure_smartpower_interface_importance
        * test_api_configure_smartpower_interface_importance_default
        * test_api_configure_smartpower_interface_keywords
        * test_api_configure_smartpower_interface_keywords_default
        * test_api_configure_smartpower_interface_level
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_mac_global_address_table_notification_change
        * test_api_configure_mac_global_address_table_static
        * test_api_configure_mac_loopback
        * test_api_unconfigure_mac_address_change_interval
        * test_api_unconfigure_mac_address_table_aging
        * test_api_unconfigure_mac_address_table_aging_time_vlan
        * test_api_unconfigure_mac_address_table_control_packet_learn
        * test_api_unconfigure_mac_address_table_learning
        * test_api_unconfigure_mac_address_table_notification_change
        * test_api_unconfigure_mac_address_table_static
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * vrf
        * Modified Unit Tests
            * test_api_configure_mdt_overlay_use_bgp
            * test_api_configure_mdt_overlay_use_bgp_spt_only
            * test_api_configure_mdt_partitioned_mldp_p2mp
            * test_api_configure_mdt_preference_under_vrf
            * test_api_configure_mdt_strict_rpf_interface_vrf
            * test_api_configure_multicast_routing_mvpn_vrf
            * test_api_configure_rd_address_family_vrf
            * test_api_configure_scale_vrf_via_tftp
            * test_api_configure_vpn_id_in_vrf
            * test_api_configure_vrf_definition_stitching
        * Removed mock_data.yaml files for refactored unit tests.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_smartpower_interface_level_default
        * test_api_configure_smartpower_interface_management_default
        * test_api_configure_smartpower_interface_name
        * test_api_configure_smartpower_interface_name_default
        * test_api_configure_smartpower_interface_role
        * test_api_configure_smartpower_interface_role_default
        * test_api_unconfigure_smartpower_activitycheck
        * test_api_unconfigure_smartpower_interface_importance
        * test_api_unconfigure_smartpower_interface_keywords
        * test_api_unconfigure_smartpower_interface_level
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_smartpower_interface_name
        * test_api_unconfigure_smartpower_interface_role
        * test_api_configure_boot_level_licence
        * test_api_configure_terminal_settings
        * test_api_disable_system_integrity
        * test_api_enable_system_integrity
        * test_api_configure_table_map
        * test_api_configure_table_map_set_default
        * test_api_unconfigure_table_map
        * test_api_configure_license_smart_transport_callhome
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * vlan
        * Modified Unit Tests
            * test_api_unconfigure_ethernet_vlan_unlimited
            * test_api_unconfigure_flow_monitor_vlan_configuration
            * test_api_unconfigure_interface_port_channel
            * test_api_unconfigure_interface_vtp
            * test_api_unconfigure_pvlan_primary
            * test_api_unconfigure_pvlan_type
            * test_api_unconfigure_switchport_trunk_pruning_vlan
            * test_api_unconfigure_vlan_configuration
            * test_api_unconfigure_vlan_group_list
            * test_api_unconfigure_vlan_state_active
        * Removed mock_data.yaml files for refactored unit tests.

* get_file_size_from_server
    * Prevent credentials embedded in file transfer URLs from being exposed in error messages.

* updated execute_copy_run_to_start api
    * Documented max_time and check_interval as ignored compatibility arguments.

* sdk
    * Report missing power-cycler host/IP configuration before initialization and safely handle cleanup of a partially initialized power-cycler.

* wsim
    * Modified wsim run_wsim_config to handle right errors and pass criteria
    * Modified simulate_ap_container to handle right errors and pass criteria

* sdk file copy utilities
    * Added opt-in runtime proxy selection using testbed route metadata.
    * Added family-safe candidate ranking, target probing, device-scoped positive and negative caching, and one-candidate retry for confirmed proxy relay setup failures, including empty relay results, while keeping file-copy errors non-retriable and preserving static proxy fallback.
    * Preserved the current static proxy before remaining declared no-route candidates without promoting unrelated server metadata.
    * Preserved exported ordered SSH service metadata and non-default ports when converting testbed servers to Linux proxy devices.

* updated api unit tests
    * IOSXE
        * Updated unittests to new testing method
            * configure_smartpower_name
            * configure_smartpower_name_default
            * configure_smartpower_role
            * configure_smartpower_role_default
            * unconfigure_auto_off_optics
            * unconfigure_ecomode_optics
            * unconfigure_smartpower_domain
            * unconfigure_smartpower_importance
            * unconfigure_smartpower_keywords
            * unconfigure_smartpower_level

* blitz
    * Fixed loop processing for empty iterators to stop without executing actions and clear previous iterator variables.

genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareFedSwitchActiveNpuSlotPortInfo
        * Added parser for 'show platform hardware fed switch {mode} npu slot 1 port {port} port-info' command.
    * Added ShowPlatformHardwareAuthenticationStatus for C9400
        * show platform hardware authentication status
    * Added ShowPlatformHardwareAuthenticationStatus for C9550
        * show platform hardware authentication status
    * Added ShowWirelessInterfaceSummary
        * Added parser for ``show wireless interface summary``.
        * Added support for IPv6 continuation addresses.
    * Added ShowPlatformSoftwareProcessDatabaseResourceManagerSwitchR0Summary
        * Added parser for 'show platform software process database resource-manager switch {switch_id} r0 summary'.
    * Added ShowIpInterfaceBriefExclude
        * Added parser for 'show ip interface brief | exclude {exclude}' command.
    * Added ShowPlatformStormControlMode
        * Added Schema and parser for 'show platform storm-control mode'.
    * Added ShowPlatformFedActiveTcamUtilization for c9400
        * Added schema and parser for 'show platform hardware fed active fwd-asic resource tcam utilization'
        * Added schema and parser for 'show platform hardware fed active fwd-asic resource tcam utilization {asic}'
    * Added ShowPlatformFedStandbyTcamUtilization for c9400
        * Added schema and parser for 'show platform hardware fed standby fwd-asic resource tcam utilization'
        * Added schema and parser for 'show platform hardware fed standby fwd-asic resource tcam utilization {asic}'

* nxos
    * Added ShowIpMrouteSourceTreeVrfAll
        * show ip mroute 225.1.1.7 47.1.1.2 source-tree vrf all
    * Added ShowIpIgmpSnoopingGroups
        * show ip igmp snooping groups

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLicenseTechSupport
        * Added support for PolicyV2 output and additional optional fields.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Added new fields in schema and parser according to new output
    * Modified ShowSpanningTree
        * Updated show spanning-tree parser
    * Modified ShowSpanningTreeDetail
        * Updated show spanning-tree detail parser
    * Modified ShowSpanningTreeInconsistentports
        * Updated show spanning-tree inconsistentports parser
    * Modified ShowSpanningTreeInterface
        * Updated show spanning-tree interface {interface} parser
    * Added ShowSpanningTreeVlanInconsistentports
        * Added schema and parser for 'show spanning-tree vlan {vlan} inconsistentports'
    * Modified ShowDeviceTrackingDatabase
        * Fixed device_info_capture_database regex to handle time_left values with a trailing 'try N' suffix (e.g. 'try 0 1710 s try 0').
    * Modified ShowIpRoute parser
        * Fix show ip route parsing for replicated OSPF external routes with combined codes like O E2+.
    * Modified ShowVersionRunning
        * Updated <p1> to capture hyphenated package names in the package key.
    * Modified ShowPlatformSoftwareFedSwitchActiveIpRoute parser
        * Enhancement added for "show platform software fed {active} ip route".
    * Modified ShowPlatformSoftwareFedSwitchActiveIpv6Route parser
        * Enhancement added for "show platform software fed {active} ipv6 route".
    * Modified ShowTemplateBrief
        * Made the `service_template` key optional when the Service Templates table is present but contains no entries.
        * Added a golden output testcase for the empty Service Templates table.
    * Modified ShowIpv6ProtocolsSchema schema
        * Added support for application and ND protocols
    * Modified ShowIpv6Protocols parser
        * REGEX update to match application and ND
        * Add application and ND protocols info in the dict
    * Modified ShowPlatformSoftwareFedMatmMacTable
        * Updated the short MATM row regex to parse C9250 output consistently.
        * Added a C9250 regression test for secure client and SVI MAC entries.
    * Modified ShowUACUplink
        * Changed the IPv4 and IPv6 `configured_interface` schema keys to Optional when configured uplink interface lines are absent.
        * Updated the <p3> and <p4> match handling to initialize the IPv4 or IPv6 section directly from the active uplink interface line.
        * Added golden output testcases for routing-platform output without configured uplink interface lines.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Changed ``qos_profile_information`` in the schema to Optional so NPD and SDK detailed output without QoS profile details can be parsed.
    * Modified ShowPlatformSoftwareFedSwitchActiveNatAcl
        * Added support for the optional ``VRF`` column introduced in IOS XE 27.1.1 while retaining support for legacy output without the column.
        * Added golden parser coverage for NAT ACL entries containing a VRF ID.
    * Added support for standby CLI variants in the ShowPlatformSoftwareFedActiveSdmFeature parser.
        * show platform software fed switch standby sdm feature
        * show platform software fed standby sdm feature
    * Modified ShowIpIgmpGroupsDetail
        * Updated the source-row regex patterns for ``v3_exp`` and ``csr_exp`` to support colon-delimited timer values.
        * Added test coverage for source and forwarding information when ``v3_exp`` contains a value such as ``00:02:49``.
    * Modified ShowPlatformSoftwareFedSwitchFnfMonitorsDump
        * Added support for the C9550 colon-separated FNF monitor attributes and pipe-separated record table.
        * Added optional schema fields for monitor identifiers, cache details, record details, and monitor handles.
        * Added support for multiple monitor-statistics blocks while retaining the existing legacy ``Monitor (0x...)`` format.
    * Modified ShowPlatformSoftwareFedSwitchActiveFnfAttachPointsDump
        * Added support for the C9500 legacy ``ap(...)`` attach-point format.
        * Added extraction of non-null FNF ``monitor0`` and ``monitor1`` pointers as integer ``monitor_ids``.
        * Added IPv4, IPv6, INGRESS, and EGRESS support while retaining the existing C9550 tabular format.
        * Updated the schema to use ``ListOf(int)`` for ``monitor_ids`` and made C9550-only fields optional.
