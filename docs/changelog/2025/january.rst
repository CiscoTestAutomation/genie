January 2025
============

 - Genie v25.1



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.1
    ``genie.libs.health``, v25.1
    ``genie.libs.clean``, v25.1
    ``genie.libs.conf``, v25.1
    ``genie.libs.filetransferutils``, v25.1
    ``genie.libs.ops``, v25.1
    ``genie.libs.parser``, v25.1
    ``genie.libs.robot``, v25.1
    ``genie.libs.sdk``, v25.1
    ``genie.telemetry``, v25.1
    ``genie.trafficgen``, v25.1




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* genie
    * Modified
        * Pinned minimum `netaddr` package version to `0.10.1`.
    * Modified
        * Unpinned `netaddr` package version in setup.py and Makefile
    * Removed `TriggerUnconfigureConfigureOspf` trigger from yaml file
    * Re-enable the syntax warning in Makefile



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ChangeBootVariable
        * Removed duplicate code from verify_boot_variable step

* clean-pkg
    * iosxe
        * set the step as passx if ignore stratup config fail.
    * Fix syntax warning


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* clean-pkg
    * iosxe
        * Remove the unused key `reload_timeout` from `install_smu`
    * iosxe
        * Added hot smu support for `install_remove_smu` and `install_smu` stage
    * iosxe
        * Added multiple smu support for `install_remove_smu` and `install_smu` stage

* iosxe
    * Added
        * ChangeBootVariable for IE3K



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* nxos
    * Fix feature service-acceleration
        * change config line `conn-token` to `connection-token` and update unit tests

* conf-pkg
    * Added new clis in interface and macsec files.
    * Fix syntax warning


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * Added support for feature service-acceleration
        * covers all possible configurations currently supported for feature service-acceleration



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* fileserver
    * Modified _get_ip
        * For newer version of `netaddr`, passing INET_ATON argument IPAddress to allow all kinds of weird-looking addresses to be parsed

* filetransferutils-pkg
    * Fix syntax warning



genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* health-pkg
    * Fix syntax warning



genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* ops-pkg
    * Fix syntax warning



genie.libs.robot
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* robot-pkg
    * Fix syntax warning



genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added configure_nat64_mapt_domain
        * API to configure nat64 mapt domain
    * Added unconfigure_nat64_mapt_domain
        * API to unconfigure nat64 mapt domain
    * Added configure_nat64_route
        * API to configure nat64 route
    * Added configure_nat64_mapt_ce
        * API to configure nat64 mapt ce
    * Added configure_nat_service_all_algs
        * API to configure nat service all algs
    * Added configure_nat_setting_gatekeeper_size
        * API to configure nat setting gatekeeper size
    * Added API request_platform_software_trace_archive
        * Added API to request_platform_software_trace_archive
    * Added configure_eem_applet_watchdog_time
    * Added configure_eem_action_cli_command
    * Added configure_eem_action_syslog_msg
    * Added configure_eem_action_wait
    * Added configure_eem_action_info_type_routername
    * Added configure_bgp_route_reflector_client
    * Added configure_fall_over_bfd_on_bgp_neighbor
    * Added unconfigure_interface_evpn_ethernet_segment
    * Added configure_l2vpn_evpn_ethernet_segment_all_active
    * Added api for clear_platform_software_fed_switch_active_access_security_table_counters
        * Added new api clear platform software fed switch active access-security table counters.
    * Added api for clear_platform_software_fed_switch_active_access_security_auth_acl_counters
        * Added new api clear platform software fed switch active access-security auth-acl counters .
    * Added configure_macro_auto_execute
        * API to configure macro auto template
    * Added unconfigure_macro_auto_execute
        * API to unconfigure macro auto template
    * Added configure_shell_trigger
        * API to configure shell trigger
    * Added unconfigure_shell_trigger
        * API to unconfigure shell trigger
    * Added configure_macro_auto_trigger
        * API to configure macro auto trigger
    * Added unconfigure_macro_auto_trigger
        * API to unconfigure macro auto trigger
    * Added configure_macro_auto_fallback
        * API to configure macro auto global processing {fallback} {parameters}
    * Added unconfigure_macro_auto_fallback
        * API to unconfigure macro auto global processing {fallback} {parameters}
    * Added Async specific APIs for line
        * configure_line for applying  configurations on line.
        * configure_line_raw_socket_tcp_client for raw socket client on line.
        * configure_line_raw_socket_tcp_server for raw socket server on line.
        * unconfigure_line for removing raw line configurations.
        * unconfigure_line_raw_socket_tcp_client for removing raw socket client on line.
        * unconfigure_line_raw_socket_tcp_server for removing raw socket server on line.
    * Added configure_radius_group_load_balance_method
    * Added configure_aaa_authorization_exec
    * Added unconfigure_aaa_authorization_exec
    * Added configure_aaa_authorization_console
    * Added unconfigure_aaa_authorization_console
    * Added configure_aaa_accounting_exec_default_start_stop
    * Added unconfigure_aaa_accounting_exec_default_start_stop
    * Added enable_ssh_on_vty
    * Added disable_ssh_on_vty
    * Added configure_login_authentication_on_vty
    * Added configure_authorization_exec_on_vty
    * Added unconfigure_login_authentication_on_vty
    * Added unconfigure_authorization_exec_on_vty
    * Added configure_aaa_authentication_enable_none
    * Added configure_ipv6_flow_monitor_sampler
        * added api to configure ipv6 flow monitor <monitor_name> sampler <sampler_name> input
    * Added configure_macro_auto_device_parameters
        * API to configure macro auto device {device_name} {parameters}
    * Added unconfigure_macro_auto_device_parameters
        * API to unconfigure macro auto device {device_name} {parameters}
    * Added configure_dhcp_option
        * API to configure ip dhcp pool with option
    * Added configure_ip_ddns_update_method
        * API to configure_ip_ddns_update_method
    * Added unconfigure_ip_ddns_update_method
        * API to unconfigure_ip_ddns_update_method
    * Added new API to configure rep ztp on the interface
        * rep ztp-enable
    * Added new API to unconfigure rep ztp on the interface
        * no rep ztp-enable
    * Added API's to configure cli commands for acl.
        * API to configure_protocol_acl_any_any
        * API to unconfigure_protocol_acl_any_any
    * Added locate_switch
        * API to locate switch
    * Added configure_interface_macro_description
        * API to configure macro description on interface
    * Added unconfigure_interface_macro_description
        * API to unconfigure macro description on interface
    * Added configure_macro_auto_mac_address_group
        * API to configure macro auto mac address group
    * Added unconfigure_macro_auto_mac_address_group
        * API to unconfigure macro auto mac address group
    * Added API set_platform_software_ilpower_mcu
        * Added API to set_platform_software_ilpower_mcu
    * Added config_pseudowire_class_interworking
    * cat9k
        * c9300
            * Added API's to configure and unconfigure the ignore startup config
        * c9400
            * Added API's to configure and unconfigure the ignore startup config
        * c9800
            * Added API's to configure and unconfigure the ignore startup config
        * c9500
            * Added API's to configure and unconfigure the ignore startup config
        * c9500
            * C9500-40X
                * Added API's to configure and unconfigure the ignore startup config
    * Added configure_mac_acl_etherType
    * Added configure_routing_ip_route_track
    * Added unconfigure_routing_ip_route_track
    * Added unconfigure_interface_speed_auto
        * API to unconfigure interface speed auto on interface
    * Added configure_ip_dhcp_relay_information_option_insert
        * API to configure_ip_dhcp_relay_information_option_insert
    * Added unconfigure_ip_dhcp_relay_information_option_insert
        * API to unconfigure_ip_dhcp_relay_information_option_insert
    * Added API show_platform_software_mcu_snapshot_detail_request
        * Added API to show_platform_software_mcu_snapshot_detail_request
    * Added Async specific apis for serial interface
        * API configure_interface_serial_physical_layer for configuring physical layer.
        * API unconfigure_interface_serial_physical_layer for unconfiguring physical layer.
        * API configure_interface_serial_encapsulation for configuring encapsulation.
        * API unconfigure_interface_serial_encapsulation for unconfiguring encapsulation.
        * API configure_interface_raw_socket_client for raw socket configuration.
        * API unconfigure_interface_raw_socket_client for raw socket unconfiguration.
    * Added
        * API for ip host <hostname> <ip_addr> (configure and unconfigure)
        * API for ip dns server (configure and unconfigure)


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_macro_auto_trigger
        * Modified api to configure trigger based on parameter passed
    * Modified configure_policy_map priority percent
    * Modified
        * Updated configure_monitor_capture API with additional arguments
    * Removed default argument trunk as True
    * Removed the configure_interface_rep_segment_edge_primary api from interface/configure.py and modified configure_rep_segment, configure_fast_rep_segment
    * Removed the unconfigure_interface_rep_segment_edge_primary api from interface/configure.py and modified unconfigure_rep_segment, unconfigure_fast_rep_segment
    * Modified configure_tacacs_server
        * Modified the api to configure tacacs server and use hostname instead of ip address as host
    * Updated configure_replace API, add hostname learning to detect hostname changes
    * Modified configure_interface_speed_auto
    * health/cpu
        * add handeling for InvalidCommandError

