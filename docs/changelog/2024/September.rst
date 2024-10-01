September 2024
==========

September 24 - Genie v24.9 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v24.9 
    ``genie.libs.health``, v24.9 
    ``genie.libs.clean``, v24.9 
    ``genie.libs.conf``, v24.9 
    ``genie.libs.filetransferutils``, v24.9 
    ``genie.libs.ops``, v24.9 
    ``genie.libs.parser``, v24.9 
    ``genie.libs.robot``, v24.9 
    ``genie.libs.sdk``, v24.9 
    ``genie.telemetry``, v24.9 
    ``genie.trafficgen``, v24.9 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* conf
    * base
        * add handling for hierarchical clean args


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* abstraction
    * Enabled use of origin token in external packages

* genie.ops
    * Modified Maker class to pass parser kwargs
        * Allows parsers with `command` argument to be used with Genie Ops



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean
    * Modified iosxe.stage.Connect.connect
        * Set learn hostname to False after hostname learned
    * Modified tftp_device_recovery
        * If username and password are not provided, use default username and password

* utils
    * Modified validate_clean to not raise any exceptions on passing image_management to clean yaml file


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified
        * Allowing a config_register option in RommonBoot stage, with a default of 0x0
    * Added
        * Added support for quad sup devices in clean to connect the active and standby
    * Modified Clean Connect
        * Added check for console speed being incorrect as well as a fix



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added lldp conf model

* nxos
    * Added lldp conf model

* device
    * Add learn_interfaces to device object
        * use the learn(interface) ops to find all the interfaces and add them to device.interfaces



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * check the version for validate_and_update_url since the behaviour changed from 7.x.x.x version



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * added a new brief argument to the interface model
    * asr1k
        * added kwargs to the interface model
    * aat3k
        * added kwargs to the interface model

* nxos
    * added a new brief argument to the interface model

* iosxr
    * added kwargs to the interface model



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_spanning_tree_bridge_assurance
        * API for configure spanning tree bridge assurance
    * Added unconfigure_spanning_tree_bridge_assurance
        * API for unconfigure spanning tree bridge assurance
    * Added configure_spanning_tree_portfast_bridge_assurance
        * API for configure spanning tree portfast bridge assurance
    * Added unconfigure_spanning_tree_portfast_bridge_assurance
        * API for unconfigure spanning tree portfast bridge assurance
    * Added configure_spanning_tree_portfast_bridge_assurance_on_interface
        * API for configure spanning tree portfast bridge assurance on interface
    * Added unconfigure_spanning_tree_portfast_bridge_assurance_on_interface
        * API for unconfigure spanning tree portfast bridge assurance on interface
    * Added configure_vlan_dot1q_tag_native
        * API to configure vlan dot1q tag native
    * Added unconfigure_vlan_dot1q_tag_native
        * API to unconfigure vlan dot1q tag native
    * Added configure_switchport_trunk_native_vlan_tag
        * API to configure switchport trunk native vlan tag
    * Added configure_auto_off_optics
        * Added configure_auto_off_optics
    * Added unconfigure_auto_off_optics
        * Added unconfigure_auto_off_optics
    * Added test_platform_software_fru_fake_insert_remove
        * New API to execute test platform software fed switch {switch_num} fru {action}
    * Added new API to not set config register value in IOT devices
        * This is done to avoid this setting in clean install of IOT devices.
    * Added configure_medium_p2p_interface
        * Configure medium p2p on interface
    * Added unconfigure_medium_p2p_interface
        * Unconfigure medium p2p on interface
    * Added configure_access_list_extend_with_dst_address_and_port
        * New API to configures access-list extend with destination address and ports on device
    * Added configure_access_list_extend_with_port
        * New API to configures access-list extend with port on device
    * Added configure_access_list_extend_with_dst_address_and_gt_port
        * New API to configures access-list extend with destination address and gt port on device
    * Added configure_access_list_extend_with_range_and_eq_port
        * New API to configures access-list extend with range and eq port on device
    * Added configure_access_list_extend
        * New API to configures access-list extend on device
    * Added configure_ipv6_address_on_hsrp_interface
        * Added configure_ipv6_address_on_hsrp_interface
    * Added configure_spanning_tree_portfast under c9610
        * New API to configures spanning-tree portfast under c9610
    * Added configure_fnf_flow_record_match_flow
        * added api to configure flow record match flow
    * Added configure_ip_sgacl
        * API for configure the ip agacl rules
    * Added unconfigure_ip_sgacl
        * API for unconfigure ip sgacl
    * Added clear_platform_qos_statistics_iif_id
        * added clear platform hardware qos statistics internal cpu policer API
    * Added monitor_capture_start_capture_filter
        * Execute monitor_capture_start_capture_filter
    * Added monitor_capture_file_location_flash
        * Execute monitor_capture_file_location_flash
    * Added monitor_capture_class_map
        * Execute monitor_capture_class_map
    * Added monitor_capture_clear
        * Execute monitor_capture_clear
    * Added unconfigure_aaa_accounting_dot1x_default_start_stop_group
        * New API to unconfigure "no aaa accounting dot1x default start-stop group {server_group_name}"

