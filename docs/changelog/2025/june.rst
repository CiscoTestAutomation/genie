June 2025
==========

June 29 - Genie v25.6 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.6 
    ``genie.libs.health``, v25.6 
    ``genie.libs.clean``, v25.6 
    ``genie.libs.conf``, v25.6 
    ``genie.libs.filetransferutils``, v25.6 
    ``genie.libs.ops``, v25.6 
    ``genie.libs.parser``, v25.6 
    ``genie.libs.robot``, v25.6 
    ``genie.libs.sdk``, v25.6 
    ``genie.telemetry``, v25.6 
    ``genie.trafficgen``, v25.6 




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* schema and main
    * Added support for alias in the trigger_datafile


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* genie/abstract
    * Added chassis_type key to the abstraction order.



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * modified reset configuration clean stage
        * Keep aaa new-model config, default enable auth to none
    * modified apply_configuration stage
        * Added show running-config / show startup-config
    * remove_smu_image
    * Updated clean stages to use syslog statement to ensure syslog messages are captured during execution.
    * connect
        * Boot device from ROMMON has been modified to reflect a 'failed' status instead of 'passx' when an exception occurs

* clean-pkg
    * iosxe
        * Updated the check_reload_dialog pattern list for install image stage

* clean/iosxe/stages
    * Modified the Rommon Boot stage
    * Modified the Rommon Boot stage

* os/iosxe
    * Modified rommon boot stage
        * deprecated the tftp argument
    * Modified reset configuration
        * add no platform console virtual to KEEP dictionary
    * Modified InstallImage stage
        * Updated the image matching logic to match the build label first and then xe_version.
        * Added new steps for Verify the ignore startup configs.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified interface.py
        * Added support to configure switchport mode dot1q-tunnel,switchport access vlan under port-channel interfaces



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* protocols/tftp
    * Added placeholder for tftp stat implementation.



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
    * Added acm_merge
        * New API to execute acm merge  with timeout and without timeout
    * Added API generate_dummy_file
        * API to generate dummy file
    * ie3k
        * Added new api execute_copy_noverify
    * Added acm_save to the IOSXE SDK
        * API to execute acm save commands
    * Added acm_rollback to the IOSXE SDK
        * API to execute acm rollback commands
    * Added API change_file_permissions
        * API to give full permissions to file
    * Added destroy_guestshell
        * API to destroy guestshell
    * Added acm_configlet_create
        * New API to execute acm configlet create flashabc
    * Added acm_configlet_remove
        * New API to execute acm configlet remove flashabc
    * Added acm_configlet_delete
        * New API to execute acm configlet modify demo delete 1
    * Added acm_configlet_insert
        * New API to execute acm configlet modify demo insert 1 vlan 15
    * Added acm_configlet_replace
        * New API to execute acm configlet modify demo replace 1 vlan 15
    * Added unconfigure_policy_map_shape_on_device
        * API to unconfigure policy_map shape on device
    * Added clear_nat_statistics
        * API to execute  clear_nat_statistics on the device
    * Added API configure_interfaces_uplink
        * Added API to configure_interfaces_uplink
    * Added API configure_interfaces_no_uplink
        * Added API to configure_interfaces_no_uplink
    * Added configure_ospf_retransmit_interval
        * API to configure_ospf_retransmit_interval
    * Added unconfigure_vlan_to_sgt_mapping
        * API to unconfigure vlan sgt
    * Added API unconfigure_ipv6_flow_monitor_sampler
        * API to configure unconfigure_ipv6_flow_monitor_sampler.
    * Added acm_confirm_commit
        * New API to execute acm confirm-commit
    * Added acm_cancel_commit
        * New API to execute acm cancel-commit
    * Added configure_ipv6_flow_monitor_on_interface
        * API to configure IPv6 flow monitor with sampler on an interface
    * Added API unconfig_flow_monitor_on_vlan_interface
    * Added acm_rules
        * New API to execute acm rules
    * Added acm_replace
        * New API to execute acm replace with timeout and without timeout
    * Added force
        * API execute_install_one_shot to execute with force argument
    * Added acm_rules
        * New API to execute acm rules flashabc
    * Added execute_factory_reset
        * API to factory reset the device.
    * configure_logging_tls_profile
        * configure_logging_tls_profile
    * configure_syslog_server_tls_profile
        * configure_syslog_server_tls_profile
    * unconfigure_logging_tls_profile
        * unconfigure_logging_tls_profile
    * unconfigure_syslog_server_tls_profile
        * unconfigure_syslog_server_tls_profile
    * change_cipher_from_tls_profile
        * change_cipher_from_tls_profile
    * configure_logging_discrimnator
        * configure_logging_discrimnator
    * unconfigure_logging_discrimnator
        * unconfigure_logging_discrimnator
    * apply_logging_discrimnator
        * apply_logging_discrimnator
    * unapply_logging_discrimnator
        * unapply_logging_discrimnator
    * configure_pki_import_cert
        * configure_pki_import_cert
    * pki
        * Added configure_crypto_pki_download_crl
        * Added unconfigure_crypto_pki_download_crl
    * Added count_trace_in_logging
        * API to count trace in logging

