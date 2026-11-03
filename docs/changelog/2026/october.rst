October 2026
==========

 - Genie v26.10
---------------



.. csv-table:: New Module Versions
    :header: "Modules", "Version"

    ``genie``, v26.10
    ``genie.lamp``, v26.10
    ``genie.libs.health``, v26.10
    ``genie.libs.clean``, v26.10
    ``genie.libs.conf``, v26.10
    ``genie.libs.filetransferutils``, v26.10
    ``genie.libs.ops``, v26.10
    ``genie.libs.parser``, v26.10
    ``genie.libs.robot``, v26.10
    ``genie.libs.sdk``, v26.10
    ``genie.telemetry``, v26.10
    ``genie.trafficgen``, v26.10




Changelogs
^^^^^^^^^^

genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* cheetah/ap
    * Added the ``ConfigureManagement`` clean stage.

* generic clean stages
    * Added optional endpoint diagnostics to ``ping_server``. On its first failed ping, the stage calls the Genie SDK collector to log Cisco and configured Linux VM state before retrying. Diagnostic failures do not change the ping result.

* clean/stages/cheetah/ap and clean/stages/iosxe/cat9k/c9800
    * Added coordinated C9800 WLC/AP registration with readiness tracking, registration verification, failure diagnostics, and parallel AP registration.

* clean/stages/iosxe
    * Added an optional ``shell`` boolean to the CopyToDevice stage schema and forwarded it to the SDK ``copy_to_device`` API to select the IOS XE shell-based FileUtils transfer path. Defaults to False to preserve the existing transfer behavior.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified SetControllerMode clean stage to publish the verified post-Clean device platform for parent-process testbed reconstruction.
    * Preserved the connection ``via`` selected by the Clean connect stage across controller-mode reconnects.
    * Keep the SD-WAN recovery worker compatible with SDK dispatchers that do not pass the console start command, and preserve the original Clean stage failure when device recovery cannot restore the device. Prevent an already-destroyed Unicon connection from blocking the console-speed recovery retry, and prevent disconnected-device verification errors from masking the original recovery result.
    * Updated InstallImage clean stage to commit activated and uncommitted images only once when ``show install active`` reports multiple locations, such as a dual-RP device.
    * Fixed ROMMON TFTP boot with wrapped Clean image/file metadata. Boot retries now keep the provider-selected TFTP image and recovery options.
    * Reject invalid or ambiguous ROMMON TFTP image metadata before boot.
    * Modified the IOS XE SD-WAN Connect stage to preserve an existing connection and fail when connection recovery is unsuccessful.
    * Added regression tests for the updated connection behavior.
    * Modified SetControllerMode to preserve or accept the connection ``via`` used for internal reconnects when a device has multiple connections.

* image handling
    * Standardized image paths after platform validation without changing supported image roles or multi-file package and SMU collections.
    * Reject terminal control characters and surrounding whitespace in image paths.

* clean/stages
    * When an IOS XE install reports ISSU in progress or an already added package, inspect the ISSU and install state. Clear only a known stale TFTP ISSU leftover (failed or aborted ISSU) without SMUs with the existing API, save the configuration, and retry the install. Wait for the command prompt on recoverable failure footers and preserve the install error if state diagnostics fail.

* clean/stages/iosxe
    * Skip the post-reload ``install commit`` when the install command already includes ``commit``.

--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* clean/stages/cheetah/ap and clean/stages/iosxe/cat9k/c9800
    * PrimeAp discovers the target controller and resolves WLC aliases during verification.

