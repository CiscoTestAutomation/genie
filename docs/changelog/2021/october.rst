October 2021
==========

October 25 - Genie v21.10
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.10                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.10                         |
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

* harness
    * Modified trigger data loading to add raw testdata data to object for use with SHA256 hash
    * Modified GeneTrigger and TestcaseVerification classes
    * Modified TestScript class
    * Modified load_atrribute() in utils.py
        * Module import statement is now in a try/except to avoid ModuleNotFound errors

* conf
    * Modified Jinja2 conf
        * Updated conf via Jinja2 to run on devices in parallel



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* generic
    * Modified 'reload' clean stage, fixed check_modules logic

* iosxe/sdwan
    * Fixed 'image' handling in 'tftp_boot' stage
    * Updated ERROR_PATTERN in 'connect' stage
    * Changed clean stage name from 'controller_mode' to 'set_controller_mode'

* all
    * Modified CleanTestcase - Cisco Internal Change
        * Telemetry data collection now uses stage order instead of all defined stages
    * Modified CleanTestcase - Cisco Internal Change
        * Telemetry data is no longer collected in genie.libs.clean

* com
    * Modified copy_to_device stage
        * To reply to the overwrite prompt if the file exists when copying
    * Modified Device Recovery
        * Fixed a bug where break_count would default to None when it should be an integer.
    * Modified PingServer
        * To fix a bug where the server name would not be resolved into an IP address


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe/sdwan
    * added 'delete_inactive_versions' option to 'controller_mode' stage
        * delete inactive versions after changing software



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified test_dot1q_tunnel_interface
        * Fixed dot1q tunnel unit test in interface tests.



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Modified filetransferutils
        * protocol identification string lack carriage return
        * no such file or directory (invalid server)



genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health plugin
    * Fixed --health-show-logging-keywords argument
        * to handle given keywords properly



genie.libs.ops
""""""""""""""

genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* api utils
    * Modified api_unittest_generator
        * Fixed module and module-path arguments to remove OS dependency.

* iosxe
    * Modified configure_ospf_routing API
        * Updated the doc string
    * Modified configure_ospfv3 API
        * Updated the doc string
    * Modified clear_interface_interfaces API
        * Updated the doc string
    * Modifed config_mka_policy_xpn API
        * Added sak_rekey_int, key_server_priority arguments
    * Modified config_macsec_keychain_on_device API
        * Added lifetime argument
    * Modified enable_ipv6_unicast_routing API
        * Updated device type in doc string
    * Modified config_wan_macsec_on_interface API
        * Added new argument dot1q_clear
    * Modified config_macsec_keychain_on_device API
        * Updated new arguments
    * Modified trigger_datafile_iosxe.yaml
        * Removed frames_tolerance as a parameter from the compare_traffic_profile postprocessor as it was causing an unexpected keyword argument error
    * Modified
        * Modified copy_file_to_running_config API
            * Modified the API to pass timeout value as an argument
    * Modified API verify_acl_usage
        * Updated API to accomodate the enhancement of ShowPlatformSoftwareFedActiveAclUsage Parser.
    * Add timeout.sleep() calls to polling loops that are missing them
    * Fix verify_ip_mac_binding_in_network to use device.parse() over device.parser()
    * Modify configure functions that directly access optional keys in dictionaries to use .get() to be more safe

* nxos
    * Modified API 'health_core'
        * Added remote_path support for http protocol
    * Modified _is_boot_variable_as_expected
        * To fix a bug where no boot variables were parsed but the parser was not empty.

* ios
    * Modified trigger_datafile_ios.yaml
        * Removed frames_tolerance as a parameter from the compare_traffic_profile postprocessor as it was causing an unexpected keyword argument error