* genielibs
    * Removed `TriggerUnconfigureConfigureOspf` trigger from yaml file

* junos
    * Modified verify_ospf_interface_in_database
        * For newer version of `netaddr`, passing INET_ATON argument IPAddress to allow all kinds of weird-looking addresses to be parsed

* utils
    * Modified netmask_to_bits
        * For newer version of `netaddr`, passing INET_ATON argument IPAddress to allow all kinds of weird-looking addresses to be parsed
    * copy to device
        * Fixed the logic for proxy dev to check for proxy in servers
    * copy_to_device
        * add support for dual rp devices for http copy using proxy
    * copy to device
        * fix the logic for proxy dev to check for proxy in servers
    * copy to device
        * update the unittest for copy to device using proxy

* sdk/blitz
    * Change pyATS Health check logging to debug level

* health
    * Change pyATS Health check logging to debug level

* sdk
    * Made code 3.13 compliant

* sdk-pkg
    * Fix syntax warning


--------------------------------------------------------------------------------
                                      Add
--------------------------------------------------------------------------------

* sdk-pkg
    * Add support for stack device password recovery



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Fixed parser ShowLoggingOnboardSwitchActiveUptimeDetail
        * Added p12, and p13 to match the uptime and uptime detail
    * Modified ShowPolicyMapInterface
        * Modified ShowPolicyMapTypeSuperParser p1 regex to match port channel subinterfaces.
    * Modified ShowControllerEthernetControllerLinkstatus
        * added optional reason key in schema and corresponding regexp for the same.
        * Deleted the  duplicate  copy of ShowControllerEthernetControllerLinkstatus.
    * Modified ShowL2tpTunnel
        * Fixed incorrect regex for parsing.
    * Modified ShowProcessesCpuPlatformSorted
        * Made <sort> key as optional in the schema to accommodate various outputs.
    * Modified ShowMacroAutoDevice
        * added optional device_name argument to return device specific output.
    * Modified ShowMacroAutoInterface
        * added optional interface argument to return interface specific output.
    * Added ShowDeviceTrackingDatabaseDetails parser
        * Modified parser for cli show device-tracking database interface {interface_name} details
        * Modified parser for cli show device-tracking database vlan {vlan_id} details
    * Modified ShowLicenseTechSupport
        * Modified regex (p0_3) to match the correct key when muliple colons are present (key should not contain colon)
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail parser.
        * Enhanced parser for cli 'show platform software fed {switch} {mode} acl info db detail'.
        * Enhanced parser for cli 'show platform software fed {mode} acl info db detail'.
        * Enhanced parser for cli 'show platform software fed switch {mode} acl info db feature {feature_name} detail'.
        * Enhanced parser for cli show platform software fed switch {switch_var} acl info db feature {feature_name} dir {in_out} cgid {cg_id} detail.
    * Modified ShowTelemetryInternalProtocolManager
        * Fix regex so that it accepts -1 for sockfd field
    * Added ShowIpNbarDiscovery
        * Added <Vlan> interface to support new output
    * Modified ShowAAServersSchema
        * Changed <requests_per_minute_past_24_hours> from schema to Optional.
    * Modified HardwareModuleBeaconSlotStatus
        * Modified p1 regex to match the correct output
        * Added "hw-module beacon RP {supervisor} status"
    * Fix ShowPlatformTcamUtilization.
        * Added "asic" optional variable to all tcam show commands under 9350, 9500, 9606 and 9600 platforms.
    * Fixed parser ShowSwitchStackPortSummary
        * Fixed regex pattern p1 to match "no cable"
    * Fixed parser ShowPppAll
        * Fixed regex pattern p1 'peername' to match "Charon-037-4P"
    * Fixed parser ShowIssuRollbackTimer
        * Added schema, regex p0 to match the slot
    * Modified ShowVersion
        * Made change for <p3> regex
    * Modified ShowSystemIntegrityAllMeasurementNonce
        * Made <PCR0> key as optional to pick the latest output
    * Modified ShowLispPublicationPrefixSuperParser
        * Changed metric in schema from int to str.
        * Fixed incorrect regex for parsing metric.
    * Modified ShowBgpAllDetail
    * Modified ShowIpBgpL2VPNEVPN
    * Modified ShowPlatformHardwareFedSwitchQosQueueConfigInterfaceQueueInclude
        * modified the op as blocked changed to byte in output.
    * Modified fix for ShowPlatformSoftwareFedSwitchActiveIpRoute
        * Added sgt keys in schema for show platform software fed switch {mode} ip route .
        * Added cli show platform software fed switch {mode} ip route vrf {vrf_name}.

