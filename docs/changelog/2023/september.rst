September 2023
==========

September 26 - Genie v23.9 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.9                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.9                          |
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
    * Modified Trigger/GenieStandalones/TestcaseVerificationOps
        * Fix Task discovery to be absolute, and include all objects in reporting rollup



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added
        * Class ConfigureReplace in clean stages


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added `verify_running_image` check to ``install_image`` clean stage



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
    * Added get_interface_capabilities_multiple_media_types
        * API for "get_interface_capabilities_multiple_media_types to know type of connection i.e fiber, copper and dual-port"
    * Added request platform_software_package_expand
        * API to expand package from filesystem
        * API to expand package from sub directory filesystem
    * Added configure_snmp_server_host_trap
        * API to configure snmp server host trap
    * Added configure_ipv6_dhcp_relay_trust
        * API to configure ipv6 dhcp relay trust
    * Added unconfigure_ipv6_dhcp_relay_trust
        * API to unconfigure ipv6 dhcp relay trust
    * Added configure_ipv6_dhcp_relay_option_vpn
        * API to configure ipv6 dhcp relay option vpn
    * Added unconfigure_ipv6_dhcp_relay_option_vpn
        * API to unconfigure ipv6 dhcp relay option vpn
    * Added configure_ipv6_dhcp_relay_source_interface_intf_id
        * API to configure ipv6 dhcp relay source-interface interfaceid
    * Added unconfigure_ipv6_dhcp_relay_source_interface_intf_id
        * API to unconfigure ipv6 dhcp relay source-interface interfaceid
    * Added configure_ipv6_dhcp_relay_destination_ipv6address
        * API to configure ipv6 dhcp relay destination ipv6address
    * Added unconfigure_ipv6_dhcp_relay_destination_ipv6address
        * API to unconfigure ipv6 dhcp relay destination ipv6address
    * Added configure_aaa_accounting_update_periodic_interval
        * API to configure aaa accounting update periodic {interval}
    * Added configure_ip_dhcp_snooping_information_option_allow_untrusted_global
        * API to configure ip dhcp snooping information option allow-untrusted global
    * Added unconfigure_ip_dhcp_snooping_information_option_allow_untrusted_global
        * API to unconfigure ip dhcp snooping information option allow-untrusted global
    * Added configure_management_gnmi api
        * New API to configure gnmi
    * Updated configure_management_protocol api
        * updated the logic to support the new schema
    * Added disable_cts_enforcement_vlan_list
        * API to disable CTS enforcement on vlan-list
    * Added execute_clear_ipv6_mld_group
        * New API to execute clear ipv6 mld group
    * Added execute_clear_ip_igmp_group
        * New API to execute clear ip igmp group
    * Added configure_object_list_schema_transfer_for_bulkstat
        * API to configure object list schema transfer for bulkstat
    * Added configure_bridge_domain
        * added api to configure bridge-domain
    * Added unconfigure_bridge_domain
        * added api to unconfigure bridge-domain
    * Added configure_interface_vlan
        * New API to configure interface vlan 10
    * Added configure_interface_range_no_switchport
        * New API to configure interface range no switchport
    * Added execute_clear_aaa_counters_server
    * Added configure_aaa_accounting_update
        * API to configure aaa accounting update
    * Added unconfigure_aaa_accounting_update
        * API to unconfigure aaa accounting update
    * Added unconfigure_aaa_accounting_identity_default_start_stop
        * API to unconfigure aaa accounting identity default start stop
    * Added configure_service_instance
        * added api to configure service instance
    * Added unconfigure_service_instance
        * added api to unconfigure service instance
    * Added configure_interface_ip_nbar
        * added api to configure interface ip nbar
    * Added unconfigure_interface_ip_nbar
        * added api to unconfigure interface ip nbar
    * Added execute_archive_tar
        * API to execute archive tar
    * Added api configure_breakout_cli
        * API to configure breakout
    * Added api unconfigure_breakout_cli
        * API to unconfigure breakout
    * Added configure_ip_multicast_routing_distributed
        * New API to configure ipv6 multicast routing
    * Added unconfigure_ip_multicast_routing_distributed
        * New API to unconfigure ipv6 multicast routing
    * Added clear_crypto_call_admission_stats
        * New API to clear ikev1 statistics
    * Added disable_crypto_engine_compliance
        * New API to disable crypto engine compliance shield
    * Added get_interface_media_types
        * API for "get interface media_types"
    * Added config_ip_pim_vrf_mode
        * added api to configure ip pim vrf mode
    * Added unconfig_ip_pim_vrf_mode
        * added api to unconfigure ip pim vrf mode
    * Added config_ip_multicast_routing_vrf_distributed
        * added api to configure ip multicast-routing vrf distributed
    * Added unconfig_ip_multicast_routing_vrf_distributed
        * added api to unconfigure ip multicast-routing vrf distributed
    * Added api erase startup-config
        * API to erase startup-config
    * Added  install_wcs_enable_guestshell
        * New API to  install wcs enable guestshell
    * Added execute_apphosting_cli
        * New API to execute apphosting cli
    * Added enable_usb_ssd_verify_exists
        * New API to  enable usb ssd verify exists
    * Added configure_app_management_networking
        * New API to configure app management networking
    * Added clear_ip_mfib_counters
        * New API to execute clear ip mfib counters
    * Added configure_controller_shutdown API
        * API to configure controller shutdown/no shutdown
    * Added api configure_mode_change
        * API to configure mode change

