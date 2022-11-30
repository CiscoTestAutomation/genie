November 2022
==========

November 28 - Genie v22.11
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.11                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.11                         |
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

* genie.conf
    * Changed default abstraction order to os/platform/model

* genie.harness
    * Add tims_uid mapping to genie trigger class instance



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added warning for removing keys for tftp-boot from next release.git status
    * Added the new clean stage ApplyConfiguration.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Removed the comment from the reload clean stage schema



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

* iosxe - cat9k
    * Ops
        * Added Device Ops for cat9k devices


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* ops
    * Modified Device ops
        * Updated schema to accommodate validation against other parser outputs



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modify unconfigure spanning tree priority API
        * Modify API to accept priority as an optional argument
    * Modified/Fixed configure_ipsec_tunnel to swap tunnel mode ipsec just after configuring tunnel ip address.
    * Modified Ping
        * Added 'extended_data' variable to Ping.
    * Modified/Fixed configure_ip_on_tunnel_interface class to include ipv4.
    * Added configure_hw_switch_switch_logging_onboard_voltage(switch_number)
        * API to configure hw switch logging onboard voltage
    * Added unconfigure_hw_switch_switch_logging_onboard_voltage(switch_number)
        * API to unconfigure hw switch logging onboard voltage
    * Added configure_hw_switch_switch_logging_onboard_environment(switch_number)
        * API to configure hw switch logging onboard environment
    * Added unconfigure_hw_switch_switch_logging_onboard_environment
        * API to unconfigure hw switch logging onboard volenvironmenttage
    * Added configure_hw_switch_switch_logging_onboard_temperature
        * API to configure hw switch logging onboard temperature
    * Added unconfigure_hw_switch_switch_logging_onboard_temperature
        * API to unconfigure hw switch logging onboard temperature
    * Added configure_clear_logging_onboard_switch_temperature
        * API to configure clear logging onboard switch temperature
    * Added configure_clear_logging_onboard_switch_environment
        * API to configure clear logging onboard switch environment
    * Added configure_clear_logging_onboard_switch_voltage
        * API to configure clear logging onboard switch voltage
    * Modified ConfigIpOnInterface
        * New parameter `secondary` in `config_ip_on_interface` to set the IPv4 address as secondary
    * Modified RemoveInterfaceIp
        * New parameter `ip_address`, `mask` and `secondary` in `remove_interface_ip` to remove the secondary IPv4 address
    * Modified configure_dot1x_cred_profile API
        * Changed the command, updated the parameters(added passwd_type)

* blitz
    * Fix for Container->List->Leaf testcase for Gnmi Rpc node grouping
    * Process leaf list value for proto encoding before appending it in opfields
    * Fix for validation of property having list type value.
    * Modify gnmi operations to pass credentials for clear-channel mode.
    * Fix for detecting the start of next stream.
    * Correcting multiple key order in opfield as while converting GetResponse() to dictionary, the key orders are not preserved.
    * Change passing parameter to path_elem_to_xpath() function from decode_update()
    * Fix for opfields appending the json_dicts having lists and dict in it.
    * Set default timeout only for GNMI STREAM mode
    * Fix for verify_opfield returning True with Failed log_msg
    * Fix for gNMI ON_CHANGE subscription.
    * Fix GNMI bytes field parsing

