April 2025
==========

April 29 - Genie v25.4 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.4 
    ``genie.libs.health``, v25.4 
    ``genie.libs.clean``, v25.4 
    ``genie.libs.conf``, v25.4 
    ``genie.libs.filetransferutils``, v25.4 
    ``genie.libs.ops``, v25.4 
    ``genie.libs.parser``, v25.4 
    ``genie.libs.robot``, v25.4 
    ``genie.libs.sdk``, v25.4 
    ``genie.telemetry``, v25.4 
    ``genie.trafficgen``, v25.4 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* abstract
    * Fixed issue where custom package order was being ignored

* device
    * Modified test_device
        * Updated the os to iosxe to execute show install summary
    * Modified _get_parser_output
        * Updated the logic to execute the parser with timeout when

* genie.harness
    * Added parallel argument to connect

* genie.abstract
    * Modified Version class to support more OS versions



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean
    * clean
        * Updated logic to enable recovery report on all stages.
    * stages
        * connect
            * Added logic to ignore rollup on connect stage.
    * recovery
        * Updated the result to Passx.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* sdk-pkg
    * iosxe/stages
        * update the config replace command to use flash instead of bootflash

* clean
    * recovery
        * update the recovery process to use state machine for bringing device to enable state



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Added
        * Increase the time for copyfile to complete the execution of copy command in configure stage.



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified management ops implementation
        * Learn IP, interface via default gateway and ARP info



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_ntp_auth_key
        * API to configure NTP authentication key.
    * Added configure_ntp_authenticate
        * API to configure NTP authentication.
    * Added configure_ntp_trusted_key
        * API to configure NTP trusted key.
    * Added configure_ntp_server_with_auth
        * API to configure NTP server with authentication.
    * Added configure_no_ntp
        * API to remove complete NTP configuration.
    * Added configure_tftp_server
        * API to configure a TFTP server with the specified file path.
    * Added configure_vlan_and_no_shutdown
        * API to configure VLAN and no shutdown on a device.
    * Added API configure_radius_server_dtls_port
        * API to Configure radius server dtls port
    * C9400
        * Added execute_install_one_shot
            * API to execute_install_one_shot
    * Added configure_logging_ipv6
        * API to configure logging ipv6
    * Added unconfigure_data_mdt
        * API to unconfigure data mdt
    * Added no ip pim send-rp-announce Loopback0 scope 10
    * Added API configure_ipv6_logging_with_transport_and_facility
        * API to Configure IPv6 logging with transport and facility on the device.
    * Added API redirect_igmp_snooping_group_info
        * API to redirect igmp snooping from the command output to a file in bootflash of the device
    * Added support for below to get output in bootflash
        * show tech-support platform layer3 multicast group_ipadd {grp} srcIp {src_ip}
        * show tech-support platform layer3 multicast vrf {vrf} group_ipv6Addr {grp_ipv6} srcv6Ip {src_ipv6}
        * show tech-support platform layer3 multicast group_ipv6Addr {grp_ipv6} srcv6Ip {src_ipv6}
    * Added API show_tech_support_platform_interface
        * API to get show tech-support platform interface <interface_name> to copy device output to a file in bootflash
        * API to get show tech-support platform interface port-channel <port_id> to copy device output to a file in bootflash
    * Added API show_tech_support_platform_l2
        * API to Redirect the VLAN, interface, or port-channel-specific information from the command output to a file in bootflash of the device
    * Added API show_tech_support_platform_l2_matm
        * API to get VLAN or MAC address-specific information from the command output to a file in bootflash of the device
    * Added API show_tech_support_platform_mld_snooping
        * API to get show tech-support platform mld_snooping Group_ipv6Addr {grp_ipv6} vlan {vlan_id} | redirect bootflash{file_name} to copy device output to a file in bootflash
    * Added API show_tech_support_platform_monitor
        * API to get show tech-support platform monitor <session_id> to copy device output to a file in bootflash
    * Added configure_fec_auto_off
        * API to configure fec auto/off on 10G interface.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_snmp_server_user API
        * Added support for 3des as a valid priv_method
        * Modified to return device CLI output
    * Modified APi configure_ip_pim_bsr_rp_candidate
        * Fixed handling of rp and bsr flags to ensure proper configuration.
        * Added handling with negate_bsr and negate_rp to ensure accurate unconfiguration.
    * Modified
        * Updated configure_span_monitor_session API with optional argument to specify the monitor session source.