* api
    * IOSXE
        * Added execute_reload_verify API for IE3K devices
        * Added execute_reload_noverify API for IE3K devices

* os/iosxe/c9800
    * Added api configure_management_ip.

* iosxe/c8kv
    * Added configure_autoboot
        * API to configure autoboot


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* updated api unit tests
    * IOSXE
        * Updated unittests to new testing method
            * configure_pnp_startup_vlan
            * unconfigure_pnp_startup_vlan
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_access_map_match_ip_address_action_forward
            * unconfigure_ace
            * unconfigure_acl
            * unconfigure_acl_with_src_dsc_net
            * unconfigure_as_path_acl
            * unconfigure_filter_vlan_list
            * unconfigure_ip_sgacl
            * unconfigure_ipv6_acl
            * unconfigure_ipv6_acl_ace
        * Removed the mock yaml under 'unconfigure_extended_acl_deny' as we do not have any API for it.
    * IOSXE
        * Updated unittests to new testing method
            * clear_arp_cache
            * clear_ip_arp_inspection
            * configure_arp_access_list_permit_ip_host
            * configure_ip_arp_inspection_filter
            * configure_ip_arp_inspection_log_buffer
            * configure_ip_arp_inspection_on_interface
            * configure_ip_arp_inspection_validateip
            * configure_ip_arp_inspection_vlan
            * configure_ip_arp_inspection_vlan_logging
            * unconfigure_arp_access_list
            * unconfigure_ip_arp_inspection_filter
            * unconfigure_ip_arp_inspection_log_buffer
            * unconfigure_ip_arp_inspection_on_interface
            * unconfigure_ip_arp_inspection_validateip
            * unconfigure_ip_arp_inspection_vlan
            * unconfigure_ip_arp_inspection_vlan_logging
    * IOSXE
        * Updated unittests to new testing method
            * unconfigure_mac_access_group_mac_acl_in_out
            * unconfigure_mac_acl
            * unconfigure_standard_acl
            * configure_app_hosting_appid_docker
            * configure_app_hosting_appid_iperf_from_vlan
            * configure_app_hosting_appid_trunk_port
            * configure_app_hosting_resource_profile
            * configure_app_management_networking
            * configure_thousand_eyes_application
            * confirm_iox_enabled_requested_storage_media
            * enable_usb_ssd_verify_exists
            * unconfigure_app_hosting_appid

