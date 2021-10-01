September 2021
==========

September 29 - Genie v21.9 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.9                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.9                          |
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

* genie.json.make_json
    * Modified MakeClean
        * To support picking up class based clean stages

* harness
    * Fixed a bug in the check_config subsection where using the device alias would cause an exception to be raised.
    * Fixed an issue where the section processors would not be cleared if the same trigger was ran more than once

* json
    * Modified MakeAPIs
        * raise custom ApiImportError exception if APIs are extended to include a module that has an error in it


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* conf
    * Modified API
        * Added telemetry data collection within get_api()

* harness
    * Modified GenieTrigger
        * Added telemetry data collection within __call__()

* genieparser
    * Added option to log a warning when unsupported keys are found by the schema validation
    * Added `warn_unsupported_keys` to parse() command,
    * Added `GENIEPARSER_WARN_UNSUPPORTED_KEYS` environment variable as alternative for the `warn_unsupported_keys` argument.



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* all
    * Modified copy_to_device
        * copy_to_device stage now supports arguments unique_file_name, unique_number, and rename_images

* iosxr
    * Updated `install_image_and_packages` clean stage to install packages with local file path
    * Added `source_directory` option for `install_image_and_packages` clean stage

* utils clean
    * Modified remove_string_from_image
        * Added condition to check unwanted removal of string from image path.

* iosxe
    * Modified install_image stage
        * changed the error_pattern['Failed'] to append_error_pattern['Failed']

* modified imageloader & imagehandler
    * added support for arbitrary extra files under the extra attribute


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added execute_delete_boot_variable
        * added the execute_delete_boot_variable api for nxos n3k

* viptela(sd-wan controllers)
    * Added pyATS Clean support for SD-WAN Controllers (vManage/vBond/vSmart)

* all
    * Modified CleanTestcase
        * Added telemetry data collection within __iter__()

* iosxe/sdwan (cedge devices)
    * Added pyATS Clean support for IOSXE/SDWAN cEdge devices

* iosxe
    * Added tftp_boot stage for cat9k

* major infrastructure overhaul
    * Clean stages have been converted from a function into a class which provides the following benefits
        * **Class inheritance** - Prevents duplicated code, duplicated work, and duplicated bugs due to copy and pasting existing code to make a small modification.
        * **Tests** - With class based stages, each step in the stage is it's own method. This provides the ability to mock up and test small steps of a stage to get complete code coverage. In turn better unittest means less bugs.
        * **Execute clean stages within scripts** - Due to the redesign it is possible to execute clean stages within your scripts (Highly asked for)! In the near future we will release an easy-to-use method for calling these stages (similar to device.api).
        * **100% backwards compatible** - From a user point of view, the clean yaml file and usage is still the exact same. Nothing changes from a user point of view as we do not want to break anyone.
    * Soon to come
        * Method to easily execute clean stages within a script
        * New developer documentation



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Modified Vxlan
        * Added new attribute "split-horizon per-site" under Evpn Msite BGW Attributes
        * This is needed to support multisite multicast underlay



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* http fileserver
    * Added support for mime/multipart file uploads (used by NXOS)



genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* all
    * Modified HealthCheckPlugin
        * Added telemetry data collection within pre_task()


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health plugin
    * Fixed pyats_health.yaml in archive as reusable

