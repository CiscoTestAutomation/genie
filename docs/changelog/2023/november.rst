November 2023
==========

November 27 - Genie v23.11
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 23.11                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 23.11                         |
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

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* clean
    * clean.py
        * Updated import to get BaseCleaner from pyats.clean

* iosxe
    * Implemented image_override setting for copy_to_linux and copy_to_device clean stages

* clean/stages/iosxe/stages.py
    * Updated image mapping logic for Copytodevice stage



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added macsec conf
        * added macsec cli for conf model


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * keychain
        * fixed typo for crypto algorithm AES_256_CMAC



genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * platform
        * fixed issue where new lc type without `ethernet` in the name would be incorrectly categorized as a `oc` slot type.



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      Add                                       
--------------------------------------------------------------------------------

* linux
    * Added API get_snmp_snmpwalk_version3
        * API added to 'snmpwalk -v {version} -u {username} {passprs} {passphrase} {var} {security_level} {security} {security_method}'
    * Added API  configure_pki_authenticate_certificate
        * API added to configure_pki_authenticate_certificate(certificate={cert}, label_name={tp1_name})


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added unconfigure_interface_speed
        * New API to unconfigure interface speed
    * Added clear_ipv6_neighbors
        * New API to clear ipv6 neighbors
    * Added unconfigure_filter_vlan_list
        * API for unconfigure filter vlan list
    * Added configure_access_map_match_ip_mac_address
        * API for configure access map match ip mac address
    * Added configure_acl_protocol_port
        * API for configure acl protocol port
    * Added configure_ip_acl_with_any
        * API for configure ip acl with any
    * Added configure_shutdown_vlan_interface_range
        * API to shut the vlan interface range {vlan_id_from}-{vlan_id_to}
    * Added configure_no_shutdown_vlan_interface_range
        * API to unshut the vlan interface range {vlan_id_from}-{vlan_id_to}
    * Added execute_crypto_pki_server
        * added api to execute crypto pki server
    * Added execute_test_opssl_nonblockingsession_client
        * added api to  execute opssl nonblockingsession client
    * Added execute_test_opssl_nonblockingsession_server_stop
        * added api to execute opssl nonblockingsession server stop
    * Added execute_test_opssl_nonblockingsession_server_start
        * added api to execute opssl nonblockingsession server start
    * Updated configure_pki_trustpoint
        * Updated configure pki trustpoint
    * Added configure_spanning_tree_mst_priority
        * New API to configure spanning tree mst priority
    * Added hw_module_sub_slot_reload
        * added api to hw_module_sub_slot_reload
    * Added configure_ospf_vrf_lite
        * New API for configuring vrf-lite capabilty under OSPF {ospf_process_id}
    * Added unconfigure_time_range
        * API to unconfigure time-range
    * Added configure_device_tracking_logging
        * API to configure device tracking logging
    * Added unconfigure_device_tracking_logging
        * API to unconfigure device tracking logging
    * Added configure_object_group
        * API to configure object group
    * Added configure_telemetry_ietf_parameters
    * Added unconfigure_ip_dhcp_snooping_limit_rate
        * API for unconfiguring dhcp snooping rate limit
    * Added configure_ip_dhcp_snooping_verify_mac_address
        * API for configuring dhcp snooping verify mac_address
    * Added unconfigure_ip_dhcp_snooping_verify_mac_address
        * API for unconfiguring dhcp snooping verify mac_address
    * Added configure_dhcp_snooping_verify_no_relay_agent_address
        * API for configuring dhcp snooping verify no_relay_agent_address
    * Added unconfigure_dhcp_snooping_verify_no_relay_agent_address
        * API for unconfiguting dhcp snooping verify no_relay_agent_address
    * Added configure_dhcp_snooping_track_server_dhcp_acks
        * API for configure dhcp snooping track server dhcp-acks
    * Added unconfigure_dhcp_snooping_track_server_dhcp_acks
        * API for unconfigure dhcp snooping track server dhcp-acks
    * Added enable_cpp_system_default_on_device
        * New API to enable cpp system-default on device
    * Added enable_switchport_protected_on_interface
        * New API to enable switchport protected on interface
    * Added clear_ip_pim_rp_mapping
        * New API to clear ip pim rp-mapping
    * Added configure_event_manager
        * API to configure event manager with applet name
    * Added execute_event_manager_run_with_reload
        * API to execute event manager with embeded applet name
    * Added get_snmp_snmpwalk_sysname
        * API to get snmp snmpwalk sysname description

