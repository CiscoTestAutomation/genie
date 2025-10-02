September 2025
==========

September 30 - Genie v25.9 
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v25.9 
    ``genie.libs.health``, v25.9 
    ``genie.libs.clean``, v25.9 
    ``genie.libs.conf``, v25.9 
    ``genie.libs.filetransferutils``, v25.9 
    ``genie.libs.ops``, v25.9 
    ``genie.libs.parser``, v25.9 
    ``genie.libs.robot``, v25.9 
    ``genie.libs.sdk``, v25.9 
    ``genie.telemetry``, v25.9 
    ``genie.trafficgen``, v25.9 




Changelogs
^^^^^^^^^^

genie
"""""

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* stages/iosxe
    * connect
        * Added optional logout argument (default True) to accommodate various scenarios.

* iosxe
    * Modified InstallImage
        * Added logic to handle ISSU in progress scenario.
    * Fixed the logic of InstallRemoveSmu stage and added support to handle uncommitted SMU images

* clean
    * IOSXE/cat9k
        * Update clean install images to use execute service and pass install timeout.
    * IOSXE/cat9k
        * Update clean install images to do configure no boot manual on the device.

* iosxe/cat9k/install_image
    * Added 'rommon_vars' to install_image stage to support setting rommon variables when booting an image in rommon mode.

* iosxe/install_image
    * add image_to_boot to install image

* clean-pkg
    * Fix syntax warning
    * Added support for matching interfaces by alias in ConfigureInterfaces.

* iosxe/connect
    * Removed duplicate configure boot manual in connect stage.



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* conf-pkg
    * Fix syntax warning

* nxos
    * Added support for 2 new clis
        * Added frr anycast source ip support in conf model
        * Added ead-evi route support in conf model
    * Modified
        * update issu trigger command to `min-disruptive` based on marketing feedback.



genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health-pkg
    * Fix syntax warning



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
    * Added execute_test_platform_hardware_sensor_value
        * API to execute_test_platform_hardware_sensor_value
    * Added enable_cts_sxp
    * Added disable_cts_sxp
    * Added configure_cts_sxp_default_password
    * Added unconfigure_cts_sxp_default_password
    * Added enable_cts_sxp_connection
    * Added disable_cts_sxp_connection
    * Added API to get the maximum and minimum temperature from the device alarm settings.
    * cat8k
        * Added api to configure no boot manual
    * c8kv
        * Added api to configure no boot manual
    * Added execute_clear
        * API to execute clear {parameter}
    * Added API configure_ipv6_cef
    * Added API unconfigure_ipv6_cef
    * Modified API `configure_standard_access_list`
        * Made 'wild_mask' as optional argument.
    * Modified API `unconfigure_standard_access_list`
        * Made 'wild_mask' as optional argument.
    * Added API to configure/unconfigure Relay mode negative
    * Added API test_platform_hardware_powersupply_oir
        * Added API for doing PSU OIR
    * cat9kv
        * Added API test_platform_hardware_chassis_fantray_action
        * Added API configure_autolc_shutdown_priority
    * Added clear_cts_environment_data
        * API to clear cts environment-data
    * Modified configure_ip_role_based_acl
        * Added support for source and destination port range
    * Added API unconfig_trust_points
        * Added API to unconfig_trust_points
    * IKE
        * configure_isakmp_key_simple
        * unconfigure_isakmp_key_simple
    * Added API execute_hw_module_beacon_fan_tray
    * Added API execute_hw_module_subslot_oir
    * Added API configure_platform_ip_multicast_ssdp
    * Added API unconfigure_platform_ip_multicast_ssdp
    * Added API to configure alarm profile
    * Added API to unconfigure alarm profile
        * Added support for configuring alarm profiles with options such as contact, severity, description, name, trigger, and type.
        * The API allows setting the configuration options to 'no' and specifying the expected settings for power supply alarms.
        * Added support for configuring and unconfiguring notifications for alarm profiles.
        * Added support for configuring and unconfiguring relay settings for alarm profiles.
        * Added support for configuring and unconfiguring syslog settings for alarm profiles.
    * Added API configure_extended_access_list
        * Added API to configure_extended_access_list
    * Added API configure_ptp_ttl
    * Added API unconfigure_ptp_ttl
    * Added execute_trim_crypto_pki_certificate
        * API to execute_trim_crypto_pki_certificate
    * Added config API configure_ikev2_disconnect_revoked_peers
    * Added API to configure facility alarm temperature primary
        * Added support for configuring the primary temperature threshold for facility alarms.
        * The API allows setting the temperature threshold to 'high' and specifying the value.
    * Added API to unconfigure facility alarm temperature primary
        * Added support for unconfiguring the primary temperature threshold for facility alarms.
        * The API allows removing the temperature threshold configuration.
        * Added support for configuring and unconfiguring notifications for primary temperature alarms.
        * Added support for configuring and unconfiguring relay settings for primary temperature alarms.
        * Added support for configuring and unconfiguring syslog settings for primary temperature alarms.
    * Added API configure_with_submode
        * Added API to configure_with_submode
    * Added API configure_with_submode
        * Added API to configure_with_submode

* iosxe/cat9k
    * c9400
        * Added new api to execute config register


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fixed issue with 'question mark' not working in certain command modes.
    * Unconfigure_banner
        * Added fix for Unconfigure_banner to make it compatible
    * Modified
        * Added support for handling reload triggered by `%PMAN-5-EXITACTION reload action requested`

* sdk-pkg
    * Fix syntax warning

* iosxe/sdk-pkg
    * Updated the configure management vrf api


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Added logic for to execute log messages
        * Added logic for to execute log messages beased on the edit operations
    * Modified unconfigure_modify_ikev2_profile
        * Modified the api unconfigure_modify_ikev2_profile
    * Modified configure_radius_group
        * Modified the configure_radius_group to add changes for ipv6 source interface.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added parser for ShowMonitorEventTraceCryptoIpsecEventAll
        * 'show monitor event-trace crypto ipsec event all'
    * Added ShowPlatformHardwareQfpActiveFeatureIpsecSa3
        * Added schema and parser for 'show platform hardware qfp active feature ipsec sa 3'
    * Added  ShowIdpromFantrayEepromDetail schema and parser
        * Added schema and parser for show idprom fan-tray {fantray_num} eeprom detail
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallDrop
        * show platform hardware qfp active feature firewall drop
        * show platform hardware qfp active feature firewall drop all
        * show platform hardware qfp active feature firewall drop clear
        * show platform hardware qfp active feature firewall drop verbose
    * Added ShowL2tp
        * show l2tp
    * Added ShowPlatformHardwareQfpActiveFeatureNatDatapathGate parser.
        * Added parser for cli 'show platform hardware qfp active feature nat datapath gatein'.
        * Added parser for cli 'show platform hardware qfp active feature nat datapath gateout'.
    * Modified ShowInterfacesTransceiverSupportedlist
        * Added new Cisco p/n min format parser for show interfaces transceiver supported list
    * Added ShowMonitorEventTraceCryptoAllDetail Parser for
        * Parser for 'show monitor event-trace crypto all detail'
    * Added ShowMonitorEventTraceCryptoFromBoot Parser for
        * Parser for 'show monitor event-trace crypto from-boot'
        * Parser for 'show monitor event-trace crypto from-boot {timer}'
    * Added Parser for show platform hardware cpp active system state
        * Added a new schema and parser for the show platform hardware cpp active system state command.
        * Supports parsing CPP system state information including component status, platform state, HA state, client state, image information, load count, active threads, and fault manager flags.
        * Handles component initialization status (cpp_cp, cpp_sp, FMAN-FP, cpp_driver0).
        * Parses hierarchical state information with proper data type conversion.
    * Added ShowVlans
    * 'show vlans <vlan-id>'
    * Added  ShowPlatformHardwareQfpActiveFeatureNatDatapathEsp schema and parser
        * Added schema and parser for show platform hardware qfp active feature nat datapath esp
    * Added ShowPlatformHardwareChassisRpFanSpeedControlData
    * Added parser for Show Platform Hardware Chassis Rp FanSpeedControlData
    * Added parser for hw-module beacon fan-tray fantray_num status
    * Added ShowX25Vc parser in show_x25.py
        * Added schema and parser for cli 'show x25 vc'
    * Added ShowPlatformSoftwareNatFpActiveMappingStatic
        * Added ShowPlatformSoftwareNatFpActiveMappingStaticSchema
        * Added parser for "show platform software nat fp active mapping static"
    * Added ShowCefTableConsistencyCheck parser in show_cef.py
        * Added schema and parser for cli 'show cef table consistency-check'
    * Added parser for ShowAlignment
        * 'show alignment'
    * Added ShowMkaSessionDetail
        * show mka session detail
            * *New**
    * Added** ShowCtsCredentials *parser.**
        * Added parser for cli 'show cts credentials'.**
    * Added ShowRunningConfigVrf
        * show running-config vrf
    * Added ShowPlatformHardwareQfpActiveFeatureFirewallRuntime
        * show platform hardware qfp active feature firewall runtime
    * Added ShowPlatformSoftwareFirewallRPActiveZones
        * sh ipv6 mfib {group} active
    * Modified ShowVoiceDsp
        * show voice dsp
    * Added ShowPlatformHardwareQfpActiveFeatureTdDatapathStatistics parser
        * Added schema and parser for 'show platform hardware qfp active feature td datapath statistics'
    * Added ShowPlatformHardwareQfpActiveFeatureEvcClientL2cpActionsInterface
    * 'show platform hardware qfp active feature evc client l2cp-actions interface GigabitEthernet0/0/4.EFP1'
    * Added ShowRomMonitor parser in show_romvar.py
        * Added schema and parser for cli 'show rom-monitor 0'
    * Added ShowIpBgpNeighborReceivedPrefixFilter schema and parser
        * Added schema and parser for show ip bgp neighbors {neighbor} received prefix-filter and show ip bgp {address_family} vrf {vrf} neighbors {neighbor} received prefix-filter
    * Added ShowPlatformHardwareChassisFantrayDetailAll
        * Added parser for "show platform hardware chassis fantray detail all"
    * Added ShowPowerDetail
        * Added schema and parser for'show power detail' under 9610c folder for iosxe

* iosxr
    * Added `ShowSubscriberSessionAllSummary` Parser
        * Added schema and parser for `show subscriber session all summary` command.
    * Added Parsers for below OSPFv3 show commands
        * show ospfv3 vrf all-inclusive database ext-router
        * show ospfv3 topology detail
        * show ospfv3 topology prefixes
    * Added Parsers for below lslib_server show commands
        * show lslib server producer detail
        * show lslib server producer {name} instance-id {id}
        * show lslib server topology-db protocol ospfv3 instance-id {id} nlri-type node detail
        * show lslib server topology-db protocol ospfv3 instance-id {id} nlri-type link detail
        * show lslib server topology-db protocol ospfv3 instance-id {id} nlri-type ipv6-prefix detail

* nxos
    * Added ShowKeyChain parser.
        * Added parser for cli show key chain {key_chain_name}.
        * Added parser for cli show key chain {key_chain_name} detail.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Added fix for ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableDef parser.
        * Added this fix to support multiple acl_entries.
    * Modified ShowInterfaceEtherchannel
        * 'show interface {interface_id} etherchannel'
    * Modified ShowInterfaces
    * 'show interfaces Serial0/3/1'
    * genie.libs.parser.iosxe.rv1.show_platform
        * Added regex to parse platform output when model, hw_ver and sw_ver are N/A
    * Modified ShowPolicyMapTypeInspectZonePairSessions
        * 'show policy-map type inspect zone-pair sessions'
    * Modified ShowPlatformPacketTracePacket
        * 'show platform packet-trace packet {packet_id}'
    * Added YANG parser for ShowSystemIntegrityAllCompliance
    * Modified ShowPlatformHardwareAuthenticationStatus
        * Added missing optional attributes to schema for 10-slot chassis.
    * Modified ShowStandbyAll parser
        * Updated regex for the state changes line and improved parsing of the last state change time to accommodate various output formats.

* iosxr
    * Modified ShowPlatform for `ASR-9903` with `IOS-XR v7.8.2`
        * Updated regex pattern <p1> to accommodate various outputs
            * Changed whitespace before <plim> to use \s+ (was a single space) for variable spacing.
            * Made <config_state> optional by wrapping it in a non-capturing group.
        * Ensures lines without a "Config state" column are parsed (e.g., `0/0/1             A9903-20HG-PEC             OK`).

* nxos
    * Fixed ShowEnvironmentPowerDetail parser.
        * Fixed parser for cli show environment power detail.


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified show environment power cache parser in iosxe/ie3k
        * Modified parser for show environment power in iosxe/ie3k
    * Updated ShowUACUplinkDB parser
        * Added support for "IPV4 Preferred Uplink" and "IPV6 Preferred Uplink".
        * Added support for optional "Allowed" field in interface tables.
        * Improved parsing logic for various output formats.
    * Modified ShowIpRouteWord parser
        * Fixed p5 where the parser was not correctly handling routes with specific keywords such as "directly connected" and "via".
        * Fixed p8 where the parser was not correctly capturing the metric and next-hop information for certain route types.
    * Modified ShowIpPolicy parser
        * Added support for IPv6 policy parsing in addition to existing IPv4 policy parsing.

* fix resolve syntaxwarnings from invalid escape sequences
    * Updated regex patterns to use raw strings (r"...") or escaped backslashes
    * Eliminated SyntaxWarnings (e.g., '\d', '\S') during runtime


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowEnvironmentAlarmContact in iosxe/ie3k
        * Modified parser for "show environment alarm-contact" in iosxe/ie3k



genie.telemetry
"""""""""""""""