genie.libs.conf
"""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added ParsedInterfaceName
        * Added support for optics port names such as '0/0/2/-PORT-0', which the base parser does not recognize
        * All other interface names continue to be parsed by the base class

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* ios-xe
    * Modified interface configuration models to classify AppGigabitEthernet and FiveGigabitEthernet ports as physical Ethernet interfaces.

* ios-xr
    * Modified ParsedInterfaceName to publish structured rack, slot, CPU instance, port, CPU path, and RSIP fields for CPU-qualified interface names.

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* platform ops
    * IOSXE
        * Added normalized member inventory, member fallback, modularity, chassis type, confidence, and member-count evidence for stacks, StackWise Virtual systems, and dual-route-processor systems.
        * Publish member-qualified modular cards, MPAs, and optics in the slot tree so consumers do not parse inventory commands independently.
        * Treat any non-Ready stack or StackWise Virtual member, including transitional states, as inconclusive, and replace stale member inventory on relearn.
    * IOSXR
        * Added normalized modularity, dual-route-processor, and fixed-system standalone evidence from learned platform data.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxr
    * Modified Platform (rev1)
        * chassis_sn now uses the show inventory Rack 0 serial when present. show diag details / admin show diag chassis (including the Rack 0 Top Assembly and Second Serial Number blocks) are used only as a fallback, and a mismatch with inventory is logged as a warning. Fixes NCS5500 fixed chassis reporting the board serial.

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* generic sdk apis
    * Added ``collect_ping_failure_diagnostics`` to capture Cisco and optional Linux endpoint state immediately after a failed ping. The API logs each command result and continues if a diagnostic command fails.

* iosxe
    * Added IE3K and IE9K ROMMON recovery support for emergency images in ``emgy:`` and ``emgy0:``. Intentional ROMMON boot now tries emergency images before the configured Clean recovery image and then tries normal boot-filesystem images in the platform's configured regex order.

* sdk/apis/iosxe/cat9k/c9800/platform/get
    * Added C9800 APIs to verify AP registration and collect bounded failure diagnostics, including AP uptime.

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified device_recovery_boot to pass the console start command and connection index to the selected IOS XE SD-WAN recovery worker.
    * Modified the following VLAN API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * config_vlan_range
        * config_vlan_tag_native
        * configure_vtp_domain
        * configure_vtp_password
        * configure_vtp_pruning
        * configure_vtp_trunk_interface
        * configure_vtp_version
        * unconfig_ip_on_vlan
        * unconfigure_default_switchport_trunk_vlan
        * execute_vtp_primary
    * Removed the mock_data.yaml fixtures for these tests.
    * Fixed recursive disk cleanup to skip directories that disappear during traversal and continue processing other removable files.
    * Refactored the following multicast API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_ipv6_pim_bsr_candidate_rp
        * test_api_configure_ipv6_pim_rp_address
        * test_api_configure_mld_version
        * test_api_configure_pim_register_source
        * test_api_configure_static_ip_pim_rp_address
        * test_api_configure_static_ipv6_pim_rp_address
        * test_api_disable_ip_igmp_snooping_report_suppression
        * test_api_enable_ip_igmp_snooping_report_suppression
        * test_api_unconfig_ip_multicast_routing_vrf_distributed
        * test_api_unconfig_ip_pim_vrf
    * Removed the mock_data.yaml files for these tests because they are no longer needed.
    * Modified the following NAT API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * execute_clear_ip_nat_translation
        * execute_clear_nat64_statistics
        * execute_clear_nat64_statistics_failure
        * execute_clear_nat64_statistics_global
        * execute_clear_nat64_statistics_interface
        * execute_clear_nat64_statistics_pool
        * execute_clear_nat64_statistics_prefix_stateful
        * execute_clear_nat64_translations_all
        * execute_clear_nat64_translations_protocol
        * execute_clear_nat_translation
    * Removed the mock_data.yaml fixtures for these tests.
    * Refactored the following multicast API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_ip_igmp_ssm_map_enable
        * test_api_configure_ip_pim_rp_candidate_priority
        * test_api_configure_ip_igmp_ssm_map_query_dns
        * test_api_configure_ip_msdp_cache_sa_state
        * test_api_configure_ip_msdp_peer
        * test_api_configure_ip_pim_bsr_candidate
        * test_api_configure_ip_pim_enable_bidir_enable
        * test_api_configure_ip_pim_rp_address
        * test_api_configure_ip_pim_ssm
        * test_api_configure_ip_msdp_vrf_peer
    * Removed the mock_data.yaml files for these tests because they are no longer needed.
    * Modified C8KV device_rommon_boot
        * Preserve the configured GRUB golden-image entry when recovery also contains TFTP image metadata.
    * Modified device_rommon_boot
        * Stop a ROMMON TFTP retry when the assignment returns a set usage error, before readback or boot.
    * Modified
        * configure_snmpv3_user
            * Added read_view, write_view as optional
        * configure_radius_server_secure
            * modified `SECURITY WARNING` message as log.debug
        * unconfigure_snmp_server_user
            * No entry/changes
        * configure_snmp_host_version
            * Added security_level as optional
            * Added input validation for CR/LF injection
        * unconfigure_snmp_host_version
            * Added security_level as optional
            * Added input validation for CR/LF injection
        * configure_snmp_server_host
            * Added security_level as optional
            * Added input validation for CR/LF injection
        * unconfigure_snmp_server_host
            * Added security_level as optional
            * Added input validation for CR/LF injection
        * copy_startup_config_to_scp
            * Added vrf as optional parameter to append vrf to the SCP copy command
    * Refactored the following OSPF API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_ip_ospf_mtu_ignore
        * test_api_unconfigure_ipv6_ospf_mtu_ignore
        * test_api_unconfigure_ipv6_ospf_routing_on_interface
        * test_api_unconfigure_ipv6_router_ospf
        * test_api_unconfigure_neighbor_under_ospf
        * test_api_unconfigure_ospf_area_type
        * test_api_unconfigure_ospf_cost
        * test_api_unconfigure_ospf_from_interface
        * test_api_unconfigure_ospf_network_non_broadcast
        * test_api_unconfigure_ospf_on_device
    * Removed the mock_data.yaml files for these tests because they are no longer needed.
    * Fixed ROMMON TFTP configuration, including HA and C9200 boot URLs, to use actual image paths rather than serialized Clean metadata.
    * Reject invalid or ambiguous TFTP images before boot. An explicit TFTP request no longer falls back to a configured golden image; existing local golden-image behavior is unchanged.
    * Reuse the provider-selected TFTP transport path across inner and outer boot retries without translating it again.
    * Stop boot on ROMMON command usage errors. On C9300/C9200 Cat9k paths, verify the environment value before each boot and reject missing or mismatched values rather than booting a stale image.
    * Matching Clean and SDK builds are required for TFTP image normalization; older Clean builds fail with an actionable import error before boot.
    * Modified send_break_boot
        * Honored configured terminal-server login prompts during breakboot reconnect and waited for device boot output before sending BREAK.
    * Refactored the following multicast API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_clear_ipv6_mld_counters
        * test_api_configure_debug_ip_pim
        * test_api_configure_igmp_version
        * test_api_configure_ip_forward_protocol_nd
        * test_api_configure_ip_igmp_access_group
        * test_api_configure_ip_igmp_join_group_source
        * test_api_configure_ip_igmp_snooping_last_member_query_interval
        * test_api_configure_ip_igmp_snooping_tcn_flood
        * test_api_configure_ip_igmp_snooping_vlan_mrouter_interface
        * test_api_configure_ip_igmp_ssm_map
    * Removed the mock_data.yaml files for these tests because they are no
    * Modified C9800-CL device_rommon_boot
        * Preserve the configured GRUB golden-image entry when recovery also contains TFTP image metadata.
    * Refactored the following API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_clear_dmvpn
        * test_api_clear_dmvpn_statistics
        * test_api_clear_ip_nhrp
        * test_api_clear_ipv6_nhrp
        * test_api_clear_bgp_all_as
        * test_api_clear_ip_bgp
        * test_api_clear_ip_bgp_af_as
        * test_api_execute_crypto_pki_server
        * test_api_execute_test_opssl_nonblockingsession_client
        * test_api_execute_test_opssl_nonblockingsession_server_stop
    * Removed the mock_data.yaml files for these tests because they are no longer needed.
    * Refactored the following multicast API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_configure_ip_pim_vrf_ssm_default
        * test_api_configure_ipv6_mld_access_group
        * test_api_configure_ipv6_mld_join_group_acl
        * test_api_configure_ipv6_mld_snooping_enhance
        * test_api_configure_ipv6_mld_snooping_vlan_mrouter_interface
        * test_api_configure_ipv6_mld_snooping_vlan_static_interface
        * test_api_configure_ipv6_mld_vlan
        * test_api_configure_ipv6_mld_vlan_immediate_leave
        * test_api_configure_ipv6_multicast_routing
        * test_api_configure_ipv6_pim_bsr_candidate_bsr
    * Removed the mock_data.yaml files for these tests because they are no longer needed.
    * Refactored the following API unit tests to use unittest.mock.Mock instead of mock_device_cli
        * test_api_unconfigure_interface_ospfv3_ipsec_esp
        * test_api_unconfigure_ip_prefix_list
        * test_api_unconfigure_ospfv3_ipsec_ah
        * test_api_unconfigure_ospfv3_ipsec_esp
        * test_api_unconfigure_ospfv3_network
        * test_api_unconfigure_redistribute_eigrp_under_ospf
        * test_api_unconfigure_route_map
        * test_api_clear_ip_ospf_rib
        * test_api_unconfig_pim_acl
        * test_api_monitor_event_trace_clear
    * Removed the mock_data.yaml files for these tests because they are no longer needed.
    * Modified request_system_shell to apply its timeout to commands executed inside the system shell.
    * Modified request_system_shell to attempt a bounded return to enable mode after a command failure without replacing the original error.
    * Added Cat8k send_break_boot
        * Interrupt boot at the system bootstrap banner using Telnet BREAK to reach ROMMON during password recovery.
    * Updated generic send_break_boot
        * Match the default console activity pattern on three or more consecutive dots.
        * Handle terminal-server authentication prompts while connecting to interrupt boot.

* iosxe/cat9k/c9800
    * Added a platform-specific configure_no_boot_manual override
        * Uses the existing configure_autoboot API to set the configuration register to 0x2102 instead of sending the unsupported no boot manual command.

* iosxe/isr1k
    * Added a platform-specific configure_no_boot_manual override
        * Uses the existing configure_autoboot API to set the configuration register to 0x2102 instead of sending the unsupported no boot manual command.

--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* sdk/apis/cheetah/ap/verify
    * Changed AP operation-state and controller verification APIs to perform immediate checks and removed the obsolete ``max_time`` and ``check_interval`` arguments.

genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* nxos
    * Added ShowIpOspfNeighbor
        * show ip ospf neighbors
        * show ip ospf neighbors vrf {vrf}
    * Added ShowNxsecureLog
        * show nxsecure log {policy_id}
    * Added ShowIpMrouteSr
        * show ip mroute sr {group}
    * Added ShowNxsecureLogfiles
        * show nxsecure logfiles
    * Added ShowForwardingRouteDetail
        * show forwarding route {prefix} detail module {module}
    * Added ShowClock
        * show clock
    * Modified ShowIpv6MrouteVrfAll
        * show ipv6 mroute
    * Added ShowNxsecurePackages
        * show nxsecure packages
    * Added ShowIpNatMax
        * show ip nat max
    * Added ShowIpMrouteSrUmnat
        * show ip mroute sr umnat
    * Added ShowMvrMembers
        * show mvr members
    * Added ShowSegmentRoutingMpls
        * show segment-routing mpls
    * Added ShowForwardingDistributionIpv6MulticastRoute
        * show forwarding distribution ipv6 multicast route
    * Added ShowNxsecurePolicyStatus
        * show nxsecure policy status
    * Added ShowHardwareInternalErrorsAll
        * show hardware internal errors all
        * Parsed multiple device records per slot with per-instance counters.
        * Supports multi-word device names and range or annotated port values.
        * Excludes formatting delimiters from parsed output.
    * Added ShowMvrGroups
        * show mvr groups
    * Added ShowBgpIpv4UnicastPrefix
        * show bgp ipv4 unicast {prefix}
        * Added schema and regex support for IPv4 unicast prefix detail paths, labels, extended communities, originator, cluster list, and advertised peers.
    * Added ShowSystemInternalNbmInfoShmTableContext
        * show system internal nbm info shm table context

* iosxe
    * Added ShowAccessSessionCount
        * Parse switch-side filtered access-session counts without serializing the full session table; empty output is not accepted as a zero count.
        * Added captured zero-count golden and empty-output fixtures.
    * Added ShowPlatformSoftwareFedSwitchActiveFnfRecordCountAllAsic
        * show platform software fed switch {switch_type} fnf record-count all-asic
        * Parse per-ASIC current flow counts, total flows added, and total flows removed.
    * Added ShowSdwanOmpPeersDetail
        * show sdwan omp peers detail
    * Added ShowPlatformHardwareFedSwitchActiveFwdAsicInsightSgaclUsageAux
        * Added parser for 'show platform hardware fed {switch} {switch_var} fwd-asic insight sgacl_usage_aux({device_id})' command.
        * Added parser for 'show platform hardware fed {switch_var} fwd-asic insight sgacl_usage_aux({device_id})' command.
    * Added C9050 abstraction wrappers that inherit C9350 parsers for
        * show platform hardware fed qos scheduler sdk interface
        * show platform hardware fed qos queue stats interface
        * show platform hardware fed qos queue config interface
        * show platform hardware fed qos queue stats internal port_type punt queue
        * show platform software fed switch active matm macTable
        * show platform software fed active acl info db detail
        * show platform software fed active punt asic cause brief
        * show platform hardware fed ... fwd-asic resource tcam utilization
        * show inventory
        * show switch stack-ports summary
    * Modified ShowLispDatabaseSuperParser
        * Added ``multihoming_site_id`` parsing for Ethernet database entries.
    * Modified ShowLispSiteDetailSuperParser
        * Added ETR-level ``l2_multihoming_site_id`` parsing.
    * Added ShowPlatformSoftwareCpuAlloc
        * 'show platform software cpu alloc'
    * Modified ShowPlatformResources
        * Added support for Service Processor data.
    * Modified ShowProcessesCpuPlatformProfile
        * Added support for sorted CPU profile commands
            * 'show processes cpu platform sorted profile {profile_name}'
            * 'show processes cpu platform sorted {sort_interval} ' 'profile {profile_name}'

* cheetah
    * Added ShowIpInterfaceBrief
        * show ip interface brief
    * Added ShowIpDhcpLease
        * show ip dhcp lease

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowNxsecurePackages
        * Updated ``show nxsecure packages`` to support LPS, RPM, SHD, PKG, and BIN package filename extensions.
    * Modified ShowNxsecureLogfiles
        * Updated ``show nxsecure logfiles`` to support ``.tar.gz`` files.
    * Modified ShowNxsecureLog
        * Updated ``show nxsecure log {policy_id}`` to support process names containing spaces.
    * Modified ShowIpv6MrouteVrfAll
        * Moved regular expression compilation outside the line-processing loop.
        * Updated regex patterns to parse IPv6 route entries, incoming interfaces, outgoing interface counts, and outgoing interface flags.
        * Updated command execution to use the resolved command argument.
        * Added support for outgoing interface count lines with Fabric OIF.

* iosxe
    * Modified ShowRomvar
        * Added support for parsing ``TFTP_SERVER`` as the optional ``tftp_server`` field.
        * Added coverage for default and revision 1 active/standby output.
    * Modified ShowAccessSessionMacDetails
        * Retain optional multiline blocked_on reasons in targeted client details.
        * Accept captured details with no Server Policies section.
        * Preserve the existing command variants and positional signature.
        * Added captured pending-deletion golden coverage.
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Added optional per-client blocked_on entries, including multiline Pending Deletion and SM Accounting Feature reasons.
        * ShowAccessSessionInterfaceDetails inherits this support without a command or positional signature change.
        * Added captured-output regression coverage and validated existing authentication/access-session golden fixtures.
    * Modified ShowPlatformSoftwareMemoryCallsite
        * Added command: show platform software memory {process} {hw} {switch_type} alloc callsite brief
        * Support active and standby command forms without a slot.
        * Parse supplied output without executing a device command.
        * Accept callsite tables without a tracekey header and preserve hexadecimal callsite identifiers.
        * Preserve the positional order of process, slot, hw, and output; switch_type is keyword-only.
        * Add slotless active/standby and supplied-output golden coverage using unchanged existing captures.
    * Modified ShowPlatformSoftwareMemoryBacktrace
        * Added command: show platform software memory {process} switch {switch_type} alloc backtrace
        * Support active and standby command forms without a slot.
        * Preserve hexadecimal callsite identifiers as strings while retaining decimal callsite support.
        * Preserve the positional order of process, slot, and output; switch_type is keyword-only.
        * Add slotless active/standby and supplied-output golden coverage using unchanged existing captures.
    * Modified ShowPlatSwObjectManagerF0ErrorObject
        * Added command: show platform software object-manager switch {switch} fp active error
    * Modified ShowPlatformSoftwareFedSwitchActiveFnfAttachPointsDump
        * Support DATALINK TRAFFIC rows in addition to existing IPv4 and IPv6 traffic rows.
        * Preserve parsing of input/output directions and attachment status for active and standby switches.
    * Modified ShowIpRouteDistributor, ShowIpv6RouteDistributor, ShowIpRoute, ShowIpv6Route parsers
        * Fix show ip/ipv6 route argument handling by separating protocol selectors from route selectors and rejecting invalid combinations
        * Support multicast routing-table names containing ':' symbol
    * Added ShowIpRouteMulticastDistributor and ShowIpv6RouteMulticastDistributor
        * New classes support show ip{v6} route multicast .. family of CLIs
    * Modified ShowIpNbarDiscovery
        * Added support for TwoGigabitEthernet interface headers in ``show ip nbar protocol-discovery protocol``.
        * Added golden output coverage for TwoGigabitEthernet and GigabitEthernet interfaces.
        * Fixed continuation row parsing to return the actual byte counts, current bit rates, and maximum bit rates without overwriting them.
        * Corrected existing golden expectations to match captured CLI values.
    * Modified ShowIpRouteDistributor and ShowIpv6RouteDistributor parsers
        * Added multicast fallback handling
    * Modified ShowLicenseTechSupport
        * Added support for pla_reporting output.
    * Modified ShowIpRouteSchema schema
        * Added boolean field possibly_down
        * Update ShowIpRoute parser to match and store `possibly down` routing table output
    * Modified ShowSdwanOmpPeersDetail
        * Added support for whitespace-separated headers in show sdwan omp peers detail.
        * Updated schema with optional tenant, peer status, packet, route, TLOC, service, and multicast fields.
        * Preserved legacy colon-separated output and added golden fixtures for both new output samples.
    * Modified ShowPlatformTcamUtilization
        * Added support for the six-slice TCAM utilization output on C9050.
    * Modified ShowPlatformSoftwareFedSwitchActivePbrInfoRouteMap parser
        * Updated p5 regex.
    * Modified ShowMkaSessions
        * Added support for the Probe Count and CA-Type columns introduced by MACsec key rotation enhancements.
        * Retained parsing support for the legacy output format.
    * Modified ShowPlatformSoftwareFedQosInterfaceSuperParser
        * Added optional MAC ACE schema coverage and recognized MAC ACE headers.
        * Captured class IDs, source and destination MAC addresses and masks, ethertype, COS, VLAN ranges, result actions, and meter fields.
        * Preserved IPv4/IPv6 ACE parsing, including outputs without ACE headers.
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed
        * Preserved the MAC ACE capture alongside existing IPv4 regression data.
    * Modified ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * Retained C9250 numbered-switch regression coverage while preserving the parser implementation and existing fixtures from dev.
    * Modified ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
        * Retained C9250 numbered-switch clear regression coverage.
    * Modified ShowPlatformTcamUtilization
        * Retained C9250 TCAM utilization regression coverage.
    * Modified ShowPlatformSoftwareFedActiveAclInfoDbDetail
        * Retained C9250 ACL detail coverage for headers with a feature prefix.
    * Modified ShowEnvironment
        * Added new optional key ``critical_alarms`` in parser and golden parser coverage.
        * Added six p4 states: ``Minor_Low``, ``Minor_High``, ``Major_Low``, ``Major_High``, ``Critical_Low``, and ``Critical_High``.
        * Added golden parser coverage for the ``Minor_Low`` environmental sensor state.
    * Modified ShowPlatform (rv1)
        * Updated p6 state pattern for ``fail, badinput``, ``fail, badoutput``, and ``fail, badcookie``.
        * Added golden parser coverage for the ``fail, badinput`` platform state.
    * Modified ShowMkaPolicy
        * Support the Probe Count column in show mka policy output from 27.1.1.
        * Add optional probe_count while preserving older policy output formats.
        * Parse wrapped interface lists for both older and newer policy rows.
        * Handle a single space between the cipher suite and applied interface.
    * Modified ShowMkaSessionsInterfaceDetails
        * Parse PSK Probing and Probe Count in show mka sessions interface {interface} detail output from 27.1.1.
        * Add optional psk-probing and probe-count keys for older output support.
    * Modified ShowAuthenticationSessionsDetailsSuperParser
        * Restored the legacy server_policies layout when Vlan Group follows Session-Timeout: both values share one numbered policy entry and subsequent policies retain their legacy indices.
        * Preserved separate VLAN entries for VLAN-only output and VLAN following other policies, including ACS ACL, without overwriting repeated VLANs.
        * Added interface-details regression coverage from multi-client and service-template authentication CLI, including MAC and switch variants.
        * Verified inherited IOS authentication and IOS/IOSXE access-session interface-details parsing and command dispatch.

* viptela
    * Modified ShowSystemStatus
        * Made build optional and parsed empty boot loader version, services, and configuration template fields.
        * Added a golden fixture for the 27.1 system status output.

* cheetah
    * Modified ShowInterfacesDot11radio
        * Allow AP output that omits the separate ``mac_address``/``HWaddr`` line while retaining the required ``radio_mac_address``.
        * Changed ``attributes``, ``mtu``, ``metric``, ``rx``, ``tx``, ``collisions``, ``txqueuelen``, ``rx_bytes``, and ``tx_bytes`` to Optional because they are not present on all AP outputs.

* ios
    * Modified ShowEnvironment
        * Added new optional key ``critical_alarms`` in golden parser coverage.
