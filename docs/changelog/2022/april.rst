April 2022
==========

April 26 - Genie v22.4 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.4                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.4                          |
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

* ops
    * Modified Utils
        * Enabled Ops to be extended via local packages and genielibs.cisco
        * Added ExtendOps class to handle extension

* conf
    * Modified Base
        * Added `__new__` definition to enable local package extension upon class creation

* harness
    * Modified Utils
        * Added Boolean parameter to load_attribute function for logger warning suppression
    * Modified GenieScriptDiscover
        * Enabled Triggers to be extended via local packages and genielibs.cisco
        * Added helper function _get_external_triggers()

* json
    * Modified MakeOps
        * Added 'package' to Ops in the ops.json file


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* harness
    * Use order of processors as loaded from the trigger datafile



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified
        * Fixed device recovery issue after power cycling and booting golden image
    * Modified
        * Fixed device recovery issue on vwlc where wrong image is booted
    * cat9k
        * Added enable_boot_manual execution step for tftp boot stage
        * Updated the unittest for tftp boot
    * Install_image
        * add dialog and error pattern for install failing.
    * Modify image hander, upload reload service arguments with image_to_boot

* clean/tests
    * updated the symlink for platforms which were not added

* iosxr
    * Added new api execute clear platform_hardware fed active qos statistics interface
        * to clear qos statistics on interface

* utils
    * Modify validate_clean API
        * Fixed a bug when clean_data[section] is None and clean_data[section].pop is called
        * Changed clean class string to be snake case during clean-file validation to properly compare clean stages and their classes

* generic
    * Modify recovery processor, only recover device if it has been connected


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_policy_map API
        * configuring policy map
    * CAT9K
        * Added rommon_boot stage



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* all
    * Modified setup.py
        * Include Ops json file regardless of location
    * Changed pkgs/ops-pkg/src/genie/libs/ops/ops.json to be a symlink



genie.libs.robot
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* robot
    * Modified setup.py and Makefile
        * Pinned robotframework version to be less than version 5.0



genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added execute_switch_renumber API
        * API for switch renumbering
    * Added 'configure_private_vlan_on_vlan' API
        * configure private vlan on device
    * Added 'disable_ip_dhcp_auto_broadcast' API
        * disable ip dhcp auto broadcast on device
    * Added 'enable_ip_dhcp_auto_broadcast' API
        * enable ip dhcp auto broadcast on device
    * Added 'enable_dhcp_smart_relay' API
        * enable dhcp smart relay on device
    * Added 'disable_dhcp_smart_relay' API
        * disable dhcp smart relay on device
    * Added 'unconfigure_ip_dhcp_snooping_verify' API
        * unconfigure ip dhcp snooping verify on device
    * Added 'configure_ip_dhcp_client' API
        * configure ip dhcp client on device
    * Added 'configure_uplink_interface' API
        * configure uplink interface setup on interface
    * Added 'configure_downlink_interface' API
        * configure downlink interface setup on interface
    * Added 'configure_switchport_trunk_native_vlan' API
        * configure switchport trunk native vlan on interface
    * Added 'configure_switchport_mode_trunk_snooping_trust' API
        * configure switchport mode trunk snooping trust on interface
    * Added 'configure_egress_interface' API
        * configure egress interface on interface
    * Added unconfigure_interfaces_on_port_channel API
        * API for unconfigure interfaces on port channel
    * Added execute_redundancy_reload API
        * API for redundancy reload peer
    * Added configure_interface_tunnel_hub API
        * Added new API for configuring Interface Tunnel Hub
    * Added configure_interface_tunnel_spoke API
        * Added new API for configuring Interface Tunnel Spoke
    * Added configure_interface_virtual_template API
        * Added new API for configuring Interface Virtual Template
    * Added API 'unconfigure_ikev2_keyring'
    * Added API 'unconfigure_ikev2_profile'
    * Added API 'clear_crypto_session'
    * Added clear_device_tracking_messages API
        * API for clearing device-tracking messages
    * Added DHCPv4 APIs
        * Added get_dhcpv4_server_stats API
        * Added get_dhcpv4_server_bindings API
        * Added get_dhcpv4_binding_address_list API
        * Added clear_dhcpv4_server_stats API
        * Added verify_dhcpv4_packet_received API
        * Added verify_dhcpv4_binding_address API
    * Added DHCPv6 APIs
        * Added get_dhcpv6_server_stats API
        * Added get_dhcpv6_server_bindings API
        * Added get_dhcpv6_binding_address_list API
        * Added verify_dhcpv6_packet_received API
        * Added verify_dhcpv6_binding_address API
    * Added get_static_routing_routes API
        * API for getting static routes, in a similar way to get_routing_routes
    * Added configure_ip_local_pool API
        * configure ip local pool on router
    * Added configure_mdns_service_list API
        * API for configuring mDNS(Multicast Domain Name System) service list
    * Added unconfigure_match_service_type_mdns_service_list API
        * API for unconfiguring mDNS(Multicast Domain Name System) matche services in service list
    * Added unconfigure_service_type_mdns_service_definition API
        * API for unconfiguring mDNS(Multicast Domain Name System) service_definition
    * Added configure_mdns_controller_service_list API
        * API for configuring mDNS(Multicast Domain Name System) controller service list
    * Added unconfigure_match_service_type_mdns_controller_service_list API
        * API for unconfiguring mDNS(Multicast Domain Name System) controller service list
    * Added configure_controller_policy API
        * API for configuring mDNS(Multicast Domain Name System) controller policy
    * Added unconfigure_controller_policy_service_export API
        * API for unconfiguring mDNS(Multicast Domain Name System) controller policy
    * Added configure_mdns_service_peer_group API
        * API for configuring mDNS(Multicast Domain Name System) service peer group
    * Added configure_dynamic_nat_outside_rule API
        * API for configuring a dynamic NAT outside rule.
    * Added unconfigure_dynamic_nat_outside_rule API
        * API for unconfiguring a dynamic NAT outside rule.
    * Added configure_disable_nat_scale API
        * API for configuring disable NAT scale.
    * Added configure_nat_translation_timeout API
        * API for configuring ip nat translation timeout.
    * Added unconfigure_nat_translation_timeout API
        * API for unconfiguring ip nat translation timeout.
    * Added configure_interface_service_policy API
        * API for configuring service policy on interface
    * Added verify_routing_route_attrs and verify_static_routing_route_attrs APIs
        * APIs to verify existence of an IPv4/IPv6 route or static route, and
    * Added get_static_routing_ipv6_routes
        * Get `show ipv6 static detail` parser output containing IPv6 static
    * Added configure_bba_group API
        * bba-group pppoe {name}
        * virtual-template {vt_number}
    * Added unconfigure_bba_group API
        * no bba-group pppoe {name}
    * Added configure_tftp_source_interface API
        * ip tftp source-interface {interface}
    * Added unconfigure_tftp_source_interface API
        * no ip tftp source-interface {interface}
    * Added configure_virtual_template API
        * Configure virtual template on the router
    * Added unconfigure_configure_virtual_template API
        * Unconfigure virtual template on the router
    * Added configure_flow_monitor_cache_entry API
        * Added new API to configure flow monitor with cache entries
    * Added unconfigure_flow_monitor API
        * Added new API to unconfigure flow monitor
    * Added configure_fnf_record API
        * Added new API to configure flow record with extra parameters
    * Added unconfigure_flow_record API
        * Added new API to unconfigure flow record
    * Added configure_sampler API
        * Added new API to configure sampler
    * Added unconfigure_sampler API
        * Added new API to unconfigure sampler
    * Added configure_fnf_monitor_sampler_interface API
        * Added new API to configure flow monitor with sampler on interface
    * Added configure_fnf_monitor_datalink_interface API
        * Added new API to configure flow monitor with datalink on interface
    * Added unconfigure_fnf_monitor_datalink_interface API
        * Added new API to unconfigure flow monitor with datalink on interface
    * Added get_total_asics_cores  API
        * Added new API to get the total number of ASICs and COREs
    * Added unconfigure_routing_ip_route_vrf API
        * unconfigure_routing_ip_route_vrf to remove the config done by configure_routing_ip_route_vrf
    * Added configure_routing_ipv6_route API
        * configure_routing_ipv6_route to configure IPv6 route
    * Added unconfigure_routing_ipv6_route API
        * unconfigure_routing_ipv6_route to unconfigure IPv6 route
    * Added configure_routing_ipv6_route_vrf API
        * configure_routing_ipv6_route_vrf to configure IPv6 route with VRF
    * Added unconfigure_routing_ipv6_route_vrf API
        * unconfigure_routing_ipv6_route_vrf to unconfigure IPv6 route with VRF
    * Added configure_ipv6_enable API
        * configure_ipv6_enable under given interface
    * Added unconfigure_ipv6_enable API
        * unconfigure_ipv6_enable under given interface
    * Added configure_eigrp_named_networks API
        * configure_eigrp_named_networks to configure named EIGRP
    * Added unconfigure_eigrp_named_router API
        * unconfigure_eigrp_named_router to unconfigured named EIGRP
    * Added copy_running_config_to_flash_memory API
        * Restore config from local file using copy function on Device
    * Added unconfig_qos_rewrite_dscp API
        * Unconfigures qos rewrite ip dscp on Device
    * Added config_qos_rewrite_dscp API
        * Configures qos rewrite ip dscp on Device
    * Added config_replace_to_flash_memory API
        * Configures replace to flash memory
    * Added get_run_configuration API
        * Search config in show running-config output
    * Added get_startup_configuration API
        * search config in show startup-config output
    * Added get_status_for_rollback_replacing_in_flash API
        * search the status for rollback replacing in flash memory
    * Added configure_fips_authorization_key API
        * API to configure fips authorization key
    * Added unconfigure_fips_authorization_key API
        * API to unconfigure fips authorization key

