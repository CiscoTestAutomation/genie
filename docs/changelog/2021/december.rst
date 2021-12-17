December 2021
==========

December 14 - Genie v21.12
--------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.12                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.12                         |
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
    * Modified
        * Removed start_pool calls in lieu of device connect pool param
    * Modified disconnect()
        * fixed a bug where HA devices would encounter a hash error during disconnection

* genie.harness
    * Fixed a bug where dev.learn('all') would not learn the device configuration.
    * Fixed a bug where section processors would run where they are not defined.

* json
    * Updated make json command
        * Fixed logic to show correct url regardless order of data


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* harness
    * Modified configure()
        * added debug message for configure() with Jinja2

* api
    * Added 'alias' argument for device.api
        * can specify device alias to switch connections

* conf
    * Updated API class
        * Added banner message to do 'make json' in case of JSON file issue



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added
        * support for platform mds in genie clean
        * support for platform n5k in genie clean

* iosxe
    * Added configure_umbrella_in_out API
        * Umbrella inside and outside configuration
    * Added unconfigure_umbrella_in_out API
        * Umbrella inside and outside unconfiguration
    * Added configure_umbrella_global_parameter_map API
        * Umbrella parameter-map configuration
    * Added unconfigure_umbrella_global_parameter_map API
        * Umbrella parameter-map unconfiguration
    * Added configure_umbrella_local_bypass API
        * Umbrella local bypass regex pattern configuration
    * Added unconfigure_umbrella_local_bypass API
        * Umbrella local bypass regex pattern unconfiguration
    * Added execute_clear_dns_statistics API
        * Umbrella statistics clear
    * Added execute_test_ngdns_lookup API
        * ngdns test cli execution
    * Added configure_ip_domain_lookup API
        * ip domain lookup configuration
    * Added unconfigure_ip_domain_lookup API
        * ip domain lookup unconfiguration
    * Added configure_ip_name_server API
        * ip name server configuration
    * Added unconfigure_ip_name_server API
        * ip name server unconfiguration
    * Added configure_nat_in_out API
        * configure nat inside outside over interface
    * Added unconfigure_nat_in_out API
        * unconfiguration nat inside outside over interface
    * Added configure_nat_overload_rule API
        * nat overload rule configuration
    * Added unconfigure_nat_overload_rule API
        * nat overload rule unconfiguration
    * Added execute_clear_nat_translation API
        * clear nat translation

* stages
    * nxos/n9k
        * Added clean stage InstallImage
    * nxos
        * Added UT for ChangeBootVariable nxos clean stage apis
    * common
        * Added UT for WriteErase common apis
        * Added UT for BackupFileOnDevice common apis
        * Added UT for DeleteFilesFromServer common apis
    * apic
        * Added UT for FabricClean clean stage apis
    * iosxe/sdwan
        * Added UT for ApplyConfiguration clean stage apis
        * Added UT for ExpandImage clean stage apis
        * Added UT for SetControllerMode clean stage apis
    * iosxe
        * Added UT for InstallImage clean stage apis
        * Added UT for InstallRemoveInactive clean stage apis
    * common
        * Added UT for ApplyConfiguration clean stage apis
    * apic
        * Added UT for FabricClean clean stage apis
        * Added UT for NodeRegistration clean stage apis
        * Added UT for ApplyConfiguration clean stage apis
    * iosxr
        * Added UT for LoadPies clean stage apis
        * Added UT for TftpBoot clean stage apis
    * common
        * Added UT for DeleteBackupFromDevice common apis
        * Added UT for PowerCycle common apis
        * Added UT for Pingserve common apis
    * nxos/aci
        * Added UT for FabricClean nxos clean stage apis
    * iosxe
        * Added UT for InstallPackages clean stage apis
    * iosxe/cat9k
        * Added UT for TftpBoot clean stage apis

* aireos
    * Added
        * Clean cli_boot


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified config_extended_acl API
        * Added line to configure policy permit any any
    * Removed pre requisite check for cat9k and cat 9500 from exec order.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added
        * Vxlan OPS object
        * Unit tests for above Vxlan OPS object
        * TriggerUnconfigConfigNveVni Trigger to unconfigure and reconfigure a

* nxos
    * Added OSPFv3 conf model
        * Conf model handles all possible attributes for NXOS


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added
        * Support for an NVE interface in the Interface CONF object
        * Unit tests for above addition to the Interface CONF object



genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health
    * Updated logic for reasons why health is not running
        * show the reason in case device is not connected
    * Fixed a case that health says PASSED even though device is not connected
    * Optimized logic for `--health-tc-groups` argument
    * Adjusted `pyats_health.yaml` template due to above.