* modified load_jinja_template api
    * Added error message in case template is not found


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_l2vpn_vfi_context_vpls API
        * Configures l2vpn vfi context vpls on device
    * Added unconfigure_l2vpn_vfi_context_vpls API
        * Unconfigures l2vpn vfi context vpls on device
    * Added configure_encapsulation_mpls_ldp API
        * Configures encapsulation mpls ldp on interface
    * Added configure_vlan_vpls API
        * Configures vpls on vlan
    * Added unconfigure_vlan_vpls API
        * Unconfigures vpls on vlan
    * Updated API 'verify_ptp_states' due to small parser changes
    * Updated API 'verify_ptp_platform_fed_results' due to small parser changes
    * Updated API 'verify_ptp_clock' due to small parser changes
    * Updated API 'verify_ptp_counters' due to small parser changes
    * Updated API 'verify_ptp_parent' due to small parser changes
    * Added 'clear_ip_nat_translation_all' API
        * clear ip nat translation *
    * Added 'clear_flow_monitor' API
        * clear flow monitor with name and options
    * Added 'clear_ipv6_mfib_vrf_counters' API
        * clear all ipv6 mfib vrf counter or for perticular
    * Added 'clear_access_list_counters' API
        * clear all access-list counters or with perticular options
    * Added 'clear_ip_mroute_all' API
        * clear ip mroute all
    * Added configure_default_gateway API
        * Configures default gateway
    * Added config_vlan_tag_native API
        * Configures vlan dot1q tag native on device
    * Added config_vlan_tag_native API
        * Unconfigures vlan dot1q tag native on device
    * Added config_license API
        * Configures license on device
    * Added API verify_template_bind
    * Added configure_tacacs_server
    * Added export_packet_capture
    * added `remove_ipv6_dhcp_guard_policy` API
    * added `remove_ipv6_nd_suppress_policy` API
    * added `remove_single_device_tracking_policy` API
    * added `remove_ipv6_source_guard_policy` API
    * added `clear_device_tracking_database` API
    * added `clear_device_tracking_counters` API
    * Added get_auth_session API
        * API for getting the dot1x/mab authentication session
    * Added get_radius_packets API
        * API for getting the radius packets from pcap file
    * Added get_packet_attributes_scapy API
        * API for getting the attribute value pairs from a packet
    * Added get_packet_info_field API
        * API for getting the packet info(code field) from a packet
    * Added get_ip_packet_scapy API
        * API for getting the IP layer from a packet
    * Added get_packet_ip_tos_field API
        * API for getting the types of services field from a packet
    * Added configure_enable_aes_encryption API
        * API for enabling aes password encryption
    * Added configure_disable_aes_encryption API
        * API for disabling aes password encryption
    * Added API `get_snmp_snmpwalk`
    * Added API `configure_snmp`
    * Added API `unconfigure_snmp`
    * Added get_bgp_rt2_community_label API
        * Gets external-community, label info from route-type 2 that
        * matches with specific ip and mac
    * Added get_bgp_rt5_community_paths_label API
        * Gets external-community, label, path from route-type 5 that
        * matches with specific ip address
    * Added verify_bgp_rt2_route_target API
        * Checks for specific Route Target from route-type 2 output
    * Added verify_bgp_rt5_reoriginated_from API
        * Checks for re-origination path from route-type 5 output
    * Added verify_bgp_rt5_route_target API
        * Verifies Route Target from route-type 5 output
    * Added verify_bgp_rt5_label API
        * Verifies for specific label from route-type 5 output
    * Added verify_bgp_rt2_label API
        * Verifies for specifi label from route-type 2 output
    * Added get_arp_interface_mac_from_ip API
        * Gets a list of mac and outgoing interface of specific route
    * Added verify_arp_vrf_interface_mac_entry API
        * Verifies for specific mac and outgoing interface in arp table
    * Added unconfigure_vlan_config API
        * Unconfigs vlan in config level
    * Added get_routing_vrf_entries API
        * Gets route entris from specific vrf route
    * Added verify_routing_subnet_entry API
        * Verifies for specific route entry
    * Added configure_evpn_instance_vlan_based_with_reoriginate_rt5 API
        * Configures evpn vlan instance with re-originate RT5 in it
    * Added unconfigure_evpn_instance_vlan_based API
        * Unconfigs evpn vlan instance with re-originate RT5 in it
    * Added 'clear_platform_software_fed_active_acl_counters_hardware' API
        * to clear acl hardware counters on device
    * Added API `configure_interface_switchport_trunk_vlan`
    * Added 'configure_ip_mtu' API
        * configure mtu value under interface
    * Added 'unconfigure_ip_mtu' API
        * unconfigure mtu value under interface
    * Added configure_radius_interface_vrf API
        * Configures RADIUS source interface via VRF
    * Added unconfigure_radius_interface_vrf API
        * Unconfigures RADIUS source interface via VRF
    * Added configure_eapol_dest_address_interface API
        * Configures EAPOL Destination address on interface
    * Added unconfigure_eapol_dest_address_interface API
        * Unconfigures EAPOL Destination address from interface
    * Added API verify_device_tracking_counters_interface
    * Added API verify_device_tracking_counters_vlan
    * Added API configure_device_tracking_binding_options
    * Added API unconfigure_device_tracking_binding_options
    * Added decrypt_tacacs_pcap
    * Added parse_tacacs_packet
    * Added verify_tacacs_packet
    * Added 'configure_mdns' API
        * Configures mDNS(Multicasr Domain name services)
    * Added 'unconfigure_mdns_config' API
        * Unconfigures mDNS(Multicasr Domain name services)
    * Added 'configure_vlan_agent' API
        * Configures vlan agent
    * Added 'unconfigure_mdns_vlan' API
        * Unconfigures mDNS vlan
    * Added 'configure_vlan_sp' API
        * Configures vlan sp(Service Peer)
    * Added 'configure_mdns_location_filter' API
        * Configures mDNS location filter
    * Added 'configure_mdns_location_group' API
        * Configures mDNS location group
    * Added 'configure_mdns_sd_agent' API
        * Configures mdns sd agent
    * Added 'configure_mdns_sd_service_peer' API
        * Configures mdns sd service peer
    * Added 'configure_mdns_trust' API
        * Configures mdns trust
    * Added 'configure_mdns_service_definition' API
        * Configures mdns service definition
    * Added perform_ssh
    * Added concurrent_ssh_sessions

