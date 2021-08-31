August 2021
==========

August 31st - Genie v21.8
-----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.8                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.8                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

If you have pyATS installed, you can use:

.. code-block:: bash

    pyats version update

**genie**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie.conf
    * Modified convertor.convert_interface()
        * To correctly support tunnel interface conversion for iosxe

* make_json
    * Added logic to ignore directories starting with dot (`.`)

* harness
    * _commons_internal
        * Fixed error with jinja2 configuration

* cli
    * Modified 'pyats develop' and 'pyats undevelop' commands
        * Execution now continues if a package fails
        * Added `pip install --upgrade pip setuptools` to start of tool execution
        * Added `Status` field to end of execution report
        * Split black box test into separate internal and external tests


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* genie
    * Added support for loading of APIs via entrypoint definition
    * Added clean ExtendClean in genie.clean.extend module

* dq
    * Added support to ignore_case_key and ignore_case_value

* harness
    * _commons_internals
        * Added support for file_location in check_config and asynchronous_configure_snapshot.

* cli
    * Added 'pyats develop' command
        * Automation tool for putting packages into development mode
        * Tool clones repos if needed and runs 'make develop' for requested packages
        * https//pubhub.devnetcloud.com/media/pyats/docs/cli/pyats_develop.html
    * Added 'pyats undevelop' command
        * Automation tool for taking packages out of development mode
        * Tool runs 'make undevelop' and 'pip install <package>' for requested packages
        * https//pubhub.devnetcloud.com/media/pyats/docs/cli/pyats_undevelop.html


**genie.libs.clean**

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Modified change_boot_variable stage
        * To support setting the boot variable to the current running image

* iosxe
    * Modified change_boot_variable stage
        * To support setting the boot variable to the current running image


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* common
    * Fixed a bug in copy_to_device where the stage would delete previously copied files if the disk space ran out while copying subsequent files.

* clean
    * Modified
        * copy_to_linux stage now takes interface as an argument
        * copy_to_device stage now takes interface as an argument
    * Modified
        * ping stage fails immediately if requested protocol was not running

* nxos
    * Modified change_boot_variable
        * change_boot_variable calls execute_delete_boot_variable before setting new boot variables
    * Modified _is_boot_variable_as_expected
        * _is_boot_variable_as_expected returns normally if show boot schema is empty and system and kickstart are None
    * N7k
        * Added execute_delete_boot_variable
            * execute_delete_boot_variable api to remove system and kickstart boot variables
    * N9k
        * Added execute_delete_boot_variable
            * execute_delete_boot_variable api to remove nxos boot variable


**genie.libs.conf**

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* genielibs
    * Added support for loading of APIs via entrypoint definition

* nxos
    * Added Interface Conf
        * Added "nve_vni_multisite_mcast_group" to support new CLI "multiste mcast-group <group-addr>" under Interface
    * Added Keychains Conf


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Added dot1q access vlan
        * Added dot1q tunnel access vlan for dot1q tunnel mode.


**genie.libs.filetransferutils**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * fileUtils.py
        * Modified copyfile() to return output

**genie.libs.health**

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* health
    * Added `type` filter for health_tc_sections


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health
    * Updated message in case device is connected, but nothing runs due to not meeting criteria
    * Changed the result from Passed to Skipped in case nothing runs due to not meeting criteria

**genie.libs.ops**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified Routing
        * learn will now loop through all vrfs if no vrf is supplied

**genie.libs.robot**

No changes

