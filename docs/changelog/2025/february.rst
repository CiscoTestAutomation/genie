February 2025
==========

February 25 - Genie v25.2 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.2 
    ``genie.libs.health``, v25.2 
    ``genie.libs.clean``, v25.2 
    ``genie.libs.conf``, v25.2 
    ``genie.libs.filetransferutils``, v25.2 
    ``genie.libs.ops``, v25.2 
    ``genie.libs.parser``, v25.2 
    ``genie.libs.robot``, v25.2 
    ``genie.libs.sdk``, v25.2 
    ``genie.telemetry``, v25.2 
    ``genie.trafficgen``, v25.2 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* ops
    * Added revisions to ops

* dq
    * Added `condition_level` argument to `get_values`

* json
    * Added standalone makers for apis, ops, clean, models, triggers, and verifications

* abstraction.token
    * Fixed bug with `VersionRange` eq

* genie.abstract
    * Updated version parser
        * support more version formats


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie harness
    * processors
        * Enhanced message for initialize_traffic



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified InstallImage
        * Updated the logic for the device to reload if it does not do


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean-pkg
    * iosxe
        * Modified CopyToDevice
            * Added check not to skip copy_to_device when smu image is provided

* iosxe
    * Modified InstallImage
        * In the show version parsed output, we don't have a 'mode' key. Instead, we have an 'installation_mode' key, from which we retrieve the 'installation_mode' value.

* clean
    * Add quad support
    * Reverted the changes to reload with service wrapper
    * Changed breakout interface behaviour in ConfigureInterfaces stage



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Fix feature service-acceleration
        * change vrf submode config to single line config and update unit tests
        * `vrf vrf1 module-affinity 1` is now in a single line instead of `vrf vrf1\n  module-affinity 1\n exit`
    * Fix interface conf model
        * Subinterfaces can now handle `mac_address` attribute for nxos.

* conf
    * Device
        * Updated Device conf learn_interface_mac_addresses to ignore case
    * Interface
        * Added sp7 and sp8 port speeds
        * IOSXE
            * Moved interface configurations
            * Moved switchport configurations
        * IOSXR
            * Added HundredGigabitEthernetInterface
            * Added FourHundredGigabitEthernetInterface
        * NXOS
            * Changed parent class of VirtualInterface to Interface
            * Added _build_config_interface_submode to PortchannelInterface



genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* ops
    * Updated management ops schema
    * IOSXE
        * Added logger to interface
        * Added include to leaves
        * Added serial number to platform ops
        * Cat9k
            * Added stack discovery
    * NXOS
        * Modified command used into interface ops
        * Modified platform ops
    * Sonic
        * Added kwargs to learn
        * Added kwargs to platform learn
    * IOSXR
        * Added leaves for chassis and chassis_sn


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* ops
    * Generic
        * Added platform ops revision
    * IOSXE
        * Added management ops
        * Added platform ops revision
        * Cat9k
            * Added platform ops revision
            * C9500-32QC
                * Added tests
    * NXOS
        * Added management ops
        * Added platform ops revision
        * n5k
            * Added platform ops revision
    * IOSXR
        * Added platform ops revision
    * IOS
        * Added management ops for IOS



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_interface_ip_subscriber
        * API to configure_interface_ip_subscriber
    * Added unconfigure_interface_ip_subscriber
        * API to unconfigure_interface_ip_subscriber
    * Added configure_ip_cef
        * API to configure_ip_cef
    * Added unconfigure_ip_cef
        * API to unconfigure_ip_cef
    * Added configure_ip_dhcp_client
        * API to configure_ip_dhcp_client
    * Added unconfigure_ip_dhcp_client
        * API to unconfigure_ip_dhcp_client
    * Added configure_ip_dhcp_server
        * API to configure_ip_dhcp_server
    * Added unconfigure_ip_dhcp_server
        * API to unconfigure_ip_dhcp_server
    * Added configure_tftp_server
        * API to configure_tftp_server
    * Added unconfigure_tftp_server
        * API to unconfigure_tftp_server
    * Added configure_interface_ipv6_rip
        * API to configure_interface_ipv6_rip
    * Added unconfigure_interface_ipv6_rip
        * API to configure_interface_ipv6_rip
    * Added configure_interface_ipv6_dhcp_server_allow_hint
        * API to configure_interface_ipv6_dhcp_server_allow_hint
    * Added unconfigure_interface_ipv6_dhcp_server_allow_hint
        * API to unconfigure_interface_ipv6_dhcp_server_allow_hint
    * Added configure_ipv6_dhcp_server
        * API to configure_ipv6_dhcp_server
    * Added unconfigure_ipv6_dhcp_server
        * API to configure_ipv6_dhcp_server
    * Added configure_ipv6_dhcp_relay_option
        * API to configure_ipv6_dhcp_relay_option
    * Added unconfigure_ipv6_dhcp_relay_option
        * API to unconfigure_ipv6_dhcp_relay_option
    * Added new API to configure ip dhcp ping packets
        * ip dhcp ping packets {packets_no}
    * Added new API to unconfigure ip dhcp ping packets
        * no ip dhcp ping packets {packets_no}
    * Added new API to configure ip dhcp remember
        * ip dhcp remember
    * Added new API to unconfigure ip dhcp remember
        * no ip dhcp remember
    * Added new API to configure ipv6 nd managed-config-flag on the interface
        * ipv6 nd managed-config-flag
    * Added new API to unconfigure ipv6 nd managed-config-flag on the interface
        * no ipv6 nd managed-config-flag
    * Added new API to configure ipv6 dhcp-relay bulk-lease
        * ipv6 dhcp-relay bulk-lease {option} {value}
        * ipv6 dhcp-relay bulk-lease {option}
    * Added new API to unconfigure ipv6 dhcp-relay bulk-lease
        * no ipv6 dhcp-relay bulk-lease {option} {value}
        * no ipv6 dhcp-relay bulk-lease {option}
    * Added new API to configure ipv6 dhcp relay destination global
        * API to configure ipv6 dhcp relay destination global
    * Added new API to unconfigure ipv6 dhcp relay destination global
        * API to unconfigure ipv6 dhcp relay destination global
    * Added new API to configure ipv6 dhcp pool functions
        * API to configure ipv6 dhcp pool functions
    * Added new API to unconfigure ipv6 dhcp pool
        * API to unconfigure ipv6 dhcp pool
    * Added unconfigure_ipv6_dhcp_pool_prefix_delegation_pool
        * added api to unconfigure_ipv6_dhcp_pool_prefix_delegation_pool under ipv6/configure.py
    * Added unconfigure_ipv6_local_pool
        * added api to unconfigure_ipv6_local_pool under ipv6/configure.py
    * Added unconfigure_ipv6_dhcp_client_pd_on_interface
        * added api to unconfigure_ipv6_dhcp_client_pd_on_interface under interface/configure.py
    * Added API configure_bfd_ospf_timers
        * added api to configure bfd timers for ospf
    * Added API rp_bfd_all_interfaces
        * API to enable BFD on all interfaces on the device
    * Added configure_route_map_with_description
        * API to configure route-map with description
    * Added route_map_unconfigure_description
        * API to unconfigure route-map with description
    * Added unconfigure_route_map
        * API to unconfigure route-map
    * Added configure_rep
        * New API to configure rep segment
    * Added configure_fastrep
        * New API to configure fastrep segment
    * Added unconfigure_rep
        * New API to unconfigure rep segment
    * Added unconfigure_fastrep
        * New API to unconfigure fastrep segment
    * Added new API to configure ipv6 dhcp binding track ppp
        * ipv6 dhcp binding track ppp
    * Added new API to unconfigure ipv6 dhcp binding track ppp
        * no ipv6 dhcp binding track ppp
    * Added new API to configure ipv6 dhcp route-add
        * ipv6 dhcp {route_add}
    * Added new API to unconfigure ipv6 dhcp route-add
        * no ipv6 dhcp {route_add}
    * Added new API to configure ipv6 dhcp server join all-dhcp-server
        * ipv6 dhcp server join all-dhcp-server
    * Added new API to unconfigure ipv6 dhcp server join all-dhcp-server
        * no ipv6 dhcp server join all-dhcp-server
    * Added new API to configure ip dhcp binding cleanup interval
        * ip dhcp binding cleanup interval {interval_time}
    * Added new API to unconfigure ip dhcp binding cleanup interval
        * no ip dhcp binding cleanup interval {interval_time}
    * Added configure_ipv6_dhcp_relay_source
        * API to configure ipv6 dhcp-relay trust source-interface {interface}
    * Added unconfigure_ipv6_dhcp_relay_source
        * API to unconfigure ipv6 dhcp-relay trust source-interface {interface}
    * Added configure_source_destination_remote_vlan
        * API for configure source destination remote vlan
    * Added unconfigure_source_destination_remote_vlan
        * API for unconfigure source destination remote vlan
    * Added configure_data_mdt
        * API to configure data mdt
    * Added new API to verify ip address on interface
        * API to verify ip address on interface
    * Added configure_interface_ipv6_dhcp_client_request_vendor
        * API to configure_interface_ipv6_dhcp_client_request_vendor
    * Added unconfigure_interface_ipv6_dhcp_client_request_vendor
        * API to unconfigure_interface_ipv6_dhcp_client_request_vendor
    * Added configure_interface_ipv6_dhcp_client_information
        * API to configure_interface_ipv6_dhcp_client_information
    * Added unconfigure_interface_ipv6_dhcp_client_information
        * API to unconfigure_interface_ipv6_dhcp_client_information
    * Added configure_ipv6_dhcp_test_relay
        * API to configure_ipv6_dhcp_test_relay
    * Added unconfigure_ipv6_dhcp_test_relay
        * API to unconfigure_ipv6_dhcp_test_relay
    * Added configure_ipv6_dhcp_test_server
        * API to configure_ipv6_dhcp_test_server
    * Added unconfigure_ipv6_dhcp_test_server
        * API to unconfigure_ipv6_dhcp_test_server
    * Added unconfigure_ipv6_dhcp_client_pd_on_interface
        * API to unconfigure_ipv6_dhcp_client_pd_on_interface
    * Added unconfigure_ip_unnumbered_on_interface
        * API to unconfigure_ip_unnumbered_on_interface
    * Added enable_ospf_bfd_all_interfaces
        * API to configure enable_ospf_bfd_all_interfaces
    * Added def configure_device_sensor_dhcpv6_snooping
    * Added def unconfigure_device_sensor_dhcpv6_snooping
    * SPAN
        * Added configure_remote_span_on_vlan
            * API to configure remote span on vlan
    * Added API set_isis_timers
        * API to configure isis timers on the device
    * Added configure_device_tracking_policy_reachable
        * API to configure device tracking options
    * Added configure_device_tracking_binding_globally
        * API to configure device-tracking binding vlan globally
    * Added unconfigure_device_tracking_binding_globally
        * API to unconfigure device-tracking binding vlan globally
    * Added configure_ip_dhcp_database
        * API to configure_ip_dhcp_database
    * Added unconfigure_ip_dhcp_database
        * API to unconfigure_ip_dhcp_database
    * Added configure_logging_host
    * Added unconfigure_logging_host
    * Added configure_logging_source_interface
    * Added unconfigure_logging_source_interface
    * Added API enable_eigrp_bfd_all_interfaces
        * configure api for Enabling bfd on all interfaces for eigrp instance
    * Added API configure_ospf_interface_cost
        * API to configure ospf interface cost on the device
    * Added API configure_radius_server_dtls_trustpoint
    * API to Configure radius server dtls trustpoint
    * Added configure_ipv6_pim_rp_vrf
        * configure api for ipv6 pim rp vrf
    * Added ip pim send-rp-announce Loopback0 scope 10
    * Added configure_interface_ip_ddns_update
        * API to configure_interface_ip_ddns_update
    * Added unconfigure_interface_ip_ddns_update
        * API to unconfigure_interface_ip_ddns_update
    * Added configure_interface_ip_dhcp_client
        * API to configure_interface_ip_dhcp_client
    * Added unconfigure_interface_ip_dhcp_client
        * API to unconfigure_interface_ip_dhcp_client
    * Added API set_platform_software_selinux
        * Added API to set_platform_software_selinux
    * Added new API to configure access-session tls-version
        * access-session tls-version {tls-version}
    * Added new API to unconfigure access-session tls-version
        * no access-session tls-version
    * Updated configure_eap_profile
        * updated api to configure_eap_profile for ciphersuite
    * Added configure_tracking_object
    * Added unconfigure_tracking_object
    * Added configure_preemption_easycli
        * New API to configure preemption easycli
    * Added unconfigure_preemption_easycli
        * New API to unconfigure preemption easycli
    * sdk-pkg
        * clear_raw_socket_transport_statistics_all
    * Added new API to configure ip dhcp relay on the interface
        * API to configure ip dhcp relay on the interface
    * Added new API to unconfigure ip dhcp relay on the interface
        * API to unconfigure ip dhcp relay on the interface
    * Added new API to configure ipv6 dhcp ping packets
        * API to configure ipv6 dhcp ping packets
    * Added new API to configure ip dhcp drop inform
        * API to configure ip dhcp drop inform
    * Added new API to unconfigure ip dhcp drop inform
        * API to unconfigure ip dhcp drop inform
    * Added
        * configure_scada_dnp3_serial_channel
        * configure_scada_dnp3_serial_session
        * configure_scada_dnp3_ip_channel
        * configure_scada_dnp3_ip_session
        * configure_scada_enable
        * unconfigure_scada_enable
        * unconfigure_scada_dnp3_ip_session
        * unconfigure_scada_dnp3_ip_channel
        * unconfigure_scada_dnp3_serial_session
        * unconfigure_scada_dnp3_serial_channel
        * configure_scada_t101_serial_channel
        * configure_scada_t101_serial_session
        * configure_scada_t101_serial_sector
        * configure_scada_t104_ip_channel
        * configure_scada_t104_ip_session
        * configure_scada_t104_ip_sector
        * unconfigure_scada_t104_ip_sector
        * unconfigure_scada_t104_ip_session
        * unconfigure_scada_t104_ip_channel
        * unconfigure_scada_t101_serial_sector
        * unconfigure_scada_t101_serial_session
        * unconfigure_scada_t101_serial_channel
    * Added unconfig_svi_vlan_range
        * API to unconfig_svi_vlan_range

