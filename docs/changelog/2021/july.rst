July 2021
==========

July 27th - Genie v21.7
-----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.7                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.7                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

If you have pyATS installed, you can use:

.. code-block:: bash

    pyats version update

**genie**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* harness
    * commons
        * Added  include_os, exclude_os, include_devices, exclude_devices and all for check_config.


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* harness
    * Modified TestScript
        * Allow URLs to be given as yaml file CLI arguments

* testbed conversion
    * Do not convert interfaces with user defined interface class


**genie.libs.clean**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Add API "get_show_output_line_count"

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxr
    * Modified clean stage 'install_image_and_packages'
    * Updated to install image directly from tftp path
    * Updated install commit to mark fail if aborted
    * Updated to remove inactive packages
    * Updated to add sleep before doing install commit

* clean
    * Image handler update image names when using change_order_if_pass

* clean
    * reload
        * Added `via` argument to specify which connection to use on reconnect


**genie.libs.conf**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * Updated Vrf Conf
        * Added vni_mode_l3 to support new CLI "vni 4091 l3" under VRF for L3 VNI Configuration

**genie.libs.filetransferutils**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* filetransferutils
    * Updated HTTP fileserver to support http authentication
    * Updated logic to support multiple lines copy related config

**genie.libs.health**

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* health
    * Updated default health yaml
        * Changed to new argument style with '--health-tc-uids', '--health-tc-sections'
        * Added 'escape_regex_chars' argument to `get_testcase_name` api action
    * Updated default health yaml
        * Changed to use 'add_total True' for cpu/memory checks

* health plugin
    * Renamed '--health-webex' argument to '--health-notify-webex'.
    * Added DeprecationWarning message for deprecated arguments
    * Suppressed deprecated arguments from CLI help
    * Modified `--health-file` argument
        * File paths or URLs can now be passed as CLI arguments

**genie.libs.ops**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Modified Learn Vrf
        * Added new keys table_id and description

* iosxr
    * Modified Learn Vrf
        * Added new key "description"

* nxos
    * Modified Learn Vrf
        * Added new key "table_id"

**genie.libs.robot**

No changes

**genie.libs.sdk**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * Added TriggerProcessCliRestartNgmvpn
        * added 'cli restart of ngmvpn'
    * Added TriggerProcessCrashRestartNgmvpn
        * added 'crash process of ngmvpn'
    * Added TriggerProcessKillRestartNgmvpn
        * added 'kill process of ngmvpn'

* iosxe
    * Added the following APIs
        * unconfigure_interface_monitor_session
        * remove_channel_group_from_interface
        * remove_port_channel_interface
        * config_edge_trunk_on_interface
        * config_wan_macsec_on_interface
        * config_macsec_replay_protection_window_size
        * config_macsec_keychain_on_device
        * config_mka_keychain_on_interface
        * config_macsec_network_link_on_interface
        * unconfig_macsec_network_link_on_interface
        * config_mka_policy_xpn
        * clear_macsec_counters
        * config_mpls_ldp_on_device
        * remove_mpls_ldp_from_device
        * config_mpls_lable_protocol
        * remove_mpls_lable_protocol_from_device
        * config_mpls_ldp_router_id_on_device
        * remove_mpls_ldp_router_id_from_device
        * config_mpls_ldp_explicit_on_device
        * remove_mpls_ldp_explicit_from_device
        * config_speed_nonego_on_interface
        * config_encapsulation_on_interface
        * config_xconnect_on_interface
        * configure_service_internal
        * configure_ospf_routing
        * configure_ospf_routing_on_interface
        * unconfigure_ospf_on_device
        * configure_ospf_message_digest_key
        * configure_ospf_network_point
        * configure_ospf_bfd
        * configure_ospfv3
        * unconfigure_ospfv3
        * enable_ip_routing
        * enable_ipv6_unicast_routing
        * disable_ip_routing
        * set_system_mtu
        * disable_keepalive_on_interface
        * config_vlan
        * configure_mpls_ldp_nsr
        * configure_mpls_ldp_graceful_restart
        * configure_pseudowire_encapsulation_mpls
        * configure_mpls_pseudowire_xconnect_on_interface
        * unconfigure_mpls_ldp_nsr
        * unconfigure_mpls_ldp_graceful_restart
        * unconfigure_pseudowire_encapsulation_mpls
        * unconfig_macsec_keychain_on_device
        * unconfig_mka_policy_xpn
        * verify_device_tracking_policy_configuration
        * verify_missing_device_tracking_policy_configuration
        * verify_ipv6_nd_raguard_policy
        * verify_ipv6_nd_raguard_configuration
        * verify_missing_ipv6_nd_raguard_configuration
        * verify_ipv6_source_guard_policy
        * verify_ipv6_source_guard_configuration
        * verify_missing_ipv6_source_guard_configuration
        * verify_device_tracking_counters_vlan_dropped
        * verify_device_tracking_counters_vlan_faults
        * get_device_tracking_policy_name_configurations
        * get_device_tracking_database_details_binding_table_configurations
        * get_device_tracking_database_details_binding_table_count
        * get_ipv6_nd_raguard_policy_configurations
        * get_ipv6_source_guard_policy_configurations
        * get_device_tracking_counters_vlan_message_type
        * get_device_tracking_counters_vlan_faults
        * config_device_tracking_policy
        * unconfig_device_tracking_policy
        * config_ipv6_nd_raguard_policy
        * unconfig_ipv6_nd_raguard_policy
        * config_ipv6_source_guard_policy
        * unconfig_ipv6_source_guard_policy
        * device_tracking_attach_policy
        * device_tracking_detach_policy
        * ipv6_nd_raguard_attach_policy
        * ipv6_nd_raguard_detach_policy
        * ipv6_source_guard_attach_policy
        * ipv6_source_guard_detach_policy
        * enable_service_internal
        * disable_service_internal
        * device_tracking_unit_test
        * configure_ipv6_dhcp_guard_policy
        * unconfigure_ipv6_dhcp_guard_policy
        * configure_ipv6_nd_suppress_policy
        * unconfigure_ipv6_nd_suppress_policy
        * configure_ip_dhcp_snooping
        * unconfigure_ip_dhcp_snooping
        * configure_device_tracking_upgrade_cli
        * attach_ipv6_dhcp_guard_policy
        * detach_ipv6_dhcp_guard_policy
        * attach_ipv6_nd_suppress_policy
        * detach_ipv6_nd_suppress_policy

