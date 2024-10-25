October 2024
==========

October 29 - Genie v24.10
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v24.10
    ``genie.libs.health``, v24.10
    ``genie.libs.clean``, v24.10
    ``genie.libs.conf``, v24.10
    ``genie.libs.filetransferutils``, v24.10
    ``genie.libs.ops``, v24.10
    ``genie.libs.parser``, v24.10
    ``genie.libs.robot``, v24.10
    ``genie.libs.sdk``, v24.10
    ``genie.telemetry``, v24.10
    ``genie.trafficgen``, v24.10




Changelogs
^^^^^^^^^^

genie
"""""

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean-pkg
    * iosxe
        * image_handler
            * Update clean schema to handle smu images
        * Added new clean stages `install_smu`, `install_remove_smu`


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean
    * Modified recovery_worker
        * Changed to use `device_rommon_boot` for TFTP booting
    * Modified device_rommon_boot
        * Changed it to try and use TFTP_BOOT environment variable if TFTP path is too long



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added
        * Segment Routing MPLS Support


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ChangeBootVariable
        * Modified verify_boot_variable to verify next reload boot variables using running image if current_running_image is True



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

* iosxe
    * Added configure_ppp_multilink
        * added api to configure ppp multilink
    * Added unconfigure_ppp_multilink
        * added api to unconfigure ppp multilink
    * Added configure_spanning_tree_portfast under c9500
        * New API to configures spanning-tree portfast under c9500
    * Added unconfigure_spanning_tree_portfast under c9500
        * New API to unconfigures spanning-tree portfast under c9500
    * Added unconfigure_spanning_tree_portfast under c9610
        * New API to unconfigures spanning-tree portfast under c9610
    * Added configure_key_config_key_newpass_oldpass
        * API to change the master key password
    * Added unconfigure_port_channel
        * API to clear port-channel configuration
    * Added new API to get interface traffic counters
        * get_interface_traffic_counters
    * Added API's to configure cli commands for QoS feature.
        * API to configure_ip_access_list_with_dscp_on_device
        * API to configure_class_map_access_group_on_device
        * API to configure_service_policy_type_queueing_on_interface
        * API to configure_traffic_class_for_class_map
    * Added configure_aaa_authorization_config_commands
        * API for configure aaa authorization config-commands
    * Added configure_aaa_accounting_connection_default_start_stop_group_tacacs_group
        * API for configure aaa accounting connection default start-stop group tacacs+ group {server_group_name}
    * Added configure_aaa_accounting_system_default_start_stop_group_tacacs_group
        * API for configure aaa accounting system default start-stop group tacacs+ group {server_group_name}
    * Added clear_ip_dhcp_snooping_track_server
        * API for clear ip dhcp snooping track server
    * Added execute_monitor_capture_limit_duration
        * Execute monitor_capture_limit_duration
    * Added execute_monitor_capture_access_list
        * Execute monitor_capture_access_list
    * Added execute_monitor_capture_vlan_in_match_any
        * Execute monitor_capture_vlan_in_match_any
    * Added configure_bgp_l2vpn_route_reflector_client
    * Added configure_bgp_l2vpn_route_map
    * Added configure_vlan_service_instance_bd_association
    * Added unconfigure_vlan_service_instance_bd_association
    * Added configure_evpn_profile,unconfigure_evpn_profile
    * Added configure_evpn_l2_profile_bd_association
    * Added unconfigure_evpn_l2_profile_bd_association
    * Added configure_evpn_l3_instance_bd_association
    * Added configure_ospf_network_broadcast
    * Added configure_ospf_priority
    * Added clear_monitor_capture
        * API for "monitor capture {capture_name} clear" command
    * Added configure_interface_rep_stcn_segment
        * rep stcn segment 1
    * Added unconfigure_interface_rep_stcn_segment
        * no rep stcn segment 1
    * Added configure_interface_rep_stcn_stp
        * rep stcn stp
    * Added unconfigure_interface_rep_stcn_stp
        * no rep stcn stp
    * Added configure_rep_segment_edge_preferred
        * rep segment 1 edge preferred
    * Added unconfigure_rep_segment_edge_preferred
        * no rep segment 1 edge preferred
    * Added configure_rep_segment_edge_primary
        * rep segment 1 edge primary
    * Added unconfigure_interface_rep_segment_edge_primary
        * no rep segment 1 edge primary
    * Added configure_rep_ztp
        * rep ztp
    * Added unconfigure_rep_ztp
        * no rep ztp
    * Added API test_platform_software_fed_switch_phy_options
        * Added API to test platform software fed switch active phy options
    * Added configure_parser_view under c8000v
        * New API to configure a parser view under c8000v
    * Added unconfigure_parser_view under c8000v
        * New API to unconfigure a parser view under c8000v
    * Added API execute_test_fru_fake_insert
        * Added execute_test_fru_fake_insert
    * Added configure_snmp_server_host under c8000v
        * New API to configure snmp-server host  under c8000v
    * Added unconfigure_snmp_server_host under c8000v
        * New API to unconfigures snmp_server host under c8000v


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified `check_memory_leaks` processor
        * changed to processor.passed/failed
    * added `execute_reload`  processor
        * new processor to reload the device
    * _condition_validator in Blitz
        * Fixed debug message
    * Modified configure_redistribute_connected to add route_map
    * Modified configure_bgp_router_id_peergroup_neighbor to add listen_range and peer_group
    * Fixed configure_evpn_instance_evi , default-gateway has to be appended with enable
    * Added eth_tag to configure_evpn_l2_instance_bd_association
    * Modified configure_route_map_permit to add match_interface
    * Updated default argument trunk as True
        * added trunk default argument in configure_rep_segment

* nxos
    * Added MPLS SR Support in conf model of interface,ospf & bgp
    * Added BGP PIC Support in conf of BGP



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveifmMappingsgid parser
        * Added parser for cli show platform software fed switch {switch} ifm mappings gid {gid_num}
    * Added ShowPlatsoftwaremcumanager
        * Added 'show platform software mcu switch {switch_num} R0 manager 0' command and schema.
    * Add ShowL2vpnEvpnAllActiveMh
        * There is a keyword change in show commands. So added new parser with the keyword change but rest of the content is same.
        * show l2vpn evpn esi-mlag summary has changed to show l2vpn evpn all-active-mh summary
        * show l2vpn evpn esi-mlag vlan brief has changed to show l2vpn evpn all-active-mh vlan brief
        * show l2vpn evpn esi-mlag mac ip deleted has changed to show l2vpn evpn all-active-mh mac ip
    * Added ShowPlatformHardwareFedSwitchStandbyVlanIngress
        * parser for show platform hardware fed switch standby vlan ingress
    * Added howPlatformHardwareFedSwitchActiveVlanIngress
        * parser for 'show platform hardware fed switch active vlan {num} ingress'
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedSisfStatistics parser.
        * Added parser for CLI `show platform software fed switch active security-fed sisf statistics`.
    * Added ShowPlatformHardwareFedSwitchActiveSgaclResourceUsage parser.
        * Added parser for CLI `show platform hardware fed switch active sgacl resource usage`.
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL3unexthop
        * show platform hardware fed switch {switch} fwd-asic insight l3u_nexthop {nh_gid}
    * Added ShowLoggingProcess parser
        * Added parser for cli show Logging Process
    * Added  ShowPlatformsoftwareFedActiveXcvrLpnLinkstatusSchema
        * Added parser for show platform software fed {switch} {mode} xcvr lpn {lpn_value} link_status
    * Added ShowPlatsoftwaremcuversionSchema
        * Added parser for show platform software mcu  switch  {switch_num} R0 version  0
    * Added ShowPlatsoftwaremcusubordinateSchema
        * Added parser for show platform software mcu  switch  {switch_num} R0 version  0
    * Added ShowPlatformfrontendcontroller parser
        * Added parser for cli show Platform Frontend Controller
    * Added ShowControllersEthernetControllerPortInfoSchema
        * Added parser for show controllers ethernet-controller tenGigabitEthernet {interface} port-info
    * Modified ShowDeviceTrackingDatabase
        * show device-tracking database address {address}
    * Added ShowAccessSessionMacDetails parser.
        * Added parser for cli 'show access-session mac {mac} details {rp_slot}'.
    * Added ShowIpDhcpSnoopingTrackServer
        * Added schema and parser for show ip dhcp snooping track server


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIsisNeighborsDetail
        * Added <algo> into schema as Optional
        * Added regex pattern <p22a> to accommodate recent changes.
    * Modified ShowPimNeighbor
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowIpRpf
        * Updated regex pattern <p5> to accommodate various outputs.
    * Modified ShowRepTopologySegment
        * Changed <edge> from schema to Optional.
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowLogging
        * Added optional keys <authentication>, <encryption> in schema.
        * Updated regex pattern <p12> to accommodate various outputs.
    * Modified fix for ShowCryptoSessionSuper
        * Modified the regex patterns <p8>, <p12> and <p18> to accommodate various outputs.
    * Modified fix for ShowLispSiteDetailSuperParser
        * Modified the regex patterns <p4>, <p5> and <p17> to accommodate various outputs.
    * Modified fix for ShowPlatformFedActiveTcamUtilization under c9600
        * Added a regex p4 to match additional output from the show command.
    * Modified ShowIpMulticast
        * Added <algorithm> key to schema as Optional.
        * Updated regex pattern <p2> to accommodate various outputs.
    * Modified ShowCryptoIpsecProfile
        * Updated regex pattern <p1> and <p8> to accommodate various outputs.
    * Modified ShowLispPublicationPrefixSuperParser
        * Changed rdp_len in schema from int to str.
        * Fixed incorrect regex for parsing domain_id and multihoming_id.
        * Added support for merged rloc programming verification (new field 'selected').
    * Modified ShowLispSiteDetailSuperParser
        * Made regex for parsing rdp more restrictive.
    * Modified fix for ShowRplRoutePolicy
        * Updated logic to track NTP peer synchronization state and update overall clock state based on synchronized peers.
    * Modified ShowLispExtranet
        * Updated regex to parse 'Config-Propagation' as source
    * Modified ShowLispDatabaseSuperParser
        * Add support for parsing 'dbmap_src'
        * Add support for parsing 'publish_mode'
    * Modified ShowLispPublicationPrefixSuperParser
        * Add support for parsing 'publish_mode'
    * Modified ShowLispSiteDetailSuperParser
        * Add support for parsing 'publish_mode'
    * Modified ShowLispMapCacheSuperParser
        * Fix regex to parse 'up, self' for locator
    * Modified ShowInstallSummary
        * added fields 'location', 'Switch 1 2', 'auto_abort_timer' in proper place

* common
    * Modified _fuzzy_search_command
        * Made a fix to handle when we have an exact match in the tree, but no actual implementation


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowRunningConfigAllClassMap parser.
        * added show running-config all | section class {class_map}
    * Added ShowPlatformSoftwareFedActiveIpUrpf parser under iosxe.
        * added show platform software fed active ip urpf
        * added show platform software fed switch {mode} ip urpf
    * Added ShowInventory parser under c9350.
        * added show inventory
    * Added ShowPlatformHardwareFedQosSchedulerSdkInterface parser under c9610.
        * added show platform hardware fed {mode} qos scheduler sdk interface {interface}
        * added show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface parser under c9610.
        * added show platform hardware fed switch {switch_num} qos queue stats interface {interface}
        * added show platform hardware fed active qos queue stats interface {interface}
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear parser under c9610.
        * added show platform hardware fed active qos queue stats interface {interface} clear
        * added show platform hardware fed switch {switch_num} qos queue stats interface {interface} clear



genie.telemetry
"""""""""""""""
