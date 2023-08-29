August 2023
==========

August 29 - Genie v23.8
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.8                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.8                          |
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

* genie.cli.commands.job
    * Added suite_name and test_suite to configure_parser to fix the broken genie

* genie.harness
    * Added support for `vty` as connection name in default mapping



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* generic
    * Change logic for copy_to_device to check for local file size before trying from remote server


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * CopyToDevice clean stage
        * Added check to verify the current running image and skip the stage.



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
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_ipv6_acl
        * added time range parameter
    * Modified `configure_management_vty_lines` API to only set authentication if username and password provided
    * Modified configure_dhcp_pool_ipv6_domain_name
        * API to configure dhcp-pool ipv6 domain-name
    * Modify configure_bgp_address_advertisement
        * Updated API to support vrf
    * Modified configure_snmp_server_enable_traps_power_ethernet_group
        * added correct mode of execution
        * variable name modified as mentioned in def arguments
    * Modified API's to unconfigure skip-client cli.
        * API to unconfigure_sks_client
    * Modified configure_interface_service_policy
        * added return statement to return the output
    * Modified configure_archive_logging
        * added optional variables hidekeys, notify_syslog. Default set to True
    * Modified request_platform_software_package_clean
        * added optional variables timeout default to 60
    * Modified generate_crypto_key
        * added mapping timeout which is missing
    * Modified delete_local_file
        * added dialog
    * Modified clear_logging
        * added timeout optional variable default to 60
    * Modified delete_local_file
        * added the dialog statement
    * Modified configure_interface_ip_verify_unicast_reversepath
        * added no_switchport optional input variable
    * Modified configure_interface_ip_verify_unicast_notification
        * added no_switchport optional input variable
    * Modified configure_interface_ip_verify_unicast_source
        * added no_switchport optional input variable
    * Modified configure_interface_ipv6_verify_unicast_reversepath
        * added no_switchport optional input variable
    * Modified hw_module_switch_usbflash_security_password
        * added return statement
    * Modified request_system_shell
        * added command optional variable
    * Modify configure_switchport_vlan_mapping
        * API for configure switchport vlan mapping
    * Modify unconfigure_switchport_vlan_mapping
        * API for unconfigure switchport vlan mapping
    * Modified config_ip_on_vlan
        * API for config_ip_on_vlan
    * Modified unconfig_ip_on_vlan
        * API for unconfig_ip_on_vlan
    * Modified configure_dhcp_pool
        * added parameter vrf and dns_server
    * Modified unconfigure_dhcp_pool
        * added parameter vrf and dns_server

* blitz
    * Converted sanity test to end-to-end tests.
    * Added
        * Added support of datastore to the Blitz action, 'yang_snapshot_restore'. Also it will send edit-config after multiple locking tries.

