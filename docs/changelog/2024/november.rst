November 2024
==========

November 26 - Genie v24.11
------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v24.11
    ``genie.libs.health``, v24.11
    ``genie.libs.clean``, v24.11
    ``genie.libs.conf``, v24.11
    ``genie.libs.filetransferutils``, v24.11
    ``genie.libs.ops``, v24.11
    ``genie.libs.parser``, v24.11
    ``genie.libs.robot``, v24.11
    ``genie.libs.sdk``, v24.11
    ``genie.telemetry``, v24.11
    ``genie.trafficgen``, v24.11




Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* conf.base
    * Modified Device.parse
        * Added `revision` keyword argument

* conf
    * base/api.py
        * Handle images to be part of kwarg_to_dict



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean-pkg
    * iosxe
        * Added default `LOAD_IMAGE` template
    * iosxe
        * image_handler
            * check if smu image is passed instead of base image in the image list
        * Skip `install_image` if smu only image passed.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* stages/iosxe
    * install image
        * Ensure startup config is verified if install image is skipped.
    * install image
        * Updated _check_for_member_config to handle install image stage.

* iosxe
    * Modified clean stages
        * Fixed the usage of steps in the clean stages to ensure correct result rollup
    * Modified copy_to_device
        * Skip verifying free space on the device if skip_deletion is set to True

* apic
    * Modified copy_to_device
        * Skip verifying free space on the device if skip_deletion is set to True

* generic
    * Modified copy_to_device
        * Skip verifying free space on the device if skip_deletion is set to True

* recovery
    * Modified recovery_processor
        * Removed unused params from docstring



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added
        * neighbor <neighbor_id> \ bfd multihop
    * Added associate_vrf_name attributes under vlan
        * associate_vrf_name = 'vxlan-1001'
    * Added
        * enabled redistribute AM routes
        * router bgp <ASN> \ address-family ipv4|ipv6 unicast \ redistribute am route-map <user defined route map>


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ipv6addr.py
        * changed route_tag type to str from bool to read the route_tag values
    * Modified ipv4addr.py
        * Modified 'tag' to 'route_tag' for configuring route_tag
    * Modified route_policy.py
        * Reading 'match_tag' for configuring match_tag under route policy



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
    * Added API execute_test_sfp_port_lpn_fake_insert
        * Added API to execute_test_sfp_port_lpn_fake_insert
    * Added API execute_test_sfp_port_lpn_fake_remove
    * Added API platform_hardware_fed_switch_phy_debug
        * Added API to platform_hardware_fed_switch_phy_debug
    * Added API debug_software_cpm_switch_pcap
        * Added API to enable disable software cpm switch
    * Added API's to configure cli commands for policy-map.
        * API to configure_policy_map_with_police_cir_percentage
        * API to configure_policy_map_parameters
    * Added API's to configure cli commands for speed auto.
        * API for configure_interface_speed_auto
    * Added execute_diagnostic_start_switch_port
        * API to execute_diagnostic_start_switch_port
    * Added execute_test_platform_hardware_cman
        * API to execute_test_platform_hardware_cman
    * Added request_platform_hardware_pfu
        * API to request_platform_hardware_pfu
    * Added remove_default_ipv6_sgacl
        * API to clear default IPv6 SGACL
    * Added API request_platform_software_trace_rotate_all
        * Added request_platform_software_trace_rotate_all api
    * Added set_platform_soft_trace_ptp_debug
        * added api for set platform software trace fed active ptp_proto debug
    * Added unconfigure_parameter_map_subscriber
        * API to unconfigure "parameter-map type subscriber attribute-to-service {parameter_map_name}"
    * Added unconfigure_policy_map_set_cos_cos_table
        * New API to unconfigure policy map set cos cos table

* added api to execute_test_sfp_port_lpn_fake_remove


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* api utils
    * Modified api_unittest_generator
        * Refactored code to streamline `configure` and `execute` API unit tests
        * Removed dependency on mock data yaml files for `configure` and `execute` API unit tests

* iosxe
    * health cpu api
        * Update the API to handle the scenario when the parser dont has the key
    * Modified verify_ignore_startup_config
        * fixed next_config_register Key Error
    * Health
        * Update the health cpu to include `show processes cpu platform` command
    * Modified configure_masked_unmasked_credentials
        * Added parameter view
    * Modified
        * Updated execute_install_one_shot to use reload service instead of execute
    * Recovery
        * Modified send_break_boot to send context with username, password and enable_password