* apis
    * APIUTGenerator
        * Fix issue where API exclusion list is not properly loaded from the test arguments YAML file.

* iosxr
    * Modified
        * Removed install commit from admin mode

* sdk-pkg
    * Modified triggers and blitz
        * Fixed issue where job would get stuck during subscription poll and subscription once

* all os
    * Modified Blitz action yang_snapshot_restore to use better Xpaths
        * Xpaths with nodes that are missing prefixes are now prefixed with the

* sdk
    * Bumped pyans1 version


--------------------------------------------------------------------------------
                                    Removed                                     
--------------------------------------------------------------------------------

* iosxe
    * Removed unconfigure_route_map
        * Removed duplicate api unconfigure_route_map.


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified Ospf unconfigure_route_map
        * Modified datatype of route_map from int to str in comments.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added Parser for ShowMonitorSession
        * Added schema and parser for 'show monitor session {session_number}'

* iosxe
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroups Parser
        * Added schema and parser for
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightRoutes
        * Added schema and parser for
            * 'show platform hardware fed switch active fwd-asic insight l2m_routes'
            * 'show platform hardware fed switch active fwd-asic insight l3m_routes'
    * Added Parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfPorts
        * show platform hardware fed switch active fwd-asic insight vrf_ports_detail()
        * show platform hardware fed switch active fwd-asic insight vrf_ports()
    * Added Parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfRouteTable
        * show platform hardware fed switch active fwd-asic insight vrf_route_table()
    * Added ShowPlatformSoftwareFedSwitchAclParallelKeyProfileEgress
        * Added schema and parser for'show platform software fed switch <active/stby> acl man parallel-key-profile egress all'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmLagStatus
        * Added schema and parser for 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_status'
    * Added ShowPlatformHardwareQfpActiveDatapathInfrastructureSwHqf and ShowPlatformHardwareFedSwitch1FwdAsicInsightIfmLagMembers parser.
        * Added parser for cli show platform hardware qfp active datapath infrastructure sw-hqf.
        * Added parser for cli show platform hardware qfp active datapath infrastructure time basic.
    * Added support for parsing the 'show policy-map type pocket service' command
    * Added support for parsing the 'show cce cpdp bindings' command
    * Added ShowBgpAllSummaryNetwork
        * Added 'show bgl * all summary' command and schema for the command.
    * Added ShowEthernetRingG8032PortStatus parser
        * Added schema and parser for 'show ethernet ring g8032 port status'
    * Added ShowIpSubscriberIp parser
        * Added schema and parser for 'show ip subscriber ip {ip_address}'
    * Added ShowIpv6PimMdtReceive
        * show ipv6 pim mdt receive
        * show ipv6 pim vrf {vrf} mdt receive
    * Added ShowMemoryDebugLeaksSummary
        * Added 'show memory debug leaks summary' command and schema for the command.
    * Added ShowMplsTpSummary parser in show_mpls.py
    * Added schema and parser for cli 'show mpls tp summary'
    * Added schema and parser for CLI show platform hardware cpp active infrastructure exmem statistics user
    * Added Parser ShowPlatformSoftwareFedSwitchAcl in show_acl.py
        * show platform software fed switch active acl
    * Added ShowPlatformSoftwareAdjacencyRpActive parser
        * Added schema and parser for cli
            * 'show platform software adjacency RP active'
    * Added ShowStackPowerDetailSwitch
        * Added schema and parser for'show stack power detail switch'
    * Added ShowPlatformSoftwareFedSwitchActiveIpmfibVrfGroupDetail parser
        * Added parser for cli show platform software fed switch {switch_type} ip mfib vrf {vrf_name} {group}
        * Added parser for cli show show platform software fed switch {switch_type} ip mfib vrf {vrf_name} {group} detail
    * Added  ShowPlatformSoftwareFedIpIgmpSnoopingGroup parser
        * Added schema and parser for cli "show platform software fed {switch} {module} ip igmp snooping group"
    * Added ShowPlatformSoftwareFedActiveIpTypeMfibGroup parser
        * Added schema and parser for cli "show platform software fed {switch} {switch_var} {ip_type} mfib {group}"
    * Added ShowPlatformSoftwareFedSwitchActiveOifsetUridl2mhash parser
        * Added parser for cli show platform software fed switch {switch_type} oifset l2m hash {hash_id} detail
    * Added ShowPlatformSoftwareFedSwitchFnfProfilesDump Parser
        * Added schema and parser for cli 'show platform software fed switch fnf profiles dump'
    * Added ShowPlatformSoftwareL2vpnFpActiveAtom parser
        * Added schema and parser for cli
            * 'show platform software l2vpn fp active atom'
    * Added schema and parser for 'show platform hardware qfp active classification class-group-manager class-group client cce all'
    * Added ShowUACUplink parser
        * Added schema and parser for cli 'show uac uplink'
    * Added ShowUACUplinkDB parser
        * Added schema and parser for cli 'show uac uplink db'
    * Added ShowUACActivePort parser
        * Added schema and parser for cli 'show uac active-port'
    * Added ShowUACActiveVlan parser
        * Added schema and parser for cli 'show uac active-vlan'
    * Added ShowPlatformSoftwareMerakiService parser
        * Added schema and parser for cli 'show platform software meraki-service'
    * Added ShowPlatSoftFedSwAcAccessSecurityDcTableSummary parser.
        * Added parser for cli show platform software fed {switch} {mode} access-security dc-table summary.
        * Added parser for cli show platform software fed {switch} {mode} access-security dc-table interface if-id {port_if_id}.
    * Added ShowPlatformSoftwareFedSwAcAccessSecurityAuthAclSum parser.
        * Added parser for cli show platform software fed {switch_type} access-security auth-acl summary.
    * Added ShowPlatformSoftwareFedSwitchActiveSecurityfedWrclientsifid parser.
        * Added parser for cli show platform software fed switch {switch_type} security-fed wrclients if_id {port_if_id}.
    * Added ShowPlatformsoftwarefedswitchactivesecurityfedpmifid parser.
        * Added parser for cli show platform software fed switch {switch_type} security-fed pm if-id {port_if_id}.
    * Added ShowDeviceTrackingMessagesDetailedNum parser
        * Added parser for cli show device-tracking messages detailed {number}
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmLagStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_status({lag_gid}).
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightIfmPortErrStatus parser.
        * Added parser for cli show platform hardware fed switch {switch_id} fwd-asic insight ifm_port_err_status({system_port_gid}).
    * Added ShowPlatformSoftwareInfrastructurePunt parser
        * Added parser for cli show platform software infrastructure punt
    * Added ShowPlatformSoftwareFedSwitchActiveAclSgaclCellSgtDgt parser
        * Added parser for cli show platform software fed switch {switch_type} acl sgacl cell {sgt} {dgt}.
    * Added ShowPlatformSoftwareFedSwitchActiveSgaclVlan parser
        * Added parser for cli show platform software fed switch {switch_type} sgacl vlan.
    * Added ShowPlatformSoftwareFedSwitchActiveAclInfoDbFeatureCgAclSummary parser
        * Added parser for cli show platform software fed switch active acl info db feature cgacl summary
    * Added ShowCryptoIsakmpPeersConfig
        * show crypto isakmp peers config
    * Added ShowCryptoSslAuthorizationPolicy
        * show crypto ssl authorization policy
    * Added ShowIpSlaApplication parser
        * Added schema and parser for cli 'show ip sla application'

