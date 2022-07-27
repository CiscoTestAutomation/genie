July 2022
==========

July 21 - Genie v22.7 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.7                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.7                          |
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

* genie.harness
    * Modified the configure method to honor the sequence specified in the config datafile
    * Allow configure() service arguments to be passed via config datafile using new config_arguments key under the config section.
    * Allow uids filter to be passed to gRun API, this will allow filtering of e.g. common_cleanup.

* device.parse()
    * Fixed breakage with json.dump()
        * changed to format_output() function

* dq
    * Modified get_values
        * Fixed dq get_values first item is empty list case

* Json
    * Moved the following directories to genielibs/pkgs/sdk-pkg/sdk_generator: 
        * docs/sdk_generator/github/  
        * docs/sdk_generator/outputs/   
    * Modified get_json.py:
        * Updated package location for triggers and verifications 
    * Modified src/genie/json/make_json.py:
        * Updated package and file locations to reflect new file locations
        * Updated make_genielibs() to also build json files for models, triggers, and verifications
    * Removed src/genie/json/clean.json
    * Removed src/genie/json/parsers.json
    * Removed src/genie/json/triggers.json
    * Removed src/genie/json/verifications.json
    * Removed docs/sdk_generator/bitbucket/
    
* All
    * Modified ci/Jenkinsfile:
        * Remove the now redundant 'make json' command from within genie repo
        * Add git diff checks for models, triggers, and verification json files
    * Removed sdk_generator/bitbucket/api_datafile.yaml 
    * Removed sdk_generator/output/bitbucket_apis.json
    * Modified pkgs/sdk-pkg/api_generator/ directory
        * Renamed to sdk_generator as model, trigger, and verifcation files will share that directory
    * Moved the following files from genie to genielibs/pkgs/sdk-pkg/sdk_generator/: 
        * github/models.yaml
        * github/trigger_datafile.yaml 
        * github/verification_datafile.yaml
        * output/github_models.json 
        * output/github_triggers.json
        * output/github_verifications.json 
    * Created following symlinks:
        pkgs/sdk-pkg/src/genie/libs/sdk/triggers/triggers.json -> pkgs/sdk-pkg/sdk_generator/output/github_triggers.json
        pkgs/sdk-pkg/src/genie/libs/sdk/verifications/verifications.json -> pkgs/sdk-pkg/sdk_generator/output/github_verifications.json

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie.libs.clean.stages
    * CopyToLinux stage
        * Added optional key to protocol to resolve ValueError Clean schema check failed in clean yaml file

* clean
    * Modified Reload stage
        * Pass expected arguments to device.initiate()

* recovery
    * _disconnect_reconnect
        * Added condition to check if the device is in rommon

* apis/verify
    * verify_connectivity
        * Added condition to check if the device is in rommon

* iosxe
    * Modified image handler to allow image override by stage
    * Fixed image management for reload stage
    * Modified InstallImage in Clean Stages
        * Removed line where show clock was being appended to packages.conf

* genie.libs.clean
    * Updated reload stage
        * fix the issue for replay object for returning mock object when accessing



