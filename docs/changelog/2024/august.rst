August 2024
==========

August 27 - Genie v24.8 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 24.8                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 24.8                          |
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

* abstraction
    * Added Version


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* abstraction
    * Modified package.py
        * Fixed some issues with discovery



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * connect stage
        * add password recovery for connect stage.

* clean-pkg
    * updated the default keep configuration


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * set controller mode stage
        * the stage is now working properly fix the issue with stage and reload stage
    * Modified install_image
        * Added new flag skip_save_running_config to skip the step to save the the running configuration to the startup config.

* generic
    * Modified configure_management
        * Added `alias_as_hostname` argument
        * Allows user to use the alias as the device hostname



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * cat9k
        * Use the cmd string format instead of importing the module.



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_macro_name
        * API to configure 'macro name {macro_name}'.
    * Enhanced existing api configure_macro_global_apply
        * Modified API to configure 'macro global apply {macro_name} {variables} {values} '.
    * Added configure_ip_pim_vrf_ssm_range
        * API to configure ip pim vrf ssm range
    * Added unconfigure_ip_pim_vrf_ssm_range
        * API to unconfigure ip pim vrf ssm range
    * Added configure_ip_msdp_vrf_peer
        * API to configure msdp vrf peer
    * Added unconfigure_ip_msdp_vrf_peer
        * API to unconfigure msdp vrf peer
    * Added config_prp_sup_vlan_aware
        * prp channel-group 1 supervisionFrameOption vlan-aware-enable
    * Added unconfig_prp_sup_vlan_aware
        * no prp channel-group 1 supervisionFrameOption vlan-aware-enable
    * Added config_prp_sup_vlan_aware_allowed_vlan_list
        * prp channel-group 1 supervisionFrameOption vlan-aware-allowed-vlan 30,40
    * Added unconfig_prp_sup_vlan_aware_allowed_vlan_list
        * no prp channel-group 1 supervisionFrameOption vlan-aware-allowed-vlan
    * Added config_prp_static_vdan_entry
        * prp channel-group 1 vdanMacaddress 000001000011 vlan-id 10
    * Added unconfig_prp_static_vdan_entry
        * no prp channel-group 1 vdanMacaddress 000001000011
    * Added config_prp_sup_vlan_aware_reject_untagged
        * prp channel-group 1 supervisionFrameOption vlan-aware-reject-untagged
    * Added def unconfig_prp_sup_vlan_aware_reject_untagged(device, interface)
        * no prp channel-group 1 supervisionFrameOption vlan-aware-reject-untagged
    * Added config_prp_sup_vlan_id
        * prp channel-group 1 supervisionFrameoption vlan-id 10
    * Added unconfig_prp_sup_vlan_id
        * no prp channel-group 1 supervisionFrameoption vlan-id 10
    * Added config_prp_sup_vlan_tagged
        * prp channel-group 1 supervisionFrameOption vlan-tagged
    * Added unconfig_prp_sup_vlan_tagged
        * no prp channel-group 1 supervisionFrameOption vlan-tagged
    * Updated the config using f-strings
        * config = f"prp channel-group {interface} supervisionFrameOption vlan-aware-enable"
    * Updated api config_prp_static_vdan_entry as configure_prp_static_vdan_entry_with_vlan
        * prp channel-group 1 vdanMacaddress 000001000011 vlan-id 10
    * Added configure_prp_static_vdan_entry
        * prp channel-group 1 vdanMacaddress 000001000012
    * Added configure_interface_cts_role_based_sgt_map
        * API to configure interface cts role based sgt map
    * Added unconfigure_interface_cts_role_based_sgt_map
        * API to unconfigure interface cts role based sgt map
    * Added debug_platform_software_fed_drop_capture
        * added api to debug_platform_software_fed_drop_capture
    * Added debug_platform_software_fed_drop_capture_action
        * added api to debug_platform_software_fed_drop_capture_action
    * Added debug_platform_software_fed_drop_capture_buffer
        * added api to debug_platform_software_fed_drop_capture_buffer
    * Added configure_ignore_startup_config
        * added api to configure_ignore_startup_config
    * Added unconfigure_ignore_startup_config
        * added api to unconfigure_ignore_startup_config
    * Added verify_ignore_startup_config
        * added api to verify_ignore_startup_config
    * Added new API get_interfaces_switchport_state
        * get_interfaces_switchport_state - Get switchport state for interfaces
    * Added configure_radius_attribute_policy_name_globally
    * Added unconfigure_radius_attribute_policy_name_globally
    * Added configure_radius_attribute_policy_name_under_server
    * Added unconfigure_radius_attribute_policy_name_under_server
    * Added configure_radius_attribute_policy_name_under_servergroup
    * Added unconfigure_radius_attribute_policy_name_under_servergroup

