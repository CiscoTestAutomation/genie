March 2022
==========

March 29 - Genie v22.3 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.3                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.3                          |
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

* genie.conf.base.api
    * Added CleanAPI
        * This class allows users to quickly call and run clean stages.
        * Usage <device>.api.clean.<stage_name>(<stage args>)
    * Modified API
        * To add the CleanAPI functionality


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* conf/utils
    * converter.py
        * fixed the bug in convert_device method

* harness
    * modified discovery.py
        * Common Cleanup will now run even if triggers fail to load
    * updated trigger datafile schema
        * added 'timeout' with 'max_time' and 'interval'

* ops
    * Updated maker for Ops
        * Fixed a bug when passing 'commands' to Learn Ops



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* utils
    * Modified load_clean_json function
        * Now it only loads the first time called and save the data in a global variable. Any consecutive calls will just return that data instantly.

* iosxr
    * Modified VerifyRunningImage
        * Fixed a bug in the version comparison

* iosxe
    * Modified device recovery grub menu logic
        * To support more device types


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* cheetah
    * Added new clean stage erase_ap_configuration
        * Erases the configurations on AP
    * Added new clean stage prime_ap
        * Primes the AP to controller and validates it joined the right controller.



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* filetransferutils
    * Common
        * Added statement to handle 'Abort Copy?[confirm]' prompt

* common
    * Modified pattern for overwrite prompt
    * Modified filetransferutils
        * Added 'No such file or directory' error pattern

* generic
    * Modfied filetransferutils to pick up custom error patterns from testbed.custom section



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
    * Modified configure_static_nat_rule API
        * API for configuring static nat rule with udp port
    * Modified unconfigure_static_nat_rule API
        * API for unconfiguring static nat rule with udp port
    * Fix SISF API get_ip_theft_syslogs
        * Update regex to consider another variation
    * Modified verify_mpls_mroute_groupip api
        * Added next_hop argument to get the mapped lspvif interface
    * Modified verify_mpls_forwarding_table_vrf_mdt api
        * added a condition on failure, if 'prefix_no' is not 0 and traffic is not flowing, returned False. As by default traffic wont be runningi on prefix mdt 0
    * Modified verify_mpls_forwarding_table_gid_counter api
        * Added a expected_prefix_exempted condition on failure, as there will be default prefixes learnet which will not learn any traffic
    * Updated `verify_ping` API to use minimum success rate of 1 percent
    * Updated 'Install_Image' Clean Stage API
        * Updated install_add_one_shot_dialog to accept success if same image is already loaded.
    * Updated health_memory API
        * Fix a bug when passing command argument
    * Updated configure_ospf_routing API
        * configure_ospf_routing api to accept the nsf options, nsr and nsr options configuration.

* blitz
    * Prefixes not handeled correctly when origin is openconfig.

* apis
    * Modified creating the remote path so the files with more than one suffixes

* ios
    * Updated `verify_ping` API to use minimum success rate of 1 percent

* iosxr
    * Updated `verify_ping` API to use minimum success rate of 1 percent

* all
    * Modified setup.py and Makefile
        * pin grpcio version to be less than or equal to 1.36.1 to be in line with yang.connector