**genie.libs.sdk**

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added AAA
        * Added API to retrive values from CLI commands to compare with YANG model data
    * Added
        * verify_show_run_aaa api for verifying the configured commands in show run aaa
        * verify_pattern_in_output api for verifying the pattern list in the output
        * configure_coa api for configuring change of authorization
    * Added get_interface_oper_yang_status to get interface oper status level.
    * Added get_interface_admin_status to get admin status of an interface.
    * Added get_interface_last_state_timestamp to get interface last state up/down time value in nanosecond.
    * Added get_interface_ifindex to get snmp ifindex of an interface.
    * Added get_interface_yang_data to get interface counters and status.
    * Added clear_logging, clear_mpls_ldp_neighbor,clear_mpls_counters, get_show_output_include and celar_counters
    * Added configure_radius_group
    * Added configure_tacacs_group
    * Added AAA
        * Added API to configure dhcp ldra commands
    * Added configure_EAP_Method
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/bgp/configure.py'
        * Added 'configure_bgp_graceful_restart' API
        * Added 'configure_bgp_log_neighbor_changes' API
        * Added 'configure_bgp_neighbor_send_community' API
        * Added 'configure_bgp_redistribute_ospf' API
        * Added 'configure_bgp_redistribute_connected' API
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/mpls/configure.py'
        * Added 'configure_mpls_label_mode_all_vrfs_protocol' API
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/bgp/configure.py'
        * Added 'unconfigure_bgp_neighbor_send_community' API
        * Added 'unconfigure_bgp_neighbor_activate' API
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/interface/configure.py'
        * Added 'config_interface_ospfv3' API
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/ospf/configure.py'
        * Added 'unconfigure_ospf_vrf_on_device' API
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/vrf/configure.py'
        * Added 'unconfigure_vrf_definition_on_device' API
    * Added API configure_interface_switchport_mode(device,interface,mode)
    * Added API configure_interface_no_switchport(device, interface)
    * Added API configure_routing_ip_route_vrf(device,ip_address,mask,vrf,interface,dest_add)
    * Added apis in 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/bgp/configure.py'
        * Added 'def configure_bgp_l2vpn_neighbor_activate'
        * Added 'def configure_redistribute_connected'
    * Added apis in 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/cdp/verify.py'
        * Added 'def verify_cdp_peer_interface'
    * Added apis in 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/cef/verify.py'
        * Added 'def verify_cef_outgoing_interface'
    * Added apis under 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/mpls/configure.py'
        * Added 'def unconfigure_layer2_vfi_autodiscovery'
        * Added 'def configure_layer2_vfi_autodiscovery'
        * Added 'def configure_attachment_circuit_vfi'
        * Added 'def unconfigure_layer2_vfi_manual'
        * Added 'def configure_layer2_vfi_manual'
        * Added 'def unconfigure_mpls_te_explicit_null'
        * Added 'def configure_mpls_te_explicit_null'
        * Added 'def remove_l2vpn_xconnect_context'
        * Added 'def l2vpn_xconnect_context'
        * Added 'def config_eompls_pseudowire'
        * Added 'def config_vc_backup_peer'
        * Added 'def remove_explicit_path'
        * Modified 'def configure_te_tunnel'
        * Added 'def configure_tunnel_auto_route'
        * Added 'def unconfigure_tunnel_auto_route'
        * Added 'def configure_tunnel_priority'
        * Added 'def configure_tunnel_bandwidth'
        * Added 'def configure_dynamic_path_in_tunnel'
        * Added 'def configure_explicit_path_in_tunnel'
        * Added 'def config_pw_class_interface'
        * Added 'def unconfig_pseudowire_class'
        * Added 'def config_pseudowire_class'
        * Added 'def configure_mpls_te_on_interface'
        * Added 'def configure_explicit_path'
        * Added 'def configure_ip_rsvp_bandwidth'
        * Added 'def configure_mpls_te_globally'
        * Added 'def unconfigure_mpls_te_under_ospf'
        * Added 'def configure_mpls_te_on_interface'
        * Added 'def config_xconnect_on_interface'
    * Added 'def configure_mpls_te_forwarding_adjacency'
    * Added 'def configure_mpls_static_binding'
    * Added 'def unconfigure_mpls_static_binding'
        * Added 'def configure_traffic_eng_passive_interface'
        * Added 'def configure_template_type_vpls'
        * Added 'def unconfigure_template_type_vpls'
        * Added 'def configure_autodiscovery_bgp_signalling_ldp_template'
    * Added 'def configure_l2vpn_vfi_context'
    * Added 'def remove_vfi_context'
    * Added apis under 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/mpls/verify.py'
        * Added 'def verify_vc_destination_sect'
        * Added 'def verify_tunnels_state'
    * Added apis 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/bgp/configure.py'
        * Added 'def configure_redistribute_connected'
        * Added 'def configure_bgp_address_family_attributes'
        * Added 'def configure_no_bgp_default'
        * Added 'def configure_ospf_internal_external_routes_into_bgp'
        * Added 'def configure_ospf_include_connected_in_bgp'
    * Added
        * Added Reload Trigger
        * Added Switchover Trigger

