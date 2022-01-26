January 2022
==========

January 25 - Genie v22.1
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 22.1                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 22.1                          |
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

* genie harness
    * Updated jinja2 config rendering error logging
    * Updated datafile schema
        * Added 'parameters'/'variables' to datafile schema

* genie conf device
    * added 'timeout' argument to device.parse()



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ApplySelfSignedCert
        * Added new clean stage called apply self signed certificate

* common
    * Added
        * CopyRunToFlash Stage

* stages
    * IOSXE
        * CAT9K
            * Update the tftp boot to support stack devices
            * update the dailog.py for IOSXE devices
        * cat3k
            * Added dialog.py for cat3k
            * Added UT for TftpBoot clean stage apis
            * Added support for copy to device for stack devices
            * Added apis for change boot variable


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Connect to devices in rommon mode
    * Use reload service for install image stage



genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* bgp
    * Modified BGP conf model
        * Added support for 4 byte AS number support in BGP id

* nxos
    * Modified pim conf model
        * Added defensive check on attributes to avoid errors when attributes member is not populated
    * Added tunnel_encryption
        * Added tunnel encryption attribute for tunnel encryption interfaces



genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* genie.filetransferutils
    * Add support for http dynamic fileserver testbed config
    * Make fileserver subnet configuration optional



