September 2026
==============

September 29 - Genie v26.9
--------------------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v26.9
    ``genie.lamp``, v26.9
    ``genie.libs.health``, v26.9
    ``genie.libs.clean``, v26.9
    ``genie.libs.conf``, v26.9
    ``genie.libs.filetransferutils``, v26.9
    ``genie.libs.ops``, v26.9
    ``genie.libs.parser``, v26.9
    ``genie.libs.robot``, v26.9
    ``genie.libs.sdk``, v26.9
    ``genie.telemetry``, v26.9
    ``genie.trafficgen``, v26.9




Changelogs
^^^^^^^^^^

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe/cat9k/c9800
    * Added the ``configure_wireless_management`` Clean stage to configure WMI from explicit stage arguments or ``device.management.wireless`` and verify the trunk VLAN, SVI state and address, and wireless management binding.
    * Added unit coverage for testbed fallback, complete missing-value reporting, readiness verification, and C9800-CL stage abstraction.
    * Updated the stage to require only mode-dependent values and to verify configured IPv6 WMI addresses.
    * Updated the stage to verify every requested static IPv4 WMI address, including secondary addresses.
    * Updated wireless binding verification to use the ``show wireless interface summary`` Genie parser without polling.

* iosxe
    * Added the ``EraseCertificates`` clean stage.
        * Erases certificate files matching configurable filename patterns.
        * Preserves certificates referenced by running-config or startup-config by default and fails safely when a reference is already missing.
        * Reports deleted files and certificate storage usage before and after cleanup.

* clean
    * Added ``testbed_config`` to Genie Clean stage parameters so stages can emit serializable devices and topology for the parent pyATS Clean engine to merge into the effective testbed.

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* clean
    * Modified the ``ConfigureManagement`` gateway verification to fail before pinging when no IPv4 or IPv6 management address is available.
    * Modified recovery_processor
        * Merge a failed device recovery result into the owning clean stage so the stage cannot remain passed while its recovery processor failed.
        * Preserve an existing stage result when it is worse than the recovery result.
    * Boot only IOS XE stack subconnections already in ROMMON with the configured golden or TFTP recovery image, then reconnect before clear-line or power-cycle recovery.
    * Improved recovery handling for HA devices with mixed enable and disable subconnections by avoiding unnecessary disconnects and reconnects.
    * Updated device recovery to clear the mapped terminal-server console lines instead of issuing ``clear line 0`` through the device management connection.
    * Improved recovery handling for stale or closed connections by avoiding commands on invalid sessions and preserving the original connection failure.

* recovery_image
    * Fixed remote recovery-image size checks to use the server protocol's FileUtils implementation instead of the device filesystem implementation.
    * Kept canonical recovery-image paths in clean data and resolves short-path aliases internally only when copying over the production HTTP(S) transport.
    * Added a disk-space check before recovery-image copies. When size verification is enabled, the stage deletes unprotected files as needed while preserving configured golden files and recovery-image targets that are not being replaced.

* clean/stages
    * Increased the default IOS XE install_remove_inactive timeout from 180 to 300 seconds to allow package removal to complete on slower devices.
    * Boot the IOS XE installed image from the generated ``packages.conf`` during the install image reload.
    * Modified ``copy_to_device`` to automatically protect an existing target image when the copy operation is skipped, preventing later free-space cleanup from deleting an image required by subsequent clean stages.

* iosxe
    * Kept the controller-mode reload dialog active after the ``Press RETURN to get started!`` prompt so that authentication and the default-admin password change can complete before the final IOS XE prompt.
    * Added regression coverage for the controller-mode authentication flow and reload timeout propagation.
    * Restored the post-reconnect autoboot step in the ROMMON boot flow.

* iosxe/cat9k/c9800
    * Organized C9800 clean stages under the C9800 abstraction.
    * Retained the AP association stage and removed the unused AP mode, RRM DCA channel, installation mode, AP transmit power, HA state, AP fabric, access tunnel, and wireless process stages. Equivalent reusable APIs are available from the C9800 SDK package.

* iosxe/cat9k/c9800/c9800_cl
    * Organized C9800-CL clean stages under the C9800-CL submodel abstraction.
    * Updated the self-signed certificate stage to prefer the Clean YAML password, fall back to the device certificate credential password, and skip when neither is configured.

genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * Added
        * `isolate` attribute support for service-acceleration conf model in NXOS.

