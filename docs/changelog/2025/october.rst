October 2025
==========

October 28 - Genie v25.10
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.10
    ``genie.libs.health``, v25.10
    ``genie.libs.clean``, v25.10
    ``genie.libs.conf``, v25.10
    ``genie.libs.filetransferutils``, v25.10
    ``genie.libs.ops``, v25.10
    ``genie.libs.parser``, v25.10
    ``genie.libs.robot``, v25.10
    ``genie.libs.sdk``, v25.10
    ``genie.telemetry``, v25.10
    ``genie.trafficgen``, v25.10




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* removed all usage of deprecated pkg_resources module in favor of importlib.metadata where possible.



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_enable_aes_encryption API
        * Added support to handle Old Masteer key prompt.

* clean-pkg/stages
    * iosxe
        * Updated ping_gateway in ConfigureManagement stage to attempt ping multiple times
    * iosxe
        * Increased the default reload_wait from 30 seconds to 150 seconds to allow sufficient time to match the reload patterns.
    * iosxe
        * Updated install image logic to skip the "Check for previous uncommitted install operation" step when the show install active output has no packages to commit.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean
    * IOSXE
        * Update clean install images to retry install image if there is not enough space after cleaning unprotected files.
    * IOSXE/cat9k
        * Delete clean install images logic for car9k stack devices to use the logic from IOSXE.

* iosxe
    * clean-pkg
        * Updated install image stage to collect debug logs on failure



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* filetransferutils
    * Added HTTPS support with HTTP fallback



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

* iosxe/c9200_480p
    * Added APIs to retrieve device recovery details and tftp boot command details for C9200-48P devices

