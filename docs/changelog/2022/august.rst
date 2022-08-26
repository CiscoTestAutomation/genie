August 2022
==========

August 26 - Genie v22.8 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.8                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.8                          |
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

* genie.conf.base
    * Fix for ''Device' object has no attribute 'management_interface''


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* genie.harness
    * Added `pyats validate jinja2_config` CLI command to validate and output jinja2 config rendering



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* generic
    * Added ``delete_files`` clean stage


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified
        * Fixed issue with reconnect_via argument in reload clean stage



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified filetranferutils to handle command lengths exceeding 253 characters by limiting the destination URL and entering the filename at the prompt



genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* ios
    * verify_file_exists
        * Fixed verify_file_exists api function



genie.libs.robot
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* generic
    * Modified 'Compare profile' keyword
        * Added timestamp for IOSXR to exclude list



genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* nxos
    * Modified _perform_issu API
        * Added support for disruptive ISSU

* iosxe
    * Modified unconfigure_stackwise_virtual_interfaces API
        * API for Unconfiguring stackwise config on interface level to hendel prompt yes or no.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* blitz
    * Fix for gNMI Payload Build for Multiple List with "/" in Key Values.
    * Fix for GNMI Subscription ONCE and POLL mode reciever stops after 1st response for Subscription list containing multiple paths.
    * Validation Support for Subscription list containing multiple paths (All Modes).
    * rpcverify.py
        * Fix to handle different namespaces in the rpc reply.

* iosxe
    * Modified verify_bgp_rt7_mvpn_all_ip_mgroup
        * Removed colon check for rd and also corrected the ipv6 check
    * Modified verify_bgp_rt5_mvpn_all_ip_mgroup
        * Removed colon check for rd and also corrected the ipv6 check
    * Modified verify_bgp_l2vpn_evpn_rt2_ipprefix api
        * Removed colon check from ip address and will consider ipv6 address in prefix
    * Modified verify_bgp_l2vpn_evpn_rt5_ipprefix api
        * Removed colon check from ip address and will consider ipv6 address in prefix
    * Modified configure_routing_static_route API
        * Added more VRF config
    * Updated get_component_descr API
        * Splited regex <p1> into <p1> and <p2>; and made the code changes in the respective section
    * Modified configure_bgp_neighbor_activate api
        * Added vrf argument to support vrf

* common
    * Updated execute_copy_run_to_start API
        * add a dialog for handling device output.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* cat9k
    * Added get_fabric_ap_state
        * Added new api to get fabric ap state for the access point
    * Added get_lisp_session_state
        * Added new api to get lisp session state of the access point
    * Added get_ap_ip
        * Added new api to get ap ip of the access point
    * Added get_rloc_ip
        * Added new api to get rloc ip of the access point
    * Added get_matching_line_processes_platform
        * Added new api to get matching lines from  processes platform for a given process
    * Added get_matching_line_platform_software
        * Added new api to get matching lines from platform software for a given process
    * Added get_processes_platform_dict
        * Added new api to get processes platform for a given process
    * Added get_platform_software_dict
        * Added new api to get platform software for a given process
    * Added VerifyApFabricSummary
        * Added new clean stage VerifyApFabricSummary
    * Added VerifyLispSessionEstablished
        * Added new clean stage VerifyLispSessionEstablished
    * Added VerifyAccessTunnelSummary
        * Added new clean stage VerifyAccessTunnelSummary
    * Added VerifyWirelessProcess
        * Added new clean stage VerifyWirelessProcess