* added execute_clear_control_plane
    * New API to execute clear control-plane all on device


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modify configure_pki_export
        * added return vlaue as self signed  certificate
    * Modify api configure_pki_enroll
        * added the serial number in subject name as an argument
    * Modified execute_reload_fast
        * Modified the exeute_reload_fast API
    * Modified execute_install_one_shot
        * Modified the execute_install_one_shot API to upgrade the image using reloadfast
    * Modified request_system_shell
        * Fixed the dialog,added new statement to handle shell prompt.
    * Modified platform exclude values for reload.py trigger
    * Modified platform exclude values for switchover.py trigger

* genie.libs.sdk
    * Modified process_sequencial_operational_state to set sequence to False as we are no longer trimming reponses

* blitz
    * Fix to enclose list entries within square brackets when building GNMI request
    * changed reference of "try_lock" function from yangexec to netconf_util.
    * Modified configure_replace action
        * added 'timeout' argument
    * Modified restore_config_snapshot action
        * added 'timeout' argument
    * Modified save_config_snapshot action
        * added 'timeout' argument
    * Modified
        * Netconf subscriptions were not tracked and did not account for multiple streams.
    * Fixed negative test handling for netconf.

* linux
    * Modify kill_processes API
        * added `sudo` argument

* processor
    * Modified check_memory_leaks processor for IOSXE
        * added 'timeout' argument

* abstracted_libs
    * Modified restore_configuration function
        * added 'timeout' argument
    * Modified save_configuration function
        * added 'timeout' argument

* utils
    * Modified copy_to_device/copy_from_device to support obtaining proxy device from servers section



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformSoftwareFedSwitchActiveIFMInterfacesSVI
        * Added schema and parser for 'sh platform software fed {switch} {active} ifm interfaces svi'
    * Added ShowPlatformSoftwareFedSwitchActiveIFMMappingsEtherchannel
        * Added schema and parser for 'show platform software fed {switch} {mode} ifm mappings etherchannel'
    * Added ShowBfdInternal
        * Added schema and parser for 'show bfd internal'
    * Added ShowCryptoPkiCertificatesPemServer
        * Added new parser for cli 'show cry pki certificates pem server'
    * Added ShowObjectGroupName
        * added parser for "show object-group name {group_name}"
    * Added ShowOspfv3NeighborInterface
        * show ospfv3 neighbor {interface}
    * Added ShowPlatformSoftwareSteeringPolicyAomInfo
        * parser for cli 'show platform software steering-policy forwarding-manager switch {switch} F0 policy-aom-info'
    * Added ShowPlatformSoftwareObjectManagerF0Object
        * parser for cli 'show platform software object-manager switch {switch} F0 object {object}'
    * Added ShowLispVrf
        * parser for cli 'show lisp vrf {vrf}'
    * Added ShowPlatformSoftwareAccessListSwitchActiveFPActiveOgLkupIds
        * parser for Show Platform Software Access List Switch Active FP ActiveOgLkupIds
    * Added ShowQfpDropsThresholds
        * show qfp drops thresholds
    * Added ShowConsistencyCheckerMcastStartAll
        * "show consistency-checker mcast {layer} start all"
        * "show consistency-checker mcast {layer} start {address} {source}"
        * "show consistency-checker mcast {layer} start {address}"
        * "show consistency-checker mcast {layer} start vrf {instance_name} {address} {source}"
        * "show consistency-checker mcast {layer} start vlan {vlan_id} {address}"
    * Added ShowConsistencyCheckerRunIdDetail
        * "show consistency-checker run-id {id} detail"
    * Added ShowConsistencyCheckerRunId
        * "show consistency-checker run-id {id}"

* iosxe/c9300
    * Modified ShowEnvironmentAll
        * Added support for < Sensor List Environmental Monitoring >.

* iosxr
    * Added ShowOspfProcessName
        * Parser for cli 'show ospf {process_name}'
    * Added ShowOspfv3ProcessName
        * Parser for cli 'show ospfv3 {process_name}'
    * Added ShowPtpForeignMastersBrief
        * Added parser for show ptp foreign-masters brief

