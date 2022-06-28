June 2022
==========

June 27 - Genie v22.6 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.6                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.6                          |
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

* harness
    * Modified connect
        * Initialize management_interface on Device to prevent later AttributeErrors while learning
    * Modified GenieScriptDiscover
        * for loopable sections, clear the parameters after each iteration rather than carrying them forward.

* genie.harness
    * Fix configure with jinja2 templates when devices have different number of config sections

* device.parse()
    * Fixed breakage with json.dump()
        * changed to format_output() function


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* conf
    * Added support for clean template

* metaparser
    * Updated the schema engine class to take description and default



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean
    * clean.py
        * Added support for clean template
    * stages.py
        * Updated clean stages schema
    * template/iosxe
        * Added default template for iosxe
    * template/sdwan
        * Added default template for sdwan


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie.libs.clean
    * Updated reload stage



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
    * Ops
        * Added Device Ops
    * Ops
        * Added Device Ops schema validation

* iosxr
    * Ops
        * Added Device Ops

* nxos
    * Ops
        * Added Device Ops



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added configure_call_admission API
        * configure call admission
    * Added unconfigure_call_admission API
        * unconfigure call admission
    * Added configure_broadband_aaa API
        * configure broadband aaa
    * Added unconfigure_broadband_aaa API
        * unconfigure broadband aaa
    * Added configure_bgp_router_id_peergroup_neighbor
        * API for configure bgp router id with peergroup neighbor name details
    * Added configure_bgp_router_id_neighbor_ip_peergroup_neighbor
        * API for configure bgp router id neighbor ip assigned to peer group neighborname
    * Added clear_ip_reflexive_list API
        * API to clear_ip_reflexive_list
    * Added clear_dmvpn_statistics API
        * API for clearing dmvpn crypto commands.
    * Added API to configure device credentials
        * configure_masked_unmasked_credentials
    * Added API to configure enable password
        * configure_masked_unmasked_enable_secret_password
    * Added API to unconfigure enable password
        * unconfigure_enable_password
    * Added API to verify device login
        * verify_login_credentials_enable_password
    * Enhanced existing API verify_enable_password to support privilege level
        * verify_enable_password
    * Added API to configure aaa password restriction
        * enable_aaa_password_restriction
    * Added API to unconfigure aaa password restriction
        * disable_aaa_password_restriction
    * Added API to configure login password-reuse-interval <interval>
        * enable_login_password_reuse_interval
    * Added API to unconfigure login password-reuse-interval
        * disable_login_password_reuse_interval
    * Added API to configure aaa authentication login default local tacacs+
        * enable_aaa_authentication_login
    * Added API to unconfigure aaa authentication login default local tacacs+
        * disable_aaa_authentication_login
    * Added API to configure automate-tester username <name> probe-on vrf <vrf>
        * enable_radius_automate_tester_probe_on
    * Added API 'rdware_qfp_active_ipsec_data_drop_clear'
    * Added configure_nat64_interface API
        * API for configuring nat64 enable on interface
    * Added  unconfigure_nat64_interface API
        * API for unconfiguring nat64 enable on interface
    * Added configure_nat64_prefix_stateful API
        * API for configuring nat64 prefix stateful
    * Added unconfigure_nat64_prefix_stateful API
        * API for unconfiguring nat64 prefix stateful
    * Added configure_nat64_translation_timeout API
        * API for configuring nat64 translation timeout
    * Added unconfigure_nat64_translation_timeout API
        * API for unconfiguring nat64 translation timeout
    * Added configure_nat64_v4_list_pool API
        * API for configuring nat64 v4 list pool
    * Added  unconfigure_nat64_v4_list_pool API
        * API for unconfiguring nat64 v4 list pool
    * Added configure_nat64_v4_list_pool_overload API
        * API for configuring nat64 list pool overload
    * Added unconfigure_nat64_v4_list_pool_overload API
        * API for unconfiguring nat64 list pool overload
    * Added configure_nat64_v4_pool API
        * API for configuring nat64 v4 pool
    * Added unconfigure_nat64_v4_pool API
        * API for unconfiguring nat64 v4 pool
    * Added configure_nat64_v6v4_static API
        * API for configuring nat64 v6v4 static
    * Added unconfigure_nat64_v6v4_static API
        * API for un configuring nat64 nat64 v6v4 static
    * Added configure_nat64_v6v4_static_protocol_port API
        * API for configuring nat64 v6v4 static protocol port
    * Added unconfigure_nat64_v6v4_static_protocol_port API
        * API for un configuring nat64 nat64 v6v4 static protocol port
    * Added configure_nat_ipv6_acl API
        * API for configuring nat ipv6 acl
    * Added clear_dmvpn_statistics API
        * API for clearing dmvpn crypto commands.
    * Added API 'hardware_qfp_active_statistics_drop_clear'
    * Added API 'verify_interface_status'
    * Added API 'configure_SVI_Unnumbered'
    * Added API 'configure_SVI_Autostate'
    * Added API 'configure_VRF_RD_Value'
    * Added configure_hsrp_interface  API
        * API for configuring hsrp on interface
    * Added configure_ipv6_mtu  API
        * API for configuring ipv6 mtu on interface
    * Added unconfigure_ipv6_mtu  API
        * API for unconfiguring ipv6 mtu on interface
    * modified configure_ip_on_tunnel_interface API
        * change tunnel mode {mode} ipv4 to tunnel mode {mode} ip
    * Added configure_ip_dhcp_snooping_information_option_allow_untrusted API
        * API for ip dhcp snooping information option allow-untrusted
    * Added unconfigure_ip_dhcp_snooping_information_option_allow_untrusted API
        * API for no ip dhcp snooping information option allow-untrusted
    * Added configure_mdns_on_interface_vlan API
        * API to configure_mdns_on_interface_vlan
    * Added unconfigure_mdns_on_interface_vlan API
        * API to unconfigure_mdns_on_interface_vlan
    * Added configure_port_channel_standalone_disable API
        * API to configure_port_channel_standalone_disable
    * Added unconfigure_port_channel_standalone_disable API
        * API to unconfigure_port_channel_standalone_disable
    * Added API for configure extended acl with reflect
        * 'config_extended_acl_with_reflect'
    * Added API for unconfigure extended acl with reflect
        * 'unconfig_extended_acl_with_reflect'
    * Added API for configure extended acl with evaluate
        * 'config_extended_acl_with_evaluate'
    * Added API for unconfigure extended acl with evaluate
        * 'unconfig_extended_acl_with_evaluate'
    * Added configure_vfi API
        * API for configuring vfi into vlan interface.
    * Added unconfigure_vfi API
        * API for unconfiguring vfi into vlan interface.
    * Modified configure_l2vpn_vfi_context_vpls API
        * API has been modified to configure autodiscovery bgp signalling ldp under vfi
    * Added execute_clear_nat64_statistics API
        * API to clear nat64 statistics.
    * Added execute_clear_nat64_statistics_failure API
        * API to clear nat64 statistics failure.
    * Added execute_clear_nat64_statistics_global API
        * API to clear nat64 statistics global.
    * Added execute_clear_nat64_statistics_interface API
        * API to clear nat64 statistics interface {interface_name}.
    * Added execute_clear_nat64_statistics_pool API
        * API to clear nat64 statistics pool {pool_name}.
    * Added execute_clear_nat64_statistics_prefix_stateful API
        * API to clear nat64 statistics prefix stateful {ipv6_address}/{prefix_length}.
    * Added execute_clear_nat64_translations_all API
        * API to clear nat64 translations all.
    * Added execute_clear_nat64_translations_protocol API
        * API to clear nat64 translations protocol {protocol_name}.
    * Added configure_platform_qos_port_channel_aggregate API
        * API for configuring platform qos port-channel-aggregate.
    * Added unconfigure_platform_qos_port_channel_aggregate API
        * API for unconfiguring platform qos port-channel-aggregate.
    * Added configure_pppoe_enable_interface API
        * Configure pppoe on the router interface
    * Added unconfigure_pppoe_enable_interface API
        * Unconfigure pppoe on the router interface.
    * Fixed iosxe vrf folder and file name
    * Added get_installation_mode
        * Added new api to get installation mode for the controller
    * Added get_ap_model
        * Added new api to get ap model of the access point
    * Added get_tx_power
        * Added new api to get tx power of the access point
    * Added get_unused_channel
        * Added new api to get un used channels of the controller
    * Added get_assignment_mode
        * Added new api to get assignment mode of the controller
    * Added verify_tx_power
        * Added new api to verify tx power of the access point
    * Added verify_unused_channel
        * Added new api to verify un used channels of the controller
    * Added verify_assignment_mode
        * Added new api to verify assignment mode of the controller
    * Added ConfigureApTxPower
        * Added new class to configure access point Tx power
    * Added VerifyInstallationMode
        * Added new class to verify installation mode
    * Added ConfigureRrmDcaChannel
        * Added new class to configure rrm dca channel