* health plugin
    * Updated logic to save 'pyats_health.yaml' for '--health-checks'
        * To reflect values based on given parameters for '--health-checks'
    * Updated health yaml template
        * to save a case which have one TC without separated connect section


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* health plugin
    * Added '--health-clear-logging' argument
        * To clear logging every health logging check
    * Updated health yaml template
        * added 'clear_logging' for '--health-clear-logging' argument



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
    * Added configure_common_criteria_policy API
        * API for configuring common criteria policy for enable password.
    * Added unconfigure_common_criteria_policy API
        * API for unconfiguring a common criteria policy.
    * Added configure_enable_policy_password API
        * API for configuring enable password with a common criteria policy
    * Added unconfigure_enable_policy_password API
        * API for unconfiguring enable password.
    * Added configure_service_password_encryption API
        * API for configuring service password with encryption.
    * Added unconfigure_service_password_encryption API
        * API for unconfiguring service password encryption
    * Added verify_enable_password API
        * API for verifying enable password
    * Added AAA Secret Key Hash API
        * Added API to retrive values from CLI commands to compare with YANG model data for Secret key Hash AAA leaf
    * Added API 'configure_evpn_default_gateway_advertise_global'
    * Added API 'configure_evpn_evi_replication_type'
    * Added API 'configure_evpn_instance_encapsulation_type'
    * Added API 'configure_evpn_l2_instance_vlan_association'
    * Added API 'configure_evpn_l3_instance_vlan_association'
    * Added API 'configure_evpn_replication_type'
    * Added API 'configure_l2vpn_evpn'
    * Added API 'configure_l2vpn_evpn_router_id'
    * Added API 'unconfigure_evpn_default_gateway_advertise_global'
    * Added API 'unconfigure_evpn_evi_replication_type'
    * Added API 'unconfigure_evpn_instance_encapsulation_type'
    * Added API 'unconfigure_evpn_l2_instance_vlan_association'
    * Added API 'unconfigure_evpn_l3_instance_vlan_association'
    * Added API 'unconfigure_evpn_replication_type'
    * Added API 'unconfigure_l2vpn_evpn'
    * Added API 'unconfigure_l2vpn_evpn_router_id'
    * Added configure_logging_buffered_errors api
        * Confgiure logging buffered errors
    * Added unconfigure_logging_buffered_errors api
        * Unconfgiure logging buffered errors
    * Added configure_logging_console_errors api
        * Confgiure logging console errors
    * Added unconfigure_logging_console_errors api
        * Unconfgiure logging console errors
    * Added get_authentication_config_mode api
        * Get current authentication config mode on device
    * Added 'clear_access_session_intf' API
        * clearing access-session interface
    * Added 'clear_ipv6_mld_group' API
        * clearing ipv6 mld group
    * Added 'configure_no_boot_manual' API
        * configuring boot manual
    * Added 'clear_ip_mroute_vrf' API
        * clearing ip mroute on perticular vrf
    * Added 'clear_errdisable_intf_vlan' API
        * clearing errdisable interface with vlan
    * Added configure_class_map API
        * API for configuring class map for policy.
    * Added unconfigure_class_map API
        * API for unconfiguring class map from policy.
    * Added configure_policy_map API
        * API for configuring policy map for service-policy.
    * Added unconfigure_policy_map API
        * API for unconfigure_policy_map policy map.
    * Added configure_table_map API
        * API for configuring table map.
    * Added unconfigure_table_map API
        * API for unconfiguring table map.
    * Added get_trunk_interfaces_encapsulation api
        * get a dictionary with interface as key and encapsulation as the value
    * Added get_show_output_section api
        * Display the lines which are match from section
    * Added execute_clear_platform_software_fed_switch_acl_counters_hardware api
        * clear platform software fed switch acl counters hardware
    * Modified start_packet_capture api
        * Added direction to capture the packets
    * Added configure_terminal_length api
        * Configure terminal length
    * Added configure_terminal_width api
        * Configure terminal width
    * Added configure_logging_buffer_size api
        * Configure logging buffer
    * Added configure_terminal_exec_prompt_timestamp api
        * Configure terminal exec prompt timestamp
    * Modified execute_delete_boot_variable api
        * boot variable arg can now be a list
    * Added configure_logging_console API
        * Enable logging console
    * Added unconfigure_logging_console API
        * disble logging console
    * Added configure_logging_monitor API
        * Enable logging monitor
    * Added unconfigure_logging_monitor API
        * disble logging monitor
    * added `get_ip_theft_syslogs` API
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
    * Added unconfigure_device_tracking_binding API
    * Added verify_empty_device_tracking_policies API
    * Added verify_empty_device_tracking_database API
    * Added
        * configure_interface_mac_address
        * unconfigure_interface_mac_address
    * Added
        * configure_interface_pvlan_host_assoc
        * configure_interface_switchport_pvlan_mode
        * configure_interface_span_portfas
        * verify_port_channel_member_state
        * configure_vtp_mode
        * configure_pvlan_svi_mapping
        * configure_pvlan_primary
        * configure_pvlan_type
        * configure_vrf_definition_family
    * Added configure_eapol_eth_type_interface API
        * Configures EAPOL Ethernet Type on interface
    * Added unconfigure_eapol_eth_type_interface API
        * Unconfigures EAPOL Ethernet Type on interface
    * Added config_mka_policy_delay_protection API
        * Configures MKA Policy with delay protection on device/interface
    * Added unconfig_mka_policy_delay_protection API
        * Unconfigures MKA Policy with delay protection on device/interface
    * Added configure_mka_policy API
        * Configures MKA policy on device/interface
    * Added unconfigure_mka_policy API
        * Unconfigures MKA policy on device/interface
    * Added unconfigure_mka_keychain_on_interface API
        * Unconfigures MKA keychain on interface
    * Added enable_ipv6_multicast_routing API
        * enables ipv6 multicast routing on device
    * Added disable_ipv6_multicast_routing API
        * disables ipv6 multicast routing on device
    * Added configure_ospfv3_network_point API
        * Configures ospfv3 network type point-to-point on interface
    * Added unconfigure_ospfv3_network API
        * Unconfigures ospfv3 network type on interface
    * Added configure_ipv6_ospf_bfd API
        * Configures ipv6 ospf bfd on interface
    * Added unconfigure_ipv6_ospf_bfd API
        * Unconfigures ipv6 ospf bfd on interface
    * Added unconfigure_bfd_on_interface API
        * Unconfigures bfd on interface
    * Added configure_ipv6_object_group_network API
        * configures ipv6 network object group  on device
    * Added configure_ipv6_object_group_service API
        * configures ipv6 service object group  on device
    * Added configure_ipv6_ogacl API
        * configures IPv6 OG ACL on device
    * Added configure_ipv6_acl_on_interface API
        * configures IPv6 og acl on interface
    * Added unconfigure_ipv6_ogacl_ace API
        * Unconfigures IPv6 OGACL ACE on device
    * Added unconfigure_ipv6_object_group_service_entry api
        * Unconfigures ipv6 service object group entry on device
    * Added unconfigure_ipv6_object_group_network_entry api
        * Unconfigures ipv6 network object group entry on device
    * Added unconfigure_ipv6_object_group_service api
        * Unconfigures ipv6 service object group  on device
    * Added unconfigure_ipv6_object_group_network api
        * Unconfigures ipv6 network object group  on device
    * Added unconfigure_ipv6_acl API
        * unconfigures ipv6 acl on device
    * Added unconfigure_ipv6_acl_on_interface api
        * Removes ipv6 acl from interface
    * Added config_ip_pim under multicast.py
    * Added config_rp_address under multicast.py
    * Added config_multicast_routing_mvpn_vrf under multicast.py
    * Added configure_igmp_version under multicast.py
    * Added unconfigure_igmp_version under multicast.py
    * Added configure_ip_pim_vrf_ssm_default under multicast.py
    * Added unconfigure_ip_pim_vrf_ssm_default under multicast.py
    * Added config_standard_acl_for_ip_pim under multicast.py
    * Added unconfig_standard_acl_for_ip_pim under multicast.py
    * Added verify_ip_pim_vrf_neighbor under verify.py multicast folder
    * Added verify_mpls_mldp_neighbor under verify.py multicast folder
    * Added verify_mpls_mldp_root under verify.py multicast folder
    * Added verify_mfib_vrf_hardware_rate under verify.py multicast folder
    * Added verify_mfib_vrf_summary under verify.py multicast folder
    * Added verify_mpls_route_groupip under verify.py multicast folder
    * Added verify_bidir_groupip under verify.py multicast folder
    * Added unconfigure_mdt_auto_discovery_mldp API
    * Added configure_mdt_overlay_use_bgp API
    * Added configure_mdt_auto_discovery_mldp API
    * Added unconfigure_mdt_overlay_use_bgp API
    * Added verify_mpls_forwarding_table_gid_counter API
    * Added verify_mpls_forwarding_table_vrf_mdt API
    * Added clear_arp_cache API
        * Clears device arp cache
    * Added config_ip_on_vlan API
        * Configures IPv4/IPv6 address on a vlan
    * Added unconfigure_interface_switchport_access_vlan API
        * Unconfigures switchport access on interface vlan
    * Added authentication convert-to new-style single-policyinterface {interface}
    * Added access-session single-policy interface {interface}
    * Added access-session single-policy policy-name {policy_name}
    * Added authentication convert-to new-style
    * Added
        * Added verify_pattern_in_show_logging api to verify the pattern list in show logging output
    * Added remove_acl_from_interface API
        * API for removing an ACL from an interface