* blitz
    * Test that should remove a value yet the value is not removed has wrong message.
        * Check if node still remains and provide correct log message.
    * Enhanced yangexec to compare the RPC error in case of negative testing
    * Added variable section.parameters
        * section.parameters can be accessed via %VARIABLES{section.parameters.<>} in Blitz yaml


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added bdi option to clear_device_tracking_messages
    * Fixed 'verify_ping' API
        * Modified logic of the API to allow use of all options
    * Modified get_ip_theft_syslogs API
        * Updated the parsing to return common interface names
    * Modified execute_issu_install_package API
        * API for installing  issu package
    * Modify get_ipv6_interface_ip_address API
        * Add `as_list` keyword argument (default `False`) to return multiple
    * Modify get_routing_routes and get_routing_ipv6_routes APIs
        * Allow the `vrf` argument to be passed as `None` and execute the
    * Modified configure_flow_monitor API
        * Made few arguments as optional, added new arguments
    * Modified configure_flow_record API
        * Made the default arguments to have proper values
    * Updated configure_ospf_routing API
        * configure_ospf_routing to configure OSPF with VRF and without router-id
    * Updated unconfigure_ospf_on_device API
        * unconfigure_ospf_on_device to take VRF for unconfiguring ospf
    * Updated configure_ikev2_profile_pre_share API
        * configure_ikev2_profile_pre_share to take fvrf
    * Updated configure_ipsec_tunnel API
        * configure_ipsec_tunnel to take ivrf (overlay) and fvrf (underlay)
    * Updated configure_bgp_neighbor API
        * configure_bgp_neighbor to take address family and VRF
    * Updated config_interface_ospfv3 API
        * config_interface_ospfv3 to take af ipv4 or ipv6
    * Updated unconfig_interface_ospfv3 API
        * unconfig_interface_ospfv3 to take af ipv4 or ipv6
    * Added unconfigure_vlan_vpls
        * API was incorrectly removed in user-submitted PR from a few months ago

* all
    * Modified setup.py and Makefile
        * pin grpcio version to be less than or equal to 1.36.1 to be in line with yang.connector

* nxos
    * Modified triggers.processrestart.libs.nxos.processrestart.ProcessRestartLib
        * Exclude nxoc_dc service from core check upon crash test
        * Avoid script crash when service 'sap' is not available in show command output

* genie.libs.sdk
    * Added `yang.connector` as dependency

* blitz
    * run_netconf
        * fixed the sequence flag issue
    * Modified yang action to fix a NoneType object is not iterable bug


genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformTcamPbrNat
        * show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowNatTranslations
        * show ip nat translations
    * Added ShowRunRoute
        * for 'show running-config | section route'
    * Added configure_bgp_sso_route_refresh_enable
        * bgp sso route referesh-enable
    * Added configure_bgp_refresh_max_eor_time
        * bgp refresh max-eor-time {max_eor_time}
    * Added ShowCryptoGdoi
        * Parser for show crypto gdoi
    * Added ShowCryptoGdoiDetail
        * Parser for show crypto gdoi detail
    * Added class ShowCryptoGdoiGroup
        * Parser for show crypto gdoi group {group_name}
    * Added ShowCryptoGkm
        * Parser for show crypto gkm
    * Added ShowCryptoGdoiKsPolicy
        * Parser for show crypto gdoi ks policy
    * Added ShowCryptoGdoiGmDataplanCounter
        * Parser for show crypto gdoi gm dataplan counter
    * Added ShowCryptoSessionInterfaceDetail
        * show crypto session interface {interface} detail
    * Added ShowEthernetCfmMaintenancePointsRemoteDetail
        * for 'show ethernet cfm maintenance-points remote detail'
    * Added ShowEthernetCfmStatistics
        * for 'show ethernet cfm statistics'
    * Added 'ShowInterfacesMtu' schema and parser
        * show interfaces mtu
        * show interfaces { interface } mtu
        * show interfaces mtu module {mod}
    * Added ShowIpNhrpTraffic
        * show ip nhrp traffic
        * show ip nhrp traffic interface {interface}
    * Added ShowIpNhrpTrafficDetail
        * show ip nhrp traffic detail
        * show ip nhrp traffic interface {interface} detail
    * Added 'ShowPlatformSoftwareFedIfm' schema and parser
        * show platform software fed switch active ifm interfaces tunnel
    * Added ShowCryptoEliAll
        * show crypto eli all
    * Added ShowPlatformHardwareQfpIpsecDrop
        * show platform hardware qfp active feature ipsec data drop
    * Added ShowIsisNodeSummary
        * show isis node summary
    * Added ShowIsisTopologyLevel
        * show isis topology {level}
    * Added ShowSystemMtu
        * show system mtu
    * Added ShowIdpromInterface for C9300
        * show idprom interface {interface}
    * Added ShowStackwiseVirtualNeighbors
        * Added 'show stackwise-virtual neighbors'
    * Added ShowSystemIntegrityMeasurement
        * Parser to support new kgv measurement cli
    * Added ShowSystemIntegrityCompliance
        * Parser to support new kgv compliance cli
    * Added ShowSystemIntegrityTrustChain
        * Parser to support new kgv trust chain cli
    * Modified ShowSystemIntegrityAllTrustChainNonce
        * Added yang parser for ShowSystemIntegrityAllTrustChainNonce
    * Added ShowPlatformHardwarefedActiveQosQueueStats parser
        * show call Show Platform Hardware fed Active Qos Queue Stats
    * Added ShowPlatformHardwareFedActiveQosQueuelabel2qmapQmapegressdataInterface  parser
        * show call Show Platform Hardware Fed Active Qos Queue label2qmap Qmap egress data Interface

* iosxr
    * Added ShowEvpnGroup
        * 'show evpn group'
        * 'show evpn group {group_id}'
    * Added ShowEvpnEviMacDetail
        * show evpn evi mac detail
        * show evpn evi vpn-id {vpn-id} mac detail
    * Modified ShowOspfInterfaceBrief
        * Fixed to get instance value properly

