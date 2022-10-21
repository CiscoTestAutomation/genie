October 2022
==========

October 25 - Genie v22.10
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.10                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.10                         |
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

genie.libs.clean
""""""""""""""""

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
    * Added configure_ip_dhcp_snooping_information_option API
        * Api to configure dhcp snooping information option
    * Added unconfigure_ip_dhcp_snooping_information_option API
        * Api to unconfigure dhcp snooping information option
    * Added configure_ip_dhcp_pool API
        * Api to configure dhcp pool
    * Added unconfigure_ip_dhcp_pool API
        * Api to unconfigure dhcp pool
    * Added configure_dhcp_channel_group_mode API
        * Api to configure Ethernet port to an EtherChannel group
    * Added unconfigure_dhcp_channel_group_mode API
        * Api to unconfigure Ethernet port from an EtherChannel group
    * Added configure_cts_manual API
        * Api to configure cts manual on the interface
    * Added verify_number_of_interfaces API
        * API to check number of interfaces in teh device
    * Added configure_interface_network_policy
        * API for configure interface network policy
    * Added unconfigure_interface_network_policy
        * API for unconfigure interface network policy
    * Added configure_nat64_nd_ra_prefix API
        * API for configure nat64 nd ra prefix
    * Added unconfigure_nat64_nd_ra_prefix API
        * API for unconfigure nat64 nd ra prefix
    * Added configure_interface_span_vlan_priority
        * API for configure interface spanning-tree vlan priority
    * Added unconfigure_interface_span_vlan_priority
        * API for unconfigure interface spanning-tree vlan priority
    * Added configure_interface_span_cost
        * API for configure interface spanning-tree cost
    * Added unconfigure_interface_span_cost
        * API for unconfigure interface spanning-tree cost
    * Added configure_monitor_capture and start_monitor_capture API
        * API for configuring monitor capture and start the monitor capture cli
    * Added configure_mac_acl api
        * API for configuring mac acl
    * Added configure_switch_provision api
        * Api to configure switch provision
    * Added unconfigure_switch_provision api
        * Api to unconfigure switch provision
    * Added configure_cdp_timer
        * API for configure cdp timer
    * Added unconfigure_cdp_timer
        * API for unconfigure cdp timer
    * Added configure_cdp_holdtime
        * API for configure cdp holdtime
    * Added unconfigure_cdp_holdtime
        * API for unconfigure cdp holdtime
    * Added configure_lldp_holdtime
        * API for configure lldp holdtime
    * Added unconfigure_lldp_holdtime
        * API for unconfigure lldp holdtime
    * Added configure_lldp_timer
        * API for configure lldp timer
    * Added unconfigure_lldp_timer
        * API for unconfigure lldp timer
    * Added configure_lldp_reinit
        * API for configure lldp reinit
    * Added unconfigure_lldp_reinit
        * API for unconfigure lldp reinit
    * Added clear_lldp_counters
        * API to clear lldp counters
    * Added clear_lldp_table
        * API to clear lldp table
    * Added configure_lldp_tlv_select
        * API for configure lldp tlv select
    * Added unconfigure_lldp_tlv_select
        * API for unconfigure lldp tlv select
    * Added configure_ipv6_mld_snooping
        * API to configure ipv6 mld snooping
    * Added unconfigure_ipv6_mld_snooping
        * API to unconfigure ipv6 mld snooping
    * Added configure_ipv6_mld_vlan_immediate_leave(number)
        * API to configure ipv6 mld snooping immediate-leave
    * Added unconfigure_ipv6_mld_vlan_immediate_leave(number)
        * API to unconfigure ipv6 mld snooping immediate-leave
    * Added unconfigure_ipv6_mld_vlan(number)
        * API to configure ipv6 mld snooping on a specific vlan
    * Added ununconfigure_ipv6_mld_vlan(number)
        * API to unconfigure ipv6 mld snooping on a specific vlan
    * Added unconfigure_ipv6_pim_rp_address(number)
        * API to configure ipv6 pim rp-address
    * Added ununconfigure_ipv6_pim_rp_address(number)
        * API to unconfigure ipv6 pim rp-address
    * Added configure_ipv6_mld_join_group(address, interface_id)
        * Api to configure ipv6 mld join group
    * Added unconfigure_ipv6_mld_join_group(address, interface_id)
        * Api to unconfigure ipv6 mld join group
    * Added configure_ipv6_mld_snooping_vlan_static_interface(device, vlan_id, address, interface_id)
        * Api to configure ipv6 mld snooping vlan static interface
    * Added unconfigure_ipv6_mld_snooping_vlan_static_interface(device, vlan_id, address, interface_id)
        * Api to unconfigure ipv6 mld snooping vlan static interface
    * Added configure_cts_enforcement_logging
        * API for configure cts enforcement logging
    * Added unconfigure_cts_enforcement_logging
        * API for unconfigure cts enforcement logging
    * Added clear_cts_counters_ipv6
        * API for clearing cts counters ipv6
    * Added configure_ip_dhcp_client_vendor_class
        * API for "Configure IP DHCP Client Vendor-class on interface"
    * Added unconfigure_ip_dhcp_client_vendor_class
        * API for "Unconfigure IP DHCP Client Vendor-class on interface"
    * Added configure_ipv6_dhcp_client_vendor_class
        * API for "Configure IPV6 DHCP Client Vendor-class on interface"
    * Added unconfigure_ipv6_dhcp_client_vendor_class
        * API for "Unconfigure IPV6 DHCP Client Vendor-class on interface"
    * Added configure_system_ignore_startupconfig_switch_all API
        * Api to configure the system ignore startup configuration on the switch
    * Added unconfigure_system_ignore_startupconfig_switch_all API
        * Api to unconfigure the system ignore startup configuration on the switch
    * Added configure_system_disable_password_recovery_switch_all API
        * Api to disable password recovery on the switch
    * Added unconfigure_system_disable_password_recovery_switch_all API
        * Api to enable password recovery on the switch
    * Added verify_portfast_state
        * API to check port fast enabled on the interface or not
    * Added get_device_classifier_profile_names
        * API to get device classifier profile names
    * Added configure_snmp_server_contact api
        * API for configuring snmp-server contact
    * Added unconfigure_snmp_server_contact api
        * API for unconfiguring snmp-server contact
    * Added show_switch_redirect api
        * API for storing output in a file
    * Added clear_logging_onboard_switch api
        * Api to clear logging onboard switch
    * Added configure_boot_system_switch_all_flash api
        * Api to configure boot variable
    * Added unconfigure_boot_system api
        * Api to unconfigure boot variable
    * Added configure_ip_access_group_in_out
        * API to add the ip access-group in an interface using the command
    * Added unconfigure_ip_access_group_in_out
        * API to remove the ip access-group in an interface using the command
    * Added configure_icmp_ip_reachables api
        * Api to configure sending of ICMP unreachable messages
    * Added unconfigure_icmp_ip_reachables api
        * Api to unconfigure sending of ICMP unreachable messages
    * Added configure_isis_keychain_key API
        * API for configuring authentication string for a key
    * Added unconfigure_isis_keychain_key API
        * API for unconfiguring the isis key chain
    * Added configure_isis_authentication_mode API
        * API for configuring the ISIS authentication mode
    * Added unconfigure_isis_authentication_mode API
        * API for unconfiguring the ISIS authentication mode
    * Added configure_isis_authentication_key_chain API
        * API for configuring the ISIS authentication Key-chain
    * Added unconfigure_isis_authentication_key_chain API
        * API for unconfiguring the ISIS authentication Key-chain
    * Added configure_isis_circuit_type API
        * API for configuring the ISIS ciruit type
    * Added unconfigure_isis_circuit_type API
        * API for unconfiguring the ISIS ciruit type
    * Added configure_isis_password API
        * API for configuring the ISIS password
    * Added unconfigure_isis_password API
        * API for unconfiguring the ISIS password
    * Added configure_enable_http_server API
        * Added new API for enabling http server
    * Added configure_set_clock_calendar API
        * Added new API for setting clock calender
    * Added configure_clock_timezone API
        * Added new API for configuring clock timezone
    * Added configure_router_bgp_maximum_paths api
        * Api to configure the maximum paths on router bgp
    * Added unconfigure_router_bgp_maximum_paths api
        * Api to unconfigure the maximum paths on router bgp
    * Added configure_router_bgp_synchronization api
        * Api to configure the synchronization on router bgp
    * Added unconfigure_router_bgp_synchronization api
        * Api to unconfigure the synchronization on router bgp
    * Added unconfigure_bgp_log_neighbor_changes api
        * Api to unconfigure the log neighbor changes on router bgp
    * Added configure_bgp_auto_summary api
        * Api to configure the auto-summary on router bgp
    * Added unconfigure_bgp_auto_summary api
        * Api to unconfigure the auto-summary on router bgp
    * Added unconfigure_interface_switchport_mode_access
        * API for unconfigure switchport mode access
    * Added configure_interface_macro_auto_port_sticky
        * API for configure interface macro auto port sticky
    * Added unconfigure_interface_macro_auto_port_sticky
        * API for unconfigure interface macro auto port sticky
    * Added configure_interface_template_sticky
        * API for configure interface template sticky
    * Added unconfigure_interface_template_sticky
        * API for unconfigure interface template sticky
    * Added configure_interface_inherit_disable
        * API for configure interface inherit disable
    * Added unconfigure_interface_inherit_disable
        * API for unconfigure interface inherit disable
    * Added unconfigure_control_policies
        * API for unconfigure control policies
    * Added configure_macro_auto_sticky
        * API for configure macro auto sticky
    * Added unconfigure_macro_auto_sticky
        * API for unconfigure macro auto sticky
    * Added configure_device_classifier
        * API for configure device classifier
    * Added unconfigure_device_classifier
        * API for unconfigure device classifier
    * Added configure_snmp_server_location api
        * Api to configure snmp-server location
    * Added unconfigure_snmp_server_location api
        * Api to unconfigure snmp-server location
    * Added configure_hw_switch_logging_onboard api
        * Api to configure OBFL on a switch
    * Added unconfigure_hw_switch_logging_onboard api
        * Api to unconfigure OBFL on a switch
    * Added configure_network_policy_profile_voice_vlan
        * API for configure network policy profile voice vlan
    * Added unconfigure_network_policy_profile_voice_vlan
        * API for unconfigure network policy profile voice vlan

* sdk/powercycler
    * Added SNMPv3 support for Raritan PDU

* added configure_ip_tftp_blocksize api
    * Api to specify tftp blocksize

* added unconfigure_ip_tftp_blocksize api
    * Api to reset tftp blocksize


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified config_ip_on_interface
        * When there are warnings in the output, it returns a `list` of them line by line instead of `None`
    * Modified configure_hsrp_interface API
        * Modified API for configure hsrp interface to support priority and preempt configuration in HSRP
    * Modified configure_mdns_sd_service_peer, unconfigure_controller_service_policy_service_export and unconfigure_controller_policy_service_export API
        * Modified configure_mdns_sd_service_peer API to change the cli from active-response-timer to active-response timer, the cli is hardcoded incorrectly so it is not backwards compatible.
        * Modified unconfigure_controller_service_policy_service_export and unconfigure_controller_policy_service_export api by removing policy_name from the cli which was there incorrectly.
    * Modified verify_platform_details API
        * API to check platform details in the device

* blitz
    * Fix timeout when yang subscribe action type is on_change
    * Fix for format of rpc building for leaf level nodes(Single/Multiple leaf nodes) as per gnmi specification section 2.3.1
    * Unit tests were not following the gnmi_specification format. Fixed unit_tests for gnmi rpc build.
    * Modify gnmi operations to pass credentials for clear-channel mode.
    * Stream Subscribe for Invalid Path infinitely logs "Waiting for notification..."
    * Prune list nodes if already in other nodes xpath logic breaks for leafs with common names.
    * Current logic of this function breaks for the testcase where multiple leafs are having common name.
    * Eg 1. Sys/Cont/vni, 2. Sys/Cont/vni-state
    * Since Leaf 1 is a substring of Leaf 2, _trim_nodes function removes the Leaf_1 node.
    * Netconf Sequence Validation Fix for Multiple Lists
    * Added GNMI Sequence Validation
    * yangexec.py
        * Fix to handle GNMI AUTO VALIDATION of edit-config operation.
        * Response will show GNMI get operation of edit-config values if AUTO VALIDATE is set to True.

* sdk
    * Modified genie.libs.sdk.genie_yamls datafile function to support `health` argument


--------------------------------------------------------------------------------
                                   Changelog:                                   
--------------------------------------------------------------------------------



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* hvrp
    * Added DisplayBgpPeer
        * display bgp {address_family} vpn-instance {vrf} peer
        * display bgp {address_family} all peer
        * display bgp {address_family} peer
        * display bgp peer
    * Added DisplayBgpPeerSummary
        * display bgp all summary
    * Added DisplayBgpPeerVerbose
        * display bgp {address_family} peer {peer_address} verbose
        * display bgp {address_family} peer verbose
        * display bgp {address_family} all peer {peer_address} verbose
        * display bgp {address_family} all peer verbose
        * display bgp {address_family} vpn-instance {vrf} peer {peer_address} verbose
        * display bgp {address_family} vpn-instance {vrf} peer verbose
        * display bgp peer {peer_address} verbose
        * display bgp peer verbose

* iosxe
    * Added ShowTelemetryIETFSubscriptionAllReceivers
        * show telemetry ietf subscription all receivers
    * Added ShowCallHomeVersion
        * show call-home version
    * Added ShowCallHomeSmartLicensing
        * show call-home smart-licensing
    * Added ShowCallHomeMailServerStatus
        * show call-home mail-server status
    * Added ShowCallHomeProfileAll
        * show call-home profile all
    * Added ShowPlatformHardwareRegisterReadAsic
        * show platform hardware fed active fwd-asic register read register-name xyz asic n core m
        * show platform hardware fed switch x fwd-asic register read register-name xyz asic n core m
    * Added ShowInterfaces
        * Added is_deleted key to schema to identify deleted interfaces.
    * Added ShowPlatformSoftwareMemorySwitchAllocCallsite
        * 'show platform software memory fed switch {switch_num} alloc callsite brief'
        * 'show platform software memory fed {switch_type} alloc callsite brief'
    * Added ShowPlatformSoftwareMemorySwitchAllocBacktrace
        * 'show platform software memory fed switch {switch_num} alloc backtrace'
        * 'show platform software memory fed {switch_type} alloc backtrace'
    * Added ShowPlatformHardwareFedSwitchQosDscpcosCounters
        * 'show platform hardware fed switch {switch_num} qos dscp-cos counters interface {interface}'
        * 'show platform hardware fed switch {switch_type} qos dscp-cos counters interface {interface}'
    * Added ShowPlatformSoftwareFedSwitchActivEAclUsage
        * added new parser for cli "show paltform software fed switch active acl usage"
    * Added ShowPlatformSwitchActiveTcamUtilization
        * added new parser for cli "show platform hardware fed switch active fwd-asic resource tcam utilization"
    * Added ShowPlatformHardwareIomdQosPortIngressQueueStats
        * added new parser for clis
            * 'show platform hardware iomd <slot> qos port <no> ingress queue stats'
            * 'show platform hardware iomd switch <switch_no> <slot> qos port <no> ingress queue stats'
    * Added ShowPlatformHardwareIomdPortgroups
        * added new parser for clis
            * 'show platform hardware iomd <slot> portgroups'
            * 'show platform hardware iomd switch <switch_no> <slot> portgroups'
    * Added ShowPlatformHardwareFedActiveQosQueueConfigInterface
        * added new parser for clis
            * 'show platform hardware fed active qos queue config interface'
            * 'show platform hardware fed switch <no> qos queue config interface'
    * Added ShowPlatformHardwareQfpActiveInfrastructureExmemStatistics
        * show platform hardware qfp active infrastructure exmem statistics
    * Added ShowCryptoKeyMypubkeyMasterSchema
    * Added ShowCryptoKeyMypubkeyAll
        * show crypto key mypubkey all
    * Added ShowCryptoKeyMypubkeyRsa
        * show crypto key mypubkey rsa
    * Added ShowCryptoKeyMypubkeyEc
        * show crypto key mypubkey ec
    * Added ShowCryptoKeyMypubkeyRsaKeyName
        * show crypto key mypubkey rsa {key_name}
    * Added ShowCryptoKeyMypubkeyEcKeyName
        * show crypto key mypubkey ec {key_name}
    * Modified ShowLicenseTechSupport
        * Updated to parse new keys added in show license tech support. i.e. telemetry_report_summary
    * Added ShowCryptoIkev2Performance
        * show crypto ikev2 performance
    * Added ShowIpOspfDatabaseSummaryDetail
        * show ip ospf database database-summary detail
        * show ip ospf {process_id} database database-summary detail
    * Added ShowMonitorCaptureBuffer
        * show monitor capture {capture_name} buffer
    * Added ShowFQDNDatabase
        * added new parser for cli "show fqdn database"
    * Added ShowIpv6NdRaPrefix
        * added new parser for cli "show ipv6 nd ra nat64-prefix"


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowCtsInterface
        * Updated regex pattern <p2> to support Tunnel and Ethernet subinterfaces
    * Modified ShowIpInterface
        * Fixed bug where first line of the command is the output and the hostname contains an IP.
        * Improved Multicast reserved groups parsing when the IPs span multiple lines
    * Modified ShowModule
        * Added regex to match switches to support svl devices"
    * Modified ShowIsisNode
        * Changed the schema to match the 9500-X output"
    * Modified ShowL2vpnEvpnEthernetSegmentDetail
        * Fix bug in parser where CLI was being invoked twice
        * Change type of the 'interface' key in schema to 'list' (NOT BACKWARDS COMPATIBLE)
        * Change type of the 'ordinal' key to also allow 'str'
        * Fix bug when RD takes multiple lines in raw output
    * Modified ShowArp
        * Allow 'type' key to include '.' in regex pattern. E.g. '802.1Q'
    * Modified ShowPlatformFedActiveIfmMapping
        * Modified "group['ifgId'] is not None,
    * Created cat9k test symbolic link
    * Modified ShowPlatformSoftwareFedActiveAclSgacl
        * Fixed format for missing variable"
    * c9400
        * Modified ShowModule
            * Updated regex pattern <p2> to accommodate various outputs
    * Modified MonitorCaptureStopSchema
        * changed the parameter bytes_dropped_in_asic in MonitorCaptureStopSchema as optional, since it is not collected in silicon devices

* nxos
    * Modified ShowBgpL2vpnEvpnRouteType
        * Modified ShowBgpL2vpnEvpnRouteType to include VRF option in cli command.
        * Added Optional keys "pathtype", "as_path", "imported_from", and "gateway_ip" to schema.
        * Added path_type, which was matched in <p8> but unused previously, to dictionary output.
        * Added as_path, which was matched in <p9> but unused previously, to dictionary output.
        * Updated <p9> to accommodate AS-Paths that are not 'NONE'.
        * Added <p20> to parse the optional line with the format "Imported from 99.99.99.9910[5][0][0][32][100.4.1.2]/224".
        * Added <p21> to parse the optional line with the format "Gateway IP 0.0.0.0".

* iosxr
    * Modified ShowMplsLdpBindings
        * Modified Local bindings options to schema as Optional.


