July 2026
==========

July 28 - Genie v26.7
---------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v26.7
    ``genie.lamp``, v26.7
    ``genie.libs.health``, v26.7
    ``genie.libs.clean``, v26.7
    ``genie.libs.conf``, v26.7
    ``genie.libs.filetransferutils``, v26.7
    ``genie.libs.ops``, v26.7
    ``genie.libs.parser``, v26.7
    ``genie.libs.robot``, v26.7
    ``genie.libs.sdk``, v26.7
    ``genie.telemetry``, v26.7
    ``genie.trafficgen``, v26.7




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie.abstract.decorator
    * Modified deprecated
        * Include the deprecated API path in warning messages so callers can identify which deprecated API needs to be updated.

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean/stages
    * Modified ConfigureManagement stage
        * Added PING_ATTEMPTS = 3

* clean
    * Modified Connect recovery result handling
        * Report the Connect stage as PASSX when device recovery succeeds and pyATS Clean continues.
    * Modified recovery_processor
        * Preserve the triggering clean stage result when device recovery reports its own result.
        * Keep recovery results visible without rolling them up into the clean stage result.
        * Record clean termination as an explicit clean-flow result when non-Connect recovery succeeds.
    * Modified recovery_processor
        * Report successful device recovery as PASSED instead of FAILED when clean is terminated.
    * Modified DeleteFiles clean stage
        * Increased default delete timeout from 500 to 3600 seconds.
        * Added timeout to stage schema.

* ioxe/stages
    * Added a new pattern to detect device reload

