January 2024
==========

30 - Genie v24.1 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 24.1                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 24.1                          |
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

* common
    * Updated pyats configuration import



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified copy_to_device clean stage, update logic for image mapping when image is already loaded


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* cheetah
    * Added LoadApImage
        * Added new clean stage load_ap_image

* stages/iosxe
    * Updated connect stage to support rommon boot

* iosxe
    * Added configure_type_access_list_action
        * API to configure ip/mac access-list with permission



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* hltapi
    * Modified traffic_control API to handle calls without mode argument

* nxos
    * macsec
        * added new command 'ppk crypto-qkd-profile' under macsec policy config


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added crypto conf
        * added crypto qkd cli for conf model



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Updated pyats configuration import



genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Updated pyats configuration import



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
    * Removed remove_routing_ip_route
    * Modified configure_pppoe_enable_interface
        * modified api to configure ppp-max-payload
    * Modified unconfigure_pppoe_enable_interface
        * modified api to unconfigure ppp-max-payload
    * Modified get_firmware_version to handle stack switches
    * Modified unconfigure_app_hosting_appid
        * Added 'appid' argument
    * Modified configure_fnf_flow_record
        * added new fields

* iosxr
    * Modified FileUtils

* sdk-pkg
    * iosxe
        * Fix the copy_file_with_scp api mock data


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_mdns_remote_purge_timer
        * API to configure enable configure mdns remote purge timer
    * Added unconfigure_mdns_remote_purge_timer
        * API to unconfigure mdns remote purge timer
    * Added unconfigure_mdns_global_service_buffer
        * API to unconfigure mdns global service buffer
    * Added clear_mdns_cache_remote
        * API to clear mdns cache remote
    * Added configure_mdns_remote_cache_enable
        * API to configure mdns remote cache enable
    * Added unconfigure_mdns_remote_cache_enable
        * API to unconfigure mdns remote cache enable
    * Added configure_mdns_remote_cache_max_limit
        * API to configure mdns remote cache max limit
    * Added unconfigure_mdns_remote_cache_max_limit
        * API to unconfigure mdns remote cache max limit
    * Added configure_mdns_global_service_buffer
        * API to configure mdns global service buffer
    * Added configure_ip_on_atm_interface
        * added api to configure_ip_on_atm_interface
    * Added unconfigure_ip_on_atm_interface
        * added api to unconfigure_ip_on_atm_interface
    * Added get_module api
    * Added hw_module_beacon_rp_toggle
        * API to turn beacon on/off for RP and R1
    * Added hw_module_beacon_rp_status
        * API to fetch beacon status for RP and R1
    * Added hw_module_beacon_slot_status
        * API to fetch beacon status for slot
    * Added hw_module_beacon_rp_active_standby_status
        * API to fetch status of the beacon for active/standby RP
    * Added clear_lacp_counters
        * added api to clear_lacp_counters
    * Added clear_active_punt_ios_cause
        * added api to clear_active_punt_ios_cause
    * Modified configure_interface_switchport_access_vlan
        * Modified the configure_interface_switchport_access_vlan API interface to swichport
    * Added configure_hw_module_switch_number_ecomode_led
        * hw-module switch number ecomode led
    * Added unconfigure_hw_module_switch_number_ecomode_led
        * no hw-module switch number ecomode led
    * Modified copy_file_with_scp
    * Modified copy_file_with_sftp

* cheetah
    * Added execute_archive_download
        * Added new API execute_archive_download


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_virtual_template
        * modified api to configure ipv6_pool_name
    * Modified configure_bba_group
        * modified api to configure tag ppp-max-payload
    * Modified configure_device_classifier_command
        * added optional timeout value
    * Modified configure_device_classifier
        * added optional timeout value


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added API clear_ip_dhcp_snooping_statistics
        * API added to clear ip dhcp snooping statistics



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * Updated regex pattern <p3_1> to accommodate various outputs.
    * Modified ShowClnsIsNeighborsDetail
        * Updated regex pattern <p2> to accommodate various outputs.
    * Modified ShowInterfaces
        * Added regex pattern <p53> to capture value of carrier transitions
    * Modified ShowPlatformSoftwareFedSwitchActiveVpSummaryVlan Parser
        * Fixed parser to execute show comman on svl, HA and SA devices
    * Modified ShowEnvironment Parser
        * Modified the p4 regex pattern to capture missing data.
    * Modified ShowRunningConfigNve
        * Fixed regex <p2> and <p3> to accomodate various values and to fix MAC value regex.
        * Changed key <serial> in schema to optional
    * Modified ShowRunningConfigNve
        * Added regex <p5_4> and <p5_5>.
        * Update code for <p3_8> to include space between 'ipv4' and 'mask' key.
    * Modify ShowPlatformSoftwareDistributedIpsecTunnelInfo
        * Updated parser to validate per tunnel info
    * Modified ShowIpNhrpNhsDetail Parser
        * parser for 'show ip nhrp nhs {tunnel} detail' Modified schema and regex pattern
    * Fix for ShowSpanningTreeInterface
        * Modified regular expression in order to satisfy P2p Peer (STP)
    * Modified parser ShowHardwareLed
        * Enhanced the parser to get LED Ecomode status, Added schema and regex pattern <p12_1>
    * Modified parser ShowProcessesCpuSorted
        * Fixed schema and regex pattern
    * Fix for ShowEnvironmentSuperParser
        * added p1_3 match pattern
    * Modified ShowIpMfib
        * To support interface port-channel type in iif and oif
        * Additional handling for egress_data
        * Sample output for iif  Port-channel5 Flags RA A MA
        * Sample output for oif  Port-channel5 Flags RF F NS
    * Modified ShowIpv6Mfib
        * To support interface port-channel type in iif and oif
        * Additional handling for egress_data
        * Sample output for iif  Port-channel5 Flags RA A MA
        * Sample output for oif  Port-channel5 Flags RF F NS
    * Modified ShowLispEthernetMapCachePrefix Parser
        * Made prefix-location optional
    * Added
        * Added condition for channel_group in pagp_dad_obj
    * Fixed ShowControllerVDSLSchema parser
        * Fixed schema for 'modem_fw__version' & 'modem_phy_version' for show controller vdsl {slot_no}
    * Modified ShowEtherchannelProtocol
        * Fix P1_1 regular expression.
    * Adding parser for ShowIpOspfRibRoute
        * Added ShowIpOspfRibRoute for "show ip ospf rib <>"
    * Modified ShowIpv6RouteWord
        * Added support for parsing output with LISP interfaces
    * Modified ShowRunningConfigNve
        * Added regex <p5_6> and <p5_7> for keys 'data_mdt_group', 'data_mdt_group_mask' and 'data_mdt_threshold'
    * Modified ShowMplsForwardingTable
        * Added bytes_label_switched to exclude