* iosxe
    * Added unconfigure_device_sgt
        * API to execute no cts sgt
    * Added execute_hardware_qfp_active_feature_nat_datapath_pap_laddrpergaddr
        * show platform hardware qfp active feature nat datapath pap laddrpergaddr
    * Added API execute_platform_hardware_chassis_fantray_oir
        * Added API to execute_platform_hardware_chassis_fantray_oir
    * Added API disable_bfd_static_route
        * Added API to disable_bfd_static_route
    * Added API disable_ospf_bfd_all_interfaces
        * Added API to disable_ospf_bfd_all_interfaces
    * Added API configure_crypto_pki_certificate_map
    * Added API unconfigure_crypto_pki_certificate_map
    * Added API unconfigure_crypto_map
        * Added API to unconfigure_crypto_map
    * Added API configure_dynamic_cmap
        * Added API to configure_dynamic_cmap
    * Added API configure_pki_vrf_trustpoint
    * Added API unconfigure_pki_vrf_trustpoint
    * Added API remove_grant_auto
    * Added API crypto_pki_trustpool_import
    * Added API configure_trustpool_policy
    * Added API unconfigure_trustpool_policy
    * Added API unconfigure_autovpn
    * Added configure_diagnostic_schedule_module_test_all_daily
        * API to schedule diagnostic on module daily at specified time
    * Added unconfigure_diagnostic_schedule_module_test_all_daily
        * API to unschedule diagnostic on module daily at specified time
    * Added support for configuring IPv6 local pool on IOSXE devices.
    * Added configure_cts_reconciliation_period
        * API to configure CTS SXP reconciliation period
    * Added unconfigure_cts_reconciliation_period
        * API to unconfigure CTS SXP reconciliation period
    * Added configure_cts_retry_period
        * API to configure CTS SXP retry period
    * Added unconfigure_cts_retry_period
        * API to unconfigure CTS SXP retry period
    * Added unconfigure_cts_sxp_default_source
        * API to unconfigure source IPv4 and IPv6 address
    * Added configure_cts_sxp_default_source
        * API to configure source IPv4 and IPv6 address
    * Added API configure_class_map_match_protocol_attribute
        * Added API to configure class map match protocol attribute
    * Added API configure_mpls_ldp_neighbor_labels_accept
    * Added API unconfigure_mpls_ldp_neighbor_labels_accept
    * Added API configure_mpls_ldp_session_protection
    * Added API unconfigure_mpls_ldp_session_protection
    * PKI
        * import_pkcs12_tftp
        * export_pkcs12_tftp
    * Added API execute_crypto_pki_server_advanced
    * Added API unconfigure_crypto_map_entry
        * Added API to unconfigure_crypto_map_entry
    * Added support for unconfiguring IPv6 local pool on IOSXE devices.
    * Added API configure_crypto_pki_export_pkcs12_terminal
        * Added API to configure_crypto_pki_export_pkcs12_terminal
    * Added execute_show_debug to debug-execute.py file.
        * New API support for 'show debug' cli.
    * Added execute_show_platform_hardware_qfp_active_feature_nat_datapath_bind to platform-execute.py
        * New API support for 'show platform hardware qfp active feature nat datapath bind' cli
    * Added execute_show_platform_hardware_qfp_active_feature_td_datapath_statistics_clear to platform-execute.py
        * New API support for 'execute_show_platform_hardware_qfp_active_feature_td_datapath_statistics_clear' cli
    * Added execute_show_policy_firewall_config_platform to platform-execute.py file.
        * New API support for 'show policy-firewall config platform' cli with filter options.
    * Added execute_test_voice_port_detector_ring_trip to platform-execute.py
        * New API support for 'test voice port {port} detector ring-trip {on-off-disable}' cli
    * Added API for get_monitor_event_trace_crypto_ipsec_event_from_boot_detail
        * 'show monitor event-trace crypto ipsec event from-boot detail'
    * Added new API to configure EAP-FAST method profile
        * API to configure EAP-FAST method profile
    * Added new API to unconfigure EAP-FAST method profile
        * API to unconfigure EAP-FAST method profile
    * Added new API to configure EAP-FAST method password
        * API to configure EAP-FAST method password
    * Added new API to unconfigure EAP-FAST method password
        * API to unconfigure EAP-FAST method password
    * Added new API to configure MAB request attribute 2 password
        * API to configure MAB request attribute 2 password
    * Added new API to unconfigure MAB request attribute 2 password
        * API to unconfigure MAB request attribute 2 password
    * Added new API to configure dot1x credential profile
        * API to configure dot1x
    * Added API to attach an alarm profile to an interface.
    * Added API to detach an alarm profile from an interface.
    * Added API to configure/unconfigure input alarm facility
    * Added `get_environment_alarm_contact`
    * Added API get_hardware_led_status to retrieve the hardware LED status of a device.
    * Fixed an issue where unconfiguring alarm contact did not work as expected.
    * Added execute_show_ethernet_cfm_maintenance_points_remote,execute_show_ethernet_cfm_maintenance_points_local,execute_show_ethernet_cfm_errors to ethernet-execute.py file.
        * New API support for 'show ethernet cfm maintenance-points remote' cli.
        * New API support for 'show ethernet cfm maintenance-points local' cli.
        * New API support for 'show ethernet cfm errors' cli.
    * Added 'execute_show_monitor_event_trace_crypto_all' and 'execute_show_monitor_event_trace_crypto_ipsec_event_clock' to iosxe crypto-execute.py file.
        * New API support for 'show monitor event-trace crypto all' cli.
        * New API support for 'show monitor event-trace crypto ipsec event clock {hh}{mm}' cli.
    * Added show_tech_support_firewall to support - tech_support.py
        * New API support for 'show tech-support firewall' cli
    * Added test_platform_software_process_exit_forwarding_manager to iosxe-platform-execute.py
        * New API support for 'test platform software process exit forwarding-manager {processor} {state}' cli

* c9800-cl
    * Added configure_autoboot
        * API to execute configure autboot

* sdk-pkg
    * iosxe
        * Update the execute_copy_run_to_start api to return a boolean indicating success or failure
        * Added new api collect install log to debug the install image failures
    * 9300
        * Added support to collect install logs to debug failure in 9300 platform
    * iosxe/c9400
        * Added execute clear install state api for c9400 devices
    * iosxe/cat8k
        * Added execute_rommon_reset and execute_config_register api for cat8k devices

* iosxe/stack
    * Added API configure_crypto_autovpn_vpn_registry
        * Added API to configure_crypto_autovpn_vpn_registry
    * Added API configure_virtual_template_for_autovpn
        * Added API to configure_virtual_template_for_autovpn
    * Added API configure_crypto_ikev2_profile_autovpn
        * Added API to configure_crypto_ikev2_profile_autovpn
    * Added API configure_dmvpn_tunnel
        * Added API to configure DMVPN tunnel
    * Added API configure_dynamic_tunnel.
    * Added API get_platform_default_dir
        * Added API to get_platform_default_dir
    * Added API free_up_disk_space
        * Added API to free up disk space
    * Added API unconfigure_crypto_keyring
        * Added API to unconfigure keyring.

