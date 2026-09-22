April 2026
==========

April 28 - Genie v26.4
----------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v26.4
    ``genie.lamp``, v26.4
    ``genie.libs.health``, v26.4
    ``genie.libs.clean``, v26.4
    ``genie.libs.conf``, v26.4
    ``genie.libs.filetransferutils``, v26.4
    ``genie.libs.ops``, v26.4
    ``genie.libs.parser``, v26.4
    ``genie.libs.robot``, v26.4
    ``genie.libs.sdk``, v26.4
    ``genie.telemetry``, v26.4
    ``genie.trafficgen``, v26.4




Changelogs
^^^^^^^^^^


genie
"""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* abstraction
    * Added merged abstract package lookup support for ``Lookup(*tokens, packages=(...))`` while preserving dict-based package lookups and covering the new behavior with unit tests


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* abstraction
    * Optimized frame lookup in declare_package by using sys._getframe() instead of inspect.stack()
    * Optimized frame lookup in declare_token by using sys._getframe() instead of inspect.stack()
    * Optimized frame lookup in magic.py by using sys._getframe() instead of inspect.stack()



genie.lamp
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* shell
    * Move cmd2 persistent history file from ~/lamp_history.dat to

* history
    * Move advanced history file from ~/lamp_adv_history.dat to



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* stages
    * Updated ApplyConfiguration stage to pass timeout to show running-config and show startup-config commands to prevent timeout
    * Update Connect stage to use parameters.internal for correct result_rollup handling
    * Updated ConfigureInterfaces to disable switchport before configuring ipv4/ipv6 address on interfaces that default to L2 mode

* clean-pkg
    * InstallImage stage
        * Added validation check for empty output after install command execution
        * If the install command returns no output, log an error and fail the step.
    * stages/CopyToDevice
        * Use the actual destination path from the history, if the file was renamed during copying, we are checking for the correct file on the device.

* stages/iosxe
    * Update Connect stage to use parameters.internal and disable result_rollup on all steps when recovery is enabled

* iosxe
    * InstallImage stage
        * Fixed unnecessary two-time 'dir' command parsing.
        * Moved 'packages.conf' creation to use `touch_file` API.
        * Removed duplicate ignore-startup-config verification from `verify_boot_variable`.
    * ConfigureManagement stage
        * Added detailed log messages for interface status verification failures.
    * CopyToDevice stage
        * Merged 'get filesize' local & remote steps into one.

* iosxe/ie3k
    * InstallImage stage
        * Removed duplicate `install_image` function logic already present in IOS-XE.
        * Added `configure_no_boot_manual` to order.
    * RommonBoot stage
        * Complete revamp with correct logic.

* clean/stages/copy_to_device
    * Modified the copy_to_device stage to verify sufficient free space on device even if image files already exist on the device.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean/apply_configuration
    * Added skip_if_no_config option to skip apply configuration if no configuration is provided.

* stages/configure_management
    * Added check for master key security configuration and configure master key if missing.

* linux
    * Added image handler to linux.
    * Added api to execute configuration lines on linux devices, as linux does not have a configure method.

* stages/configure_interfaces
    * Added api to apply configuration lines to device.

* iosxe/ie3k
    * Added WriteErase stage.

* iosxe/ie9k
    * Added RommonBoot stage.
    * Added InstallImage stage.
    * Added WriteErase stage.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* linux
    * Added support for Linux configure interfaces in clean yaml.

* nxos
    * Modified
        * updating the interface configuration from 'mac address <>' to 'mac-address <>'



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Modified
        * Updated FileUtils abstraction resolution to use merged abstract package lookups for base and extension filetransferutils plugins

* protocols/http
    * Ignore SSL errors for stat.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* protocols
    * Added https support.



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""

genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Enchanced api for configure_crypto_ikev2_proposal
        * Added new  args to api configure_crypto_ikev2_proposal .
    * Enchanced api for configure_ikev2_profile
        * Added new args to api configure_ikev2_profile .
    * Enchanced api for config_extended_acl
        * Added new  args to api config_extended_acl .


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* ios
    * Added IOS SDK API support for
        * `enable_debug`
        * `disable_debug`
    * Matches existing iosxe debug API style and naming.
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_ip_cef`
        * `unconfigure_ip_cef`
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_interface`
        * `unconfigure_interface`
    * Supports optional IPv4/IPv6 addressing, MAC address, ipv6 enable,
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_interface_ipv6_nd`
        * `unconfigure_interface_ipv6_nd`
    * Supports optional ipv6 enable, ns-interval, dad attempts, keepalive,
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_simulator_radius_subscriber`
        * `unconfigure_simulator_radius_subscriber`
        * `configure_service_simulator_radius`
        * `unconfigure_service_simulator_radius`
    * Supports optional attributes, VSAs, authentication, service type,
    * Added unit test coverage for the new APIs.
    * Added IOS SDK API support for
        * `configure_simulator_radius_server`
        * `unconfigure_simulator_radius_server`
        * `configure_simulator_radius_key`
        * `unconfigure_simulator_radius_key`
    * Supports optional user-name prefixes and client shared-secret.
    * Added unit test coverage for the new APIs.

* iosxe/management
    * Added configure_management_master_key API to check and configure master key.

* iosxe
    * Added
        * configure_crypto_mib_ipsec_flowmib_history_failure_size API
    * Added API configure_redundancy_interchassis_group
        * added api to configure redundancy interchassis group
    * Added execute_show_ipv6_dhcp_interface, execute_show_ipv6_dhcp_interface_all to dhcpv6-execute.py
        * New API support for 'show ipv6 dhcp interface' and 'show ipv6 dhcp interface {interface}' cli
    * API for unconfigure_ip_igmp_access_group
    * Added API configure_mpls_label_range
    * Added API unconfigure_mpls_label_range
    * Added configure_ip_igmp_filter
    * Added unconfigure_ip_igmp_filter
    * Added configure_igmp_filter_on_interface
    * Added unconfigure_igmp_filter_on_interface
    * Added configure_igmp_profile
    * Added unconfigure_igmp_profile
    * Added test_system_secure_db API
        * Added new api to execute the "test system secure db" command
    * Added test_system_secure_all API
        * Added new api to execute the "test system secure all" command
    * KEY
        * Added api for configure_key_config_key_password_encrypt
        * Added api for unconfigure_key_config_key_password_encrypt
    * Added API enable_autoconfig
        * added api to configure uplink autoconfig
    * Added VPDN clear execute APIs
        * execute_clear_vpdn_dead_cache_all
        * execute_clear_vpdn_dead_cache_ip_address
        * execute_clear_vpdn_dead_cache_group
        * execute_clear_vpdn_tunnel_l2tp_all
        * execute_clear_l2tp_all
    * Added configure_vrf_route_leak_static
    * Added unconfigure_vrf_route_leak_static
    * Added API configure_vpdn_group enhancements
        * added support for prioritized initiate-to ip entries and l2tp tunnel busy timeout
    * Added APIs for vpdn l2tp attributes
        * added configure helper for the initial-received-lcp-confreq attribute
        * added configure and unconfigure helpers for the physical-channel-id attribute
    * Added
        * configure_crypto_mib_ipsec_flowmib_history_tunnel_size API
    * Added AAA SDK API support for
        * `no aaa accounting network default group <group_name>`
        * `aaa authentication ppp default group <group_name>`
    * Added unit test coverage for the new APIs and the existing
    * Added configure_interface_port_settings to interface-configure.py
        * New API support for 'port-settings speed {speed} duplex {duplex} autoneg {autoneg}' cli
    * Added unconfigure_interface_port_settings to interface-configure.py
        * New API support for 'no port-settings speed {speed}', 'no port-settings duplex {duplex}', 'no port-settings autoneg {autoneg}' cli
    * Added default_interface_port_settings to interface-configure.py
        * New API support for 'default port-settings [speed] [duplex] [autoneg]' cli
    * Added configure_ospfv3_max_path
        * configure maximum number of equal cost paths for OSPFv3.
    * Added API touch_file.
    * Added API get_filesystems.
    * Added unconfigure_ip_fqdn_acl API
        * Added new api to unconfigure ip fqdn acl
    * Added
        * configure_crypto_isakmp_enable API

* *******************************************************************************

* iosxe/ie3k
    * Added API touch_file.
    * Added API get_recovery_details.
    * Added API execute_rommon_reset.
    * Added API device_rommon_boot.
    * Added API password_recovery.

* iosxe/ie9k
    * Added API touch_file.
    * Added API get_recovery_details.
    * Added API execute_rommon_reset.
    * Added API device_rommon_boot.
    * Added API password_recovery.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_unconfigure_ipv6_flow_monitor
        * test_unconfigure_monitor_capture_buffer_size
        * test_unconfigure_monitor_capture_limit_packet_len
        * test_unconfigure_monitor_capture_without_match
        * test_unconfigure_record_configs_from_flow_monitor
        * test_unconfigure_sampler
        * test_configure_flow_monitor_sampler_fnf_sampler
        * test_configure_crypto_map_for_gdoi
        * test_configure_gdoi_group
        * test_unconfigure_crypto_map_for_gdoi
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Added API for configuring live-protect shield enforcing mode
        * configure_platform_security_live_protect_shield_enforcing
        * unconfigure_platform_security_live_protect_shield_enforcing
    * Modified the following unit tests to replace mock_data.yaml usage with unittest.mock.Mock
        * test_api_configure_interface_vlan_standby_ip
        * test_api_configure_interface_vlan_standby_preempt
        * test_api_configure_interface_vlan_standby_timers
        * test_api_configure_vrrp_interface
        * test_api_unconfigure_hsrp_interface
        * test_api_unconfigure_interface_vlan_standby_ip
        * test_api_unconfigure_interface_vlan_standby_preempt
        * test_api_unconfigure_interface_vlan_standby_timers
        * test_api_unconfigure_vrrp_interface
        * test_api_configure_hw_module_slot_shutdown
    * Removed mock_data.yaml files associated with the above unit tests as they are no longer required
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_ip_igmp_snooping_vlan_querier
        * test_api_unconfigure_ip_igmp_snooping_vlan_query_version
        * test_api_unconfigure_ip_igmp_snooping_vlan_static
        * test_api_unconfigure_ip_igmp_snooping_vlan_vlanid
        * test_api_clear_crypto_call_admission_stats
        * test_api_clear_crypto_session
        * test_api_configure_crypto_logging_ikev2
        * test_api_configure_ikev2_authorization_policy
        * test_api_configure_ikev2_cac
        * test_api_configure_ikev2_dpd
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Added configure_ignore_startup_config
        * Added configure_ignore_startup_config to c8kv.
    * Added execute_monitor_capture_file_location_flash
        * execute monitor capture file location flash command enhancement
    * Modified the following unit tests to replace mock_data.yaml usage with unittest.mock.Mock
        * test_api_configure_server_redundancy_under_gkm_group
        * test_api_configure_gnxi
        * test_api_configure_400g_mode_for_port_group
        * test_api_configure_400g_mode_for_port_group_onsvl
        * test_api_configure_400g_mode_port_group_range
        * test_api_configure_hw_module_breakout
        * test_api_unconfigure_400g_mode_for_port_group
        * test_api_unconfigure_400g_mode_for_port_group_onsvl
        * test_api_unconfigure_400g_mode_port_group_range
        * test_api_unconfigure_hw_module_breakout
    * Removed mock_data.yaml files associated with the above unit tests as they are no longer required
    * Refactored the following unit tests as part of the API UT mock cleanup
        * test_api_unconfigure_hw_module_slot_shutdown
        * test_api_configure_icmp_ip_reachables
        * test_api_unconfigure_icmp_ip_reachables
        * test_api_configure_igmp_snooping_tcn_flood
        * test_api_configure_ip_igmp_querier_query_interval
        * test_api_configure_ip_igmp_querier_tcn_query_count
        * test_api_configure_ip_igmp_snooping
        * test_api_configure_ip_igmp_snooping_querier
        * test_api_configure_ip_igmp_snooping_vlan_querier
        * test_api_configure_ip_igmp_snooping_vlan_query_version
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_gdoi_group
        * test_api_unconfigure_gdoi_group_on_gm
        * test_api_configure_client_protocol_under_gkm_group
        * test_api_configure_gikev2_profile_under_gkm_group
        * test_api_configure_gkm_group_identity_number
        * test_api_configure_ipsec_under_gkm_group
        * test_api_configure_ipv4_server_under_gkm_group
        * test_api_configure_pfs_enable_or_disable_under_gkm_group
        * test_api_configure_protocol_version_optimize_cli_under_gkm_group
        * test_api_configure_rekey_under_gkm_group
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified configure_interface_port_settings in interface-configure.py
        * Added optional ``combined_port_settings``argument to build a single combined``port-settings`` command
    * Modified unconfigure_interface_port_settings in interface-configure.py
        * Added optional ``combined_port_settings``argument to build a single combined``port-settings`` command
    * Modified default_interface_port_settings in interface-configure.py
        * Added optional ``combined_port_settings``argument to build a single combined``port-settings`` command
    * Refactored the following unit tests as part of the API UT mock cleanup
        * test_api_configure_ip_igmp_snooping_vlan_static
        * test_api_configure_ip_igmp_snooping_vlan_vlanid
        * test_api_unconfigure_igmp_snooping_tcn_flood
        * test_api_unconfigure_ip_igmp_querier_max_response_time
        * test_api_unconfigure_ip_igmp_querier_query_interval
        * test_api_unconfigure_ip_igmp_querier_tcn_query_count
        * test_api_unconfigure_ip_igmp_querier_tcn_query_interval
        * test_api_unconfigure_ip_igmp_querier_timer_expiry
        * test_api_unconfigure_ip_igmp_snooping
        * test_api_unconfigure_ip_igmp_snooping_querier
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_ikev2_fragmentation
        * test_api_configure_ikev2_keyring
        * test_api_configure_ikev2_policy
        * test_api_configure_ikev2_profile
        * test_api_configure_ikev2_profile_advanced
        * test_api_configure_isakmp_key
        * test_api_configure_isakmp_policy
        * test_api_configure_modify_ikev2_profile
        * test_api_disable_crypto_engine_compliance
        * test_api_unconfigure_crypto_logging_ikev2
    * Removed mock_data.yaml files for the above tests as they are no longer needed

* updated api unit tests
    * IOSXE
        * Updated unittests to new testing method
            * configure_bulkstat_profile
            * configure_call_admission
            * configure_call_home_reporting
            * configure_cdp_run
            * configure_clear_logging_onboard_slot_environment
            * configure_clear_logging_onboard_slot_temperature
            * configure_clear_logging_onboard_slot_voltage
            * configure_clear_logging_onboard_switch_environment
            * configure_clear_logging_onboard_switch_temperature
            * configure_clear_logging_onboard_switch_voltage
    * IOSXE
        * Updated unittests to new testing method
            * configure_clock_timezone
            * configure_commands_to_template
            * configure_cos
            * configure_default_stack_power_auto_off
            * configure_default_stack_power_ecomode
            * configure_default_stack_power_switch_power_priority
            * configure_device_classifier
            * configure_device_classifier_command
            * configure_diagnostic_bootup_level_minimal
            * configure_diagnostic_monitor_interval_module
    * IOSXE
        * Updated unittests to new testing method
            * configure_diagnostic_monitor_module
            * configure_diagnostic_monitor_switch
            * configure_diagnostic_monitor_syslog
            * configure_diagnostic_schedule_module
            * configure_diagnostic_schedule_switch
            * configure_diagonistics_monitor_switch
            * configure_enable_http_server
            * configure_enable_secret_password
            * configure_event_manager
            * configure_event_manager_applet
    * IOSXE
        * Updated unittests to new testing method
            * configure_archive_rollback
            * configure_archive_time_period
            * configure_archive_write_memory
            * configure_bba_group
            * configure_bba_group_session_auto_cleanup
            * configure_boot_manual_switch
            * configure_boot_system_image_file
            * configure_boot_system_switch_switchnumber
            * configure_bridge_domain
            * configure_broadband_aaa
    * IOSXE
        * Updated unittests to new testing method
            * configure_pbr_route_map
            * configure_route_map_under_interface
            * modify_pbr_route_map
            * unconfigure_route_map_under_interface
            * configure_crypto_pki_profile
            * configure_no_pki_enroll
            * configure_pki_authenticate
            * configure_pki_authenticate_certificate
            * configure_pki_enroll
            * configure_pki_export
    * IOSXE
        * Updated unittests to new testing method
            * configure_event_manager_applet_event_none
            * configure_graceful_reload
            * configure_graceful_reload_interval
            * configure_hw_module_logging_onboard
            * configure_hw_module_slot_breakout
            * configure_hw_module_slot_logging_onboard_environment
            * configure_hw_module_slot_logging_onboard_temperature
            * configure_hw_module_slot_logging_onboard_voltage
            * configure_hw_module_slot_upoe_plus
            * configure_hw_module_switch_number_auto_off_led
    * IOSXE
        * Updated unittests to new testing method
            * configure_hw_module_switch_number_ecomode_led
            * configure_hw_switch_logging_onboard
            * configure_hw_switch_switch_logging_onboard_environment
            * configure_hw_switch_switch_logging_onboard_temperature
            * configure_hw_switch_switch_logging_onboard_voltage
            * configure_interface_macro
            * configure_interface_VirtualPortGroup
            * configure_ip_domain_name
            * configure_ip_domain_name_vrf_mgmt_vrf
            * configure_ip_domain_timeout
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_crypto_pki_server
            * unconfigure_trustpoint
            * clear_macro_auto_confgis
            * config_cns_agent_passwd
            * configure_absolute_time_range
            * configure_action_string
            * configure_action_syslog_msg
            * configure_archive_default
            * configure_archive_logging
            * configure_archive_maximum

* nxos
    * Modified
        * ISSU HA boot-mode validation now skips `show boot mode` on EOR platforms.
        * EOR/TOR detection is based on `show module` output (`Virtual Supervisor Module`).
        * Added unit tests for EOR detection and EOR ISSU boot-mode skip behavior.

* iosxe/interface/execute
    * Fixed execute_test_crash API authentication failure after device reboot

* dependencies
    * update pyasn1 to 0.6.3 to address CVE-2026-23490
    * Removed `pysnmp-sync-adapter` dependency from the SNMP powercycler implementation

* iosxe/ie3k
    * Removed API configure_ignore_startup_config.
    * Removed API unconfigure_ignore_startup_config.
    * Removed API verify_ignore_startup_config.
    * Removed API get_config_register.
    * Removed API execute_set_config_register.

* iosxe/ie9k
    * Modified API get_boot_variables to use IE3k implementation for consistency.

* iosxe/rommon
    * Updated device_rommon_boot
        * Added support for getting all the subconnections to rommon to maintain the stability.


--------------------------------------------------------------------------------
                                     Iosxe                                      
--------------------------------------------------------------------------------

* *******************************************************************************

* added `execute_ping_egress_next_hop` to support next-hop ping egress execution

* added `configure_ip_local_policy_route_map` for global `ip local policy`


--------------------------------------------------------------------------------
                                 Configuration.                                 
--------------------------------------------------------------------------------

* added `replace_extended_acl_entries` to recreate extended acl entries in a


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* nxos
    * UTILS
        * Modified `mgmt_src_ip_addresses` and `mgmt_ip_addresses` regex patterns to capture both mgmt_src_ip_addresses and mgmt_ip_addresses correctly.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowTelemetryIETFSubscription
        * Handling renamed column header
    * Modified ShowTelemetryIETFSubscriptionAllReceivers
        * Handling added field
    * Modified ShowTelemetryReceiverName
        * Handling renamed column header
    * Modified ShowTelemetryReceiverAll
        * Handling renamed column header
    * Added ShowIpv6Dhcp
        * Added schema and parser for 'show ipv6 dhcp'
    * Added ShowPlatformHardwareQfpActiveInterfaceAllStatistics parser in show_platform_hardware.py
        * Added schema and parser for cli 'show platform hardware qfp active interface all statistics'
    * Added ShowPlatformSoftwareLiveProtectShield
        * show platform software live-protect shield
    * Added ShowIpSshPubkeyServerAll
        * Added schema and parser for 'show ip ssh pubkey server all'
    * Created ShowSystemInsecureConfiguration
        * Added schema and parser implementation for "show system insecure-configuration".
    * Created ShowSystemSecurityMode
        * Added schema and parser implementation for "show system security-mode".
    * Added SnmpGetBulk
        * Added schema and parser for 'snmp get-bulk v{version} {ip} vrf {vrf} {community_str} non-repeaters {non_repeaters} max-repetitions {max_repetitions} oid {oid}' command.
        * Added schema and parser for 'snmp get-bulk v{version} {ip} {community_str} non-repeaters {non_repeaters} max-repetitions {max_repetitions} oid {oid}'
        * Added timeout parsing support for invalid VLAN community strings.
    * Added ShowPlatformSoftwareAccessListFpActiveStatistics
        * Added schema and parser for 'show platform software access-list fp active statistics'
    * Added ShowRepTopology
        * Added schema and parser for 'show rep topology'
    * Added ShowPlatformHardwareSlotSlotSensorConsumerAll
        * Added schema and parser for 'show platform hardware slot {slot} sensor consumer all'
    * Modified ShowTelemetryIETFSubscriptionDetail
        * Adding parsing of reciever information
    * Added ShowPlatformSoftwareFedSwitchFnfFlowTableMonId
        * Parser for 'show platform software fed switch {switch} fnf flow-table mon-id {mon_id} asic {asic} start-index {start_index} {num_flows}'
    * Added ShowPlatformHardwareSlotSlotSensorProducerAll
        * Added schema and parser for 'show platform hardware slot {slot} sensor producer all'
    * Added ShowRedundancyInterchassis parser in show_redundancy.py
        * Added schema and parser for cli 'show redundancy interchassis'
    * Added ShowPlatformSoftwareFedSwitchActiveVmapAll parser.
        * Added parser for cli 'show platform software fed switch active vmap all'.
    * Added ShowPlatformSoftwareFedSwitchActiveVpKeyDetail parser.
        * Added parser for cli 'show platform software fed switch active vp key {iif_id} {vlan_id} detail'.
    * Added ShowPolicyMapControlPlaneAll
        * Added schema and parser for 'show policy-map control-plane all'
    * Added show platform software selinux
        * Added schema and parser for show platform software selinux
    * Added ShowInterfacesInterfaceStat
        * Added schema and parser for 'show interfaces {interface} stat'
    * Added Parser for show cts keystore
        * Added a new schema and parser for the show cts keystore command.
    * Added show ipv6 route vrf {vrf} summary internal
        * Parse "show ipv6 route vrf {vrf} summary internal"
    * Added ShowHwModuleSubslotSubslotTransceiverTransceiverStatus
        * Added schema and parser for 'show hw-module subslot {subslot} transceiver {transceiver} status'

* iosxr
    * Added ShowControllersInterface
        * Added schema and parser for 'show controllers {interface}' command.
    * Added ShowControllersOpticsAppselAdvertised
        * Added schema and parser for 'show controllers optics {port} appsel advertised' command.
        * Added schema and parser for 'show controllers optics * appsel advertised' command.
    * Added ShowControllersOpticsObservableInfo
        * Added schema and parser for 'show controllers optics {port} observable-info' command.
        * Added schema and parser for 'show controllers optics * observable-info' command.
    * Added ShowControllersOpticsAppselDetailed
        * Added schema and parser for 'show controllers optics {port} appsel detailed' command.
        * Added schema and parser for 'show controllers optics * appsel detailed' command.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformSoftwareFedActiveMonitor
        * Updated regex pattern and code the fetch the valn name.
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmMactable
        * Updated regex pattern to handle "machandle", "sihandle", "rihandle", "dihandle" values.
    * Modified ShowCryptoIpsecSaInterface
        * Updated regex pattern p3 and p30 to handle missing remaining_key_lifetime values.
    * Modified ShowModule
        * Updated show module parsing to correctly match module entries for multiple entries also(switch number 1 and 2).
    * Modified ShowIpv6cefExactRouteSchema parser
        * changed regex to take both ip and ipv6 addresses
    * Modified ShowPlatformHardwareFedSwitchActiveVlanIngress
        * Modified parser by adding cli 'show platform hardware fed switch active vlan {num} egress'
    * Modified ShowPlatformSoftwareFedSwitchActiveMatmMactable
        * Made 'machandle', 'sihandle', 'rihandle', 'dihandle' fields optional in schema
        * Updated regex to handle output format without handle columns
    * Modified ShowPlatformSoftwareFedIpv6RouteSummaryInclude
        * Added support to make available of below clis for all cat9k.
    * show platform software fed {switch} {mode} ipv6 route summary | include {match}
    * show platform software fed {mode} ipv6 route summary | include {match}
    * Modified ShowDeviceTrackingDatabase
        * Updated regex pattern to handle parenthesized time_left values from DHCPv6 prefix delegation entries.

* iosxr
    * Modified ShowPlatform
        * Modified parser for 'show platform' command to include '[]' in Type column


--------------------------------------------------------------------------------
                                    Command.                                    
--------------------------------------------------------------------------------



genie.telemetry
"""""""""""""""