* iosxe/cat9k
    * Added send_break_boot
        * send break boot command for cat9k devices

* sdk/triggers
    * blitz
        * Added new action check_yang_subscribe


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * send_break_boot
        * update the pattern for break boot for iosxe
    * Fixed clear_logging_onboard_rp_active_standby
        * added optional variable 'log_name'
    * Fixed confirm_iox_enabled_requested_storage_media
        * Added mod_storage_string and sso_storage_strings to support modular
    * Fixed configure_app_management_networking
        * Fixed returns True or False instead of none
    * Fixed issue with 'verify_interface_config_duplex' API
        * API not working fine when any other config present under interface for auto duplex.
    * Fixed issue with 'verify_interface_config_speed' API
        * API not working fine when any other config present under interface for auto speed.
    * Modified verify_current_image
        * Added provision to compare images based on regex if regex_search parameter is True
    * ASR1K
        * Added verify_current_image
            * Passing regex_search as True to compare images based on regex
    * Modified configure_management
        * Added `alias_as_hostname` argument
        * Allows user to use the alias as the device hostname
    * Modified health_logging
        * Fixed logic error with log count

* execute
    * execute power cycle
        * add try except for destroying device object.

* abstracted_libs
    * Modified __init__.py file to import all modules available in the abstracted_libs folder

* power cycler
    * snmp client
        * update the logic to work with tuple instead of iterator.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowSwitchStackRingSpeed
        * parser for 'show switch stack-ring speed'
    * Modified ShowLispEthernetPublisher
        * Modified the ShowLispEthernetPublisher parsers to facilitate new options.
    * Modified ShowEnvironmentStack
        * Fixed regular expressions p2 and p3 to match the correct values
    * Modified ShowXfsuEligibility
        * Added optional argument 'xfsu_platform_stauts' and made 'reload_fast_platform_stauts' as optional
    * Fixed ShowPlatformSoftwareFedIgmpSnooping
        * Fixed 'show platform software fed {switch_var} {state} ip igmp snooping vlan {vlan}' command and schema for the command.
    * Fixed ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlan
        * Fixed 'show platform software fed {switch_var} {state} ipv6 igmp snooping vlan {vlan}' command and schema for the command.
    * Modified fix for ShowLispRegistrationHistory
        * Modified the command to use the ShowLispRegistrationHistory parser for a more exact match and to fix the fuzzy search issue
    * Modified ShowBgpAllNeighbors
        * Mode peer_group as optional in schema and added p73 regex to match peer-group from user's output.
    * Modified fix for ShowCdpEntry
        * Made 'peer_mac' as optional in the schema
    * Modified parser ShowIpv6MldSnoopingVlan
        * Modified 'host_tracking' as optional argument, fix regex p2 and added unit tests
    * Modified parser ShowEnvironmentSuperParser
        * Added PS_MAPPING keyvalue for C and added unit test files
    * Modified ShowLicenseTechSupport Parser
        * Added optional agruments 'trust_point', 'ip_mode', 'trustpointenrollmentonboot', 'smartagentpurgeallreports'
        * 'smartagentslpenhanced', 'smartagentmaxermnotifylistsize'
    * Modified ShowEtherChannelDetail Parser
        * Made 'fast_switchover' and 'dampening' as optional agruments and added unit tests for the same
    * Modified fix for ShowPlatformFedSwitchActiveFnfRecordCountAsicNum
        * Modified the name of the command in the parser comment section in ShowPlatformFedSwitchActiveFnfRecordCountAsicNum
    * Added ShowPlatformFedActiveFnfRecordCountAsicNum
        * Added schema and parser for show platform software fed active fnf record-count asic <asic num>
    * Modified ShowPlatformSoftwareFedSwitchActiveAclUsage
        * Added switch_num to show command.
    * Modified ShowPlatformSoftwareFedSwitchActivEAclUsage
        * Added switch_num to show command.
        * Renamed class name ShowPlatformSoftwareFedSwitchActivEAclUsage to ShowPlatformSoftwareFedSwitchActiveAclUsage
    * Deleted ShowPlatformSoftwareFedSwitchStandbyAclUsage
        * Removed duplicate class.
    * Modified fix for ShowPlatformSoftwareFedSwitchActiveAclUsage
        * Modified the Regex pattern p<2> to accommodate various outputs
    * Modified fix for ShowVersion
        * Modified the schema, Added regex pattern <p33> and added the corresponding code to get SMUs data in the output.
    * Modified ShowPlatform
        * update lines to match the output of the IE model into genie parser show platform i.e IE- , ESS- keywords that will ensure IE family supports.
    * Modified fix for ShowPlatformSoftwareFedSwitchActiveIpRouteDetail
        * Updated regex pattern and added keys in schema for show platform software fed {switch} {mode} ip route {ip_add} {detail}
        * Updated regex pattern and added keys in schema for show platform software fed {switch} {mode} ip route {ip_add}
    * Modified ShowMonitorEventTraceDmvpnAll
        * Fixed incorrect regex for events NHRP-CTRL-PLANE-RETRANS and NHRP-TUNNEL-ENDPOINT-ADD
    * Modified ShowMonitorEventTraceDmvpnAll
        * Fixed incorrect regex for events NHRP-CTRL-PLANE-RETRANS
    * Added missing empty_output_arguments.json files.
    * Removed unused golden output tests
    * Modified ShowPlatformSoftwareIgmpSnoopingGroupsCount
        * Added regex pattern <p2> and <p3> to accommodate various outputs.
    * Modified ShowPlatformSoftwareFedSwitchActiveIpRoute
        * Updated parameters default value
    * Added ShowPlatformSoftwareFedIpMfibCount/ShowPlatformSoftwareFedIpMfibSummary
        * Added missing ShowPlatformSoftwareFedSwitchActiveIpRoute
    * Removed ShowPlatformSoftwareFedIgmpSnoopingGroupsCount
        * Because we have ShowPlatformSoftwareIgmpSnoopingGroupsCount parser for same commands
    * Modified ShowInterfaces
        * Added <in_drops>, <out_drops>, <peer_ip> and <vc_id> into schema as Optional.
        * Renamed regex pattern <p_cd>, <p_cd_2> to <p54>, <p55> respectively and updated the code accordingly.
        * Added regex pattern <p1_2>, <p6_1>, <p56>, <p57> and <p58> to accommodate various outputs.
    * Modified ShowModule
        * Changed <mac_address>, <hw>, <fw>, <sw> and <status> from schema to Optional.
    * Modified ShowCtsInterface
        * Added Vlan Sgt-Map tabulated data to the schema.
        * Added regex p27 to parse the Vlan Sgt-Map tabulated data.
    * Modified fix for ShowLogging
        * Removed the variable that initializes a dictionary for the key log_buffer_bytes