genie.libs.filetransferutils
""""""""""""""""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxr
    * Added automatic temporary transfer routing to FileUtils.
        * A temporary host route towards the file transfer endpoint is now installed for the duration of a copy and removed afterwards. This is the default behaviour on IOSXR and requires no opt-in flag.
        * The route is only installed when the transfer endpoint is a remote IP address, a management gateway is declared in the testbed, and the device does not already reach the endpoint via that gateway. A DNS hostname or a device local path (``disk0:``, ``harddisk:`` ...) never triggers a route.

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified
        * File transfers temporarily use the requested source interface and restore the original interface configuration afterward.

* filetransferutils
    * Modified
        * HTTP filesize checks now include the HTTP status, reason, redirect URL, and relevant response headers in diagnostic errors while redacting URL credentials.

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* iosxe
    * Added configure_autoboot API
        * Sets the configuration register to 0x2102.
    * Added device tracking API for IOSXE.
        * API to verify device tracking database: verify_device_tracking_database
    * Added unit test coverage for the new API.
    * Added certificate storage APIs for inventory, reference discovery, deletion, verification, and storage usage reporting.
    * Allowed extra time to inventory large certificate directories over slow console connections.
    * Made stack deletion idempotent when IOS XE synchronizes an active member's certificate removal to its standby member.
    * Added stack and dual-RP implementations that operate through connected member subconnections and their local ``nvram:`` storage.
    * Added VRF and global address-family route-replicate configure APIs.
        * API to configure_vrf_route_replicate_from_vrf.
        * API to unconfigure_vrf_route_replicate_from_vrf.
        * API to configure_global_route_replicate_from_vrf.
        * API to unconfigure_global_route_replicate_from_vrf.
    * Added unit test coverage for the new APIs.
    * Added verify_ip_access_list
        * API to verify IP access list
    * Added BGP VRF cleanup APIs.
        * API to unconfigure_bgp_address_advertisement.
        * API to unconfigure_bgp_advertise_l2vpn_evpn.
    * Added unit test coverage for the new APIs.
    * Added iosxe dot1q tunnel configuration view API support
        * New API support for 'configure_interface_switchport_dot1q_tunnel' CLI command to configure dot1q tunnel on interface
    * Added SDK API support for
        * configure_interface_spanning_tree_port_priority
        * configure_interface_spanning_tree_vlan_cost
        * unconfigure_interface_spanning_tree_vlan_cost
        * configure_spanning_tree_pathcost_method
    * Added unit test coverage for spanning-tree APIs.
    * Added running-config verify APIs for IOSXE.
        * API to verify_show_running_config_section.
    * Added unit test coverage for the new API.

* iosxe/cat9k/c9800
    * Added ``configure_wireless_management`` API to configure the C9800 WMI uplink, Layer 3 interface, routes, wireless binding, and AP management credentials.
    * Updated ``configure_management_ip`` to allow callers to disable fallback to the generic device management VRF, keeping the WMI in the global VRF.
    * Added unit coverage for WMI orchestration, input validation, same-VRF gateway conflict handling, and management VRF fallback behavior.
    * Corrected ``configure_management_routes`` to render IPv6 entries with ``ipv6 route`` commands, including VRF routes.
    * Added APIs
        * configure_ap_tx_power
        * configure_rrm_dca_channel
        * verify_ap_fabric_summary
        * verify_ap_mode
        * verify_access_tunnel_summary
        * verify_ha_state
        * verify_installation_mode
        * verify_wireless_process

* iosxr
    * Added configure_static_routing_route
        * API to configure a static route, taking ``prefix``, ``next_hop``, an optional ``address_family`` (``ipv4``/``ipv6``) and an optional ``vrf``. Returns the configuration that was applied and raises ``SubCommandFailure`` when the device rejects it.
    * Added unconfigure_static_routing_route
        * API to remove a static route, taking the same arguments as ``configure_static_routing_route`` so only the exact route that was configured is removed.
    * Added get_routing_route_next_hop
        * API to look up the next hop details for a route, taking ``route``, an optional ``address_family`` (derived from ``route`` when not given) and an optional ``vrf``.

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_mdns_gateway_globally
        * test_api_unconfigure_mdns_global_service_buffer
        * test_api_unconfigure_mdns_location_filter
        * test_api_unconfigure_mdns_remote_cache_enable
        * test_api_unconfigure_mdns_remote_cache_max_limit
        * test_api_unconfigure_mdns_remote_purge_timer
        * test_api_unconfigure_mdns_service_policy
        * test_api_unconfigure_mdns_service_policy_vlan
        * test_api_unconfigure_mdns_trust
        * test_api_unconfigure_service_type_mdns_service_definition
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified configure_interface_storm_control_level API
        * Updated the API to return the output of the configuration command instead of None.
        * Updated unit test in test_api_configure_interface_storm_control_level.py accordingly.
    * Improved cleanup performance by verifying free space with a bounded filesystem query after each deletion batch.
    * Protected running images and system, configuration, and NVRAM files.
    * Updated configure_autoboot to use execute_set_config_register so platform-specific boot behavior and HA connection handling are preserved for IOS XE devices.
    * Added C9800 and C9800-CL support for the full ``config-register 0x2102`` command. Physical Catalyst 9000 platforms continue to use their ``boot manual`` equivalent.
    * Modified configure_ikev2_profile_pre_share
        * modified configure_ikev2_profile_pre_share
    * Modified send_break_boot API to stop sending additional console break characters after detecting the ROMMON switch: prompt.
    * Modified configure_management_master_key to increase the master key configure timeout from 120s to 300s, fixing a ConfigureManagement clean stage timeout on some platforms (e.g. IE9xxx) when no master key is yet configured and key generation takes longer than the previous timeout. Also added defensive handling for the 'New key:' and 'Confirm key:' prompts in case a platform prompts interactively instead of accepting the key inline.
    * Improved IE3K and IE9K ROMMON recovery error reporting when the default ROMMON boot command fails and no golden image is available.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_ipv6_mld_snooping
        * test_api_configure_ipv6_mld_snooping_querier
        * test_api_configure_ipv6_mld_snooping_querier_version
        * test_api_configure_ipv6_mld_snooping_vlan_querier_version
        * test_api_unconfigure_ipv6_mld_snooping
        * test_api_unconfigure_ipv6_mld_snooping_querier
        * test_api_unconfigure_ipv6_mld_snooping_querier_version
        * test_api_unconfigure_ipv6_mld_snooping_vlan_querier_version
        * test_api_config_no_keepalive_intf
        * test_api_config_qinq_encapsulation_on_interface
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Fixed IE3K ROMMON recovery when hostname learning is enabled and the configured hostname differs from the device hostname.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_interface_template_with_default_ipv6_nd_raguard_policy
        * test_api_configure_ipv6_dhcp_guard_on_interface
        * test_api_configure_ipv6_nd_raguard_on_interface
        * test_api_remove_device_tracking_policy
        * test_api_unconfigure_device_tracking_binding
        * test_api_unconfigure_device_tracking_on_interface
        * test_api_unconfigure_ipv6_dhcp_guard_on_interface
        * test_api_unconfigure_ipv6_nd_raguard_on_interface
        * test_api_configure_debug_snmp_packets
        * test_api_configure_logging_snmp_trap
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified configure_ospf_routing
        * api configure_ospf_routing now supports segment routing, fast-reroute, microloop, flex-algo, and bfd options
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_dynamic_path_in_tunnel
        * test_api_unconfigure_ip_rsvp_bandwidth
        * test_api_unconfigure_ldp_discovery_targeted_hello_accept
        * test_api_config_ip_multicast_routing_vrf_distributed
        * test_api_config_ip_pim
        * test_api_config_ip_pim_vrf
        * test_api_config_multicast_routing_mvpn_vrf
        * test_api_config_pim_acl
        * test_api_config_rp_address
        * test_api_config_standard_acl_for_ip_pim
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Modified send_break_boot
        * Fixed break-boot recovery after a refused console connection to use the actual detected device state and reliably reach ROMMON.
        * Preserved existing connected and multi-console behavior.
    * Enhanced ``configure_management_ntp``
        * Added support for configuring the NTP server in the management VRF.
    * Modified the following unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_switchport_port_security_maximum
        * test_api_configure_radius_server
        * test_api_configure_tacacs_server
        * test_api_unconfigure_radius_server
        * test_api_clear_device_tracking_counters
        * test_api_clear_device_tracking_database
        * test_api_clear_device_tracking_messages
        * test_api_configure_device_tracking_on_interface
        * configure_interface_template_with_default_device_tracking_policy
        * configure_interface_template_with_default_ipv6_dhcp_guard_policy
    * Removed mock_data.yaml files for the above tests as they are no longer needed
    * Fixed question-mark command cleanup to send Ctrl-A followed by Ctrl-K instead of Ctrl-C.
    * Added unit coverage to verify the control sequence used by ``question_mark_retrieve``.
    * Modified unconfigure_key_config_key_password_encrypt
        * Added backward-compatible password argument alongside old_key
        * no key config-key password-encrypt
    * Removed duplicate unconfigure_key_config_key_password_encrypt from platform
    * Modified execute_set_config_register
        * Added the optional preserve_console_speed argument. At rommon, when explicitly enabled for '0x0', writes each connection's hex(current & 0x1820) so its console-speed bits survive.
        * Retained the Cat9K manual-boot behavior; Cat9K does not execute confreg when console-speed preservation is requested.
        * Added support for the argument to the C9800 override, which retains the IOS-XE config-register behavior.
    * Modified password_recovery
        * Explicitly requests console-speed preservation when setting '0x0'.

* generic
    * Improved ``free_up_disk_space`` reliability and safety by batching deletions, reusing directory listings, and stopping when free space cannot be verified.

* apic
    * Restricted cleanup to valid regular files while preserving protected-file behavior.

* iosxr
    * Improved handling of regular files, directories, and symlinks during cleanup.

* nxos
    * Restored cleanup of file entries from ``dir`` output without permission metadata while excluding directory names ending in ``/``.

* iosxe/cat9k/c9800
    * Organized C9800 API tests under the Cat9K C9800 hierarchy.

* iosxe/cat9k/c9800/c9800_cl
    * Moved the management-IP API that defaults to ``no switchport`` under the C9800-CL submodel hierarchy so physical C9800 devices use the generic IOS XE behavior.
    * Moved GRUB-specific boot interruption defaults from physical C9800 to C9800-CL.

* iosxe/ir1k/ir1101
    * Added a platform-specific configure_no_boot_manual override
        * Uses the existing configure_autoboot API to set the configuration register to 0x2102 instead of sending the unsupported no boot manual command.

--------------------------------------------------------------------------------
                                    Modified
--------------------------------------------------------------------------------

* iosxe
    * Enhanced "execute_monitor_capture_access_list"
        * Added optional parameters interface,direction,file_path

genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* nxos
    * Added ShowNxsecureStatus
        * show nxsecure status
    * Modified ShowIpMrouteSummary
        * show ip mroute summary count
    * Added ShowHardwareProfileForwardingMode
        * show hardware profile forwarding-mode
    * Added ShowMvrInterface
        * show mvr interface
    * Added ShowSystemRoutingMode
        * show system routing mode
    * Added ShowProcessesMemoryShared
        * show processes memory shared
    * Added ShowIpv6PimStatistics
        * show ipv6 pim statistics
    * Added ShowDampeningInterface
        * show dampening interface
    * Added ShowPolicyMapInterfaceControlPlane
        * show policy-map interface control-plane
        * Added schema and parser support for byte and packet transmitted and dropped counters.
        * Added regex handling for byte and packet counter units.
        * Added optional schema support for offered, conformed, violate, and violated rate sections.
        * Added golden fixtures for byte counter, packet-only, and empty output.
    * Added ShowIcamScaleMulticastRouting
        * show icam scale multicast-routing
    * Added ShowCandidateSummary
        * show candidate summary
        * show candidate summary committed
        * show candidate summary pending
    * Added ShowIpPimVrfInternal
        * show ip pim vrf internal
        * Parsed RP change and PFM SD state as booleans
    * Added ShowIpNatTimeout
        * show ip nat timeout
    * Added ShowIpMrouteDetail
        * show ip mroute detail
        * Added schema and regex support for detailed multicast route counters, route client counts, data-created state, statistics, incoming interfaces, and outgoing interfaces.

* iosxe
    * Modified ShowInventory revision 1
        * Added a member inventory view that preserves member-qualified chassis, supervisor, line-card, and descendant records without changing the existing main and slot trees.
    * Added C9250 support for C9350-compatible parsers
        * show platform hardware fed qos scheduler sdk interface
        * show platform hardware fed qos queue stats interface
        * show platform hardware fed qos queue config interface
        * show platform hardware fed qos queue stats internal port_type punt queue
        * show platform software fed active acl info db detail
        * show platform software fed active punt asic cause brief
        * show platform software fed switch active matm macTable
        * show inventory
        * show switch stack-ports summary
    * Added ShowDeviceTrackingAnchors
        * show device-tracking anchors
        * show device-tracking anchors vlan {vlan}
    * Added ShowPlatformSoftwareFedSwitchActivePbrUsageRouteMap
        * Added parser for 'show platform software fed switch {switch_var} pbr usage route-map {route_map}' command.
    * Added ShowPlatformSoftwareFedSwitchActivePbrInfoRouteMap
        * Added parser for 'show platform software fed switch {switch_var} pbr info route-map {route_map}' command.
    * Added C9250 support to ShowPlatformTcamUtilization
        * show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization
        * show platform hardware fed active fwd-asic resource tcam utilization
        * show platform hardware fed switch {mode} fwd-asic resource tcam utilization
        * show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization {asic}
        * show platform hardware fed active fwd-asic resource tcam utilization {asic}
        * show platform hardware fed switch {mode} fwd-asic resource tcam utilization {asic}
    * Added ShowIpPortsAll
        * show ip ports all
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * Added schema and parser for 'show platform hardware fed switch {switch_num} qos queue stats interface {interface}'
        * Added schema and parser for 'show platform hardware fed active qos queue stats interface {interface}'
    * Added ShowEnvironmentAll
        * show environment all
    * Added ShowPlatformHardwareVoltageMarginRpActive
        * show platform hardware voltage margin rp active
    * Added ShowDhcpServerTrackingDatabase
        * show dhcp-server-tracking database
        * show dhcp-server-tracking database vlan {vlan_id}
    * Added ShowDhcpServerTrackingDatabaseDetail
        * show dhcp-server-tracking database detail
        * show dhcp-server-tracking database vlan {vlan_id} detail

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* ios
    * Modified ShowInventory
        * Accept inventory records whose NAME field is empty.
        * Initialize record context so a malformed orphan PID line is ignored instead of raising an unbound-local exception.

* iosxe
    * Modified ShowPlatformHardwareFedSwitchForwardLastSummary parser
        * Updated fields Optional.
    * Modified ShowMonitorCaptureBufferDetailed
        * Added support for parsing "request_frame" and "response_time"
    * Modified ShowIpInterface
        * Added support for parsing the optional ``(host-routing)`` suffix on the Local Proxy ARP status line.
        * Added the optional ``local_proxy_arp_host_routing`` field.
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface to C9400
        * Reused the C9610 VOQ/ASIC queue statistics parser for c9400 devices.
    * Modified ShowIpRouteSchema schema
        * Added optional vrf under next_hop.outgoing_interface.<interface>.
    * Modified ShowIpRoute parser
        * Updated parsing logic in the shared route parser: %vrf suffixes are now split from outgoing interface names and stored as vrf.
    * Modified ShowEnvironmentAll
        * Added support for C9400 output with optional power-supply summaries and table-based fantray states.
    * Added ShowPlatformSoftwareFedSwitchActiveAclInfoSdkDetail
        * Fix the regex to capture the asic number in the output of 'show platform software fed switch {switch_num} acl info sdk detail'
    * Fix ShowPlatformSoftwareFedQosInterfaceIngressNpd
        * Fix the regex to capture the port_oid and system_port_oid
    * ShowPlatformSoftwareFedQosInterfaceIngressSdkDetailed
        * Fix regex p7 to use (Asic|ASIC) to capture the asic number in the output of 'show platform software fed switch {switch_num} qos interface ingress sdk detailed'
    * ShowFlowMonitorCache
        * Added timeout optional variable with default value of 300 seconds
    * Modified ShowSdmPrefer
        * Updated the L3 Multicast entries regex to support the optional ``(Stats)`` label and numeric statistics annotation.
    * Modified ShowRouteMapAllSchema schema
        * Added support for ip tos and ipv6 precedence set clauses
    * Modified ShowRouteMapAll parser
        * REGEX logic update to match ip tos <value> and ipv6 precedence <value>
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed
        * Added support for ACL ACE details that begin with ``Class id`` when the ``IPV4/IPv6 ACE Key/Mask`` marker is absent.
        * Prevented an ``UnboundLocalError`` while parsing this output format.
        * Added corresponding golden parser coverage.

* iosxr
    * Modified ShowVrfAllDetail
        * Modified regex <p4_1> to capture all interface names
            * Replaced the previous regex that relied on specific interface prefixes (e.g., Gi, Bun, Ten, etc.) with a more general pattern.
        * Introduced `in_interfaces_section` flag for accurate section tracking
    * Modified ShowControllersOpticsAppselAdvertised
        * Updated parser to revise the pattern to accept any non-pipe content in each table cell. This basically means to allow letters, digits, whitespace, parentheses, dots, hyphens, '/', comma etc

* nxos
    * Modified ShowNveInterfaceDetail
        * Added fabric_convergence_time, fabric_convergence_time_left, and multisite_fabric_advertise_pip_l3 keys to the schema.
        * Added regex patterns p27, p28, and p29 to parse Fabric convergence time, Fabric convergence time left, and Multisite fabric-advertise-pip l3 configured output.
