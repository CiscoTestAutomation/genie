February 2023
==========

February 28 - Genie v23.2
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.2                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.2                          |
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
    * Fixed discovery of triggers, ignore global_processors as trigger

* genie.json
    * Removed the ignore directory from MAkeApi

* harness
    * Fixed schema of mapping datafile
        * Supported `list` for `via` in mapping datafile for HA device


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* harness
    * Added parallel
        * Added Verifications test container to support running verifications over different devices in parallel



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* linux
    * Added
        * New clean stages were added for wsim under linux.
    * Added configure_controller_details
        * API Configures the controller details on wsim
    * Added configure_ap_details
        * API Configures the ap details on wsim
    * Added configure_client_details
        * API Configures the client details on wsim
    * Added run_wsim_config
        * API that runs the configs on wsim
    * Added configure_ap_client_count
        * API Configures the ap client count details on wsim
    * Added simulate_ap_container
        * API simulates the containers on wsim
    * Added verify_ap_associate
        * API verify ap join status on wsim

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


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* common
    * Updated 'apply_configuration' clean stage
        * added dialog to handle prompt by `license accept end user agreement`



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
                                      Fix
--------------------------------------------------------------------------------

* genie.libs.robot
    * Updated use genie testbed keyword, ensure mapping values are set



genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added unconfigure_router_bgp_network_mask
        * New API to unconfigure router bgp network mask
    * Added configure_call_home_street_address
        * API to configure call-home street-address
    * Added configure_call_home_syslog_throttling
        * API to configure call-home syslog-throttling
    * Added configure_call_home_vrf
        * API to configure call-home vrf
    * Added configure_call_home_aaa_authorization
        * API to configure call-home aaa-authorization
    * Added configure_call_home_alert_group
        * API to configure call-home alert-group
    * Added configure_call_home_alert_group_config_snapshot
        * API to configure call-home alert-group-config snapshot
    * Added configure_call_home_contact_email_addr
        * API to configure call-home contact_email_addr
    * Added configure_call_home_contract_id
        * API to configure call-home contract-id
    * Added configure_call_home_copy_profile
        * API to configure call-home copy profile
    * Added configure_call_home_customer_id
        * API to configure call-home customer-id
    * Added configure_call_home_data_privacy
        * API to configure call-home data-privacy
    * Added configure_call_home_http_resolve_hostname_ipv4_first
        * API to configure call-home http resolve-hostname ipv4-first
    * Added configure_call_home_http_secure_server_identity_check
        * API to configure call-home secure server-identity-check
    * Added configure_call_home_http_proxy
        * API to configure call-home http-proxy
    * Added configure_call_home_mail_server
        * API to configure call-home mail-server
    * Added configure_call_home_phone_number
        * API to configure call-home phone-number
    * Added configure_call_home_rate_limit
        * API to configure call-home rate-limit
    * Added unconfigure_call_home_sub_cli
        * API to unconfigure call-home sub-cli
    * Added unconfigure_call_home
        * API to unconfigure call-home
    * Added clear_cdp_table API
        * API to clear cdp table
    * Added configure_hsrp_interface API
        * API to configure hsrp on interface
    * Added unconfigure_hsrp_interface API
        * API to unconfigure hsrp on interface
    * Added configure_vrrp_interface and configure_vrrp_interface  API
        * API to configure, unconfigure vrrp on interface
    * Added configure_vtp_password API
        * API to configure vtp password
    * Added unconfigure_vtp_password API
        * API to unconfigure vtp password
    * Added configure_vtp_primary API
        * API to set vtp primary
    * Added unconfigure_udld API
        * API to unconfigure udld with options
    * Added clear_bgp_all_as
        * New API to clear bgp all
    * Added configure_default_vxlan
        * New API to configure default vxlan under vrf definition
    * Added configure_mdt_overlay_use_bgp_spt_only
        * New API to configure mdt overlay under bgp
    * Added configure_router_ospf_redistribute_internal_external
        * New API to configure ospf under redistribute internal/external
    * Added clear_platform_qos_statistics_internal_cpu_policer
        * API to clear qos statistics internal cpu policer
    * Added clear_platform_qos_dscp_cos_counters_interface
        * API to clear qos dscp-cos counters on interface
    * Added get_dscp_cos_qos_queue_stats
        * API to get qos dscp-cos counters on interface
    * Added configure_bgp_neighbor_filter_description
        * API configure_bgp_neighbor_filter_descriptionto configure bgp neighbor filter
    * Added configure_service_template_with_command_line
        * New API to configure service template with commands
    * Added configure_unconfigure_interface_port_channel
        * API for configure unconfigure interface port channel on device
    * Added configure_unconfigure_default_switchport_trunk_vlan
        * API for configure unconfigure default switchport trunk vlan
    * Added configure_unconfigure_vlan_state_suspend
        * API for configure unconfigure vlan state suspend
    * Added configure_unconfigure_vlan_state_active
        * API for configure unconfigure vlan state active
    * Added configure_unconfigure_mac_address_table_notification_change
        * API for configure unconfigure mac address table notification change
    * Added configure_unconfigure_datalink_flow_monitor
        * API for configure unconfigure datalink flow monitor
    * Added configure_ip_dhcp_pool_host API
        * API to configure DHCP host pool
    * Added unconfigure_ip_dhcp_pool_host API
        * API to unconfigure host for DHCP pool
    * Added configure_stack_power_switch_power_priority
        * API to configure stack_power_switch/stack power-priority high/low/switch priority value
    * Added unconfigure_stack_power_switch_power_priority
        * API to unconfigure stack_power_switch/stack power-priority high/low/switch priority value
    * Added configure_default_stack_power_switch_power_priority
        * API to configure stack_power_switch/stack default power-priority high/low/switch priority value
    * Added configure_stackpower_stack_switch_standalone
        * API to configure stackpower stack switch standalone
    * Added unconfigure_stackpower_stack_switch_no_standalone
        * API to unconfigure stackpower stack switch no standalone
    * Added configure_stack_power_switch_standalone
        * API to enable configure stack power_switch standalone
    * Added configure_stack_power_switch_no_standalone
        * API to enable configure stack_power switch no standalone
    * Added to configure_stack_power_mode_power_shared
        * API to enable configure stack power mode power shared
    * Added unconfigure_boot_system_switch_switchnumber
        * API to unconfigure boot system switch
    * Added configure_boot_system_switch_switchnumber
        * API to configure boot system switch
    * Added restore_running_config_file
        * API to restore_running_config_file
    * Modified configure_software_auto_upgrade
        * Added auto_upgrade_option == 'disable' option
    * Added snmp_server_engine_id_local API
        * snmp_server_engine_id_local
    * Added cry key generate rsa encryption mod label API
        * cry key generate rsa encryption
    * Added configure_service_private_config_encryption
        * configure service private config encryption
    * Added unconfigure_service_private_config_encryption
        * no configure service private config encryption
    * Added configure_device_sensor_filter_list_lldp
        * configure device sensor filter list lldp
    * Added configure_hw_module_switch_num_usbflash
        * configure hw module switch num usbflash
    * Added unconfigure_hw_module_switch_num_usbflash
        * unconfigure hw module switch num usbflash
    * Added configure_hw_module_switch_num_usbflash_security_password
        * configure hw module switch num usbflash security password enable/disable
    * Added execute_set_memory_debug_incremental_starting_time
        * execute set memory debug incremental starting-time command
    * Added unconfigure_ip_igmp_join_group
        * New API to unconfigure ip igmp join group
    * Added configure_aaa_authorization_network
        * New API to configure aaa authorization network group
    * Added configure_mac_address_table_static and unconfigure_mac_address_table_static
        * API to configure mac address table , unconfigure
    * Added unconfigure_network_policy_profile_number
        * API to unconfigure network policy
    * Added configure_ip_pim_ssm and unconfigure_ip_pim_ssm
        * API to configure ip pim ssm , unconfigure
    * Added configure_ipv6_mld_snooping and unconfigure_ipv6_mld_snooping
        * API to configure mld snooping, unconfig
    * Added configure_ip_pim_rp_address and unconfigure_ip_pim_rp_address
        * API to configure and unconfigre ip pim rp address.
    * Added configure_ip_pim_enable_bidir_enable and unconfigure_ip_pim_enable_bidir_enable
        * API to configure and unconfigure ip bim enable bidir.
    * added configure_ipv6_mld_snooping_vlan_mrouter_interface
        * APIs to configure snooping vlan morouter with interface
    * Added unconfigure_global_network_policy
        * API for unconfigure network policy profile globally
    * Modified configure_network_policy_profile_voice_vlan
        * Added "voice-signaling vlan {vlan} cos {cos}" and "voice-signaling vlan {vlan} cos {dscp}" optional configs
    * Modified unconfigure_network_policy_profile_voice_vlan
        * Added optional keyword arguments cos=None, dscp=None
    * Added configure_interface_ipv6_acl API
        * API to configure ipv6 acl
    * Added configure_standard_acl and unconfigure_standard_aclAPI
        * API to configure , unconfigure standard acl
    * Added configure_as_path_acl API
        * API to configure as path acl on interface
    * Added unconfigure_as_path_acl API
        * API to unconfigure as path acl on interface
    * Added configure_administrative_weight API
        * API to configure the interface admin weight
    * Added configure_interface_path_selection_metric API
        * API to configure interface path selection metric
    * Added unconfigure_ip_rsvp_bandwidth API
        * API to unconfigure the ip rsvp bandwith in interface
    * Added unconfigure_dynamic_path_in_tunnel API
        * API to unconfigure various dynamic paths
    * Added l2vpn_xconnect_context_interface API
        * API to configure the xconnect context in the interface
    * Added unconfigure_ospf_cost
        * Added new API unconfigure ospf cost in interface
    * Modified configure_explicit_path
        * Modified the existing API configure_explicit_path
    * Delete API configure_hsrp_interface from /iosxe/hsrp/configure.py file as it is duplicate.
        * Delete API configure_hsrp_interface
    * Added execute_install_label
        * New API to execute install label
    * Added configure_process_cpu_threshold_type_rising_interval
        * New API to configure cpu thershold type rising interval
    * Added unconfigure_process_cpu_threshold_type_rising_interval
        * New API to unconfigure cpu thershold type rising interval
    * Added configure_process_cpu_statistics_limit_entry_percentage_size
        * New API to configure cpu statistics limit entry percentage size
    * Added unconfigure_process_cpu_statistics_limit_entry_percentage_size
        * New API to unconfigure cpu statistics limit entry percentage size
    * Added configure_macro_auto_global_processing_on_interface
        * New API to configure macro auto global processing on interface level
    * Added unconfigure_macro_auto_global_processing_on_interface
        * New API to unconfigure macro auto global processing on interface level
    * Added configure_macro_auto_global_processing
        * New API to configure macro auto global processing on global mode
    * Added unconfigure_macro_auto_global_processing
        * New API to unconfigure macro auto global processing on global mode
    * Added unconfigure_autoconf
        * New API to unconfigure autoconf enable
    * Added unconfigure_ip_igmp_ssmmap_static
        * New API to unconfigure ip igmp ssmmap static
    * Added configure_ip_igmp_access_group
        * New API to configure ip igmp access-group on interface
    * Added configure_call_home_profile_destination_address
    * Added configure_call_home_profile_destination_message_size_limit
    * Added configure_call_home_profile_destination_preferred_msg_format
    * Added configure_call_home_profile_destination_transport_method
    * Added unconfigure_call_home_profile
    * Added configure_service_call_home
    * Added unconfigure_service_call_home
    * Added configure_call_home_profile_subscribe_to_alert_group
    * Added configure_call_home_profile_anonymous_reporting_only
    * Added configure_call_home_profile_active
    * Added unconfigure_call_home_profile_active
    * Added configure_call_home_profile_reporting
    * Added configure_management_ip api
        * API to configure the management ip
    * Added configure_management_gateway api
        * API to configure the management gateway
    * Added configure_management_routes
        * API to configure the management routes
    * Added configure_management_protocols
        * API to configure the management protocols
    * Added configure_management
        * API to configure the management information from testbed
    * Added configure_management_tftp
        * API to configure the management tftp
    * Added configure_management_http
        * API to configure the management http
    * Added configure_management_ssh
        * API to configure the management ssh
    * Added configure_management_telnet
        * API to configure the management telnet
    * Added configure_management_vty_lines
        * API to configure the management vty_lines
    * Added configure_management_netconf
        * API to configure the management netconf