* sdk-pkg
    * Update load_image api in utils.py



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowSoftwareAuthenticityRunning
        * Added schema and parser for 'show software authenticity running'
    * Added ShowPlatformHardwareFedXcvrRegisters parser
        * Added parser for cli show platform Hardware Fed XCVR Registers
    * Added ShowPlatformHardwareFedSwitchActiveNpuSlotPortRecreate parser
        * Added parser for cli show platform Hardware NPUSlot PortCreate
    * Added `ShowPlatformSoftwareFedSwitchActiveIfmMappingsL3if_le` parser.
    * Added parser for CLI `show platform software fed switch active ifm mappings l3if-le`.
    * Added ShowPlatformSoftwareFedSwitchNumberIfmMappingsPortLE parser.
        * Added parser for CLI `show platform software fed switch active ifm mappings port-le`.
    * Added ShowDnsLookup Parser in show_dns_lookup.py
        * show dns-lookup cache
        * show dns-lookup hostname {hostname}
    * Added ShowControllerEthernetControllerInterfaceMac parser
        * Added parser for cli show controller interface mac
    * Added ShowIdpromEeprom parser
        * Added parser for cli show idprom all eeprom
    * added ShowPlatformSoftwareFedPuntEntriesInclude Parser
        * parser for show platform software fed {switch} {port_num} punt entries | include {match}
    * Added ShowPlatformSoftwareFedSwitchActiveStatisticsInit parser.
        * Added parser for CLI 'show platform software fed switch active statistics init'
    * Added revision1 for ShowProcessesCpuPlatformSorted parser.
        * Added revision1 for CLI `show processes cpu platform sorted`.
    * Added ShowPlatformSoftwareFedSwitchActiveCpuInterfaces parser.
        * Added parser for CLI `show platform software fed switch active cpu-interfaces`.
    * Added ShowPlatformSoftwareWiredClientID parser.
        * Added parser for cli 'show platform software wired-client {client_id}'.

* utils
    * Added revision keyword and handling to get_parser.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified fix for golden_output_expected.py
        * fixed the regex spaces fixes
    * Modified fix for show_platform_software_fed.py
        * removed unnecessary blank lines
        * added pattern as a comment for regex
        * conflict for show_platform_software_fed.py resolved
        * test commit done
        * added comment for match line
    * Modified fix for ShowIdprom.
        * Modified the key value as optional to accomodate various outputs.
    * Modified fix for ShowLispDatabaseConfigPropSuperParser
        * Modified the regex patterns <p3> to accommodate different output.
    * Modified ShowIpNbarVersion
        * made file and creation_time optional
    * Modified fix for ShowPolicyMapInterface
        * added rate_bps and burst_bytes under child policy-name section.
    * Modified ShowIpIgmpSnoopingGroups
        * Modified <vlan_id>, <type>, <version> and <port> in the schema as Optional.
        * Added regex pattern <p1_0> to accommodate various outputs.
    * Modified ShowLispExtranet
        * Changed <home_instance>, <total> from schema to Optional.
    * Modified ShowPlatformSoftwareCpmCountersInterfaceIsis
        * Added BP  command for the same schema and output.
    * Modified ShowPlatformSoftwareCpmSwitchB0CountersPuntInject
        * Added BP command for the same schema and output.
    * Modified ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceLacp
        * Added BP command for the same schema and output.
    * Modified ShowPlatformSoftwareCpmSwitchB0CountersDrop
        * Added BP command for the same schema and output.
    * Update revision1 for ShowProcessesCpuPlatformSorted parser.
        * Made cpu_utilization, five_sec_cpu_total, one_min_cpu, five_min_cpu optional.

* viptela
    * Modified ShowControlConnections
        * Updated regex pattern <p1> to accommodate string length changes in rows.
    * Modified ShowIpRoutes
        * Updated regex pattern <p1> to accommodate the nh_if_name column running into the nh_addr column.
    * Modified ShowOmpPeers
        * Updated regex pattern <p1> to accommodate tenant id and region id.
    * Modified ShowSystemStatus
        * Updated regex pattern <p10> to accommodate matching key values correctly when additional colons are in values.

* iosxr
    * Modified ShowLacp
        * Changed <rate> key from schema to Optional.
        * Updated regex pattern <p1> and <p2> to accommodate various outputs.

* nxos
    * Modified ShowIpIgmpGroups
        * Updated regex pattern <p2> and <p3> to accommodate various outputs.
    * Modified ShowPimRp
        * Updated regex pattern <p8_3> to accommodate various outputs.
    * Modified ShowIpv6MldGroups
        * Updated regex pattern p4, p6 and p7 to handle white space.
        * Modified line.strip() to rstrip().
        * Modified the logic to handle different output

* common
    * Modified _fuzzy_search_command and _is_regular_token functions to make it work for commands which contains arguments inside parenthesis.



genie.telemetry
"""""""""""""""