* added api configure_trust_device_on_interface
    * Added API to configure trust device on interface

* iosxe/dual_rp
    * Added API get_platform_default_dir
        * Added API to get_platform_default_dir
    * Added API free_up_disk_space
        * Added API to free up disk space

* powercycler module
    * Added
        * Support for power cycling of virtual machines in vCenter


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_route_map_permit to fix a integration case
        * When default_recursive is passed as True do not configure set vrf clause
    * Modified configure_route_map_permit to add few arguments
        * Added normal_nhop_ip for direct next hop address
    * Modified unconfigure_route_map_permit to add few arguments
        * Added normal_nhop_ip for direct next hop address
    * Modified API configure_access_map_match_ip_mac_address
        * Modified to support all output
    * Fixed API configure_crypto_map_entry
        * Fixed API to configure_crypto_map_entry
    * rommon
        * Setting the context of boot cmd to grub_breakboot handler.
        * Removed the escape character pattern from the connection dialog to not interfere with the breakboot detection.
    * Added new parameters in API configure_crypto_pki_server
    * Added new parameters in API configure_trustpoint
    * Fixed an issue in API configure_crypto_pki_download_crl
    * Added new Day choices in unconfigure_crypto_pki_download_crl
    * Pki
        * Added additional dialogs to configure_pki_enroll.
        * Added additional dialogs to change_pki_server_state
    * fixed API configure_crypto_pki_profile.
    * fixed API unconfigure_crypto_pki_profile.
    * Added parameters split_horizon, passive_interface and af_interface_shutdown to the API configure_eigrp_named_networks_with_af_interface to enhance its functionality.
    * updated remote_prefix, remote_ipv6_prefix parameters to use in correct CLI
    * updated API configure_ikev2_proposal with additional arguments to configure.
        * Added arguments ake_algos, ake_required
    * FlexVPN Fixed the issue where the API did not correctly configure NHRP redirect for IPv4 and IPv6 in FlexVPN tunnel interfaces.
    * updated API with additional arguments to configure.
    * Added new parameters in API configure_tunnel_with_ipsec
    * Health
        * Added a support to handle the notifying for new core files added.
    * Enhanced existing API `set_platform_soft_trace_debug` to handle `rp="RP"` case by
    * No changes were made to the switch-specific logic.
    * updated API with additional arguments to configure.
    * rommon
        * Fix the attribute error in send_break_boot api.
    * execute_install_one_shot
        * Added install_timeout post install to wait for reload.
    * Modified get_flow_monitor_cache_format_table_output to take timeout as input parameter as the output was getting truncated
    * Added timeout parameter to the API
    * Modified question_mark_retrieve API
        * Fixed prompt regex handling in question_mark_retrieve API to support flexible trailing characters.
    * Modified device_rommon_boot
        * Updated the code to extract the TFTP image from recovery information and provide it to the ROMMON TFTP configuration api's.
    * Modified delete_files
        * Enhanced to handle both relative and absolute file paths.
    * Made few changes in 'unconfigure_alarm_contact'

* iosxe/cat9k/c9400
    * Modified execute_install_one_shot to execute when device reloads

* iosxe/c8kv
    * rommon
        * Added `send_break_boot` api for c8kv devices to send break sequence during bootup to enter rommon mode.

* utils
    * Added build_export_filename
        * Added build_export_filename to preserve .tar.gz extension when copying files from device to local system.
    * Added configure_stealthwatch_cloud_monitor & unconfigure_stealthwatch_cloud_monitor
        * Added unconfigure_stealthwatch_cloud_monitor to configure stealtchwatch CLI & unconfigure them.

* generic
    * Update copy_to_device and copy_from_device APIs
        * use 'ip route get' to get source IP address of proxy host

* iosxe/ie3k
    * Modified
        * Included missing arguments of `execute_set_config_register` to match its function signature to the base API.

* updated timeout for api
    * Iosxe
        * Added the timeout fpr API.