* genieparer
    * Modified
        * Unpinned `netaddr` package version in Makefile
        * Updated parsers to pass INET_ATON argument to IPAddress to allow all kinds of weird-looking addresses to be parsed

* iosxr
    * Modified ShowRouting
        * Added support for new optional variables via_class,weight,via_interface,via_flags.
        * Modified regex pattern to support above variables.

* nxos
    * Modified ShowForwardingDistributionMulticastRoute
        * Updated <gaddr> key as option in schema to match new output.
    * Fixed parser ShowIpv6InterfaceVrfAll
        * Fixed regex Pattern to match and additional attribut RFC compliant in urser's output
    * Modified ShowBfdNeighbor
        * Changed <p8> regex to match new output.
    * Modified ShowInterfaceCounters
        * Added Optional <in_pkts>, <out_pkts> in schema.
        * Updated regex pattern <p1> to accommodate new nxos output for S1 G200 sub interface stats.

* nsos
    * Enhanced parser ShowModule
        * Enhanced the parser for the cli 'show module' to parse new SAM (Service Accelerator Module)
    * Modified parser ShowInventory
        * Enhanced the parser for the cli 'show inventory' to parse new SAM (Service Accelerator Module)

* genie.libs.parser
    * Fix syntax warnings across all os

* added optional multipath arguement to return multipath for specific output.

