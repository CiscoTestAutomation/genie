June 2024
==========

 - Genie v24.6 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 24.6                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 24.6                          |
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

* abstract
    * Modified AbstractTree
        * Fixed an issue where a forked process would be created when the `AbstractTree` class was loaded.

* genie.conf
    * Modified parse method
        * Assigning cli as a value to context if it is None
        * Removing connection_alias from kwargs



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified InstallRemoveInactive
        * Modified logic to search image using regular expression in remove_inactive_pkgs
    * Added c9800_cl stages back


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean
    * Added ConfigureInterfaces stage



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* conf
    * Added breakout interface support to IOSXE
    * Added ParsedInterface class


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * configure_interface
        * Add portsec
            * portsec_enable True
            * portsec_count '1025'
            * portsec_violation_mode 'restrict | protect | shutdown'
            * portsec_aging_type 'inactivity | absolute'
            * portsec_type 'static|sticky'
            * portsec_static_mac '001506000001'
            * portsec_static_vlan '1002'
            * portsec_aging_time '5'
        * Add vpc_id
            * port-channel12
                * vpc_id "12"
        * Add vpc_peerlink
            * port-channel10
                * vpc_peer_link True



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* generic
    * Modified deletefile to accept and override command

* iosxe
    * Modified deletefile to add the force option



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * debug
        * configure.py
            * debug_platform_software_fed_switch_active_punt_packet_capture api Added
                * Args
                    * device (obj) Device to execute on
                    * allow_buffer_limit(bool)  if user want to set buffer limit , Default False
                    * buffer_limit(int , optional) Number of packets to capture <256-16384> , Default 16384 (max)
                    * allow_circular_buffer_limit(bool)  if user want to set circular buffer limit , Default False
                    * circular_buffer_limit(int , optional) Number of packets to capture <256-16384> , Default 16384 (max)
                    * allow_set_filter(bool) if user want to set filter , Default False
                    * set_filter_value(str) user input of filter
                    * allow_clear_filter(bool) if user want to clear all filters , Default False
                    * start(bool) starting the capture
                    * stop(bool) stop the capture


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified incomplete_mapper
        * Added support to handle args and kwargs

* ios
    * Modified incomplete_mapper
        * Added support to handle args and kwargs



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fix usage of golden image in recovery
        * Consolidating lookup of golden_image from recovery_info so that it is properly used when defined.
    * Modified configure_rommon_tftp
        * Updated code to handle all possible variation of image handling
    * Modified device_rommon_boot
        * Changed sequence of condition when image is not passed in clean yaml
    * Modified delete_local_file
        * Added timeout to delete_local_file
    * Modified delete_unprotected_files to force delete
    * Modify get_boot_time
        * Added a check to split and parse the uptime_str more robustly by handling the 'hours' and 'minutes' parts individually.
        * Added initialization for hours and minutes to ensure they default to 0 if not found in uptime_str.
    * Modified request_system_shell
        * Added functionality to pass list of commands to execute
    * Fix copy_file API
        * Added timeout optional variable to the copy_file API to allow the user to


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added API config_replace_to_flash_memory_force
        * Added API to configure replace to flash memory force
    * Added `get_power_supply_info` to retrieve power_supply information of respective components under cat9k/c9300
    * udld
        * Added unconfigure_udld_recovery
    * Added configure_interface_dot1q_ethertype
    * Added configure_subinterface_second_dot1q
    * policy_map
        * Added configure_policy_map_set_cos_cos_table
            * command policy-map {policy-map name}
            * command class {class name}
            * command set cos cos table {table name}
    * table_map
        * Added configure_table_map_set_default
            * command table-map {table_map_name}
            * command default {copy or ignore or any value}
    * Added API verify_interface_status_duplex
        * This API is used to verify the interface status duplex
    * Added new API verify_cdp_neighbors_interface
        * Verifies if the CDP neighbors of a device are connected to the specified interface.
    * Added new API get_cdp_neighbor_port_id
        * Added new API to get the port id of the CDP neighbor.
    * Added configure_flow_monitor
        * New API to configure flow monitor
    * Added `get_power_supply_info` to retrieve power_supply information of respective components under cat9k/c9400.
    * Added `get_platform_fan_speed` to retrieve fan_speed of respective fan components under cat9k/c9300
    * Added configure_tunnel_mode_gre_multipoint
        * API for configure tunnel mode gre multipoint
    * Added unconfigure_tunnel_mode_gre_multipoint
        * API for unconfigure tunnel mode gre multipoint
    * Added configure_tunnel_source
        * API for configure tunnel source
    * Added unconfigure_tunnel_source
        * API for unconfigure tunnel source
    * Added configure_ip_nhrp_network_id
        * API for configure ip nhrp network id
    * Added unconfigure_ip_nhrp_network_id
        * API for unconfigure ip nhrp network id
    * Added configure_ip_nhrp_redirect
        * API for configure ip nhrp redirect
    * Added unconfigure_ip_nhrp_redirect
        * API for unconfigure ip nhrp redirect
    * Added configure_ip_nhrp_redirect
        * API for configure ip nhrp redirect
    * Added unconfigure_ip_nhrp_redirect
        * API for unconfigure ip nhrp redirect
    * Added configure_ip_nhrp_map
        * API for configure ip nhrp map
    * Added unconfigure_ip_nhrp_map
        * API for unconfigure ip nhrp map
    * Added configure_ip_nhrp_map_multicast
        * API for configure ip nhrp map multicast
    * Added unconfigure_ip_nhrp_map_multicast
        * API for unconfigure ip nhrp map multicast
    * Added configure_ip_nhrp_nhs
        * API for configure ip nhrp nhs
    * Added unconfigure_ip_nhrp_nhs
        * API for unconfigure ip nhrp nhs
    * Added configure_ip_nhrp_authentication
        * API for configure ip nhrp authentication
    * Added unconfigure_ip_nhrp_authentication
        * API for unconfigure ip nhrp authentication
    * Added configure_nhrp_group
        * API for configure ip nhrp group
    * Added unconfigure_ip_nhrp_group
        * API for unconfigure ip nhrp group
    * Added configure_ip_nhrp_map_multicast_dynamic
        * API for configure ip nhrp map multicast dynamic
    * Added unconfigure_ip_nhrp_map_multicast_dynamic
        * API for unconfigure ip nhrp map multicast dynamic
    * Added new API verify_interface_config_no_speed
        * Added new API to verify interface configuration without speed.