* iosxr
    * Added configure_bandwidth_remaining_policy_map API
        * API for configure bandwidth remaining policy map on device
    * Added unconfigure_bandwidth_remaining_policy_map API
        * API for unconfigure bandwidth remainging policy map on device


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Updated configure_bgp_neighbor API
        * Fixed address-family being mandatory issue
    * Fixed get_software_version API
        * Changed the output of the API, added enclosing square bracket
        * NOT BACKWARDS COMPATIBLE
    * Modified api 'verify_file_exists'
        * Api checks exact directory and returns False if folder does not exist

* nxos
    * Modified
        * filetransferutils.fileutils.FileUtils.get_server()
        * sdk.apis.utils.copy_from_device()
        * sdk.apis.nxos.platform.get.get_platform_core()


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Added configure_tacacs_server API
        * Added the configure.py(configure_tacacs_server api) to cat9k folder



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowCryptoGdoiKsCoopVersion
        * show crypto gdoi ks coop version
    * Adding new schema and parser in Show_platform.py
        * Added schema and parser for ShowPlatformSoftwareBPCrimsonContentConfig
    * Added ShowCryptoGdoiRekeySa
        * show crypto gdoi rekey sa
    * Added ShowCryptoGdoiRekeySaDetail
        * show crypto gdoi rekey sa detail
    * Added ShowCryptoGdoiKsDetail
        * show crypto gdoi ks detail
    * Added 'show platform hardware qfp active infrastructure bqs status | include QOS|QFP' schema and parser
        * show platform hardware qfp active infrastructure bqs status | include QOS|QFP
    * Added 'show platform hardware qfp active feature qos interface < interface> hierarchy detail | include sub' schema and parser
        * show platform hardware qfp active feature qos interface < interface> hierarchy detail | include sub
    * Added ShowSdwanPolicyAppRoutePolicyFilter
        * added new parser for cli "show sdwan policy app-route-policy-filter"
    * Added ShowSubscriberSession parser
        * show subscriber session
    * Added ShowSubscriberLiteSession parser
        * show subscriber lite-session
    * Added ShowSubscriberStatistics parser
        * show subscriber statistics
    * Added ShowTunnelProtectionStatistics
        * show tunnel protection statistics
    * Added ShowCryptoGdoiKs
        * show crypto gdoi ks
    * Added ShowDiagnosticResultSwitchModuleTestDetail
        * show diagnostic result switch {switch_num} module {mod_num} test {include} detail
    * Added ShowIpDhcpBindingActiveCount Parser
        * show ip dhcp binding | count Active
    * Added ShowCableTdrInterface
        * Added parsing support (schema and parsers) for show cable tdr {interface}
    * Added ShowPppAtmSession
        * show pppatm session
    * Added ShowLslibProducerAllLscacheLinksDetail
        * show lslib producer all lscache links detail