genie.libs.health
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* health_yamls
    * Updated pyats_health.yaml
        * Added timeout 120 secs to health_cpu/health_memory



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
    * Added 'configure access vlan' API
        * creating access vlan and adding interface
    * Added 'show mac address table| i count' API
        * api to display final mac count without displaying all mac address enties
    * Added 'udld port alert' API
        * configuring udld alert only mode on interface
    * Added 'trigger udld tx drop' API
        * configuring udld transmiddion drop on interface
    * Added API 'configure_ip_igmp_snooping_querier'
    * Added API 'unconfigure_ip_igmp_snooping_querier'
    * Added API 'configure_ip_igmp_snooping_vlan_querier'
    * Added API 'unconfigure_ip_igmp_snooping_vlan_querier'
    * Added API 'configure_ip_igmp_snooping_vlan_query_version'
    * Added API 'unconfigure_ip_igmp_snooping_vlan_query_version'
    * Added API 'configure_ipv6_mld_snooping'
    * Added API 'unconfigure_ipv6_mld_snooping'
    * Added API 'configure_ipv6_mld_snooping_querier_version'
    * Added API 'unconfigure_ipv6_mld_snooping_querier_version'
    * Added API 'configure_ipv6_mld_snooping_querier_address'
    * Added API 'unconfigure_ipv6_mld_snooping_querier_address'
    * Added API 'configure_ipv6_mld_snooping_vlan_querier_version'
    * Added API 'unconfigure_ipv6_mld_snooping_vlan_querier_version'
    * Added API 'configure_vrf_definition_stitching'
    * Added API 'unconfigure_vrf_definition_stitching'
    * Added API 'configure_static_ip_pim_rp_address'
    * Added API 'configure_static_ipv6_pim_rp_address'
    * Added API 'unconfigure_static_ip_pim_rp_address'
    * Added API 'unconfigure_static_ipv6_pim_rp_address'
    * Added API 'unconfig_disable_ipv6_routing'
    * Added API 'configure_ip_multicast_routing'
    * Added API 'unconfigure_ip_multicast_routing'
    * Added API 'configure_ip_multicast_vrf_routing'
    * Added API 'unconfigure_ip_multicast_vrf_routing'
    * Added API 'configure_interface_storm_control_level'
        * configure storm-control level under interface
    * Added API 'unconfigure_interface_storm_control_level'
        * unconfigure storm-control level under interface
    * Added API 'configure_interface_storm_control_action'
        * configure storm-control action under interface
    * Added API 'unconfigure_interface_storm_control_action'
        * unconfigure storm-control action under interface
    * Added API 'configure_platform_sudi_cmca3'
    * Added API 'unconfigure_platform_sudi_cmca3'
    * Added API 'configure_service_private_config_encryption'
    * Added API 'unconfigure_service_private_config_encryption'
    * Added API 'verify_Parser_Encrypt_decrypt_File_Status'
    * Added API 'verify_cmca3_certificates'
    * Added API 'verify_crypto_entropy_status'
    * Added API 'verify_crypto_pki_certificate'
    * Added API 'verify_hardware_slot'
    * Added API 'verify_hw_auth_status'
    * Added API 'verify_sudi_cert'
    * Added API 'verify_sudi_pki'
    * Added configure_hqos_policer_map API
        * API for configuring hqos policy map for service-policy.
    * Added API 'configure_nve_interface' in evpn
    * Added API 'unconfigure_nve_interface' in evpn
    * Added API 'configure_interface_pim' in mcast
    * Added API 'unconfigure_interface_pim' in mcast
    * Added config_mka_policy API
        * API for configuring MKA Policy globally and also interface level
    * Added unconfig_macsec_should_secure API
        * API for Removal of Should secure on interface level
    * Added config_macsec_should_secure API
        * API for Configuring Should secure on interface level
    * Added unconfig_mka_policy API
        * API for unconfiguring MKA Policy globally and also interface level
    * Added configure_default_mpls_mldp api
    * Added configure_mdt_data_mpls_mldp api
    * Added configure_mdt_data_threshold api
    * Added configure_mdt_partitioned_mldp_p2mp api
    * Added configure_mdt_preference_under_vrf api
    * Added configure_mdt_strict_rpf_interface_vrf api
    * Added configure_multicast_routing_mvpn_vrf api
    * Added configure_vpn_id_in_vrf api
    * Added unconfigure_mdt_data_threshold api
    * Added 'clear_mdns_cache' API
        * clears mDNS cache
    * Added 'clear_mdns_statistics_all' API
        * clears mDNS statistics
    * Added 'clear_mdns_statistics_sp_sdg' API
        * clears mDNS statistics sp(Service Peer)_sdg(Agent)
    * Added 'clear_mdns_statistics_servicepeer' API
        * clears mDNS statistics sp(Service Peer)
    * Added 'configure_mdns_boot_level_license' API
        * Configures mDNS boot level license
    * Added config_vlan_range API
        * To configure vlan for a range
    * Added unconfig_vlan_range API
        * To unconfigure vlan for a range
    * Added config_portchannel_range API
        * To configure portchannel for a range
    * Added 'unconfigure_ipv6_mld_snooping_querier_version' API
        * Added doc string to unconfigure.
    * Added 'configure_ipv6_mld_snooping_querier_address' API
        * Changed Args headline for ipv6_address and updated ipv6 MLD querier source IPv6 address
    * Added execute_issu_install_package API
        * To execute issu install packages on device
    * Added verify_wireless_management_trustpoint_name
        * Added new api to verify wireless management trustpoint
    * Added verify_pki_trustpoint_state
        * Added new api to verify crypto pki trustpoint
    * Added get_wireless_management_trustpoint_name
        * Added new api to get wireless management trustpoint certificate name
    * Added get_pki_trustpoint_state
        * Added new api to get crypto pki trustpoint key state
    * Added execute_self_signed_certificate_command
        * Added new file called execute.py where all execute commands can be written
        * Added api to execute command that installs self-signed certificate
    * Added enable_http_server
        * Added new file called configure.py where all configure commands can be written
        * Added api to configure  ip http server on controller
    * Added set_clock_calendar
        * Added api to configure valid clock calendar
    * Added configure_pki_trustpoint API
        * Configures Trustpoint on device
    * Added unconfigure_pki_trustpoint API
        * Unconfigures Trustpoint on device
    * Added configure_pki_export_pem API
        * Generates a certificate in device
    * Added configure_pki_authenticate_certificate API
        * Pastes the pagent certificate in the device
    * Added unconfigure_crypto_pki_server API
        * Unconfigures Crypto PKI server on device
    * Added configure_crypto_pki_server API
        * Configures Crypto PKI server on device
    * Added configure_pki_enroll_certificate API
        * Enrolls certificate on device
    * Added ignore modules argument for verify_module_status api
    * Added
        * Added new API config_port_security_on_interface, configuring port security on interface.
    * Added disable_ipv6_dhcp_server API
        * unconfigures ipv6 dhcp server  on interface
    * Added configure_dhcp_pool_ipv6_domain_name API
        * configures domain name under dhcp pool on device
    * Added enable_ipv6_address_dhcp API
        * enables ipv6 address dhcp on interface
    * Added disable_ipv6_address_dhcp API
        * disables ipv6 address dhcp on interface
    * Added configure_ipv6_ospf_mtu_ignore API
        * Configures ipv6 ospf mtu-ignore on interface
    * Added unconfigure_ipv6_ospf_mtu_ignore API
        * Unconfigures ipv6 ospf mtu-ignore on interface
    * Added configure_ipv6_ospf_routing_on_interface API
        * Configures ipv6 ospf routing instance on interface
    * Added unconfigure_ipv6_ospf_routing_on_interface API
        * Unconfigures ipv6 ospf routing instance on interface
    * Added unconfig_interface_ospfv3 API
        * unconfigures ospfv3 on interface