* iosxe
    * InstallImage
        * Continued reload handling when install add activate commit reports SUCCESS before the execute service times out during auto-reload.
        * Made install log collection best-effort when image installation fails so diagnostic collection errors do not mask the original install failure.
    * Modified break boot recovery
        * Update Unicon current_state when the break-boot dialog matches a state prompt such as rommon.
    * Updated InstallImage clean stage
        * Detect C9350 quick reload messages that include "reload fru action requested", "Reload Command", or "Reload Firmware Command".
        * Added unittest coverage for C9350 quick reload dialog matching.
    * Modified the InstallImage stage to use create_empty_file API
    * Updated InstallImage clean stage
        * Continue reload handling when the install dialog detects a success marker even if execute returns empty output.
        * Fail the install step when execute returns empty output without a success marker.
    * Updated InstallImage clean stage
        * Updated required space conversion from KB to bytes before calling free_up_disk_space
    * Modified Reload clean stage
        * Preserved reload service arguments when retrying reload with manual boot command.
    * Modified Reload clean stage
        * Honor grub_boot_image during the manual boot fallback so GRUB based platforms (e.g. cat9kv) boot the requested menu entry instead of sending an invalid 'boot <image>' command at the bootloader prompt
    * Modified the SD-WAN Connect clean stage
        * Accepted ``logout: false`` while preserving the connection for later clean stages.
        * Rejected ``logout: true`` because SD-WAN clean requires the connection to remain active.

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added C9200 collect_install_log API using the Cat9k switch-active install-manager command syntax.
    * Added debug_access_session_all
        * API to enable or disable 'debug access-session all'
    * Added debug_dot1x_all
        * API to enable or disable 'debug dot1x all'
    * Added debug_mab_all
        * API to enable or disable 'debug mab all'
    * Added debug_aaa_authentication
        * API to enable or disable 'debug aaa authentication'
    * Added debug_aaa_authorization
        * API to enable or disable 'debug aaa authorization'
    * Added debug_epm_all
        * API to enable or disable 'debug epm all'
    * Added debug_radius_authentication
        * API to enable or disable 'debug radius authentication'
    * Added get_show_access_session_mac_detail
        * API to get 'show access-session mac {mac} details' output
    * Added get_show_access_session_interface_detail
        * API to get 'show access-session interface {interface} details' output
    * Added get_access_session_interface_mac_detail
        * API to get access-session interface detail for a specific mac address
    * Added get_access_sessions_interface_count
        * API to get the access sessions count on an interface
    * Added IOSXE SDK API support for
        * `configure_aaa_group_server_radius`
    * Added unit test coverage for the new API and non-standard option.
    * Added verify_access_session_detail
        * API to verify access session client details on an interface
    * Added verify_access_session_timeout_remaining
        * API to verify the access session timeout remaining time is within an expected range
    * Added verify_access_session_removed
        * API to verify the access session for a mac on an interface is removed
    * Added IOSXE SDK API support for
        * `configure_class_map_type_control`
        * `unconfigure_class_map_type_control`
    * Added unit test coverage for the new APIs.
    * Added cloud_mgmt verify APIs for Meraki/cloud management (show cloud-mgmt)
        * verify_cloud_id
        * verify_current_mode
        * verify_conversion_status
        * verify_cloud_mgmt_migration_status
    * Added configure_enable_debugs
        * service timestamps
        * logging queue-limit
        * logging rate-limit
        * logging buffered
    * Added unconfigure_enable_debugs
        * no service timestamps
        * logging queue-limit
        * logging rate-limit
        * no logging buffered
    * Added unit test coverage for the new APIs.
    * Added
        * configure_interface_ip_address_no_shutdown API
    * Added configure_mpls_bgp_forwarding
        * added api to execute 'mpls bgp forwarding' on the device
    * Added unconfigure_mpls_bgp_forwarding
        * added api to execute 'no mpls bgp forwarding' on the device
    * Added execute_erase_nvram
        * added api to execute 'erase nvram:' on the device
    * Added execute_erase_nvram_all
        * added api to execute 'erase /all nvram:' on the device
    * Added get_show_output
        * API to execute a show command on the active or standby RP. Accepts an optional ``target`` kwarg and returns ``(bool(output), output)``.
    * Added unit test coverage for the new API.
    * Added get_hw_module_subslot_oir
        * API to get the OIR status of a hardware module subslot
    * Added get_platform_hardware_subslot_module_interface_status
        * API to get the interface status of a hardware module subslot interface
    * Added verify_show_hw_module_subslot_oir
        * Verify OIR status in show hw-module subslot output for a given subslot
    * Added verify_platform_hardware_subslot_module_interface_status_mac_learning
        * Verify MAC learning status in show platform hardware subslot module interface status output
    * Added configure_ip_igmp_snooping_robustness
        * added api to configure ip igmp snooping robustness variable
    * Added unconfigure_ip_igmp_snooping_robustness
        * added api to unconfigure ip igmp snooping robustness variable
    * Added configure_ip_igmp_snooping_check_rtr_alert_option
        * added api to configure ip igmp snooping check rtr-alert-option
    * Added unconfigure_ip_igmp_snooping_check_rtr_alert_option
        * added api to unconfigure ip igmp snooping check rtr-alert-option
    * Added configure_ip_igmp_snooping_check_ttl
        * added api to configure ip igmp snooping check ttl
    * Added unconfigure_ip_igmp_snooping_check_ttl
        * added api to unconfigure ip igmp snooping check ttl
    * Added configure_ip_igmp_snooping_last_member_query_count
        * added api to configure ip igmp snooping last-member-query-count
    * Added unconfigure_ip_igmp_snooping_last_member_query_count
        * added api to unconfigure ip igmp snooping last-member-query-count
    * Added configure_ip_igmp_snooping_last_member_query_interval
        * added api to configure ip igmp snooping last-member-query-interval
    * Added unconfigure_ip_igmp_snooping_last_member_query_interval
        * added api to unconfigure ip igmp snooping last-member-query-interval
    * Added configure_ip_igmp_snooping_querier_address
        * added api to configure ip igmp snooping querier address
    * Added unconfigure_ip_igmp_snooping_querier_address
        * added api to unconfigure ip igmp snooping querier address
    * Added configure_ip_igmp_snooping_querier_interval
        * added api to configure ip igmp snooping querier query-interval
    * Added unconfigure_ip_igmp_snooping_querier_interval
        * added api to unconfigure ip igmp snooping querier query-interval
    * Added configure_ip_igmp_snooping_querier_max_response_time
        * added api to configure ip igmp snooping querier max-response-time
    * Added unconfigure_ip_igmp_snooping_querier_max_response_time
        * added api to unconfigure ip igmp snooping querier max-response-time
    * Added configure_ip_igmp_snooping_querier_version
        * added api to configure ip igmp snooping querier version
    * Added unconfigure_ip_igmp_snooping_querier_version
        * added api to unconfigure ip igmp snooping querier version
    * Added configure_ip_igmp_snooping_immediate_leave
        * added api to configure ip igmp snooping immediate-leave
    * Added unconfigure_ip_igmp_snooping_immediate_leave
        * added api to unconfigure ip igmp snooping immediate-leave
    * Added get_igmp_snooping_group
        * added api to retrieve an ip igmp snooping group entry by vlan and group
    * Added get_igmp_snooping_groups_count
        * added api to retrieve the ip igmp snooping groups count, optionally filtered by vlan
    * Added get_igmp_vrf_snooping_groups
        * added api to retrieve the ip igmp snooping groups of a vrf
    * Added get_igmp_groups
        * added api to retrieve ip igmp groups, optionally filtered by interface
    * Added get_igmp_vrf_groups
        * added api to retrieve ip igmp groups of a vrf
    * Added get_igmp_snooping
        * added api to retrieve ip igmp snooping information
    * Added unit test coverage for the new IGMP snooping get APIs.
    * Added verify_igmp_snooping_group
        * added api to verify an ip igmp snooping group entry matches the expected type, version and port list
    * Added verify_igmp_snooping_group_notexist
        * added api to verify an ip igmp snooping group entry does not exist
    * Added verify_igmp_snooping
        * added api to verify ip igmp snooping global and per vlan parameters
    * Added verify_igmp_vrf_snooping_group
        * added api to verify an ip igmp snooping group entry of a vrf matches the expected type, version and port list
    * Added verify_igmp_vrf_snooping_group_notexist
        * added api to verify an ip igmp snooping group entry of a vrf does not exist
    * Added verify_igmp_group
        * added api to verify an ip igmp group entry matches the expected interface and last reporter
    * Added verify_igmp_group_notexist
        * added api to verify an ip igmp group entry does not exist
    * Added verify_igmp_vrf_group
        * added api to verify an ip igmp group entry of a vrf matches the expected interface and last reporter
    * Added verify_igmp_vrf_group_notexist
        * added api to verify an ip igmp group entry of a vrf does not exist
    * Added verify_igmp_snooping_group_count
        * added api to verify the ip igmp snooping group count is within the expected range
    * Added unit test coverage for the new IGMP snooping verify APIs.
    * Added get_show_interface_output
        * API to get show interfaces <interface> command output as a parsed dictionary
    * Added verify_interface_counters_increment
        * API to verify the increment of an interface counter field against an expected min/max range after test traffic
    * Added unit test coverage for get_show_interface_output and verify_interface_counters_increment
    * Added IOSXE SDK API support for
        * `configure_ip_portbundle`
        * `unconfigure_ip_portbundle`
    * Added unit test coverage for the new APIs.
    * Added get_l2qos_max_queue_number
        * added api to get the max queue number supported by the device for l2 qos
    * Added get_show_wrr_queue_bandwidth
        * added api to get parsed output of 'show wrr-queue bandwidth'
    * Added get_show_wrr_queue_cos_map
        * added api to get parsed output of 'show wrr-queue cos-map'
    * Added unit test coverage for the new L2 QoS get APIs.
    * Added verify_wrr_queue_enabled
        * Verify l2 qos wrr queue enabled status
    * Added verify_wrr_queue_bandwidth
        * Verify l2 qos wrr queue bandwidth of a given queue id
    * Added verify_wrr_queue_cos_map
        * Verify l2 qos wrr queue cos map of a given cos value
    * Added get_mac_address_table_aging_time
        * added api to get the mac address-table aging-time of the device
    * Added get_mac_address_table
        * added api to get the mac address-table, optionally filtered by interface and/or vlan
    * Added get_mac_address_table_count
        * added api to get the mac address-table count, optionally filtered by vlan
    * Added unit test coverage for the new MAC get APIs.
    * Added verify_mac_address_table_aging_time
        * Verify mac address table aging time
    * Added verify_mac_address_table_entry
        * Verify a mac address entry in mac address table
    * Added verify_mac_address_table_entry_flush
        * Verify a mac address entry is flushed from mac address table
    * Added verify_mac_address_table_entry_learned
        * Verify a mac address entry is learned in mac address table
    * Added verify_mac_address_table_count
        * Verify mac address table count against min and max thresholds
    * Added configure_ipv6_mld_snooping_suppression
        * added api to configure ipv6 mld snooping listener-message-suppression
    * Added unconfigure_ipv6_mld_snooping_suppression
        * added api to unconfigure ipv6 mld snooping listener-message-suppression
    * Added get_mld_snooping_address_count
        * added api to retrieve ipv6 mld snooping address count
    * Added get_ipv6_mld_snooping_address_summary
        * added api to retrieve ipv6 mld snooping groups by vlan and group
    * Added get_mld_snooping
        * added api to retrieve ipv6 mld snooping information, optionally filtered by vlan
    * Added verify_mld_snooping
        * added api to verify ipv6 mld snooping global and per vlan parameters
    * Added verify_mld_snooping_address_count
        * added api to verify the ipv6 mld snooping address count is within the expected range
    * Added verify_ipv6_mld_snooping_address_summary
        * added api to verify an ipv6 mld snooping group entry matches the expected type, version, port and source address
    * Added unit test coverage for the new MLD snooping verify APIs.
    * Added SDK API support for
        * configure_class_map_type_traffic
        * configure_policy_map_type_service
    * Added unit test coverage for service policy-map and traffic class-map APIs.
    * Added verify_span_session
        * added api to verify a span session in 'show monitor session <session_id>' against expected values
    * Added verify_span_session_running_config
        * added api to verify a span session line exists (or not) in device running-config monitor section
    * Added configure_local_span_and_verify_output
        * added api to configure a local span session and verify the session validation result against an expected reason code
    * Added verify_span_port_counters
        * added api to verify span source/destination interface packet counters within a tolerance window
    * Added configure_vpdn_group_l2tp_tunnel_retransmit_retries
        * added api to configure l2tp tunnel retransmit retries under vpdn-group
    * Added unconfigure_vpdn_group_l2tp_tunnel_retransmit_retries
        * added api to unconfigure l2tp tunnel retransmit retries under vpdn-group
    * Added SDK API support for VPDN clear commands
        * `clear vpdn tunnel pptp {remote_hostname} {local_hostname}`
        * `clear vpdn counters`
        * `clear vpdn counters tunnel {protocol} all`
        * `clear vpdn counters tunnel {protocol} id {tunnel_id}`
        * `clear vpdn counters tunnel {protocol} hostname {remote_hostname} {local_hostname}`
        * `clear vpdn counters tunnel {protocol} ip {ip_filter} {ip_address}`
        * `clear vpdn counters session username {username}`
        * `clear vpdn counters session id {tunnel_id} {session_id}`
        * `clear vpdn counters session interface virtual-access {virtual_access_interface}`
    * Added unit test coverage for the new helper APIs.
    * Modified configure_trustpoint
        * API to configure_trustpoint on Device
    * Added unconfigure_cts_policy_server_optional_parameters 
        * API to unconfigure_cts_policy_server_optional_parameters on Device
    * Added unconfigure_ipv6_flow_monitor_on_interface
        * API to unconfigure ipv6 flow monitor on an interface
    * API for enable_device_tracking_debug
    * API for disable_device_tracking_debug
    * API for execute_hw_module_beacon_slot_port_status
    * Enhanced configure_macsec_key_chain
        * Added optional parameters mka_policy_name, mka_cipher, and key_server_priority to configure MKA policy from within the keychain context. This supports ACE/Cat9K access platforms where 'mka policy' must be configured inside 'key chain ... macsec' rather than at global config level.
    * Modified
        * Extended configure_vpdn_group to support request dialout, accept dialout, source-ip, vpn vrf, terminate-from hostname, and multihop hostname
        * Extended configure_dialer_interface to support ip unnumbered, dialer remote-name, dialer string, dialer vpdn, dialer in-band, dialer aaa, and ppp authentication without callin
        * Extended configure_subinterface_dot1q_encapsulation to support VRF, IPv4 address, and no shutdown
        * Extended unconfigure_subinterface_dot1q_encapsulation to support full subinterface cleanup
    * Added unconfigure_management_restconf and configure_management_restconf
        * API to unconfigure and configure management via RESTCONF
    * Added touch_file API for ir1k/ir1101 platform execute
        * Creates an empty file using 'copy null:' command.
        * Added unit test in test_api_touch_file.py.
    * Added SDK API support for
        * `clear simulator radius request all`
        * `clear simulator radius testcase all`
        * `clear pppoe int <interface>`
        * `clear subscriber session all`
        * `clear subscriber session username <username>`
    * Modified `configure_virtual_template` API to support
        * `no ppp authentication`
        * `ppp pap sent-username <username> password [type] <password>`
        * `ppp chap hostname <hostname>`
        * `ppp chap password [type] <password>`
        * `ip address negotiated`
        * `peer default ip address pool local <pool>`
        * `ppp chap splitnames`
        * `ppp timeout ncp <value>`
        * `ppp timeout idle <value>`
        * `no logging event link-status`
        * `no ip address`
        * `ip vrf forwarding <vrf>`
    * Modified `unconfigure_virtual_template` API to support removing
        * `ip address negotiated`
        * `ip vrf forwarding <vrf>`
        * `peer default ip address pool local <pool>`
        * `ppp chap hostname <hostname>`
        * `ppp chap password [type] <password>`
        * `ppp chap splitnames`
        * `ppp timeout ncp <value>`
        * `ppp timeout idle <value>`
    * Added unit test coverage for the new helper APIs and virtual-template PPP options.

