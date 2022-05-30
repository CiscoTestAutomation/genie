May 2022
==========

May 30 - Genie v22.5 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.5                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.5                          |
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

* metaparser
    * Modified parse
        * Added logic to collect the raw output of a device.execute call

* device object
    * Modified device.parse()
        * Added logic to store the raw output of show commands by calling device.parse(command, raw_data=True)

* ops
    * Modified base
        * Added argument to allow ops models to access the raw output of a parser call
    * Modified maker
        * Added argument to allow ops models to access the raw output of a parser call

* harness
    * Modified GenieScriptDiscover
        * Enabled Triggers to be extended via local packages and genielibs.cisco
        * Added helper function _get_external_triggers()


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* device object
    * Updated logic in device.parse()
        * Fixed handling timeout for device.parse()



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * tftp boot stage
        * check the length of image befor trying to boot the device. add ether_port


--------------------------------------------------------------------------------
                                      Key.                                      
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified tftp boot stage
        * edit ecovery_en_password name and add it to docstring.
    * Modified device recovery to fix grub menu logic
    * Modify image hander, upload reload service arguments with image_to_boot
    * Modified install_image stage
        * check the current image and skip the stage if the image for instalation is the

* common
    * Updated power_cycle stage, added sleep_after_connect.
    * Modified copy_to_device stage
        * to fix a bug when retrieving the running image in order to protect it from deletion
    * Modified copy_to_linux stage
        * to fix a bug for renaming the file.
    * Added prompt_recovery to copy_to_device and set the default value to False,

* clean/iosxe
    * Modified install_image stage
        * to fix the issue when packages.conf does not exist

* generic
    * Modify recovery processor, only recover device if it has been connected



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
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* robotframework
    * Removed robot framework version pinning



genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_interface_switchport API
        * API for configure interfaces on switchport
    * Added configure_ip_unnumbered_loopback API
        * API for configure ip unnumbered loopback
    * Added configure_span_monitor_session API
        * API for configure span monitor session
    * Added unconfigure_span_monitor_session API
        * API for unconfigure span monitor session
    * Added configure_stack_mac_persistent_timer API
        * API for stack_mac-persistent timer {mac_timer}
    * Added configure_stack_mac_persistent_timer API
        * API for stack_mac-persistent timer {mac_timer}
    * Added execute_diagnostic_start_switch_module_test API
        * API for diagnostic start switch {switch_num} module {mod_num} test {include}
    * Added verify_Software_Fed_Active_Ipv6_Mld_Snooping_Vlan
        * Added new api to verify value parallel to provided key in dict from the mentioned command in API
    * Added verify_Software_Fed_Igmp_Snooping
        * Added new api to verify value parallel to provided key in dict from the mentioned command in API
    * Added verify_Software_Fed_Ipv6_Mld_Snooping_Groups
        * Added new api to verify value parallel to provided key in dict from the mentioned command in API
    * Added verify_software_fed_ip_igmp_snooping_groups
        * Added new api to verify value parallel to provided key in dict from the mentioned command in API
    * Modified configure_ipsec_tunnel to add vrf option
    * Modified configure_ikev2_profile_pre_share to add vrf option
    * Added configure_mdns_active_response_timer API
        * API for configuring mDNS(Multicast Domain Name System) active response timer
    * Added unconfigure_mdns_active_response_timer API
        * API for unconfiguring mDNS(Multicast Domain Name System) active response timer
    * Added configure_mdns_service_query_timer_periodicity API
        * API for unconfiguring mDNS(Multicast Domain Name System) service query timer periodicity
    * Added clear_mdns_controller_statistics API
        * API for configuring mDNS(Multicast Domain Name System) controller statistics
    * Added configure_mdns_service_policy API
        * API for unconfiguring mDNS(Multicast Domain Name System) service policy
    * Added configure_default_mdns_controller API
        * API for configuring mDNS(Multicast Domain Name System) default mdns controller
    * Added configure_controller_policy API
        * API for configuring mDNS(Multicast Domain Name System) controller policy
    * Added unconfigure_controller_policy_service_export API
        * API for unconfiguring mDNS(Multicast Domain Name System) controller policy service export
    * Added unconfigure_mdns_service_policy API
        * API for unconfiguring mDNS(Multicast Domain Name System) service policy
    * Added unconfigure_mdns_service_policy_vlan API
        * API for unconfiguring mDNS(Multicast Domain Name System) service policy vlan
    * Added unconfigure_mdns_gateway_globally API
        * API for unconfiguring mDNS(Multicast Domain Name System) gateway globally
    * Added unconfigure_mdns_trust API
        * API for unconfiguring mDNS(Multicast Domain Name System) trust
    * Added force_unconfigure_static_nat_route_map_rule API
        * API for force unconfiguring static nat route-map rule
    * Added configure_dhcp_relay_short_lease API
        * configure configure dhcp relay short lease on router
    * Added unconfigure_dhcp_relay_short_lease API
        * unconfigure dhcp relay short lease on router
    * Added configure_ethernet_vlan_unlimited API
        * configure ethernet vlan unlimited on subslot
    * Added unconfigure_ethernet_vlan_unlimited API
        * unconfigure ethernet vlan unlimited on subslot
    * Added configure_ip_vrf_forwarding_interface API
        * configure ip vrf forwarding on interface
    * Added unconfigure_ip_vrf_forwarding_interface API
        * unconfigure ip vrf forwarding on interface
    * Added create_ip_vrf API
        * create ip vrf on router
    * Added delete_ip_vrf API
        * delete ip vrf on router
    * Added enable_dhcp_relay_information_option API
        * configure dhcp relay information option on router
    * Added disable_dhcp_relay_information_option API
        * unconfigure dhcp relay information option on router
    * Added API 'execute_diagnostic_start_module_test'
    * Added configure_hw_module_breakout API
        * configuring hw_module breakout
    * Added unconfigure_hw_module_breakout API
        * unconfiguring hw_module breakout
    * Added configure_vpdn_group API
    * Added unconfigure_vpdn_group API
    * Added configure_ip_ospf_mtu_ignore
        * Added new API for configuring ip ospf mtu-ignore
    * Added unconfigure_ip_ospf_mtu_ignore
        * Added new API for unconfiguring ip ospf mtu-ignore
    * Added Verify_ospf_icmp_ping
        * Verifying "ping <ip> df size <size>"
    * Added configure_dope_wrsp API
        * Added new API to configure WRSP parameters in dope shell
    * Added get_show_derived_interface_dict API
        * get_show_derived_interface_dict to get the IPv4 and IPv6 ACLs
    * Added clear_ip_traffic API
        * clear_ip_traffic to clear ip traffic counters
    * modified API 'configure_nve_interface'
        * Added l3vni option for nve interface
    * Added configure_switchport_trunk_vlan API
        * Configure switchport trunk vlan on Device
    * Added configure_switchport_trunk_vlan_with_speed_and_duplex API
        * Configure switchport trunk vlan on interface with speed and duplex type on Device
    * Added get_switch_qos_queue_config_on_interface API
        * Get platform hardware fed on switch and qos queue config on Interface
    * Added config_policy_map_on_device API
        * Configure policy-map type on Device
    * Added perform_telnet API
        * API to perform telnet
    * Updated execute_card_OIR API
        * API for Card OIR powercycle
    * Updated execute_card_OIR_remove API
        * API for Card OIR remove
    * Updated execute_card_OIR_insert API
        * API for Card OIR insert
    * Added verify_matm_mactable API
    * Added API for configure ipv6 static route
        * 'configure_ipv6_static_route'
    * Added API for un-configure ipv6 static route
        * 'unconfigure_ipv6_static_route'


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added API configure_local_span_source
        * added api to configure local span for source interface
    * Added API configure_local_span_destination
        * added api to configure local span to specficy destination interface
    * Added API remove_all_span
        * added api to unconfigure all span session
    * Added `verify_ptp_profile` API to verify the configured ptp profile using "show run | include ptp" command
    * Modified api 'transceiver_info'
        * changed the comments according to the function args
    * Modified `execute_write_memory` API, added dialog to handle confirm prompt
    * Modified configure_enable_nat_scale API
        * Added dialog to configure_enable_nat_scale
    * Modified configure_fnf_exporter API
        * Made few arguments as optional
    * Modified configure_fnf_record API
        * Made collect interface as Optional
    * Modified api 'verify_file_exists'
        * Api returns False if folder and/or file does not exist
    * Modified API for configure/unconfigure ipsec tunnel
        * 'configure_ipsec_tunnel'
        * 'unconfigure_ipsec_tunnel'
    * Modified API for configure ikev2 profile pre share
        * 'configure_ikev2_profile_pre_share'