* iosxe
    * Added unconfigure_hw_module_slot_shutdown API
        * API to unshut hw-module slot.
    * Added configure_hw_module_slot_shutdown API
        * API to shutdown hw-module slot.
    * Added unconfigure_ripng
        * API for unconfigure the rip ipv6 configuation on device
    * Added configure_ripng
        * API for configure the rip ipv6 configuration on device
    * Added unconfigure_rip
        * API for unconfigure the rip ipv4 configuration on device
    * Added config_interface_ripng
        * API for configure the rip ipv6 configuration on interface
    * Added unconfig_interface_ripng
        * API for unconfigure the rip ipv6 configuration on interface
    * Added configure_rip
        * API for configure the rip ipv4 configuration on device
    * Added tunnel_range_shut_unshut
        * API for doing shutdown and unshutdown of tunnel interface range configuation on device
    * Added copy_config_from_tftp_to_media
        * API for copying configuration file from tftp location to device media
    * Added configure_snmp_server_user and unconfigure_snmp_server_user API
        * API for configure, unconfigure snmp server user cli
    * Added clear_ipv6_pim_topology api
        * Api for clear ipv6 pim topology
    * Added verify_bgp_l2vpn_evpn_rt2_nxthop api
        * Api for verifying rt2 next hop in show ip bgp l2vpn evpn all
    * Added verify_bgp_l2vpn_evpn_rt5_nxthop api
        * Api for verifying rt5 next hop in show ip bgp l2vpn evpn all
    * Added debug_platform_memory_fed_backtrace and debug_platform_memory_fed_callsite API
        * API for debug platform memory callsite and backtrace
    * Added get_neighbor_count
        * api for  show ip ospf neighbor count
    * Added configure_ipv4_dhcp_relay_helper_vrf API
        * API to configure IPv4 DHCP relay helper IP under interface
    * Added unconfigure_ipv4_dhcp_relay_helper_vrf API
        * API to unconfigure IPv4 DHCP relay helper IP under interface
    * Added configure_vrf_select_source API
        * API to configure VRF select source under interface
    * Added unconfigure_vrf_select_source API
        * API to unconfigure VRF select source under interface
    * Added configure_snmp_server_trap and unconfigure_snmp_server_trap API
        * API for configure, unconfigure snmp server traps and informs cli
    * Added get_total_cdp_entries_displayed API
        * Added new API to get the total cdp entries dispalyed
    * Added verify_total_cdp_entries_displayed_interfaces API
        * Added new API to verify total cdp entries i.e interfaces displayed
    * Added get_cpu_processes_details_include_with_specific_process
        * api for  show cpu processes details include with specific process
    * Added transceiver_power_intf,transceiver_interval_intf and transceiver_intf_components API's
        * API's for getting the values from "show interfaces transceiver detail" parser,related switch transceiver interfaces and return values respectively
    * Added configure_mpls_mtu API
        * API for configure mpls mtu on device interface
    * Added configure_ip_igmp_static_group api
        * Api for configuring ip igmp static-group
    * Added configure_ipv6_mld_static_group
        * Api for configuring ipv6 mld static-group addr addr
    * Added configure_ip_igmp_join_group
        * Api for configuring ip igmp join-group addr source addr
    * Added configure_bgp_neighbor_advertisement_interval api
        * Api for configuring advertisement interval in addressfamily of
        * router bgp that includes vrf also if given
    * Added configure_bgp_l2vpn_evpn_rewrite_evpn_rt_asn api
        * Api for configuring rewrite evpn rt asn in l2vpn evpn of router bgp
    * Added clear_ip_bgp_af_as api
        * Api for clearing clear ip bgp address_family as_numbers
    * install
        * Added install_auto_abort_timer_stop under configure.py
        * Added clear_install_state under configure.py
        * Added create_rollback_label under configure.py
        * Added clear_install_label under configure.py
        * Added create_rollback_description under configure.py
        * Added install_remove under configure.py
        * Added install_commit under configure.py
        * Added install_add under configure.py
        * Added install_activate under configure.py
        * Added install_one_shot under configure.py
        * Added install_abort under configure.py
        * Added install_deactivate under configure.py
        * Added install_rollback under configure.py
        * Added get_install_version under get.py
        * Added verify_rollback_label under verify.py
        * Added verify_active_standby under verify.py
        * Added verify_rollback_description under verify.py
        * Added verify_install_state under verify.py
        * Added verify_install_auto_abort_timer_state under verify.py
    * platform
        * Added execute_clear_parser_statistics under execute.py
    * Added cts_refresh_policy API
        * API to refresh CTS policy
    * Added cts_refresh_environment_data API
        * API to refresh CTS environment data
    * Added cts_refresh_pac API
        * API to refresh CTS pac
    * Added clear_ipv6_nhrp
        * API for clear ipv6 nhrp