* sdk/powercycler
    * Fixed default auth argument for SNMPv3


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_spanning_tree_vlan_root
        * API for configure spanning-tree vlan root
    * Added unconfigure_spanning_tree_vlan_root
        * API for unconfigure spanning-tree vlan root
    * Added configure_spanning_tree_guard_loop
        * New API to add the spanning-tree guard loop in an interface using the command
    * Added unconfigure_spanning_tree_guard_loop
        * New API to remove the spanning-tree guard loop in an interface using the command
    * Added configure_spanning_tree_bpdufilter
        * New API to add the spanning-tree bpdufilter in an interface using the command
    * Added unconfigure_spanning_tree_bpdufilter
        * New API to remove the spanning-tree bpdufilter in an interface using the command
    * Added clear_ipv6_route and clear_ipv6_route_all
        * clear ipv6 route vrf {<optional> vrf} {route} and clear ipv6 route vrf {<optional> vrf} {route} *
    * Fix clear_arp_cache
        * Fixing clear_arp_cache api to handle more options
    * Added configure_source_template
        * API for configuring template from a source template
    * Added unconfigure_source_template
        * API for unconfiguring template from a source template
    * Added configure_commands_to_template
        * API for adding configurations to a template
    * Added unconfigure_commands_to_template
        * API for removing configurations from a template
    * Added configure_interface_ip_verify_unicast_source
        * API for configuring ip verify unicast source on a interface
    * Added unconfigure_interface_ip_verify_unicast_
        * API for unconfiguring ip verify unicast on a interface
    * Added configure_interface_ipv6_verify_unicast_source
        * API for configuring ipv6 verify unicast source on a interface
    * Added unconfigure_interface_ipv6_verify_unicast_
        * API for unconfiguring ipv6 verify unicast on a interface
    * Added configure_ip_igmp_static_group api
        * Api to configure igmp static group
    * Added configure_ip_igmp_join_group api
        * Api to configure igmp join group
    * Added configure_ip_igmp_ssm_map api
        * Api to configure ip igmp ssm-map
    * Added unconfigure_ip_igmp_ssm_map api
        * Api to unconfigure ip igmp ssm-map
    * Added an api clear_ipv6_dhcp_binding to clear ipv6 dhcp bindings in the server
    * Added verify_spanning_tree_root_inc
        * New API to verify the spanning-tree root inconsistancy states on an interface
    * Added verify_spanning_tree_loop_inc
        * New API to verify the spanning-tree loop inconsistancy states on an interface
    * Added configure_spanning_tree_guard_root
        * New API to add the spanning-tree guard root in an interface
    * Added unconfigure_spanning_tree_guard_root
        * New API to remove the spanning-tree guard root in an interface
    * Added configure_radius_server_accounting_system API
        * API to  configure radius-server accounting system host-config
    * Added configure_service_template_with_inactivity_timer API
        * API to configure service template with inactivity timer
    * Added configure_service_template_with_vlan API
        * API to configure service template with vlan
    * Added configure_service_template_with_access_group API
        * API to configure service template with access group
    * Added configure_class_map_type_match_any API
        * API to configure class-map type control subscriber match-any
    * Added configure_class_map_type_match_none API
        * API to configure class-map type control subscriber match-none
    * Added configure_template_methods_for_dot1x API
        * API to configure template methods for dot1x
    * Added configure_template_methods_using_max_reauth API
        * API to configure template methods using max reauth and timeout
    * Added configure_interface_udld_port
        * API for configure interface udld port
    * Added unconfigure_interface_udld_port
        * API for unconfigure interface udld port
    * Added configure_udld_message_time
        * API for configure udld message time
    * Added unconfigure_udld_message_time
        * API for unconfigure udld message time
    * Added unconfigure_http_client_source_interface api
        * Api to unconfigure http client source interface
    * Added unconfigure_ip_domain_name api
        * Api to unconfigure ip domain name
    * Added configure_ip_http_secure_server api
        * Api to configure http secure-server
    * Added configure_pki_import
        * added to configure pki import
    * Added configure_pki_export
        * added to configure pki export
    * Added change_pki_server_state
        * added to change pki server state.
    * Added dialogue statemenst in configure_pki_enroll
        * added more dialogue statements in configure pki enroll.
    * Added options configure_trustpoint
        * added more options to handle more configs.
    * Added cmd in configure_crypto_pki_server
        * added a cmd for option database_url_storage_location.
    * Added copy_file
        * added api to copy file locally on device.
    * Added configure_cts_aaa_methods
        * API for configure cts aaa methods
    * Added unconfigure_cts_aaa_methods
        * API for unconfigure cts aaa methods
    * Added execute_install_three_step_issu_package
        * Api for executing three step issu package
    * Added configure_interface_ip_verify_unicast_reversepath
        * API for configuring ip verify unicast reverse-path on a interface
    * Added configure_interface_ip_verify_unicast_notification
        * API for configuring ip verify unicast notification on a interface
    * Added configure_interface_ipv6_verify_unicast_reversepath
        * API for configuring ipv6 verify unicast reverse-path on a interface
    * Added unconfigure_commands_to_template
        * API for removing configurations from a template
    * Added request_platform_software_package_clean
        * API for performing request platform software package clean switch on device
    * Added install_autoupgrade
        * API to perform install upgrade on the device
    * Added verify_no_access_session
        * New API to verify if the access-session monitor is present on an interface
    * Added unconfigure_source_template
        * New API to unconfigure the source template on an interface
    * Added configure_ip_igmp_snooping_tcn_flood api
        * Api to configure flood query count
    * Added unconfigure_ip_igmp_snooping_tcn_flood api
        * Api to unconfigure flood query count
    * Added configure_ip_igmp_snooping_last_member_query_interval api
        * Api to configure the IGMP last-member query interval
    * Added unconfigure_ip_igmp_snooping_last_member_query_interval api
        * Api to unconfigure the IGMP last-member query interval
    * Added configure_platform api
        * Api to configure platform license
    * Added configure_license_smart api
        * Api to configure license smart license
    * Added verify_platform_resources API
        * API to verify the platform resources details in the device
    * Added configure_ip_igmp_ssm_map_query_dns api
        * Api to configure ip igmp ssm map query dns
    * Added unconfigure_ip_igmp_ssm_map_query_dns api
        * Api to unconfigure ip igmp ssm map query dns
    * Added configure_stack_power_mode_redundant
        * API to configure mode redundant on stack-power stack
    * Added unconfigure_stack_power_mode_redundant
        * API to unconfigure mode redundant on stack-power stack
    * Added configure_stack_power_default_mode
        * API to configure default mode on stack-power stack
    * Added configure_interface_vlan_standby_ip api
        * API to configure vlan interface standby ip
    * Added configure_interface_vlan_standby_timers api
        * API to configure vlan interface standby timers
    * Added configure_interface_vlan_standby_preempt api
        * API to configure vlan interface standby preempt
    * Added unconfigure_interface_vlan_standby_ip api
        * API to unconfigure vlan interface standby ip
    * Added unconfigure_interface_vlan_standby_timers api
        * API to unconfigure vlan interface standby timers
    * Added unconfigure_interface_vlan_standby_preempt api
        * API to unconfigure vlan interface standby preempt
    * Added configure_ip_domain_timeout api
        * configures the IP domain timeout
    * Added unconfigure_ip_domain_timeout api
        * unconfigures the IP domain timeout
    * Added unconfigure_ip_http_server api
        * unconfigures ip http server
    * Added configure_ip_http_authentication_local api
        * configures ip http authentication local
    * Added unconfigure_ip_http_authentication_local api
        * unconfigures ip http authentication local
    * Added configure_ip_http_secure_server api
        * configures ip http secure-server
    * Added unconfigure_ip_http_secure_server api
        * unconfigures ip http secure-server
    * Added verify_neighbor_count
        * API for verify the neighbor count
    * Added configure_vrf_forwarding_interface
        * API for Creating vrf forwarding on interface
    * Added unconfigure_vrf_forwarding_interface
        * API for Removing vrf forwarding on interface
    * Added unconfigure_call_home api
        * API to unconfigure call-home
    * Added configure_license_smart_usage_interval api
        * API to configure license smart usage interval
    * added api unconfigure_ipv4_dhcp_relay_helper
        * API for unconfiguring ipv4 dhcp helper address in interface
    * addded api unconfigure_ipv6_dhcp_relay
        * API for unconfiguring ipv6 dhcp relay destination in interface
    * Added configure_interface_switchport_block_address
        * API for configure interface switchport block address
    * Added unconfigure_interface_switchport_block_address
        * API for unconfigure interface switchport block address
    * Added configure_interface_logging_event
        * API for configure interface logging event
    * Added unconfigure_interface_logging_event
        * API for unconfigure interface logging event
    * Added license_smart_factory_reset
        * API to clear licensing information from the trusted store and memory
    * Added disable_debug_all
        * API to turn debugging off
    * Added unconfigure_ipv6_mld_snooping_vlan_mrouter_interface
        * API to Unconfigure ipv6 mld snooping vlan mrouter interface
    * Added configure_clear_ipv6_mld_counters
        * API to Configure clear ipv6 mld counters
    * Added configure_ip_igmp_ssm_map_enable
        * API to  Configure ip igmp ssm-map enable
    * Added configure_ip_igmp_snooping_vlan_mrouter_interface
        * API to Configure ip igmp snooping vlan mrouter interface
    * Added configure_debug_ip_pim
        * API to Configure debug ip pim
    * Added configure_ip_igmp_snooping_vlan_static_ipaddr_interface
        * API to Configure ip igmp snooping vlan static ipaddr interface
    * Added configure_ip_igmp_snooping_vlan_mrouter_learn_pim_dvmrp
        * API to Configure ip igmp snooping vlan mrouter learn pim-dvmrp
    * Added configure_spanning_tree_portfast
        * API for configure spanning-tree portfast
    * Added unconfigure_spanning_tree_portfast
        * API for unconfigure spanning-tree portfast
    * Added configure_spanning_tree_uplinkfast
        * API for configure spanning-tree uplinkfast
    * Added unconfigure_spanning_tree_uplinkfast
        * API for unconfigure spanning-tree uplinkfast
    * Added configure_spanning_tree_backbonefast
        * API for configure spanning-tree backbonefast
    * Added unconfigure_spanning_tree_backbonefast
        * API for unconfigure spanning-tree backbonefast
    * Added configure_router_bgp_neighbor_remote_as API
        * API to configure the router bgp neighbor
    * Added configure_router_bgp_network_mask API
        * API to configure the router bgp network mask
    * Added configure_router_bgp_neighbor_ebgp_multihop API
        * API to configure the router bgp neighbor ebgp multihop
    * Added configure_stack_power_switch
        * API to configure stack-power switch
    * Added configure_stack_power_stack
        * API to configure stack-power stack
    * Added unconfigure_stack_power_stack
        * API to unconfigure stack-power stack
    * Added GetInterfaceSecondaryIpv4Address
        * New API `get_interface_secondary_ipv4_address` to retrieve the secondary IPv4 address
    * Added stop_monitor_capture API
        * API for configuring stop monitor capture cli
    * Added configure_virtual_service api
        * Api to configure virtual-service name
    * Added unconfigure_virtual_service api
        * Api to unconfigure virtual-service name
    * Added unconfigure_virtual_service_activate api
        * Api to deactivate virtual-service
    * Added configure_interface_VirtualPortGroup api
        * Api to configure interface VirtualPortGroup
    * Added unconfigure_interface_VirtualPortGroup api
        * Api to unconfigure interface VirtualPortGroup
    * Added get_show_output_exclude
        * API for "Get Show Output Exclude"
    * Added configure_switchport_dot1q_ethertype and unconfigure_switchport_dot1q_ethertype
        * API for configuring switchport dot1q ethertype and no switchport dot1q ethertype
    * Added configure_spanning_tree_mst_configuration
        * API for to add the spanning tree mst configuration
    * Added unconfigure_spanning_tree_mst_configuration
        * API for unconfigure the spanning tree mst configuration
    * Added configure_eui_64_over_ipv6_enabled_interface API
        * API to Configure eui-64 over ipv6 enabled interface
    * Added unconfigure_eui_64_over_ipv6_enabled_interface API
        * API to UnConfigure eui-64 over ipv6 enabled interface
    * Added configure_ipv6_nd_dad_processing API
        * API to Configure ipv6 nd dad processing
    * Added unconfigure_ipv6_nd_dad_processing API
        * API to UnConfigure ipv6 nd dad processing
    * Added configure_service_policy API
        * Added configure_service_policy API
    * Added configure_interface_switchport_port_security_violation API
        * Added configure_interface_switchport_port_security_violation API
    * Added unconfigure_interface_switchport_port_security_violation API
        * Added unconfigure_interface_switchport_port_security_violation API
    * Added configure_interface_dot1x_timeout_txp API
        * Added configure_interface_dot1x_timeout_txp API
    * Added unconfigure_interface_dot1x_timeout_txp API
        * Added unconfigure_interface_dot1x_timeout_txp API
    * Added configure_interface_dot1x_max_req API
        * Added configure_interface_dot1x_max_req API
    * Added unconfigure_interface_dot1x_max_req API
        * Added unconfigure_interface_dot1x_max_req API
    * Added configure_interface_dot1x_max_reauth_req API
        * Added configure_interface_dot1x_max_reauth_req API
    * Added unconfigure_interface_dot1x_max_reauth_req API
        * Added unconfigure_interface_dot1x_max_reauth_req API
    * Added configure_interface_dot1x_eap_profile API
        * Added configure_interface_dot1x_eap_profile API
    * Added unconfigure_interface_dot1x_eap_profile API
        * Added unconfigure_interface_dot1x_eap_profile API
    * Added configure_interface_dot1x_auth_vlan API
        * Added configure_interface_dot1x_auth_vlan API
    * Added unconfigure_interface_dot1x_auth_vlan API
        * Added unconfigure_interface_dot1x_auth_vlan API
    * Added configure_interface_dot1x_auth_vlan_no_resp API
        * Added configure_interface_dot1x_auth_vlan_no_resp API
    * Added unconfigure_interface_dot1x_auth_vlan_no_resp API
        * Added unconfigure_interface_dot1x_auth_vlan_no_resp API
    * Added unconfigure_ip_route_cache API
        * API to unconfigure ip route-cache on interface
    * Added configure_scale_ipv6_accesslist_config API
        * API to configure acls under ipv6 access-list
    * Added configure_aaa_authentication_login API
        * API to configure aaa authentication login
    * Added configure_aaa_default_group_methods API
        * API to configure aaa default group methods
    * Added configure_aaa_authorization_exec_default API
        * API to configure aaa authorization exec default
    * Added configure_aaa_accounting_update_periodic API
        * API to configuring aaa accounting update newinfo periodic
    * Added configure_aaa_accounting_identity_default_start_stop API
        * API to configure aaa accounting identity default start-stop
    * Added configure_radius_attribute_8 API
        * API to configure radius-server attribute 8 include-in-access-req
    * Added configure_radius_attribute_25 API
        * API to configure radius-server attribute 25 access-request include
    * Added configure_radius_attribute_31_mac_format API
        * API to configure radius-server attribute 31 mac format ietf upper-case
    * Added configure_radius_attribute_31_send_mac API
        * API to configure radius-server attribute 31 send nas-port-detail mac-only
    * Added unconfigure_subinterface API
        * API to unconfigure subinterface
    * Modified config_ip_on_interface API
        * Modified API to configure ipv6 link-local address
    * Added configure_license_smart_transport_cslu api
        * Api to configure license smart transport cslu type
    * Added unconfigure_license_smart_transport api
        * Api to unconfigure license smart transport type
    * Added configure_license_smart_url_cslu api
        * Api to configure license smart url to cslu type
    * Added unconfigure_license_smart_url_cslu api
        * Api to unconfigure license smart url from cslu type
    * Added configure_line_console api
        * Api to configure line console on a line