* linux
    * Added `scp` API for linux os

* blitz
    * actions
        * Added dialog action to handle dialog interactions
    * actions_helper
        * Added dialog_handler to process dialog interactions

* sdk
    * Added RestconfRequestBuilder class, run_restconf, dict to XML conversion, and map to determine function to run based on protocol


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified export_packet_capture



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowTrackBrief
        * Added parser for
            * show track interface brief
            * show track ip sla brief
            * show track ip route brief
            * show track ipv6 route brief
    * added ShowTrackListBrief
        * show track list boolean and brief
        * show track list boolean or brief
        * show track list threshold percentage brief
        * show track list threshold weight brief

* iosxe
    * Added ShowEnvironmentStatus
        * show environment status
    * Added ShowPlatformSudiCertificate
        * show platform sudi certificate sign nonce {signature}
    * Added class ShowLispIpv6Publication
        * show lisp instance-id {instance_id} ipv6 publication
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publication
        * show lisp eid-table {eid-table} ipv6 publication
        * show lisp eid-table vrf {vrf} ipv6 publication
        * show lisp locator-table {vrf} instance-id {instance-id} ipv6 publication
    * Added ShowStormControl
        * added a new parser to parse 'show storm-control {interface}' output on IOS XE devices
    * Added class ShowLispEthernetPublication
        * show lisp instance-id {instance_id} ethernet publication
        * show lisp {lisp_id} instance-id {instance_id} ethernet publication
        * show lisp locator-table {vrf} instance-id {instance-id} ethernet publication
    * Added class ShowLispEthernetPublicationPrefix
        * show lisp instance-id {instance_id} ethernet publication {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ethernet publication {eid_prefix}
        * show lisp eid-table vlan {vlan} ethernet publication {eid_prefix}
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
    * Added ShowUdldInterface
        * show udld interface {interface}
    * Added ShowUdldNeighbor
        * show udld neighbor
    * ShowLispIpv4PublisherRloc
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
        * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
        * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
        * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
        * show lisp eid-table vrf ipv4 publisher {publisher_id}
    * Added ShowLispPrefixList
        * show lisp prefix-list
        * show lisp prefix-list {prefix_list_name}
        * show lisp {lisp_id} prefix-list
        * show lisp {lisp_id} prefix-list {prefix_list_name}
    * Added ShowParser
        * show parser encrypt file status
    * Added ShowBootSystem
        * show boot system
    * Added ShowPost
        * show post
    * Added ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobal
        * show platform hardware qfp active feature sdwan datapath fec global
    * Added ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummary
        * show platform hardware qfp active feature sdwan datapath fec session summary
    * Added ShowSdwanAppRouteSlaClass
        * show sdwan app-route sla-class
        * show sdwan app-route sla-class name <name>
    * Added ShowSdwanAppRouteStatistics
        * show sdwan app-route stats local-color <color>
        * show sdwan app-route stats remote-color <color>
        * show sdwan app-route stats remote-system-ip <ip>
    * Added ShowSdwanTunnelSla
        * show sdwan tunnel sla
        * show sdwan tunnel sla index <index>
        * show sdwan tunnel sla name <name>
        * show sdwan tunnel remote-system-ip <ip> sla
    * Added ShowSdwanTunnelStatistics
        * show sdwan tunnel statistics
        * show sdwan tunnel statistics fec
        * show sdwan tunnel statistics bfd
        * show sdwan tunnel statistics ipsec
        * show sdwan tunnel statistics pkt-dup
        * show sdwan tunnel statistics table
    * Added ShowSdwanSystemOnDemand
        * show sdwan system on-demand
        * show sdwan system on-demand remote-system
        * show sdwan system on-demand remote-system system-ip <ip>
    * Added ShowSdwanAppqoeServiceControllers
        * show sdwan appqoe service-controllers
    * Added ShowServiceInsertionTypeAppqoeClusterSummary
        * show service-insertion type appqoe cluster-summary
    * Added class ShowLispARDetailParser
        * show lisp instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp eid-table vlan {vlan} ethernet server address-resolution {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp instance-id {instance_id} ethernet server address-resolution detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp eid-table vlan {vlan} ethernet server address-resolution detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution detail
    * Added ShowPowerInlineConsumption
        * show power inline consumption
        * show power inline consumption {interface}
    * Added ShowLispIpv4RouteImportMapCache
        * 'show lisp instance-id {instance_id} ipv4 route-import map-cache'
        * 'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid}'
        * 'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache'
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid}'
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp eid-table vrf {vrf} ipv4 route-import map-cache'
        * 'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid}'
        * 'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp eid-table {eid_table} ipv4 route-import map-cache'
        * 'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid}'
        * 'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid_prefix}'
        * 'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache'
        * 'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid}'
        * 'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
    * Added ShowLispV4PublicationPrefix
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix}'
        * Added 'show lisp eid-table {eid_table} ipv4 publication {eid_prefix}'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication {eid_prefix}'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}'
        * Added 'show lisp instance-id {instance_id} ipv4 publication detail'
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication detail'
        * Added 'show lisp eid-table {eid_table} ipv4 publication detail'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication detail'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication detail'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication detail'
    * Added ShowLispV6PublicationPrefix
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication {eid_prefix}'
        * Added 'show lisp eid-table {eid_table} ipv6 publication {eid_prefix}'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication {eid_prefix}'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}'
        * Added 'show lisp instance-id {instance_id} ipv6 publication detail'
        * Added 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication detail'
        * Added 'show lisp eid-table {eid_table} ipv6 publication detail'
        * Added 'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication detail'
        * Added 'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication detail'
        * Added 'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication detail'
    * Added ShowL2vpnEvpnDefaultGatewayDetail
        * show l2vpn evpn default-gateway detail
        * show l2vpn evpn default-gateway evi {evi_id} detail
        * show l2vpn evpn default-gateway bridge-domain {bd_id} detail
        * show l2vpn evpn default-gateway vlan {vlan_id} detail
    * Added ShowL2vpnEvpnDefaultGatewaySummary
        * show l2vpn evpn default-gateway summary
        * show l2vpn evpn default-gateway evi {evi_id} summary
        * show l2vpn evpn default-gateway bridge-domain {bd_id} summary
        * show l2vpn evpn default-gateway vlan {vlan_id} summary
    * Added ShowL2vpnEvpnPeersVxlanDetail
        * show l2vpn evpn peers vxlan detail
        * show l2vpn evpn peers vxlan address {peer_addr} detail
        * show l2vpn evpn peers vxlan global detail
        * show l2vpn evpn peers vxlan global address {peer_addr} detail
        * show l2vpn evpn peers vxlan vni {vni_id} detail
        * show l2vpn evpn peers vxlan vni {vni_id} address {peer_addr} detail
        * show l2vpn evpn peers vxlan interface {nve_interface} detail
        * show l2vpn evpn peers vxlan interface {nve_interface} address {peer_addr} detail
    * Added ShowLispSessionRedundancy
        * for 'show lisp session redundancy'
    * Added ShowSnmpMibIfmibIfindexSchema
        * show snmp mib ifmib ifindex
        * show snmp mib ifmib ifindex | include {interface}
    * Added ShowVlansDot1qVlanIdSecondDot1qVlanId
        * show vlans dot1q {first_vlan_id} second-dot1q {second_vlan_id}
    * ShowLispIpv4Subscriber
        * show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber
        * show lisp instance-id {instance_id} ipv4 subscriber
        * show lisp eid-table {eid_table} ipv4 subscriber
        * show lisp eid-table vrf {vrf} ipv4 subscriber
    * ShowLispIpv6Subscriber
        * show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber
        * show lisp instance-id {instance_id} ipv6 subscriber
        * show lisp eid-table {eid_table} ipv6 subscriber
        * show lisp eid-table vrf {vrf} ipv6 subscriber
    * ShowLispEthernetSubscriber
        * show lisp {lisp_id} instance-id {instance_id} ethernet subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber
        * show lisp instance-id {instance_id} ethernet subscriber
        * show lisp eid-table vlan {vlan} ethernet subscriber
    * Added ShowArchiveLogConfig
        * show archive log config all
        * show archive log config {include}
    * Added  ShowArchiveLogStatistics
        * show archive log config statistics
    * Added ShowPlatformSoftwareFedQosPolicyTarget
        * show platform software fed active qos policy target brief
    * Added ShowIpMrouteCount
        * show ip mroute count
    * Added ShowMplsLabelRange
        * show mpls label range
    * Added class ShowLispSessionCapability
        * show lisp vrf {vrf} session capability
    * Modified ShowRunPolicyMap
        * Added set cos
        * Added set precedence
        * Added set dscp
        * Added priority percent
    * Added ShowLispAR
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution
    * Added ShowL2vpnAtomPreferredPath
        * show l2vpn atom preferred-path
    * Added ShowLispIpv4Publisher
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
        * show lisp instance-id {instance_id} ipv4 publisher
        * show lisp eid-table {eid_table} ipv4 publisher
        * show lisp eid-table vrf {vrf} ipv4 publisher
    * Added ShowLispIpv6Publisher
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
        * show lisp instance-id {instance_id} ipv6 publisher
        * show lisp eid-table {eid_table} ipv6 publisher
        * show lisp eid-table vrf {vrf} ipv6 publisher
    * Added ShowLispEthernetPublisher
        * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
        * show lisp instance-id {instance_id} ethernet publisher
        * show lisp eid-table vlan {vlan} ethernet publisher
    * Added ShowCryptoSession
        * show crypto session
    * Added ShowCryptoSessionDetail
        * show crypto session detail
    * Added class ShowLispIpv4Publication
        * show lisp instance-id {instance_id} ipv4 publication
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publication
        * show lisp eid-table {eid-table} ipv4 publication
        * show lisp eid-table vrf {vrf} ipv4 publication
        * show lisp locator-table {vrf} instance-id {instance-id} ipv4 publication
    * Added ShowSegmentRoutingTrafficEngFirstHopResolution
        * show segment-routing traffic-eng first-hop-resolution
        * show segment-routing traffic-eng first-hop-resolution {label}
    * Added ShowLispIpv4Away
        * show lisp instance-id {instance_id} ipv4 away
        * show lisp instance-id {instance_id} ipv4 away {eid}
        * show lisp instance-id {instance_id} ipv4 away {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 away
        * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}
        * show lisp eid-table {eid_table} ipv4 away
        * show lisp eid-table {eid_table} ipv4 away {eid}
        * show lisp eid-table {eid_table} ipv4 away {eid_prefix}
        * show lisp eid-table vrf {eid_table} ipv4 away
        * show lisp eid-table vrf {eid_table} ipv4 away {eid}
        * show lisp eid-table vrf {eid_table} ipv4 away {eid_prefix}
    * Added ShowLispDatabaseEID
        * for 'show lisp instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp {lisp_id} instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp locator-table {vrf} instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp locator-table vrf {vrf} instance-id {instance-id} {address-family} database {prefix}'
        * for 'show lisp eid-table {vrf} {address-family} {prefix}'
        * for 'show lisp eid-table vrf {vrf} {address-family} database {prefix}'
        * for 'show lisp eid-table vlan {vlan_id} {address_family} database {prefix}'
    * Added class ShowLispV4SMRParser
        * show lisp instance-id {instance_id} ipv4 smr
        * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
        * show lisp eid-table {eid_table} ipv4 smr
        * show lisp eid-table vrf {vrf} ipv4 smr
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    * Added class ShowLispV6SMRParser
        * show lisp instance-id {instance_id} ipv4 smr
        * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
        * show lisp eid-table {eid_table} ipv4 smr
        * show lisp eid-table vrf {vrf} ipv4 smr
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    * Added ShowDiagnosticEvent
        * show diagnostic events
    * Added ShowDiagnosticDescriptionModuleTestAll
        * show diagnostic description module {include} test all
    * Added ShowDiagnosticContentModule
        * show diagnostic content module {mod_num}
    * Added ShowDiagnosticResultModuleTestDetail
        * show diagnostic result module {mod_num} test {include} detail