* utils
    * Added get_interface_type_from_yaml
        * get 'type' of interface for a device from topology in testbed object

* api utils
    * Modified api_unittest_generator
        * Added support to positional arguments and keyword arguments in API calls
    * Added test_api_unittest_generator
        * Added unit tests to cover api_unittest_generator code

* common
    * Added 'execute_and_parse_json' API
        * Executes a CLI command that outputs JSON and parses the output of the command as

* iosxr
    * Added clear_logging API
        * To clear logging message

* nxos
    * Added clear_logging API
        * To clear logging message

* aireos
    * Added
        * verify_ping
        * get_boot_variables


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fix remove_device_tracking_policy
        * changed string format variable name
    * Fix clear_device_tracking_database
        * changed to parse passed in args properly
    * Fixed `get_ip_theft_syslogs` to support syslogs without a timezone
    * Modified
        * configure_dot1x_supplicant
    * Modified
        * configure_interface_switchport_access_vlan
    * Modified get_bgp_route_ext_community
        * Fixed a hole in the logic if neither vrf nor rd arguments were passed
    * Modified unconfigure_acl
        * Added option to unconfigure standard no ip access-list as well as extended
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/mdns/configure.py'
        * Added 'configure_mdns_controller' API
        * Added 'unconfigure_mdns_controller' API
        * Added 'configure_mdns_svi' API
        * Added 'unconfigure_mdns_svi' API
        * Added 'clear_mdns_query_db' API
        * Added 'clear_mdns_statistics' API
        * Added 'unconfig_mdns_sd_service_peer' API
        * Added 'unconfigure_mdns_service_definition' API
    * Modified TriggerUnconfigConfigVrf
        * handle SchemaEmptyParserError on empty 'show vrf detail' output
    * APIs configure_interfaces_shutdown and configure_interfaces_unshutdown
        * Now raises a SubCommandFailure instead of logging an error
    * BGP API name change from 'get_routing_routes' to 'get_bgp_routes' due to conflict API name
        * WARNING API name is changed. if using this API, script/testcase needs to be Updated
    * BGP verify_bgp_routes_from_neighbors API
        * Updated to adjust API name change of from 'get_routing_routes' to 'get_bgp_routes'
    * PBR API name change from 'configure_route_map' to 'configure_pbr_route_map' due to conflict API name
        * WARNING API name is changed. if using this API, script/testcase needs to be Updated
    * PBR API name change from 'unconfigure_route_map' to 'unconfigure_pbr_route_map' due to conflict API name
        * WARNING API name is changed. if using this API, script/testcase needs to be Updated
    * Updated health_logging API
        * Added 'clear_log' argument to clear logging message