* nxos
    * Fix for ShowRunningConfigInterface
        * Added p20 regex to match the user's data.
    * Modified ShowRunningConfigBgp
        * Updated code for <p32> to match the list of values.
    * Modified ShowInterfaceStatus
        * Refactored regex pattern to accommodate modern outputs from Nexus 9000 series and be easier to maintain overall.
    * Added
        * Updated regex pattern for <p31>
    * Modified ShowRunningConfigInterface
        * Modified schema to store secondary ip address
        * Improved p17 regex to capture proper ip address
        * Added p21 regex to capture secondary ip address

* iosxr
    * Modified ShowBgpL2vpnEvpnSummary Parser
        * Added regex p8a and p8b
        * Added code in pattern <p8a> and <p8b>
    * Modified ShowIsisDatabaseDetail
        * Added pattern <r26> to parse line 'Metric 10         MT (IPv6 Unicast) IPv6-Ext-InAr fc00a00020003/128'
        * Modified pattern <r25> code to parse multiple srv6 locator lines
    * Modified ShowOspfNeighbor
        * Modified schema and code to store multiple neighbor values into a list
    * Modified ShowL2vpnBridgeDomainDetail
        * Modified schema and existing code to have separate entry for access pw
        * Modified regex p27 to fix mismatch pw_class and xc_id value
    * Modified ShowBgpVrfAfPrefix Parser
        * Added code in pattern <p11>
        * Added keys <group_best, backup, add_path, import_candidate, imported, redistributed> in schema as optional parameters
        * Modified 'r_value' key as optional parameter

* viptela
    * Modified ShowOmpRoutes
        * Added tenant key as option.
        * Updated regex pattern p1 and p2 to accommodate various outputs.

* iosxe/c9600/c9606r
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Added command for switch mode standby
    * Modified ShowPlatformTcamPbrNat
        * Added command for switch mode active

* common
    * Updated pyats configuration import
    * Modified .gitignore
        * Added the `venv/` directory to the .gitignore file. Common convention dictates that Python virtual environments are stored in a directory named `venv`, which should not be committed to a repository.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* ios
    * Added ShowVlanInternalUsage
        * show vlan internal usage

* iosxe
    * Added ShowPlatformSoftwareMatmSwitchTable
        * Parser for cli 'show platform software matm switch {switch} {slot} table'
    * Added ShowIsisNeighborSuperParser
        * Added super parser for show isis neighbor and schema
        * Added parser for show isis neighbor and show isis neighbor detail
    * Added ShowMdnsSdCache
        * parser for 'show mdns-sd cache remote'
    * Added ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsite
        * show platform software memory database fed {switch} {switch_var} callsite
    * Added ShowIPNameServer Parser in show_ip.py
        * show ip name-servers
            * show ip name-servers vrf {vrf}
    * Added ShowPlatformSoftwareFedSwitchActiveNatAcl
        * Parser for cli 'show platform software fed switch active nat acl'
    * Added ShowPlatformSoftwareFedSwitchActiveNatFlows
        * Parser for cli 'show platform software fed switch active nat flows'
    * Added ShowPlatformSoftwareFedSwitchActivePuntBrief
        * Parser for cli 'show platform software fed switch active punt ios-cause brief'
    * Added ShowIsisIpv6RibParser
        * Added parser for show isis ipv6 rib and schema
    * Added ShowDiagnosticStatus
        * Added parser for show diagnostic status
    * Added ShowL2routeEvpnEs
        * show l2route evpn es
        * show l2route evpn es esi {esi}
        * show l2route evpn es origin-rtr {origin_rtr}
        * show l2route evpn es origin-rtr {origin_rtr} esi {esi}
        * show l2route evpn es producer {producer}
        * show l2route evpn es producer {producer} origin-rtr {origin_rtr}
        * show l2route evpn es producer {producer} origin-rtr {origin_rtr} esi {esi}

* iosxr
    * Added ShowBgpL2vpnEvpnSummary
        * Added parser for show bgp l2vpn evpn summary
    * Added ShowBgpAddressFamily
        * Added parser for show bgp
        * Added parser for show bgp {address_family}
    * Modified ShowBgpInstanceSummary
        * Modified pattern <p11> to parse both lines 'Table ID 0x0' and 'Table ID 0x0   RD version 0'
        * Modified pattern <p15> to parse line 'BGP scan interval 60 secs'

* generic
    * Show version
        * Added support for cheetah/ap


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowTerminal Parser



genie.telemetry
"""""""""""""""""