* added parser for cli show platform software fed switch {active} ipv6 mfib vrf {vrf_name} {group} detail
    * Added ShowPlatformSoftwareFedSwitchActiveIpIgmpSnoopingGroupsVlan parser
        * Added parser for cli show platform software fed {switch} {module} ip igmp snooping groups vlan {vlan_id} {group} detail
        * Added parser for cli show platform software fed {switch} {module}  ipv6 mld snooping group vlan  {vlan_id} {group} detail

* generic/rv1
    * Add pid for iosxr

* added showcryptosslsessionprofile
    * show crypto ssl session profile


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified ShowIpDhcpSnoopingBinding
        * Modified Schema  accept list of entries from single vlan using ListOf
    * Modified ShowLogging
        * Modified regex pattern to support filtering enabled (0 messages logged)*
    * Modified AdminShowDiagChassis
        * Changed part_number optional in the schema
    * Modified ShowIsisDatabase
        * Modified regex pattern to support LSP Holdtime/Rcvd 43588/*

* iosxe
    * Added ShowPlatformUplinks parser.
        * Added parser for cli 'show platform uplink'.
    * Modified ShowPlatformSoftwareFedActiveIpv6MldSnoopingVlanDetail parser
        * Added keys for cli show platform software fed {switch_var} {state} ipv6 mld snooping vlan {vlan} detail
    * Modified ShowLicenseTechSupport
        * Updated the parser to support additional lines
    * Modified ShowPlatformSoftwareFedIgmpSnoopingVlanDetail parser
        * Added keys for cli show platform software fed {switch_var} {state} ip igmp snooping vlan {vlan} detail
    * Fixed parser ShowSwitchStackPortsSummary
        * Fixed regex pattern to handle space.
    * Fixed parser ShowPlatformSoftwareFedSwitchSecurityfedDhcpsnoopVlanVlanid
        * Added regex pattern p4 to match the output of the command.
    * fixed parser ShowDeviceTrackingDatabaseMacDetails - modified regex
    * Fixed parser ShowFipsStatus
        * Fixed the logic under p1 regex to match Switch and Stacking for new output
    * Modified ShowInstallSummary
        * Changed the `auto_abort_timer` as an Optional key
    * Fixed parser ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id
        * Made switch as hardcoded value
    * Fixed parser ShowPlatformSoftwareMldSnoopingGroupsCount
        * Added support cli for all types of devices
    * Fixed parser ShowPlatformSoftwareFedActiveIpTypeMfibGroup
        * according to output modified schema and Optional added in for pps_approx
    * Fixed parser ShowPlatformSoftwareFedActiveIpMfibVrf
        * according to output modified schema and Optional added in for pps_approx
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIpMulticastInterface
        * Instead of ipv6 always script picking ipv4, so added ip type in cli, then we can pick ipv4 or ipv6 based on the cli
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveMatmMactable
        * Added "show platform software fed active matm macTable" to the command
    * Fixed parser ShowPlatformSoftwareFedSwitchPortSummary
        * Added 'show platform software fed {mode} port summary' command to support modular and svl platforms.
    * Fixed parser ShowPlatformSoftwareFedSwitchActivePortIfId
        * made 'operational_speed' type as either int or str and fix reg ex p5
    * Fixed parser ShowPlatformSoftwareFedIpv6MfibSummary
        * modified p1 and p7 regular expressions to match single digit numbers also
    * Fixed parser ShowPlatformSoftwareMldSnoopingGroupsCount
        * according to output modified shema
    * Modified ShowPlatformSoftwareFedSwitchActiveOifsetL3mHash parser
        * Modified schema and parser for CLI
            * 'show platform software fed switch {switch} {module} oifset l3m'
            * 'show platform software fed switch {switch} {module} oifset l3m hash {hash_data} detail'
    * Modified ShowEnvironmentFan
        * Modified schema and parser for'show environment fan'
    * Modified ShowPlatformSoftwareFedSwitchActiveAclInfoDbSummary parser
        * Modified parser for cli show platform software fed {switch} {mode} acl info db summar
        * Added parser for cli show platform software fed {switch} {mode} acl info db feature {feature_name} summary
    * Modified ShowPlatformSoftwareFedSwitchStateIfmIfIdIf_id parser
        * Modified parser for cli show platform software fed switch {state} ifm if-id {if_id
    * Modified ShowPlatformSoftwareFedPuntEntriesInclude parser
        * Modified parser for cli 'show platform software fed {port_num} punt entries | include {match}'
    * Modified ShowEnvironmentPowerAll
        * Modified schema and parser for 'show environment power all'
    * Added ShowInventoryName parser in show_inventory.py
        * Added schema and parser for 'show inventory {name}'
    * Added ShowMacsecHw parser in show_macsec.py
        * Added schema and parser for 'show macsec hw'
    * Modified show users parser
        * Include tty as new field

* iosxr/rv1
    * Updated the parser 'ShowDiagDetails' to support

* sonic
    * Modified ShowPlatformInventory
        * Modified p3 regex pattern

* nxos
    * Updated ShowInventory class
        * Fixed logic to identify slot number


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandL2
        * Added schema and parser for CLI 'show platform hardware fed switch active fwd-asic-insight l2 mirror command l2'
    * Added parser show cloud-mgmt
    * Added parser show cloud-mgmt connect
    * Add schema and parser for show platform hardware qfp active feature tcp stats detail
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightL3mRoutes parser
        * Added schema and parser for CLI 'show platform hardware fed switch active fwd-asic-insight l3m_routes(filter)'



genie.telemetry
"""""""""""""""