* health
    * Fixed section result handling in case no item in Section



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
    * Added API 'source_configured_template'
    * Added API 'configure_dot1x_cred_profile'
    * Added API 'configure_eap_profile_md5'
    * Added API 'configure_dot1x_supplicant'
    * Added API 'configure_mode_to_eEdge'
    * Added API 'enable_autoconf'
    * Added API 'configure_access_session_monitor'
    * Added API 'configure_access_session_sticky'
    * Added API 'enable_dot1x_sysauthcontrol'
    * Added API 'clear_access_session'
    * Added API 'config_identity_ibns'
    * Added attach_dhcpv6_guard_policy_to_vlan API
        * Attaches DHCPv6 guard policy to a vlan
    * Added detach_dhcpv6_guard_policy_vlan API
        * Detaches DHCPv6 guard policy from a vlan
    * Added attach_device_tracking_policy_to_interface API
        * Attaches device tracking policy to an interface
    * Added configure_authentication_parameters_interface
        * Configures authentication parameters on interface
    * Added authentication_convert_to_new_style API
        * Configures new style authentication
    * Added API `configure_ptp_modes'
    * Added API `configure_ptp_transport_ipv4'
    * Added API `configure_ptp_domain'
    * Added API `configure_ptp_priority'
    * Added API `configure_switchport_trunk'
    * Added API `configure_svi'
    * Added API `configure_ptp_dscp_message'
    * Added API `unconfigure_ptp_dscp_message'
    * Added API `unconfigure_svi'
    * Added API 'unconfigure_ptp_modes'
    * Added API 'configure_ptp_aes67_rates'
    * Added API 'unconfigure_ptp_transport_ipv4'
    * Added API 'unconfigure_ptp_domain'
    * Added API 'verify_ptp_states'
    * Added API 'verify_ptp_platform_fed_results'
    * Added API 'verify_ptp_clock'
    * Added API 'verify_ptp_counters'
    * Added API 'verify_ptp_parent'
    * Added API 'verify_ptp_calibration_states'
    * Added API 'unconfig_vlan'
    * Added TriggerClearIpv4BGPSoft
        * Trigger to soft clear for IPv4 BGP session using ```clear ip bgp * soft``` command
    * Added TriggerClearIpv4BGPHard
        * Trigger to hard clear for IPv4 BGP session using ```clear ip bgp *``` command
    * Added TriggerUnconfigConfigPortChannelInterface
        * Trigger to unconfigure and reconfigure Port-channel interfaces on IOSXE devices
    * Added TriggerUnconfigConfigBridgeDomainInterface
        * Trigger to unconfigure and reconfigure Port-channel interfaces on IOSXE devices
    * Added API configure_radius_attribute_6(device)
    * Added API unconfigure_radius_attribute_6(device)
    * Added API configure_any_radius_server(device, server_name, addr_type, address, authport, acctport, secret)
    * Added API unconfigure_any_radius_server(device, server_name)
    * Added API configure_radius_server_group(device, servergrp, rad_server)
    * Added API unconfigure_radius_server_group(device, servergrp)
    * Added API configure_aaa_new_model(device)
    * Added API configure_aaa_default_dot1x_methods(device,server_grp,group_type='group',group_type2='',server_grp2='')
    * Added API unconfigure_aaa_default_dot1x_methods(device)
    * Added API configure_aaa_login_method_none(device,servergrp)
    * Added API unconfigure_aaa_login_method_none(device,servergrp)
    * Added API configure_wired_radius_attribute_44(device)
    * Added API unconfigure_wired_radius_attribute_44(device)
    * Added API configure_radius_interface(device, interface)
    * Added API unconfigure_radius_interface(device, interface)
    * Added API get_running_config_section_attr44(device, option)
    * Added API verify_test_aaa_cmd(device, servergrp, username, password, path)
    * Added API configure_interface_switchport_voice_vlan(device, interface, vlan)
    * Added API unconfigure_dot1x_supplicant(device, profile_name, intf, eap_profile='')
    * Added API unconfigure_dot1x_system_auth_control(device)
    * Added API configure_authentication_host_mode(device,mode,intf,style='legacy')
    * Added API unconfigure_authentication_host_mode(device,mode,intf,style='legacy')
    * Added API configure_authentication_order(device,order,intf)
    * Added API unconfigure_authentication_order(device,order,intf)
    * Added API configure_authentication_priority(device,priority,intf)
    * Added API unconfigure_authentication_priority(device,priority,intf)
    * Added API configure_authentication_port_control(device,control,intf,style='legacy')
    * Added API unconfigure_authentication_port_control(device,control,intf,style='legacy')
    * Added API configure_authentication_periodic(device,intf)
    * Added API unconfigure_authentication_periodic(device,intf)
    * Added API configure_authentication_timer_reauth(device,value,intf)
    * Added API unconfigure_authentication_timer_reauth(device,value,intf)
    * Added API configure_auth_method(device,value,intf)
    * Added API unconfigure_auth_method(device,value,intf)
    * Added API 'configure_ip_on_tunnel_interface'
        * conigure ip address on tunnel interface
    * Added API 'unconfigure_tunnel_interface'
        * unconfigure tunnel interface
    * Added API 'configure_route_map_under_interface'
        * configure route-map under interface
    * Added API 'unconfigure_route_map_under_interface'
        * unconfigure route-map under interface
    * Added API 'configure_route_map'
        * configure route-map
    * Added API 'unconfigure_route_map'
        * unconfigure route-map
    * Added API 'unconfigure_acl'
        * unconfigure acl
    * Added API 'unconfigure_ace'
        * unconfigure ace
    * Added API 'verify_acl_usage'
        * verify acl usage
    * Added API 'verify_route_map'
        * verify route-map
    * Added API 'verify_tunnel_status'
        * verify tunnel status
    * Added API 'verify_tunnel_stats'
        * verify tunnel statistics
    * Added API clear_aaa_cache(device, server_grp, profile='all')
    * Added API configure_username(device, username, pwd, encryption=0)
    * Added API unconfigure_username(device, username)
    * Added API configure_radius_automate_tester(device, server_name, username, idle_time=None)
    * Added API unconfigure_radius_automate_tester(device, server_name, username)
    * Added API configure_eap_profile(device, profile_name,method='md5')
    * Added API unconfigure_eap_profile(device, profile_name)
    * added `configure_device_tracking_binding` API
    * added `configure_ipv6_destination_guard_attach_policy` API
    * added `configure_ipv6_destination_guard_detach_policy` API
    * added `configure_ipv6_destination_guard_policy` API
    * added `unconfigure_ipv6_destination_guard_policy` API
    * added `configure_device_tracking_tracking` API
    * Added API `configure_cts_authorization_list'
    * Added API `enable_cts_enforcement'
    * Added API `enable_cts_enforcement_vlan'
    * Added API `configure_device_sgt'
    * Added API `configure_vlan_to_sgt_mapping'
    * Added API `configure_ipv4_to_sgt_mapping'
    * Added API `configure_ipv4_subnet_to_sgt_mapping'
    * Added API `assign_static_ipv4_sgacl'
    * Added API `assign_default_ipv4_sgacl'
    * Added API 'configure_cts_credentials'
    * Added API 'configure_pac_key'
    * Added API 'configure_port_sgt'
    * Added new trigger 'TriggerUnconfigConfigBgpVpnRd'
    * Added configure_global_stackwise_virtual API
        * Configures global SVL and domain
    * Added unconfigure_global_stackwise_virtual API
        * Removes global SVL
    * Added configure_stackwise_virtual_interfaces API
        * Attaches interfaces to SVL
    * Added unconfigure_stackwise_virtual_interfaces
        * Removes interfaces from SVL
    * Added API 'disable_dhcp_snooping'
    * Added API 'unconfigure_cts_authorization_list'
    * Added API 'disable_cts_enforcement'
    * Added API 'disable_cts_enforcement_vlan'
    * Added API 'unconfigure_ipv4_to_sgt_mapping'
    * Added API 'remove_static_ipv4_sgacl'
    * Added API 'remove_default_ipv4_sgacl'
    * Added API 'clear_cts_credentials'
    * Added API 'clear_cts_counters'
    * Added API 'unconfigure_ipv4_subnet_to_sgt_mapping'
    * Added configure_errdisable API
        * Configures error disable
    * Added unconfigure_errdisable API
        * Removes error disable
    * Added configure_template API
        * Configures template
    * Added unconfigure_template
        * Removes template
    * Added configure_spanning_tree API
        * Configures spanning tree
    * Added unconfigure_spanning_tree API
        * Removes spanning tree
    * Added configure_interface_template API
        * Attaches template to an interface
    * Added unconfigure_interface_template
        * Removes templates from an interface
    * Added execute_clear_logging
        * Executes clear logging