* sdk-pkg
    * Modified pysnmp to pysnmp-lextudio

* linux
    * Added generate_rsa_ssl_key
        * New API to generate an RSA key on a linux server via OpenSSL
    * Added generate_ecc_ssl_key
        * New API to generate an Elliptic Curve key with a user selected algorithm via OpenSSL
    * Added generate_ca_certificate
        * New API to generate a CA Certificate via OpenSSL
    * Added generate_ssl_certificate
        * New API to generate an SSL Certificate via OpenSSL
    * Added get_supported_elliptic_curves
        * New API to fetch supported curves on a Linux server via OpenSSL and return a list
    * Added get_file_contents
        * New API that cats out the contents of a file to a return


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* utils
    * Modified
        * Fix trigger discovery from relative Task object

* iosxe
    * Modified configure_evpn_l2_instance_vlan_association
        * added protected optional input variable
    * Modified configure_ospf_redistributed_connected
        * added vrf optional input variable
    * Modified configure_ospfv3
        * added redistribute {route_method} command
    * Modified configure_static_nat_route_map_rule
        * Added no_alias to configure static nat route-map rule with no-alias
    * Modified unconfigure_static_nat_route_map_rule
        * Added no_alias to unconfigure static nat route-map rule with no-alias
    * Modified config_extended_acl
        * added parameter port type
    * Modified
        * Modified copy_to_device to update the image path if verify_running_image is True
    * Modify configure_cdp and unconfigure_cdp
        * Added timeout for show interfaces
    * Modified configure_snmp_server_user
        * Added elif to configure snmp server user
    * Updated get_interface_interfaces_under_vrf
        * No change to API. Adjusted UT for related parser change
    * Modified configure_gdoi_group
        * added additional attributes gikev2_profile, rekey_address_acl, gikev2_client and pfs

* jinja2
    * Modified change_configuration_using_jinja_templates
        * Passing kwargs to device.configure

* general
    * Fix loading APIs under threaded environment