* subsection
    * Added  include_os, exclude_os, include_devices, exclude_devices and all for configure_replace.

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* blitz
    * Updated 'include'/'exclude' with Dq reason message
    * Updated decorator for pyATS Health Check
        * Support '--health-notify-webex' argument
    * gNMI empty datatype value not verifying correctly.
    * Added several tests for all gNMI reponse verification.
    * Updated 'check_opfield' API.
        * Avoided adding double quotes if value is already enclosed with quotes.

* sdk
    * updated copy_from_device and copy_to_device APIs to use http authentication

* utils
    * Updated 'get_testcase_name' API
        * Added `escape_regex_chars` argument to return escaped regex chars in testcase name
    * Updated 'copy_from_device' API
        * changed return value for API to str/None from boolean
    * Updated 'copy_to_device' API
        * changed return value for API to str/None from boolean

* iosxe
    * Modified the following APIs
        * configure_interface_monitor_session - Added description,source_vlan,mtu and vrf to config.
        * config_mpls_ldp_on_interface - Added named arguments to log and config.
        * remove_mpls_ldp_from_interface - Added named arguments to log and config.
    * Updated 'health_core' API
        * To support HTTP transfer via proxy support
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/dhcp/configure.py'
        * changed 'def disable_dhcp_snooping_Option_82(device)' to lowercase
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/interface/configure.py'
        * changed 'def config_helper_ip_on_interface' name
    * Modified 'health_cpu' API
        * Added 'add_total' argument to add total of CPU load
    * Modified 'health_memory' API
        * Added 'add_total' argument to add total of Memory usage

* iosxr
    * Modified get_available_space and get_total_space
        * Update get_available_space and get_total_space to return an int like other platforms do
    * Updated 'health_core' API
        * To support HTTP transfer via proxy support
    * Modified 'health_cpu' API
        * Added 'add_total' argument to add total of CPU load
    * Modified 'health_memory' API
        * Added 'add_total' argument to add total of Memory usage

* nxos
    * Updated 'health_core' API
        * To support HTTP transfer via proxy support
    * Modified 'health_cpu' API
        * Added 'add_total' argument to add total of CPU load
    * Modified 'health_memory' API
        * Added 'add_total' argument to add total of Memory usage

* iosxe/iosxr/nxos/aci
    * Delete file after get_show_tech API copied the file successfully