* added unconfigure_switchport_trunk_native_vlan_tag
    * API to unconfigure switchport trunk native vlan tag

* generic/nxos
    * Added configure_hostname
        * New API to configure hostname on device.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fixed configure_hw_module_switch_number_auto_off_led
        * Changed ecomode to auto-off
    * Fixed unconfigure_hw_module_switch_number_auto_off_led
        * Changed ecomode to auto-off
    * Fixed configure_stack_power_auto_off
        * Changed ecomode to auto-off
    * Fixed unconfigure_stack_power_auto_off
        * Changed ecomode to auto-off
    * Fixed configure_default_stack_power_auto_off
        * Changed ecomode to auto-off
    * Modified API configure_ikev2_profile_pre_share
        * Added local_interface parameter
        * Added logic and command to execute if local_interface parameter is provided
    * Fixed configure_boot_level_licence
        * Added optional agruments advantage and essentials
    * Removed duplicate entry of configure_interface_monitor_session_shutdown_erspan_dest, configure_interface_monitor_session_mtu and configure_interface_monitor_session_no_mtu
    * Modified configure_management_vty_lines API
        * Added stackable check for configure_management_vty_lines API using stackable parameter
    * Fixed configure_ipv6_address_on_hsrp_interface
        * Changed version to groupnumber