* sdk
    * triggers
        * update exclude platform for ha reload.
    * Updated the key value regex to handle unquoted integer key values in the xpath.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added 'configure_auto_qos' API
        * configure auto qos policy under interface
    * Added 'unconfigure_auto_qos' API
        * unconfigure auto qos policy under interface
    * Added verify_macsec_session API
        * API for verifying MKA MACsec session
    * Added verify_mka_session API
        * API for verifying MKA session
    * Added clear_ip_bgp API
        * API for clear ip bgp *
    * Added clear_mac_address_table_dynamic API
        * API for clear mac address-table dynamic
    * Added configure_cdp_interface API
        * API to configure cdp on interface.
    * Added unconfigure_cdp_interface API
        * API to unconfigure cdp on interface.
    * Added configure_disable_sci_dot1q_clear API
        * API to configure disable-sci and dot1q-in-clear on interface.
    * Added unconfigure_disable_sci_dot1q_clear API
        * API to unconfigure disable-sci and dot1q-in-clear on interface.
    * Added configure_scp_local_auth API
        * API to configure scp parameter with local authentication.
    * Added unconfigure_scp_local_auth API
        * API to configure scp parameter with local authentication.
    * Added execute_clear_platform_software_fed_active_cpu_interface API
        * API for executing clear cpu interface.
    * Added clear_mka_session API
        * API for clearing mka session.
    * Added execute_switch_card_OIR API
        * API for executing switch card OIR.
    * Added fp_switchover API
        * API to perform FP Switchover.
    * Added configure_ikev2_dpd API
        * API for configure ikev2 dpd.
    * Added configure_ikev2_fragmentation API
        * API for configure ikev2 fragmentation.
    * Added configure_ikev2_cac API
        * API for configure ikev2 CAC.
    * Added unconfigure_ikev2_proposal API
        * API for unconfigure ikev2 proposal.
    * Added unconfigure_ikev2_policy API
        * API for unconfigure ikev2 policy.
    * Added unconfigure_ikev2_dpd API
        * API for unconfigure ikev2 dpd.
    * Added unconfigure_ikev2_fragmentation API
        * API for unconfigure ikev2 fragmentation.
    * Added unconfigure_ikev2_cac API
        * API for unconfigure ikev2 CAC.
    * Added unconfigure_ikev2_authorization_policy API
        * API for unconfigure ikev2 authorization policy CAC.
    * Added configure_ipsec_fragmentation API
        * API for configure ipsec fragmentation.
    * Added configure_ipsec_df_bit API
        * API for configure ipsec donot fragment bit.
    * Added configure_ipsec_sa_global API
        * API for configure ipsec security association parameters.
    * Added unconfigure_ipsec_fragmentation API
        * API for unconfigure ipsec fragmentation.
    * Added unconfigure_ipsec_df_bit API
        * API for unconfigure ipsec donot fragment bit.
    * Added unconfigure_ipsec_sa_global API
        * API for unconfigure ipsec security association parameters.
    * Added get_component_details API
        * API for getting components' details (name, description, part number, serial number, hardware version)
    * Added get_component_description API
        * API for getting components' description
    * Added get_hardware_version API
        * API for getting components' hardware version
    * Added configure_mka_macsec API
        * API for configure mka macsec on interface.
    * Added unconfigure_mka_macsec API
        * API to unconfigure mka macsec on interface.
    * Added remove_ntp_master API
        * API to remove ntp master on interface.
    * Added configure_mdns_service_record_ttl API
        * API for configuring mDNS(Multicast Domain Name System) service record TTL value.
    * Added configure_mdns_service_receiver_purge_timer API
        * API for configuring mDNS(Multicast Domain Name System) service receiver Timer value.
    * Added configure_mdns_query_response_mode API
        * API for configuring mDNS(Multicast Domain Name System) query response mode.
    * Added configure_nat_route_map API
        * API for configuring a route-map in NAT feature.
    * Added unconfigure_nat_route_map API
        * API for unconfiguring a route-map in NAT feature.
    * Added configure_nat_extended_acl API
        * API for configuring a extended acl in NAT feature.
    * Added verify_ipv6_pim_neighbor API
        * verifies ipv6 pim neighbor on device
    * Added verify_acl_info_summary API
        * verifies acl summary on device
    * Added verify_ipv6_dhcp_pool
        * verifies ipv6 dhcp pool
    * Added verify_ipv6_ospf_neighbor_address_in_state
        * verifies ipv6 ospf neighbor
    * Added verify_ipv6_ospf_neighbor_addresses_are_not_listed
        * verifies ipv6 ospf neighbor not listed
    * Added get_ipv6_ospf_neighbor_address_in_state
        * get ipv6 ospfneighbor address
    * Added configure_bfd_neighbor_on_interface
        * configures bfd neighbor on interface
    * Added unconfigure_bfd_neighbor_on_interface
        * unconfigures bfd neighbor on interface
    * Added verify_acl_log
        * verifies acl log
    * Added verify_object_manager_error_objects_statistics
        * verifies error object stats
    * Added get_slice_id_of_interface
        * get slice id of interface
    * Added verify_ipv6_acl_tcam_utilization
        * verifies tcm uitilization of acl
    * Added 'execute_card_OIR_remove' API
        * execute card OIR remove API to remove the card
    * Added 'execute_card_OIR_insert' API
        * execute card OIR insert API to insert the card
    * Add disable debug API
    * Add clear matm table dynamic API
    * Added interface_counter_check api
        * Verifies packet flow on interface
    * Add EVPN API change_nve_source_interface
        * Added new API to change NVE source-interface IP
    * Added clear device-tracking database trigger
        * clear device-tracking database trigger added
    * Added 'verify_nve_evni_peer_ip_state' API
        * check whether evni for a given peer_ip is UP/DOWN
    * Added 'configure_crypto_ikev2_NAT_keepalive' API
        * configure crypto ikev2 nat keepalive <keepalive time>
    * Added 'unconfigure_crypto_ikev2_NAT_keepalive' API
        * unconfigure crypto ikev2 nat keepalive <keepalive time>
    * Added configure_boot_manual API
        * configure boot manual on device
    * Added configure_crypto_pki_server
        * Added new api to configure crypto pki server
    * Added configure_trustpoint
        * Added new api to configure crypto pki trustpoint
    * Added unconfigure_crypto_pki_server
        * Added new api to unconfigure crypto pki server
    * Added 'configure_crypto_ikev2_policy' API
        * configure crypto ikev2 policy <poicy_name>
    * Added 'unconfigure_crypto_ikev2_policy' API
        * unconfigure crypto ikev2 policy <policy_name>
    * Added 'configure_crypto_ikev2_proposal' API
        * configure crypto ikev2 proposal <proposal_name>
    * Added 'unconfigure_crypto_ikev2_proposal' API
        * unconfigure crypto ikev2 proposal <proposal_name>
    * Updated 'execute_card_OIR' API
        * execute card OIR updated to accept switch number for HA/SVL systems
    * Added configure_interface_switchport_pvlan_and_native_vlan API
        * Configuring switchport pvlan mode on Interface
    * Added configure_interface_switchport_pvlan_association API
        * Configuring switchport pvlan association on Interface
    * Added configure_interface_switchport_pvlan_mapping API
        * Configuring switchport pvlan mapping on Interface
    * Added configure_interface_pvlan_mode_with_submode API
        * Configuring switchport pvlan mode with submode on Interface
    * Added get_software_version API
        * API for getting a device software version info
    * Added get_firmware_version API
        * API for getting components' firmware version in CAT 9600 and 9400 series
    * Added removeMissingComp API
        * API for removing components that are in CLI but are not present in GNMI query
    * Added new configure_shape_map API
        * configure queuing shape-map on device
    * Added configure_vlan_shutdown API
        * Added new api to shutdown the data vlan
    * Added unconfigure_vlan_configuration API
        * Added new api to unconfigure the vlan configuration
    * Added unconfigure_mdns_location_filter API
        * Added new api to unconfigure the mdns location filter
    * Added configure_ospf_redistributed_static API
        * Added new api to configure the ospf params redistribute static
    * Added configure_bgp_update_delay API
        * Added new api to configu bgp params update delay
    * Added 'configure_crypto_ipsec_nat_transparency' API
        * configure/unconfigure crypto ipsec nat-transparency udp-encapsulation