* nxos
    * Revised ShowNveEthernetSegment
        * removed keys 'cc_failed_vlans', 'cc_timer_left' and 'ead_evi_rt_timer_age' keys
        * added keys 'df_bd_list', 'df_vni_list', 'esi_type' and 'esi_df_election_mode'
        * made changes to regular expressions to accomodate the parent interface as port-channel
    * Fixed parser show access-lists summary
        * Updated the attachment_points as optional so that it should not throw errors if no attached interfaces are present
    * Modified ShowNtpPeerStatus
        * Updated regex pattern <p2_1> to parse valid IP adddress.
        * Updated code to fix wrong clock_state value.

* added showplatformsoftwarefedigmpsnoopingvlandetail
    * Added 'show platform software fed {switch_var} {state} ip igmp snooping vlan {vlan} detail' command and schema for the command.

* added showplatformsoftwarefedactiveipv6mldsnoopingvlandetail
    * Added 'show platform software fed {switch_var} {state} ipv6 igmp snooping vlan {vlan} detail' command and schema for the command.

* iosxr
    * Modified fix for ShowMplsLdpParameters
        * Modified schema, updated regex pattern <p21>, added patterns <p32> and <p33>, and added the corresponding code to get IGP sync delay data.
    * Modified MonitorInterface
        * Added missing empty_output_arguments.json files
    * Modified MonitorInterfaceInterface class
        * Renamed class to MonitorInterface
        * Added support for the following CLI commands
            * monitor interface
            * monitor interface full-name
            * monitor interface filter physical
            * monitor interface {interface} full-name
            * monitor interface {interface} full-name wide
            * monitor interface {interface} wide full-name
    * Added Revision 1 of MonitorInterface
        * Changed convert_intf_name to use iosxr specific mapping
    * Modified ShowSegmentRoutingSrv6LocatorSid
        * Updated code to fix folder_parsing job for empty test

