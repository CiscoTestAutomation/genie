February 2024
==========

February 27 - Genie v24.2 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 24.2                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 24.2                          |
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

* genie
    * setup
        * Pinned `netaddr` to `0.10.1`



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* modified and added hasattr
    * is_ha triggered error added hasattr and attributes.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Update failed pattern for install image stage



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
    * Added unconfigure_policy_map_with_pps
        * New API to unconfigure policy-map pps
    * Added api test_configure_cdp_1
        * added api for validate show interface {interface}
    * Added configure_ip_http_client_secure_trustpoint
        * API to configure_ip_http_client_secure_trustpoint
    * Added hw_module_filesystem_security_lock
        * API to enable/disable filesystem's security-lock
    * Added API verify_interface_capabilities_multiple_media_types
        * Added API to verify the interface media type
    * Added API verify_interfaces_transceiver_supported
        * Added API to verify the transceivers supported in the device
    * Updated `configure_management_gnmi` API to support secure server
    * Modified `generate_rsa_ssl_key` API to support legacy 3des
    * Modified `get_file_contents` API, added removal of carriage return option
    * Modified `configure_pki_import`, added device key and root CA options
    * Added new api `generate_pkcs12` to generate pkcs12 file.
    * Added API unconfigure_ip_igmp_querier_query_interval
        * Added API for unconfigure ip igmp querier query interval
    * Added API unconfigure_ip_igmp_querier_max_response_time
        * Added API for unconfigure ip igmp querier max response time
    * Added API unconfigure_ip_igmp_querier_tcn_query_count
        * Added API for unconfigure ip igmp querier tcn query count
    * Added API unconfigure_ip_igmp_querier_tcn_query_interval
        * Added API for unconfigure ip igmp querier tcn query interval
    * Added API unconfigure_ip_igmp_querier_timer_expiry
        * Added API for unconfigure ip igmp querier timer expiry

* api utils
    * Add
        * check_and_wait decorator

* makefile
    * Added pyasyncore dependency to fix pysnmp script


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* linux
    * Add api get_valid_ipv4_address
        * added api to validate and return ipv4 address
    * Add api get_ip_route_for_ipv4
        * added api to get the routing ip form routing table
    * Modified get_snmp_snmpwalk
        * Added timeout parameter to increase timeout of execute operation

* iosxe/rommon
    * configure
        * Updated `configure_rommon_tftp` API to set TFTP_FILE as the rommon variable.
    * utils
        * Updated `device_rommon_boot` API with a an option to boot using TFTP_FILE.

* iosxe
    * Modified configure_sdm_prefer_custom_template
        * added parameters custom_template, entried and priority
    * Modified get_snmp_snmpwalk
        * Added timeout parameter to increase timeout of execute operation
    * `get_running_config_dict` API
        * Added `output` parameter to pass the output of `show running-config` command.


--------------------------------------------------------------------------------
                                     Modify                                     
--------------------------------------------------------------------------------

* iosxe
    * Modified configure_virtual_template
        * modified api to configure ipv6_pool_name



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * c9300
        * Remove unused imports
    * Modified ShowPlatformSoftwareFedSwitchActiveAclStatisticsEventsSchema
        * Modified schema by added mac_ingress_acl_deny , mac_egress_acl_deny
    * Modified ShowIdpromTan Parser
        * Modified the revision_num from int to str, Since revision number is consists alphanumeric.
    * Modified ShowIpIgmpSnoopingQuerierVlanDetailSchema
        * added vlan_id in def cil command
    * Fix for ShowPlatformTcamUtilization
        * Modified script by adding the command "show platform hardware fed switch {mode} fwd-asic resource tcam utilization".
    * Modified ShowPlatformSoftwareFedSwitchActiveStpVlan Parser
        * Modified the p2 regex pattern.
    * Modified ShowPlatformSoftwareFedSwitchActiveMonitor Parser
        * added support for switch number
    * Modified parser ShowPlatformTcamPbr
        * Fixed schema and regex pattern
    * Modified ShowEthernetCfmMaintenancePointsRemoteDetail
        * Changed flat output working only for single instance to multiple instance support
            * Add index for multile remote points
            * Add key for total_remote_meps, total_mep_port_up, total_mep_intf_up
        * Updated regex pattern p5(ma_name) p7(evc) to accommodate various outputs.
    * Modified ShowIpArpInspectionVlan
        * Updated regex pattern <p5> to accommodate various outputs.
    * C9500
        * Modified ShowPlatformTcamUtilization
            * Changed schema to accomodate various outputs.
            * Added regex pattern <p2> and <p3> to accommodate various outputs.
    * Added ShowFipsStatus
        * show fips status
    * Modified ShowPlatformHardwareAuthenticationStatus
        * Modified optional keys to support SVL and Stack setups
    * Modified ShowCtsInterfaceSchema
        * Changed global_dot1x_feature from schema to Optional (not present on port-channel interfaces)
        * Changed cts mode value from schema to Optional to (not present when cts status is disabled)
    * Modified ShowCtsInterface
        * Updated regex pattern p2 to also match Port-channel interfaces
        * Updated regex pattern p3 to also match CTS disabled status
        * Added conditional to cts_dict so mode key is not generated if cts is disabled
    * Modified golden_output2_expected test data
        * Added expected output for Port-channel interfaces
    * Added golden_output4 test data & expected results
    * Modified show_policy_map
        * Added priority_percent to the schema.
        * Added regex p10_2 to accommodate getting the data from the output.