* iosxe/c9400
    * Modified execute_install_one_shot api reverted the condtion for output from PR-3757

* fix the gh auth issue in jenkinsfile.

* updated unittests
    * IOSXE
        * Updated below API unit tests with the latest unit testing methodology
            * copy_file_with_scp

* iosxe/install
    * Modified execute_install_activate to execute when device reloads
    * Fixed the modification and removed the execution of default reload when 'command=cmd' called.

* iosxe/rommon/utils

* triggers
    * Removed all usage of deprecated pkg_resources module in favor of importlib.metadata where possible.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added hw-module beacon slot {slot_num} port {port_num} status
        * hw-module beacon slot {slot_num} port {port_num} status
    * Added show firmware version fantray
        * show firmware version fantray
    * Added show logging onboard slot {slot_num} voltage
        * show logging onboard slot {slot_num} voltage
    * Added show logging onboard slot {slot_num} termperature
        * show logging onboard slot {slot_num} temperature
    * Added show platform hardware chassis fantray detail
        * show platform hardware chassis fantray detail
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallUcodeZonepair
        * Added schema and parser for 'show platform hardware qfp active feature firewall ucode zonepair {zone1} {zone2}' command.
    * Added ShowEnvAll
        * Added parser for "show env all" for 9610 platform.
    * Added ShowLoggingOnboardRpUptimeDetail
    * Added parser for Show logging onboard rp active uptime detail command
    * Added ShowIpPimRp
        * show ip pim rp
    * Added parser for ShowIpSsh
        * 'show ip ssh'
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsLoginClear
        * show platform hardware qfp active feature alg statistics login clear
    * Added ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSip
        * show platform hardware qfp active feature alg statistics sip
    * Added parser for ShowPlatformHardwareQfpActiveInfrastructureBqsScheduleOutputDefault
        * 'show platform hardware qfp active infrastructure bqs schedule output default interface {interface}'
    * Added parser ShowSwitch for cat9kv
        * show switch
    * Added ShowPlatformHardwareIomdEthernetControllersPhyHistogram
        * Added parser for 'show platform hardware iomd {iomd} ethernet_controllers phy {phy} histogram'
    * Added ShowPlatformManagementInterface
        * show platform management-interface
    * Added  ShowPlatformSoftwareSubslotModuleFirmware schema and parser
        * Added schema and parser for show platform software subslot {subslot} module firmware
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathPool and ShowPlatformHardwareQfpNatDatapathSessDump schema and parser
        * Added schema and parser for show platform hardware qfp active feature nat datapath pool and show platform hardware qfp active feature nat datapath sess-dump
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathTime schema and parser
        * Added schema and parser for show platform hardware qfp active feature nat datapath time
    * Added Parser for command
        * show platform hardware qfp active feature firewall zonepair {id}
    * Added ShowCryptoPkiServerCrl
        * show crypto pki server {servername} crl
    * Added ShowPlatformHardwareSubslotModuleInterfaceStatistics
        * show platform hardware subslot {subslot} module interface {interface} statistics
    * Added ShowLoggingOnboardRpActiveUptimeDetail
        * Added schema and parser for 'show logging onboard rp active uptime detail' command.
    * Added ShowPlatformSoftwareStatusControlProcessor
        * Added schema and parser for 'show platform software status control-processor' command.
    * Added Parser for parsers for below commands
        * 'show platform software audit monitor status'
        * 'show platform software audit ruleset'
    * Added Schema and Parser for ShowPlatformSoftwareSubslotModuleStatus
        * 'show platform software subslot <subslot> module status'
    * Fixed Parser for Parser for show crypto pki trustpool
        * Added a new schema and parser for the show crypto pki trustpool command.
    * Added parser ShowPlatformSoftwareBPCrimsonContentOper
        * show platform software bp crimson content oper
    * Added Schema and Parser for ShowPolicyMapMultipoint
        * Added 'show policy-map multipoint'
    * Added parser for ShowPlatformHardwareQfpActiveDatapathUtilization
        * 'show platform hardware qfp active datapath utilization'
    * Added parser for 'show fcs-threshold' command
    * Added parser for ShowClassMapTypeInspect
        * 'show class-map type inspect {name}'
    * Added class ShowCryptoDatapathIpv4SnapshotNonZero parser in show_crypto.py
        * Added schema and parser for cli 'show crypto datapath ipv4 snapshot non-zero'
    * Added ShowCryptoEli parser in show_crypto.py
        * Added schema and parser for cli 'show crypto eli'
    * Added ShowDmvpnIpv6
        * Added schema and parser for cli 'show dmvpn ipv6' and 'show dmvpn ipv6 interface {interface}'.
    * Added ShowHosts parser in show_hosts.py
        * Added schema and parser for cli 'show hosts'
    * Modified ShowInterfaceAccount
        * show interface Te0/1/0 acoount
    * Added ShowIpBgpAllLabel parser in show_ip_bgp.py
        * Added schema and parser for cli 'show ip bgp {address_family} all label'
    * Added ShowIpBgpAllLabel parser in show_ip_bgp.py
        * Added schema and parser for cli 'show ip bgp vpnv4 all label'
    * Modified ShowIpMrmInt
        * sh ip mrm int
    * Added ShowNat64Routes
        * show nat64 routes
    * Added parser for ShowPlatformHardwareQfpActiveFeatureFirewallRuntimeRstSegment
        * 'show platform hardware qfp active feature firewall runtime | sec RST segment'
    * Added ShowPlatformHardwareQfpActiveFeatureEssSession parser in show_platform_hardware.py
        * Added schema and parser for cli 'show platform hardware qfp active feature ess session'
    * Modified ShowPlatformHardwareCppActiveFeatureFirewallSession parser in show_platform_hardware.py
        * Modified schema and parser for cli 'show platform hardware cpp active feature firewall session create 1 10'
    * Modified ShowPlatformHardwareQfpActiveFeatureNat66DatapathStatistics
        * show platform hardware qfp active feature nat66 datapath statistics
    * Added ShowPlatformHardwareSubslotModuleHostIfStatistics parser in show_platform_hardware_subslot.py
        * Added schema and parser for cli 'show platform hardware subslot 0/1 module host-if statistics'
    * Added ShowPlatformHardwareSubslotModuleHostIfStatus
        * show platform hardware subslot <subslot> module host-if status
    * Added ShowPlatformSoftwareFirewallRPActiveParameterMaps
        * show platform software firewall RP active parameter-maps
    * Added ShowPlatformSoftwareObjectManagerFpActiveStatistics
        * show platform software object-manager FP standby statistics
    * Added ShowPlatformSoftwareObjectManagerF0PendingAckUpdate
        * show platform software object-manager FP active pending-ack-update
    * Added parser for ShowPlatformSoftwareAccessListFpActiveSummary
        * 'show platform software access list fp active summary'
    * Added parser for ShowPlatformSoftwareNatFpActiveCppStats
        * 'show platform software nat fp active cpp-stats'
    * Added ShowPlatformSoftwareFedSwitchSwcStatistics
        * show platform software fed switch active swc statistics
    * Added ShowPlatformSoftwareFirewallFPActiveParameterMaps parser in show_platform_software.py
        * Added schema and parser for cli 'show platform software firewall FP active parameter-maps'
    * Modified ShowPlatformSoftwareInfrastructureThreadFastpath
        * show platform software infrastructure thread fastpath.
    * Modified ShowPlatformSoftwareNat66RpActivePrefix-translation
        * show platform software nat66 rp active prefix-translation
    * Added ShowPrivilege parser in show_privilege.py
        * Added schema and parser for cli 'show privilege'
    * Added parser for ShowVoiceDspGroupAll
        * 'show voice dsp group all'
    * Modified ShowVoiceDspA
        * show voice dsp a.