* nxos
    * Added ShowInterfaceCounters
        * show interface counters
        * show interface {interface} counters
    * Added ShowHsrpEventHistoryErrors for
        * 'show hsrp internal event-history errors'
    * Added ShowHsrpEventHistoryDebugs for
        * 'show hsrp internal event-history debugs'
    * Added ShowHsrpEventHistoryMsgs for
        * 'show hsrp internal event-history msgs'


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpRoute
        * Updated the key and value of "source_protocol_dict" dict
    * Modified ShowLispDatabaseEid
        * Changed <srvc_ins_type> from schema to Optional
        * Changed <srvc_ins_id> from schema to Optional
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Fixed regex for "unknown-eid-forward"
    * Modified ShowLispEthernetDatabase
        * Changed <srvc_ins_type> from schema to Optional
        * Changed <srvc_ins_id> from schema to Optional
    * Modified ShowLispEthernetMapCache
        * Updated regex pattern due to change in output
    * Modified ShowLisp
        * Updated regex pattern due to change in output
    * Modified ShowLispSession
        * Added cmd 'show lisp session {established}'
    * Modified ShowLispServiceSchema
        * Changed <xtr_id> to Optional
        * Changed <site_id> to Optional
    * Modified ShowLispInstanceIdService
        * Updated regex pattern due to change in output
    * Modified ShowLispRemoteLocatorSetSchema
        * Updated <instance_id> type as str
    * Modified ShowLispPublicationPrefixSuperParser
        * Updated regex pattern due to change in output
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Updated regex pattern
        * No backward compatibility
    * Modified ShowIdpromInterface
        * Changed the key <nominal_bitrate_per_channel>' to optional
        * Updated regex <p2>, <p3>, <p4>, <p5>, <p8>, <p13>, <p14>, and <p15>
    * Modified ShowIpStaticRoute
        * Add the optional `owner_code` key under `next_hop.outgoing_interface`
    * Modified ShowIpv6DhcpBinding
        * Add the optional client 'interface' key to the schema
        * Make the existing client 'ia_na' key optional
        * Add the optional client 'ia_pd' key to the schema
        * Update existing regex processing for 'Address' under 'IA NA' to
        * Fix populating of schema so that multiple keys for IA ID are
    * Modified ShowIpv6Route
        * Add "ND" and "NDp" to the dict of accepted protocol codes
        * Modify the regular expression to accept 3-character long protocol
    * Modified ShowIsisDatabaseVerbose
        * Modified the regex to parse the flex algo portion of a prefix sid
    * Modified ShowNveVni
        * Added the functionality to run parser with vni id
    * Modified ShowStandbyBrief
        * Updated regex <p0> to parse IP addresses as active addresses
    * Modified ShowIpNhrpTrafficDetail
        * Added return statement for parser output to return
    * Modified ShowIpRpf
        * Added optional key <directly_connected>
        * Modified regex <p3_1>
    * Modified ShowL2vpnServiceAll
        * Fixed regex <p2> to match more patterns in output
    * Modified ShowDeviceTrackingMessages
        * Added option for `show device-tracking messages | section {message}`
    * Modified ShowInterfaces
        * Added optional keys <tunnel_source_interface>
        * Updated regex pattern p46 to accommodate various outputs.
    * Modified ShowLicenseEventlog2
        * Added proper no_event_log key  to schema
    * Modified ShowLicenseTechSupport
        * Added optional key <autorization_renewal> to schema
        * Added optional key <failures_reason> to schema
        * Added the key <local_device> to schema
        * Modified the expression for p11_data1_3 to work on all scenario.
    * Modified ShowIpMfib
        * Updated ShowIpMfibSchema with optional keys <ingress_vxlan_version>,<ingress_vxlan_vni>,<ingress_vxlan_nxthop>,<ingress_vxlan_cap>,<egress_vxlan_version>,<egress_vxlan_vni>,<egress_vxlan_nxthop>,<egress_vxlan_cap>
        * Updated regex pattern of "show ip mfib" by changing the existing one to accomodate optional incoming interfaces, entries with no flags, no preceding spaces in flags output and adding another line to parse vxlan related information
    * Modified ShowIpMrib
        * Updated ShowIpMribSchema to make incoming_interface_list and egress_interface_list as optional keys
        * Updated regex pattern of ShowIpMrib parser to accomodate vxlan related keywords
    * Modified ShowSystemIntegrityAllMeasurementNonce
        * Minor correction to match bundle boot output in regex pattern <p5>
    * Modified ShowVersion
        * All switches (active and standby) now appear in the switch_num dictionary
    * Modified ShowIpRoute
        * Updated the key and value of "source_protocol_dict" dict
    * Modified ShowSystemIntegrityAllMeasurementNonce
        * Added yang parser for ShowSystemIntegrityAllMeasurementNonce
        * Modified the parser name to showsystemintegrityalltrustchainnonce


* ios
    * Modified ShowIpStaticRoute
        * Add the optional `owner_code` key under `next_hop.outgoing_interface`

* iosxr
    * Modified ShowPolicyMapInterface Parser, update pattern p4 output direction
    * Modified ShowInterfacesDescription
        * Match interfaces only after table header (prevent matching timestamp)
        * Use iosxr interface naming (ex MgmtEth or nVFabric interface)
    * Modified ShowMplsLdpIgpSync
        * Fixed regex <p1>, <p3>, and <p5> to match more patterns in output
    * Modified ShowEvpnEviMac
        * Changed 'label' from int to str.
        * Added 'sid', 'sid_flags', 'endpt_behavior', 'sid_struct', 'transposition', 'local_e_tree', 'remote_e_tree', 'remote_matching_e_tree_rt', 'local_ac_id', 'remote_ac_id', 'ext_flags' and 'stamped_xcid' key to the schema
        * Updated regex pattern p1 and p1_1 to accommodate various outputs.
        * Added new regex pattern and match for all the new keys
    * Modified ShowEvpnEviMacPrivate
        * Updated cli to accept vpn-id key
        * show evpn evi vpn-id {vpn-id} mac private
    * Modified ShowMplsForwarding
        * Added command filtering with prefix (ex show mpls forwarding prefix 1.1.1.1/32)

* common
    * Modified Common
        * Modified convert_intf_name to allow letter in interface port (ex 0/RP0/CPU0/0)

* nxos
    * Modified ShowSystemInternalSysmgrServiceName
        * Updated regex pattern <p2> to accept 'no SAP'

