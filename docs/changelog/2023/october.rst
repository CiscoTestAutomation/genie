October 2023
==========

October 31 - Genie v23.10
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.10                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.10                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

If you have pyATS installed, you can use:

.. code-block:: bash

    pyats version update



.. warning::
    Backwards compatibility in ``genie.libs.parser``:

    `ShowLispEthernetDatabase` was removed as a duplicate of the
    `ShowLispDatabaseSuperParser`. The super parser output schema is similar
    but not fully backward compatible with the removed parser and may result in
    errors in tests that depend on specific values of the removed parser output.


Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* harness
    * Modified Standalone
        * Fixed searching parent or task object for loaded triggers and verifications



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* recovery
    * Update device recovery logic for checking the state machine. Instead of clearing the line

* generic
    * Update defaults for clean stages



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

* iosxe
    * Added API configure_paramter_map
        * API for configuring the parameter map with all the sub-commands included
    * Added API unconfigure_paramter_map
        * API for unconfiguring the parameter map
    * Added __init__.py for vdsl folder
        * Added __init__.py for vdsl folder
    * Added added_api_rep_admin_vlan_configure API
        * API to configure rep admin vlan
    * Added configure_ospfv3_network_type
        * New API to configure ospfv3 network type
    * Added configure_ospfv3_interface
        * New API to configure ospfv3 interface
    * Added clear_ip_dhcp_snooping_binding_on_interface
        * API for clear ip dhcp snooping binding on interface
    * Added configure_device_policy_tracking
        * API for configure device policy tracking
    * Added configure_source_tracking_on_interface
        * API for configure source tracking on interface
    * Added configure_interface_range_dhcp_channel_group_mode
        * New API to configure interface range channel-group 1 mode desirable
    * Added unconfigure_interface_range_dhcp_channel_group_mode
        * New API to unconfigure interface range channel-group 1 mode desirable
    * Added configure_ip_sftp_password
        * API to configure ip sftp password
    * Added unconfigure_ip_sftp_password
        * API to unconfigure ip sftp password
    * Added configure_ip_scp_password
        * API to configure ip scp password
    * Added unconfigure_ip_scp_password
        * API to unconfigure ip scp password
    * Added config_interface_prpchannel
        * added api to config_interface_prpchannel
    * Added unconfig_interface_prpchannel
        * added api to unconfig_interface_prpchannel
    * Added `configure_management_ntp` API
    * Added format_directory
        * API to format {directory}
    * Added configure_vtp_pruning
        * API to vtp pruning
    * Added unconfigure_vtp_pruning
        * API to no vtp pruning
    * Added configure_switchport_trunk_pruning_vlan
        * API to configure switchport trunk pruning vlan
    * Added unconfigure_switchport_trunk_pruning_vlan
        * API to configure no switchport trunk pruning vlan
    * Added configure_periodic_time_range
        * API to configure periodic time range
    * Added unconfigure_periodic_time_range
        * API to unconfigure periodic time range
    * Added configure_absolute_time_range
        * API to configure absolute time range
    * Added unconfigure_absolute_time_range
        * API to unconfigure absolute time range
    * Added configure_hw_module_slot_logging_onboard_voltage API
        * Added API for hw-module slot {slot} logging onboard voltage
    * Added unconfigure_hw_module_slot_logging_onboard_voltage API
        * Added API for no hw-module slot {slot} logging onboard voltage
    * Added configure_hw_module_slot_logging_onboard_temperature API
        * Added API for hw-module slot {slot} logging onboard temperature
    * Added unconfigure_hw_module_slot_logging_onboard_temperature API
        * Added API for no hw-module slot {slot} logging onboard temperature
    * Added configure_hw_module_slot_logging_onboard_environment API
        * Added API for hw-module slot {slot} logging onboard environment
    * Added unconfigure_hw_module_slot_logging_onboard_environment API
        * Added API for no hw-module slot {slot} logging onboard environment
    * Added configure_clear_logging_onboard_slot_temperature API
        * Added API for clear  logging  onboard  slot {slot}  temperature
    * Added configure_clear_logging_onboard_slot_voltage API
        * Added API for clear  logging  onboard  slot {slot}  voltage
    * Added configure_clear_logging_onboard_slot_environment API
        * Added API for clear  logging  onboard  slot {slot}  Environment
    * Added configure_ip_sftp_username
        * API to configure ip sftp username
    * Added unconfigure_ip_sftp_username
        * API to unconfigure ip sftp username
    * Added configure_ip_scp_username
        * API to configure ip scp username
    * Added unconfigure_ip_scp_username
        * API to unconfigure ip scp username
    * Added configure_snmp_mib_bulkstat_transfer
        * API to configure snmp mib bulkstat transfer
    * Added copy_file_with_sftp
        * API to copy file from device to sftp host
    * Added copy_file_with_scp
        * API to copy file from device to scp host
    * Added api to execute more file
        * API to execute more file on device and get the output
    * Added execute_install_package_reloadfast
        * API to execute install package reloadfast
    * Added api to execute set platform hardware rom-monitor virtualization
        * API to execute set platform hardware rom-monitor virtualization on device and get the output
    * Added configure_interface_vlan_range_priority
        * API to set vlan interface priority
    * Added configure_interface_vlan_priority
        * API to set vlan interface rnage priority
    * Added unconfigure_ipv6_router_ospf
        * New API for no ipv6 router ospf {ospf_process_id}
    * Added api to configure service compress-config
        * API to configure service compress-config on device
    * Added api unconfigure service compress-config
        * API to unconfigure service compress-config on device
    * Added api configure_ip_igmp_querier_query_interval
        * API to configure ip igmp querier query interval
    * Added api configure_ip_igmp_querier_tcn_query_count
        * API to configure ip igmp querier tcn query count
    * Added configure_spanning_tree_etherchannel_misconfig
        * added api to configure_spanning_tree_etherchannel_misconfig
    * Added unconfigure_spanning_tree_etherchannel_misconfig
        * added api to unconfigure_spanning_tree_etherchannel_misconfig