* blitz
    * Added GNMI ASCII encoding support
        * Specify ASCII encoding in format for GNMI request.
        * To verify the GNMI response, in returns section, set datatype to ascii, and expected value. An acceptable operator is '=='.



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCryptogdoiIpsecSa
        * added new parser for cli "show crypto gdoi ipsec sa"
    * Added ShowDeviceSensor
        * show device sensor cache interface {interface}
    * Added ShowIpDhcpSnoopingBindingTotalNumber
        * show ip dhcp snooping binding | include Total number of bindings
    * Added ShowIpDhcpSnoopingGleaning
        * show ip dhcp snooping | include gleaning
    * Added ShowFileSystems Parser in show_platform.py
        * show file systems
    * Added ShowException parser in show_install.py
        * show exception
    * Added ShowIssuClients parser in show_issu.py
        * show issu clients
    * Added ShowPlatformHardwareQfpActiveInfraPuntStatTypePer
        * show platform hardware qfp active infra punt stat type per | ex _0_
    * Added ShowSwitchStackPortSummary
        * Created parser for show switch stack port summary to check the stack port summary status.
    * Added ShowSdwanPolicyFromVsmart
        * added new parser for cli "show sdwan policy from-vsmart"
    * Added ShowPlatformSoftInfraBipc
        * show platform soft infra bipc | inc buffer
    * Added ShowLispDatabaseConfigPropV4Parser
        * 'show lisp instance-id {instance_id} ipv4 database config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv4 database config-propagation',
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 database config-propagation',
        * 'show lisp all instance-id * ipv4 database config-propagation'
    * Added ShowLispDatabaseConfigPropV6Parser
        * 'show lisp instance-id {instance_id} ipv6 database config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv6 database config-propagation',
        * 'show lisp {lisp_id} instance-id {instance_id} ipv6 database config-propagation',
        * 'show lisp all instance-id * ipv6 database config-propagation'
    * Added ShowPlatformHardwareQfpActiveDatapathPmdIfdev
        * show platform hardware qfp active datapath pmd ifdev
    * Added ShowSdmPrefer
        * added new parser for cli 'show sdm prefer'
    * Added ShowPlatformHardwareAuthenticationStatus
        * Created show platform hardware authentication status parser to check switch, stackAdaptor and FRU status
    * Added ShowRunSectionBgp
        * added new parser for cli "show running-config | section bgp"
    * Added ShowSpanningTreeInstances
        * show spanning-tree instances
    * Added ShowPlatformHardwareThroughputLevel
        * show platform hardware throughput level
    * Added ShowPlatformHardwareQfpActiveInfraDatapathInfraSwDistrib
        * show platform hardware qfp active datapath infra sw-distrib
    * Added ShowCtsServerList
        * added new parser for cli "show cts server-list"
    * Added ShowPlatformSoftwareFedSwitchStandbyAclUsage
        * added new parser for cli "show platform software fed switch standby acl usage"
    * Added ShowPlatformSwitchStandbyTcamUtilization
        * added new parser for cli "show platform hardware fed switch standby fwd-asic resource tcam utilization"
    * Modified ShowPlatformFedActiveFnfRecordCountAsicNum
        * Modified parser for cli "show platform software fed switch <state> fnf record-count asic <asic num>"
    * Added ShowPlatformHardwareFedSwitchActiveFwdResourceUtilizationLabel
        * for 'show platform hardware fed switch active fwd resource utilization | include {label}'
    * Added ShowPlatformHardwareQfpActiveSystemState
        * show platform hardware qfp active system state
    * Added ShowPlatformHardwareQfpActiveFeatureIpsecDatapathDropsAll
        * show platform hardware qfp active feature ipsec datapath drops all
    * Added ShowOspfv3vrfNeighbor
        * show ospfv3 vrf {vrf} neighbor
    * Added ShowNat64Pools
        * show nat64 pools
        * show nat64 pools {routes}
        * show nat64 pools hsl-id {hsl_id}
        * show nat64 pools hsl-id {hsl_id} {routes}
        * show nat64 pools name {pool_name}
        * show nat64 pools name {pool_name} {routes}
        * show nat64 pools range {pool_start_ip} {upper_range}
        * show nat64 pools range {pool_start_ip} {upper_range} {routes}
    * Added ShowNat64PrefixStatefulGlobal
        * show nat64 prefix stateful global
    * Added ShowNat64PrefixStatefulInterfaces
        * show nat64 prefix stateful interfaces
        * show nat64 prefix stateful interfaces prefix {prefix}
    * Added ShowNat64PrefixStatefulStaticRoutes
        * show nat64 prefix stateful static-routes
        * show nat64 prefix stateful static-routes prefix {prefix}
    * Added ShowPlatformHardwareQfpActiveDatapathInfraSwCio
        * show platform hardware qfp active datapath infra sw-cio
    * Added ShowPlatformHardwareQfpActiveDatapathInfraSwNic
        * show platform hardware qfp active datapath infra sw-nic
    * Added ShowPlatformHardwareQfpActiveInterfaceAllStatisticsDropSummary
        * show platform hardware qfp active interface all statistics drop_summary
    * Added ShowGnxiState
        * show gnxi state
    * Added ShowGnxiStateDetail
        * show gnxi state detail
    * Added ShowUtdEngineStandardConfig
        * show utd engine standard config
    * Added ShowBdDatapath
        * show platform hardware qfp active feature bridge-domain datapath {bd_id}
    * Added ShowLispServerConfigPropV4Parser parser
        * show lisp instance-id {instance_id} ipv4 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation
        * show lisp all instance-id {instance_id} ipv4 server config-propagation
    * Added ShowLispServerConfigPropV6Parser parser
        * show lisp instance-id {instance_id} ipv6 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation
        * show lisp all instance-id {instance_id} ipv6 server config-propagation
    * Added ShowLispPublicationConfigPropV4Parser
        * 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
        * 'show lisp instance-id {instance_id} ipv4 publication config-propagation detail',
        * 'show lisp all instance-id * ipv4 publication config-propagation'
    * Added ShowPlatformSoftwareFactoryResetSecureLog
        * Added show platform software factory-reset secure log
    * Added ShowLispV4ServerConfigPropagation parser
        * show lisp instance-id {instance_id} ipv4 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation
    * Added ShowLispV6ServerConfigPropagation parser
        * show lisp instance-id {instance_id} ipv6 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation
    * Added ShowCryptoGdoiKsAcl
        * show crypto gdoi ks acl
    * Added ShowCryptoGdoiGmAclLocal
        * show crypto gdoi gm acl local
    * Added ShowCryptoGdoiKsMembers
        * show crypto gdoi ks members
    * Added ShowCryptoGdoiKsMembersIp
        * show crypto gdoi ks members {member_ip}
    * Added ShowCryptoGdoiKsMembersSummary
        * show crypto gdoi ks members summary
    * Added ShowIpv6CefInternal parser
        * 'show ipv6 cef internal'
        * 'show ipv6 cef {prefix} internal'
        * 'show ipv6 cef vrf {vrf} {ip} internal'

