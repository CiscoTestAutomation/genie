July 2024
==========

July 30 - Genie v24.7 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 24.7                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 24.7                          |
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

* conf/base
    * api
        * Updated warning with exception message when the api json file is missing on first load.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* utils
    * Enhanced Dq
        * Added `condition_key_value` argument to get_values method to allow for filtering of values based on a key value pair.

* abstract
    * Modified AbstractPackage
        * Fixed an issue where root level modules were not being discovered



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified
        * Added prompt-level none to image install command


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Recovery
        * Refactored Recovery logic to use send_break_boot api.
    * Reload
        * Updated logic todo Reload when the boot variable is not set.
    * Modified InstallRemoveInactive
        * Added new parameter force_remove to remove inactive package forcefully
    * Added dialog
    * api
        * Added condition for golden image



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added
        * Urpf config model
    * Added configuration support for nxos evpn multihoming by adding below commands
        * evpn multihoming
            * df-election mode modulo
            * df-election mode per-flow
            * ethernet-segment delay-restore time 45
            * system-mac aaaa.deaf.beef
        * interface
            * evpn multihoming core-tracking
            * ethernet-segment
                * esi system-mac <system-mac> <local_discriminator>
                * esi system-mac <local_discriminator>
                * esi <esi_tag>
    * Added interface level configuration CLI support for vpc, for following commands
        * port-type fabric
        * vpc peer-link
        * vpc <vpc-id>



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* fileutils
    * Modified  FileUtils
        * Updated logic to use hostname if not able to resolve to IP address



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* sonic
    * platform
        * Added ops support for sonic platforms
    * interface
        * Added ops support for sonic interface



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Add API configure_breakout_cli
        * Added the timeout for the Proc
    * Add API unconfigure_breakout_cli
        * Added the timeout for the Proc
    * Add API configure_mode_change
        * Added the timeout for the Proc
    * Added API config_qinq_encapsulation_on_interface
        * This API configures dot1q encapsulation on an interface with double tagging (Q-in-Q).
        * Takes device, interface, VLAN, and second VLAN as arguments.
        * Applies the encapsulation configuration to the specified interface.
        * Raises SubCommandFailure in case of errors during the configuration.
    * Added configure_sub_interface_range
        * API for configure the sub interface range
    * Added configure_interface_range_switchport_mode
        * API for configure the interface range switchport mode
    * Added shutdown_sub_interface_range
        * API for shutdown the subinterface range
    * Added shutdown_interface_range
        * API for shutdown the interface range
    * Added no_shut_interface_range
        * API for un shut the interface range
    * Added no_shut_sub_interface_range
        * API for un shut the subinterface range
    * Added configure_sub_interface_encapsulation_dot1q
        * API for configure_sub_interface_encapsulation_dot1q
    * Added configure_ip_ssh_client_algorithm_mac
    * Added configure_ip_ssh_client_algorithm_kex
    * Added configure_ip_ssh_client_algorithm_encryption
    * c8000v
        * Added configure_autoboot API
    * Added configure_datalink_flow_monitor
        * New API to configure datalink flow monitor
    * Added unconfigure_datalink_flow_monitor
        * New API to unconfigure datalink flow monitor
    * Added configure_ipv6_nd_cache_expire
        * New API to configure ipv6 nd cache expire {timeout}
    * Added unconfigure_ipv6_nd_cache_expire
        * New API to unconfigure ipv6 nd cache expire
    * Added configure_policy_map_class
        * API to configure policy map class
    * Added configure_interface_span_portfast
        * API to configure interface portfast
    * Added execute_issu_set_rollback_timer API
        * Added API for execute_issu_set_rollback_timer
    * Added unconfigure_issu_set_rollback_timer API
        * Added API for unconfigure_issu_set_rollback_timer
    * Added API test_platform_software_usb_fake_insert_remove
        * Added API to test_platform_software_usb_fake_insert_remove
    * Added API configure_aaa_authentication_enable_default_group_enable
        * Added API to configure_aaa_authentication_enable_default_group_enable
    * Added API configure_aaa_authentication_login_default_group_local
        * Added API to configure_aaa_authentication_login_default_group_local
    * Added API configure_aaa_authorization_exec_default_group_if_authenticated
        * Added API to configure_aaa_authorization_exec_default_group_if_authenticated
    * Added API configure_aaa_authorization_network_default_group
        * Added API to configure_aaa_authorization_network_default_group
    * aaa
        * configure
            * configure_aaa_accounting_network_default_start_stop_group
                * Args
            * unconfigure_aaa_accounting_network_default_start_stop_group
                * Args
            * configure_aaa_accounting_identity_default_start_stop_group
                * Args
            * unconfigure_mab_on_switchport_mode_access_interface
                * Args
            * configure_mab_eap_on_switchport_mode_access_interface
                * Args
    * Added monitor_event_trace_dmvpn_nhrp_enable
        * API for monitor event trace dmvpn nhrp enable
    * Added monitor_event_trace_dmvpn_nhrp_clear
        * API for monitor event trace dmvpn nhrp clear
    * Added configure_phymode_ignore_linkup_fault
    * Added unconfigure_phymode_ignore_linkup_fault
    * Added configure_system_debounce_link_up_timer
    * Added configure_system_debounce_link_down_timer
    * Added unconfigure_system_debounce_link_up_timer
    * Added unconfigure_system_debounce_link_down_timer
    * Added configure_default_spanning_tree_vlan
        * API to configure default spanning tree vlan.
    * Added configure_ip_ssh_server_algorithm_mac
    * Added configure_ip_ssh_server_algorithm_kex
    * Added configure_ip_ssh_server_algorithm_encryption
    * Added configure_ip_ssh_server_algorithm_hostkey
    * Added new API get_boot_variables for IE3K devices
        * get_boot_variables - Get boot variables for IE3K devices