* iosxr
    * Added ShowControllersOpticsPRBSInfo parser.
        * Added parser for cli 'show controllers optics prbs-info'.
    * Added ShowControllersOpticsPRBSCapability parser.
        * Added parser for cli 'show controllers optics prbs-capability-info'.
    * Added Parsers for below lslib show commands
        * show lslib server topology-db protocol ospf nlri-type link detail
        * show lslib cache ospf <process_id> links attributes
    * Modified Parsers for below OSPF show commands
        * Modified parser for 'show ospf vrf all-inclusive database opaque-area'
    * Added parser for "show platform security tam device-info" command

* nxos
    * Added MroutepdL3Show
        * dchal module 1 "mroutepd l3 show"
        * Parser for multicast routing protocol daemon L3 information.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified existing Parsers for below ospfv3 show commands to accomodate changes in
        * show ospfv3 topology detail
        * show ospfv3 topology prefixes

* iosxe
    * Modified ShowPolicyMapTypeInspectZonePairSession
    * Added support to Terminating Sessions in addition to Established Session
    * Fixed ShowCryptoPkiServer
        * 'show crypto pki server'
    * Modified ShowMplsLdpNeighbor parser
        * Fix the regex p5 to handle different interfaces
        * Added new regex p8_1 and p8_2 to fetch ldp session details
    * changed one parameter datatype for parser command
        * show platform software fed switch <switch> wdavc function wdavc_ft_show_all_flows_seg_ui
    * Modified ShowPolicyMapTypeInspectZonePair
    * Added support to match new output 0 packets,0 bytes that appear before class_map_action
    * Modified parser ShowUdldNeighbor
        * Updated regex pattern p1 to match the interface name
    * Modified parser ShowPlatformSoftwareCpmSwitchB0ControlInfo
        * Updated regex pattern p3 to make 'Preferred Link' field optional
    * Modified ShowIpv6NhrpSummary
        * updated the regex to parser the nhrp entries with singular form.
    * Modified ShowIpv6NhrpSummary
        * updated the regex to parser the nhrp entries with singular form.
    * Modified ShowInstallState parser
        * Updated the ShowInstallState parser to handle empty output when show install active returns no packages.
    * IE3k
        * Added support to parse LED status for EIP-MOD and EIP-NET in 'show hardware led' command output.
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * Reverted changes made by removing a command from cli_command list.
    * Modified ShowInterfacesTransceiverSupportedlist
        * updated regex pattern p1, p2, and p3 for various output formats.
    * Modified ShowPlatform
        * updated regex pattern p6 for Fatray failures
    * Modified ShowPlatformSoftwareYangManagementProcessState
        * updated regex pattern <p1> for various output formats.
    * Modified ShowCryptoIkev2SaDetail
        * Added keys ake into the schema.
    * Modified ShowDeviceTrackingDatabase
        * 'show device tracking database' - Added support for timeleft in the output parsing.
    * Modified ShowCtsRoleBasedSgtMapAll
        * 'show cts role-based sgt-map all' - Added support for CLI-HI SGT bindings.
    * Modified ShowCtsServerList
        * 'show cts server list' - Added support for parsing server entries without asterisk (*) prefix.
    * Modified ShowIpv6AccessLists
        * 'show ipv6 access-list {acl}'
    * Modified ShowControllerT1
        * 'show controller Serial1/0/0'
    * Modified ShowDiagSubslotEepromDetail
        * 'show diag subslot {subslot} eeprom detail'
    * Modified ShowDmvpn
        * updated the regex to parser ipv6 fields correctly.
    * Modified ShowDmvpnCountStatus
        * fixed the CLI commands with correct format.
    * Modified ShowProcessesCpu
        * 'show processes cpu'
    * Modified ShowTimeRange
        * 'show time-range <name>'
    * Modified ShowPlatformPacketTracePacket
        * 'show platform packet-trace packet {packet_id}'
    * Modified ShowPlatformHardwareQfpActiveFeatureFirewallMemory
        * 'show platform hardware qfp {rpname} feature firewall memory'
    * Modified ShowPlatformHardwareQfpActiveFeatureTdDatapathStatistics
        * 'show platform hardware qfp active feature td datapath statistics'

* genieparser
    * Removed all usage of deprecated pkg_resources module in favor of importlib.metadata where possible.


--------------------------------------------------------------------------------
                                     Added                                      
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPost in iosxe/Cat9k/c9610
        * Added parser for show post


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIdprom
        * show idprom all
    * Updated ShowLispIpv4Publisher parser in show_lisp.py
        * Added support for additional character in 'type' field.


--------------------------------------------------------------------------------
                                    Removed                                     
--------------------------------------------------------------------------------

* iosxe
    * Removed ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbAnyAnyAnyAnyAnyAllAnyDetail
        * 'show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'



genie.telemetry
"""""""""""""""