--------------------------------------------------------------------------------
                                    Seconds.                                    
--------------------------------------------------------------------------------



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowLispPlatform
        * Updated the schema to account for new section in show cli output.
    * Modified ShowLispServerSubscriptionPrefix
        * Updated the schema to allow to have optional keys.
    * Modified ShowLispSubscriber
        * Updated the schema and parser to allow to have optional keys.
            * Revision structure incorporated.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* utils
    * Modified unittests.py
        * Enhanced the unittests script to search local folders for a tests folder instead of using the root tests folder with symlinks

* general
    * Cleaned up existing unittests and brought to light a few that were never being picked up

* iosxe
    * Modified ShowMkaStatistics
        * Changed mkpdu-failures key from schema to Optional.
    * Modified ShowFlowMonitorCache
        * Added <datalink_mac_dst_output> key to schema as Optional.
        * Added regex pattern <p39> to accommodate various outputs.
    * Modified ShowIsisRib
        * Changed algo key from schema to Optional.
        * Updated code to accomodate various outputs.
    * Modified fix for ShowLogging
        * Modified patterns p11 regex to match user's data.
    * Modified ShowNtpAssociations
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified fix for ShowDlepClients
        * Modified parser to accomodate various outputs
    * Modified ShowIsisNodeLevel
        * Updated regex pattern p4 to accommodate various outputs.
    * Modified ShowPlatformSoftwareFedSwitchActiveNatFlows
        * Added elif condition to parser 'show platform software fed {switch} {mode} nat flows {flow_based_on}' and 'show platform software fed {switch} {mode} nat flows {flow_based_on} {flow_based_on_value}'
    * Modified ShowPlatformSoftwareFedSwitchMatmStats parser
        * Added cli show platform software fed {act_mode} matm stats
    * Modified ShowLispInstanceIdService
        * Fixed incorrect regex for ETR Map-Server and ITR Map-Resolver
    * Modified ShowModule
        * Added optional variables under module
        * Modified p3 and p4 regex
    * Fixed ShowDiagnosticResultModuleTestDetail parser
        * Fixed one regex pattern to match for all the conditions for 'Show diagnostic result module {mod_num} test {include} detail'
    * Modified fix for ShowMkaPolicy
        * Reverted the name expansion changes introduced in the last PR #3292.
    * Modified fix for ShowInterfaces
        * Modified the Regex pattern p<12> to correctly retrieve the send and receive status and accommodate varios outputs.
    * Modified fix for ShowIsisTopology
        * Modified patterns p5 and p6 to accommodate various outputs
    * Modified ShowSystemIntegrityAllMeasurementNonce parser
        * Updated regex to match LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
    * Modified ShowSystemIntegrityAllComplianceNonce parser
        * Updated regex to match LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
    * Modified ShowSystemIntegrityAllTrustChainNonce parser
        * Updated regex to match LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
    * Modified ShowL2vpnBridgeDomain
        * Added revised version 1 for ShowL2vpnBridgeDomain parser
        * Added <p10> and <p11> regex pattern to decide where to store neighbour values
        * Update <p7> parser to accommodate various outputs