* api utils
    * Modified API Unit Test Generator
        * Fixed `--module-path` parsing
    * Modified api_uniitest_generator.py
        * Fixed Value Error when no arguments were provided
    * Modified API Unit test Generator
        * Added exception for unsupported connections
        * Added init_config_command and init_exec_command to connection settings
        * Updated test template to include connection settings
    * Modified api_unittest_generator
        * Fixed bug with --module-path
        * Removed unused arguments on _create_testbed

* modified is_next_reload_boot_variable_as_expected api
    * Added better error handling by rising an exception.

* common
    * Modified verify.py
        * Changed verify_current_image comparison method to split directories and images on delimiter characters
    * Updated load_jinja_template API
        * Added StrictUndefined jinja2.Environment to error out in case definition in template is not passed

* ios and iosxe
    * Using regex search in get_md5_hash_of_file API

* apic
    * Updated apic_rest_get API
        * Added target_subtree_class argument support
    * Updated apic_rest_post API
        * Added xml_payload argument support

* common api
    * Updated get_devices API
        * Show more accurate message depending on condition
        * check if testbed object is same with runtime.testbed and give warning if different

* iosxr
    * Updated health_logging API
        * Added 'clear_log' argument to clear logging message

* nxos
    * Updated health_logging API
        * Added 'clear_log' argument to clear logging message