* nxos
    * Added ShowMacSecMkaSummary
        * parser for 'show macsec mka summary'
    * Added ShowMacSecMkaSession
        * parser for 'show macsec mka session'
    * Added ShowMacSecMkaSessionDetails
        * parser for 'show macsec mka session details'
    * Added ShowMacSecMkaStats
        * parser for 'show macsec mka statistics'

* sonic
    * Added ShowVersion
        * Added new OS SONiC and created ShowVersion parser
    * Inherited DockerStatsNoStream from Linux parsers


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fix for ShowPlatformHardwareFedSwitchQosQueueConfig
        * Added str and list pattern to match all possible values
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Added ipv6 source and destination
    * Modified ShowIpv6Interface Parser
        * parser for 'show ipv6 inerface {interface}' added new regex p18_1.
    * Modified ShowSpanningTree Parser
        * parser for 'show spanning tree' added new regex p1_1,p1_2,p1_3,p1_4
    * Modified ShowPlatformFedActiveTcamUtilization
        * Modified cli_command
    * Modified ShowPlatform
        * show platform parser now recognizes 'init, active' state
    * Modified ShowPlatformSoftwareMemoryCallsite
        * Enhanced ShowPlatformSoftwareMemoryCallsite parser to work for show platform software memory fed switch active alloc callsite brief
    * Modified ShowCryptoPkiCertificatesPemServer
        * Enhanced the parser by adding '\n' to each line in the output
    * Fix for ShowPdmSteeringPolicy
        * fixed old parser for cli 'show pdm steering policy' to capture full contract name as contract name can be anything
    * Fix for ShowPlatformSoftwareFedActiveSecurityFed
        * fixed old parser for cli 'show platform software fed {switch} active security-fed sis-redirect firewall all' due to change in output
    * Modified ShowRunInterface
        * Added 112 regex for service-policy outputs
    * Fix for ShowSpanningTreeSummary
        * Added additional key "bpdu_sender_conflict"
    * Modified for ShowAccessSessionInterfaceDetails parser
        * Added new regex <p11_1> for matching ipv6 address '1555105ced6cc3825b39d' '1555102251fffe005'
    * Modified ShowLispIpv4Publication
        * Added support for missing locator addresses.
    * Modified ShowLispIpv6Publication
        * Added support for missing locator addresses.
    * Modified ShowLispServiceDatabase
        * Added support for optional Service-Insertion ID.
    * Modified ShowNat66Statistics
        * Changed enable_count from schema to Optional.
        * Updated regex pattern p0 to accommodate various outputs
    * Added ShowPlatformSoftwareDistributedIpsecTunnelInfo
        * Added ShowPlatformSoftwareDistributedIpsecTunnelInfo for CLI "show platform software distributed-ipsec tunnel-info".

* iosxr
    * Modified ShowIsisInterface Parser
        * Modified pattern r38 to support "Layer-2 Multicast"
        * Modified pattern r40 to support "All ISs              Listening"
        * Added key "lsp_rexmit_queue_size" in topology section in schema
    * Modified ShowBgpInstanceNeighborsDetail
        * Added Optional parameter configured_keepalive_interval to schema
        * Added Optional parameter configured_holdtime to schema
        * Added Optional parameter ttl_security to schema
        * Added Optional parameter external_bgp_neighbor_hop_count to schema
        * Added Optional parameter bfd to schema
        * Added Optional parameter bfd_status inside bfd to schema
        * Added Optional parameter session_status inside bfd to schema
        * Added Optional parameter mininterval inside bfd to schema
        * Added Optional parameter multiplier inside bfd to schema
        * Added Optional parameter messages to schema
        * Added Optional parameter messages_count inside messages to schema
        * Added Optional parameter notifications inside messages to schema
        * Added Optional parameter queue inside messages to schema
        * Added pattern for graceful_restart key
        * Added pattern for graceful_restart_restart_time key
        * Added pattern for graceful_restart_stalepath_time key
    * Modified ShowOspfDatabase
        * Modified Router Id option to schema as Optional.
        * Added regex pattern p5 to match lsa type 2 network link.

* nxos
    * Added
        * Updated regex <p1> with <.> in <type> field
    * Modified ShowInterfaceCounters
        * Modified regex to handle `--` in interface counters output.
    * Modified show_interface_status
        * Modified the p1 regex pattern to capture missing data and remove junk
    * Fixed ShowInterface Parser
        * Fixed regex for some failing output of show interface status command



genie.telemetry
"""""""""""""""""