* nxos
    * Removed duplicate TriggerAddRemoveBgpNetworkIPv4 trigger from trigger_datafile_nxos.yaml file
    * Removed duplicate iteration attribute under Verify_BgpIpMvpnRouteType_vrf_all_route_type_4 from verification_datafile_nxos.yaml file



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowBgpNeighborsReceivedRoutesSuperParser
        * Make optional to handle regex without CICD
    * Modified ShowInterfaces
        * Added <in_drops>, <out_drops>, <peer_ip> and <vc_id> into schema as Optional.
        * Renamed regex pattern <p_cd>, <p_cd_2> to <p54>, <p55> respectively and updated the code accordingly.
        * Added regex pattern <p1_2>, <p6_1>, <p56>, <p57> and <p58> to accommodate various outputs.
    * Modified ShowIpRouteWord
        * Updated regex pattern <p2> to accommodate various outputs.
    * Modified ShowSdwanOmpSummary
        * Added the new fields in schema to match the output
    * Modified ShowPlatformSoftwareFedSwitchActiveVtAll
        * Added CLI without Switch keyword too in the CLI list.
    * Modified ShowInterfacesTransceiver
        * parser for 'show interfaces transceiver'
    * Modified fix for auto off addition
        * Replaced ecomode with auto-off due to new cli
    * Modified ShowIPVerifySource
        * Fixed regular expressions p1 to match filter_type which is 'ip'
    * Added ShowRepTopologyDetail
        * show rep topology detail
    * Modified ShowMeraki
        * Updated the P2 regex based on the latest output at line number 70.
    * Modified ShowSpanningTreeSummaryTotals
        * Made "portfast_bpdu_guard" and "portfast_bpdu_filter" optional and
    * Modified ShowVersion
        * c9500 Added schema key 'bootldr' to match the schema of the iosxe parser.
    * Modified ShowRedundancyStates
        * Made rf_debug_mask variable as optional and unit test added
    * Modified fix for ShowEthernetTags
        * Updated the interface variable, now uses the correct OS-specific format.when converting the interface name.
    * Modified ShowPolicyMapControlPlaneClassMap parser.
        * added extra regx. for burst_pkt pattern.
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Changed <locators> key from schema to Optional.
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added commands 'show platform software fed {mode} acl info db detail' and 'show platform software fed {switch} {mode} acl info db detail {acl_name}' under iosxe
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added commands 'show platform software fed {mode} acl info db detail' and 'show platform software fed {switch} {mode} acl info db detail {acl_name}' under c9350
        * fixed reg ex p1 for 'show platform software fed {mode} acl info db detail' under c9350
    * Modified ShowMonitor
        * Removed un-necessary cli command from ShowMonitor parser.
    * Modified fix for ShowLispRegistrationHistory
        * Reverted the changes due to the CLI index issue
    * Modified fix for ShowPlatformHardwareFedQosSchedulerSdkInterface
        * Modified 'rate' as string from 'int' under 'svcse_scheduler' and added unit test to support the same.
    * Modified ShowAPSummary
        * Updated regex pattern <ap_ip_address> to accommodate IPv6 address.
    * Modified ShowAPDot115ghzChannel
        * Updated regex pattern <lead_auto_chan_assn_capture> to accommodate Local or Leader words based on release.
        * Made last_run_seconds as Optional key.
    * Modified fix for ShowPowerDetail
        * Replaced ecomode with auto off to accomodate CLI change
    * Added support for Stack total input power variable
        * Added 'stack_total_input_power' in the schema
    * Modified ShowPlatformSoftwareFedSwitchActiveAclStatisticsEvents
        * Made switch and mode optional variables.
    * Modified ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummary
        * Made switch and mode optional variables.
    * Modified ShowCtsRoleBasedSgtMapAll
        * Added optional argument total_cached
    * Modified fix for ShowLispInstanceIdService
        * database value is present in Publication_entries_exported and Publication (Type - Config Propagation)
        * database value was overriden by the second occurence hence added a flag to avoid the overriding issue
    * Modified ShowProcessesMemorySorted
        * Made "reserve_p_pool" as optional field.

* iosxr
    * Modified fix for ShowRplRoutePolicy
        * Modified the 'as-path in' block in p19.match to correctly capture the 'as-path in' data
    * Modified MonitorInterface
        * Added missing empty_output_arguments.json files
    * Modified ShowBundle
        * Modified <wait_while_timer_ms> in schema to store either integer or string value.
        * Modified regex pattern <p9> to capture either integer or string value.
    * Modified ShowL2vpnXconnect
        * Updated regex pattern <p3> and <p6> to accommodate various outputs.

* viptela
    * Modified ShowOmpSummary
        * Added the new fields in schema to match the output