* util
    * Added configure_peripheral_terminal_server
        * API for configure speed for line of terminal server in the testbed
    * Added configure_terminal_lines_speed
        * API for configure speed of a line

* utils
    * Added configure_management_console api
        * New api for configuring speed on console

* apis
    * iosxe/asr1k
        * Added new api configure_boot_manual.
    * iosxe
        * cat9k
            * utils
                * Added new api password_recovery.
            * configure
                * Added new api configure_ignore_startup_config.
                * Added new api unconfigure_ignore_startup_config.
            * verify
                * Added new api verify_ignore_startup_config.
        * rommon/utils
            * Added new api send_break_boot.

* sdk-pkg
    * update `pysnmp-lextudio==6.1.2` to avoid deprecation issues


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated API get_boot_variables
        * Handled a scenario were current/next boot variable not found in parser output
    * Fixed enable_usb_ssd_verify_exists
        * command provided is incorrect. Fixed the show command to display the correct output.
    * Fixed install_wcs_enable_guestshell
        * API call is incorrect. Fixed the API call to enable the guestshell.
    * Fixed save_device_information
        * Added try except block to handle the exception since the configureation is no more applicable to latest iosxe

* nxos
    * Added virtual peer link attributes in vPC Domain
        * virtual_peer_link_dst_ip = '2.2.2.2'
        * virtual_peer_link_src_ip = '2.2.2.1'
        * virtual_peer_link_dscp = 56

* sdk
    * verifcation
        * Updated verifcation file to address moved parsers

