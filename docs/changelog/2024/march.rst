March 2024
==========

 - Genie v24.3 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 24.3                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 24.3                          |
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

* schemaengine
    * Class Any()
        * Added kwargs to support arguments in Any schema

* ops
    * Modified Base
        * Allow for commands to be passed to learn as strings instead of Parser classes



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean
    * clean
        * add template to not a stage list.

* clean-pkg
    * ncs540/stages
        * Update install_and_replace to use reload instead of execute api

* clean/utils
    * Updated get_clean_template api to load other clean packages using entrypoint.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean/iosxe
    * Updated iosxe generic templates.



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added learn support for show terminal
    * Modified Platform
        * Added label to platform ops model

* iosxr
    * Added learn support for show terminal

* nxos
    * Added learn support for show terminal

* cheetah
    * Added learn support for platform and interface

* platform
    * Cleanup of redundant functions under ios and iosxe to use from utils.common


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* ops
    * Modified Lisp
        * Fixed List Ops and added unittest symlink

* iosxr
    * Platform
        * Update platform tempalte to include device_family from show version for the value of chassis.



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added
        * Added support for <processor_slot> in <request platform software system shell> command.
    * Added upgrade_rom_monitor_capsule_golden
        * upgrade rom-monitor capsule golden switch active R0
    * Added new API `get_cpu_instant_interval` to extract CPU utilization instant and CPU utilization interval.
    * Added new API `get_cpu_min_max_avg` to extract minimum, maximum, and average CPU utilization values.
    * Added API configure_l2_traceroute
        * Added API to configure l2 traceroute
    * Added API unconfigure_l2_traceroute
        * Added API to unconfigure l2 traceroute
    * Added unconfigure_record_configs_from_flow_monitor
        * Added API to unconfigure_record_configs_from_flow_monitor
    * Added unconfigure_flow_exporter
        * Added API to unconfigure_flow_exporter
    * Added new api 'execute_test_cable_diagnostics_tdr_interface'
        * Executes 'test cable disgnostics tdr interface'
    * Added `get_port_speed_info` to retrieve port_speed status for repective interfaces.
    * Added get_interfaces_transceiver_supported_dom API
        * Added API to get the DOM type for the given transceivers list
    * Added new api `verify_last_reload_reason` to verify the Last Reload reason.
    * Added unconfigure_spanning_tree_portfast_on_interface
        * added api to unconfigure_spanning_tree_portfast_on_interface
    * Added new api `get_mac_table_entries` to generate MAC table entries with VLAN, MAC address, interfaces, and their associated VRFs.
    * Added `get_platform_memory_status` to generate VLAN information with VLAN ID, VLAN name, VLAN state and its associated VRFs.
    * Added `get_boot_time` to retrieve boot_time in timeticks format.
    * Added configure_smartpower_interface_level
        * API to configure SmartPower interface level
    * Added unconfigure_smartpower_interface_level
        * API to unconfigure SmartPower interface level
    * Added configure_smartpower_interface_name
        * API to configure SmartPower interface name
    * Added unconfigure_smartpower_interface_name
        * API to unconfigure SmartPower interface name
    * Added configure_smartpower_interface_role
        * API to configure SmartPower interface role
    * Added unconfigure_smartpower_interface_role
        * API to unconfigure SmartPower interface role
    * Added configure_smartpower_interface_domain_default
        * API to configure SmartPower default interface domain

* nxos
    * Added get_standby_supervisor_slot
        * New API to get standby supervisor slot number
    * Added get_active_supervisor_slot
        * New API to get acive supervisor slot number
    * Added get_slots_by_state
        * New API to get list of all the slot/module match the given status
    * Added get_fm_slots
        * New API to get list of FM(Fabric Modules) which match the given status
    * Added get_lc_slots
        * New API to get list of LC(Linecard Modules) which match the given status
    * Added get_current_boot_image
        * New API to get current boot image name
    * Added get_next_reload_boot_image
        * New API to get next reload boot image name


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* blitz
    * Modified verifiers_find_xpath
        * Decoded response Xpath can contain integers as keys, so cast all keys as strings.
    * Modified gnmi_util.GnmiMessage.process_update
        * Decoded response had an extra dict from jsonVal, so corrected logic.