* api utils
    * Added API `scale_accesslist_config`
        * To configure more than 1k acls
    * Added API `unconfig_extended_acl`
        * To unconfigure extended acl
    * Added API `configure_qos_policy`
        * To configure qos service policy on interface
    * Added API `unconfigure_qos_policy`
        * To unconfigure qos service policy on interface

* blitz
    * blitz.py
        * Modified custom_start_step_message to support the use of %VARIABLES{}
    * blitz.py
        * Added support to save variable as dictionary.

* ios
    * Added
        * execute_delete_boot_variable
        * execute_set_boot_variable
        * execute_set_config_register
        * execute_write_erase
        * execute_write_memory
        * delete_unprotected_files
        * execute_card_OIR
        * get_diffs_platform
        * get_boot_variables
        * get_available_space
        * get_file_size
        * get_running_image
        * get_total_space
        * write_erase_reload_device_without_reconfig
        * verify_file_exists
        * verify_boot_variable
        * verify_show_boot_variable


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* subsection.py
    * configure_replace
        * Modified configure_replace to handle default dir

* nxos
    * Added new attribute to Evpn Msite Bgw Attributes
        * Added evpn_msite_dci_advertise_pip attribute
    * Modified ISSU to check for config load status post trigger
        * Will ensure modules are up and config status is **System ready**
    * Modified ISSU trigger to transfer scale config to runtime directory
        * Addresses issue where the console is unable to handle scale config and causes unintended typos.

* iosxe
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/utils.py'
        * reverted the changes back for proc verify_ping
    * updated ' pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/mpls/configure.py'
        * Added back the proc remove_mpls_ldp_router_id_from_device
    * updated  'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/ipv6/configure.py'
        * Added doc string to the proc config_enable_ipv6_routing
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/interface/configure.py'
        * Changed function name to contain lower case letters
    * updated 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/ospf/configure.py'
        * included 'def configure_ospf_vrf()' try and except
        * changed pid to ospf_process_id variable
    * changed 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/mpls/verify.py'
        * wrapped 'def verify_tunnels_state()' content and removed inline comment.
        * changed 'def def Configure_Tunnel_Destination()" to lowercase and removed inline comment,
        * Removed camelcase letters to lowercase where ever required.
        * Modified 'def configure_mpls_label_mode' to contain else condition
    * changed 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/interface/configure.py'
        * Fixed indentation for 'def config_mpls_on_device'
        * changed definition to start with lower case.
        * included docstring for 'def config_enable_ip_routing'
    * changed 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/cef/verify.py'
        * removed inline comments.
        * Added spaces between arguments where ever necessary.
        * Fixes indentation in doc string.
        * removed f"", formatted string to .format().
    * changed 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/cdp/verify.py'
        * Added spaces between parameters.
    * changed 'pkgs/sdk-pkg/src/genie/libs/sdk/apis/iosxe/bgp/get.py'
        * Changed 'def get_bgp_state_pfx_rcd' parameters adress_family and neighbor_address are optional

* common
    * modified execute_power_cycle_device API
        * now it works with more than 1 power_cycle.

* utils
    * modified copy_to_device API
        * Will now attempt to delete the remote file before trying to copy it again
            * Removes potentially corrupted files

* blitz
    * Modified parallelism
        * Fixed issue where `continue False` wouldn't end the test on Failure
    * Modified custom actions
        * Fixed issue where `continue False` wouldn't end the test on Failure