* nxos/aci
    * Added `verify_file_exists` and `delete_files` APIs

* api utils
    * Added API Unit Test Generator
        * Added module that is capable of connecting to a device and automatically


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified TriggerReload
        * Changed TriggerReload from NotImplemented to complete implementation of node reload.
    * Modified `get_show_tech` API, improved exception handling
    * Modified configure_radius_group API
    * Modified API configure_dot1x_supplicant(device, interface, cred_profile_name, eap_profile='')
    * Modified RouteOutput
        * Updated template for routeOpsOutput_vrf1 and routeOpsOutput for ipv6 routes since the parser logic was incorrect.
    * Modified config_extended_acl
        * new condition is added to configure acl with using only host keyword.
    * Modified config_identity_ibns
        * Added port_control as an arg, and made 'auto' the default
    * Modified configure_authentication_host_mode
        * Added spaces between args for readability
    * Modified API execute_card_OIR(device, card_number, timeout=60)

* iosxr
    * Modified `get_show_tech` API, improved exception handling

* nxos
    * Modified `get_show_tech` API, improved exception handling
    * Modified
        * Issu trigger can now handle invalid boot mode command on unsupported platforms/images.

* aci
    * Modified `get_show_tech` API, improved exception handling

* mapping
    * Added logging to show Ops structure when Mapping errors out


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Added configure_fnf_exporter API
        * Configures Flow exporter
    * Added unconfigure_flow_exporter_monitor_record API
        * Unconfigures the Flow exporter, monitor and record
    * Added configure_fnf_monitor_on_interface API
        * Configures the interface with the flow monitor
    * Added configure_flow_record API
        * Configures Flow record
    * Added configure_flow_monitor API
        * Configures Flow monitor
    * Added unconfigure_fnf_monitor_on_interface API
        * Unconfigures flow monitor from interface
    * Added set_filter_packet_capture_inject API
        * Sets filter for packet capture inject
    * Added start_packet_capture_inject API
        * Starts packet capture inject
    * Added stop_packet_capture_inject API
        * Stops packet capture inject API