* nxos
    * Modified ShowVrfAllInterface
        * Updated regex pattern <p1> to accommodate various outputs which may contain underscore (_) as well.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedIpMfibVrfGroupDetail
        * Added schema and parser for 'show platform software fed switch active ip mfib vrf vrf_name group detail'
    * Added ShowL2vpnEvpnEsiMlagSummary
        * Introduced ShowL2vpnEvpnEsiMlagSummary parsers.
    * Added ShowL2vpnEvpnEsiMlagMacIP
        * Introduced ShowL2vpnEvpnEsiMlagMacIP parsers.
    * Added ShowL2vpnEvpnEsiMlagVlanBrief
        * Introduced ShowL2vpnEvpnEsiMlagVlanBrief parsers.
    * Added ShowPlatSoftFedSwAccessSecuritySecMacLrnTable parser.
        * Added parser for cli show plat soft fed sw {switch} access-security sec-mac-lrn-table summary.
        * Added parser for cli show plat soft fed sw {switch} access-security sec-mac-lrn-table mac {client_mac}.
        * Added parser for cli show plat soft fed sw {switch} access-security sec-mac-lrn-table interface if-id {if_id}.
    * Added ShowPlatformSoftwareFedSwitchNumberIfmMappingsLpn
        * Added schema and parser for 'Show Platform Software Fed Switch Number Ifm Mappings Lpn' under c9300
    * Added ShowHardwareLed
        * Added schema and parser for 'show hardware led' under c9610
    * Added ShowPlatformHardwareFedSwitchQosQueueConfigInterfaceQueueInclude
        * Added 'show platform hardware fed switch {sw_number} qos queue config interface {interface} queue {queue_id} | include {match}' command and schema for the command.
    * Added ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added schema and parser for 'show platform software fed {mode} acl info db detail' under c9610
    * Added ShowPlatformSoftwareFedSwitchActiveAclinfoSdkDetail parser.
        * Added parser for cli 'show platform software fed switch {switch_var} acl info sdk detail'.
        * Added parser for cli 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} detail'.
        * Added parser for cli 'show platform software fed switch {switch_var} acl info sdk feature {feature_name} dir {in_out} cgid {cg_id} detail'.
    * Added show interfaces | include {include}, show ip interface | include {include}, show ipv6 interface | include {include}
    * Added ShowSwitchStackPortSummary
        * Added schema and parser for 'show switch stack-ports summary' under c9350
    * Added ShowPlatformHardwareFedSwitchActiveStandbyFwdAsicInsightNplSummaryDiff
        * show platform hardware fed switch {type} fwd-asic insight npl_summary_diff({f1}, {f2}).
    * Added ShowDeviceTrackingCapturePolicy parser.
        * Added parser for cli show device-tracking capture-policy.
        * Added parser for cli show device-tracking capture-policy interface {interface_name}'.
        * Added parser for cli show device-tracking capture-policy vlan {vlan_id}.
    * Added ShowPlatformSoftwareFedIpMfibVrfCount
        * Added 'show platform software fed {switch_var} {state} ip mfib vrf {vrf_name} count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpIgmpSnoopingSummary
        * Added 'show platform software fed {switch_var} {state} ip igmp snooping summary' command and schema for the command.
    * Added ShowPlatformSoftwareFedMldSnoopingIpv6GroupsCount
        * Added 'show ipv6 mld snooping address vlan {vlan} {group} summary' command and schema for the command.
    * Added ShowPrpChannelDetails
        * Added schema and parser for show prp channel detail
    * Added ShowPlatformSoftwareInterfaceF0Name
        * Added 'show platform software interface f0 name {intf}' command and schema for the command.
    * Added ShowPlatformSoftwareObjectManagerF0ObjectDownlinks
        * Added 'show platform software object manager f0 object down links' command and schema for the command.
    * Added ShowPlatformSoftwareInfrastructureInject parser
        * Added parser for cli show platform software infrastructure Inject
    * Added ShowIpNbarProtocolPackActive
        * Added show show ip nbar protocol-pack active

* nxos
    * Modified ShowNveVni
        * show nve vni {vni}
    * Added show interface {interface} | include {include}, show interface | include {include} to show interface

* added showplatformhardwarefedswitchqosschedulerinterfaceinclude
    * Added schema and parser for 'show platform hardware fed switch {sw_number} qos scheduler interface {interface} | include {match}'

* added showplatformhardwarefedswitchqosinterfaceingressndpdetailedinclude
    * Added schema and parser for 'show platform software fed switch {sw_number} qos interface {interface} ingress npd detailed | include {match}'


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformFedActiveTcamUtilization
        * Added parser for show platform software fed switch active tcam utilization parser for c9610



genie.telemetry
"""""""""""""""