* iosxe
    * Modified config_identity_ibns
        * Modified the api to config_identity_ibns


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_fnf_flow_record
        * Modified API to configure collect configs
    * Modified configure_flow_record_match_datalink
        * Modified API to configure match datalink vlan and ethertypes
    * Modified configure_flow_exporter
        * Modified API to configure export-protocol



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowFlowMonitorCache
        * Added patterns <P34> to <P38> to capture datalink and interface inputs
    * Modified ShowBannerMotd
        * Enhanced parser to capture multiple line messages.
    * Modified ShowInterfaceStatusModule Parser
        * Modified the regular expression for value of vlan to allow not only numbers but also str (i.e. routed), so routed ports can be matched.
    * Modified ShowDiagnosticResultModuleTestDetail Parser
        * Modified the schema to have a new optional key 'port_status'
        * Modified the parser to always use the test name as the index key for the test
    * Modified the show inventory parser.
        * Modified the regexp p1_8 to support the latest changes in 17.15 and to  support the  old  releases.
    * Modified ShowLispPrefixList
        * Added support for parsing additional fields
        * Added support for parsing entry sources as a list
    * Fixed ShowMonitor
        * Fixed regex and support for new attribute Source EFPs
    * Modified ShowLispDatabaseSuperParser
        * Fixed p2 regex to make value optional
    * Modified ShowLispIpMapCachePrefixSuperParser
        * Fixed typo for parsing rloc_probe_in in regex.
    * Modified ShowLispPrefixList
        * Made entries optional in schema.
    * Modified ShowOspfv3NeighborInterface Parser
        * Fix p2 regex to capture when dead time is -
    * Modified ShowAuthenticationSessionsInterfaceDetails Parser
        * Added execute timout of 300 seconds to cater large output
    * Modified ShowPlatformSoftwareFedActiveMonitor Parser
        * fix p2 regex
    * Modified ShowHardwareLed Parser
        * Modified the Metadata for beacon value as optional and added alarm-in3 and alarm-in4 values to support for ie9k devices
    * Modified ShowEeeStatusInterface Parser
        * Added few more optional arguments to the schema.
    * Modified ShowFacilityAlarmStatus
        * Added <p3> and <p4> regex
        * Added key 'index' as optional parameter to schema
    * Modified parser ShowPlatformSoftwareFedIgmpSnooping
        * Enhanced the parser to get Snoop State, Added schema and regex pattern <p1_1>
    * Modified parser ShowPolicyMapControlPlaneClassMap
        * Modified arguments bytes and bps as optional in schema
    * Modified show_vtp_password
        * Enhanced the parser by adding '^VTP +Password +is +configured.$' to each line in the output
    * Fix for TracerouteIpv6
        * Fixed strig split to remove *
    * Added New Parser
        * Added New Parser ShowSmartPowerDomain
        * Added New Parser ShowSmartPowerVersion
    * Modified ShowPlatformTcamPbr
        * Added switch_type same as in iosxe/c9600/c9606r
    * Modified ShowLispPublicationPrefixSuperParser
        * Added support for parsing the same locator from different source addresses.

* nxos
    * Modified ShowAccessListsSummary
        * Modified regex pattern <p1> and <p3> to accommodate various outputs.
    * Modified ShowMacAddressTableBase
        * updated mac_type and age in drop section.

* iosxr
    * Update baud_rate key same as iosxe schema
    * Modified fix for ShowInstallCommitSummary
        * Added schema and code for fix the new output

* iosxe/c9500
    * Modified ShowPlatformFedTcamPbrNat
        * Added switch_type same as in iosxe/c9600/c9606r


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowMeraki
        * added new parser for cli 'show meraki'
        * added new parser for cli 'show meraki connect'
    * Added ShowPlatformSoftwareFedSwitchActiveNatInterfaces
        * Parser for cli 'show platform software fed switch active nat interfaces'
    * Added ShowPlatformSoftwareFedSwitchActiveNatRules
        * Parser for cli 'show platform software fed switch active nat rules'
    * Added ShowL2vpnSdwanAll
        * parser for ShowL2vpnSdwanAll
    * Modified existing Parser
        * Added New 33 and 34 regex
    * c9400
        * Added ShowPost
            * parser for 'show post' on modular platform c9400
    * Added ShowIpSockets
        * parser for 'show ip sockets'
    * Added ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsite Parser.
    * Added ShowDiagnosticStatus Parser.
    * Added ShowPlatformSoftwareFedSwitchActivePuntBrief Parser.
    * Added ShowL2ProtocolTunnelSummary
        * added new parser for cli 'show l2protocol-tunnel summary'
    * Added ShowPlatformHardwareIomdMacsecPortSubport
        * Added parser for show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free" and schema
    * Modified ShowBgpNeighborsAdvertisedRoutes
        * Added show bgp address_family vrf vrf neighbors neighbor advertised-routes to accommodate various outputs.
    * Added ShowPlatformSoftwareIomdMacsecInterfaceDetail
        * Added parser for show platform software iomd {lc_no} macsec interface {port_no} detail and schema
    * Added ShowPlatformHardwareQfpInterfaceIfnamepath parser
        * Parser for "show platform hardware qfp <status> interface if-name <interface> path"
    * Added parser ShowPlatformSoftwareFedSwitchActiveFnfSwStatsShow
        * show platform software fed {switch} {switch_var} fnf sw-stats-show
        * show platform software fed {switch_var} fnf sw-stats-show
    * Added class ShowSdroutingControlLocalPropertiesSummary
        * show sd-routing control local-properties summary
    * Added class ShowSdroutingControlLocalPropertiesWanDetail
        * show sd-routing control local-properties wan detail
    * Added class ShowSdroutingControlLocalPropertiesWanIpv4
        * show sd-routing control local-properties wan ipv4
    * Added class ShowSdroutingControlLocalPropertiesWanIpv6
        * show sd-routing control local-properties wan ipv6
    * Added class ShowSdroutingControlLocalPropertiesVbond
        * show sd-routing control local-properties vbond

* cheetah
    * Updated parsers for ShowInterfacesDot11radio to support vap_rx and vap_tx statistics
    * Added parsers for ShowInterfacesDot11radio, ShowInterfacesWired, ShowVersion

* iosxr
    * Modified Ping
        * Modified regex pattern <p1> to accommodate various outputs.
    * Added ShowSegmentRoutingTrafficEnggPccLsp
        * parser for show segment-routing traffic-eng pcc lsp

* generic
    * Added pid to ShowVersion


--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* ios
    * Added ShowLispInstanceIdService
        * show lisp instance-id {instance_id} {service}
        * show lisp all instance-id {instance_id} {service}
        * show lisp {lisp_id} instance-id {instance_id} {service}
        * show lisp locator-table {locator_table} instance-id {instance_id} {service}



genie.telemetry
"""""""""""""""""