* iosxr
    * Added Parser
        * For 'show tacacs'

* linux
    * Added DockerStatsNoStream
        * added new parser for cli "docker stats --no-stream"

* nxos
    * Updated ShowInterface
        * Updated <p1>, <p12>, <p13> and <p19> regex


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowInterface
        * Adjusted <p10> to capture port speed unit
    * Modified ShowInterface
        * Added key fec_mode into the schema
        * Updated regex pattern p12, p12_1 to accommodate additional output for fec_mode
    * Modified ShowSpanningTreeMstSchema
        * Converted 'bridge_assurance_inconsistent' to optional in Line 46
        * Converted 'vpc_peer_link_inconsistent' to optional in Line 47
        * Converted 'designated_regional_root_cost' to optional in Line 54
        * Converted 'designated_regional_root_priority' to optional in Line 55
        * Converted 'designated_regional_root_address' to optional in Line 56
    * Modified ShowSpanningTreeMst
        * Updated Regex p1_1 to match multiple VLAN pairs in line 99
        * Updated Regex p5_1 to match Non-VPC port-channel, physical interfaces (inaddition to VPC port-channel) in line 114
        * Updated p5_1.match code to reflect aforementioned changes in regex p5_1 in line 197, 201 to 205

* iosxe
    * Modified ShowFlowMonitorCache
        * Fixed local variable 'entry_dict' referenced before assignment
        * Fixed p10 match condition, changed 'entries' schema keys as optional
    * Fixed ShowIpv6Routers
    * Fixed ShowLispSessionRLOC
    * Fixed ShowLispSubscriberSuperParser
    * Fixed ShowLispDatabaseEid
    * Fixed ShowLispPublicationPrefixSuperParser
    * Fixed ShowLispMapCacheSuperParser
    * Fixed ShowLispSession
    * Added ShowLispSessionAll
    * Added ShowLispSessionEstablished
    * No backward compatibility
    * Modified ShowRunInterface
        * Fixed local variable 'inbound_dict' referenced before assignment
        * Fixed parser returning empty dict
    * Modified the ShowLogging
        * Fix for local variable referenced before assignment
    * Fixed ShowPolicyMapInterface
        * Fixed the parser to support multilevel indentation.
        * Updated regex for dscp.
        * Added regex to support service group as optional key.
        * Added new regex to support cir, bc, be in police.
        * Added <p47>, <p48>, <p49>, <p50> missing regex.
        * no backward compatibility.
    * Made number_of_prefixes as Optional,generic for "show ipv6 route summary"
        * show ipv6 route summary
        * show ipv6 route vrf <vrf> summary
    * Modified ShowTrack
        * Updated the parser schema with type, latest operation return code and latest rtt
        * Added <p1_1>, <p3_1>, <p8> and <p9> regex
    * Modified ShowRunInterface
        * Added ip dhcp snooping information option allow-untrusted
        * Added regex pattern <p83> <P84> to accommodate outputs
    * Modified ShowRunAllSectionInterface
        * Added ip dhcp snooping information option allow-untrusted
        * Added regex pattern <p39> <P40> to accommodate outputs
    * Modified ShowVrrp
        * Modified the code to work for BACKUP as it was working only for MASTER
        * Added optional key <master_down_expiration_secs> to schema
        * Updated regex pattern <p2> to accommodate state BACKUP
        * Updated regex pattern <p11> to accommodate priority configured
        * Updated regex pattern <p16> to accommodate when server not present with priority
        * Updated regexp pattern <p17> to accommodate adv interval (learned)
        * Updated regexp pattern <p18> to accommodate down interval expiration details

* iosxr
    * Modified the ShowOspfInterface
        * Fix for local variable 'ospf_dict' referenced before assignment
        * Added the missing authentication key in the schema.
    * Modified ShowL2VpnXconnect
        * Updated parser to support version 7.2.2
    * Modified ShowHsrpDetail
        * changed <timers> and <redirects_disable> to optional to accommodate MGO outputs
        * Added optional string <configured> to pattern <p13> to accommodate config mac address


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpDhcpBinding Parser
        * show ip dhcp binding