* cheetah
    * Added verify_operation_state
        * Added new api to verify operation state of AP
    * Added verify_controller_name
        * Added new api to verify controller name to which AP has joined
    * Added verify_controller_ip
        * Added new api to verify controller IP/IPv6 address to which AP has joined
    * Added get_ap_mode
        * Added new api to get AP Mode
    * Added get_operation_state
        * Added new api to get AP Operation state
    * Added get_controller_name
        * Added new api to get controller name to which AP has joined
    * Added get_ip_address
        * Added new api to get controller IP/IPv6 address to which AP has joined
    * Added get_ip_prefer_mode
        * Added new api to get AP IP preferred mode.
    * Added execute_prime_ap
        * Added new file called execute.py where all execute commands can be written
        * Added api to execute command that primes AP to the controller
    * Added execute_erase_ap
        * Added api to execute command that erases the configurations of AP

* nxos
    * Added the following process restart test triggers
        * TriggerProcessKillRestartMonitor
        * TriggerProcessCrashRestartMonitor
        * TriggerProcessKillRestartIntersight
        * TriggerProcessCrashRestartIntersight
        * TriggerProcessKillRestartNXOSDC
        * TriggerProcessCrashRestartNXOSDC

* <iosxe>
    * Added API for execute_test_idprom_fake_insert
        * test idprom interface {interface} fake-insert
    * Added API for execute_test_idprom_fake_remove
        * test idprom interface {interface} fake-remove
    * Added API for configure_stackwise_virtual_dual_active_interfaces
        * interface {interface}; stackwise-virtual dual-active-detection
    * Added API for unconfigure_stackwise_virtual_dual_active_interfaces
        * interface {interface}; no stackwise-virtual dual-active-detection
    * Added API for configure_global_dual_active_recovery_reload_disable
        * stackwise-virtual; dual-active recovery-reload-disable
    * Added API for unconfigure_global_dual_active_recovery_reload_disable
        * stackwise-virtual; no dual-active recovery-reload-disable
    * Added API for configure_stackwise_virtual_dual_active_pagp
        * stackwise-virtual; dual-active detection pagp; dual-active detection pagp trust channel-group {port_channel}
    * Added API for unconfigure_stackwise_virtual_dual_active_pagp
        * stackwise-virtual; no dual-active detection pagp trust channel-group {port_channel}