* nxos/n9k
    * Moved health API for nxos n9k
        * To fix API pickup via abstraction

* linux
    * Updated scp API
        * Updated prompt pattern and docstring



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added class ShowLispEthernetDatabase
        * show lisp instance-id {instance_id} ethernet database
        * show lisp {lisp_id} instance-id {instance_id} ethernet database
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet database
        * show lisp eid-table vlan {vlan} ethernet database
    * Added ShowPolicyMapClass
        * show policy-map {policy_name} class {class_name}
    * Modified ShowPolicyMapInterfaceOutput
        * Added p38_1 regexp to match new priority output line
    * Added class ShowLispIpv4MapCachePrefix
        * show lisp instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}
    * Added class ShowLispIpv6MapCachePrefix
        * show lisp instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}
    * Added class ShowLispSessionRLOC
        * show lisp session {rloc}
        * show lisp {lisp_id} session {rloc}
        * show lisp locator-table {locator_table} session {rloc}
        * show lisp vrf {vrf} session {rloc}
    * Added AuthenticationDisplayConfigMode parser
        * authentication display config-mode
    * Modified ShowRunInterface parser
        * Added code to grep trust_device, ipv6_destination_guard_attach_policy and ipv6_source_guard_attach_policy
    * Added AuthenticationDisplayConfigMode
        * 'authentication display config-mode'
    * Added ShowIpMfibVrfSummay
        * show ip mfib vrf vrf summary
    * Added ShowIpMfibVrfActiveHwRate
        * show ip mfib vrf vrf active | c HW Rate
    * Added ShowIpMfibVrfActive
        * show ip mfib vrf vrf active
    * Added class ShowLispInstanceIdIpv4ForwardingEID
        * show lisp instance-id {instance_id} ipv4 forwarding eid remote
    * Added class ShowLispInstanceIdIpv6ForwardingEID
        * show lisp instance-id {instance_id} ipv6 forwarding eid remote
    * Added ShowAAACommonCriteraPolicy
        * Parser for show aaa common-criteria policy name {policy_name}
    * Added ShowFlowExporter parser
        * show flow exporter
    * Added ShowVlanSummary parser
        * show vlan summary
    * Added ShowFlowRecord parser
        * show flow record
    * Added ShowRunningConfigFlowExporter parser
        * show running-config flow exporter
    * Added ShowIpIgmpSnoopingGroupsCount parser
        * show ip igmp snooping groups count
    * Added ShowIpv6MldSnoopingAddressCount parser
        * show ipv6 mld snooping address count
    * Modified ShowBootSystem parser
        * Changed enable_break type and regexp according to stack output
    * Added  ShowIpPimTunnel parser
        * show ip pim tunnel
    * Fixed ShowStandbyBrief parser
        * Modified regexp to grep preempt state
    * Added ShowIpv6DhcpLdra
        * show ipv6 dhcp-ldra
    * Added ShowIpv6DhcpLdraStatistics
        * show ipv6 dhcp-ldra statistics
    * Added ShowLicenseAll
        * show license all
    * Added ShowLicenseEventlog2
        * show license eventlog 2
    * Added ShowLicenseRumIdDetail
        * show license rum id detail
    * Added ShowLicenseStatus
        * show license status
    * Added ShowLicenseUsage
        * show license usage
    * Added class ShowLispIAFServer
        * show lisp instance-id {instance_id} {address_family} server summary
        * show lisp {lisp_id} instance-id {instance_id} {address_family} server summary
        * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary
    * Added ShowLispEidWatch
        * for 'show lisp {lisp_id} instance-id {instance_id} {address_family} eid-watch'
        * for 'show lisp instance-id {instance_id} {address_family} eid-watch'
        * for 'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} eid-watch'
        * for 'show lisp eid-table {eid_table} {address_family} eid-watch'
        * for 'show lisp eid-table vlan {vlan_id} ethernet eid-watch'
    * Added ShowLispEthernetMapCache
        * 'show lisp instance-id {instance_id} ethernet map-cache'
        * 'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache'
        * 'show lisp eid-table vlan {vlan_id} ethernet map-cache'
        * 'show lisp locator-table {vrf} instance-id {instance_id} ethernet map-cache'
    * Added ShowLispInstanceIdForwardingState
        * 'show ip lisp instance-id {instance_id} forwarding state'
        * 'show ipv6 lisp instance-id {instance_id} forwarding state'
        * 'show lisp instance-id {instance_id} {service} forwarding state'
    * Added ShowLispInstanceIdDNStatistics
        * 'show lisp {lisp_id} instance-id 16777214 dn statistics'
        * 'show lisp instance-id 16777214 dn statistics'
    * Added ShowLispRedundancy
        * for 'show lisp {lisp_id} redundancy'
        * for 'show lisp redundancy'
        * for 'show lisp locator-table {locator_table} redundancy'
    * Added class ShowLispSessionCapabilityRLOC
        * show lisp vrf {vrf} session capability {rloc}
    * Added ShowLoggingOnboardRpActiveUptime
        * show logging onboard rp active uptime
    * Added ShowLoggingOnboardRpActiveStatus
        * show logging onboard rp active status
    * Added ShowLoggingOnboardRpActiveTemperatureContinuous
        * show logging onboard rp active temperature continuous
        * show logging onboard rp active voltage continuous
        * show logging onboard rp active message continuous
    * Added ShowMkaStatistics
        * show mka statistics
    * Added ShowPlatformSoftware
        * for 'show platform software fed {switchvirtualstate} mpls lspa all | c {mode}'
        * for 'show platform software fed {switchvirtualstate} mpls lspa all'
    * Added ShowPlatformHardware
        * for 'show platform hardware fed switch active fwd-asic drops exceptions'
    * Added ShowPowerInlineUpoePlusModule
        * show power inline upoe-plus module {mod_num}
    * Added ShowRunningConfigFlowMonitor
        * show running-config flow monitor
    * Added ShowFlowMonitorAll
        * show flow monitor all
    * Added ShowTelemetryReceiverName
        * show telemetry receiver name {name}
    * Added ShowTelemetryReceiverAll
        * show telemetry receiver all
    * Added ShowTelemetryInternalSensor
        * show telemetry internal sensor subscription {sub_id}
        * show telemetry internal sensor stream {stream_type}
    * Added ShowTelemetryInternalSubscriptionAllStats
        * show telemetry internal subscription all stats
    * Added ShowTelemetryConnectionDetail
        * show telemetry connection all
        * show telemetry connection {con_idx} detail
    * Updated ShowTelemetryIETFSubscription
        * show telemetry ietf subscription {sub_id}
        * show telemetry connection {con_idx} subscription
    * Added ShowVpdn
        * show vpdn
    * Modified ShowUsers
        * Added Optional schema keys <connection_details>, <intf>, <u_name>, <mode>, <idle_time>, and <peer_address>
    * Added ShowIpIgmpVrfGroups
        * show ip igmp vrf {vrf} groups
    * Added ShowPlatformMplsRlistSummary
        * show platform software fed switch {switch_type} mpls rlist summary
    * Added ShowPlatformSoftwareInterfaceSwitchF0Brief
        * show platform software interface switch {mode} F0 brief
    * Added ShowPlatformSoftwareFedSwitchPortSummary
        * show platform software fed switch {mode} port summary
    * Added ShowPower
        * show power {detail}
    * Added ShowIdprom
        * show idprom
    * ADDED ShowUmbrellaDeviced
        * 'show umbrella deviceid'
    * ADDED ShowUmbrellaConfig
        * 'show umbrella config'
    * ADDED ShowPlatformSoftwareDnsUmbrellaStatistics
        * 'show platform software dns-umbrella statistics'
    * Added ShowInterfaceSummaryVlan
        * show interface summary vlan
    * Added ShowMacAddressTableCountSummary
        * show mac address-table count summary
    * Added `show cef path sets summary`
    * Added `show cef uid`
    * Addded `show cef path set id <id> detail | in Relpicate oce`
    * Added `show mpls forwarding-table | sect gid`
    * Added ShowLispEthernetMapCachePrefix
        * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp eid-table vlan {vlan} ethernet map-cache {eid_prefix}
        * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    * Added class ShowControllerVDSL
    * Added ShowAAACacheGroup
        * show aaa cache group {server_grp} all
        * show aaa cache group {server_grp} profile {profile}
    * Inherit schema and parser for show crypto pki certificates verbose commands
        * show crypto pki certificates verbose {trustpoint}
    * Inherit Ipv4 schema and parser for Show Lisp Ipv6 Route Import Map Cache commands
        * show lisp instance-id {instance_id} ipv6 route-import map-cache
        * show lisp instance-id {instance_id} ipv6 route-import map-cache {eid}
        * show lisp instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache
        * show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}
        * show lisp eid-table vrf {vrf} ipv6 route-import map-cache
        * show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid}
        * show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid_prefix}
        * show lisp eid-table {eid_table} ipv6 route-import map-cache
        * show lisp eid-table {eid_table} ipv6 route-import map-cache {eid}
        * show lisp eid-table {eid_table} ipv6 route-import map-cache {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}
    * Added ShowLispIpv6Away
        * show lisp instance-id {instance_id} ipv6 away
        * show lisp instance-id {instance_id} ipv6 away {eid}
        * show lisp instance-id {instance_id} ipv6 away {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 away
        * show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid_prefix}
        * show lisp eid-table {eid_table} ipv6 away
        * show lisp eid-table {eid_table} ipv6 away {eid}
        * show lisp eid-table {eid_table} ipv6 away {eid_prefix}
        * show lisp eid-table vrf {eid_table} ipv6 away
        * show lisp eid-table vrf {eid_table} ipv6 away {eid}
        * show lisp eid-table vrf {eid_table} ipv6 away {eid_prefix}
    * Added ShowInventoryOID
        * show inventory OID
    * Added  ShowInventoryRaw
        * show inventory raw
        * show inventory raw | include {include}
    * Added ShowNveInterfaceDetail
        * show nve interface nve {nve_num} detail
    * Added ShowNveVni
        * show nve vni
    * Modified ShowIpEigrpInterfaces
        * show ip eigrp vrf <vrf> interfaces
    * Added ShowControllers for Catalyst 9300 platform
        * show controllers ethernet-controller {interface} phy detail
    * Modified ShowRunInterface
        * Added parsing support (schema and parsers) for following output
            * spanning-tree portfast trunk