* aireos
    * Added class ShowBoot
        * show boot
    * Added class Ping
        * ping command

* iosxr
    * Added ShowLpts
        * show lpts pifib hardware police

* ios
    * Added ShowEnvironment for ASR901 platform
        * show environment

* show lisp instance-id {instance_id} ethernet server address-resolution


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetailSchema
        * Changed 'bfd_enable' key in schema to str type from bool.
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetail
        * Added support for 'bfd_enable' and 'bfd_mode'
    * Modified ShowBgpInstanceNeighborsAdvertisedRoutes
        * Modified RegEx <p4>,<5_1> to capture dotted Notation ASN
    * Modified ShowIpv6Interface
        * Added 'show ipv6 interface'
    * Modified ShowStaticTopologyDetail
        * Correctly match IPv6 addresses

* iosxe
    * Modified ShowModule
        * Modified show module parser for supporting 9500 device.
    * Modified ShowPlatformIntegrity
        * show platform integrity {signature}
    * Modified ShowServiceInsertionTypeAppqoeServiceNodeGroup
        * Changed schema to support varied iosxe output. Not backwards compatible
    * Modified ShowPlatformHardwareQfpActiveFeatureAppqoe
        * Changed schema to support varied iosxe output. Chnages are backward compatible.
    * Modified ShowSslProxyStatistics
        * Output of the CLI is enhanced with new addtional keys in latest release. Added
    * Modfied ShowTcpProxyStatistics
        * Output of the CLI is enhanced with new addtional keys in latest release. Added
    * Modified ShowPlatformHardwareQfpActiveDatapathUtilSum
        * Changed schema to support varied iosxe output. Chnages are backward compatible.
    * Modified ShowRunInterface
        * Added keepalive key in schema
    * Modified ShowPowerInline
        * Fixed regex pattern <p1> for adding '-' support in oper_state string.
    * ShowIpMrouteCount
        * Added the key type for average
    * ShowMplsLabelRange
        * Coreected merge conflict
    * ShowPlatformSoftwareFedQosPolicyTarget
        * Added state_cfg,state_opr and address keyies
    * Modified ShowIpOspfDatabaseTypeParser
        * Fixed overwritten af variable
        * Fixed issue where sub_tlv variables were referenced before assignment
    * Modified ShowMemoryStatistics
    * Modified ShowRunInterface
        * Added regex pattern <p42 and p43> to accommodate policy config lines
    * Modified ShowRunInterface
        * Corrected merge conflict
    * Modified ShowMplsLabelRange
        * Corrected merge conflict
    * Modified ShowPlatformSoftwareFedQosPolicyTarget
        * Corrected merge conflict
    * Modified ShowLogging
        * Fixed to ignore 'show logging' command syntax line in case it's included
    * Added ShowIpv6Routers
        * show ipv6 routers
    * Added ShowMabAllSummary
        * show mab all summary
    * Modified ShowIsisFlexAlgo
        * Fixed regex, code logic, added additional fields to the schema, and added unit tests
    * Modified ShowStormControl
        * Corrected merge conflict
    * Modified ShowPlatformSoftwareFed
        * Removed ShowPlatformSoftwareFed since it is failing on Jenkin test
    * Modified ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface
        * Changed "if_id" data type from int to str
        * Changed the following keys to optional
            * log_mean_delay_interval
            * log_mean_sync_interval
            * num_delay_requests_received
            * num_delay_responses_received
            * num_delay_requests_transmitted
            * num_delay_responses_transmitted
    * Modified ShowIsisRib
        * Fixed regexes and added new fields to the schema
    * Modified ShowMacsecInterface
        * Changed parser to support multiple receive channels. NOT BACKWARDS COMPATIBLE.
    * Modified Ping
        * Updated parser to support timeout 0 seconds.
    * Modified ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface
        * show platform software fed switch active ptp interface {interface}
    * Modified ShowMplsL2TransportDetail
        * Updated regex to decode multiple labels in imposed label stack
        * Added regex to properly decode output when LDP is down
    * Fixed conflict merge on ShowIpMrouteCount, ShowMplsLabelRange, ShowPlatformSoftwareFedQosPolicyTarget and ShowRunPolicyMap classes
    * Modified ShowL2routeEvpnPeers
        * Updated regex to support varying time format
    * Modified ShowLispAR
        * Fixed UnboundLocalError local variable 'cmd' referenced before assignment
    * Updated ShowInventory
        * Fixed error where subslot dictionary wasn't initialized before accessing
    * Modified ShowMplsForwaringTable
        * Corrected blank label entries going to No Label rather than the correct label
        * Corrected where single entry is split across 2 lines being put into wrong label information
        * Updated parser to handle new "algo" filter
        * Updated parser to ahdnle new flex algo information that may or may not be present
    * Modified ShowVlanAccessMap
        * Changed regexp patter for <p1,p2> to gerp the access-map name and protocol name and value proper
    * Modified ShowVlanFilter
        * Changed regexp patter for <p1> to gerp the vlan_access_map_tag proper

* changed regex to grep 'reserve p'.

* aireos
    * Modified class ShowBoot
        * Fixed accommodate the new output

* common
    * Added 'Wl' 'Wlan-GigabitEthernet' interface mapping in convert_intf_name

* nxos
    * Modified ShowInterface
        * Fix pattern p1 and p1_1 to handle empty 'type'
    * Modified ShowIpv6StaticRoute
        * Correctly match IPv6 addresses