* triggers
    * Blitz
        * Removed the if condition because it is not connecting when the connection is lost inbetween.


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_bgp_neighbor_filter_description
        * Modified api in configure bgp neighbor filter description
    * Modified configure_ip_igmp_join_group
        * Modified configure ip igmp join group
    * Fixed configure_clear_logging_onboard_switch_temperature.
        * API y/n prompt handling is fixed.
    * Fixed configure_clear_logging_onboard_switch_voltage.
        * API y/n prompt handling is fixed.
    * Fixed configure_clear_logging_onboard_switch_environment.
        * API y/n prompt handling is fixed.
    * Fixed clear_macro_auto_confgis.
        * Returing api output
    * Modified
        * Fix Restore API check_checkpoint_status which gave KeyError due to change in ShowArchive parser
    * Modified configure_switchport_trunk_allowed_vlan
        * Added two commands of "switchport", "switchport mode trunk" to accept allowed vlans configuration command
    * Modified execute_install_one_shot
        * Added xfsu optional flag.
    * Updated `delete_unprotected_files` API
        * Added `destination` argument

* sdk/powercycler
    * Modified raritan-px2_v3 to raritan-px2 and changed the connection_type to snmpv3.

* updated make json

* common
    * Updated `free_up_disk_space` API
        * Added `destination` argument