* generic
    * Fix copy_to_device API filename path
    * Add support for sshtunnel host as proxy for copy_to_device and copy_from_device APIs

* all
    * Modified
        * Ignore unconnected devices in learn_system_defaults setup subsection

* ios
    * Modified `execute_write_memory` API, added dialog to handle confirm prompt
    * Modified api 'verify_file_exists'
        * Api returns False if folder and/or file does not exist

* blitz
    * gNMI subscibe ONCE and POLL not working
        * Fix thread handling for action, add poll message, fix verification.
    * Fix for gNMI subscibe and get returns validation not working for Boolean "False" and 0 values
        * Fix for xpath appending an extra '/' at the start, causing error in validation.
    * loop action
        * fixed the markup issue with range


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified clear_crypto_session API
        * clear_crypto_session to clear crypto sessions
    * Modified perform_ssh API
        * API to perform ssh



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowNhrpStats
        * show nhrp stats
    * Added ShowNhrpStatsDetail
        * show nhrp stats detail
    * Added ShowMatmMacTable
        * show platform software fed {state} matm macTable vlan {vlan}
    * Added ShowIgmpSnooping
        * show platform software fed {state} ip igmp snooping vlan {vlan}
    * Added ShowIgmpSnoopingGroups
        * show platform software fed {state} ip igmp snooping groups vlan {vlan}
    * Added ShowIpv6MldSnoopingGroups
        * show platform software fed {state} ipv6 mld snooping groups vlan {vlan}
    * Added ShowFedActiveIpv6MldSnoopingVlan
        * show platform software fed {state} ipv6 mld snooping vlan {vlan}
    * Added ShowBfdSummaryHost
        * Added new parser for cli "show bfd summary host"
    * Added ShowCryptoGdoiGm
        * Added new parser for cli "show crypto gdoi gm"
    * Added ShowCryptoIkev2SaRemoteDetail parser
        * show crypto ikev2 sa remote {ip_address} detail
    * Added ShowCryptoIkev2SaRemote parser
        * show crypto ikev2 sa remote {ip_address}
    * Added ShowCryptoSocketsInternal
        * show crypto sockets internal
    * Added ShowDmvpnCountStatus
        * added new parser for cli "show dmvpn | count Status {service}"
    * Added ShowIpNhrp
        * show ip nhrp
    * Added ShowIpNhrpDetail
        * show ip nhrp detail
    * Added ShowIpNhrpNhs
        * show ip nhrp nhs
        * show ip nhrp nhs {tunnel}
    * Added ShowIpNhrpNhsDetail
        * show ip nhrp nhs detail
        * show ip nhrp nhs {tunnel} detail
    * Adding new schema and parser in Show_platform.py
        * Added schema and parser for ShowPlatformSoftwareFedIpsecCounter
    * Added ShowU2MSR
        * show plshow platform hardware qfp active feature uni-sr
    * Added ShowPowerInlineDetail
        * show power inline {interface} detail
    * Added ShowPowerInlinePolice
        * show power inline police
        * show power inline police {interface}
    * Added 'ShowRunIncludePtp' schema and parser
        * show run | include ptp
    * Added ShowSdwanAppHostingOperData
        * for 'show sdwan app-hosting oper-data'
    * Added ShowUtdEngineStandardStatistics
        * show utd engine standard statistics
    * Added ShowUtdEngineStandardStatisticsDaqAll
        * show utd engine standard statistics daq all
    * Added ShowModule
        * show module
    * Added ShowRedundancyRpr
        * show redundancy rpr
    * Added subclass ShowLispInstanceIdEthernetMapCacheRAR and ShowLispInstanceIdEthernetMapCachePrefixRAR for parsing Map-Cache RAR and Map-Cache RAR prefix inheriting from Superparsers
    * Modified superparser ShowLispMapCacheSuperParser and ShowLispIpMapCachePrefixSuperParser
    * Added ShowPlatformHardwareVoltageMarginSwitch
        * show platform hardware voltage margin switch {mode} rp active
    * Modified the ShowLogging
        * Fix for local variable referenced before assignment
    * Added ShowIpv6NhrpSummary
        * added new parser for cli "show ipv6 nhrp summary"
    * Added parsers for the following show commands
        * ShowLispInstanceServerRAR
            * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution parser
            * show lisp instance-id {instance_id} ethernet server reverse-address-resolution
        * ShowLispInstanceServerRARDetail
            * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution detail
            * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution {mac}
            * show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail
            * show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail {mac}
    * Added ShowDerivedConfigInterface
        * Added show derived-config interface <>  parser
    * Added ShowMemoryDebugLeaksChunks parser
        * Parser for 'show memory debug leaks chunks' command
    * Added ShowIpNhrpStats
        * show ip nhrp stats
        * show ip nhrp stats {tunnel}
    * Added ShowIpNhrpStatsDetail
        * show ip nhrp stats detail
        * show ip nhrp stats {tunnel} detail