* nxos
    * Added ShowIncompatibilityNxos
        * show incompatibility nxos {image}
    * Added ShowBootMode
        * show boot mode
    * Added ShowInstallAllStatus
        * show install all status
    * Added ShowIpv6Neighbor
        * show ipv6 neighbor
        * show ipv6 neighbor vrf all
        * show ipv6 neighbor vrf <vrf>
    * Added ShowSpanningTreeIssuImpact
        * show spanning-tree issu-impact
    * Modified ShowInterfaceBrief
        * show interface brief fix to handle vlan bd down state
    * Added ShowIpv6Ospfv3NeighborsDetail
        * show ipv6 ospfv3 neighbors detail
        * show ipv6 ospfv3 neighbors <neighbor> detail
        * show ipv6 ospfv3 neighbors detail vrf <vrf>
        * show ipv6 ospfv3 neighbors <neighbor> detail vrf <vrf>

* generic
    * Added ShowVersion
        * show version
    * Added Inventory
        * show inventory
    * Added Uname
        * uname -a

* utils
    * Modified common.py
        * Added banner message to do 'make json' in case of JSON file issue
    * Modified unittests.py
        * To support excluding parser class via EXCLUDE_CLASSES

* iosxr
    * Added ShowIsisSegmentRoutingSrv6Locators
        * show isis segment-routing srv6 locators
        * show isis instance {instance} segment-routing srv6 locators


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispIpv4Publication
        * Updated regex patterns and logic to handle updated device output from show command
    * Modified ShowLispIpv6Publication
        * Updated regex patterns and logic to handle updated device output from show command
    * Modified ShowLispPublicationPrefixSuperParser
        * Updated regex pattern <p1> and logic to handle updated device output from show command
    * Modified ShowLicenseSummary
        * Modified show license summary parser in order to grep all information & also to support other platform devices
    * Modified ShowTelemetryConnectionAll
        * show telemetry connection all
    * Modified ShowIpMfibSchema
        * Added optional keyword for key 'incoming_interface_list'
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * To support more varied output in the 'show bgp all neighbor {neighbor} advertised-routes' command
    * Modified ShowInterfacesTransceiverDetail
        * Value key can be string or a float to cover cases where device outputs 'N/A'
    * Modified ShowLispInstanceIdDNStatistics
        * Fixed for generic instance id
    * Modified ShowInterfacesTransceiverDetail
        * Improved handling for larger outputs
    * Modified ShowIsisRib
        * Fixed a regex to cover another cli output variation
    * Modified ShowL2vpnEvpnPeersVxlanDetail
        * Added support for UP Time in 000000 format
    * Modified ShowStormControl
        * Added support for Filter State in Link Down
    * Modified Traceroute
        * Fixed regex matching order
        * Added support for address hostname
    * Modified ShowBgpDetailSuperParser
        * Changes made for ShowIpBgpDetail to handle ext_community lists that are multiple lines
    * Modified ShowUdldInterface
        * Fixed schema and output to parse all lines of command
    * Modified ShowDmvpn
        * Change to regex to capture UNKNOWN peer
    * Modified ShowIpInterface
        * Added if statements to broadcast address logic to check for existence
        * Allows unnumbered interfaces to pass since they report a broadcast
    * Modified ShowIpBgpL2vpnEvpn
        * Fixed regex for supporting both IPv4 and IPv6 address
    * Modified ShowL2vpnEvpnMacDetail
        * Fixed regex for supporting both IPv4 and IPv6 address
    * Modified ShowL2vpnEvpnMacIpDetail
        * Fixed regex for supporting both IPv4 and IPv6 address
    * Modified ShowBgpSummarySchema
        * Modified bgp_id and local_as keys to work as either int/str types. BGP AS Notation Dot does not work with strictly type int.
    * Modified ShowBgpSummarySuperParser
        * Modified p2 match line to get local_as variable working as int or str type.
    * Modified ShowBgpAllNeighborSchema
        * Modified remote_as and local_as keys to work as either int/str types. BGP AS Notation Dot does not work with strictly type int.
    * Modified ShowBgpNeighborSuperParser
        * Modified p2_1, p2_2, p2_3 match line to get local_as variable working as int or str type.
    * Modified ShowIpRoute
        * Modified p3 regex pattern to be able to handle patterns such i*L1 without any spaces.
        * Changed names of folder unit tests to be consistent format golden_output<#>
    * Modified ShowIpv6Route
        * Modified golden_output8_expected.py to be able to handle the parser modifications over the past months. Initial was incorrect.
    * Modified ShowIpBgpL2VPNEVPN
        * Changed CLI from show ip bgp l2vpn evpn evi {evi} to show ip bgp l2vpn evpn evi {evi} detail.
    * Added ShowApStatus to support
        * show ap status
    * Modified ShowApSummary
        * Separated 'country' from 'location' in parsed output
    * Modified ShowApConfigGeneral
        * Added optional argument for AP name
    * Added ShowCapwapClientRcb to support
        * show capwap client rcb
    * Modified ShowCryptoPkiCertificateVerbose
        * Modified schema to make certain key optional.
        * Corrected counters to give the exact order of numbering
    * Modified ShowCryptoPkiCertificateVerbose
        * Modified for key error.
    * Modified ShowRomVarSchema
        * Corrected the keyword from crash to crashinfo
    * Modified ShowLispServiceSummary
        * show lisp service {service} summary,
        * show lisp {lisp_id} service {service} summary,
        * show lisp locator-table {locator-table} service {service} summary,
        * show lisp locator-table vrf {vrf} service {service} summary
    * Modified ShowRunInterface
        * Added support for Nve interfaces
    * Modified ShowMacsecSummary
        * Added support for empty response
    * Modified ShowIpEigrpTopology
        * Modified regex to support parsing EIGRP in named mode.
    * Modified ShowInterfacesDescription
        * Added two tests to check Di, Vi, Vp, pw and Ce full interface name conversion
    * Modified ShowSnmpMibIfmibIfindex
        * Modify regex pattern p1 to correctly match interfaces of the type 'unrouted VLAN <ID>'
    * Modified ShowPowerInline
        * Re-named regex pattern p1 to p1a and changed the pattern for <power> & <max> to always include ´.´,
        * Added regex pattern p1b to cover 'show power inline' output from Cat45xxR.
    * Modified ShowRunInterface
        * Removed duplicate schema variables
            * Optional('snmp_trap_link_status') bool,
            * Optional('snmp_trap_mac_notification_change_added') bool,
            * Optional('snmp_trap_mac_notification_change_removed') bool,
            * Optional('spanning_tree_bpduguard') str,
            * Optional('spanning_tree_portfast') bool,
            * Optional('spanning_tree_bpdufilter') str,
            * Optional('switchport_access_vlan') str,
            * Optional('switchport_trunk_vlans') str,
            * Optional('switchport_mode') str,
            * Optional('switchport_nonegotiate') str,
            * Optional('vrf') str,
        * Added the following schema variable
            * Optional('spanning_tree_portfast_trunk') bool,
    * Modified ShowRunInterface schema and parser
        * Added regex to parse ACLs applied to an interface.

* nxos
    * Modified ShowNveInterfaceDetail
        * Fixed handling of interface discovery when given output
    * Modified ShowBgpSessions
        * Added two new regex patterns to accommodate link local ipv6 bgp peers.
        * Added a new test case for the testing of these new patterns.

* utils
    * Modified unittests.py
        * Modified unittests.py to be able to handle older legacy parsers with the parser_command variable instead of cli_command.
    * Modified Common
        * Added Di, Vi, Vp, pw and Ce to convert list of interfaces

* asa
    * Modified ShowRoute
        * Supports tunneled routes

* iosxr
    * Modified ShowL2vpnMacLearning
        * Changed cli_command from string to list