* added unconfigure_vlan_interface api
    * Unconfigures vlan interface



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn to support
        * show platform software fed switch active ifm mappings lpn
        * show platform software fed switch active ifm mappings lpn {interface}
    * Added ShowPlatformSoftwareFedSwitchActivePtpDomain to support
        * show platform software fed switch active ptp domain
    * Added ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface to support
        * show platform software fed switch active ptp Interface {interface}
    * Added ShowPlatformSoftwareFedActiveAclUsage to support
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    * Modified ShowBgpDetailSuperParser
        * Fixed p3_3 match logic to allow multicast src to be * when the multicast src len is 0.
    * Modified ShowMplsTrafficEngTunnelBrief
        * Moved to 'show_mpls.py'
    * Modified ShowMplsTrafficEngTunnelTunnelid
        * Moved to 'show_mpls.py'
    * Modified ShowMplsTrafficEngTunnel
        * Moved to 'show_mpls.py'
    * Modified ShowBgpDetailSuperParser
        * Fixed p2 to allow for cases in show output that have same tableids in different locations.
    * Modified ShowAuthenticationSessionsInterfaceDetails
        * show authentication sessions interface {interface} details switch {switch} r0
    * Modified ShowSegmentRoutingTrafficEngPolicy
        * Fixed regex, added unit tests, and added to the schema
    * Modified ShowinterfacesStatus to support
        * show interfaces {interface} status
    * Added ShowPlatformSoftwareDpidIndex
        * show platform software dpidb index
    * Added ShowMplsTrafficEngTunnelBrief
        * Added ShowMplsTrafficEngTunnelBrief in IOSXE c9400 folder
        * Add folder based unittests
    * Modified ShowEnvironmentAll
        * subclass of ShowEnvironmentSuperParser
    * Modified ShowPlatformSoftwareFedActiveAclUsage to support
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    * Modified ShowIpRouteSummary
        * Added parsing support for devices that don't record 'Replicates' in the routing table
    * Modified ShowRouteMapAll to support
        * show route-map {name}
    * Modified ShowLicenseSummary
        * Updtaed regex pattern for <license> capturing group to accommodate various outputs
    * Modified ShowRomVarSchema
        * Changed mcp_startup_traceflags field to Optional
    * Modified ShowRomVar
        * Added other  keyword CRYPTO_BI_THPUT for thrput parameter
    * Modified ShowVersion
        * Fixed regex for capturing correct build_label, added unit tests,
    * Modified ShowIpv6Route
        * Fixed p6 match logic to allow % in case of leaked route in current vrf table.
    * Modified ShowIpRoute
        * Fixed p3 match logic for Ipv6 and Ipv6 to properly parse code 1 (in cases such as replicated routes or additional codes). Ipv6 routes now properly parsed as well
    * Modified ShowMonitor
        * Made the status key optional.
    * Modified ShowMplsForwardingTable
        * Fixed code logic
    * Modified  ShowLicenseSummary
        * modified regex pattern to support other types of licenses
    * Modified ShowStackPower
        * Modified multiple schema keys to accept either float or int data types
    * Added ShowStackPowerBudgeting
        * show stack-power budgeting
    * Modified ShowL2routeEvpnMacIp
        * Updated logic for the order of specific filter use
        * Added show l2route evpn mac ip host-ip {ip}
        * Updated Schemas in show_l2route.py to use evi, mac addr and etag as keys
        * Added support to all allow all classes in show_l2route to support multiple next hops
        * Updated function arguments to allow evi and etag to be passed in as one argument, evi_etag
        * Added support for long ipv6 addresses for all show_l2route parsers
        * Added and updated tests
    * Modified ShowL2routeEvpnMacIpDetail
        * Added and updated tests
        * Updated Schemas to use evi, mac addr and etag as keys. NOT BACKWARDS COMPATIBLE.
        * Updated function arguments to allow evi and etag to be passed in as one argument, evi_etag
            * show l2route evpn mac ip topology <evi_etag> detail
            * Updated logic for the specific filter use
    * Modified ShowL2routeEvpnImetDetail
        * Added and updated tests
        * Updated function arguments to allow evi and etag to be passed in as one argument, evi_etag
            * show l2route evpn imet topology {evi_etag} detail
            * Updated logic for the specific filter use
        * Updated Schemas to use evi, mac addr and etag as keys. NOT BACKWARDS COMPATIBLE.
    * Modified ShowBgpNeighborsReceivedRoutesSuperParser
        * Made neighbor_id and original_address_family have default values in parser class
    * Modified ShowDeviceTrackingPolicies
        * Removed a misplaced empty dictionary test from cli/equal test folder (raised SchemaEmptyParserError)
    * Added ShowPtpBrief to support
        * show ptp brief
        * show ptp brief | exclude {ptp_state}
    * Added ShowPtpClock to support
        * show ptp clock
    * Added ShowPtpParent to support
        * show ptp parent
    * Added ShowPtpPortInterface to support
        * show ptp port {interface}
    * Added new parser for 'show run all | sec {interface}'
    * Modified ShowBoot
        * Added regex to accommodate resolve corner case
    * Modified ShowL2vpnEvpnMac
        * changed schema to support vary outputs
            * added evi, eth_tag and bd_id as key
        * updated test cases
        * added cli filter and tests for vlan_id
            * show l2vpn evpn mac vlan {vlan_id}
            * show l2vpn evpn mac vlan {vlan_id} address {mac_addr}
            * show l2vpn evpn mac vlan {vlan_id} duplicate
            * show l2vpn evpn mac vlan {vlan_id} local
            * show l2vpn evpn mac vlan {vlan_id} remote
    * Modified ShowL2vpnEvpnMacIp
        * changed schema
            * added evi, mac_addr and bd_id as key
        * updated test cases
        * added cli filter and tests for vlan_id
            * show l2vpn evpn mac ip vlan {vlan_id}
            * show l2vpn evpn mac ip vlan {vlan_id} address {ipv4_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} address {ipv6_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} duplicate
            * show l2vpn evpn mac ip vlan {vlan_id} local
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv4_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv6_addr}
            * show l2vpn evpn mac ip vlan {vlan_id} remote
    * Modified ShowL2vpnEvpnMacDetail
        * changed schema
            * added evi, eth_tag, mac_addr and bd_id as key
        * updated test cases
    * Modified ShowL2vpnEvpnMacIpDetail
        * changed schema
            * added evi, mac_addr, eth_tag and bd_id as key
        * updated test cases
    * Modified ShowL2fibPathListId
        * changed schema key 'path_ids' to 'pathlist_id'
        * updated tests
    * Modified ShowL2routeEvpnImetDetail
        * updated regex logic
        * updated testcase
    * Modified ShowL2fibPathListId
        * updated incorrect logic
    * Modified ShowL2routeEvpnMacIp
        * The c code has changed, the full length ipv6 addresses and next hop is now on the same line.
        * updated logic
        * updated test cases
    * Modified ShowFlowMonitorSdwanFlowMonitorStatistics
        * Added line.strip() and Optional("high_watermark")
    * Modified ShowVersion
        * Adding backspace to list of whitespace characters stripped from output lines