* apis
    * Modified `verify_is_syncing_done` API
        * Renamed API to verify_yang_is_syncing_done, deprecate `verify_is_syncing_done`
        * Added namespace



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIpRouteDetail
        * Added Show Platform Software Fed Switch Active IpRoute Detail
    * Added ShowPlatformSoftwareFedActiveMatmMacTableVlanMacDetail
        * Added 'show platform software fed {switch} {mode} matm macTable vlan {vlan_id} mac {dynamic_mac} detail'
    * Added ShowNetworkClocksSynchronizationDetail
        * Added schema and parser for show network-clocks synchronization detail
    * Added ShowNetworkClocksSynchronization
        * Added schema and parser for show network-clocks synchronization
    * Added ShowNetworkClocksSynchronizationGlobalDetail
        * Added schema and parser for show network-clocks synchronization global detail
    * Added ShowNetworkClocksSynchronizationGlobal
        * Added schema and parser for show network-clocks synchronization global
    * Added ShowNetworkClocksSynchronizationInterface
        * Added schema and parser for show network-clocks synchronization interface {interface}
    * Added ShowNetworkClocksSynchronizationT0Detail
        * Added schema and parser for show network-clocks synchronization t0 detail
    * Added ShowNetworkClocksSynchronizationT0
        * Added schema and parser for show network-clocks synchronization t0
    * Added ShowESMCDetail
        * Added schema and parser for show esmc detail
    * Added ShowESMC
        * Added schema and parser for show esmc
    * Added ShowESMCInterfaceDetail
        * Added schema and parser for show esmc interface {interface} detail
    * Added ShowESMCInterface
        * Added schema and parser for show esmc interface {interface}
    * Added ShowHardwareLed
        * Added schema and parser for 'show hardware led' under c9600
    * Added HardwareModuleBeaconFanTrayStatus
        * Added schema and parser for 'hw-module beacon fan-tray status'
    * Added HardwareModuleBeaconSlotStatus
        * Added schema and parser for 'hw-module beacon slot {slot_num} status'
    * Added ShowPlatformSoftwareFedSwitchActivePuntPacketcaptureStatus
        * Added schema and parser for 'show platform software fed switch active punt packet-capture status'
    * Added ShowPlatformSoftwareFedIgmpSnoopingGroupsCount
        * Added 'show Platform Software fed ip igmp snooping groups count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpMfibCount
        * Added 'show platform software fed switch active ip mfib count' command and schema for the command.
    * Added ShowPlatformSoftwareFedIpMfibSummary
        * Added 'show platform software fed switch active ip mfib summary' command and schema for the command.
    * Added ShowIpIgmpSnoopingGroupsVlanGroup
        * Added 'show ip igmp snooping groups vlan {vlan} {group}' command and schema for the command.
    * Added ShowPlatformSoftwareFedSwitchActiveIpAdj
        * Added schema and parser for 'show platform software fed switch active ip adj'
    * Added ShowPlatformSoftwareFedSwitchActiveIpRoute
        * Added schema and parser for 'show platform software fed switch active ip route'
    * Added ShowPlatformSoftwareMountSwitchActiveRpTmpfs
        * Added schema and parser for 'show platform software mount switch active rp active | include {tmpfs}'
    * Added ShownMonitorEventTraceDmvpnAll
        * Added schema and parser for show monitor event-trace dmvpn all
    * cat9k
        * c9500
            * show_platform_software_fed_switch_active_punt_packet_capture_display_filter_key_brief.py
                * ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterKeyBrief


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowL2vpnEvpnMacIpDetail
        * Added '(' ')' characters to regrex for next-hop
    * Modified ShowL2vpnEvpnEviDetail
        * parser for 'show l2vpn evpn evi {evi} detail'
    * Modified ShowMonitorCaptureBufferDetailed
        * Added revised version 1 for ShowMonitorCaptureBufferDetailed parser
        * Added <p9>, <p10>, <p11>, <p12> and <p13> to accommodate various outputs
    * Modified ShowIsisNodeLocators
        * added support for new cli show isis node locators
    * Modified ShowIsisNodeLocatorsSchema
        * added schema for new cli show isis node locators
    * Modified fix for ShowInterfaces
        * Modified the Regex pattern p<11> to accomodate various outputs
    * Modified fix for ShowMplsTrafficEngTunnelTunnelid
        * Added the frr_outlabel key to the schema and modified the regex patterns p<1> and p<3> to accommodate various outputs
    * Modified ShowLicenseAll Parser
        * Made miscellaneous, policy, and usage_reporting optional
        * Made smart_licensing_status non-optional as some of its members are not optional
    * Modified ShowLicenseStatus Parser
        * removed matching for <none> in parsing trust_code_installed as it is not specific enough
    * Modified ShowLldpNeighborsInterfaceDetail Parser
        * Made media_attachment_unit_type optional
    * Modified ShowPlatformSoftwareFedSwitchActivEAclUsage Parser
        * Added switch_num variable to the show command
    * Modified ShowPlatformSoftwareFedSwitchActiveStpVlan
        * Added switch variable to the command
    * Added ShowIpDhcpSnoopingBinding
        * Make {interfaces} key as Optional to handle the key error
    * Modified init file in c9350
        * Updated model token
    * cat9k
        * 9300
            * Modified ShowPlatformHardwareAuthenticationStatus
                * Added support for RoT
            * Modified ShowEnvironmentAll
                * Modified to support more than 2 PSs in a switch
    * Modified ShowLispInstanceIdService
        * Fixed incorrect regex for Publisher(s)
    * Modified ShowLispInstanceIdService
        * Added support for parsing publisher addresses without ETR Map-Servers
    * Modified ShowMkaStatistics
        * Changed tx-sc-creation key in schema from `0` to `int`.
    * Modified ShowLoggingOnboardRpClilog parser
        * Modified ShowLoggingOnboardRpClilog parser
    * Modified ShowLoggingOnboardRpActiveStatus parser
        * Modified ShowLoggingOnboardRpActiveStatus parser
    * Modified ShowLoggingOnboardRpActiveTemperatureContinuous parser
        * Modified ShowLoggingOnboardRpActiveTemperatureContinuous parser
    * Modified ShowLoggingOnboardRpActiveTemperature parser
        * Modified ShowLoggingOnboardRpActiveTemperature parser
    * Modified ShowIsisIpv6Rib
        * added support for new cli show isis ipv6 rib flex-algo {flex_id} {prefix}
        * added new key flex_algo under tag key
        * added new key src_rtr_id under prefix key
        * added new key pfx_algo under prefix key
    * Modified ShowIsisIpv6RibSchema
        * added new optional keys flex_algo,src_rtr_id,pfx_algo
    * Modified ShowLispSiteSummarySchema
        * made configured_registered_prefixes.ipv6 optional
    * Modified ShowLispPlatformSchema
        * made make remote_eid_idle and mapping_cache_full optional optional
    * MOdified ShowHardwareLedPortMode parser
        * Modified current_mode & status parameters in schema as Optional
    * Modified ShowWatchdogMemoryState parser
        * Adjusted to missing spaces in CLI output
        * Do not fail parser if there is no node location appearing in output
    * Modified ShowVrf
        * updated schema to support additional `route_distinguisher_auto`
    * Modified cat9k/c9800/ewc_ap
        * Changed parameter pid to submodel in __init__.py file.
    * Modified cat9k/c9600/c9606r
        * Changed parameter pid to submodel in __init__.py file.

* iosxr
    * Modified ShowPceIPV4PeerDetail
        * Modified schema and adding optional to the keys
    * Modified ShowRouteIpv6
        * Modified parer and defined outgoing dict
    * Modified ShowOspfVrfAllInclusive
        * Added <current_lsa>, <threshold>, <ignore_time>, <reset_time>, <allowed_ignore_count>, <current_ignore_count>, <max_external_prefix>, <warning_threshold> keys to schema.
    * Modified ShowPlatform
        * Updated regex pattern p1 to allow for both IN-RESET and SW_INACTIVE as valid states.

* staros
    * Modified init file
        * Updated os token

* sonic
    * Modified init file
        * Updated os token

* rdp
    * Modified init file
        * Updated os token

* various
    * Split large parser files (>10000 lines) into smaller files


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareModuleInterfaceStatus
        * Added support for command "show platform hardware subslot {id} module interface {intf} status"



genie.telemetry
"""""""""""""""""