* genie.libs.sdk
    * Modified blitz RPC verification code to support XPATH with and without key prefix
    * Modified blitz RPC verification code to support XPATH with leading and trailing WHITESPACE in Key content
    * Modified trim_response method to return the list of all responses from the index of parent_key


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added api delete_directory
        * API to delete directory from the filesystem
    * Added API's to configure cli commands to collect smd logs and store it in a flash feature.
        * API to show_logging_smd_output_to_file
    * Added unconfigure_ipv6_redirects
        * API to unconfigure ipv6 redirects
    * Added configure_ipv6_nd_suppress_ra
        * API to configure ipv6 nd suppress-ra
    * Added unconfigure_ipv6_nd_suppress_ra
        * API to unconfigure ipv6 nd suppress-ra
    * Added unconfigure_ipv6_address_test
        * API to unconfigure ipv6 address test
    * Added configure_ipv6_address_config
        * API to configure ipv6 address config
    * Added unconfigure_ipv6_address_config
        * API to unconfigure ipv6 address config
    * Added unconfigure_ipv6_address_autoconfig
        * API to unconfigure ipv6 address autoconfig
    * Added API's to configure cli commands for aaa filter-spec protocol config feature.
        * API to configure_access_session_attr_filter_list
        * API to unconfigure_access_session_attr_filter_list
        * API to unconfigure_access_session_attr_filter_list_protocol
    * Added configure_bba_group_session_auto_cleanup
        * added api to configure_bba_group_session_auto_cleanup
    * Added configure_avb
        * API to configure avb
    * Added unconfigure_avb
        * API to unconfigure avb
    * Added enable_keepalive_on_interface
        * API to configure enable_keepalive_on_interface
    * Added configure_ptp_enable_on_interface
        * New API to configure ptp enable on interface
    * Added configure_no_ptp_enable_on_interface
        * New API to unconfigure no ptp enable on interface
    * Modified cts manual cli
        * API to configure policy with or without trust and also to disable propagation
    * Add new API verify_bgp_neighbor_state_vrf
        * Verify state/pfxrcd entry in show bgp {vpnv4/vpnv4} {unicast} vrf {vrfid} summary
    * Add logging pre-check in health check
    * Added configure_monitor_capture_export_location
        * New API to Configure Monitor capture export location file
    * Added configure_monitor_capture_export_status
        * New API to Configure Monitor capture export status
    * Added enable_debug_pdm
        * API to execute debug pdm {parameter} {enable}
    * Added disable_debug_pdm
        * API to configure no debug pdm {parameter} {enable}
    * Added unconfigure_switchport_trunk_allowed_vlan
        * API to unconfigure switchport trunk allowed vlan
    * Added unconfigure_switchport_trunk_native_vlan
        * API to unconfigure switchport trunk native vlan
    * Added disable_switchport_trunk_on_interface
        * API to disable switchport trunk
    * Added configure_switchport_pvlan_trunk_allowed_vlan
        * API for configure pvlan trunk allowed vlan
    * Added unconfigure_switchport_pvlan_trunk_allowed_vlan
        * API for unconfigure pvlan trunk allowed vlan
    * Added configure_switchport_pvlan_trunk_native_vlan
        * API for configure pvlan trunk native vlan
    * Added unconfigure_switchport_pvlan_trunk_native_vlan
        * API for unconfigure pvlan trunk native vlan
    * Added configure_interface_pvlan_mapping
        * API for configure interface pvlan mapping
    * Added unconfigure_interface_pvlan_mapping
        * API for unconfigure interface pvlan mapping
    * Added unconfigure_interface_switchport_pvlan_mapping
        * API for unconfigure interface switchport pvlan mapping
    * Added unconfigure_interface_switchport_pvlan_association
        * API for unconfigure interface switchport pvlan association
    * Added unconfigure_interface_pvlan_host_assoc
        * API for unconfigure interface pvlan host association
    * Added clear_interface_range
        * API for clear the interface range
    * Added API's to configure cli commands for QoS feature.
        * API to configure_table_map_on_device
        * API to configure_policy_map_class_precedence
        * API to unconfigure_interface_service_policy
    * Added API's to configure cli commands for aaa filter-spec accounting feature.
        * API to config_access_session_accnt_attr_filter_spec_include_list
        * API to unconfig_access_session_accnt_attr_filter_spec_include_list
    * New unconfigure_management_netconf
        * Added api unconfigure_management_netconf
    * Added configure_ipv4_object_group_network
        * API for configure ipv4 object group network
    * Added unconfigure_ipv4_object_group
        * API for unconfigure ipv4 object group
    * Added configure_ipv4_object_group_service
        * API for configure ipv4 object group service
    * Added unconfigure_ipv4_object_group_service
        * API for unconfigure object group service
    * Added configure_ipv4_ogacl_src_dst_nw
        * API for configure ipv4 ogacl src dst nw
    * Added configure_ipv4_ogacl_service
        * API for configure ipv4 ogacl service
    * Added configure_ipv4_ogacl_ip
        * API for configure ipv4 ogacl ip
    * Added unconfigure_ipv4_ogacl
        * API for unconfigure ipv4 ogacl
    * Added configure_ipv4_ogacl_on_interface
        * API for configure ipv4 ogacl on interface
    * Added unconfigure_ipv4_ogacl_on_interface
        * API for unconfigure ipv4 ogacl on interface
    * Added configure_glbp_details_on_interface
        * API for configure glbp details on interface
    * Added API's to configure cli commands for aaa authentication filter-spec feature.
        * API to config_access_session_auth_attr_filter_spec_include_list
        * API to unconfig_access_session_auth_attr_filter_spec_include_list
    * Added execute_switch_card_OIR_power_force
        * New API to executr switch card oir power force
    * Added configure_evpn_instance_evi
        * New API to configure evpn instance evi
    * Added unconfigure_evpn_instance_evi
        * New API to unconfigure evpn instance evi
    * Added configure_vfi_context_evpn
        * New API to  configure vfi context evpn
    * Added unconfigure_vfi_context_evpn
        * New API to unconfigure vfi context evpn
    * Added upgrade_hw_programmable
        * API to execute upgrade hw-programmable all
    * Added configure_udld_recovery
        * API to configure udld recovery
    * Added configure_l2vpn_evpn_ethernet_segment
        * API for configure_l2vpn_evpn_ethernet_segment
    * Added unconfigure_snmp_server_enable_traps_power_ethernet_group
        * API to unconfigure snmp server enable traps power ethernet group
    * Added configure_rommon_tftp
        * API to configure tftp rommon variables
    * Added clear_cts_counters_ipv4
        * API for clear cts role-based counters ipv4
    * Added unshut_port_channel
        * API for unshut_port_channel
    * Added get_lisp_instance_id_running_config
        * API for get_lisp_instance_id_running_config
    * Added clear_controllers_ethernet_controller
        * API to clear_controllers_ethernet_controller