* blitz
    * Added support for gnmi 0.8
    * Added proto folder containing protofiles, protomodels and script to generate models from protofile


--------------------------------------------------------------------------------
                                       ~                                        
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_fnf_exporter API
        * Corrected the source_int parameter



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowPceIPV4PeerDetail
        * Added Instantiation option for Capabiities to schema as Optional.
        * Added MD5 option to schema as Optional.
        * Added Maximum SID depth option to schema as Optional.
        * Added Last pcerror option to schema as Optional.
    * Modified ShowIsisInterface
        * Added Total bandwidth as Optional parameter to schema.
        * Added Delay normalization as Optional parameter to schema.
        * Added Interval and Offset options in delay normalization to schema.
        * Added Link loss as Optional parameter to schema.
        * Added Metric fallback as Optional parameter to schema.
        * Added Bandwidth and Anomaly options in metric fallback to schema.
        * Modified Adjacency formation, State, Prefix advertisement, Metric, Weight and Mpls as Optional under topology in schema.
        * Added Status option in Ldp sync as Optional parameter to schema.
        * Modified Forwarding address, Global prefix as Optional under address_family in schema.
        * Added <r56> to parse the optional line with the format "LDPv4 Sync Status    Achieved".
        * Added <r57> to parse the optional line with the format "Total bandwidth                1000000".
        * Added <r58> to parse the optional line with the format "Metric fallback".
        * Added <r59> to parse the optional line with the format "Bandwidth (L1/L2)    Inactive/Inactive".
        * Added <r60> to parse the optional line with the format "Anomaly (L1/L2)    Inactive/Inactive".
        * Added <r61> to parse the optional line with the format "Delay Normalization      Interval0 Offset0".
        * Added <r62> to parse the optional line with the format "Link Loss                1".