**genie.libs.parser**

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxr
    * Added ShowBgpBrief
        * Added 'show bgp {address_family} {ip_address} brief'
    * Modified show_mpls
        * added 'ShowMplsLdpDiscoveryDetails'
    * Added ShowWatchdogMemoryState
        * show watchdog memory-state
        * show watchdog memory-state Location {location}
    * Added ShowVariablesBoot
        * show variables boot
    * Added ShowVariablesSystem
        * 'show variables system'
    * Modified show_bgp
        * Added 'ShowBgpAllAllNexthops'
    * Added ShowShmwinSummary
        * Add show shmwin summary command

* nxos
    * Added ShowIpMrouteSummaryVrfAll
        * added 'show ip mroute summary vrf all'
    * Added ShowSystemInternalKernelMeminfo
        * show system internal kernel meminfo
    * Added ShowSystemResources
        * added 'show system resources'

* iosxe
    * Modified ShowRunInterface
        * Added parsing support (schema and parsers) for following outputs
            * power inline port priority high
            * power inline static max 30000
            * spanning-tree bpdufilter enable
            * ip flow monitor IPv4NETFLOW input
            * switchport protected
            * switchport block unicast
            * switchport block multicast
            * switchport trunk allowed vlan 820,900-905
            * ip dhcp snooping trust
            * ip arp inspection trust
    * Added ShowIpDhcpSnoopingDatabase
        * show ip dhcp snooping database
    * Added ShowIpDhcpSnoopingDatabaseDetail
        * show ip dhcp snooping database detail
    * Modified ShowStackPower
        * show stack-power budgeting
        * Added keys and regexes to incorporate a new cli_command
    * Added ShowPowerInlinePriority
        * show power inline priority
        * show power inline priority {interface}
    * Added ShowPowerInlineUpoePlus
        * show power inline upoe-plus
        * show power inline upoe-plus {interface}
    * Added ShowL2vpnEvpnEthernetSegment
        * show l2vpn evpn ethernet-segment
    * Added ShowL2vpnEvpnEthernetSegmentDetail
        * show l2vpn evpn ethernet-segment detail
        * show l2vpn evpn ethernet-segment interface {id} detail
    * Added ShowDeviceTrackingCountersInterface
    * Added ShowDeviceTracking
        * show device-tracking features
        * show device-tracking events
    * Added ShowIpv6
        * show ipv6 dhcp guard policy {policy name}
        * show flooding-suppression policy {policy name}
    * Added ShowDeviceTracking
        * show device-tracking database details
        * show device-tracking policy {policy_name}
        * show device-tracking counters vlan {vlanid}
    * Added ShowIpv6
        * show ipv6 nd raguard policy {policy_name}
        * show ipv6 source-guard policy {policy_name}
    * Modified ShowMplsLdp
        * Added ShowMplsLdpParameters
    * Added Parser
        * For "show sdwan tunnel sla index 0"
    * Added ShowL2fibPathListId
        * show l2fib path-list {id}
        * show l2fib path-list detail
    * Added ShowL2routeEvpnMacIpDetail
        * show l2route evpn mac ip detail
        * show l2route evpn mac ip host-ip <ip> detail
        * show l2route evpn mac ip host-ip <ip> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> producer <producer> mac-address <mac_addr> detail
        * show l2route evpn mac ip host-ip <ip> topology <evi><etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    * Added ShowNvePeers
        * 'show nve peers'
        * 'show nve peers interface nve {nve}'
        * 'show nve peers peer-ip {peer_ip}'
        * 'show nve peers vni {vni}'
    * Added ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlows
        * 'show platform software fed active fnf et-analytics-flows'
    * Added ShowL2vpnEvpnMacIp
        * show l2vpn evpn mac ip
        * show l2vpn evpn mac ip address {ipv4_addr}
        * show l2vpn evpn mac ip address {ipv6_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id}
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate
        * show l2vpn evpn mac ip bridge-domain {bd_id} local
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr}
        * show l2vpn evpn mac ip bridge-domain {bd_id} remote
        * show l2vpn evpn mac ip duplicate
        * show l2vpn evpn mac ip evi {evi_id}
        * show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr}
        * show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr}
        * show l2vpn evpn mac ip evi {evi_id} duplicate
        * show l2vpn evpn mac ip evi {evi_id} local
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr}
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr}
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr}
        * show l2vpn evpn mac ip evi {evi_id} remote
        * show l2vpn evpn mac ip local
        * show l2vpn evpn mac ip mac {mac_addr}
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr}
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr}
        * show l2vpn evpn mac ip remote
    * Added ShowL2vpnEvpnMacIpDetail
        * show l2vpn evpn mac ip address {ipv4_addr} detail
        * show l2vpn evpn mac ip address {ipv6_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}  detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} local detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} detail
        * show l2vpn evpn mac ip bridge-domain {bd_id} remote detail
        * show l2vpn evpn mac ip detail
        * show l2vpn evpn mac ip duplicate detail
        * show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} detail
        * show l2vpn evpn mac ip evi {evi_id} duplicate detail
        * show l2vpn evpn mac ip evi {evi_id} local detail
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} detail
        * show l2vpn evpn mac ip evi {evi_id} remote detail
        * show l2vpn evpn mac ip local detail
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr} detail
        * show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr} detail
        * show l2vpn evpn mac ip mac {mac_addr} detail
        * show l2vpn evpn mac ip remote detail
    * Added ShowL2vpnEvpnMacIpSummary
        * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} local summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} remote summary
        * show l2vpn evpn mac ip bridge-domain {bd_id} summary
        * show l2vpn evpn mac ip duplicate summary
        * show l2vpn evpn mac ip evi {evi_id} duplicate summary
        * show l2vpn evpn mac ip evi {evi_id} local summary
        * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} summary
        * show l2vpn evpn mac ip evi {evi_id} remote summary
        * show l2vpn evpn mac ip evi {evi_id} summary
        * show l2vpn evpn mac ip local summary
        * show l2vpn evpn mac ip mac {mac_addr} summary
        * show l2vpn evpn mac ip remote summary
        * show l2vpn evpn mac ip summary
    * Modified ShowL2vpnEvpnMac
        * show l2vpn evpn mac
        * show l2vpn evpn mac address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id}
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate
        * show l2vpn evpn mac bridge-domain {bd_id} local
        * show l2vpn evpn mac bridge-domain {bd_id} remote
        * show l2vpn evpn mac duplicate
        * show l2vpn evpn mac evi {evi_id}
        * show l2vpn evpn mac evi {evi_id} address {mac_addr}
        * show l2vpn evpn mac evi {evi_id} duplicate
        * show l2vpn evpn mac evi {evi_id} local
        * show l2vpn evpn mac evi {evi_id} remote
        * show l2vpn evpn mac local
        * show l2vpn evpn mac remote
    * Modified ShowL2vpnEvpnMacDetail
        * show l2vpn evpn mac address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} detail
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate detail
        * show l2vpn evpn mac bridge-domain {bd_id} local detail
        * show l2vpn evpn mac bridge-domain {bd_id} remote detail
        * show l2vpn evpn mac detail
        * show l2vpn evpn mac duplicate detail
        * show l2vpn evpn mac evi {evi_id} address {mac_addr} detail
        * show l2vpn evpn mac evi {evi_id} detail
        * show l2vpn evpn mac evi {evi_id} duplicate detail
        * show l2vpn evpn mac evi {evi_id} local detail
        * show l2vpn evpn mac evi {evi_id} remote detail
        * show l2vpn evpn mac local detail
        * show l2vpn evpn mac remote detail
    * Added ShowL2vpnEvpnMac
        * show l2vpn evpn mac
        * show l2vpn evpn mac address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id}
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate
        * show l2vpn evpn mac bridge-domain {bd_id} local
        * show l2vpn evpn mac bridge-domain {bd_id} remote
        * show l2vpn evpn mac duplicate
        * show l2vpn evpn mac evi {evi_id}
        * show l2vpn evpn mac evi {evi_id} address {mac_addr}
        * show l2vpn evpn mac evi {evi_id} duplicate
        * show l2vpn evpn mac evi {evi_id} local
        * show l2vpn evpn mac evi {evi_id} remote
        * show l2vpn evpn mac local
        * show l2vpn evpn mac remote
    * Added ShowL2vpnEvpnMacDetail
        * show l2vpn evpn mac address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail
        * show l2vpn evpn mac bridge-domain {bd_id} detail
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate detail
        * show l2vpn evpn mac bridge-domain {bd_id} local detail
        * show l2vpn evpn mac bridge-domain {bd_id} remote detail
        * show l2vpn evpn mac detail
        * show l2vpn evpn mac duplicate detail
        * show l2vpn evpn mac evi {evi_id} address {mac_addr} detail
        * show l2vpn evpn mac evi {evi_id} detail
        * show l2vpn evpn mac evi {evi_id} duplicate detail
        * show l2vpn evpn mac evi {evi_id} local detail
        * show l2vpn evpn mac evi {evi_id} remote detail
        * show l2vpn evpn mac local detail
        * show l2vpn evpn mac remote detail
    * Added ShowL2vpnEvpnMacSummary
        * show l2vpn evpn mac bridge-domain {bd_id} duplicate summary
        * show l2vpn evpn mac bridge-domain {bd_id} local summary
        * show l2vpn evpn mac bridge-domain {bd_id} remote summary
        * show l2vpn evpn mac bridge-domain {bd_id} summary
        * show l2vpn evpn mac duplicate summary
        * show l2vpn evpn mac evi {evi_id} duplicate summary
        * show l2vpn evpn mac evi {evi_id} local summary
        * show l2vpn evpn mac evi {evi_id} remote summary
        * show l2vpn evpn mac evi {evi_id} summary
        * show l2vpn evpn mac local summary
        * show l2vpn evpn mac remote summary
        * show l2vpn evpn mac summary


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowRouteAllSummary
        * Fixed pattern p3 to accept routed source instances with '.'
    * Modified ShowPlatformi(show redundancy)
        * Added regex p3_2 to accomodate standby RP for eXR
    * Modified ShowOspfv3Neighbor
        * updated regex pattern p1 to handle hyphens in VRF name
    * Modified ShowRouteIpv4
        * updated regex pattern p6 to handle 'type' after 'candidate default path'
        * updated class to folder based unit tests
    * Modified ShowProcesses
        * Added Location data if not applicable
    * Modified ShowHsrpDetail
        * Updated regex pattern <p1> to accommodate various outputs.
        * Moved regexes outside of loop
    * Modified ShowHsrpSummary
        * Moved regexes outside of loop