* blitz
    * Added Negative Test banner
        * Negative Test banner will show if it is Negative Test
    * Yang action
        * Added support for include/exclude
        * Added sequence key to support return values and return sequence verified



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPolicyMapTypeQueueingInterfaceOutput parser
        * show call policy-map type queuing
    * Added ShowPppoeSession
        * for 'show pppoe session'
    * Added ShowPppoeSummary
        * for 'show pppoe summary'
    * Added ShowPlatformHardwareFedActiveTcamUtilization under new directory c9606r
        * show platform hardware fed active fwd-asic resource tcam utilization
    * Added 'ShowCryptoIkev2Proposal' schema and parser
        * show crypto ikev2 proposal
    * Added 'ShowCryptoIkev2Policy' schema and parser
        * show crypto ikev2 policy
    * Added 'ShowCryptoIpsecProfile' schema and parser
        * show crypto ipsec profile
    * Added ShowFlowMonitor parser for 9400 platform
        * Parser for show flow monitor cli
    * Added "flow_monitor_output" field in ShowRunInterface parser
        * To match "ip flow monitor monitor_ipv4_out output" config
    * Added ShowIpBgpMdtVrf parser
        * show ip bgp {address_family} mdt vrf {vrf}
    * Added ShowPlatformHardwareFedActiveQosSchedule parser
        * show platform software fed active qos schedule
    * Added ShowSdwanAppfwdCflowdStatistics
        * for 'show sdwan app-fwd cflowd statistics'
    * Added ShowSdwanAppfwdCflowdFlowCount
        * for 'show sdwan app-fwd cflowd flow-count'
    * Added ShowVrrpDetail
        * for 'show vrrp detail'
    * Added ShowVrrpVpn
        * for 'show vrrp vpn <vpn_ID>'
    * Added ShowLispRemoteLocatorSet
        * 'show lisp remote-locator-set {remote_locator_type}'
        * 'show lisp remote-locator-set name {remote_locator_name}'
        * 'show lisp {lisp_id} remote-locator-set {remote_locator_type}'
        * 'show lisp {lisp_id} remote-locator-set name {remote_locator_name}'
    * Added ShowPlatformHardwareFedActiveVlanIngress parser
        * show platform hardware fed active vlan <num> ingress
    * Added ShowIpArpInspectionVlan parser
        * show ip arp inspection vlan <num>
    * Added ShowControllers
        * for 'show controllers'
    * Added ShowSdwanSdwaAppFwdDpiSummary
        * for 'show sdwan app-fwd dpi summary'
    * Added ShowControlConnectionHistory
        * for 'show sdwan control connection-history'
    * Added ShowCryptoSockets
        * Parser for show crypto sockets
    * Added ShowCryptoMibIpsecFlowmibGlobal
        * Parser for show crypto mib ipsec flowmib global
    * Added ShowCryptoIpsecInternalDual
        * Parser for show crypto ipsec internal dual
    * Added ShowEndpointTrackerRecords
        * for 'show endpoint-tracker records'
    * Added ShowEndpointTrackerStaticRoute
        * for 'show endpoint-tracker static-route'
    * Added ShowEndpointTrackerTrackerGroup
        * for 'show endpoint-tracker tracker-group'
    * Added 'ShowGroupPolicyTrafficSteeringPolicy' schema and parser
        * show group-policy traffic-steering policy sgt
    * Added 'ShowGroupPolicyTrafficSteeringEntries' schema and parser
        * show group-policy traffic-steering entries
    * Added 'ShowGroupPolicyTrafficSteeringCounters' schema and parser
        * show group-policy traffic-steering counters
    * Added 'ShowGroupPolicyTrafficSteeringPermissions' schema and parser
        * show group-policy traffic-steering permissions
    * Added ShowHardwareLed
        * show hardware led
    * Added ShowHardwareLedPort
        * show hardware led port {port}
    * Added ShowIpSlaResponder
        * show ip sla responder
    * Updated ShowIpSlaResponder
        * Added option parameters for show ip sla responder schema
    * Added ShowIpv6DhcpBinding
        * Parser for 'show ipv6 dhcp binding'
    * Added ShowIpv6DhcpStatistics
        * Parser for 'show ipv6 dhcp statistics'
    * ShowIsisDatabase
        * show isis database
        * show isis database verbose
    * Added 'ShowL2tpTunnel' schema and parser
        * show l2tp tunnel
    * Added show_platform_ifm_mapping
        * show platform software fed {switch} {state} ifm mappings
        * show platform software fed active ifm mappings
    * Added 'ShowLldpTrafficInterface' schema and parser
        * show lldp traffic interface {id}
    * Added 'ShowCryptoIkev2StatsExchange' schema and parser
        * show crypto ikev2 stats exchange
    * Added ShowPlatformPktTraceStats
        * show packet-trace statistics
    * Added ShowPlatformPktTraceSummary
        * show platform packet-trace summary
    * Added ShowPlatformPacketTracePacket
        * show platform packet-trace packet all
    * Modified ShowIsisRib
        * Added the "from_srapp" feature to the schema
    * Added ShowIsisNodeLevel
        * show isis node {level}
    * Added ShowStackwiseVirtualDualActiveDetectionPagp
        * show stackwise-virtual dual-active-detection Pagp
    * Added 'ShowMdnsSdCacheInvalid' Parser
        * Parser for show mDNS(Multicasr Domain name services)sd cache invalid
    * Added ShowPppStatistics
        * parser for show ppp statistics
    * Added ShowFipsAuthorizationKey
        * Added 'show fips authorization-key'
    * Below are the new parsers added for Hawkeye feature
        * Added show platform software steering-policy forwarding-manager {switch} R0 permissions ipV4 {sgt} {dgt}
        * Added show platform software steering-policy forwarding-manager switch {switch} F0 policy-summary
        * Added show platform software steering-policy forwarding-manager F0 policy-summary
        * Added show platform software steering-policy forwarding-manager switch {switch} F0 cell-info
        * Added show platform software steering-policy forwarding-manager F0 cell-info
        * Added show platform software steering-policy forwarding-manager switch {switch} F0 service-all
        * Added show platform software steering-policy forwarding-manager F0 service-all
        * Added show platform software steering-policy forwarding-manager switch {switch} r0 service-id {service_id}
        * Added show platform software steering-policy forwarding-manager r0 service-id {service_id}
        * Added show platform software fed {switch} active security-fed sis-redirect firewall all
        * Added show platform software fed active security-fed sis-redirect firewall all
        * Added show platform software fed {switch} active security-fed sis-redirect firewall service-id {service_id} detail
        * Added show platform software fed active security-fed sis-redirect firewall service-id {service_id} detail
        * Added show platform software fed {switch} active security-fed sis-redirect acl all
        * Added show platform software fed active security-fed sis-redirect acl all
    * Added 'ShowCryptoIkev2Sa' schema and parser
        * show crypto ikev2 sa
    * Added ShowCryptoIpsecSaDetail
        * show crypto ipsec sa detail
    * Added ShowCryptoIpsecSa
        * show crypto ipsec sa
    * Added ShowCryptoIpsecSaPeerDetail
        * show crypto ipsec sa peer {} detail
    * Added ShowCryptoIpsecSaPeer
        * show crypto ipsec sa peer {}
    * Added ShowRunningConfigNve
        * show running-config nve
    * Added ShowRunningConfigNve
        * show running-config nve