* sdk
    * ios
        * Added new API to clear_idle_vty_sessions
    * iosxe
        * Added new API to clear_idle_vty_sessions
        * Added execute_issu_set_rollback_timer API
        * Added API for execute_issu_set_rollback_timer
        * Updated regex for is_management_interface
    * utils
        * Added abstract argument to parser call
        * Added time_to_int
        * Added PID_BREAKOUT_MAP
    * IOSXR
        * Added breakout_interface_names API

* sdk-pkg
    * ixos
        * Added api to get bandwidth


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified
        * Updated configure_interface_monitor_session API with additional optional argument to specify the monitor session direction.
    * Updated api configure_ip_on_tunnel_interface
        * updated api with ip_mode to support both ip and ipv4
    * Modified configure dhcp pool API to support all the dhcp pool parameters
        * API to configure dhcp pool
    * Added configure_ipv6_dhcp_relay_destination_ipv6address
        * API to configure_ipv6_dhcp_relay_destination_ipv6address
    * Added uncconfigure_ipv6_dhcp_relay_destination_ipv6address
        * API to unconfigure_ipv6_dhcp_relay_destination_ipv6address
    * cat9k
        * c9500
            * Updated API's to configure and unconfigure the ignore startup config
        * c9500
            * C9500-48Y4C
                * Added API's to configure and unconfigure the ignore startup config
    * Updated configure_interface_switchport_access_vlan
        * updated api to configure_interface_switchport_access_vlan
    * Updated configure_dialer_interface
        * updated api to configure_dialer_interface
    * Updated configure_ppp_multilink
        * updated api to configure_ppp_multilink
    * Updated clear_platform_software_fed_switch_active_access_security_table_counters
        * updated api to clear_platform_software_fed_switch_active_access_security_table_counters
    * Updated clear_platform_software_fed_switch_active_access_security_auth_acl_counters
        * updated api to clear_platform_software_fed_switch_active_access_security_auth_acl_counters
    * Modified configure_subinterface to include vrf
    * Modified config_interface_carrier_delay made delay_type an optional argument
    * Modified
        * Updated configure_replace API to raise SubCommandFailure exception if error pattern matched