* com
    * Added device_boot_recovery
        * API to boot the device from rommon using golden image or tftp boot.

* blitz
    * Added support for veryfing deletion of nodes while using GNMI
    * Added possibility to create custom verifiers and decoders when using Netconf.
    * Changed custom verifiers architecture from monolitic to modular (separate class per protocol).

* sdk
    * Version pinned pysnmp and pyasn1 to fix the type error in execute_power_cycle_device api



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPerformanceMeasurementPaths
        * show performance-measurement paths
    * Added ShowPerformanceMeasurementSummary
        * show performance-measurement summary
        * show performance-measurement summary {detail}
        * show performance-measurement summary {detail} {private}
    * Added ShowIpv6DhcpInterface Parser
        * Parser for 'show ipv6 dhcp interface'
        * Parser for 'show ipv6 dhcp interface {interface}'
    * Added ShowPlatformSoftwareFedSwitchActiveMatmMacTableVlanMac
        * show platform software fed {state} matm macTable vlan {vlan} mac {mac}
        * show platform software fed {switch} {state} matm macTable vlan {vlan} mac {mac}
    * Added ShowSdwanPolicyServicePath Parser
        * Parser for 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol}'
        * Parser for 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol} {all}'
    * Added show platform software fed switch {switch} fnf flow-record asic {asic} start-index {index} num-flows {flow} parser
    * Added ShowIpNatTranslationsTotal parser
        * Parser for "show ip nat translations total"
        * Parser for "show ip nat translations vrf <vrf name> total"
    * Added ShowMdnsSdCache
        * parser for 'show mdns-sd cache'
    * Added ShowTimeRange
    * Added ShowOspfv3vrfNeighborInterfaceSchema
        * parser for 'show ospfv3 vrf {vrf_id} neighbor interface'
    * Added ShowFlowMonitorCacheFilterInterfaceIPv4 Parser
        * Parser for 'show flow monitor {name} cache filter interface {direction} {interface_name} ipv4 {address_direction} address {address}'
    * Added ShowDropsHistoryQfp
        * show drops history qfp
    * Added ShowDropsHistoryQfpClear
        * show drops history qfp clear
    * Added ShowPlatformHardwareQfpStatisticsDropHistory
        * show platform hardware qfp {status} statistics drop history
    * Added ShowPlatformHardwareQfpStatisticsDropHistoryClear
        * show platform hardware qfp {status} statistics drop history clear
    * Added ShowFileInformation
        * Added schema and parser for ShowFileInformation

* iosxr
    * Added ShowIsisIpv4Topology
        * Parser for cli 'show isis ipv4 topology'
    * Added ShowRibIpv6Iid
        * parser for 'show rib ipv6 iid all'
    * Added ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummary
        * parser for 'Show Platform Software Fed Switch Active Acl Info Db Summary'

* iosxe showsdwanappqoeadstatistics
    * Added
        * parser for 'show sdwan appqoe ad-statistics'

* iosxe showsdwanappqoedreoptstatistics
    * Added
        * parser for 'show sdwan appqoe dreopt statistics'