* iosxr
    * Added ShowEvpnEviInclusiveMulticast
        * 'show evpn evi inclusive-multicast'
        * 'show evpn evi vpn-id {vpn_id} inclusive-multicast'
    * Added ShowEvpnEviInclusiveMulticastDetail
        * 'show evpn evi inclusive-multicast detail'
        * 'show evpn evi vpn-id {vpn_id} inclusive-multicast detail'
    * Added showEvpnInternalId
        * 'show evpn internal-id'
        * 'show evpn internal-id vpn-id {vpn-id}'
    * Added showEvpnInternalIdDetail
        * 'show evpn internal-id detail'
        * 'show evpn internal-id vpn-id {vpn-id} detail'
    * Added ShowSegmentRoutingSrv6LocatorSid
        * show segment-routing srv6 sid
        * show segment-routing srv6 locator {locator} sid
    * Added ShowSnmp
        * show snmp
        * show snmp host

* nxos
    * Added "Show fabric multicast ipv4  mroute parser
        * show fabric Multicast ipv4 vrf all
        * show fabric Multicast ipv4  vrf <vrf_name>

* viptela
    * Added ShowIpRoutes parser
        * show ip routes
        * show ip routes <prefix>
        * show ip routes vpn <vpn>
        * show ip routes vpn <vpn> <prefix>


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowRomvar
        * changed schema key <ps1> to Optional
        * added Optional schema key <abnormal_reset_count>
    * Modified ShowLispEidAway
        * Changed <eid_prefix> from schema to Optional
    * Modified ShowLispInstanceIdService
        * Changed <xtr_id> and <site_id> from schema to Optional
    * Modified ShowIpCefSchema
        * Changed <nexthop> from schema to Optional
    * Modified ShowIsisDatabaseDetail
        * Converted the base parser to a super parser
    * Modified ShowRunningConfigAAAUsername
        * To support more varied output
    * Modified Convert_intf_name
        * Modified Convert_intf_name function to expand Fou - FourHundredGigE.
    * Modified ShowLispServiceStatistics
        * The existing schema does not properly represent the output of the show command So fixed all the schema and updated code accordingly. Note This change is NOT backwards compatible.
    * Modified ShowIpMfib
        * merged the comments addressed / committed in ShowIpv6Mfib  to  ShowIpMfib
    * Modified ShowIpMrib
        * initialization of dictionary variable was moved before first match was executed
    * Modified ShowIsisRib
        * Added the functionality to parse a rib entry where the first line is only a single IP
    * Modified ShowMplsMldpRoot
        * Modified interface field regex to grep all kind of interfaces
    * Modified ShowMplsMldpNeighbors
        * Modified LDP GR regex to grep all kind of states
    * Modified ShowBgp
        * Modified prefix field in p3_1 regex to consider \*
    * Modified ShowSdwanOmpRoutes
        * Return the prefix and VPN to the upstream Viptela class parser.
    * Modified ShowPlatformTcamPbr Parser
        * Modified ShowPlatformTcamPbr schema to use Any() for output specific and also modified cli_command to run on  Standalone and HA setup.
    * Modified ShowPlatformSoftwareFedSwitchActivePuntCpuq
        * Modified ShowPlatformSoftwareFedSwitchActivePuntCpuq cli_command to run on Standalone and HA setup.
    * Modified ShowStackwiseVirtualDualActiveDetection
        * Covered parsing of entire output which was missing in existing Parser
    * Modified 'ShowMdnsSdQueryDb' Parser
        * Added new variables in schmea as optional for the latest release
    * Modified 'ShowMdnsSdSummary' Parser
        * Added new variables in schema as optional for the latest release
    * Modified show_run
        * changed regex pattern <p1_1> to match optional policy-map type queueing
    * Modified ShowVlanId
        * changed schema key <ports> to Optional
        * changed regexp pattern to match optional ports field
    * Modified ShowVrf
        * changed schema key <protocols> to Optional
        * changed regexp pattern to match optional protocol field
    * Modified ShowVersion
        * Added optional key <installation_mode> to schema
    * Modified ShowWirelessClientMacDetail
        * Added missing keys
        * Optionalized keys that aren't consistent
        * current_rate and vlan now record types correctly
    * Modified ShowIpMroute
        * Updated ShowIpMrouteSchema with optional keys <vxlan_version>,<vxlan_vni>,<vxlan_nxthop>
        * Updated regex pattern of outgoing interface list by including another line to accomodate vxlan
    * Modified ShowStackwiseVirtualLink
        * Updated schema to properly support device output. This is not backwards compatible.
    * Modified ShowPlatformSoftwareObjectManagerFpActiveStatistics parser
        * Added "show platform software object-manager switch {switchstate} {serviceprocessor} active statistics" cli
    * Modified ShowInterfaces{interface} parser
        * Added optional keys <tunnel_source_ip>, <tunnel_destnation_ip>, <tunnel_protocol>, <tunnel_ttl>, <tunnel_transport_mtu>, <tunnel_transmit_bandwidth>, <tunnel_receive_bandwidth> into the schema.
    * Modified ShowMacsecInterfaceSchema
        * Changed few values of macsec-data key as optional.
    * Modified ShowRunningConfigAAAUsername
        * To support more varied output
    * Modified ShowWirelessProfilePolicyDetailed
        * Added format for policy_name argument
    * Modified ShowTelemetryIETFSubscriptionReceiver
        * Added "name" field to schema to account for named receivers
        * Added regex pattern <p9> for newly added "name" field
        * Updated regex pattern <p7> to accommodate for multi-word entries
    * Modified ShowTelemetryConnectionAll
        * Strip entry under 'VRF' from letter 'M' that might be present in output