* added configure_hw_module_logging_onboard api
    * Added API for hw-module slot {slot} logging onboard

* added unconfigure_hw_module_logging_onboard api
    * Added API for no hw-module slot {slot} logging onboard


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_bandwidth_remaining_policy_map
        * Fixed the mandatory argument to optional "class_names=None,bandwidth_list=None"
    * Modified enable_usb_ssd_verify_exists
        * Fixed the time argument to timeout
    * Fixed logic for get_mgmt_ip_and_mgmt_src_ip_addresses when passing IP address
    * Modify configure_enable_nat_scale
        * added boolean variables nat_aot and nat_scale
    * Modify configure_disable_nat_scale
        * added boolean variables nat_aot and nat_scale
    * Modified change_configure_crypto_pki_server_eaptls
        * Passing kwargs and condition to configure_crypto_pki_server
    * Modified change_configure_crypto_pki_server_pki
        * Passing kwargs and condition to configure_crypto_pki_server
    * Removed
        * Removed duplicate keyword configure_stack_power_stack and unconfigure_stack_power_stack
        * Removed corresponding UT as well for those keywords.

* nxos
    * Modified
        * Updated nxapi_method_nxapi_rest API to handle output of type RESPONSE
    * Fixed logic for get_mgmt_ip_and_mgmt_src_ip_addresses when passing IP address

* blitz
    * Fix gnmi_util to enclose leaf-list entries within [].
    * Fixed negative test handling for gnmi get
    * Fixed decoding of proto encoding in Gnmi
    * Added better logging for Gnmi

* iosxr
    * Fixed logic for get_mgmt_ip_and_mgmt_src_ip_addresses when passing IP address

* genie.libs.sdk
    * Fixed RPC Verifier regex substitution usage
    * Added check for allowed fields for OptFields class, log warning for unknown fields


--------------------------------------------------------------------------------
                                     Modify
--------------------------------------------------------------------------------

* iosxe
    * Modify configure_scale_vrf_via_tftp
        * add both ipv4 and ipv6 address family



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * ShowL2vpnBridgeDomainDetail
        * Added missing UT for ShowL2vpnBridgeDomainDetail