* iosxe
    * Modified ShowLispAR
        * changed the regular expression P2 to match any type of ipv6 address
    * Modified ShowDeviceTrackingDatabaseDetails
        * Enhanced the regex to match "time_left" with format "224 s(7177 s)"
    * Modified Ping
        * Added 'extended_data' variable to Ping.
    * Modified ShowIpProtocols
        * Fixed to capture ISIS enabled interfaces properly
    * Modified ShowIpv6Protocols
        * Fixed to capture ISIS enabled interfaces properly
    * Modified ShowCryptoIkev2Stats Added Quantum resistance line to parser.
    * Modified ShowInventoryRaw
        * changed the regular expression P1 to work Temp values.
    * Modified ShowIpOspf
        * Updated regex p12_4 to match warning-only
        * Update regex p33 to match warning-only
    * Modified ShowCdpNeighbors parser
        * Added a new command "show cdp neighbors {interface}" in the existing schema.
    * Modified ShowSwitch
        * Made hw_ver parameter as optional to support some of the outputs witout hw_ver.
    * Modified ShowVersion
        * Added system_fpga_version parameter as optional to support some of the outputs with System FPGA Version.
    * Modified ShowHardwareLed
        * modified code to match code for not having SWITCH match or non stack devices, also for IE3x00 devices
    * Modified ShowIdpromInterface.
    * Added the parser in the proper file show_idprom.py.