* genie.libs.sdk
    * Updated yang.connector and rest.connector dependencies to use correct versions.


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* sdk-pkg
    * Modified health logging



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added schema and parser for show platform software fed switch active acl info db detail
    * Added ShowPlatformSoftwareIlppowerPortSchema
        * Added parser for show platform software ilpower port {interface}
    * Added ShowPtpTimeProperty
        * parser for 'show ptp time-property'
    * Added ShowPlatformHardwareFpgaSwitch
        * Parser for show platform hardware fpga switch {switch_num}
    * Added ShowPlatformSoftwareWiredClientFpActive
        * show platform software wired-client {process} active
    * Added ShowEtherchannelSwportAuto
        * show etherchannel swport auto
    * show etherchannel swport <port_channel> auto
    * New Parser for TestVdslRawcli
        * Parser for 'test vdsl rawcli "basic show summary {number}"'
    * Added ShowNveVniDetail
        * added parser for "show nve vni <vni_id> detail"
    * Added ShowMacAddresstableDynamicVlanCount
        * Added schema and parser for ShowMacAddresstableDynamicVlanCount
    * Added show ap image
        * Added new parser for show ap image under iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveAclOgPcl Parser
        * parser for show platform software fed switch active acl og-pcl

* staros
    * Added ShowVersion
        * show version

* added showetherchannelswloadbalance
    * show etherchannel swport load-balancing

* iosxr
    * Added ShowMplsLdpInterfaceBrief
        * show mpls ldp interface brief


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified show_interface
        * Modify 'mode' as optional in p11 regex.
    * Fix for ShowBgpVrfAllNeighborsReceivedRoutes parser
        * Updated regex p3_2 for new output format.
    * Fix for ShowBgpVrfAllNeighborsRoutes parser
        * Updated regex p3_2 for new output format.
    * Modified ShowHardwareInternalTctrlUsdDpllState
        * parser for 'show hardware internal tctrl_usd dpll state'

* iosxe
    * Fixed error with TestVdslRawCli unittests
    * Modified ShowLispSiteSuperParser
        * Added additional field port to schema
        * Added split function to get port and ip on matching lines<p2> <p3_1> <p3_2>
        * Modified test files for the parsers which uses ShowLispSiteSuperParser
    * Modified ShowLoggingOnboardRpActiveTemperatureContinuous
        * Added show logging onboard rp {rp_standby} {include} continuous to support standby
    * Modified ShowLoggingOnboardRpActiveUptime
        * Added show logging onboard rp {rp_standby} uptime to support standby
    * Modified ShowLoggingOnboardRpActiveStatus
    * Modified ShowCableTdrInterface
        * Modified parser for "show cable tdr interface {inetrface}"
    * Modified ShowIsisDatabaseVerbose
        * Added support for parsing segment routing features in any order
    * Modified ShowPlatformHardwareRegisterReadAsic
        * Fixed the issue in command by changing 'register-name' to 'register'
    * Updated ShowVrf
        * Ordered elements for comparison failure
    * Updated ShowBgpAllSummary
        * Added `input_queue` and `output_queue` to exclude as dynamic value
    * Modified ShowBeaconall parser as per the output change.
        * Added power_supply_beacon_status and fantray_beacon_status in schema and in parser.
    * Modified ShowMacAddressTable Parser
        * typecast 'preferred_lifetime' and 'valid_lifetime' key int or str.
        * Made 'expires' key as optional.
        * Modified p8 regex.
    * Fix for ShowLispIpv4Publicatioin parser
        * Updated regex for new output format without locators
    * Fix for ShowLispIpv6Publicatioin parser
        * Updated regex for new output format without locators
    * Fix for ShowLispEthernetPublicatioin parser
        * Updated regex for new output format without locators
    * Modified ShowMacAddressTable Parser
        * parser for 'show mac address-table interface {interface} vlan {vlan}'
    * Added ShowEnvironmentAll
        * Made power_supply, state and system_temperature_state key optional in schema.
    * Modified ShowDerivedConfigInterfaceSchema
        * Added fields vrf, ipv4_unnumbered_intf, ipv6_unnumbered_intf, autostate into the schema.
    * Modified ShowDerivedConfigInterface
        * Added regexps for vrf, ipv4_unnumbered_intf, ipv6_unnumbered_intf, autostate.
    * Fix for ShowNveInterfaceDetail parser
        * Split tunnel interfaces line in two fields if needed
    * Fix for ShowNvePeers parser
        * Peer state regex does not include all possible state values
    * Modified ShowDeviceTrackingDatabaseInterface Parser
        * Fixed made "network_layer_address" optional in schema
    * Added ShowFileDescriptorsDetail
        * Added schema and parser for ShowFileDescriptorsDetail
    * Added ShowPlatformSoftwareFedActiveAclBindDbDetail
        * Added schema and parser for show platform software fed active acl bind db detail
    * Added ShowPlatformSoftwareFedActiveAclBindDbSummary
        * Added schema and parser for show platform software fed switch active acl bind db feature {feature_name} summary
    * Modified  ShowLicenseTechSupport
        * Modified the schema for the proxy port from str to Or(int, str)
    * Modified ShowIpAccessLists parser.
        * Modified regx. p_ip pattern.