**genie.libs.parser**

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowL2fibBridgedomainAddressUnicast
        * show l2fib bridge-domain {bd_id} address unicast {mac_addr}
    * Added ShowL2fibBdPort
        * show l2fib bridge-domain {bd_id} port
    * Added ShowL2routeEvpnMacIp
        * show l2route evpn mac ip
        * show l2route evpn mac ip esi {esi}
        * show l2route evpn mac ip mac-address {macaddr}
        * show l2route evpn mac ip mac-address {macaddr} esi {esi}
        * show l2route evpn mac ip next-hop {next-hop}
        * show l2route evpn mac ip next-hop {next-hop} mac-address {macaddr}
        * show l2route evpn mac ip next-hop {next-hop} mac-address {macaddr} esi {esi}
        * show l2route evpn mac ip producer {prod}
        * show l2route evpn mac ip producer {prod} next-hop {next-hop}
        * show l2route evpn mac ip producer {prod} next-hop {next-hop} mac-address {macaddr}
        * show l2route evpn mac ip producer {prod} next-hop {next-hop} mac-address {macaddr} esi {esi}
        * show l2route evpn mac ip topology {evietag}
        * show l2route evpn mac ip topology {evietag} producer {prod}
        * show l2route evpn mac ip topology {evietag} producer {prod} next-hop {next-hop}
        * show l2route evpn mac ip topology {evietag} producer {prod} next-hop {next-hop} mac-address {macaddr}
        * show l2route evpn mac ip topology {evietag} producer {prod} next-hop {next-hop} mac-address {macaddr} esi {esi}
        * show l2route evpn mac ip topology {evi}
        * show l2route evpn mac ip topology {evi} producer {prod}
        * show l2route evpn mac ip topology {evietag} producer {prod} next-hop {next-hop}
        * show l2route evpn mac ip topology {evietag} producer {prod} next-hop {next-hop} mac-address {macaddr}
        * show l2route evpn mac ip topology {evietag} producer {prod} next-hop {next-hop} mac-address {macaddr} esi {esi}
    * Added ShowIsisAdjacencyStagger
        * Added ShowIsisAdjacencyStagger
            * show isis adjacency stagger
        * Added ShowIsisAdjacencyStaggerAll
            * show isis adjacency stagger all
        * Added ShowIsisAdjacencyStaggerDetail
            * show isis adjacency stagger detail
    * Added ShowIsisFlexAlgo
        * "show isis flex-algo"
        * "show isis flex-algo {flex_algo}"
    * Added ShowIsisNode
        * added a new parser to parse "show isis node" output on IOS XE devices
    * Added ShowIsisRib
        * show isis rib
        * show isis rib {flex_algo}
        * show isis rib {source_ip}
        * show isis rib {source_ip} {subnet_mask}
    * Added ShowIsisTopology
        * Added a new parser for "show isis topology" and "show isis topology flex-algo {algo_num}" on IOS XE devices
    * Added ShowLicenseSummary
        * show license summary
    * Added ShowMdnsServiceList
        * show mdns-sd service-list
    * Added ShowStandbyBrief
        * show standby brief
    * Added ShowMdnsSdgSpSummary
        * show mdns-sd sdg service-peer summary
    * Added ShowMdnsControllerStatistics
        * show mdns-sd controller statistics
    * Added ShowMdnsServicePeerStatistics
        * show mdns-sd service-peer statistics
    * Added ShowMdnsStatisticsInterfaceVlan
        * show mdns-sd statistics interface vlan {vlan}
        * show mdns-sd statistics vlan {vlan}
    * Added ShowMdnsQueryDb
        * show mdns-sd query-db
    * Added showRunMdns
        * show running-config mdns-sd
    * Add ShoTcpDetailPcbAll
        * show tcp detail pcb all
    * Added ShowStackPowerDetail
        * show stack-power detail
        * Added keys and regexex to incoperate detail output for powerstack
    * Added ShowAppHostingDetailAppIdMeraki
        * show app-hosting detail appid meraki | i version
    * Modified ShowLogging
        * Add accumulator 'outer_logging_sources_dict' to capture multiple logging source interfaces
    * Modified ShowLoggingSchema
        * Add Optional 'tls_profiles' dictionary
    * Modified ShowLogging
        * Inserted regex p19-p23 to capture TLS Profile information profile name, ciphersuites, trustpoint, and TLS version
        * Add accumulator 'outer_tls_profile_dict' to capture multiple logging source interfaces
        * Inserted matching logic statements p19-p23 for TLS profile dictionary creation
    * Added ShowMerakiCompatibility
        * show meraki compatibility
        * Added keys and regexes to incorporate a new cli_command
    * Modified ShowRomvar
        * show romvar
        * Added keys and optional parameters
    * Modified ShowAAServers
        * show aaa servers
    * Added ShowAAAUserAll
        * show aaa user all
    * Added ShowAaaFqdnAll
        * show aaa fqdn all
    * Added ShowTacacs
        * show tacacs
    * Added ShowDeviceTrackingMac
        * show device-tracking database mac
        * show device-tracking database mac details
        * show device-tracking database mac {mac}
        * show device-tracking database mac {mac} details
    * Added ShowIpv6SourceGuard
        * show ipv6 destination-guard policy {policy_name}
    * Added ShowDeviceTrackingMessages
    * Added ShowL2routeEvpnImetDetail
        * show l2route evpn imet origin-rtr <origin-ip> detail
        * show l2route evpn imet producer <prod> detail
        * show l2route evpn imet producer <prod> origin-rtr <origin-ip> detail
        * show l2route evpn imet topology <evi><etag> detail
        * show l2route evpn imet topology <evi><etag> producer <prod> detail
        * show l2route evpn imet topology <evi><etag> origin-rtr <origin-ip> detail
        * show l2route evpn imet topology <evi><etag> producer <prod> origin-rtr <origin-ip> detail
    * Added ShowPlatformHarwareThroughputCrypto
        * show platform harware throughput crypto
    * Added ShowWirelessManagementTrustPoint
        * 'show wireless management trustpoint'
    * Added ShowSdwanControlSummary
        * show sdwan control summary