* ios
    * Updated `delete_unprotected_files` API
        * Added `destination` argument

* nxos
    * Updated `delete_unprotected_files` API
        * Added `destination` argument

* apic
    * Updated `delete_unprotected_files` API
        * Added `destination` argument

* powercycler
    * Updated `on` and `off` methods
        * Fixed `outlets` argument handling


--------------------------------------------------------------------------------
                                     Fixed
--------------------------------------------------------------------------------

* iosxe
    * Fixed iosxe verify module state method


--------------------------------------------------------------------------------
                                     Update
--------------------------------------------------------------------------------

* iosxe
    * Added few parameters to configure_parameter_map_subscriber API
    * Added a space and corrected spelling in remove_port_channel_interface API



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMroute
        * To support vxlan v6 enacap and ipv6 address
        * Sample output (Vlan500, VXLAN v6 Encap (50000, FF131), Forward/Sparse, 001731/stopped, flags)
    * Modified ShowIpMfib
        * To support vxlan v6 enacap and ipv6 address
        * Sample output (Vlan500, VXLAN v6 Encap (50000, FF131) Flags F)
    * Modified ShowIpv6MfibSchema
        * To support optional multicast group and source addresses, Where "show ipv6 mfib" output can be empty.
        * Sample output ((66666,FF131) entry not found)
    * Modified ShowFlowMonitoreCache
        * Added more parameters to the entry dict.
        * Made the existing variables optional in the schema.
    * Modified ShowIpDhcpBinding
        * Added "show ip dhcp binding vrf {vrf_name}" cli.
    * Modified ShowIdpromInterface
        * Fixed parser for ParserNotFound error.
            * Changed 'mode' to 'interface'
    * Fixed ShowIpIgmpSnoopingDetail
        * Changed 'cgmp_inter_mode' key as optional in schema and added unit test.
    * Fixed ShowIpIgmpSnoopingGroups
        * Fixed regular expression to fetch multiple ports as a string for 'port' key.
    * Fixed ShowIpMroute
        * Fixed 'flags' regular expression pattern and supporting unit tests files are added
    * Modified showIpv6MldSnooping
        * Added optional key 'explicit_host_tracking' and unit tests
    * Modified ShowIsisNeighbors
        * updated regex to account for the new cli output when there is a long hostname
    * Modified ShowLldpEntry
        * Fixed the parser by making 'chassis_id' as optional and unit test case is added.
    * Enhanced ShowMonitorCaptureBufferDetailed
        * Enhanced the parser by adding the optional argument 'display-filter' to the existing cli show command, and included 'dscp_value' in the parser output.
    * Deleted ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface
        * Duplicate parser for show platform hardware fed switch {switch_type} qos dscp-cos counters interface {interface} deleted.
    * Modified ShowProcessesPlatformCProcess
        * Moved up the class from iosxe/cat9k to iosxe
        * Moved also UTs from iosxe/cat9k/tests to iosxe/tests
    * Modified ShowProcessesPlatformIProcess
        * Moved up the class from iosxe/cat9k to iosxe
        * Moved also UTs from iosxe/cat9k/tests to iosxe/tests
    * Modified ShowSdmPrefer
        * Made some parameters as Optional and fixed regular expressions.
    * Modified ShowSpanningTreeInterfaceDetail
        * Made couple of schema variables optional and added unit test case.
    * Fixed ShowSpanningTreeInterface
        * Fix the command from "show spanning tree interface {interface}" to "show spanning-tree interface {interface}"
    * Modified ShowTemplate
        * Fixed groupdict None type error and added bound and nested template keys support.
    * Fixed ShowVlanSummary
        * Made "existing_extend_vlans" as optional and added "existing_extend_vtp_vlans" optional key
    * Modified ShowVrrp
        * Fixed parser error for Ipv6 vrrp show command.
    * Modified ShowWirelessFabricClientSummary
        * Removed duplicated class entry
        * Added <l2_vnid> and <rloc_ip> keys as Optional.
        * Added regex pattern <p_client_info_n> to accommodate new version of show command.
        * Added UT covering new version of show commands and new keys
    * Modified ShowVtpStatus
        * fixed genie.metaparser.util.exceptions.SchemaMissingKeyError Missing keys [['vtp', 'pruning_mode']]
    * Modified ShowNat64Translations
        * Added new show cli 'show nat64 translations vrf {vrf_name}'
    * Modified ShowNat64Statistics
        * Added regexp to match vrf and vrf name
    * Modified ShowNat64PrefixStatefulGlobal
        * Added regexp to match vrf and vrf name
    * Modified ShowNat64PrefixStatefulStaticRoutes
        * Added new show cli 'show nat64 prefix stateful static-routes prefix {prefix} vrf {vrf_name}' and regexp to match vrf and vrf name
    * Modified ShowRunInterface
        * Added p87 and p88 for  speed  and speed  nonegotiate under interface  running  configurations.
    * Modified ShowLispIpv4ServerDetail
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Modified ShowLispIpv6ServerDetail
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Modified ShowLispV4PublicationPrefix
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Modified ShowLispV6PublicationPrefix
        * Added RDP info as per the output change in latest polaris version.
        * Added Merged Locator info as per the output change in latest polaris version.
    * Added ShowLispIpv4ServerSHD
        * Added new parser for ipv4 registrations for silent-host
    * Added ShowLispIpv6ServerSHD
        * Added new parser for ipv6 registrations for silent-host
    * Modified ShowLispServiceServerDetailInternal
        * Added support for split-line output format for longer ETR addresses
    * Modified ShowLispPublisherSuperParser
        * Added support for new state string No ETR MS
    * Modified ShowLispPublicationPrefixSuperParser
        * Added support for split-line output format for longer publisher addresses
    * Modified ShowLispSiteDetailSuperParser
        * Added support for split-line output format for longer ETR addresses
    * Modified ShowPlatform
        * added show platform software fed {switch} active vt counter
        * show platform software fed switch active vt all
    * Added ShowPlatformSoftwareFedSwitchActiveMatmAdjacencies
        * added show platform software fed switch active matm adjacencies

