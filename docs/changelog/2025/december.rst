December 2025
==========

December 30 - Genie v25.11
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.11
    ``genie.libs.health``, v25.11
    ``genie.libs.clean``, v25.11
    ``genie.libs.conf``, v25.11
    ``genie.libs.filetransferutils``, v25.11
    ``genie.libs.ops``, v25.11
    ``genie.libs.parser``, v25.11
    ``genie.libs.robot``, v25.11
    ``genie.libs.sdk``, v25.11
    ``genie.telemetry``, v25.11
    ``genie.trafficgen``, v25.11




Changelogs
^^^^^^^^^^

genie
"""""

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean-pkg
    * Added support to block copy operations if the target file size does not match.

* rommonboot stage
    * iosxe
        * Removed duplicate task function.
    * cat9k
        * Removed device.destroy() call and added device.sendline() in the rommon boot stage so that the device reaches the rommon prompt.

* clean-pkg/stages
    * Added the reset of the rollup flag when recovery is enabled
    * Updated the api configure_management to able to skip for missing attribute instead of failing complete stages.

* iosxe
    * clean-pkg/utils
        * Fixed issue with updating protected file for image


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean/recover
    * Added power cycle retry mechanism to enhance reliability during device recovery.
    * Updated the console speed configuration in case of failiure connection to device



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* fileserver/protocols/scp.py
    * Added dynamic SCP fileserver protocol support for file transfer operations.


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added HTTPS support for FileTransfer

* iosxr
    * Added HTTPS support for FileTransfer

* nxos
    * Added HTTPS support for FileTransfer



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""

genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe/install
    * Added dialog from failed senario in install one shot
    * Added dialog from failed senario in install one shot

* iosxe/cat9k/c9400
    * Added dialog from failed senario in install one shot

* utils
    * Added get_server_certificate_pem API

* iosxe
    * dns
        * configure_ip_host
            * Added VRF support
        * unconfigure_ip_host
            * Added VRF support

* iosxr
    * dns
        * added configure_ip_host
        * added unconfigure_ip_host
    * pki
        * added configure_trustpoint
        * added unconfigure_trustpoint
        * added configure_pki_authenticate_certificate

* nxos
    * dns
        * added configure_ip_host
        * added unconfigure_ip_host
    * pki
        * added configure_trustpoint
        * added unconfigure_trustpoint
        * added configure_pki_authenticate_certificate


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_bgp_tcpao API
        * API to configure BGP TCP Authentication Option for bgp neighbor
    * Added unconfigure_bgp_tcpao API
        * API to remove BGP TCP Authentication Option for bgp neighbor
    * Added configure_tcp_keychain API
        * API to configure TCP-AO keychain on device
    * Added remove_tcp_keychain API
        * API to remove TCP-AO keychain from device
    * Added configure_bgp_md5 API
        * API to configure BGP MD5 authentication on BGP router
    * Added unconfigure_bgp_md5 API
        * API to unconfigure BGP MD5 authentication on BGP router
    * PKI
        * configure_pki_export_advanced
        * configure_pki_import_advanced
        * change_pki_certificate_hash
    * sdk-pkg
        * Updated configure_management_gnmi api
            * Made default value of 'secure_server' parameter as True.
    * Added configure_bgp_ipv6_dampening
        * New API to configure bgp dampening parameters for IPV6 address family
    * PKI
        * execute_return_crypto_pki_server
    * Added unconfigure_ip_ssh_client_algorithm_kex API support for the CLI command
        * New API support for 'unconfigure ip ssh client algorithm kex' CLI command to unconfigure key exchange algorithms for SSH client on IOSXE devices.
    * Added unconfigure_ip_ssh_server_algorithm_kex API support for the CLI command
        * New API support for 'unconfigure ip ssh server algorithm kex' CLI command to unconfigure key exchange algorithms for SSH server on IOSXE devices.
    * sdk-pkg
        * Updated `configure_management_credentials` and `unconfigure_management_credentials` APIs to use secret password instead of plain text password.
        * Updated `configure_management_ssh` to set modulus size to 4096 bits while generating RSA keys.
    * Added 'execute_test_platform' to iosxe test_platform-execute.py file.
        * New API support for 'test platform' cli.
    * Added API to execute test led cli command
    * Added suport for verify ping api to support new parameters
    * Added execute_test_platform_hardware_sensor_value_cm
        * API to execute_test_platform_hardware_sensor_value_cm
    * Added API get_alarm_contact_relay_mode to retrieve the alarm contact relay mode configuration.
    * Added API get_interfaces_connect_status to retrieve interfaces with connect/not connect status.
    * configure_aaa_group_radius_interface
        * Added support for IPv6 address configuration
        * Added 'protocol' parameter to specify protocol type (default is 'ip')
        * Added 'forwarding' parameter to enable/disable vrf forwarding
    * unconfigure_aaa_group_radius_interface
        * Added support for IPv6 address unconfiguration
        * Added 'protocol' parameter to specify protocol type (default is 'ip')
        * Added 'forwarding' parameter to enable/disable vrf forwarding

* sdk-pkg
    * update ruamel.yaml.clib to avoid break from 0.2.15 release

* apis/utils.py
    * Default to SCP for file copy operations using the copy_from_device and copy_to_device APIs

* nxos/utils
    * Device Boot Recovery


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated api configure_key_config_key_password_encrypt
        * updated api with new dialog pattern
    * Updated api unconfigure_key_config_key_password_encrypt
        * updated api with new dialog pattern
    * Install
        * Added statement in execute_install_one_shot.
        * Added install_timeout to execute_install_activate.
    * cat9k/c9500x
        * Added __init__ file.
    * Modified perform_telnet API
        * Added support to execute command on remote_device before exit the telnet.
    * Added new parameter in API configure_crypto_ikev2_proposal
    * configure_radius_interface_vrf Added support for IPv6 address configuration
        * Added 'protocol' parameter to specify protocol type (default is 'ip')
    * unconfigure_radius_interface_vrf Added support for IPv6 address unconfiguration
        * Added 'protocol' parameter to specify protocol type (default is 'ip')
    * configure_radius_group Added support for IPv6 address configuration
        * Added 'ipv6_addr' in server_config to configure IPv6 address for RADIUS server



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowBgpNeighbors
        * Updated parser and schema for Showbgp neighbour to support tcp aco keychain
    * Modified ShowInterfaces
        * 'show interfaces <interface>'
    * Modified ShowIpVirtualReassemblyInterface
        * 'show ip virtual-reassembly {interface}'
    * Modified ShowCryptoPkiTimerDetail parser
    * Modified ShowPlatformSoftwareInfrastructureThreadFastpath
        * show platform software infrastructure thread fastpath.
    * Modified ShowControllerVDSL
        * 'show controller VDSL {interface}'
    * Modified ShowParameterMapInspectGlobalScema
    * Added Optional keyword for log_flow_export_template_timeout_rate variable to support new cli output
    * Modified ShowKeyChain
        * updated parser and schema for ShowKeyChain parser to support TCP key chain and MACsec Key Table (MKT) features.
    * Modified ShowPlatformHardwareQfpActiveFeatureFirewallDrop
        * 'show platform hardware qfp active feature firewall drop {actions}'
    * Modified ShowRedundancyApplicationGroup
        * Fixed UnboundLocalError by initializing media_active_peer dictionary before use.
        * Added Optional "local" key to active_peer schema.
        * Changed authentication, authentication_failures, reload_peer, resign keys in stats to Optional.
        * Changed all keys in active_peer (pkts, bytes, ha_seq, seq_number, pkt_loss, status, hold_timer) to Optional.
        * Added regex pattern p47 to accommodate "Standby Peer" output lines.
    * Fixed parser ShowPlatformSoftwareFedSwitchActiveIpv6Route
        * Updated handle additional lines in the show platform software fed switch active ipv6 route command.
    * Fixed parser ShowPlatformSoftwareFedActiveIpRoute
        * Updated handle additional lines in the show platform software fed active ip route command.
    * Fixed parser ShowCtsServerList
        * Updated to handle radius server group configuration with IPv6 interface.
    * Fixed parser ShowIpSlaStatistics
        * Updated  handle additional lines in the show ip sla statistics {probe_id} command.

* nxos
    * Modified ShowIsis, ShowIsisAdjacency, ShowIsisHostname, ShowIsisHostnameDetail, ShowIsisInterface
        * Adjust area address regex to account for addresses that are hex or None
        * Adjust schemas to account for valid VRF configurations that do not have all information
    * Modified ShowBgpVrfAllAllSummary
        * Handle cases where BGP neighbor information is spread over 3 lines


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveStpVlan parser
        * show platform software fed switch {switch_num} stp-vlan {vlan_id}
        * show platform software fed active stp-vlan {vlan_id}
    * Added Parser for show ipv6 traffic
        * Added a new schema and parser for the show ipv6 traffic command.
    * Enhanced ShowCtsSxpConnectionsBrief parser.
        * Enhanced parser for cli show cts sxp connections brief.
    * Added ShowCtsSxpSgtMap parser.
        * Added parser for cli show cts sxp sgt-map.
    * Added ShowPlatformHardwareQfpActiveInfrastructurePuntStatisticsTypePerCauseClear
        * 'show platform hardware qfp active infrastructure punt statistics type per-cause clear'
    * Added Parser for show platform software firewall qfp active runtime
        * Added a new schema and parser for the show platform software firewall qfp active runtime command.
    * Added ShowIpv6MfibActive parser in show_mfib.py
        * Added schema and parser for cli 'show ipv6 mfib active'
    * Modified ShowHwModuleSubslotAttribute
        * 'show hw-module subslot {slot} attribute'
    * Added ShowPolicyFirewallStatsGlobal
        * 'show policy-firewall stats global'
    * Added ShowLocateSwitch
        * Added show locate switch parser and tests for IOSXE IE3K platform
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallUcodeScbDetail
        * 'show platform hardware qfp {instance} feature firewall ucode scb a a a a a a a detail'
    * Added showidprom
        * Added parser for "show idprom supervisor eeprom detail"
    * Added ShowDiagSubslotEeprom
    * 'show diag subslot 1/0 eeprom'
    * Added ShowHardwareLed
        * Added show hardware led parser and tests for C9610R platform, revision 1

* nxos
    * Added ShowSystemInternalFlash
        * show system internal flash
    * Modified ShowIpMrouteSummary
        * Updated regex pattern p8 to capture bitrate_unit with optional k/m/g/t prefixes.
        * Added conversion logic to normalize bitrate values to bps format.
    * Modified ShowIpv6MrouteSummary
        * Updated regex pattern p8 to capture bitrate_unit with optional k/m/g/t prefixes.
        * Added conversion logic to normalize bitrate values to bps format.


--------------------------------------------------------------------------------
                                     Added                                      
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareChassisPowerSupplyDetailAll in iosxe/Cat9k/c9550
        * Added parser for show platform hardware chassis power supply detail all
    * Added ShowPlatformHardwareChassisFantrayDetail in iosxe/Cat9k/c9550
        * Added parser for show platform hardware chassis fantray detail


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* iosxe
    * Added new parameters show cloud-mgmt connect
    * Added new parameters show uac uplink, show uac Active-vlan, show uac Active-port


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowCefInterfacePolicyStatistics parser in show_cef.py
        * Modified ShowCefInterfacePolicyStatistics for cli 'show cef interface {interface_name} policy-statistics {direction}'



genie.telemetry
"""""""""""""""