* iosxe
    * Added show mrp ring parser
        * Parser to get values for show mrp ring
    * Added ShowPortSecurityAddress
        * parser for "show port-security address"
    * Added ShowPlatformSoftwareFedSwitchAclIfId
        * parser for 'show platform software fed switch {switch} {mode} if-id {if_id}'
    * Added affinity_id support
        * Added affinity_id support in show publication prefix schema, parser.
        * Added affinity_id support in show map-cache prefix schema, parser.
        * Added affinity_id support in show database schema, parser.
    * New Parser for TestVdslOption
        * Parser for 'test vdsl option option1 option2'
    * Added ShowPlatformHardwareFedSwitchQosQueueConfig
        * show platform hardware fed {switch_var} qos queue config interface {interface}
        * show platform hardware fed {switch} {switch_var} qos queue config interface {interface}
    * Added ShowNat66Statistics
        * show nat66 statistics
    * Added ShowNat66Prefix
        * show nat66 prefix
    * Added ShowNat66Nd
        * show nat66 nd
    * Added ShowPlatformHardwareQfpActiveFeatureNat66DatapathPrefix
        * show platform hardware qfp active feature nat66 datapath prefix
    * Added show mrp ports parser
        * Parser to get values for show mrp ports
    * Added ShowTechSupportIncludeShow
        * Added schema and parser for show tech-support | i show
    * Added ShowIpMfibCount
        * parser for show ip mfib | count {interface}
    * Added ShowInterfaceHumanReadableIncludeDrops
        * show interface {interface} human-readable | i drops
    * Added ShowIpIgmpSnoopingMrouterVlan Parser
        * Parser for show ip igmp snooping mrouter vlan {vlan}
    * Added ShowAvbDomain
        * parser for 'show avb domain'
    * Added ShowPlatformSoftwareAccessListSwitchActiveF0Summary
        * Added schema and parser for show platform software access-list switch active F0 summary
    * Added ShowIpIgmpSnoopingQuerierVlanDetail
        * added parser for "show ip igmp snooping querier vlan {vlan} detail"
    * Added ShowPlatformSoftwareFedSwitchActiveAclStatisticsEvents
        * parser for Show Platform Software Fed Switch Active Acl Statistics Events
    * Added ShowPlatformPmEtherchannelGroupMask
        * Parser for show platform pm etherchannel {ec_channel_group_id} group-mask
    * Added ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Parser for show platform software fed switch active stp-vlan {vlan_id}

* iosxr
    * Added ShowL2vpnForwardingXconnectDetailLocation
        * parser for 'show l2vpn forwarding xconnect {xconnect_name} detail location {location_name}'
    * Added ShowOspfSummary
        * Added parser for cli 'show ospf {process_name} summary'
        * Added parser for cli 'show ospf {process_name} vrf {vrf_name} summary'
    * Added ShowBgpVrf
        * added new parser for cli 'show bgp vrf {vrf}'
        * added new parser for cli 'show bgp vrf {vrf} {summary}'
        * added new parser for cli 'show bgp vrf {vrf} {address_family} summary'
        * added new parser for cli 'show bgp vrf {vrf} {address_family} {value}'


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowAccessSessionMacDetails parser.
        * Added Local policies New keys in Schema.
        * Added Server policies New key in Schema.
        * Modified user_name key as optional in Schema.
        * Added regex pattern for newly added keys
    * Modified ShowPlatformSoftwareMemoryCallsite
        * Updated regex pattern <p2> to accommodate hex callsites.
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * added switch_type argument to execute show cli on standby
    * Modified ShowPlatformTcamPbrNat
        * added switch_type argument to execute show cli on standby
    * Modified ShowPlatformSoftwareFedSwitchActivePuntCpuq
        * added switch_type argument to execute show cli on standby
    * Modified ShowFirmwareVersionAll Parser
        * Added "switch" option to the firmware CLI
    * Fixed ShowControllerVDSLSchema parser
        * Parser for "show controller vdsl <slot no>"
    * Modified affinity_id support
        * Removed affinity_id support in show database prefix schema, parser under
        * Added affinity_id support in show database prefix schema, parser under
    * Fixed ShowIdpromInterface Parser
        * Added the key 'vendor_part_number' to schema.
    * Modified ShowIpMroute
        * Allow parsing IPv6 next hop for LISP outgoing interface.
        * Allow parsing Inherited outgoint interface list.
    * Modified ShowIpv6Mfib
        * Allow parsing blank Mfib flags.
        * Allow parsing IPv6 next hop for LISP outgoing interface.
    * Modified ShowRunInterface
        * Added 111 regex for pim outputs
    * Modified ShowModule Parser
        * Fixed parser for multiple switches
    * Enhanced BGP router ID extraction
        * Modified the regular expression pattern (p1) to support both interface name and IP address for BGP router ID.
    * Modified BGP router ID extraction from IP Address
        * Added new support for BGP router ID extraction from the provided IP address.
    * Modified ShowRomMonSwitchR0
        * parser for 'show rom-mon switch {switch_num} {process}'
    * Added ShowIpNatStatistics Parser
        * Added if condition for name_1 and name_2 key to match with all available output.
    * Modified ShowClnsNeighborsDetail
        * Updated the regex to support `-`
    * Removed duplicate class ShowLispEthernetDatabase
        * removed the duplicate class and add a optional key to ShowLispDatabaseSuperParser schema
    * Modified ShowIpIgmpSnoopingQuerier Parser
        * Fixed parser for all type of ports
    * Modified ShowBootvar
        * Updated regex pattern <p1> to parse the output which contains WHITESPACE in BOOT variable string.
    * Modified ShowStackPowerLoadShedding Parser
        * Fixed p2 and p3 regular expressions
    * Modified ShowPlatformSoftwareWiredClientFpActive Parser
        * Added line.strip()
    * Modified ShowPtpClock Parser
        * Made message_general_ip_dscp and message_event_ip_dscp as optional keys
    * Modified ShowPlatformSoftwareFedSwitchActivePtpDomain Parser
        * Made message_general_ip_dscp and message_event_ip_dscp as optional keys
    * Modified ShowIpv6MldGroups Parser
        * parser for 'show ipv6 mld groups'
    * Updated ShowBgpAllNeighbors parser
        * Added `ack_hold` and `fastretransmit` to exclude list
    * Modified ShowCdpNeighborsDetail
        * Changed software_version from schema to Optional.
    * Modified ShowEnvironmentSuperParser Parser
        * Fixed p1 and p1_1 regex
            * Added New regex p13,p14 and p15 for new log