* iosxr
    * Added ShowMplsLdpIgpSync
        * Added 'show mpls ldp igp sync' parser
    * Added ShowMplsLdpGracefulRestart
        * Added 'show mpls ldp graceful-restart' parser
    * Added ShowMplsLdpNsrSummary
        * Added 'show mpls ldp nsr summary' parser
    * Added ShowPolicyMapInterface
        * Added 'show policy-map interface {interface}'
    * Added ShowBgpBestpathCompare
        * Added 'show bgp {address_family} {ip_address} bestpath-compare'
    * Added ShowOspfInterfaceBrief
        * show ospf interface brief

* nxos
    * Modified ShowRunInterface
        * Added parsing support (schema and parsers) for the following outputs
            * no switchport (switchport is default)
            * mtu 1500
            * ip address 10.1.1.1/30
            * vrf member test-vrf
        * show running-config interface
        * show running-config | section ^interface
        * Moved all regex match to before the loop
    * created respective test folder and files under nxos/tests/ShowRunningConfigInterface/

* viptela
    * Added ShowOrchestratorConnections
        * show orchestrator connections

* ios
    * Added ShowCryptoSessionDetail
        * show crypto session detail
    * Added ShowCryptoSession
        * show crypto session


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowStandbyAll
        * To support interface names that contain a hyphen
    * Modified ShowL2routeEvpnImetDetail
        * Added an else clause to consider the case of having only an evi filter
        * Updated docs with missing commands
    * Modified ShowL2routeEvpnMacIp
        * Updated docs for missing commands
    * Modified ShowBfdNeighborsDetails
        * Parser now captures echo_tx and echo_rx fields
        * ld and rd values are also recorded separately
    * Modified ShowBgpNeighborsAdvertisedRoutesSuperParser
        * Updated regex pattern <p3_1> to accommodate various outputs.
        * Updated regex pattern <p3_2> to accommodate various outputs.
    * Modified ShowInterfaces class
        * Added 'suspended' key with boolean value type
        * Fixed input broadcast counter
        * Fixed output broadcast/multicast counter
    * Modified ShowLogging
        * Fixed parser error when output has no logging to information
    * Modified ShowLoggingSchema
        * Comment spacing to improve PEP8 result
    * Modified ShowLogging
        * Updated regex p18 to capture VRF of source interface
        * Logic in source interface matching to populate key 'logging_source_interface' in trap_dict with optional VRF.  Empty dict if not present.
    * Modified ShowLogging
        * Add regex p3 to capture Buffered logging whether enabled or disabled
        * Update regex p6 to capture Exception logging when disabled
        * Updated regex p9 to capture persistent logging output for threshold, alert, notify, immediate, protected
        * Renumber matching statements due to new Buffered regex p3
        * Change dictionary value assignment for p2 to use lower() - ensure values are lowercase when the status starts with Uppercase
        * Update p6 matching logic to account for disabled Exception logging
        * Change p9 matching logic to extract persistent logging options for threshold, alert, notify, immediate, protected.  Delete these keys from the dict if present so remainder of matching logic is unchanged
    * Modified ShowLogging
        * Updated regex p18 to exclude lines after logging source interface is there is a colon after the first string to avoid matching TLS profile output as an interface
    * Modified ShowStandbyAll
        * To support interface names that contain a hyphen
    * Modified ShowL2routeEvpnMacIpDetail
        * Fixed implementation of cli_cmd, added a placeholder for variables used to build the command
    * Modified ShowL2routeEvpnImetDetail
        * Fixed implementation of cli_cmd, added a placeholder for variables used to build the command
    * Modified ShowDeviceTrackingPolicies
        * Added options for specified VLAN or Interface
    * Modified ShowRomVarSchema
        * Changed some schema fields to Optional
        * Added device_managed_mode field
    * Modified ShowRomVar
        * Added regexp for device_managed_mode
    * Modified ShowVersion
        * Added regexp for router_operating_mode
    * Modified  ShowPlatformHardwareThroughputCrypto
        * added strip() function to removed leading trailing whitespaces in a line before  doing regex.
    * Modified ShowPlatform
        * Fixed regex + unittests
    * Modified ShowSegmentRoutingTrafficEngPolicy
        * Fixed regex, added unit tests, and added to the schema
    * Modified ShowVrrp
        * Changed master_router_priority,master_advertisement_interval_secs and master_advertisement_interval_secs from schema to be int or string
        * Updated regex pattern <p2>, <p3> to accommodate various outputs
        * Added regex pattern <p17_2> to accomdate unknown values for negative cases