* viptela
    * Modified ShowSystemStatus
        * Add vManage storage options to schema as Optional.
        * Modified Optional cpu_allocation dict order to align with the device output.
        * Updated p1 regex to accomodate various single line output.
        * Updated p3 regex to accomodate for vManage/vController output and keep existing router output support.
        * Updated how p3/m3 dict group was parsed to build schema to support vManage along with existign router support.
        * Updated p7 and p8 to fix matching and parsing issues.
        * Fixed spacing within the conditional m8 business logic.
        * Added p9 and m9 to support the new vManage storage options Optional schema.
        * Updated comments throughout to be the same spacing/format.

* iosxr
    * Removed ShowL2VpnXconnectSummary
        * Class uses TCL and is replaced by ShowL2vpnXconnectSummary
    * Modified ShowControllersOptics
        * Added Optional key <fec_state> to schema
        * Added regex pattern <p4_1> to accommodate new <fec_state> schema key
        * Updated regex pattern <p3> to accommodate various outputs.
        * Updated regex pattern <p4> to accommodate various outputs.
        * Updated regex pattern <p40> to accommodate various outputs.
    * Modified ShowBgpInstanceNeighborsRoutesSchema
        * Modified key 'local_as' to capture dotted Notation ASN.
    * Modified ShowBgpInstanceNeighborsReceivedRoutesSchema
        * Modified key 'local_as' to capture dotted Notation ASN.
    * Modified ShowBgpInstanceNeighborsReceivedRoutes
        * Modified RegEx <p3>,<p13>,<p13_1>, (<m1><m2><m3>) under <p13>, <p17> to capture dotted Notation ASN in BGP
    * Modified ShowRouteIpv4
        * Handle nexthop without an outgoing interface
    * Modified ShowControllersFiaDiagshellL2showLocation
        * Remove extra bracket from regular expression
    * Modified ShowRSVPSession
        * Modified schema and changed respective parser logic
    * Modified ShowRSVPNeighbor
        * Replaced '-' with '_' in schema
    * Modified ShowRSVPGracefulRestartNeighbors
        * Replaced '-' with '_' in schema