* iosxe
    * Modified ShowRunInterface
        * Fixed channel_group (was not working).
            * Added channel_group to ShowRunInterfaceSchema
            * Updated intf_dict to make it work properly
    * Modified ShowPolicyMapTypeSuperParser
        * Added patterns p43..p47 for AFD WRED stats
    * Modified ShowEtherchannelSummary
        * Added regex pattern p6 to accommodate various port outputs.
    * Modified ShowDeviceTrackingDatabaseInterface
        * Made `limit` key optional on binding_table and refactored code to support this change.
    * Modified ShowStandbyAll
        * Optimized parser and fixed issue with multiple group numbers under same interface
    * Modified ShowDeviceTrackingCountersVlan
        * Fix parsing of faults
        * Fix parsing of dropped message to account for more cases
    * Modified ShowBgpDetailSuperParser
        * modified p10 to cover scenario where EVPN ESI is in output, but not paired with gateway address or local_vtep information
    * Modified ShowLispEidTableVrfIpv4Database
        * Changed key <User> to Any() in schema
    * Modified ShowStandbyAll
        * Updated regex pattern <p11> to accommodate various outputs.
        * Updated format of parser and moved regexes out of loop
    * Modified ShowStandbyInternal
        * Updated format of parser and moved regexes out of loop
    * Modified ShowStandbyDelay
        * Updated format of parser and moved regexes out of loop
    * Modified ShowWirelessClientMacDetail
        * rewrote parser for better stability
        * added missing argument to cli command
        * added new optional keys, made several keys in schema optional
        * some schema entries are now int or string
        * added new test to cover schema changes
    * Modified ShowPlatformSoftwareFed
        * Update regex P36 to include objidADJ SPECIAL0
        * Update regex P25 and corresponding schema to include bwalk parameters
        * Modify regex P11 and corresponding schema to modify flags and pdflags from str to
        * Modify regex P14 to include label_aal
        * Add blank lines and comments between regex
        * Add full syntax of commands
        * Modify capital letters to small letters in key name in Schema and parser class
        * Delete Optional Keyword in some of key names in Schema
        * Modify nobj0 and nobj1 from str to list in regex P9 and corresponding Schema
        * Add folder based unittests
    * Delete iosxe/show_platform_software_fed.py instead content is Appended in iosxe/show_platform.py
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * Fixed pattern p1 to accept `Not Running` as valid state
        * Fixed patter p2 to accept `Down` and `Reset` as valid states

* nxos
    * Modified ShowInterface
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modify ShowSpanningTreeDetail
        * Added schema key 'peer_type'
    * Modified ShowMacAddressTableBase
        * updated regex to handle NA for age value
        * added test golden_output_3 to test changes
    * Updated RunBashTop
        * updated p1 regex to support various output for uptime

* junos
    * Modified ShowRouteReceiveProtocolExtensive()
        * Modified Regex to also match IPv6 Nethops.
    * Modified ShowRouteReceiveProtocolPeerAddressExtensive()
        * Modified Regex to also match IPv6 Destinations.
        * Modified Regex to also match IPv6 Nexthops.

**genie.telemetry**

No changes

**genie.trafficgen**

No changes

**genie.webdriver**

No changes
