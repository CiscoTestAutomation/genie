March 2025
==========

March 25 - Genie v25.3 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.3 
    ``genie.libs.health``, v25.3 
    ``genie.libs.clean``, v25.3 
    ``genie.libs.conf``, v25.3 
    ``genie.libs.filetransferutils``, v25.3 
    ``genie.libs.ops``, v25.3 
    ``genie.libs.parser``, v25.3 
    ``genie.libs.robot``, v25.3 
    ``genie.libs.sdk``, v25.3 
    ``genie.telemetry``, v25.3 
    ``genie.trafficgen``, v25.3 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* genie.harness
    * Updated discovery
        * Added support to retry triggers



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * ResetConfiguration
        * Added stopbits to the KEEP the variables while resetting the Configurations in ResetConfiguration class.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie.libs.conf
    * Fix ParsedInterfaceName to avoid crash with unsupported graph

* nxos
    * Fix feature service-acceleration
        * Add `https_proxy` and `https_port` to the list of attributes to be handled by the conf model
        * Add unit tests
    * Fix nxapi_method_restconf api
        * output from a rest call is a response object, not a list
        * fixed api call to check for instance of `output.json()` which is a list.



genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Platform Rev 1
        * Added backup options for chassis serial number
    * Platform Rev 2
        * New rev added to pick up LC and RP slot SN and PID



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_ipv6_dhcp_pool
        * API to configure_ipv6_dhcp_pool
    * Added API configure_vrf_rd_rt
        * added api to configure vrf rd and rt on the device
    * Added API enable_ip_classless
        * API to enable ip classless on the device
    * Added configure_radius_server_dtls_ip
        * API to configure radius server dtls ip
    * Added configure_interface_media_type_backplane
    * Added unconfigure_device_sampler
        * API to unconfigure a sampler on an IOS-XE device.
    * Added configure_radius_server_dtls_idletimeout
        * API to configure radius server dtls idletimeout
    * Added unconfigure_boot_system_switch_all_flash
        * API to unconfigure boot system variable on all switches in the stack.
        * Example no boot system switch all flashtestAll
    * Added API configure_interfaces_uplink
        * Added API to configure_interfaces_uplink
    * Added API configure_interfaces_no_uplink
        * Added API to configure_interfaces_no_uplink
    * Added configure_ip_pim_bsr_rp_candidate
        * API to Configure ip pim candidate rp or bsr for both global and VRF contexts.
    * Added API configure_radius_server_dtls_connection
    * Added new API to Release DHCP on interface
        * API to execute release dhcp on interface
    * Added new API to Renew DHCP on interface
        * API to execute renew dhcp on interface
    * Added new API to Execute 'clear ipv6 dhcp conflict *' on device
        * API to Execute 'clear ipv6 dhcp conflict' on device
    * Added new API to Configure service-policy type control default on interface
        * API to configure service-policy type control default on interface
    * Added new API to Configure ip dhcp class static on device
        * API to configure ip dhcp class static on device
    * Added configure_vlan_config_device_tracking
        * API to configure vlan configuration <vlan_number>
    * Added configure_pbr_route_map_nhop_verify_availability
        * API for configure pbr route map with next hop verify availability
    * Added unconfigure_exporter
        * API to unconfigure flow exporter on device.
    * Added configure_radius_server_with_dtls
        * configure api for radius_server_with_dtls
    * Added unconfigure_interface_media_type_backplane
        * API to unconfigure backplane media_type on interface.
    * Added configure_dhcp_pool_ztp
        * API to configure DHCP pool for ZTP.
    * PBR
        * Added api_configure_pbr_route_map_add_set
            * API to add set action to route map
    * Added API configure_radius_server_dtls_watchdoginterval
    * API to Configure radius server dtls watchdoginterval
    * SLA
        * Added configure_ip_sla_icmp_echo
        * Added unconfigure_ip_sla
        * Added configure_ip_sla_schedule
        * Added unconfigure_ip_sla_schedule
        * Added configure_ip_sla_at_track

* api to configure backplane media_type on interface.