* iosxe
    * Modified configure_ipv6_logging_with_discriminator
        * Added conditional logic to handle syslog_host and discriminator_name parameters.
    * Added API debug_software_cpm_switch_pcap_drop
        * Added API to debug_software_cpm_switch_pcap_drop
    * Added API debug_software_cpm_switch_feature
        * Added API to debug_software_cpm_switch_feature
    * Added API debug_software_cpm_switch_pcap
        * Added API to debug_software_cpm_switch_pcap
    * Added API debug_software_cpm_switch_pcap_count
        * Added API to debug_software_cpm_switch_pcap_count
    * Fix the configure rommon tftp to get `tftp_server` from recovery.
    * Modified configure_fnf_flow_record
        * Modified the API to configure "match routing vrf input" if match_vrf is True.
    * Modified configure_ipv6_flow_monitor_sampler
        * Modified the API to configure sampler based on direction.
    * Modified fix for execute_install_one_shot API.
        * Converted output to string for the result verification.
    * Modified "configure_management_ssh" API
        * added ip ssh source-interface command
    * cat9k
        * Modified configure_ignore_startup_config
            * Added handling for standby connections to prevent failures when standby is locked
            * Skip standby devices since configuration is already applied with "switch all" command
        * Modified unconfigure_ignore_startup_config
            * Added debug logging for troubleshooting function calls
            * Added handling for standby connections to prevent failures when standby is locked
            * Skip standby devices since configuration is already applied with "switch all" command
    * Modified configure_logging_ipv6
        * Added conditional logic to handle syslog_host and transport parameters.
    * Added unconfigure_logging_facility_and_trap
        * API to unconfigure logging facility and trap.
    * Modified configure_ipv6_logging_with_transport_and_facility
        * Added conditional logic to handle transport_protocol parameters.
        * Removed cli "no logging facility local0", "no logging trap debugging"

* updated unittests
    * IOSXE
        * Updated below API unit tests with the latest unit testing methodology
            * configure_call_home_alert_group_config_snapshot
            * configure_call_home_contact_email_addr
            * configure_call_home_contract_id
            * configure_call_home_copy_profile
            * configure_call_home_customer_id
    * IOSXE
        * Updated below API unit tests with the latest unit testing methodology
            * configure_call_home_data_privacy
            * configure_call_home_http_proxy
            * configure_call_home_http_resolve_hostname_ipv4_first
            * configure_call_home_http_secure_server_identity_check
            * configure_call_home_phone_number

* cleaning api ut's
    * Iosxe
        * Updated with latest UT method to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's
            * configure_access_list_extend_with_range_and_eq_port
            * configure_access_map_match_ip_address_action_forward
            * configure_bgp_address_advertisement
            * configure_bgp_advertise_l2vpn_evpn
            * configure_bgp_auto_summary
            * configure_bgp_best_path_as_path_multipath_relax
    * Iosxe
        * Updated with latest UT mathod to all of the below mentioned API UT's
            * config_ip_tcp_mss
            * config_refacl_global_timeout
            * configure_access_list_extend
            * configure_access_list_extend_with_dst_address_and_gt_port
            * configure_access_list_extend_with_dst_address_and_port
            * configure_access_list_extend_with_port
    * Iosxe
        * Updated with latest UT method to all of the below mentioned API UT's
    * Iosxe
        * Updated with latest UT method to all of the below mentioned API UT's

* sdk
    * IOSXE
        * Updated `send_break_boot`
            * Set buffer to an empty string before processing the dialog
    * IOSXE
        * Updated `configure_rommon_tftp_ha`
            * Change to look for rommon information in `management` attribute instead of `rommon` attribute due to service conflict.

* updated error pattern for copy /verify
    * Iosxe
        * Ie3k
            * Passed the Error_pattern to match the execution error of api.


--------------------------------------------------------------------------------
                        Configure_Ipv6_Dhcp_Relay_Trust                         
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                            Configure_Ldra_Interface                            
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                   Unconfigure_Ipv6_Dhcp_Client_Vendor_Class                    
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
              Unconfigure_Ipv6_Dhcp_Relay_Destination_Ipv6Address               
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                     Unconfigure_Ipv6_Dhcp_Relay_Option_Vpn                     
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
              Unconfigure_Ipv6_Dhcp_Relay_Source_Interface_Intf_Id              
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                       Unconfigure_Ipv6_Dhcp_Relay_Trust                        
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                        Configure_Ip_Nhrp_Map_Multicast                         
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                    Configure_Ip_Nhrp_Map_Multicast_Dynamic                     
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                          Configure_Ip_Nhrp_Network_Id                          
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                             Configure_Ip_Nhrp_Nhs                              
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                           Configure_Ip_Nhrp_Redirect                           
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                              Configure_Nhrp_Group                              
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                       Unconfigure_Ip_Nhrp_Map_Multicast                        
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                   Unconfigure_Ip_Nhrp_Map_Multicast_Dynamic                    
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                         Unconfigure_Ip_Nhrp_Network_Id                         
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                            Unconfigure_Ip_Nhrp_Nhs                             
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                          Unconfigure_Ip_Nhrp_Redirect                          
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                             Unconfigure_Nhrp_Group                             
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                     Unconfigure_Tunnel_Mode_Gre_Multipoint                     
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                      Configure_Tunnel_Mode_Gre_Multipoint                      
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                            Configure_Tunnel_Source                             
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                        Unconfigure_Interface_Tunnel_Key                        
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                       Unconfigure_Ip_Nhrp_Authentication                       
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                          Unconfigure_Ip_Nhrp_Holdtime                          
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                            Unconfigure_Ip_Nhrp_Map                             
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                     Update                                     
--------------------------------------------------------------------------------