genie.libs.conf
"""""""""""""""

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
    * Added configure_isis_network_entity
        * API for configure the isis network entity on device
    * Added remove_isis_configuration
        * API for remove the isis configuration on device
    * Added config_interface_isis
        * API for isis configuration on interface
    * Added unconfig_interface_isis
        * API for remove the isis configuration on interface
    * Added verify_bgp_l2vpn_evpn_rt2_ipprefix api
        * APi for verifying rt2 ipprefix in show ip bgp l2vpn evpn all
    * Added verify_bgp_l2vpn_evpn_rt5_ipprefix
        * Api for verifying rt5 ipprefix in show ip bgp l2vpn evpn all
    * Added verify_bgp_rt5_mvpn_all_ip_mgroup
        * Api for verifying rt5 ipprefix,group in
        * show ip bgp ipv4 mvpn all
    * Added verify_bgp_rt7_mvpn_all_ip_mgroup
        * Api for verifying rt7 ipprefix,group in
        * show ip bgp ipv4 mvpn all
    * Modified configure_ikev2_keyring api
        * Added the option to configure manual or dynamic ppk while making pre share key optional
    * Added configure_snmp_server_view and unconfigure_snmp_server_view API
        * API for configure, unconfigure snmp server view
    * Added configure_sdm_prefer_custom_template API
        * API for sdm prefer custom template
    * Added configure_sap_pmk_on_cts API
        * Added new API to configure sap pmk under cts
    * Added unconfigure_cts_manual API
        * Added new API to unconfigure cts manual
    * Added install_remove_version API
        * API to remove installed packages for particular version
    * Added configure_flow_monitor_vlan_configuration API
        * API to configure flow monitor under vlan configuration
    * Added unconfigure_flow_monitor_vlan_configuration API
        * API to unconfigure flow monitor under vlan configuration
    * Added enable_dhcp_relay_information API
        * API to enable DHCP Relay Information
    * Added disable_dhcp_relay_information API
        * API to disable DHCP Relay Information
    * Added configure_snmp_server_group and unconfigure_snmp_server_group API
        * API for configure, unconfigure snmp server group cli
    * Modified configure_common_criteria_policy api
        * Added the options char_rep and restrict, and set default values to existing options.
    * Modification of existing API for configure_lldp,unconfigure_lldp,configure_lldp_interface,unconfigure_lldp_interface API
        * API to configure lldp neighbors on interface level
    * Modification of existing API for configure_cdp_neighbors,configure_cdp_neighbors,API
        * API to configure and unconfigure cdp neighbors on globally
    * Added configure_port_channel_lacp_max_bundle,unconfigure_port_channel_lacp_max_bundle API
        * API to configure configure_port_channel_lacp_max_bundle and unconfigure_port_channel_lacp_max_bundle on port-channel interface level
    * Added configure_ospf_nsf_ietf API
        * API for configure nsf ietf under ospf
    * Added enable_multicast_advertise_on_evi API
        * API for Enable multicast advertise on evi
    * Added configure_replication_type_on_evi API
        * API for configure replication-type on evi
    * Added enable_switchport_trunk_on_interface API
        * API for enable switchport trunk on interface
    * Added disable_autostate_on_interface API
        * API for disable autostate on interface
    * Added configure_ip_unnumbered_on_interface API
        * API for configure ip unnumbered loopback on interface
    * Added configure_switchport_trunk_allowed_vlan API
        * API for configure switchport trunk allowed vlan on interface
    * Added configure_ip_pim_bsr_candidate API
        * API for configure ip pim bsr-candidate on interface
    * Added configure_ip_pim_rp_candidate_priority API
        * API for configure ip pim rp candidate priority on device
    * Added configure_bgp_router_id_interface API
        * API for configure bgp router-id interface on interface
    * Added configure_bgp_redistribute_static API
        * API for configure bgp redistribute static
    * Added configure_bgp_advertise_l2vpn_evpn API
        * API for configure bgp advertise l2vpn evpn
    * Added configure_nat_pool_overload_rule API
        * API to configure nat pool overload rule.
    * Added unconfigure_nat_pool_overload_rule API
        * API to unconfigure nat pool overload rule.
    * Added configure_static_nat_network_rule API
        * API to configure nat static network rule.
    * Added unconfigure_static_nat_network_rule API
        * API to unconfigure static nat network rule.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* blitz
    * Fix for gNMI SET for List with Multiple Key Values in same testcase.
    * rpcverify.py
        * Fixed issue with remove/delete operation under verify_rpc_data_reply method
    * test_rpc.py
        * Updated existing test case and added new test case to test failed remove/delete operation.

* iosxe
    * Modified unconfigure_fnf_monitor_datalink_interface API
        * Changed the command, updated the parameters(added sampler_name and direction)
    * Fixed configure_ikev2_profile_advanced API
        * Fixed API for trustpoint configuration.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowNat64Translations
        * added new parser for below cli's
    * Added ShowCryptoGdoiGmIdentifierDetail
        * added new parser for cli 'show crypto gdoi gm identifier detail'
    * Added ShowInstallVersion superparser
        * show install  version all
        * show install  version summary
        * show install  version  value <value>
    * Added ShowInstallVersionAll parser
        * show install  version all
    * Added ShowInstallVersionSummary parser
        * show install  version summary
    * Added ShowInstallVersionValue parser
        * show install  version  value <value>
    * Added ShowMemoryDeadTotal
        * show memory dead total
    * Added  show crypto gdoi ks identifier and show crypto gdoi ks identifier detail
        * show crypto gdoi ks identifier
        * show crypto gdoi ks identifier detail
    * Added ShowCryptoGdoiKsCoopIdentifier
        * show crypto gdoi gm identifier detail
    * Added ShowIpNhrpSummary
        * show ip nhrp summary
    * Added ShowCryptoIkev2StatsPsh
        * show crypto ikev2 stats psh
    * Added ShowFabricApSummary
        * Added new parser for "show fabric ap summary".
    * Added ShowAccessTunnelSummary
        * Added new parser for "show access tunnel summary".
    * Added ShowProcessesPlatformCProcess
        * Added new parser for "show processes platform | c wncd".
    * Added ShowProcessesPlatformIProcess
        * Added new parser for "show processes platform | i wncd".
    * Added ShowPlatformSoftCProcess
        * Added new parser for "show plat soft proc slot sw standby r0 monitor | c wncd".
    * Added ShowPlatformSoftIProcess
        * Added new parser for "show plat soft proc slot sw standby r0 monitor | i wncd".
    * Added ShowPlatformSoftwarePuntPolicer
        * show platform software punt-policer
    * Added ShowCryptoGdoiKsCoopDetail
        * show crypto gdoi ks coop detail
    * Added ShowCryptoGdoiGmRekeyDetail
        * added new parser for cli 'show crypto gdoi gm rekey detail'
    * Added ShowPlatformHardwareChassisPowerSupplyDetailAll parser
        * show platform hardware chassis power-supply detail all
    * Added ShowPlatformHardwareChassisFantrayDetail parser
        * show platform hardware chassis fantray detail
    * Added ShowPlatformHardwareChassisFantrayDetailSwitch parser
        * show platform hardware chassis fantraySwitch detail
    * Added ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll parser
        * show platform hardware chassis power-supply detail switch {mode} all
    * Added ShowPlatformFedTcamPbrNat parser
        * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowCryptoGdoiGmIdentifier
        * added new parser for cli 'show crypto gdoi gm identifier'
    * Added ShowIpAccessListDumpReflexive
        * added new parser for cli "show ip access-lists <reflect_acl_name> dump-reflexive"
    * Added ShowPlatformFedActiveFnfRecordCountAsicNum
        * added new parser for cli "show platform software fed active fnf record-count asic <asic_num>"
        * added new parser for cli "show platform software fed <switch> active fnf record-count asic <asic_num>"
    * Modified ShowPlatformHardwareFedActiveTcamUtilization
        * Added new parser for cli "show platform hardware fed <switch> active fwd-asic resource tcam utilization"
        * Modified parser for cli "show platform hardware fed active fwd-asic resource tcam utilization"
    * Modified ShowAccessLists
        * Added space in ShowAccessLists parser
    * Added ShowIpAccessListDumpReflexive
        * added new parser for cli "show platform software fed switch active ifm mappings"
    * Inherited ShowPlatformFedTcamPbrNat parser for c9600 from c9500
        * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    * Added ShowCryptoGdoiGmPubkey
        * added new parser for cli 'show crypto gdoi gm pubkey'
    * Added ShowNat64Timeouts
        * Added new schema and parser for cli show nat64 timeouts
    * Added ShowNat64Statistics
        * Added new schema and parser for cli show nat64 statistics
        * Added new schema and parser for cli show nat64 statistics <global>
        * Added new schema and parser for cli show nat64 statistics mapping <dynamic>
        * Added new schema and parser for cli show nat64 statistics mapping dynamic acl <acl_name>
        * Added new schema and parser for cli show nat64 statistics mapping dynamic pool <pool_name>
    * Added ShowNat64MappingsStaticAddresses
        * Added new schema and parser for cli show nat64 mappings static addresses
        * Added new schema and parser for cli show nat64 mappings static addresses <ip_address>
        * Added new schema and parser for cli show nat64 mappings static addresses <ipv6_address>
    * Added ShowNat64MappingsDynamic
        * Added new schema and parser for cli show nat64 mappings dynamic
        * Added new schema and parser for cli show nat64 mappings dynamic id <number>
        * Added new schema and parser for cli show nat64 mappings dynamic list <access_list_name>
        * Added new schema and parser for cli show nat64 mappings dynamic pool <pool_name>
    * Added ShowNat64StatisticsPrifixStateful
        * Added new schema and parser for cli show nat64 statistics prefix stateful <ipv6>/<prefix_length>
    * Added ShowNat64MappingsStatic
        * Added new schema and parser for cli show nat64 mappings static
    * Added ShowMemoryPlatformInformation
        * show memory platform information
    * Added ShowProcessesCpuPlatformSorted
        * show processes cpu platform sorted
    * Added ShowUtdEngineStandardStatisticsUrl
        * for 'show utd engine standard statistics url'


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpMfib
        * Updated regex pattern <p8> to include "LISPv4 Decap".
    * Modified ShowAAServers
        * Fixed cli_command location. So that device.parse() could pick up.
    * Modified ShowAAAUserAll
        * Fixed cli_command location. So that device.parse() could pick up.
    * Modified ShowAaaFqdnAll
        * Fixed cli_command location. So that device.parse() could pick up.
    * Modified ShowPlatformResources
        * Added one more golden_output and golden_expected_output
        * Modified the key 'tcam' under 'qfp' to Optional
        * Removed keys 'pkt_buf_mem_0' and 'pkt_buf_mem_1'. Replaced it with 'Any()'
    * Modified ShowCryptoIkev2StatsExt
        * Updated parser class. Marked parameters gkm_operation, ppk_sks_operation and ike_preroute as Optional.
    * Modified ShowCryptoIpsecPALHWcreate_ipsec_sa_by_q
        * Updated parser class. Modified regex to reflect behaviour.
    * Modified ShowIpRoute parser
        * Added support for m-OMP
        * Fixed local variable 'source_protocol' referenced before assignement
    * Fixed ShowNat64Translations
        * Modified parser schema to grep multiple outputs under the same key.
        * Removed 'proto' dict and capturing values in index_dict instead as per modified schema. This change is not backwards compatible
    * Modified ShowEnvironmentStatus parser
        * Updated regex pattern <P1> to accommodate various outputs
    * Modified ShowIpMroute
        * Added optional key <lisp_vrf> under incoming_interface_list for lisp specific information.
        * Updated regex pattern <p3> to accommodate various above changes.
        * Added optional key <e_rp> under extranet_rx_vrf_list for additional lisp specific information.
        * Updated regex pattern <p8> to accommodate various above changes.
    * Modified ShowInterfacesTransceiverDetail
        * Removed the line 'stat = None'
        * Fixed <p3_0> regex to include the whole line
    * Modified ShowNat64Translations
        * Updated parser regex to match white space characters.
    * Modified ShowProcessesCpuPlatform
        * Updated regex pattern <p2> to grep the utilization even when its 100%
    * Modified ShowLoggingOnboardRpActiveTemperatureContinuous
        * Added show logging onboard switch {switch_num} rp active {include} continuous as new cli to support stack
    * Modified ShowLoggingOnboardRpActiveUptime
        * Added show logging onboard switch {switch_num} rp active uptime as new cli to support stack
        * Modified the  regex pattern <p6> to accomodate current reset reason change
    * Modified ShowInvetory
        * Added  'GigabitEthernet', 'TwoGigabitEthernet' in code of schema .
        * Updated few lines of code under p2 pattern to accommodate various outputs of IE platform.
    * Modified ShowPlatform
        * Changed state from schema to Optional.
        * Updated regex pattern p3 to accommodate various outputs for IE platforms.

* nxos
    * Modified ShowIpRoute
        * Fix for UnboundLocalError local variable 'route_dict' referenced before assignment
        * Updated the p2 regex to capture 'all-best' key
    * Modified ShowBgpVrfAllAllSummary
        * Added regex pattern <p8_3> and <p8_4> to accommodate output of neighbors with 4byte asn.
    * Modified ShowBgpVrfAllAllSummary
        * Added regex pattern <p8_3> and <p8_4> to accommodate output of neighbors with 4byte asn.