* pbr
    * Added API configure_pbr_route_map_nhop_recursive
        * configure api for PBR route map nhop recursive


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated api unconfigure_hw_module_breakout
        * updated api with module_number and port_number to support hw-module breakout module cli
    * Updated api configure_hw_module_breakout
        * updated api with module_number and port_number to support no hw-module breakout module cli
    * Updated api verify_ignore_startup_config
        * updated api to make it optional to check for switch_ignore_startup_config variable to be exist in show romvar 'rommon_variables' output when it's not setted.
    * Updated api function name from configure_pae to configure_product_analytics
        * updated api for cli change from PAE to product-analytics
    * Updated api function name from unconfigure_pae to unconfigure_product_analytics
        * updated api for cli change from no PAE to no product-analytics
    * Deleted UT files for configure_pae and unconfigure_pae
        * deleted UT files for configure_pae and unconfigure_pae
    * Updated api execute_install_one_shot
        * updated api with optional arguments post_reload_wait_time and error_pattern

* generic
    * Modified `execute_clear_line` API
        * Changed disconnect_termserver argument to default to True
        * Update logic to avoid disconnecting twice



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fixed parser ShowIpv6MldGroups
        * Fixed regex pattern p1 to work for different uptime format
    * Fixed parser ShowIpPimRpMapping
        * Fixed the logic under p3 regex to match "protocol" for new output
    * Fix ShowIpv6Mfib parser
        * Updated regex pattern p7 to accomodate various outputs.
        * Updated regex pattern p8 to accomodate various outputs.
        * Added optional keys 'ingress_mdt_ip', 'egress_mdt_ip' to the parser.
    * Modified ShowIpEigrpInterfacesDetail
        * Modified parser for 'show ip eigrp interfaces detail' and added <interface> option
    * Fixed the regex p1 for new output.
    * ShowIpRouteWord
        * Added line parsing for `Default gateway is 172.27.147.1`
    * Fixed parser ShowVersion
        * Fixed regex pattern - p1_1 for show version in IOS device
    * Modified ShowPlatformSoftwareFedIgmpSnoopingGroups
        * Modified schema and parser for 'show platform software fed {state} ip igmp snooping groups vlan {vlan}'
    * ShowInterfaces
        * Fixed p2_2 regex to correctly match this line `Hardware is BUILT-IN-4x2_5GE, address is 8c1e.8068.9f6c (bia 8c1e.8068.9f6c)`
    * Modified parser ShowIpMroute
        * Updated regex pattern p3 to accomodate various outputs
        * Added optional key 'iif_mdt_ip' to schema
    * Added ShowMacAddressTableDynamicVlan to support show mac address-table dynamic vlan
        * Added a parser
    * Modified ShowDhcpLease
        * Added regex <p5_1> to handle Infinite lease time.
    * Modified ShowIpDhcpBinding
        * Added regex <p2> to match multiline Client-ID
    * Show Platform
        * Made `chassis` optional
    * Fixed schema parser ShowIpMfib
        * In regex p7, added optional parameters - 'ingress_mdt_ip'
        * In regex p8, added optional parameters - 'egress_mdt_decap' and 'egress_mdt_ip'
    * Fixed parser ShowPlatformSoftwareFedIgmpSnooping
        * Added p14_3 regex to match the output of the command
    * Fixed parser ShowLispMapCacheSuperParser
        * Added support for parsing optional keyword 'self' as part of 'via' capture group.
    * cat9k
        * fixed parser ShowL2ProtocolTunnelSummary - initialised last_port
    * Fixed parser ShowPimNeighbor
        * Fixed regex pattern p2 to accomodate different output
    * Fixed parser ShowVersion
        * Fixed regex pattern - p1_1 for show version in IOS device
    * Modified ShowIpIgmpGroups
        * Modified parser for 'show ip igmp groups {interface}'
    * Modified ShowIpIgmpGroupsDetail
        * Modified parser for 'show ip igmp groups  {ip} detail'
    * Modified ShowIpIgmpInterface
        * Modified parser for 'show ip igmp interface {interface}'
    * Modified ShowIpEigrpNeighbors
        * Modified parser for 'show ip eigrp neighbors' and added <interface> option
    * Fixed the regex p1 to handle the last entry in the output.
    * Fixed the unittest that was failing to parse the last line of the output.

* added cli command 'show platform software fed {switch_var} {state} ip igmp snooping groups vlan {vlan}'

* sonic
    * Added multiple regex and conditions for output in golden_output_3_output.txt

* iosxr
    * Modified ShowBgpInstanceNeighborsReceivedRoutes
        * Modified regex pattern
        * Added testfolder for  ShowBgpInstanceNeighborsReceivedRoutes
    * Modified ShowMonitorCaptureBufferDetailed
        * Modified schema and parser for'show monitor capture file {path} packet-number {number} detailed'
    * Modified ShowVrfAllDetail
        * Modified regex pattern to support multiple interfaces