* utils
    * Updated unittest.py to use exec_module() instead of load_module()

* nxos
    * Modified ShowIpInterfaceVrfAll Parser
        * Modified pattern <p2> to parse line 'lo2, Interface status protocol-up/link-up/admin-up, iod 7, mode anycast-mac,external'
        * Added key 'mode' as optional parameter to schema
        * Modified keys 'counters', 'ip_mtu', 'proxy_arp', 'local_proxy_arp', 'multicast_routing', 'icmp_redirects', 'directed_broadcast' as optional parameters in schema
        * Modified keys 'icmp_unreachable', 'icmp_port_unreachable', 'unicast_reverse_path', 'load_sharing', 'int_stat_last_reset' as optional parameters in schema
    * Modified ShowCdpNeighbors
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowModule
        * Updated regex pattern <p3> to make status optional
        * Added new regex pattern <p7> to capture status separately
    * Modified ShowModule
        * Updated regex pattern <p1> to accommodate `N9K-vSUP` model.

* iosxr
    * Modified ShowBgpVrfAfPrefix
        * Added support for cli 'show bgp {address_family} rd {route_rd} detail'
        * Added support for cli 'show bgp {address_family} {route} detail'
    * Modified ShowPtpPlatformServo
        * Modified pattern <p15> to support line 'setTime()0  stepTime()0 adjustFreq()0'
        * Modified pattern <p16> to support line 'Last setTime 0.000000000 flag0  Last stepTime0 Last adjustFreq0'
        * Modified key 'adjust_freq_time' as optional parameter in schema

* generic
    * Update show version
        * Update show version for checking if device is in controller mode.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added ShowMplsForwardingPrefixIPV4Unicast
        * parser for 'show mpls forwarding prefix ipv4 unicast {prefix}'
    * Added ShowOspfv3DatabaseprefixAdvRouter
        * Added schema and parser for show ospfv3 database prefix advertising router
    * Modified ShowBgpAddressfamilyPrefix Parser
        * parser for 'show bgp {address_family} {bgp_prefix}'
    * Added ShowFilesystemLocationAll
        * Added schema and parser for cli 'show filesystem location all'
    * Added ShowRouteSummary
        * added new parser for cli 'show route summary'

* iosxe
    * Added ShowMplsTrafficEngFastRerouteDatabaseDetail
        * Added schema and parser for show mpls traffic-eng fast-reroute database detail
    * Added ShowIpRsvpFast
        * Added schema and parser for show ip rsvp fast
    * Added ShowIsisIpv6MicroloopAvoidance
        * Added parser for show isis ipv6 microloop avoidance and schema
    * Added ShowIsisIpv6RibParser
        * Updated pattern to capture lfa_type to include 'TILFA node-protecting'.
        * Fixed issues with 'show isis ipv6 rib' command to handle single flag ouput cases.
    * Added ShowL2tpSessionPackets
        * show l2tp session packets
        * show l2tp session packets vcid {vcid}
    * Added ShowTelemetryInternalProtocolManager
        * parser for 'show telemetry interal protocol {protocol} manager'
    * Added ShowIpDhcpSnoopingBibdingInterfaceCount
        * parser for ShowIpDhcpSnoopingBibdingInterfaceCount
    * Added ShowIpVerifySourceInterfaceCount
        * parser for ShowIpVerifySourceInterfaceCount
    * Added ShowPortSecurityInterfaceCount
        * parser for ShowPortSecurityInterfaceCount
    * Added ShowDeviceTrackingDatabaseInterfaceCount
        * parser for ShowDeviceTrackingDatabaseInterfaceCount
    * Added ShowHwModuleSecurityLockStatus
        * show hw-module {filesytem} security-lock status
    * Added ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsite Parser.
    * Added ShowDiagnosticStatus Parser.
    * Added ShowPlatformSoftwareFedSwitchActivePuntBrief Parser.

* nxos
    * Added ShowBfdIpv4Session
        * show bfd ipv4 neighbors
        * show bfd ipv4 neighbors vrf {vrf}
        * show bfd ipv4 {ipv4_address} neighbors vrf {vrf}
    * Added ShowBfdIpv6Session
        * show bfd ipv6 neighbors
        * show bfd ipv6 neighbors vrf {vrf}
        * show bfd ipv6 {ipv6_address} neighbors vrf {vrf}



genie.telemetry
"""""""""""""""""