* added show logging onboard rp {rp_standby} status to support standby
    * Modified ShowLoggingOnboardRpActiveEnvironmentContinuous
        * Added show logging onboard rp {rp_standby} environment continuous to support standby

* modified showloggingonboardswitchmessagedetail

* added show logging onboard rp {rp} message detail to support modular

* added showloggingonboardrpclilog
    * Added show logging onboard rp {rp} clilog to support modular

* iosxr
    * Fix for ShowL2vpnBridgeDomainDetail parser
        * Added flow_label_flags key in schema
    * Modified ShowL2VpnXconnectDetail
        * Modified folder name from ShowL2VpnXconnectDetail to ShowL2vpnXconnectDetail to match with class name in iosxr/show_xconnect.py
        * Added support for srv6 in cli 'show l2vpn xconnect detail' in ShowL2VpnXconnectDetail
        * Modified pattern <p14> to support 'SRv6         Local                          Remote'
        * Modified pattern <p43> to support 'Encap type Ethernet'
        * Added new pattern <p45> to support 'Ignore MTU mismatch Enabled'
        * Added new pattern <p46> to support 'Transmit MTU zero Enabled'
        * Added new pattern <p47> to support 'Reachability Up'
        * Modified folder name from ShowL2VpnXconnectMp2mpDetail to ShowL2vpnXconnectMp2mpDetail to match with class name in iosxr/show_xconnect.py
        * Modified folder name from ShowL2VpnXconnect to ShowL2vpnXconnect to match with class name in iosxr/show_xconnect.py
    * Modified ShowCefDetail
        * Modified regex <p1> to support pattern 'ffff10.0.0.1/128, version 189, SRv6 Headend, IID (EVPN-MH), internal 0x1000001 0x0 (ptr 0x8afff4a8) [3], 0x0 (0x0), 0x0 (0x8c2c70a8)'
        * Readded regex <p8> as it is not supporting pattern 'LDI Update time Oct 13 181819.691' properly in <p9> regex
        * Modified regex <p10> to support pattern 'via fc00c0001002/128, 8 dependencies, recursive, backup [flags 0x100]'
        * Modified regex <p11> to support pattern 'path-idx 0 NHID 0x0 [0x8b001f38 0x0], Internal 0x89d70af0'
        * Modified regex <p18> to support pattern '0     Y   Bundle-Ether313           fe8096aef0fffe726cda'
        * Added new regex <p21> to support pattern 'next hop VRF - 'default', table - 0xe0800000'
        * Added new regex <p22> to support pattern 'SRv6 H.Encaps.L2.Red SID-list {fc00c0001001e006}'
        * Modified schema according to the latest code and updated all unittest cases


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified Parser for ShowPppAll
        * Parser for show ppp all cli


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispV4PublicatioinPrefix
        * Added support for parsing sgt value
    * Modified ShowLispV6PublicatioinPrefix
        * Added support for parsing sgt value
    * Modified ShowLispEidTableServiceDatabase
        * Added support for parsing 'do not register', both for total count and per-prefix info
    * Modified ShowLispServiceDatabase
        * Added support for parsing 'do not register', both for total count and per-prefix info



genie.telemetry
"""""""""""""""""