* utils
    * Added get_interface_attr_from_yaml
        * get attribute value of a interface from topology in testbed object

* clean/reload
    * Added an argument to ignore modules during check modules step.

* iosxr
    * Added ignore modules argument for verify_module_status api

* nxos
    * Added ignore modules argument for verify_module_status api

* added new api configure_control_policies, configuring policy-map.

* added new api clear_port_security, clearing port security stats, clear port-security all.

* added new api unconfig_vlan_tag_native, unconfig vlan dot1q tag native.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fix config_mka_keychain_on_interface API
        * API for Configuring Primary MKA Key chain and fallback MKA Key chain on interface level
    * Updated 'configure_mdns' API
        * Added if condition for creating only one service list with direction and definition name
    * Modified `verify_ip_mac_binding_in_network`
        * Added verify_reachable option to require entries to be reachable
    * Fixed `get_ip_theft_syslogs`
        * Corrected to support new syslog output
    * Modified `verify_module_status` API to ignore empty slots
    * Updated `get_md5_hash_of_file` API to use 180s default timeout
    * Updated health_cpu API
        * Added 'timeout' argument
    * Updated health_memory API
        * Added 'timeout' argument

* generic
    * Updated `copy_from_device` and `copy_to_device` APIs to support dynamic HTTP fileserver

* api utils
    * Modified api_unittest_generator
        * Proxy connection raises proper error message

* iosxr
    * Added c8000 platform for get_mgmt APIs
    * Updated health_cpu API
        * Added 'timeout' argument
    * Updated health_memory API
        * Added 'timeout' argument

* blitz
    * actions_helper
        * Fixed the issue with configure_dual
    * Added gnmi_util module for message constuction
        * Fixed OpenConfig module gNMI message building for complex RPCs.
        * Fixed "empty" error when gNMI return message does not validate zero value.
        * Negative range not validating return message values.
    * Added protobuf and cisco-gnmi dependency for genie.libs.sdk package
    * Updated rest_handler
        * Fixed 'save' handling in 'rest' action

* apic
    * Updated apic_rest_get API
        * Added order_by argument support