* common
    * Modified get_parser function to pass the formatted command as `command` variable
    * User can now use the following syntax for parser `cli` method
        * ``def cli(self, command, output=None, **kwargs)``

* utils
    * Updated unittest code to run empty tests successfully

* <nxos>
    * Modified ShowIpRoute
        * Updated regex pattern <p2> to accommodate new output line


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * New ShowSwitchStackBandwidth
        * Parser for 'show switch stack-bandwidth'
    * Added ShowPlatformSoftwareFedSwitchAclUsageIncludeAcl
        * Added show platform Software fed switch {switch_num} acl usage
        * Added show platform Software fed switch {switch_num} acl usage | include {acl_name}
    * Added ShowPlatformSoftwareFedSwitchActiveAclBindDbIfid parser.
        * Added parser for cli show platform software fed switch active acl bind db if-id {if_id} detail.
    * Added ShowPlatformSoftwareFedSwitchAclUsageIncludeAcl
        * Added show platform Software fed switch {switch_num} acl usage
        * Added show platform Software fed switch {switch_num} acl usage | include {acl_name}
    * Added ShowPlatformSoftwareFedSwitchActiveIfmInterfacesInternal parser.
        * Added parser for cli show platform software fed switch active ifm interfaces internal {interface}.
    * Fixed regex pattern for cli ShowPlatformSoftwareFedSwitchActiveIfmInterfacesLabel parser.
        * Fixed regex pattern for cli show platform software fed {switch} active ifm interfaces {label}.
    * Added ShowPlatformSoftwareFedSwitchActiveInjectBrief
        * Added show platform software fed {switch} {mode} inject ios-cause brief
        * Added show platform software fed active inject ios-cause brief
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedArpIf parser.
        * Added parser for cli show platform software fed switch active security-fed arp if {if_id}.
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityFedArpVlan parser.
        * Added parser for cli show platform software fed switch active security-fed arp vlan {vlan}.
    * Added ShowIdprom parser
        * Added show idprom all cli
    * Added ShowSpanningTreeSummaryTotals
        * Added show spanning-tree summary totals
    * Added ShowModule
        * Added schema and parser for 'show module' under c9610
    * Added ShowPlatformSoftwareFedIpv6MfibCount
        * Added 'show platform software fed {switch_var} {state} ipv6 mfib count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpv6MfibSummary
        * Added 'show platform software fed {switch_var} {state} ipv6 mfib summary' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpv6MldSnoopingSummary
        * Added 'show platform software fed {switch_var} {state} ipv6 mld snooping summary' command and schema for the command.
    * Added ShowPlatformSoftwareFedSwitchActiveipecrexactroutesourceipdestinationip
        * show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip} {sourceport} {destinationport} {protocol}
            * show platform software fed switch {type} ip ecr exact-route {sourceip} {destinationip}
    * Added ShowPlatformHardwareFedPortPrbscmdSchema
        * Added parser for show platform hardware fed {switch} {mode} npu slot 1 port {port_num} prbs_cmd {num}
    * Added ShowPlatformHardwareFedPrbsPolynomialSchema
        * Added parser for show platform hardware fed switch {mode} npu slot 1 port {port_num} prbs_polynomial {num}
    * Added ShowPlatformHardwareFedloopbackSchema
        * Added parser for show platform hardware fed switch {mode} npu slot 1 port {port_num} loopback {num}
    * Added ShowPlatformHardwareFedeyescanSchema
        * Added parser for show platform hardware fed switch {mode} npu slot 1 port {port_num} eye_scan
    * Added ShowPlatformSoftwareFedSwitchActivePuntPacketCapturedisplayFiltericmpv6Brief
        * Added schema and parser for 'show platform software fed switch active punt packet-capture display-filter icmpv6 brief'
    * Added ShowPlatformHardwareFedSwitchActiveFwdasicdropsasic
        * show platform hardware fed switch {switch} fwd-asic drops asic {asic}

* nxos
    * Added ShowNveEthernetSegmentSummary
        * show nve ethernet-segment summary
        * show nve ethernet-segment summary esi {esi_id}
    * Added ShowNveEthernetSegment
        * show nve ethernet-segment esi {esi_id}


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowLispEthernetARSubscriber
        * Introduced the ShowLispEthernetARSubscriber parsers.
    * Added ShowLispEthernetARPublisher
        * Introduced ShowLispEthernetARPublisher parsers.
    * Added ShowLispEthernetMapCachePrefixAR
        * Introduce ShowLispEthernetMapCachePrefixAR parser.



genie.telemetry
"""""""""""""""""