* iosxr
    * Added show vrrp commads
        * Show vrrp detail
        * show vrrp statistics
        * show vrrp summary
    * Adding new schema and parser in Show_lldp.py
        * Added schema and parser for ShowLldpNeighborsInterfaceIdDetail
    * Added Showhsrpbfd
        * show hsrp bfd
        * show hsrp bfd {interface}
        * show hsrp bfd {interface} {destination_ip}
    * Modified ShowHsrpDetail
        * show hsrp {address_family} {interface} {group_number} detail
    * Added ShowHsrpStatistics
        * show hsrp statistics
        * show hsrp {interface} statistics
        * show hsrp {interface} {group_number} statistics
    * Added ShowHsrpStatus
        * show hsrp status


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpOspfInterface
        * Changed regex pattern <p2> to cover the case where Interface is unnumbered
    * Modified ShowIpOspfInterface2
        * Changed regex pattern <p2> to cover the case where Interface is unnumbered
        * Change <cmd> to <cli_command> so that the class ShowIpOspfInterface2 is reached
        * Update json file for the class ShowIpOspfInterface2
        * Create folder-based testing files
    * Modified ShowPowerInlinePriority
        * Added optional power_inline_auto_shutdown for 9400 Platform.
        * Updated regex pattern <p1a> <p2> for 9400 Platform.
        * Converted the interface name to use long name to align with other POE parsers.
    * Modified ShowPowerInlineUpoePlus
        * Updated regex pattern <p1> to match 'n/a' for type.
    * Modified ShowPowerInlineUpoePlusModule
        * Changed ieee_mode to optional.
        * Added regex pattern <p1a> for 9400 Platform.
        * Converted the interface name to use long name to align with other POE parsers.
    * Modified ShowVersion
        * Updated regex to parse build information
    * Fixed an error in show lisp instance-id <> ethernet server reverse-address-resolution mac <> command.
    * Modified ShowCryptoIkev2StatsExchange
        * Added key Any to schema, to take into account variations in output.
        * Updated regex to take into consideration, spaces in output.
        * Updated ShowCryptoIkev2StatsExchange class with respect to change in schema.
    * Modified ShowDmvpnCountStatus
        * Updated parser class to incorporate IPv6 variant.
    * Modified ShowIpMroute
        * Changed the code to handle multiple interface of different name to escape suffix appending
    * Modified ShowIpNhrpStats
        * Added code for "show nhrp stats",'show ipv6 nhrp stats','show nhrp stats {tunnel}','show ipv6 nhrp stats {tunnel}' CLI commands
        * Updated ShowIpNhrpStats class with respect to addition of commands included.
    * Modified ShowMdnsSdSummary
        * Updated regex to verify entire output
    * Modified ShowLispEidWatch
    * Modified ShowLispIpMapCachePrefixSuperParser
    * Modified ShowLispDatabaseEid
    * Modified ShowLispSiteDetailSuperParser
    * Modified ShowLispMapCacheSuperParser
    * Modified ShowLispIpv4PublisherRloc
    * Modified ShowLispIpv4PublisherRlocSchema
    * Modified ShowLispService
    * Modified ShowLispPublicationPrefixSchema
    * No backward compatible
    * Modified ShowLispEthernetMapCachePrefix
    * Modified ShowLispSiteDetailSuperParser
    * No backward compatible
    * Modified ShowLispMapCacheSuperParser
        * Changed "metric" in Schema to accept int and None
        * Changed regex for "metric" to accept '-' along with integers
    * Modified ShowTelemetryIETFSubscription/ShowTelemetryIETFSubscriptionDetail
        * added keywords "all", "configured", "dynamic", "permanent", "brief" to list of supported CLIs
    * Modified ShowMdnsSdSummary
        * Updated regex to verify latest release output
    * Modified ShowPlatformNatTranslations
        * Modify the regular expression to accept any number of digits
    * Modified ShowIsisDatabaseVerbose
        * Non-backwards compatible change Removed the segment routing key from the flex algo sub dictionary as it does not belong in that location
    * Modified ShowIsisDatabaseVerbose
        * Added new keys for uni link loss and appl spec uni link loss in the show isis database parser
    * Modified ShowRunInterface
        * Updated in schema "cdp enable" optional in the output
    * Modified ShowIpNhrpTrafficDetail
        * Added new argument to support ipv6.
    * Modified ShowIpNhrpTraffic
        * Added new argument to support ipv6
    * Modified ShowPost
        * Modified ShowPost parser and schema to fetch details of two devices.
    * Modified ShowPlatformIfmMapping
        * Removed the int data type from optional variables ifg_id, first_serdes, last_serdes
    * Modified ShowInventory
        * Added two more interfaces in if condition.
    * Modified ShowLicenseTechSupport
        * Added optional key <smartagenttelemetryrumreportmax> to schema.
        * Added optional key <smartagentrumtelemetryrumstoremin> to schema.
    * Modified ShowTcpProxyStatistics
        * Added optional key dre_bypass_received_from_peer to schema
        * Added optional key dre_bypass_hints_sent to schema
        * Added optional key dre_smb_bypass_success_received to schema
        * Added optional key dre_http_bypass_success_received to schema
    * Modified ShowIpMroute
        * Added keys iif_lisp_rloc, iif_lisp_group under incoming_interface_list
        * Added keys extranet_vrf and {e_src,e_grp,e_uptime,e_expire,e_oif_count,e_flags} under newly created extranet_rx_vrf_list
        * Modified incoming_interface_list regex to include parsing of the two above mentioned additional keys
    * Modified ShowSystemIntegrityAllMeasurementNonce
        * Modified the regex pattern of p5 to support smu package
    * Modified ShowPlatformTcamPbrNat
        * Modified ShowPlatformTcamPbrNat cli_command to run on SVL and HA setup

* nxos
    * Modified RunBashTop
        * Modified regex pattern in Cpu, Mib mem and swap for fixing missing key error.
        * For <p4_1>, <p5_1> and <p6> added conversion to support k to Mib and m to Mib

* utils
    * common
        * Removed duplicated key Two
    * common
        * Added new keys Fif, Fifty, Two, TwoH

* updated argument.json class to include changes for ipv6.

* added golden_output_arguments.json file

* iosxr
    * modified ShowPimVrfInterfaceDetail
        * Updated regex pattern p9 and p10 to accommodate for optional output "(config  xx)" for Propagation delay and Override Interval
    * Modified ShowLldpTrafficInterfaceId
        * Added last_clear in a schema.
    * Modified ShowVrrpDetail
        * Updated regex pattern <p20> to accommodate master_name and number_of_slave.
        * Updated regex pattern <p21> to accommodate slave_to
        * Updated regex pattern <p22> to accommodate authentication_string
        * Updated regex pattern <p23> to accommodate master_router_ip and master_router_priority


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Updated ShowCryptoIkev2Session
        * Modified show crypto ikev2 session parser for the latest output change in 17.9