* nxos
    * Updated health_cpu API
        * Added 'timeout' argument
    * Updated health_memory API
        * Added 'timeout' argument
    * Updated nxapi_method_nxapi_rest API
        * Fixed wrong avariable name to show proper error message



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added MonitorCaptureStop parser
        * monitor capture {capture_name} stop
    * Added ShowCryptoPkiTimerDetail
        * show crypto pki timer detail
    * Added ShowCryptoPkiServerRequests
        * show crypto pki server {server} request
    * Added ShowIpv6MldSnoopingGroups
        * show ipv6 mld snooping address vlan {vlan_id}
    * Added class ShowLispPlatformStatistics
        * show lisp platform statistics
    * Added ShowLispSiteDetail
        * show lisp site detail
        * show lisp site name {site_name}
        * show lisp site {eid}
        * show lisp site {eid} instance-id {instance_id}
        * show lisp site {eid} eid-table {eid_table}
        * show lisp site {eid} eid-table vrf {vrf}
        * show lisp {lisp_id} site detail
        * show lisp {lisp_id} site name {site_name}
        * show lisp {lisp_id} site {eid}
        * show lisp {lisp_id} site {eid} instance-id {instance_id}
        * show lisp {lisp_id} site {eid} eid-table {eid_table}
        * show lisp {lisp_id} site {eid} eid-table vrf {vrf}
        * show lisp locator-table {locator_table} site detail
        * show lisp locator-table {locator_table} site name {site_name}
        * show lisp locator-table {locator_table} site {eid}
        * show lisp locator-table {locator_table} site {eid} instance-id {instance_id}
        * show lisp locator-table {locator_table} site {eid} eid-table {eid_table}
        * show lisp locator-table {locator_table} site {eid} eid-table vrf {vrf}
    * Added ShowLispEthernetServerDetail
        * show lisp instance-id {instance_id} ethernet server detail
        * show lisp instance-id {instance_id} ethernet server name {site_name}
        * show lisp instance-id {instance_id} ethernet server {eid}
        * show lisp instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ethernet server detail
        * show lisp eid-table vrf {vrf} ethernet server name {site_name}
        * show lisp eid-table vrf {vrf} ethernet server {eid}
        * show lisp eid-table vrf {vrf} ethernet server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server etr-address {etr_address}
    * Added ShowLispIpv4ServerDetail
        * show lisp instance-id {instance_id} ipv4 server detail
        * show lisp instance-id {instance_id} ipv4 server name {site_name}
        * show lisp instance-id {instance_id} ipv4 server { }
        * show lisp instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv4 server detail
        * show lisp eid-table {eid_table} ipv4 server name {site_name}
        * show lisp eid-table {eid_table} ipv4 server {eid}
        * show lisp eid-table {eid_table} ipv4 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv4 server detail
        * show lisp eid-table vrf {vrf} ipv4 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv4 server {eid}
        * show lisp eid-table vrf {vrf} ipv4 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server etr-address {etr_address}
    * Added ShowLispIpv6ServerDetail
        * show lisp instance-id {instance_id} ipv6 server detail
        * show lisp instance-id {instance_id} ipv6 server name {site_name}
        * show lisp instance-id {instance_id} ipv6 server {eid}
        * show lisp instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv6 server detail
        * show lisp eid-table {eid_table} ipv6 server name {site_name}
        * show lisp eid-table {eid_table} ipv6 server {eid}
        * show lisp eid-table {eid_table} ipv6 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv6 server detail
        * show lisp eid-table vrf {vrf} ipv6 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv6 server {eid}
        * show lisp eid-table vrf {vrf} ipv6 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server etr-address {etr_address}
    * Added class ShowDlepClients
    * Added class ShowDlepNeighbors
    * Modified ShowLispExtranet
        * Updated schema,regex patterns and logic to handle updated device output from show command
    * Added ShowCryptoEntropyStatus
        * show crypto entropy status
    * Added ShowPlatformSudiPki
        * show platform sudi pki
    * Added ShowPlatformHardwareAuthenticationStatus
        * show platform hardware authentication status
    * Added ShowCryptoIkev2StatsExt
        * show crypto ikev2 stats ext-service
    * Added ShowCryptoPkiServer
        * show crypto pki server
    * Added ShowCryptoSessionRemoteDetail
        * show crypto session remote {remote_ip} detail
    * Added ShowCryptoSessionRemote
        * show crypto session remote {remote_ip}
    * Added class ShowCtsRoleBasedSgtMapAll
        * show cts role-based sgt-map all
        * show cts role-based sgt-map all vrf <vrf> all
    * Added class ShowCtsSxpConnections
        * show cts sxp connections
        * show cts sxp connections vrf <vrf>
    * Added class ShowCtsSxpSgtMapBrief
        * show cts sxp sgt-map brief
        * show cts sxp sgt-map vrf <vrf> brief
    * Added ShowInterfacesSummary
        * show interfaces summary
        * show interfaces {interface} summary
    * Added ShowIpv6Mfib
        * show ipv6 mfib
        * show ipv6 mfib {group}
        * show ipv6 mfib {group} {source}
        * show ipv6 mfib verbose
        * show ipv6 mfib {group} verbose
        * show ipv6 mfib {group} {source} verbose
        * show ipv6 mfib vrf {vrf}
        * show ipv6 mfib vrf {vrf} {group}
        * show ipv6 mfib vrf {vrf} {group} {source}
        * show ipv6 mfib vrf {vrf} verbose
        * show ipv6 mfib vrf {vrf} {group} verbose
        * show ipv6 mfib vrf {vrf} {group} {source} verbose
    * Added ShowIpv6Mrib
        * added the new parser for cli "show ipv6 mrib route"
        * show ipv6 mrib route
        * show ipv6 mrib route {group}
        * show ipv6 mrib route {group} {source}
        * show ipv6 mrib vrf {vrf} route
        * show ipv6 mrib vrf {vrf} route  {group}
        * show ipv6 mrib vrf {vrf} route  {group} {source}
    * Added ShowIsisRibRedistribution
        * show isis rib redistribution
    * Added ShowLicenseTechSupport
        * show license tech support
    * Added ShowLispRegistrationHistory
        * 'show lisp {lisp_id} instance-id {instance_id} {address_family} server {eid} registration-history'
        * 'show lisp {lisp_id} instance-id {instance_id} {address_family} server registration-history'
        * 'show lisp {lisp_id} instance-id {instance_id} {address_family} server {address_resolution} {eid} registration-history'
        * 'show lisp instance-id {instance_id} {address_family} server registration-history'
        * 'show lisp server registration-history'
    * Added ShowPlatformHardwareChassisFantrayDetailSwitch
        * show platform hardware chassis fantray detail switch {mode}
    * Added ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll
        * show platform hardware chassis power-supply detail switch {mode} all
    * Added ShowPlatformSoftwareCpmSwitchB0CountersDrop
        * show platform software cpm switch {mode} B0 counters drop
    * Added ShowPlatformSoftwareCpmSwitchB0CountersPuntInject
        * show platform software cpm switch {mode} B0 counters punt-inject
    * Added ShowPlatformSoftwareCpmSwitchB0IpcDetail
        * show platform software cpm switch {mode} B0 ipc detail
    * Added ShowPlatformSoftwareCpmSwitchB0IpcBrief
        * show platform software cpm switch {mode} B0 ipc brief
    * Added ShowPlatformSoftwareCpmSwitchB0ControlInfo
        * show platform software cpm switch {mode} B0 control-info
    * Added ShowPlatformSoftwareCpmSwitchB0Resource
        * show platform software cpm switch {mode} B0 resource
    * Added ShowIdpromInterface
        * show idprom interface {mode}
    * Added ShowPlatformSoftwareBpCrimsonContentConfig
        * show platform software bp crimson content config
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Node
        * show platform software node cluster-manager switch {mode} B0 node {node}
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Local
        * show platform software node cluster-manager switch {mode} B0 local
    * Added ShowPlatformSoftwareTdlContentBpConfig
        * show platform software tdl-database content bp config {mode}
    * Added ShowPlatformSoftwareTdlContentBpOper
        * show platform software tdl-database content bp oper {mode}
    * Added ShowPlatformSoftwareNodeClusterManagerSwitchB0Counters
        * show platform software node cluster-manager switch {mode} B0 counters
    * Added ShowPlatformSoftwareBpCrimsonCounterOper
        * show platform software bp crimson content oper
    * Added ShowPlatformSoftwareBpCrimsonStatistics
        * show platform software bp crimson statistics
    * Added ShowStackwiseVirtualBandwidth
        * show stackwise-virtual bandwidth
    * Added ShowMdnsSdControllerDetail
        * Parser for Show Mdns-Sd Controller Detail
    * Fixed ShowDeviceTrackingDatabaseInterface parser
        * Modified regexp to match network_layer_address and link_layer_address
    * Fixed  ShowRunInterface parser
        * Added regexp to grep ipv6_nd_raguard_attach_policy and device_tracking_attach_policy
    * ShowIsisRib
        * Added the ability to parser the cli command `show isis rib flex-algo`
    * Added ShowLispIpv4ServerExtranetPolicyEid
        * show lisp instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv4 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy {prefix}
    * Added ShowLispIpv6ServerExtranetPolicyEid
        * show lisp instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv6 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy {prefix}
    * Added ShowPolicyMapTypeInspectZonePair
        * show policy-map type inspect zone-pair {zone_pair_name}
        * show policy-map type inspect zone-pair
    * Modified ShowVlanId
        * Added support vlan-name to be more diverse, including " ", "-", "_"