* sros
    * Added ShowServiceSdpUsing
        * show service sdp-using

* nxos
    * Added ShowFex
        * show fex

* updated <state> as argument to validate stack device active or standby commands. now the parser will work for both standlone and stack devices.

* added showlisppublicationconfigpropv6parser
    * 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
    * 'show lisp instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
    * 'show lisp instance-id {instance_id} ipv6 publication config-propagation detail',
    * 'show lisp all instance-id * ipv6 publication config-propagation'

* iosxr
    * Added ShowRcmdNode
        * show rcmd node
    * Added ShowRcmdMemory
        * show rcmd memory


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Added ShowFabricApSummary
        * Moved new parser for "show fabric ap summary" from iosxe to iosxe/cat9k.
    * Added ShowAccessTunnelSummary
        * Moved new parser for "show access tunnel summary" from iosxe to iosxe/cat9k.
    * Added ShowProcessesPlatformCProcess
        * Moved new parser for "show processes platform | c wncd" from iosxe to iosxe/cat9k.
    * Added ShowProcessesPlatformIProcess
        * Moved new parser for "show processes platform | i wncd" from iosxe to iosxe/cat9k.
    * Added ShowPlatformSoftCProcess
        * Moved new parser for "show plat soft proc slot sw standby r0 monitor | c wncd" from iosxe to iosxe/cat9k.
    * Added ShowPlatformSoftIProcess
        * Moved new parser for "show plat soft proc slot sw standby r0 monitor | i wncd" from iosxe to iosxe/cat9k.
    * Modified ShowApSummary
        * Modified parser "show ap summary" to handle 0 APs and new output change in 17.10 release.
    * Modified ShowBootvat Parser in show_platform.py
        * show bootvar
    * Modified ShowBoot Parser in show_platform.py
        * show boot
    * Modified ShowBoot Parser in show_issu.py
        * show boot
    * Modified ShowApSummary
        * Fixed show ap summary to handle both outputs.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated /d to /d+ in compile for the following Parsers to match the numbers correctly
        * ShowNat64Statistics
            * Modified <p8> to accommodate values with 2 or more digits
        * ShowNat64MappingsStaticAddresses
            * Modified <p2> to accommodate values with 2 or more digits
        * ShowNat64MappingsDynamic
            * Modified <p2> and <p4> to accommodate values with 2 or more digits
        * ShowNat64MappingsStatic
            * Modified <p5> to accommodate values with 2 or more digits
    * Modified ShowVersion
        * Updated regex pattern p16_1 to accommodate a license_type with a spaces, e.g. "Type Permanent Right-To-Use"
    * Modified ShowCryptoGdoiGmIdentifier
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiGmIdentifierSchema
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiGmIdentifierDetail
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiGmIdentifierDetailSchema
        * changed schema and parsers to handle multiple group-member per group
    * Modified ShowCryptoGdoiKsCoopDetail
        * changed schema and parsers to handle multiple ks-member per group
    * Modified ShowCryptoGdoiKsCoopDetailSchema
        * changed schema and parsers to handle multiple ks-member per group
    * Modified ShowCryptoGdoiGmPubkey
        * changed schema and parsers to handle multiple sessions per group
    * Modified ShowCryptoGdoiGmPubkeySchema
        * changed schema and parsers to handle multiple sessions per group
    * Modified ShowBgpSummarySuperParser
        * Changed p9 and p11 to work with 4 byte BGP AS number
    * Modified ShowBgpSummarySchema
        * Changed field 'as' to return type int or str in case of 4 byte BGP AS.
    * Modified ShowLslibProducerAllLscacheLinksDetail
        * updated regexp pattern p36 to accomodate A bit
    * Modified ShowCtsRoleBasedPermissions
        * added support to options of the show cts role-based permissions
    * Modified ShowCtsRoleBasedCounters
        * added support to options of the show cts role-based counters
    * Modified ShowNat64Statistics
        * Added the new command show nat64 statistics interface <interface_name>
    * Modified ShowNat64MappingsDynamic
        * Corrected the show command "show nat64 mappings dynamic"
    * Modified ShowNat64MappingsStaticSchema
        * Corrected the show command in schema "show nat64 mappings static"
    * Modified ShowRunningConfigNve
        * Made the key 'l2vpn_global' optional
        * Made the keys 'l2vni' and 'l3vni' under 'nve_interfaces' optional
    * Modified ShowTelemetryIETFSubscription, ShowTelemetryIETFSubscriptionDetail
        * Parsers for 'all', 'configured', 'dynamic', and 'permanent' variants of 'show telemetry ietf subscription' were broken by the previous change. Fix by moving them to separate classes that inherit from the base class for this CLI.
    * Modified ShowCryptoGdoiKsCoopIdentifierDetail class
        * Changed Regex to include spaces, which was missing.
    * Modified Expected and Golden output
        * Changed Expected and Golden output, in line with actual device output.
    * Modified ShowLoggingOnboardRpActiveUptime
        * Added show logging onboard switch {switch_num} uptime as new cli to support stack

* generic
    * Add debug log message showing which parser is being used

* iosxr
    * Added ShowRouteIpv4
        * Updated the regex <p11> to fix local variable 'outgoing_interface_dict' referenced before assignment

* nxos
    * Modified ShowIpArpDetailVrfAll
        * Updated regex pattern p1 to support VRF in output
    * Modified ShowRunningConfigBgp
        * Updated regex pattern <p45> to accommodate more than just letters and numbers in BGP neighbor description.  E.g.  []-"_' '
    * ShowRunningConfigBgp
        * Fix for Schema missing key error
    * Modified ShowIpRoute
        * Add Regex <p7> to match multiple lines not captured in existing code
    * Modified ShowModule
        * Updated schema/parser to add new header type `lem` to accommodate edelweiss platform output variant.