* nxos
    * Modified ShowFex
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowLldpNeighbors
        * Changed <interfaces> key from schema to Optional.

* iosxr
    * Modified ShowBgpAddressFamily
        * New Show Command - show bgp {address_family} community {community}
        * New Show Command - show bgp {address_family} community {community} {exact_match}
        * Updated regex for handling IPv6 adresses/prefixes
        * Updated regex pattern for handling new lines in IPv6 address family output
    * Modified ShowBgpVrfAfPrefix
        * adding new schema key srv6_pn_sid
        * adding new line p1_1 regex
        * adding p1_1 parser
    * Fixed ShowOspfInterface
        * Modified the p5 regex to handle optional field `cost`.
    * Modified fix for ShowVlanId
        * Modified parser to accomodate various outputs
    * Modified Traceroute
        * Added support for new traceroute command

* sonic
    * Modified ShowVersion
        * Refactored the code to current standard

* modified showplatformsoftwarefedswitchactivelearningstats parser
    * Added cli show platform software fed {rp} learning stats

* added regex for parsing itr map-resolver reachability, prefix-list and etr map-server doman-id and last map-register info.

* common
    * Modified format_output
        * Updated sorted function to sort the data in string and integer order
    * Modified _load_parser_json
        * Updated code to use correct variables


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added class ShowPtpForeignMastersInterface
        * Parser for show ptp foreign-masters {interface}
    * Added ShowOspfProcessIdVrfName
        * parser for 'show ospf {process_name} vrf {vrf_name} interface {interface}'
    * Added class ShowPoolAddressFamilyPool
        * show pool {address_family} name {pool_name}
    * Added show frequency synchronization interfaces brief
        * parser for 'show frequency synchronization interfaces brief'

* iosxe
    * Updated ShowRomvar
        * Added support to parse switch_ignore_startup_config.
    * Added ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus
        * Added schema and parser for 'show platform hardware fed switch {mode} npu slot 1 port {port_num} port link_status'
    * Added ShowPlatformTcamUtilization
        * Added schema and parser for 9350 'show platform hardware fed active fwd-asic resource tcam utilization'
    * Added ShowMonitorCaptureStatistics
        * Added schema and parser for 'show monitor capture {capture_name} capture-statistics'
    * Added TestPlatformHardwareFepSwitchDumpStatistics
        * Added 'test platform hardware fep switch {switch_num} {fep_slot} dump-statistics' cat9k/c9300.
    * Added ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceIsisSchema
        * Added parser for "show platform software cpm switch active B0 counters interface isis" and schema
    * Modified ShowPlatformSoftwareCpmSwitchB0CountersPuntInject
        * Updated to support timestamps  in the output
    * Added ShowDeviceTrackingDatabase
        * Added timeout 300 to parse bigger output
    * Added ShowLispInstanceIdIpv4MapCache
        * Added timeout 300 to parse bigger output
    * Added ShowLispInstanceIdIpv6MapCache
        * Added timeout 300 to parse bigger output
    * Added ShowLispServiceDatabase
        * Added timeout 300 to parse bigger output
    * Added ShowLispEthernetMapCache
        * Added timeout 300 to parse bigger output
    * Added ShowLispEidTableServiceDatabase
        * Added timeout 300 to parse bigger output
    * Added ShowPlatformSoftwareFedSwitchActiveNatPools
        * Parser for cli 'show platform software fed switch active nat pools'
    * Added ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added schema and parser for 9350 'show platform show platform software fed switch active acl info db detail'

* nxos
    * Added show_ngoam.py
        * added new parser for cli 'show ngoam loop-detection status'
        * added new parser for cli 'show ngoam loop-detection summary'
    * Modidy show_vxlan.py
        * Fixed parser for ShowRunningConfigNvOverlay to include peer-ip command
    * Added ShowVlanCounters
        * added new parser for cli 'show vlan counters'
        * added new parser for cli 'show vlan id <id> counters'

* sonic
    * Added ShowPlatformInventory parser
        * show platform inventory
    * Added ShowInteraces
        * show interfaces transceiver eeprom



genie.telemetry
"""""""""""""""""