* iosxe
    * Updated doc string for config_macsec_keychain_on_device api
        * Added doc string for these arguments  key, crypt_algorithm


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified unconfigure switch provision
        * Modified API to unconfigure switch provision using switch model



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPost Parser
        * Added ShowPost parser for c9200
    * Added ShowIpv6MldSnoopingAddress Parser
        * Added schema and parser for cli "show ipv6 mld snooping address vlan {vlan} {group}"
    * Added ShowPlatformSoftwareFedIpRouteSummary parser
        * Added c9610 schema and parser for 'show platform software fed {switch} ip route summary'
    * Added Schema and Parser for ShowPlatformHardwareFedSwitchFwdAsicInsightAclL2AclAttachmentCircuits
        * show platform hardware fed switch {state} fwd-asic insight acl_l2_acl_attachment_circuits()
    * Added ShowPlatformSoftwareIgmpSnoopingGroupsVlanCount
        * Added schema and parser for 'show platform software fed {state} ip igmp snooping groups vlan {vlan} count' command.
    * Added ShowIpv6MfibInterface
    * 'show ipv6 mfib interface'
    * Added ShowPlatformSoftwareFirewallFPActivePairs
        * show platform software firewall FP active pairs
    * Added acm log parser
        * Added Acm Log {command}
        * Added Acm Log IndexNumber
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallClientStatistics
        * show platform hardware qfp active feature firewall client statistics
    * Added ShowCryptoIpsecSaIpv6Detailed Parser
        * Parser for 'show crypto ipsec sa ipv6 detailed'
    * Added ShowCryptoIkev2DiagnoseError Parser
        * Parser for 'show crypto ikev2 diagnose error'
    * ShowIpMrmStatus
        * show ip mrm status.
    * Added ShowMplsTpTunnelTp parser in show_mpls.py
    * Added schema and parser for cli 'show mpls tp tunnel-tp 1 lsps detail'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclEthPortMixMode
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_eth_port_mix_mode'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclEthPortDense
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_eth_port_dense'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclGroupDetails
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_group_details'
    * Added ShowPlatformHardwareFedFwdAsicInsightAclAttachmentCircuit
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_attachment_circuit'
    * Added ShowPlatformSoftwareNatFpActiveMappingDynamic
    * 'show platform software nat fp active mapping dynamic'
    * Added ShowControlCpu
        * Added schema and parser for 'show control cpu'
    * Added ShowIpvMldVrfGroup parser in show_ip.py
    * Added schema and parser for cli 'show ipv mld vrf {vrf} groups {group}'
    * Added ShowParameterMapTypeInspect
        * 'show parameter-map type inspect {param}'
    * Added acm merge <configlet_file> validate parser
        * Parse "acm merge demo validate"
    * Added ShowL2vpnServiceAll
        * show l2vpn service vfi all
    * Added ShowIpWccpWebCacheDetail parser in show_ip.py
    * Added schema and parser for cli 'show ip wccp web-cache detail'
    * Added Parser for dir crashinfo
        * Added a new schema and parser for the dir crashinfo command.
    * Added ShowMplsL2transportSummary
        * show mpls l2transport summary
    * Added show platform hardware fed switch {switch_id} fwd-asic insight l2_attachment_circuit_status(lag_gid={lag_gid})
    * cat9k
        * Added ShowLoggingOnboardSlotStatus parser
            * Added schema and parser for cli "show logging onboard slot {slot} status"
    * Added show platform software fed switch <active/stby> acl manager acl-group interface <interface>
        * Added show platform software fed switch <active/stby> acl manager acl-group iif_id <if_id_num>
    * Added support for ShowPlatformHardwareFedSwitchFwdAsicInsightL2SwitchMacTable parser
    * Added ShowPlatformSoftwareNatFpActivePool
    * 'show platform software nat fp active pool'
    * Modified ShowIpPimInterfaceCount
        * show ip pim int count.
    * Added ShowPlatformSudiCertificateNonce schema in iosxe/ie3k
        * Added parser for show software platform sudi certificate sign in iosxe/ie3k
    * Added ShowPlatformIntegrity schema
        * Added parser for show platform integrity sign in iosxe/ie3k
    * Added ShowPlatformUplinks parser.
        * Added parser for cli 'show platform uplink'.
    * Added ShowPlatformSoftwareFedActiveAclBindDbSummary parser
        * Added rv1 schema and parser for 'show platform software fed active acl bind db summary'
    * Added ShowPlatformSoftwareFedActiveAclBindDbDetail parser
        * Added rv1 schema and parser for 'show platform software fed active acl bind db detail'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightS1TrapStatus
        * Added schema and parser for
            * 'show platform hardware fed switch {state} fwd-asic insight s1_trap_status()'
    * Added ShowPlatformSoftwareMemoryForwardingManager
    * 'show platform software memory forwarding-manager F0 brief | include {option}'
    * Added ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableDef
        * Added schema and parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_table_def()'.
    * Added ShowPlatformSoftwareFedSwitchAclBindSdkInterfaceFeatureDirDetailAsic
        * Added schema and parser for 'show platform software fed {switch} {state} acl bind sdk interface {interface} feature {feature} dir {dir} detail asic {asic}'
    * Added ShowPlatformSoftwareFedSwitchAclParallelKeyProfileIngress
        * Added schema and parser for 'show platform software fed {switch} {state} acl man parallel-key-profile ingress all'
    * Added ShowPlatformSoftwareAccessListFpActiveStatistics
        * Added 'show platform software access-list fp active statistics' command and schema for the command.
    * ShowVoiceCallSummary
        * show voice call summary.
    * Added ShowMplsTpLspsDetail parser in show_mpls.py
    * Added schema and parser for cli 'show mpls tp lsps detail'
    * Added ShowCallHomeProfileAll
        * show call-home profile {include}
    * Added ShowIpIgmpSnoopingGroupsVlanCount
        * Added schema and parser for 'show ip igmp snooping groups vlan {vlan} count' command.
    * Added show platform hardware fed switch active fwd-asic insight acl_svi_attachment_circuits
    * Added acm configlet status parser
        * Parse "acm configlet status"


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpd
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceEgressSdkDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressSdk
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceEgressNpdDetailed
        * Calling super parser cli with command argument
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailedAsicAll
        * Calling super parser cli with command argument
    * Modified parser ShowPlatformSoftwareFedSwitchActiveAclOgPcl
        * Added support for show platform software fed active acl og-pcl
        * Added mode to support switch numbers
    * Fixed parser ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added "show platform software fed {switch} {mode} acl info db feature {feature_name} dir {in_out} detail" to the command
        * modified switch as variable for flexibility
    * Modified ShowProcessesCpuSorted
    * 'show processes cpu sorted'  #Changed timeout from default to timeout 300 for this cli
    * Fixed parser ShowLoggingOnboardSlotUptime
        * Added 'show logging onboard slot {slot} uptime latest'.
    * Modified ShowPlatformHardwareFedSwitchFwdAsicInsightIfmLagStatus parser
        * Modified parser for CLI
            * 'show platform hardware fed switch {switch_id} fwd-asic insight ifm_lag_status({lag_gid})',
            * 'show platform hardware fed {switch} {switch_id} fwd-asic insight ifm_lag_status({lag_gid})'
        * Modified parser for arguments
            * 'switch_id'"1" to "Any"
    * Removed ShowPlatformHardwareFedSwitchFwdAsicInsightIfmLagStatus parser
        * due to dublication of the parser
    * Modified ShowFlowMonitor
        * Modified regexn and parser schema
    * Fixed ShowFlowInterface parser
        * Fixed regex pattern p4 to match the output of the command.
    * Modified ShowPlatformHardwareFedSwitchQosQueueConfig parser
        * Removed duplicate parser code.
        * addded kwargs and command to detect the correct parser.
    * Fixed ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandStatus parser.
        * Modified parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_mirror_command_status({mirror_gid}).
    * Fixed ShowPlatformHardwareFedSwitchActiveFwdAsicInsightL2MirrorCommandL2 parser.
        * Modified parser for cli show platform hardware fed switch {switch_id} fwd-asic insight l2_mirror_command_l2({mirror_gid}).
    * show_route_map
        * Modified ShowRouteMapAll
            * Added regex pattern for ipv6 next-hop verify-availability
            * Added regex pattern for ipv6 next-hop recursive
    * Modified ShowPlatformSoftwareFedSwitchActiveOifset parser
        * Added support for show platform software fed active oifset
    * Modified ShowPolicyMapTypeInspectZonePair
    * Added show policy-map type inspect zone-pair new-trusted-untrusted cli
    * IE3K
        * Modified ShowHardwareLed
            * Modified the regex pattern
    * Added ShowPlatform
        * Added ShowPlatform parser in rv1
    * Modified parser Ping
        * Added the "B" flag as the indicator for the IPv6 Packet Too Big result
    * Modified ShowPlatformSoftwareFedSwitchAclBindDbInterfaceFeatureDirDetailAsic
        * Modified schema and parser for 'show platform software fed {switch} {state} acl bind db interface {interface} feature {feature} dir {dir} detail asic {asic}'
    * Modified ShowPlatformSoftwareFedSwitchAclParallelKeyProfileEgress
        * Modified schema and parser for'show platform software fed {switch} {state} acl man parallel-key-profile egress all'
    * Modified ShowPlatformSoftwareFedSwitchActiveAclBindSdkDetail
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk detail'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} cgid {cg_id} detail'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} dir {dir} detail asic {asic_no}'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk feature {feature_name} detail'
        * Modified schema and parser for'show platform software fed {switch} {switch_var} acl {acl} sdk if-id {if_id} detail'
    * Modified ShowPlatformSoftwareFedActiveIpMfibVrf parser
        * Modified p1 regex to match the correct line
    * Modified ShowPlatformSoftwareFedSwitchActiveIpMfibVrf parser
        * Modified p1 regex to match the correct line
    * Modified parser ShowRunInterface
        * Added support for pnp startup-vlan 1200
    * Modified parser ShowPlatformHardwareFedSwitchActiveFwdAsicInsightS1SecGroupsMatrixMapStatus
        * changed 'switch' as a variable for flexibility
    * IE3K
        * Modified ShowHardwareLed
            * Modified the show hardware led for support additional field
    * Modified ShowInstallRollbackId
        * Modified regex p1

* modified parser for 'show platform hardware fed switch active fwd-asic insight vrf_for_us_routes'.

* updated cli output handling to generalize parsing for all vrfs.

* iosxr
    * Modified ShowInventoryRaw
        * Upadted the regex
    * Modified ShowProcesses
        * Added regex for 'level' & 'mandatory'
        * Updated type for 'instance' from str to int

* nxos
    * Modified ShowVersion
        * Added the new regex pattern for supporting system version


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPolicyMapTypeInspectZonePair
    * Have added the new golden expected output for the clishow policy-map type inspect zone-pair in-out
    * Added ShowInterfacesTransceiverModule
        * Added ShowInterfacesTransceiverModule parser

* iosxr
    * Added ShowInterfacesTransceiverDetail
        * Added  ShowInterfacesTransceiverDetail in rv1 for supporting multiplle lanes


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Enhanced ShowMerakiConnect parser
        * Added support for delta fields in meraki_tunnel_interface section
        * Fields with "(Last Xs)" pattern are now converted to "*_delta" format



genie.telemetry
"""""""""""""""