* nxos
    * Added Service-Ethernet interface
        * This will be used to convert the SEth to Service-Ethernet


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareCppActiveStatisticsDrop
        * Updated schema and parser for cli show platform hardware cpp active statistics drop


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCallerSummary
        * show caller summary
    * Added ShowPlatformSoftwareFedIpIgmpSnoopingGroupsVlan parser
        * 'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group}',
        * 'show platform software fed {switch} {module} ip igmp snooping group vlan {vlan_id} {group} detail'
    * Added ShowPlatformSoftwareFedSwitchActiveOifset parser
        * Added schema and parser for cli 'show platform software fed switch active oifset'
    * Added ShowPlatformSoftwareFedSwitchFnfSwStatsShow
        * Added schema and parser for'show platform software fed switch fnf sw stats show'
    * Added revision 2 for "show inventory" parser
        * Modified code to add slot number as key under slots dict
        * Supervisor cards added under RP dict
    * Added ShowIpNhrpSelf parser
        * Added schema and parser for cli 'show ip nhrp self'
    * Added ShowAutoInstStat parser
        * Added schema and parser for cli 'show auto inst stat'
    * Added ShowPlatformHardwareFedSwitchFwdAsicResourceTcamTableNflAclFormat0
        * Added schema and parser for'show platform hardware fed switch fwd asic resource tcam table nfl acl format 0'
    * Added ShowIpEigrpTimers Parser in show_eigrp.py
        * Added schema and parser for 'show ip eigrp timers'
    * Added ShowIpNhrpVrf parser
        * Added schema and parser for cli
            * 'show ip nhrp vrf {vrf}'
            * 'show ip nhrp vrf {vrf} {ip}'
    * Added ShowCryptoIsakmpSaStatus
        * show crypto isakmp sa {status}
    * Added ShowCryptoIsakmpPeer
        * show crypto isakmp peer {peer_ip}
    * Added ShowIpPimVrfMdtBgpSchema parser
        * Added schema and parser for cli 'show ip pim vrf {vrf_name} mdt bgp'
    * Added ShowEthernetRingG8032Brief schema and parser.
        * Added schema and parser for show ethernet ring g8032 brief.
    * Added ShowCryptoIpsecSpiLookupDetail
        * show crypto ipsec spi-lookup detail
    * Added ShowCryptoIsakmpDefaultPolicy
        * show crypto isakmp default policy
    * Added ShowIpMfibActive parser
        * Added schema and parser for cli 'show ip mfib active'
    * Added ShowPlatformSoftwareFedIpv6RouteSummaryInclude
        * Added schema and parser for 'show platform software fed ipv6 route summary'
    * Added  ShowPlatformSoftwareFedSwitchFnfMonitorsDump parser
        * Added schema and parser for cli "show platform software fed Switch {Switch_num} fnf monitors dump"
    * Added ShowIpIgmpMembership parser
        * Added schema and parser for cli 'show ip igmp membership'
    * Added ShowIpv6PimMdtSend
        * show ipv6 pim mdt send
        * show ipv6 pim vrf {vrf} mdt send
    * Added ShowPlatformSoftwareFedActivePuntAsicCauseBrief parser
        * Added schema and parser for cli
            * 'show platform software fed {switch} active punt asic-cause brief'
    * Added ShowPlatformHardwareFedSwitchActiveQosQueueStatsInternalPortTypePuntQueue parser
        * Added schema and parser for cli
            * 'show platform hardware fed {switch} active qos queue stats internal port_type punt queue {voq_id}'
    * Added parser  ShowPlatformHardwareQfpActiveFeatureCtsClientInterface
        * Added parser for cli show platform hardware qfp active feature cts client interface.
    * Added ShowIpNhrpRedirect parser
        * Added schema and parser for cli 'show ip nhrp redirect'
    * Added ShowPlatformSoftwareFedSwitchActiveOifsetUrid parser
        * Added schema and parser for cli 'show platform software fed switch active oifset urid {id}'
        * Added schema and parser for cli 'show platform software fed switch active oifset urid {id} detail'
    * Added schema and parser for show platform hardware cpp active feature firewall session create {session_context} {num_sessions}

* showcryptoisakmpsacount
    * show crypto isakmp sa count



genie.telemetry
"""""""""""""""