* iosxr
    * Added ShowEventManagerEnv
        * show event manager environment
        * show event manager environment all
        * show event manager environment | include {event_name}
    * Added ShowEventManagerPolicyRegistered
        * show event manager policy registered
        * show event manager policy registered {type}
        * show event manager policy registered {type} | include {eemfile_name}
    * Added ShowEventManagerPolicyAvailable
        * show event manager policy available
        * show event manager policy available {type}
        * show event manager policy available {type} | include {eemfile_name}
    * Added ShowRipIpv6
        * show rip ipv6
        * show rip ipv6 vrf {vrf}
    * Added ShowRipIpv6Statistics
        * show rip ipv6 statistics
        * show rip ipv6 vrf {vrf} statistics
    * Added ShowRipIpv6Database
        * show rip ipv6 database
        * show rip ipv6 vrf {vrf} database
    * Added ShowRipIpv6Interface
        * show rip ipv6 interface
        * show rip ipv6 vrf {vrf} interface

* generic
    * Modified ShowVersion
        * Added Optional <os_flavor> key to schema to better handle IOSXR show version output

* nxos
    * Added ShowForwardingIpv4Recursive
        * show forwarding ipv4 recursive
        * show forwarding ipv4 recursive vrf {vrf}

* ios
    * Added ShowPolicyMapTypeInspectZonePair
        * show policy-map type inspect zone-pair {zone_pair_name}
        * show policy-map type inspect zone-pair


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowMdnsSdSpSdgStatistics
        * Added support to agent and sp
    * Modified ShowMdnsSdSummaryVlan
        * Added support to agent and sp
    * Added TracerouteMPLSIPv4 parser
        * traceroute mpls ipv4 {addr} {mask}
    * Fixed ShowInterfacesStatusErrDisabled parser
        * Modified regexp to grep all kind of reasons
    * Fixed ShowFlowRecord Schema
        * Modified match_list and collect_list to Optional arg in schema as those are not mandate
    * Modified ShowAccessLists
        * Add support to role-based acl
    * Modified ShowIpPimTunnel
        * Modified to support different address family and vrf
    * Modified ShowIsisRibSchema
        * Added a new key to differentiate output by level type
        * Changed the flex algo key to contain a set of associated prefixes
        * No backwards compatibility
    * Modified ShowIsisRib
        * Modified a regex to parse lines starting with `Prefix-SID index`
    * Modified ShowSegmentRoutingTrafficEngPolicy
        * Added regex pattern p3_1 to handle different output
        * Added regex pattern p6_1 to handle different output
    * Modified ShowStormControl
        * Added support for pps/bps
        * Added support for command "show storm-control"
    * Modified ShowStormControl
        * Added support for Unknown-Unicast
    * Modified ShowInterfacesSwitchport
        * Fixed issue when parsing single interface that belongs to a port channel
    * Modified ShowLispServiceSummary
        * Fixed missing router ID when no banner
        * Added support for maximum db and map-cache values
    * Modified ShowRomVarSchema
        * Added "default_gateway,ip_address,crashinfo,subnet_mask" field to schema.
    * Modified ShowRomVar
        * Modified Regular Expression to handle if any value is provided with "" or without codes. Also modified to deal spaces in regular expression.
        * For few variables added len check for value. if value for that key is empty then that key will not be added to master key i.e rommon_variable.
    * Modified ShowBgpAllDetail
        * Updated the Schema to handle 'binding_sid' field
        * Added regex p20 and p20_1 to match the binding_sid

* generic
    * Modified ShowVersion
        * Modified schema key <model> to <pid>

* viptela
    * Modified ShowSystemStatus
        * Refactored parser to adhere to standard parser format
        * Modified almost all regexes and logic

* nxos
    * Modified ShowBgpSessions
        * Updated regex pattern p6_1 to split up 'nei' from 'linklocal_interfaceport'