* iosxr
    * Modified ShowOspfNeighbor
        * Modified up_time as Optional parameter in schema.

* common
    * Refactor parser loading, deprecate entrypoint callable function
    * Add support for multiple parser packages via environment variable `PYATS_LIBS_EXTERNAL_PARSER` using comma separated syntax.

* nxos
    * Modified ShowBgpL2vpnevpnSummary
        * Updated regex to support ipv6 neighbors
    * Modified ShowNveInterfaceDetail
        * Added regex pattern to support ipv6


--------------------------------------------------------------------------------
                                      Add
--------------------------------------------------------------------------------

* iosxe
    * Added
        * show idprom tan switch {switch_num}
        * show idprom tan switch all


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added ShowIpVerifySource Parser
        * Parser for "show ip verify source interface"
        * Parser for "show ip verify source"
    * Added ShowPlatformHardwareFedSwitchActiveQosDscpCosCountersInterface
        * show platform hardware fed switch active qos dscp-cos counters interface {interface}
    * Added ShowPlatformSoftwareFedActiveMonitor Parser
        * Parser for "show platform software fed active monitor {session}"
    * Added ShowPlatformSoftwareFedSwitchActiveMonitor Parser
        * Parser for "show platform software fed switch active monitor {session}"
    * Added ShowRedundancyLinecardAll
        * show redundancy linecard all
    * Added ShowTemplateInterfaceBindingTarget
        * show template interface binding target {interface}
    * Added ShowPlatformSoftwareFedActiveVtIfId
        * show platform software fed active vt if-id {if_id}
    * Added ShowWirelessMulticast
        * show wireless multicast
    * Added showIpv6MldSnooping
        * show ipv6 mld snooping
    * Added ShowIpcefExactRoute
        * show ip cef exact-route {source} {destination}
    * Added ShowPmPortInterface parser
        * adding ShowPmPortInterface parser
    * Modified ShowLoggingOnboardSwitchClilog
        * show logging onboard switch {switch} clilog
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Added 'interface_template', 'device_type' and 'device_name' keys support to super parser
    * Modified ShowHwModuleUsbflash1Security
        * show hw-module usbflash1 switch {switch_num} security status

* iosxr
    * Added ShowCdpInterface
        * Added parser for show cdp interface
        * Added parser for show cdp interface {interface}

* showplatformifmmapping
    * iosxe
        * Changed switch key from dynamic to static
    * c9500
        * Changed switch key from dynamic to static