* nxos
    * Modified ShowIpv6MrouteVrfAll
        * Updated regex pattern p5_1  to accommodate bridge only outputs as well.
        * Moved the regex patterns outside of the for loop so that they will
    * Modified ShowRouting
        * Updated regex pattern to match nextop line attr "tunnelid" to match hex properly [0-9a-fA-Fx].
        * Updated regex pattern to match nextop line attr "segid" to only optionally match colon.
    * Modified ShowBgpSessions
        * Added regexes p7_1 and p7_2 in order to correctly parse the outputs where there is a line break due to large AS numbers
    * Modified ShowBgpVrfAllAll
        * Reordered <p3_4> to match after <p3_1>, <p3_2>, and <p3_3> to avoid matching nexthop when a network is the only value on the line.

* cheetah
    * Modified show_capwap_client_rcb
        * Modified capwap image download, hyperlocation options to schema as Optional.

* deleted the duplicate parser under iosxe/show_platform.py and iosxe/c9300/show_platform.py.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowIpArpInspectionInterfaces
        * show ip arp inspection interfaces {interface}
    * Added ShowTemplateBrief
        * show template brief
    * Added ShowSwitchStackRingSpeed
        * Parser for show switch stack-ring speed
    * Added ShowPlatformMatmMacTable Parser
        * Parser for "show platform hardware fed switch active matm macTable"
    * Added ShowOspfv3Gracefulrestart
        * added new parser for cli "show ospfv3 {pid} graceful-restart"
    * Added ShowOspfv3FloodList
        * added new parser for cli "show ospfv3 {pid} flood-list"
    * Added ShowOspfv3Events
        * added new parser for cli "show ospfv3 {pid} events"
    * Added ShowOspfv3Neighbor
        * show ospfv3 {pid} neighbor
    * Added ShowOspfv3RetransmissionList
        * show ospfv3 {pid} retransmission-list
    * Added ShowOspfv3RequestList
        * show ospfv3 {pid} request-list
    * Added ShowSdwanAppFwdDpiFlows
        * show sdwan app-fwd dpi flows parser
    * Fixed ShowSdwanAppfwdCflowdStatistics
        * Whole method was under "if output" statement - fixed it
    * Added ShowVlanDot1qTagNative
        * show vlan dot1q tag native
    * Added ShowCefInterfaceVlanBrief
        * show cef interface Vlan {id} brief
    * Added ShowCefInterfacePolicyStatistics
        * Parser for show cef interface policy-statistics
    * Added ShowEnvironmentStack
        * show environment stack
    * Added ShowCableDiagnosticsTdrInt
        * show cable-diagnostics tdr interface {interface}
    * Added ShowSnmpEngineid
        * Parsef for show snmp engineid
    * Added ShowSnmpCommunity
        * Parsef for show snmp community
    * Added ShowSnmpMibBulkstatTransfer
        * Parsef for show snmp mib bulkstat transfer
    * Added ShowLicenseHistoryMessage
        * show license history message
    * Added ShowSdwanUtdDataplaneConfig
        * show sdwan utd dataplane config
    * Added ShowPlatformHardwareFedSwitchStateFwdAsicAbstractionPrintResourceHandleClient_le parser
        * Added ShowPlatformHardwareFedSwitchStateFwdAsicAbstractionPrintResourceHandleClient_le parser
    * Added ShowIpOspfNsr
        * added new parser for cli 'show ip ospf nsr'
    * Added ShowInterfacesTransceiverSupportedlist
        * Parser for show interfaces transceiver supported-list
    * Added ShowIpArpInspectionStatisticsVlan
        * show ip arp inspection statistics vlan {num}
    * Added ShowTemplateInterfaceSourceBuiltInOriginalAll Parser
        * Parser for "show template interface source built-in Original all"
    * Added ShowlldpErrors
        * added new parser for cli "show lldp errors"
    * Modified ShowBoot and ShowBootSystem
        * Modified regexp of boot mode in ShowBoot parser to display boot mode other then 'device'.
        * Modified regexp of boot mode and boot variable in ShowBootSystem parser.
    * Added ShowIpv6MldSnoopingVlan
        * show ipv6 mld snooping vlan
    * Added ShowIpv6MldSnoopingMrouter
        * show ipv6 mld snooping mrouter
    * Added ShowSpanningTreeInterfaceDetail
        * Parser for "show spanning-tree interface detail"
    * Added ShowSpanningTreeInterface
        * Parser for "show spanning-tree interface"
    * Added ShowSpanningTreeInconsistentports
        * Parser for "show spanning-tree inconsistentports"
    * Added ShowOspfv3Interface
        * show ospfv3 {pid} interface
    * Added ShowMacroAutoDevice Parser
        * Parser for "show macro auto device"
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Node
        * show platform software node cluster-manager switch {mode} B0 node {node}
    * Added ShowPlatformSoftwareFedStateVpSummaryInterfaceIf_id parser
        * Added ShowPlatformSoftwareFedStateVpSummaryInterfaceIf_id parser
    * Added ShowIpCefSummary
        * Parser for show ip cef summary
    * Added ShowPlatformRewriteUtilization
        * parser for chec the rewrite utilization
    * Added ShowAdjacencySummary
        * parser for show adjacency summary
    * Added ShowOspfv3
        * show ospfv3
        * show ospfv3 vrf {vrf_id}
    * Added ShowOspfv3DatabaseSummaryDetail
        * show ospfv3 database database-summary detail
        * show ospfv3 {process_id} database database-summary detail
    * Added ShowRunSectionOspfv3
        * show running-config | section ospfv3
    * Added ShowPmVpInterfaceVlan parser
        * Added ShowPmVpInterfaceVlan parser
    * Added ShowMacAddressTableCount
        * show mac address-table count
    * Added ShowOspfv3StatisticDetail
        * New parser for "show ospfv3 {pid} statistic detail"
    * Added ShowInstallCommitted
        * show install committed
    * Added ShowLoggingOnboardSwitchClilog parser
        * for 'Show logging onboard switch {switch} clilog'
    * Added ShowLoggingOnboardSwitchActiveStatus parser
        * for 'show logging onboard switch active status'
    * Added ShowLoggingOnboardSwitchActiveUptimeDetail parser
        * for 'show logging onboard switch active uptime detail'
    * Added ShowLoggingOnboardSwitchContinuous parser
        * for 'show logging onboard switch {switch_num} {include} continuous'
    * Added ShowPlatformPmPortDataInt parser
        * Added ShowPlatformPmPortDataInt parser
    * Added ShowMacAddressTableCountVlan
        * Parser for show mac address space
    * Added ShowIpDnsView
        * show ip dns view parser
    * Added ShowAccessSessionsInfo
        * show access-session info
    * Added ShowAaaDeadCriteriaRadius Parser
        * Parser for "show aaa dead-criteria radius"
    * Added ShowCdpTraffic Parser
        * Parser for "show cdp traffic"
    * Added ShowCdpInterface Parser
        * Parsre for "show cdp interface"
    * Added ShowCdpEntry Parser
        * Parser for "show cdp entry"
    * Added ShowCefInterface Parser
        * Parser for "show cef interface {interface}"
    * Added ShowCefInterfaceInternal Parser
        * Parser for "show cef interface {interface} internal"
    * Added parser
        * Added ShowIpAdmissionCache parser
    * Added parser
        * Added ShowAccessSessionEventLoggingMac parser
    * Added ShowAaaSessions parser
        * Added ShowAaaSessions parser
    * Added ShowDot1xStatistics parser
        * Added ShowDot1xStatistics parser
    * Added ShowAaaMemory parser
        * Added ShowAaaMemory parser
    * Added ShowPlatformSoftwareWiredClientSwitchR0 parser
        * Added ShowPlatformSoftwareWiredClientSwitchR0 parser
    * Added ShowPlatformAuthenticationSbinfoInterface parser
        * Added ShowPlatformAuthenticationSbinfoInterface parser
    * Added ShowPlatformHostAccessTableIntf parser
        * Added ShowPlatformHostAccessTableIntf parser
    * Added ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id parser
        * Added ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id parser

* added showiparpinspectionlog
    * show ip arp inspection log

* iosxr
    * Modified ShowRcmdIsisEventSpf
        * show rcmd isis {isis} event spf {spf_run_no}
    * Modified ShowRcmdIsisEventPrefix
        * show rcmd isis {isis} event prefix {prefix_name}
    * Added ShowRcmdIsisEventPrefixLastDetail
        * show rcmd isis {isis} event prefix {prefix_name} last {event_no} detail
        * show rcmd isis {isis} event prefix {prefix_name} detail
    * Added ShowRcmdIsisEventSpfLastDetail
        * show rcmd isis {isis} event spf last {event_no} detail
        * show rcmd isis {isis} event spf {spf_run_no} detail
    * Added ShowRcmdProcess
        * show rcmd process
    * Added ShowRcmdInterfaceEvent
        * show rcmd interface event

* show access-session info switch {switch} r0