* iosxr
    * Modified ShowBgpInstanceNeighborsRoutes
        * Removed hardcoded variable
    * Modified ShowBgpInstanceProcessDetailSchema
        * Modified key 'as_number' to Or(int, str). This captures dotted Notation ASN which is string.
    * Modified ShowBgpInstanceProcessDetail
        * Modified RegEx <p4> to capture dotted Notation ASN in BGP
    * Modified ShowBgpInstanceAllAllSchema
        * Modified key 'local_as' to Or(int, str). This captures dotted Notation ASN which is string.
    * Modified ShowBgpInstanceAllAll
        * Modified RegEx <p6>,<p16_2>,<p16>, (<m1><m2><m3>) under <p16>, <p17> to capture dotted Notation ASN in BGP
    * Modified ShowBgpInstanceNeighborsDetail
        * Correctly match 'no-prepend' 'replace-as' and 'dual-as'
        * Add matched values to returned dictionary
    * Migrated parser tests to folder based

* nxos
    * Modified ShowRunningConfigNvOverlay
        * Added key <multisite mcast-group> to schema
        * Added regex pattern <p18> and related code
    * Modified ShowIpRoute
        * Modified regex pattern p2 to accommodate nxos/aci functions.
    * Modified ShowL2routeEvpnMac
        * Added a new optional key 'label' to increase coverage of this parser
        * Added a testcase that will test this new coverage
    * Modified ShowNvePeers
        * Allows the uptime to include a dot, e.g. '0.000000'
    * Modified ShowIsisInterface
        * Changed schema keys <ipv4>, <ipv4_subnet>, <ipv6>, <ipv6_subnet>, <ipv6_link_local_address>, <authentication>, and <auth_check> to Optional to accomodate various device outputs

* viptela
    * Modified ShowControlConnections
        * added a conditional check for change in cli for 17.04 onward to check for ORGANIZATION column in control connection tale
        * updated regex pattern p1 to accommodate new organization column in 17.04 releases onward, otherwise use previous p1
        * moved keys list out of line for loop and update if ORGANIZATION column exists for 17.04 release or greater
        * updated folder based unittest
        * this also updates IOSXE ShowControlConnections

* junos
    * Modified ShowRouteReceiveProtocol
        * Correctly match IPv6 output on multiple lines.
        * Correctly match IPv6 routes and next-hops with a-f characters
        * Correctly match the presence or absence of either med or local-pref in output

* utils
    * Modified unittests.py
        * To show exception in case of parser issue regardless '--display_only_failed' option


--------------------------------------------------------------------------------
                                  Modification                                  
--------------------------------------------------------------------------------

* iosxe
    * Addressed the review comments for  ShowCryptoPkiTrustpointsStatus
        * for 'show crypto pki trustpoints status'
        * for 'show crypto pki trustpoints {trustpoint_name} status'


**genie.telemetry**

No changes

**genie.trafficgen**

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* ixianative
    * Added support for multiple chassis with `ixianative` implementation

* pagent
    * Added pagent and igmp multicast APIs implementation

**genie.webdriver**

No changes