* added optional multipath arguement to return multipath for specific output.


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIpv4SgtMapping parser.
        * Added parser for CLI `show platform hardware fed switch {switch_var} fwd-asic insight ipv4_sgt_mapping({devid})`.
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIpv6SgtMapping parser.
        * Added parser for CLI `show platform hardware fed switch {switch_var} fwd-asic insight ipv6_sgt_mapping({devid})`.
    * Added ShowPlatformNatTranslationsStandby parser.
        * Added parser for CLI 'show platform nat translations standby'.
    * Added ShowPlatformNatTranslationsStandbyStatistics parser.
        * Added parser for CLI 'show platform nat translations standby statistics'.
    * Added ShowPlatformHardwareFedSwitchQosQueueConfig
        * Added parser "show platform hardware fed active qos queue config interface {interface}" under c9350, c9610, c9500
    * Added schema and parser for
        * 'show authentication sessions session-id {session_id} policy',
        * 'show authentication sessions session-id {session_id} switch active R0',
        * 'show authentication sessions session-id {session_id} details'
    * Added ShowPreemptionSummary.
        * Added parser for CLI 'show preemption summary'.
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandErspan parser.
        * Added parser for cli show platform hardware fed switch active fwd-asic insight l2_mirror_command_erspan({mirror_gid}).
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandStatus parser.
        * Added parser for cli show platform hardware fed switch active fwd-asic insight l2_mirror_command_status.
    * Added ShowIpPimVrfMdtSendSchema parser
        * Added schema and parser for cli 'show ip pim vrf {vrf_name} mdt send'
    * Added ShowControllersPowerInline
        * Added schema and parser for show controllers power inline
    * Added ShowIpDhcpPool Parser in show_ip.py
        * show ip dhcp pool
    * Added ShowHardwareLedState schema and parser
        * Added schema and parser for show hardware led state
    * Added ShowPlatformSoftwareCpmSwitchActiveB0PacketsControlIpc
        * Added parser ShowPlatformSoftwareCpmSwitchActiveB0PacketsControlIpc
    * Added schema and parser for cli
        * 'show access-session session-id {session_id} details',
        * 'show access-session session-id {session_id} policy',
        * 'show access-session session-id {session_id} switch {mode} {rp_slot}''
    * Added ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocolsSchema
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-port-v6 {sourcemac} {destinationmac}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-v6 {sourcemac} {destinationmac} {flow_label} {next_header}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-port-v4 {source} {destinatio} {protocol} {sour_port} {dest_port}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-v4 {source} {destination} {protocol}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-addr {sourcemac} {destinationmac}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-port-v6 {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-v6 {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}'
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-v4 {sourcemac} {sourceip} {destinationip} {protocol}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-port-v4 {sourcemac} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-port-v6 {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-v6 {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-port-v4 {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-v4 {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol}',
    * Added parser for cli 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlanid {sourcemac} {vlan_id}'.
    * Added  ShowPlatsoftwaremcusnapshot parser
        * Added schema and parser for cli show platform software mcu switch {switch_num} {route-processor} snapshot_detail display
    * Added ShowPlatformSoftwareFedSwitchActiveAclBindSdkDetail parser.
        * Added parser for CLI 'show platform software fed switch {switch_var} acl {acl} sdk detail'.
        * Added parser for CLI 'show platform software fed switch {switch_var} acl {acl} sdk feature {feature_name} dir in cgid {cg_id} detail'.
        * Added parser for CLI 'show platform software fed switch {switch_var} acl {acl} sdk feature {feature_name} dir in detail asic {asic_no}'.
        * Added parser for CLI 'show platform software fed switch {switch_var} acl {acl} sdk feature {feature_name} detail'.
        * Added parser for CLI 'show platform software fed switch {switch_var} acl {acl} sdk if-id {if_id} detail'.
    * Added ShowPlatformSoftwareFedSwitchActiveAclBindSdkfeatureCgaclDetail parser.
        * Added parser for CLI 'show platform software fed switch active acl bind sdk feature cgacl detail'.
    * Added support for parsing the 'show authentication sessions mac 001a.a136.c68a details',
    * Added ShowFlowMonitorS1InputCacheFilter
        * Added schema and parser for 'show flow monitor {name} cache filter {ip_version} source address {src_addr} {ip_version} destination address {dst_addr} format table'
    * Added  parser for ShowMacroAutoAddressgroup
        * Added parser for cli "show macro auto address-group {address_group_name}"
    * Added ShowSampler.
        * Added parser for CLI 'show sampler <sampler>'.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedSisfIfId parser.
        * Added parser for cli show platform software fed switch {switch} security-fed sisf if-id {if_id}.
    * Added ShowPlatformSoftwareFedSwitchSecurityFedSisfVlan parser.
        * Added parser for cli show platform software fed switch {switch} security-fed sisf vlan {vlan}.
    * Added ShowPlatformHardwareFedNpuDscDump parser
        * Added schema and parser for cli show platform hardware fed switch {mode} npu slot 1  port {port_num} dsc_dump
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV4 parser.
        * Added parser for CLI 'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v4({devid})'.
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SgtMappingStatusV6 parser.
        * Added parser for CLI 'show platform hardware fed switch {switch} fwd-asic insight s1_sgt_mapping_status_v6({devid})'.
    * Added ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureBriefCount parser.
        * Added parser for cli 'show platform software fed {switch} {switch_number} punt packet-capture brief | count {key}'.
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObjects parser.
        * Added parser for cli show platform hardware fed switch active fwd-asic insight sdk_objects{('otype')}.
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSdkObject parser.
        * Added parser for cli show platform hardware fed switch active fwd-asic insight sdk_object{('otype')}.
    * Added ShowL2vpnEvpnMultihomingVlan
        * show l2vpn evpn multihoming vlan
    * Added class ShowPlatformSoftwareFedSwitchActiveSgaclDetail
        * show platform software fed switch {switch_type} sgacl detail .
    * Added class ShowPlatformSoftwareFedSwitchActiveSgaclPort
        * show platform software fed switch {switch_type} sgacl port.
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityDhcpStatistics
        * show platform software fed switch {switch_type} security dhcp statistics
    * Added ShowPlatformSoftwareFedSwitchSecurityFedDhcpVlandetail
        * show platform software fed switch {switch_type} security-fed dhcp vlan {vlan_num} detail
    * Added ShowPlatformHardwareFedeyescan parser
        * Added parser for cli show platform Hardware Fed Eyescan
    * Added ShowPlatoformSoftwareFedSwitchActiveInsightNplTable parser
        * Added parser for cli sh platform hard fed switch {switch_type} fwd-asic insight npl_table{table_name}
    * Added ShowPlatformSoftwareFedSwitchActiveAclSgaclResourceUsageSchema parser
        * Added parser for cli show platform software fed switch {switch_type} acl sgacl resource usage
    * Added ShowPlatformSoftwareFedSwitchActiveIfmMappingsGpn.
        * Added parser for CLI 'show platform software fed switch active ifm mappings gpn'.
        * Added an example of a string that would match to the regular expression.
        * Added required comments in the file.
        * Added parser for CLI 'show platform software fed switch active ifm mappings gpn'.
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicResourceTcamTableSghash parser.
        * Added parser for cli 'show platform hardware fed switch {switch_var} fwd-asic resource tcam table sghash all'.
        * Added parser for cli 'show platform hardware fed switch {switch_var} fwd-asic resource tcam table sghash asic_no {asic_no}'.
        * Added parser for cli 'show platform hardware fed switch {switch_var} fwd-asic insight sgmatrix({max_asic})'.
    * Added ShowAccessSessionDetails
        * Added schema and parser for 'show access-session interface {interface} details switch {switch_num} R0',
        * Added schema and parser for 'show access-session interface {interface} policy',
        * Added schema and parser for 'show access-session interface {interface} policy switch {mode} R0',
        * Added schema and parser for 'show access-session database interface {interface} details',
        * Added schema and parser for 'show access-session database interface {interface} policy',
        * Added schema and parser for 'show access-session database interface {interface} policy switch {mode} R0',
        * Added schema and parser for 'show access-session database interface {interface} switch {switch_num} R0'
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SecGroupsMatrixMapStatus parser.
        * Added parser for cli "show platform hardware fed switch {switch} fwd-asic insight s1_sec_groups_matrix_map_status({devid})".
    * Added ShowIpDhcpSnooping parser.
        * Added parser for cli 'show ip dhcp snooping'.
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedArpStatistics parser.
        * Added parser for cli show platform software fed switch active security-fed arp statistics.
    * Added ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage parser.
        * Added parser for cli show platform software fed switch active access-security table usage.
    * Added schema and parser for 'show authentication sessions switch {switch} R0', \
    * Added ShowIpVrfMdtReceiveDetail parser
        * Added schema and parser for cli 'show ip pim vrf {vrf_name} mdt receive detail'
    * Added Parser for ShowPlatSoftFedSwAcAccessSecurityClientTableMac
        * show platform software fed switch active access-security mac-client-table summary
        * show platform software fed switch active access-security mac-client-table interface if-id {port_if_id}
    * Added ShowIpSourceBinding parser.
        * Added parser for cli
    * Added ShowPlatformSoftwareFedSwitchSecurityFedIpsgIfId parser.
        * Added parser for cli 'show platform software fed switch {switch} security-fed ipsg if-id {if_id}'.
    * Added ShowIpPimVrfMdtHistoryInterval parser
        * Added schema and parser for cli 'show ip pim vrf {vrf_name} mdt history interval {interval}'
    * Added support for parsing the 'show authentication sessions interface {interface} details',
    * Added support for parsing the 'show authentication sessions interface {interface} policy',
    * Added support for parsing the 'show authentication sessions interface {interface} details switch {switch} R0',
    * Added support for parsing the 'show authentication sessions interface {interface} policy switch {switch} R0',
    * Added support for parsing the 'show authentication sessions database interface {interface} details',
    * Added support for parsing the 'show authentication sessions database interface {interface} policy',
    * Added support for parsing the 'show authentication sessions database interface {interface} policy switch {switch} R0',
    * Added  parser for ShowPlatformSoftwareFedSwitchActiveIfmInterfacesDetail
        * Added pattern as a comment for regex
    * Added ShowRawSocketTcpSessions
        * Added schema and parser for show raw-socket tcp sessions
        * Added schema and parser for show raw-socket tcp statistic
    * Added ShowPlatformSoftwareFedSwitchActiveIfmMappings
        * show platform software fed switch active ifm mappings l2-attachment-circuit
        * show platform software fed switch active ifm mappings l3-attachment-circuit
        * show platform software fed switch active ifm mappings system-port
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardDef parser.
        * Added parser for cli 'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_def',
        * Added parser for cli'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_def()',
        * Added parser for cli'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_def({devid})'.
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAcl parser.
        * Added parser for cli'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl',
        * Added parser for cli'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl()',
        * Added parser for cli'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl({devid})'.
    * Added ShowControllersEthernetControllerPreemptionDrops.
        * Added parser for CLI 'show controllers ethernet-controller <intf> preemption drops'.
    * Added ShowControllersEthernetControllerPreemptionHandshake.
        * Added parser for CLI 'show controllers ethernet-controller <intf> preemption handshake'.
    * Added ShowControllersEthernetControllerPreemptionStats.
        * Added parser for CLI 'show controllers ethernet-controller <intf>> preemption stats    '.
    * Added ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableSummary parser.
        * Added parser for cli show platform software fed switch active access-security table summary.
        * Added parser for cli show platform software fed switch active access-security table mac {mac_id}.
        * Added parser for cli show platform software fed switch active access-security table interface if-id {if_id}
    * Added ShowPlatformSoftwareFedSwitchActiveIpv6Route parser.
        * Added parser for cli show platform software fed switch {mode} ipv6 route.
    * Added parser for cli show platform software fed switch {mode} ipv6 route vrf {vrf_name}.
    * Added ShowAuthenticationSessionMethodDetails parser.
        * Added schema and parser for 'show access-session mac {mac} interface {interface} details'
        * Added schema and parser for 'show access-session mac {mac} method {method} details'
        * Added schema and parser for 'show access-session mac {mac} method {method} details switch {mode} {rp_slot}'
        * Added schema and parser for 'show access-session mac {mac} policy'

* utils
    * Add a new api to find duplicates in the AbstractTree passed to function.
    * unittest

* 'show authentication sessions mac 001a.a136.c68a interface gigabitethernet2/0/3 details',

* 'show authentication sessions mac 001a.a136.c68a method dot1x details',

* 'show authentication sessions mac 001a.a136.c68a method dot1x details switch active r0',

* 'show authentication sessions mac 001a.a136.c68a  policy'.

* nxos
    * added new parser ShowInterfaceCountersErrors
        * Added new parser for the cli "show interface counters errors"
    * added new parser ShowInterfaceSnmpIfIndex
        * added new parser for the cli "show interface  snmp-ifindex"
    * Added ShowBfdNeighbor
        * show bfd neighbor
    * Added ShowBfdNeighborDetail
        * show bfd neighbor detail
    * rv1
        * Added  ShowIpIgmpSnooping
            * Added schema and parser for 'show ip igmp snooping'

* show platform software fed switch active access-security mac-client-table mac {client_mac}



genie.telemetry
"""""""""""""""