* sdk
    * Generic
        * Added `disconnect_termserver` argument to `execute_clear_line`

* sdk-pkg
    * iosxe
        * updated the clear_idle_vty_sessions api
    * utils
        * updated the time_to_int function

* tooling
    * Modified Makefile
        * Updated makefile to include make jsons for each feature

* abstracted_libs
    * processors
        * Enhanced message for initialize_traffic



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIpMfibVrf parser
        * Added schema and parser for cli
            * 'show platform software fed switch active ip mfib vrf {vrf_name} {group} {source}'
            * 'show platform software fed switch active ip mfib {group} {source}'
            * 'show platform software fed active ip mfib vrf {vrf_name} {group} {source}'
            * 'show platform software fed active ip mfib {group} {source}'
    * Added ShowPlatformSoftwareFedPuntAsicCauseBrief
        * show platform software fed switch {mode} punt asic-cause brief
    * Added ShowAutoInstTrace parser
        * Added schema and parser for cli 'show auto inst trace'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAn37Status parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_an37_status({system_port_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortAnltStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_anlt_status({system_port_gid}).
    * Added
        * show raw-socket tcp sessions local
    * Added  ShowPlatformSoftwareRouteMap parser
        * Added schema and parser for cli "show platform software route-map R0 map"
    * Added ShowPlatformHardwareAuthenticationStatus
        * Added parser "show platform hardware authentication status" under c9610
    * Added support for parsing the 'show access method dot1x details'
    * Added ShowHardwareLed schema and parser
        * Added schema and parser for show hardware led
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_status({system_port_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightPortSerdesStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_serdes_status({system_port_gid}).
    * Added ShowRunningConfigAAARadiusServer
        * Added schema and parser for 'Show Running Config AAA Radius Server'
    * Added support for parsing the 'show cts policy sgt {sgt}'
    * Added parser ShowPlatformSoftwareFedSwitchActivePortIfId
        * Added parser for 'show platform software fed {switch} {mode} port if_id {if_id}'
    * Added ShowInterfacesCountersPort parser
        * Added schema and parser for cli 'show interfaces counters port'
    * Added ShowIPDhcpImport Parser in show_ip.py
        * show ip dhcp import
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatus and ShowPlatformHardwareFedSwitch1FwdAsicInsightIfmLagMembers parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status().
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_members({lag_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2mRoutes parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2m_routes({switch_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL2mGroups parser.
        * Added parser for cli sshow platform hardware fed switch {switch_id} fwd-asic insight l2m_groups({l2_mcg_gid}).
    * Added ShowIpv6GeneralPrefix Parser in show_ipv6.py
        * show ipv6 general-prefix
    * Added schema and parser for 'show spanning-tree mst interface {interface}'
    * Added schema and parser for 'show switch stack-ports summary'
    * Added ShowAuthenticationSessionMethodDetails parser.
        * 'show authentication sessions method {method} details'
        * 'show authentication sessions method {method} interface GigabitEthernet2/0/3 details'
        * 'show authentication sessions method {method} policy'
    * Added support for parsing the 'show platform software fed {switch} {active} ip mfib vrf {vrf_name} {group} {source}',
    * Added ShowPlatformSoftwareFedActiveIfmInterfaceNameTunnel5 parser
        * Added schema and parser for cli 'show platform software fed active ifm interface_name tunnel5'
    * Added ShowPlatformSoftwareFedSwitchActiveIpMulticastInterface parser
        * Added parser for cli show platform software fed switch {module} ip multicast interface {if_id}
        * Added parser for cli show platform software fed switch {module} ipv6 multicast interface {if_id}
    * Added ShowPlatformSoftwareFedSwitchActiveOifsetL3mHash parser
        * Added parser for cli show platform software fed switch active oifset l3m hash {hash} detail
    * Added  ShowPlatformSoftwareFedSwitchFnfMonitorRulesAsic0 parser
        * Added schema and parser for cli "show platform software fed switch {switch_num} fnf monitor rules asic 0"
    * Added support for parsing the following commands
        * 'show authentication sessions interface GigabitEthernet2/0/3'
        * 'show authentication sessions interface GigabitEthernet2/0/3 switch standby R0'
        * 'show authentication sessions interface GigabitEthernet2/0/3 switch active R0'
        * 'show authentication sessions database interface GigabitEthernet2/0/3 switch active R0'
        * 'show authentication sessions database interface GigabitEthernet2/0/3 switch standby R0'
        * 'show authentication sessions database interface GigabitEthernet2/0/3 switch 1 R0'
    * Added ShowMonitorCaptureFileDetailed
        * Added schema and parser for'show monitor capture file flashfile1.pcap packet-number 7 detailed'
    * Added ShowIPDhcpConflict Parser in show_ip.py
        * show ip dhcp conflict
    * Added ShowIpPolicy Parser in show_ip.py
        * show ip policy
    * Added schema and parser for cli
        * 'show mac address-table dynamic',
        * 'show mac address-table dynamic interface {intf_name}'
    * Added ShowIpv6OspfDatabase
        * Added schema and parser for 'ShowIpv6OspfDatabase'
    * Added ShowIpDhcpSnoopingStatisticsDetail parser
        * Added schema and parser for cli 'show ip dhcp snooping statistics detail'

* nxos
    * added new parser ShowIpDhcpSnoopingBindingDynamicEvpn
        * Added new parser for the cli "show ip dhcp snooping binding dynamic evpn"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> dynamic evpn"
        * Added new parser for the cli "show ip dhcp snooping binding vlan <vlan> dynamic evpn"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> vlan <vlan> dynamic evpn"
    * added new parser ShowIpDhcpSnoopingBindingStaticEvpn
        * added new parser for the cli "show ip dhcp snooping binding static evpn"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} static evpn"
        * added new parser for the cli "show ip dhcp snooping binding vlan {vlan} static evpn"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} vlan {vlan} static evpn"
    * added new parser ShowIpDhcpSnoopingBindingDynamic
        * Added new parser for the cli "show ip dhcp snooping binding dynamic"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> dynamic"
        * Added new parser for the cli "show ip dhcp snooping binding vlan <vlan> dynamic"
        * Added new parser for the cli "show ip dhcp snooping binding interface <intf> vlan <vlan> dynamic"
    * added new parser ShowIpDhcpSnoopingBindingStatic
        * added new parser for the cli "show ip dhcp snooping binding static"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} static"
        * added new parser for the cli "show ip dhcp snooping binding vlan {vlan} static"
        * added new parser for the cli "show ip dhcp snooping binding interface {intf} vlan {vlan} static"
    * added new parser ShowL2routeFhs
        * added new parser for the cli "show l2route fhs all"
        * added new parser for the cli "show l2route fhs topology {vlan}"
    * added new parser ShowForwardingRouteIpsgVrf
        * added new parser for the cli 'show forwarding route ipsg vrf all'
        * added new parser for the cli 'show forwarding route ipsg vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg module {ipsg_module} vrf all'
        * added new parser for the cli 'show forwarding route ipsg module {ipsg_module} vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} module {ipsg_module} vrf all'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} module {ipsg_module} vrf {vrf}'
        * added new parser for the cli 'show forwarding route ipsg max-display-count {max_count} vrf all'
    * added new parser ShowIpDhcpSnoopingStatistics
        * added new parser for the cli 'show ip dhcp snooping statistics'
        * added new parser for the cli 'show ip dhcp snooping statistics vlan {vlan}'
    * added new parser ShowIpDhcpRelayStatisticsInterfaceVlan
        * added new parser for the cli 'show ip dhcp relay statistics interface vlan {vlan}'
    * added new parser ShowIpv6DhcpRelayStatisticsInterfaceVlan
        * added new parser for the cli 'show ipv6 dhcp relay statistics interface vlan {vlan}'
    * Added ShowIpv6RouteSummary
        * show ipv6 route summary
        * show ipv6 route summary vrf {vrf}

* iosxr
    * Added parser for show inventory sparse


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowInterface
        * Added line
    * Modified ShowMonitorCaptureBufferDetailed
        * Modified schema and parser for'show monitor capture file {path} packet-number {number} detailed'
    * Modified ShowPlatformHardwareFpgaSwitch
        * Modified parser to handle spaces flexibly in the output
        * Added regular expression p0 which skips the table tile line
    * Modified ShowIpDhcpBinding
        * Added "show ip dhcp binding vrf {vrf_name} {ip_address}" cli
        * Added "show ip dhcp binding {ip_address}" cli
    * Fixed parser ShowLine
        * Fixed regex pattern for show line for int field to be optional"
    * Fix ShowPlatformSoftwareFedActiveMonitor parser
        * Removed duplicate parser for show platform software fed active monitor and modified the existing parser regex p2 to handle the output of the command.
    * cat9k
        * c9610
            * Fixed parser ShowHardwareLed
                * Modified the parser regex p6 to handle the output of the command.
                * Added optional "beacon" keyword to the parser schema.
    * Fixed the regex p1 for new output.
    * rv1
        * Added few keys for the ShowPlatform parser schema.
        * Added 'IE-35' as part of the condition for lc_type 'rp'.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShSoftwareFed
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveCpuInterfaces
        * Modified switch as optional in the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmMappingsL3if_le
        * Modified switch as optional in the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmMappingsGpn
        * Modified switch as optional in the parser.
    * Modified ShowPlatformSoftwareFedSwitchActiveSgaclPort parser
        * Added optional parameters "ingress" and "egress" , modified "interface_state" to be OPtional
        * Added new regex pattern p2 to accomodate output for sgacl port details for all catalyst platfroms 9200,0300,9400 etc
    * Modified ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableSummary
        * added support parser should work on active and standby
    * Modified ShowPlatformSoftwareFedActiveAclBindDbDetail
        * added support cg_name filed to accepct ! and
    * Modified ShowPlatformSoftwareFedSwitchActiveAclBindDbIfid
        * added support parser should work on active and standby
    * Modified ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage
        * added support parser should work on active and standby
    * Modified ShowPowerInline schema and parser to support on IE3K platforms
        * Modified schema and parser for 'show power inline interface' command
    * Modify parser ShowRunInterface
        * Modified URPF Features.
    * cat9k
        * c9400
            * Fixed parser show boot to make the standby details optional.
    * cat9k
        * c9350
            * Modified ShowPlatformHardwareFedSwitchQosQueueConfig
                * modified switch_var to swich_num to match parser under iosxe.
    * Modified parser ShowHardwareLed
        * Enhanced the parser to get LED auto-off status, Added schema and regex pattern <p12_1>
        * Enhanced the parser to get LED Hardware State, Added schema and regex pattern <p12_2>
    * Fix ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id
        * Added fed active and fed switch commands to the parser.
    * Modify parser ShowCefInterfaceInternal
        * Added IP unicast RPF check is enabled.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveStatisticsInit
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchNumberIfmMappingsPortLE
        * Added fed active and fed switch commands to the parser.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIfmInterfacesDetail
        * Modified switch as optional in the parser.
    * Modified ShowRepTopologyDetail
        * Modified  regex to support new device output.
    * Modified ShowDiagnosticContentModule
        * Added parser supprot for 'show diagnostic content module' command
        * Added regular expression p0 which extracts the module number
    * Fixed parser ShowWirelessClientMacDetail
        * Modified current_rate and max_client_protocol_capability to be optional
        * Allowed space within Device Type (e.g. 'Un-Classified Device')
    * Fixed parser ShowPlatformSoftwareAccessListSwitchActiveF0Summary
        * Added parser support for 'show platform software access-list f0 summary' command

* nxos
    * Fixed parser ShowNveEthernetSegment
        * Fixed the case where df_vni_list will be populated.
    * Modified ShowVdcMembershipStatus
        * Updated regex <p4> to allow for a space between interface name and status.
    * Modified ShowIpRoute
        * Updated regex pattern <p3> to handle the following cases

* generic
    * Modified ShowVersion
        * Added os_flavor field to the parser output

* iosxr
    * Fixed parser ShowInterfacesDetail
        * Fixed regex pattern p9_3 to match "flow control"



genie.telemetry
"""""""""""""""