* ios
    * Added IOS SDK API support for
        * ``configure_aaa_new_model``
        * ``unconfigure_aaa_new_model``
        * ``configure_aaa_authentication_login``
        * ``unconfigure_aaa_authentication_login``
        * ``configure_aaa_authorization_exec``
        * ``unconfigure_aaa_authorization_exec``
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_bba_group`
        * `unconfigure_bba_group`
    * Added unit test coverage for the new APIs.
    * Modified `unconfigure_bba_group` API to support
        * `vt_number` to remove only the virtual-template from a bba-group
    * Added unit test coverage for the modified API.
    * Added IOS SDK API support for
        * `clear_ip_dhcp_binding`
    * Added unit test coverage for the new API.
    * Added configure_ip_routing SDK API for ios platform
        * Configures ``ip routing`` on the device to enable IPv4 routing.
    * Added unit test coverage for the new API.
    * Added IOS SDK API support for
        * `execute_test_pppoe`
    * Added unit test coverage for the above API.
    * Added IOS SDK API support for
        * `configure_line_console`
        * `configure_line_vty`
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_pppoe_enable_interface`
        * `unconfigure_pppoe_enable_interface`
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `remove_virtual_interface`
        * `shut_interface`
        * `unshut_interface`
    * Added unit test coverage for the above APIs.
    * Added IOS SDK API support for
        * ``configure_ripng``
        * ``unconfigure_ripng``
        * ``configure_interface_ripng``
        * ``unconfigure_interface_ripng``
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `execute_show_simulator_radius_server_all`
    * Added unit test coverage for the new API.
    * Added configure_simulator_radius_account_coa
        * simulator radius account-coa
    * Added unconfigure_simulator_radius_account_coa
        * no simulator radius account-coa
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_simulator_radius_client_host`
        * `unconfigure_simulator_radius_client_host`
    * Modified `configure_simulator_radius_subscriber` API to support
        * `framed_protocol`
    * Added unit test coverage for the new and modified APIs.
    * Added get_interface_ip_address SDK API for ios platform
        * Parses ``show ip interface brief <interface>`` and returns the assigned IPv4 address, or None if unassigned/missing.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * cat9k
        * c9800
            * Added GRUB defaults to ``send_break_boot`` for ``grub_activity_pattern`` and ``grub_breakboot_char`` to fix password recovery on C9800-CL (vWLC).
    * Modified `configure_any_radius_server` API to support
        * `non-standard`
    * BLITZ
        * Modified gnmi_util script
            * preserved serialized JSON values for custom gNMI messages
            * fixed repeated leaf-list values to build a single JSON list
    * Fixed configure_clear_macsec_interface_statistics
        * Changed from device.configure() to device.execute() since 'clear macsec statistics interface ...' is an EXEC mode command, not a configuration mode command
        * Updated unit test to assert device.execute is called
    * Added configure_400g_mode_port_group_range
        * Added closing paranthesis to the slot parameter to configure_400g_mode_port_group_range API
    * Added unconfigure_400g_mode_port_group_range
        * Added closing paranthesis to the slotparameter to unconfigure_400g_mode_port_group_range API
    * Added configure_400g_mode_port_group_range
        * Added timeout parameter to configure_400g_mode_port_group_range API
    * Added unconfigure_400g_mode_port_group_range
        * Added timeout parameter to unconfigure_400g_mode_port_group_range API
    * management
        * Added a longer timeout when configuring the Type 6 master key.
        * Added unit test coverage for the master key configure timeout.
    * Fixed configure_monitor_capture
        * Use 'buffer size' instead of 'buffer-size'
        * Emit single 'limit' keyword for duration/packets/packet-len/every/pps
        * Apply 'size' only when file_location is set
    * Added create_empty_file API to create empty files using copy null
    * Kept touch_file as a deprecated compatibility wrapper around create_empty_file
    * Updated execute_write_memory to use config-transaction commit on Controller-Managed devices while preserving write memory behavior on Autonomous devices.
    * Updated free_up_disk_space to delete top level unprotected files before recursively cleaning unprotected directories.
    * Updated dual RP free_up_disk_space wrapper to forward optional arguments such as allow_deletion_failure, dir_output, compact, and min_free_space_percent to the stack implementation.
    * Fixed configure_hw_module_slot_reload, configure_hw_module_slot_start, configure_hw_module_slot_stop
        * Changed from device.configure() to device.execute() since 'hw-module slot ...' commands are EXEC mode commands, not configuration mode commands
        * Updated unit tests to assert device.execute is called
    * Modified free_up_disk_space API
        * Traverse directories before same-level files during recursive cleanup.
        * Delete larger files first while cleaning each recursive directory.
        * Use an explicit longer timeout for recursive directory listings.
    * Modified stack free_up_disk_space API
        * Traverse directories before same-level files during recursive cleanup.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_interface_storm_control_level
        * test_api_unconfigure_interface_switchport_access_vlan
        * test_api_unconfigure_interface_switchport_block_address
        * test_api_unconfigure_interface_switchport_dot1q_ethertype
        * test_api_unconfigure_interface_switchport_mode_access
        * test_api_unconfigure_interface_switchport_port_security
        * test_api_unconfigure_interface_switchport_port_security_violation
        * test_api_unconfigure_interface_switchport_pvlan_association
        * test_api_unconfigure_interface_switchport_pvlan_mapping
        * test_api_unconfigure_interface_switchport_trunk_allowed_vlan
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_interface_template_sticky
        * test_api_unconfigure_ip_dlep
        * test_api_unconfigure_ip_on_atm_interface
        * test_api_unconfigure_ip_on_interface
        * test_api_unconfigure_ip_route_cache
        * test_api_unconfigure_ipv4_dhcp_relay_helper
        * test_api_unconfigure_ipv6_address_autoconfig
        * test_api_unconfigure_ipv6_address_config
        * test_api_unconfigure_ipv6_address_test
        * test_api_unconfigure_ipv6_dhcp_relay
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_ipv6_enable
        * test_api_unconfigure_ipv6_mtu
        * test_api_unconfigure_ipv6_nd_dad_processing
        * test_api_unconfigure_ipv6_nd_suppress_ra
        * test_api_unconfigure_ipv6_redirects
        * test_api_unconfigure_mdns_on_interface_vlan
        * test_api_unconfigure_medium_p2p_interface
        * test_api_unconfigure_monitor_erspan_source_interface
        * test_api_unconfigure_phymode_ignore_linkup_fault
        * test_api_unconfigure_port_channel_mode
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_port_channel_ip
        * test_api_unconfigure_port_channel_lacp_max_bundle
        * test_api_unconfigure_port_channel_standalone_disable
        * test_api_unconfigure_portchannel_dpi_algorithm
        * test_api_unconfigure_power_efficient_ethernet_auto
        * test_api_unconfigure_power_inline
        * test_api_unconfigure_ppp_multilink
        * test_api_unconfigure_pppoe_enable_interface
        * test_api_unconfigure_profile_on_tunnel_interface
        * test_api_unconfigure_service_instance
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_span_monitor_session
        * test_api_unconfigure_subinterface
        * test_api_unconfigure_switchport_nonegotiate
        * test_api_unconfigure_switchport_protected
        * test_api_unconfigure_switchport_pvlan_trunk_allowed_vlan
        * test_api_unconfigure_switchport_pvlan_trunk_native_vlan
        * test_api_unconfigure_switchport_trunk_allowed_vlan
        * test_api_unconfigure_switchport_trunk_native_vlan
        * test_api_unconfigure_switchport_trunk_native_vlan_tag
        * test_api_unconfigure_system_debounce_link_down_timer
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_system_debounce_link_up_timer
        * test_api_unconfigure_vfi
        * test_api_unconfigure_vrf_select_source
        * test_api_unshut_port_channel
        * test_api_clear_crypto_ikev2_stats
        * test_api_clear_crypto_sa_counters
        * test_api_configure_crypto_ikev2_keyring
        * test_api_configure_crypto_ikev2_policy
        * test_api_configure_crypto_ikev2_proposal
        * test_api_configure_crypto_ipsec_nat_transparency
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_crypto_map
        * test_api_configure_crypto_transform_set
        * test_api_configure_ikev2_profile_pre_share
        * test_api_configure_interface_tunnel_mode_ipsec
        * test_api_configure_ipsec_df_bit
        * test_api_configure_ipsec_fragmentation
        * test_api_configure_ipsec_ike_sa_strength_enforcement
        * test_api_configure_ipsec_sa_global
        * test_api_configure_ipsec_transform_set
        * test_api_configure_ipsec_tunnel
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_sks_client
        * test_api_unconfigure_crypto_ikev2_keyring
        * test_api_unconfigure_crypto_ikev2_policy
        * test_api_unconfigure_crypto_ikev2_proposal
        * test_api_unconfigure_crypto_ipsec_nat_transparency
        * test_api_unconfigure_crypto_transform_set
        * test_api_unconfigure_ikev2_profile_pre_share
        * test_api_unconfigure_interface_tunnel_mode_ipsec
        * test_api_unconfigure_ipsec_df_bit
        * test_api_unconfigure_ipsec_fragmentation
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_ipsec_ike_sa_strength_enforcement
        * test_api_unconfigure_ipsec_profile
        * test_api_unconfigure_ipsec_sa_global
        * test_api_unconfigure_ospfv3_authentication_null
        * test_api_unconfigure_sks_client
        * test_api_configure_ipv6_dhcp_pool_preifx_delegation_pool
        * test_api_configure_ipv6_flow_monitor_sampler
        * test_api_configure_ipv6_local
        * test_api_configure_ipv6_local_pool
        * test_api_configure_ipv6_nd_cache_expire
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_ipv6_nd_cache_expire
        * test_api_configure_dhcpv6_guard_policy
        * test_api_clear_isis
        * test_api_config_interface_isis
        * test_api_config_interface_with_isis_router_name
        * test_api_configure_interface_ipv6_isis_router_name
        * test_api_configure_interface_isis_network
        * test_api_configure_isis_authentication_key_chain
        * test_api_configure_isis_authentication_mode
        * test_api_configure_isis_circuit_type
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_isis_interface_metric
        * test_api_configure_isis_keychain_key
        * test_api_configure_isis_metric_style
        * test_api_configure_isis_network_entity
        * test_api_configure_isis_network_type
        * test_api_configure_isis_nsf_xfsu
        * test_api_configure_isis_password
        * test_api_configure_isis_redistributed_connected
        * test_api_configure_isis_router_configs
        * test_api_configure_isis_with_router_name_network_entity
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_router_isis
        * test_api_remove_isis_configuration
        * test_api_unconfig_interface_isis
        * test_api_unconfig_interface_isis_router_name
        * test_api_unconfigure_isis_authentication_key_chain
        * test_api_unconfigure_isis_authentication_mode
        * test_api_unconfigure_isis_circuit_type
        * test_api_unconfigure_isis_interface_metric
        * test_api_unconfigure_isis_keychain_key
        * test_api_unconfigure_isis_password
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_isis_router_configs
        * test_api_unconfigure_isis_vrf
        * test_api_unconfigure_isis_with_router_name
        * test_api_crypto_key_export
        * test_api_generate_crypto_key
        * test_api_generate_crypto_key_execute
        * test_api_configure_evpn_instance_vlan_based_flood_suppression
        * test_api_configure_l2vpn_evpn_ethernet_segment
        * test_api_configure_l2vpn_evpn_ethernet_segment_all_active
        * test_api_configure_l2vpn_vfi_context_vpls
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_evpn_instance_vlan_based_flood_suppression
        * test_api_unconfigure_l2vpn_vfi_context_vpls
        * test_api_clear_lacp_counters
        * test_api_configure_lacp_port_priority
        * test_api_configure_lacp_ratefast
        * test_api_configure_lacp_system_priority
        * test_api_configure_port_channel_mode
        * test_api_unconfigure_lacp_port_priority
        * test_api_unconfigure_lacp_ratefast
        * test_api_unconfigure_lacp_system_priority
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified remove_port_channel_interface API
        * Render the IOS XE port-channel interface name without an invalid embedded space.
    * Modified request_system_shell API
        * Preserve the underlying error details when system shell entry fails.
    * Modified touch_file in ie3k platform execute
        * Replaced bash_console/SELinux approach with 'copy null:' command.
        * Updated unit test in test_api_touch_file.py accordingly.
    * Updated ROMMON TFTP recovery error handling to report missing TFTP information for dual-RP devices.
    * Modified remove_ospf_passive_interface API
        * Added optional vrf_name argument to support removing passive interfaces under VRF-aware OSPF process configuration

* ios
    * Modified `configure_simulator_radius_subscriber` API to support
        * Negating VSA lines when `negate=True` (emits `no vsa ...`)
    * Added unit test coverage for the above change.

* updated api unit tests
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_rep_ztp
            * clear_ipv6_rip
            * config_interface_ripng
            * configure_rip
            * configure_ripng
            * unconfig_interface_ripng
            * unconfigure_ripng
            * configure_route_map_match_length
            * configure_route_map_permit
            * configure_route_map_route_map
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_route_map_permit
            * configure_ipv6_route_nexthop_vrf
            * configure_ipv6_static_route
            * configure_routing_ipv6_route
            * configure_routing_ipv6_route_vrf
            * configure_routing_static_route
            * configure_routing_static_routev6
            * configure_scale_static_route_via_tftp
            * configure_stack_mac_persistent_timer
            * configure_system_jumbomtu
    * IOSXE
        * Updated unittests to new testing method
            * configure_tftp_source_interface
            * disable_ipv6_multicast_routing
            * enable_ipv6_multicast_routing
            * enable_keepalive_on_interface
            * remove_static_route_all
            * unconfigure_ipv6_route_nexthop_vrf
            * unconfigure_ipv6_static_route
            * unconfigure_ipv6_unicast_routing
            * unconfigure_routing_ip_route_vrf
            * unconfigure_routing_ipv6_route
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_routing_ipv6_route_vrf
            * unconfigure_routing_static_routev6
            * unconfigure_stack_mac_persistent_timer
            * unconfigure_system_mtu
            * unconfigure_tftp_source_interface
            * configure_scp_local_auth
            * unconfigure_scp_local_auth
            * configure_switchport_port_security_aging_time
            * configure_switchport_port_security_aging_type
            * configure_switchport_port_security_mac_address
    * IOSXE
        * Updated unittests to new testing method
            * config_erspan_monitor_session_filter
            * config_erspan_monitor_session_shut_unshut
            * configure_interface_monitor_session_mtu
            * configure_interface_monitor_session_no_mtu
            * configure_interface_monitor_session_shutdown_erspan_dest
            * configure_local_span_destination
            * configure_local_span_filter
            * configure_local_span_source
            * unconfig_erspan_monitor_session_no_filter
            * unconfig_erspan_monitor_session_no_source
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_local_span_destination_interface
            * unconfigure_local_span_filter
            * unconfigure_local_span_source
            * configure_default_spanning_tree
            * configure_default_spanning_tree_mode
            * configure_default_spanning_tree_vlan
            * configure_spanning_tree_backbonefast
            * configure_spanning_tree_bpdufilter
            * configure_spanning_tree_bpdufilter_disable
            * configure_spanning_tree_bpdugaurd
    * IOSXE
        * Updated unittests to new testing method
            * configure_spanning_tree_bridge_assurance
            * configure_spanning_tree_etherchannel_misconfig
            * configure_spanning_tree_guard_loop
            * configure_spanning_tree_guard_root
            * configure_spanning_tree_mode
            * configure_spanning_tree_mst_configuration
            * configure_spanning_tree_mst_configuration_name
            * configure_spanning_tree_mst_configuration_revision
            * configure_spanning_tree_mst_priority
            * configure_spanning_tree_portfast
    * IOSXE
        * Updated unittests to new testing method
            * configure_spanning_tree_portfast_bridge_assurance
            * configure_spanning_tree_portfast_bridge_assurance_on_interface
            * configure_spanning_tree_portfast_default
            * configure_spanning_tree_portfast_on_interface
            * configure_spanning_tree_priority
            * configure_spanningtree_sso_block_tcn
            * configure_spanning_tree_uplinkfast
            * configure_spanning_tree_vlan_root
            * unconfigure_spanning_tree_backbonefast
            * unconfigure_spanning_tree_bpdufilter
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_spanning_tree_bpdufilter
            * unconfigure_spanning_tree_bridge_assurance
            * unconfigure_spanning_tree_etherchannel_misconfig
            * unconfigure_spanning_tree_guard_loop
            * unconfigure_spanning_tree_guard_root
            * unconfigure_spanning_tree_mode
            * unconfigure_spanning_tree_mst_configuration
            * unconfigure_spanning_tree_portfast
            * unconfigure_spanning_tree_portfast_bridge_assurance
            * unconfigure_spanning_tree_portfast_bridge_assurance_on_interface
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_spanning_tree_portfast_on_interface
            * unconfigure_spanning_tree_priority
            * unconfigure_spanningtree_sso_block_tcn
            * unconfigure_spanning_tree_uplinkfast
            * unconfigure_spanning_tree_vlan_root
            * configure_global_dual_active_recovery_reload_disable
            * configure_global_stackwise_virtual
            * configure_stackwise_virtual_dual_active_interfaces
            * configure_stackwise_virtual_dual_active_pagp
            * unconfigure_spanningtree_cost_on_interface
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_stackwise_virtual_dual_active_interfaces
            * unconfigure_stackwise_virtual_dual_active_pagp
            * unconfigure_stackwise_virtual_interfaces
            * configure_subscriber_template
            * configure_platform_sudi_cmca3
            * configure_service_private_config_encryption
            * unconfigure_platform_sudi_cmca3
            * unconfigure_service_private_config_encryption
            * configure_ecomode_optics
            * configure_auto_off_optics
    * IOSXE
        * Updated unittests to new testing method
            * configure_smartpower_domain
            * configure_smartpower_domain_default
            * configure_smartpower_endpoint_default
            * configure_smartpower_importance
            * configure_smartpower_importance_default
            * configure_smartpower_keywords
            * configure_smartpower_keywords_default
            * configure_smartpower_level
            * configure_smartpower_level_default
            * configure_smartpower_management_default
    * IOSXE
        * Updated unittests to new testing method
            * configure_system_debounce_link_up_timer_doppler
            * unconfigure_system_debounce_link_up_timer_doppler

* blitz
    * Modified gnmi_util script to handle prefixes for augmented models

* powercycler
    * Validates proxy start_socat_relay results before unpacking so relay setup failures report the underlying proxy relay error instead of raising TypeError.
    * Drains pending pysnmp asyncio callbacks before closing the SNMP dispatcher so successful SNMP powercycler operations do not log non-fatal "Unregistered transport" errors.
    * Add actionable, non-secret logging for incomplete SNMPv3 credentials and credential-related command TypeErrors.

* sdk/apis/utils
    * Updated ``copy_to_device`` and ``copy_from_device`` to use the device's local IP for the dynamic file server when the management session source IP is the device's gateway (e.g. VXR/NATed setups). Previously the dynamic file server was only used when the local IP was directly present in the management source IP list, which caused failures for devices whose management traffic egresses through a gateway.
    * Added helper ``_management_session_uses_gateway`` that detects when the management session source IP matches either the configured management ``gateway`` in the testbed or an inferred gateway (``.1``/``.254``) for the management IPv4 subnet.

* dependencies
    * Updated pyasn1 pin to >=0.6.4 to address CVE-2026-23490, CVE-2026-30922, CVE-2026-59885

--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified
        * configure_bba_group
            * Added session_per_vlan_limit and session_per_mac_limit optional parameters
        * unconfigure_bba_group
            * Modified vt_number to be optional
    * Enhanced ``configure_policy_map_type_control``
        * Added optional per-class ``class_name`` field (default ``always``) so callers can render custom class-map predicates such as ``class type control ISG-IP-UNAUTH event timed-policy-expiry``.
        * Backward compatible - existing callers omit ``class_name`` and continue to emit ``class type control always event <event>``.
    * Added unit test coverage for the new ``class_name`` field.

genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedIpRouteSummary
        * Parser for 'show platform software fed {switch_var} {state} ip route summary' command.
    * Added ShowPlatformSoftwareIpsecPolicyStatistics
        * Added schema and parser for 'show platform software ipsec policy statistics'
    * Added ShowPlatformSoftwareIpsecSwitchFlowAll
        * Added schema and parser for 'show platform software ipsec {switch} {switch_var} f0 flow all'
    * Added ShowPlatformSoftwareIpsecSwitchSadbAll
        * Added schema and parser for 'show platform software ipsec {switch} {switch_var} f0 sadb all'
    * Added ShowPlatformHardwareFedSwitchFwdAsicResourceFeatureIdMapping
        * Added schema and parser for 'show platform hardware fed {switch} {switch_var} fwd-asic resource feature-id-mapping'
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicResourceUtilizationFeature
        * Added schema and parser for 'show platform hardware fed {switch} {switch_var} fwd-asic resource utilization feature {feature_id}'
    * Added ShowCryptoIkev2Profile
        * Added schema and parser for 'show crypto ikev2 profile {profile_name}'
    * Added ShowRunningConfigFormatNetconfXml
        * show running-config | format netconf-xml
    * Added ShowYangSyncStatus
        * show yang sync status
    * Added ShowPlatformHardwareFedSwitchQosQueueConfig
        * Added schema and parser for 'show platform hardware fed switch active qos queue config interface {interface}'
    * Added ShowSubscriberDefaultSession
        * show subscriber default-session
    * Added ShowTopology, ShowTopologyAll, ShowTopologyDetailAll, ShowTopologyDetailAfi, ShowTopologyDetailVrf
        * show topology
        * show topology all
        * show topology detail all
        * show topology detail {ipv4 | ipv6} all
        * show topology detail {ipv4 | ipv6} topo <topo_name>
        * show topology detail {ipv4 | ipv6} multicast all
        * show topology detail {ipv4 | ipv6} multicast topo {topo_name}
        * show topology detail vrf {vrf} all
        * show topology detail vrf {vrf} {ipv4 | ipv6} all
        * show topology detail vrf {vrf} {ipv4 | ipv6} topo <topo_name>
        * show topology detail vrf {vrf} {ipv4 | ipv6} {multicast} all
        * show topology detail vrf {vrf} {address_family} {multicast} topo {topo_name}
    * Added ShowVpdnGroupSelectDefault
        * show vpdn group-select default
    * Added ShowVpdnSession
        * Added schema and parser for 'show vpdn session'
    * Added ShowCloudMgmtMigration
        * show cloud-mgmt migration
    * Added ShowCloudMgmtCompatibility
        * show cloud-mgmt compatibility
    * Added ShowPlatformHardwareQfpActiveClassificationClassGroupAll
        * show platform hardware qfp active classification class-group-manager class-group all
    * Added ShowSubscriberSessionFeatureAccessList
        * show subscriber session feature access-list
        * show subscriber session uid {uid} feature access-list
    * Added ShowSubscriberSessionFeatureL4Redirect
        * show subscriber session feature l4redirect
        * show subscriber session uid {uid} feature l4redirect
    * Modified ShowSubscriberSessionDetailed
        * show subscriber session uid {uid} detailed

* iosxr
    * Added ShowInventoryVendorType
        * Added schema and parser for 'show inventory vendor-type' command.

* iosxe
    * Added output changes in show meraki config updater command to include new fields for better visibility of configuration updates.
    * Added output changes in show cloud_mgmt config updater command to include new fields for better visibility of configuration updates.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInventory (rv1)
        * Recognize StackWise-Virtual ``Switch N Slot M Linecard/Supervisor/Router`` inventory names so ``slot_dict`` is bound for chassis such as the C9600 SVL.
        * Guard the pluggable/transceiver branch to prevent ``UnboundLocalError`` when ``slot_dict`` has not been assigned.
        * Recognize ``SM subslot <slot>/<subslot>`` inventory lines.
    * Modified ShowIpCefInternal
        * Added support for parsing Lookup in table output chain entries
    * Modified ShowIpv6CefInternal
        * Added support for parsing Lookup in table output chain entries
    * Modified ShowPlatformSoftwareFedSwitchActiveIpRouteDetail
        * Added parsing support for VRF route detail output with VXLAN next-hop information.
        * Added parsing support for global leaked route `LOOKUP` object output.
    * Added ShowPlatformSoftwareFedSwitchActiveIpv6RouteDetail
        * Added parsing support for IPv6 FED route detail output.
        * Added parsing support for IPv6 VRF VXLAN next-hop details.
        * Added parsing support for IPv6 global leaked route `LOOKUP` object output.
    * Added golden output testcases for EVPN route leaking IPv4 and IPv6 FED route detail validation.
    * Modified ShowPlatformRewriteUtilization
        * Modified parser by adding cli 'show platform hardware fed {switch} {active} fwd-asic resource rewrite utilization' and 'show platform hardware fed {active} fwd-asic resource rewrite utilization'
    * Modified ShowPlatformSoftwareFedIfm
        * Modified parser by adding cli 'show platform software fed {switch} {active} ifm interfaces tunnel' and 'show platform software fed {active} ifm interfaces tunnel'
    * Added fix for ShowPlatformSoftwareFedActiveAclBindDbSummary parser.
        * Added this fix to support multiple entries.
    * Added fix for ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetail parser.
        * Added this fix to support multiple entries.
    * Modified <ShowCtsEnvironmentData>
        * Added support to parse the transport_type field.
    * Modified ShowPlatformSoftwareFedIpv6MldSnoopingSummary parser
        * Enhancement added for "show platform software fed switch active ipv6 mld snooping summary".
    * Modified ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAcl
        * Added support for parsing IPv6 SIP entries without Source MAC (delegated/PD prefix entries)
    * Modified ShowPlatformSoftwareFedSwitchIfmInterfaceName
        * Added support for parsing "Mpp port oid"
    * Modified ShowIpNbarDiscovery
        * Modified P1 regex to match "Five gigabit" interface
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Added server_policies vlan_group parsing and schema support for 'show authentication sessions interface {interface} details'.
        * Refined UT expected data for interface details to align with real output containing dual MAC sessions and per-session server_policies vlan_group values.
    * Modified ShowIpv6MldSnoopingVlan
        * Made 'mld' key Optional at global level
        * Added Optional 'oper_state' key at global level
        * Added Optional 'admin_state' and 'oper_state' keys at VLAN level
        * Added vlan-level 'max_response_time' parsing
        * Improved parsing logic to separate global and VLAN level fields
    * Modified ShowIpv6ProtocolsSchema schema
        * Added support for connected and static protocols
    * Modified ShowIpv6Protocols parser
        * REGEX update to match connected and static
        * Add connected and static protocols info in the dict
    * Modified ShowParameterMapTypeInspectParam
        * Changed keys `audit_trail`, `max_incomplete`, `one_minute`, `sessions_rate`, `udp`, `icmp`, `dns_timeout`, `tcp`, `zone_mismatch_drop`, `application_inspect`, and `sessions_maximum` from schema to Optional.
        * Added parsing support for `lisp inner packet inspection <state>` and exposed it as `lisp_inner_packet_inspection`.
        * Added a golden output testcase for `show parameter-map type inspect global` to validate parsing when those sections are absent.
    * Modified ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuit parser
        * Enhancement added for "show platform hardware fed switch fwd asic insight l2 attachment circuit".
    * Modified ShowPlatformSoftwareFedSwitchIfmInterfaceName parser
        * Added support for parsing "speed"
    * Modified ShowPlatformSoftwareFedIpIgmpSnoopingSummary parser
        * Enhancement added for "show platform software fed switch active ip igmp snooping summary".
    * Modified ShowPlatformSoftwareFedSwitchWdavcFlows
        * Updated regex pattern p1 to match software-handled (SW) flows in addition to hardware-handled (HW) flows.
    * Modified ShowSdmPreferNew parser
        * Updated schema for missing fields and made those fields Optional.
        * Updated parser for 'show sdm prefer' and 'show sdm prefer custom' on C9500 to handle generic current/proposed feature lines and proposed-only feature lines.
    * Modified ShowPlatformSoftwareFedMatmMacTable
        * Added support for MATM output without machandle, siHandle, riHandle, and diHandle columns.
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmMacTableVlanMac
        * Added support for MATM vlan/mac output without machandle, siHandle, riHandle, and diHandle columns.
    * Modified ShowPortSecurityAddress
        * Updated port field parsing to support short interface names.
    * Modified ShowLldpNeighborsInterfaceDetail
        * Made 'compiled' field as optional in schema to support outputs that do not contain 'compiled' field.
        * Added 'age_sec' and 'time_since_last_update_sec' fields as optional.
    * Modified ShowCloudMgmtConnect
        * Fixed section header regex (p2) to match Cloud-Mgmt prefixed section headers
        * Fixed p3 pattern to match 'service cloud-mgmt connect is disabled'
    * Modified ShowCloudMgmtConfigUpdater
        * Renamed p4_1/p4_2 to p4a/p4b to align with ShowMerakiConfigUpdater naming convention
        * Fixed p0 pattern to match 'service cloud-mgmt connect is disabled'
    * Modified ShowCloudMgmtCompatibility
        * Changed cloud_mgmt_cloud_monitoring and cloud_mgmt_cloud_management to Optional in schema to support empty output

* iosxr
    * Modified ShowProcessesMemoryDetail
        * Added optional pid key to the schema.
        * Updated regex pattern to accommodate show processes memory detail output with PID column.
    * Modified ShowPlatform
        * Modified parser for 'show platform' command for new State

* linux
    * Modified Ls
        * Updated command execution to build ``ls -{args}`` and ``ls -{args} {directory}`` from parser arguments.
        * Added ``l`` to supplied option arguments when long-listing output is not requested so the parser receives the expected output shape.
        * Added golden fixture coverage for ``ls -{args}`` and ``ls -{args} {directory}``.

* apic
    * Modified Ls
        * Updated command execution to build ``ls -{args}`` and ``ls -{args} {directory}`` from parser arguments.
        * Added ``l`` to supplied option arguments when long-listing output is not requested so the parser receives the expected output shape.
        * Added golden fixture coverage for ``ls -{args}`` and ``ls -{args} {directory}``.

* nxos
    * Modified Ls
        * Added golden fixture coverage for the inherited NXOS ACI ``Ls`` command forms.

* common
    * Modified package metadata
        * Added SDK generator parser datafiles to installed package data for ``make json_all``.
        * Updated the parser development package version to satisfy the current ``genie`` dependency range during CI installs.
    * Modified _fuzzy_search_command
        * Added exact command lookup after command preprocessing so normalized commands still resolve to their exact parser when available.
        * Updated fuzzy token scoring to prefer exact token matches over argument captures.
        * Added unittest coverage for fuzzy matching and argument extraction regressions.

--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInterfaceCounterErrors
        * show interfaces counters errors
        * show interfaces {interface} counters errors
    * Modified ShowIpCefDetail
        * Added support for parsing LISP related nexthops and remote EID stats
    * Modified ShowSubscriberSessionDetailed
        * Updated regex to support multi-word Access-type and Client values in the config history section
    * Modified ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Made 'ingress' and 'egress' fields as optional in schema to support outputs that do not contain the 'ingress' and 'egress' fields.