* iosxe showsdwanappqoermstatistics
    * Added
        * parser for 'show sdwan appqoe rm-statistics'


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified  ShowPowerInlineModule
        * Modified in the p2 regular expression to match the poe names
    * Modified  ShowIpBgpNeighbors
        * Added New variables in Restricted address families to validate "l2vpn evpn" Neighbor
    * Modified ShowPlatformTcamUtilization Parser
        * Added mode variable
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed Parser
        * Fix p1 regular expression to match port-channel
    * Modified ShowPolicyMapTypeSuperParser Parser
        * Fix p1 regular expression to match port-channel
    * Modified ShowPlatformIfmMapping c9500 Parser
        * Fix p1 regular expression to match IFG_ID, First Serdes, Last Serdes
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser Parser
        * added timeout value to execute command and fix p5 with if condition on the counter
    * Modified ShowDerivedConfigInterface Parser
        * Made violation key as Optional
    * Modified ShowCallHomeProfileAll Parser
        * Fix p7 regex
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpiDetailed Parser
        * Added regex p4_12, p4_13, p4_14, p4_15, p4_16, p4_17, p4_18
    * Modified ShowLldpNeighborsInterfaceDetail Parser
        * Made 'management_addresses' as optional
    * Modified ShowInterfacesTransceiverSchema Parser
        * Added 'max_power' as optional key
    * Modified ShowSwitchStackMode Parser
        * Fix p1 regular expression pattern
    * Added ShowUSB
        * Added schema and parser for ShowUSB
    * Modified ShowPolicyMapInterface
        * Modified qos sets
            * Added cos cos table t1
            * Added traffic-class cos table t1
    * Modified ShowDeviceTrackingCountersVlan
        * Added new dict in the schema for the 'reason' variable with multiple
        * Modified the existing golden_ouputs to match the schema
    * Modified ShowDeviceTrackingDatabase
        * Added 'show device-tracking database vlan {vlan_id}' cli
        * Added New regex for vlan_db_capture
        * Added New variables in Schema and made existing Optional
    * Modified ShowLispEthernetMapCache
        * Added new regex p3_1 for new pattern output,and changed schema as Optional
        * Modified p3 regex to match the output
    * Modified ShowIpMfib
        * Modified p8 regex to match the output
    * Modified show_derived.py
        * Modificiation for show derived-config interface nve1
            * Added regex to handle configuration under nve1
    * Modified show_vrf.py
        * Modificiation for show vrf detail
            * Added regex to handle vnid, vni and core-vlan
    * Modified ShowPlatformHardwareAuthenticationStatus
        * Modified parser for "show platform hardware authentication status"
    * Modified ShowPlatformSoftwareFedIfm
        * Fixed TunnelID range and support for both modular and stack platforms
    * Modified ShowFlowMonitorCache
        * Added additional field fw_fw_event to schema
        * Added regex pattern <p33> to accomodate fw_fw_event outputs
    * Added ShowCableDiagnosticsTdrInt
        * Parser for show cable diagnostics tdr int {interface}
        * modified regex. p1,p2 and p3
    * Modified show l2route evpn multicast smet
        * Fixed issue of wrong index used for cli_command list in cli method of class ShowL2routeEvpnMulticastSmet
    * Added ShowHwProgrammableAll
        * Added schema and parser for ShowHwProgrammableAll
    * Added ShowAuthenticationSessionsDetailsSuper
        * Added <webauth> in p6 regex as Optional
    * Modified ShowLicenseTechSupport as per the output change in latest polaris version.
    * Added the key smartagentcompliancestatus in schema.
    * Modified ShowLogging
        * Local variable 'trap_dict' referenced before assignment
    * Modified ShowAccessSessionMacDetails
        * Modified keys <session_timeout>, <vlan_group>, <acs_acl>, <timeout_action> , <session_timeout> as Optional in the schema.

* asa
    * Fix for ShowVersion parser
        * Updated regex p7

* nxos
    * Fix for ShowModule parser
        * Updated regex for much more tightly controlled matching
    * Modified ShowVpc
        * Updated show vpc parser to include Virtual-peerlink mode status
    * Fix for ShowBgpVrfAllNeighbors parser
        * modify regex to handle new pattern.
    * Fix for ShowInterfaceBrief parser
        * add regex to handle tunnel interfaces

* iosxr
    * Modified ShowRouteIpv6
        * Added pattern <p15> to match 'ffff50.1.1.1, from ffff50.1.1.8'
    * Modified ShowL2vpnBridgeDomainBrief
        * Added p2 and p3 pattern
    * Modified ShowBfdSessionDestination
        * Added Interfaces as key under dest value and moved complete schema which was under dest to interfaces key.
        * Modified async_detection_time_ms as optional parameter under timer_vals in schema.
        * Modified echo_detection_time_ms as optional parameter under timer_vals in schema.
        * Added <p3> to parse the format "No                  n/a             n/a              n/a              UP".
        * Added <p4> to parse the format "BE10                1.1.1.1         n/a              n/a              DOWN".


--------------------------------------------------------------------------------
                                      Add
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformTcamUtilization Parser
        * added 'show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization' for c9500
    * Added ShowInterfaceCountersEtherchannel Parser
        * added 'show interface {interface} counters etherchannel'
    * Added ShowHardwareLed parser
        * Added parser for 'show hardware led' for c9400 switch.


--------------------------------------------------------------------------------
                                    Entries
--------------------------------------------------------------------------------



genie.telemetry
"""""""""""""""""