* nxos
    * Fixed Show Fabic Multicast ipv4  sa-ad route parser
        * Fixed the regular expression while parsing the output

* asa
    * Modified ShowInterfacesSummary
        * Updated regex pattern p1 to accommodate various outputs.
    * Modified ShowVersion
        * Made certain keys optional
        * Added optional key for SSP Slot Number
    * Modified ShowInventory
        * Updated regex patterns p1 and p2 to accommodate various outputs.
        * Added another file for unit testing

* iosxr
    * Modified ShowLldpEntry
        * Added the "age" feature to the schema
    * Modified ShowLldpTraffic
        * Added the "tlv_accepted" feature to the schema
        * Added the "last_clear" feature to the schema
    * Modified ShowPolicyMapInterface Parser, update pattern p2 input direction
    * Updated showEvpnInternalId
        * Updated p1 pattern to include hex value for esi in 'show evpn internal-id'

* viptela
    * Modified ShowOmpRoutes
        * Added "route_info" variable to correctly populate the parsed_dict dictionary.
        * Added vpn/vrf variable to dynamically populate the correct VPN used.

* cheetah
    * Modified ShowCapwapClientRcb
        * Made "mwar_name" as optional string
    * Modified ShowCapwapClientRcb
        * Made "ap_tcp_mss_size" as optional string
        * Added "flex_group_name" as new key,value pair

* dnac
    * Updated Interface
        * Added additional keys