* nxos/aci
    * Add parser for `ls -l` command

* utils
    * Modified unittest.py
        * Changed from json.dumps() to format_output() for showing parsed output
    * Modified Common.convert_intf_name
        * Added Fi and Fiv for FiveGigabitEthernet

* nxos
    * Modified ShowVxlan
        * Added new patterns ShowL2routeMacAllDetail.
        * Updated regex pattern to validate new ESI outputs.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* viptela
    * Created ShowOmpRoutes
        * Added ShowOmpRoutesSchema
        * Added ShowOmpRoutes parser
            * Added p1 and p2 regex pattern to match OMP routes table
            * Added conditional to handle variants of omp routes command that yields same output

* iosxe
    * Created ShowSdwanOmpRoutes
        * Added ShowSdwanOmpRoutes
        * Added unit test
    * Added ShowL2routeEvpnDGW
        * show l2route evpn default-gateway
        * show l2route evpn default-gateway host-ip {ip}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} producer {prod} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr}
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway host-ip {ip} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr}
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway topology {evi_etag} esi {esi}
        * show l2route evpn default-gateway producer {prod}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr}
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway producer {prod} esi {esi}
        * show l2route evpn default-gateway next-hop {next_hop}
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr}
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway next-hop {next_hop} esi {esi}
        * show l2route evpn default-gateway mac-address {macaddr}
        * show l2route evpn default-gateway mac-address {macaddr} esi {esi}
        * show l2route evpn default-gateway esi {esi}
    * Added ShowL2routeEvpnDGWDetail
        * show l2route evpn default-gateway detail
        * show l2route evpn default-gateway host-ip {ip} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} topology {evi_etag} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} producer {prod} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} detail
        * show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway host-ip {ip} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} producer {prod} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} detail
        * show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway topology {evi_etag} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr} detail
        * show l2route evpn default-gateway producer {prod} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway producer {prod} esi {esi} detail
        * show l2route evpn default-gateway next-hop {next_hop} detail
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} detail
        * show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway next-hop {next_hop} esi {esi} detail
        * show l2route evpn default-gateway mac-address {macaddr} detail
        * show l2route evpn default-gateway mac-address {macaddr} esi {esi} detail
        * show l2route evpn default-gateway esi {esi} detail
    * Added ShowL2routeEvpnPeers
        * show l2route evpn peers
        * show l2route evpn peers topology {evi_etag}
        * show l2route evpn peers topology {evi_etag} peer-ip {peer_ip}
        * show l2route evpn peers peer-ip {peer_ip}
    * Added ShowL2routeEvpnPeersDetail
        * show l2route evpn peers detail
        * show l2route evpn peers topology {evi_etag} detail
        * show l2route evpn peers topology {evi_etag} peer-ip {peer_ip} detail
        * show l2route evpn peers peer-ip {peer_ip} detail
    * Added ShowAuthenticationSessionsDetailsSuperSchema
        * show authentication sessions interface {interface} details
        * show authentication sessions interface {interface} details switch {switch} r0
        * show authentication sessions mac {mac_address} details
        * show authentication sessions mac {mac_address} details switch {switch} r0
    * Added ShowAuthenticationSessionsDetailsSuperParser
        * show authentication sessions interface {interface} details
        * show authentication sessions interface {interface} details switch {switch} r0
        * show authentication sessions mac {mac_address} details
        * show authentication sessions mac {mac_address} details switch {switch} r0
    * Added ShowAuthenticationSessionsMACDetails
        * show authentication sessions mac {mac_address} details
        * show authentication sessions mac {mac_address} details switch {switch} r0
    * Added ShowLispDynamicEid
        * Added 'show lisp {lisp_id} instance-id {instance_id} dynamic-eid'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid'
        * Added 'show lisp instance-id {instance_id} dynamic-eid'
        * Added 'show lisp eid-table {eid_table} dynamic-eid'
        * Added 'show lisp eid-table vrf {vrf} dynamic-eid'
        * Added 'show lisp eid-table vlan {vlan} dynamic-eid'
    * Added ShowLispDynamicEidAllDetail
        * Added 'show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid detail'
        * Added 'show lisp instance-id {instance_id} dynamic-eid detail'
        * Added 'show lisp eid-table {eid_table} dynamic-eid detail'
        * Added 'show lisp eid-table vrf {vrf} dynamic-eid detail'
        * Added 'show lisp eid-table vlan {vlan} dynamic-eid detail'
    * Added ShowEnvironmentSuperParser
        * 'show env all'
        * 'show env fan'
        * 'show env power'
        * 'show env power all'
        * 'show env rps'
        * 'show env stack'
        * 'show env temperature'
        * 'show env temperature status'
        * 'show environment all'
    * Added ShowEnvAll
        * 'show env all'
    * Added ShowEnvFan
        * 'show env fan'
    * Added ShowEnvPower
        * 'show env power'
    * Added ShowEnvPowerAll
        * 'show env power all'
    * Added ShowEnvRPS
        * 'show env rps'
    * Added ShowEnvStack
        * 'show env stack'
    * Added ShowEnvTemperature
        * 'show env temperature'
    * Added ShowEnvTemperatureStatus
        * 'show env temperature status'
    * Added ShowPlatformSoftware under c9600
        * for 'show platform software object-manager {serviceprocessor} statistics'
        * for 'show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics'
    * Added ShowInterfacesStatusErrDisabled
        * show interfaces status err-disabled
    * Added ShowTemplateBindingTarget
        * show template binding target {interface}
    * Added ShowLispDynamicEidSummary
        * Added 'show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary'
        * Added 'show lisp instance-id {instance_id} dynamic-eid summary'
        * Added 'show lisp eid-table vrf {vrf} dynamic-eid summary'
        * Added 'show lisp eid-table vlan {vlan} dynamic-eid summary'
        * Added 'show lisp eid-table {eid_table} dynamic-eid summary'
        * Added 'show lisp all instance-id * dynamic-eid summary'
    * Added ShowPlatformSoftwareFedactiveAclCountersHardware
        * 'show platform software fed active acl counters hardware'
    * Added ShowLicenseRumIdAll
        * show license rum id all
    * Added new parser for 'show platform software fed active inject packet-capture detailed'
    * Added new parser for 'show ip dhcp snooping binding'
    * Added ShowNetconfYangDatastores
        * show netconf-yang datastores
    * Added ShowNetconfYangStatus
        * show netconf-yang status
    * Modified ShowBgpNeighborsReceivedRoutes
        * 'show bgp {address_family} vrf {vrf} neighbors {neighbor} received-routes'
    * Added ShowCtsInterface for
        * show cts interface
    * Added ShowIpIgmpSnoopingGroups for
        * show ip igmp snooping groups
    * Added ShowIpIgmpSnoopingMrouter for
        * show ip igmp snooping mrouter
    * Added ShowIpIgmpSnoopingQuerier for
        * show ip igmp snooping querier
    * Added ShowMacsecSummary for
        * show macsec summary
    * Added ShowMacroAutoInterface for
        * show macro auto interface
    * Added ShowGlbpBrief for
        * show glbp brief
    * Added ShowL2routeEvpnMacDetail
        * show l2route evpn mac detail
        * show l2route evpn mac esi {esi} detail
        * show l2route evpn mac mac-address {mac_addr} detail
        * show l2route evpn mac mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac next-hop {next_hop} detail
        * show l2route evpn mac next-hop {next_hop} esi {esi} detail
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} detail
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac producer {producer} detail
        * show l2route evpn mac producer {producer} esi {esi} detail
        * show l2route evpn mac producer {producer} mac-address {mac_addr} detail
        * show l2route evpn mac producer {producer} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} esi {esi} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} detail
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} detail
        * show l2route evpn mac topology {evi_etag} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr} detail
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} detail
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} detail
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi} detail
    * Added ShowL2routeEvpnMac
        * show l2route evpn mac
        * show l2route evpn mac esi {esi}
        * show l2route evpn mac mac-address {mac_addr}
        * show l2route evpn mac mac-address {mac_addr} esi {esi}
        * show l2route evpn mac next-hop {next_hop}
        * show l2route evpn mac next-hop {next_hop} esi {esi}
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr}
        * show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac producer {producer}
        * show l2route evpn mac producer {producer} esi {esi}
        * show l2route evpn mac producer {producer} mac-address {mac_addr}
        * show l2route evpn mac producer {producer} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac producer {producer} next-hop {next_hop}
        * show l2route evpn mac producer {producer} next-hop {next_hop} esi {esi}
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr}
        * show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac topology {evi_etag}
        * show l2route evpn mac topology {evi_etag} esi {esi}
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr}
        * show l2route evpn mac topology {evi_etag} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} esi {esi}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr}
        * show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi}
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr}
        * show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi}

* junos
    * Added ShowSecurityPoliciesHitCount
        * show security policies hit-count

* iosxr
    * Added ShowMplsTrafficEngTunnelsTabular
        * show mpls traffic-eng tunnels tabular
    * Added ShowMplsTrafficEngTunnelsTunnelid
        * Added show mpls traffic-eng tunnels {tunnel_id}
    * Added ShowRSVPSession
        * Added 'show rsvp session'
        * Added 'show rsvp session destination {ipaddress}'
    * Added ShowRSVPNeighbor
        * Added 'show rsvp neighbor'
    * Added ShowRSVPGracefulRestartNeighbors
        * Added 'show rsvp graceful-restart neighbors'
    * Added MonitorInterfaceInterface
        * Added 'monitor interface {interface}'
    * Added ShowRSVPGracefulRestartNeighborsDetail
        * Added 'show rsvp graceful-restart neighbors detail'
    * Added ShowRSVPSessionDetail
        * Added 'show rsvp session detail'
        * Added 'show rsvp session destination {ip_address} detail dst-port {tunnel_id}'

* nxos
    * Added ShowTrack
        * show track
        * show track {id}
        * show track brief

* utils
    * Modified common.py
        * Added telemetry data collection within get_parser()