* nxos
    * Fix for show bgp vrf all all summary parser
        * Added int and float pattern to match all possible values
    * Fix for show bgp vrf <vrf> all neighbors <neighbor> advertised-routes parser
        * Added p9_1 pattern to match all possible state values

* iosxr
    * Modified ShowL2vpnBridgeDomainDetail
        * Adding Optional evi in schema due to parser failed with schema key error
    * Modified ShowRouteIpv4
        * Modified 'outgoing_interface' keyname as optional parameter in schema
        * Added keys 'label', 'tunnel_id', 'binding_label', 'extended_communites_count', 'nhid', 'path_grouping_id', 'srv6_headend' and 'sid_list' as optional parameters in scehma
        * Fixed pattern <p11> as it should not match line 'NHID0x0(Ref0)'
        * Added pattern <p16> to support line 'Label None'
        * Added pattern <p17> to support line 'Tunnel ID None'
        * Added pattern <p18> to support line 'Binding Label None'
        * Added pattern <p19> to support line 'Extended communities count 0'
        * Added pattern <p20> to support line 'NHID0x0(Ref0)'
        * Added pattern <p21> to support line 'Path Grouping ID 100'
        * Added pattern <p22> to support line 'SRv6 Headend H.Encaps.Red [f3216], SID-list {fc00c0001002e002}'
    * Modified ShowRouteIpv6
        * Fixed pattern <p12> as it should not match line 'NHID0x0(Ref0)'
        * Added pattern <p15> to support line 'Label None'
        * Added pattern <p16> to support line 'Tunnel ID None'
        * Added pattern <p17> to support line 'Binding Label None'
        * Added pattern <p18> to support line 'Extended communities count 0'
        * Added pattern <p19> to support line 'NHID0x0(Ref0)'
        * Added pattern <p20> to support line 'Path Grouping ID 100'
        * Added pattern <p21> to support line 'SRv6 Headend H.Encaps.Red [f3216], SID-list {fc00c0001002e003}'

* <iosxe>
    * Added <ShowControlConnections>
        * Change the <p1> regex under if block for <peer_organization>

* iosxe/c9600
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Made mode dynamic in CLI command

* iosxe/c9600/c9606r
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Made mode dynamic in CLI command


--------------------------------------------------------------------------------
                                     Modify
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispInstanceidService
        * Added ethernet_fast_detection to schema and parser.
    * Modified ShowRomvar
        * Made boot key as optional.


--------------------------------------------------------------------------------
                                    Modified
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPppoeSession parser
        * Parser for "show pppoe session"



genie.telemetry
"""""""""""""""""



genie.trafficgen
"""""""""""""""""

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* trex
    * Modified Trex
        * Add ability to pass a cfg file when autobooting trex


--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* trex
    * Add new APIs to trex implementation.py:
        * Added support for injecting ns nud, ns dad, rs, ra, redirect packets
