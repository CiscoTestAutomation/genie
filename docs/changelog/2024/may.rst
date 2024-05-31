May 2024
==========

May 28 - Genie v24.5 
------------------------



+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 24.5                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 24.5                          |
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

* genie.abstract
    * Fixed usage of get_caller_stack_pkgs
        * Call stack wasn't looking at the correct frame all the time
    * Added unittests for magic.py



genie.libs.clean
""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * The clean stages 'verify_running_image' and 'copy_to_device' were using the 'xe_version' field
    * Also fixed the wrong default type when calling get on a dict in 'verify_running_image'.

* clean/stages
    * iosxe
        * update install remove inactive stage to check for the image before remvoving image and packages.

* clean
    * Modified recovery_processor
        * Added condition to check if device has is_ha attribute


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* clean/iosxe
    * Connect
        * Added logic to iosxe connect stage to support HA recovery.

* iosxe/cat9k
    * Added new clean stage `install_image`

* clean
    * Modified clean.py
        * Added resources to NOT_A_STAGE variable.



genie.libs.conf
"""""""""""""""

genie.libs.filetransferutils
""""""""""""""""""""""""""""

genie.libs.health
"""""""""""""""""

genie.libs.ops
""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified test_route_all
        * Added kwargs to mapper



genie.libs.robot
""""""""""""""""

genie.libs.sdk
""""""""""""""
--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added new API verify_dual_port_interface_media_type
        * Added new API to verify the media type of dual port interface.
    * Added verify_yang_management_process API
        * command show platform software yang-management process
    * Added verify_yang_management_process_state API
        * command show platform software yang-management process state
    * Added clear_configuration_lock API
        * command clear configuration lock
    * Added verify_is_syncing_done API
        * This is to validate the netconf way of sync status of a device!
    * Added `get_platform_fan_speed` to retrieve fan_speed of respective fan components under iosxe/cat9k/c9400
    * Added configure_cdp_run API
        * Added API for cdp run
    * Added unconfigure_cdp_run API
        * Added API for no cdp run
    * Added configure_diagnostic_monitor_module API
        * Added API for diagnostic monitor threshold module {mod_num} test {test_name} failure count {failure_count}
    * Added unconfigure_diagnostic_monitor_module API
        * Added API for no diagnostic monitor threshold module {mod_num} test {test_name} failure count {failure_count}
    * Added configure_diagnostic_schedule_module API
        * Added API for diagnostic schedule module {mod_num} test all
    * Added unconfigure_diagnostic_schedule_module API
        * Added API for no diagnostic schedule module {mod_num} test all
    * Added configure_diagnostic_monitor_interval_module API
        * Added API for diagnostic monitor interval module {mod_num} test {test_name} {time} {millisec} {days}
    * Added unconfigure_diagnostic_monitor_interval_module API
        * Added API for no diagnostic monitor interval module {mod_num} test {test_name} {time} {millisec} {days}
    * Added configure_hw_module_slot_upoe_plus API
        * Added API for hw-module slot {slot_num} upoe-plus
    * Added `get_platform_component_type_id_info` that retrieves name, type and id for platform components.
    * Added `get_platform_component_temp_info` to retrieve cname, temp_instant, temp_avg, temp_min, temp_max, temp_interval, alarm_status, alarm_threshold and alarm_severity.
    * Added API configure_dual_port_interface_media_type
        * Added API to configure dual port media type on interface
    * Added `get_platform_component_firmware_info` to retrieve name and firmware_version for their respective platform components.
    * Added configure_ecomode_optics
    * Added unconfigure_ecomode_optics
    * Added new API configure_interface_range_shutdown
        * Added new API to configure interface range shutdown.
    * Added new API configure_interface_range_no_shutdown
        * Added new API to configure interface range no shutdown.

* added unconfigure_hw_module_slot_upoe_plus api
    * Added API for no hw-module slot {slot_num} upoe-plus

* iosxe/rommon
    * Added `configure_rommon_tftp_ha` to configure rommon variables on HA device.
    * Renamed ipv6_address argument to use_ipv6 on `configure_rommon_tftp` api.


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modify enable_ipv6_dhcp_server
        * Updated API to add dhcp server without pool name
    * Modify configure_radius_interface
        * Updated API to Support IPv4 and IPv6
    * Modify unconfigure_radius_interface
        * Updated API to Support IPv4 and IPv6
    * Fixed configure_smartpower_level
    * Fixed unconfigure_smartpower_level
    * Update show commands to use numeric

* nxos
    * Add use_kstack=True as default for NXOS copy APIs


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* cheetah
    * Added retries field
        * Added retries field to execute_archive_download to retry image downloads if fails first time



genie.libs.parser
"""""""""""""""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowIpArpstatisticsVrfAll
        * Added <rewritepkt>, <droppedrewritepkt> and <del_dynamic_on_static_add> optional keys to schema.
        * Updated regex pattern <p2, <p3> and <p50> to accommodate various outputs.
    * Update p5 and p6 regex to capture only system version

* iosxe
    * Modified ShowPolicyMapTypeSuperParser Parser
        * Fix p1 regex to match interface
    * Modified ShowPlatformHardwareFedQosSchedulerSdkInterface parser
        * Fix p3_1 regex and made cstse_scheduler oid optinal
    * Modified ShowTimeRange parser
        * used_in as optional schema variable
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed super parser
        * Fix p5 regex and added 2 optional variables
    * Modified ShowIpRouteDistributor parser
        * Added timeout variable to parse bigger output
    * Modified ShowFlowMonitor parser
        * Updated name="" in function
    * Added support for rommonboot variable
        * Modified <p6> regex to support rommonboot variable
    * Modified ShowIsisDatabaseVerboseParser
        * Parser not taking into consideration if LSPID line is split. Also added recent changes from external parser in polaris.
    * Modified fix for ShowMkaPolicy
        * Made send_secure_announcements key as optional and expanded names of Te,Fo and Gi to accomodate various outputs
    * Modified ShowIsisHostname parser
        * Modified <p2> regex to match
    * Modified ShowMacsecSummary
        * Changed <transmit_sc>, <receive_sc> from schema to Optional.
        * Updated schema to accommodate various outputs.
        * Added regex pattern <p2> and <p3> to accommodate various outputs.
    * Modified ShowIpOspf
        * Added additional unit tests
    * Modified ShowIpOspfDatabase
        * Added additional unit tests
    * Modified ShowIpOspfDatabaseRouter
        * Added additional unit tests
    * Modified ShowIpOspfInterfaceBrief
        * Added additional unit tests
    * Modified ShowSdwanServiceChainStatsDetail
        * Added <track_obj>, <tx_tracker>, <rx_tracker>, <sent>, <dropped> and <rtt> optional keys in schema.
        * Added regex pattern <p5>, <p6>, <p7>, <p8>, <p9>, <p10>, <p11>, <p12> and <p13> to accommodate various outputs.
    * Modified ShowSdmPrefer Parser
        * Added optional parameters to schema and converted some of the keys to optional
        * Added new keys to schema
        * Fixed regex p14-p23 to parse (**) values
        * Added new regex p42-p49
    * Modified fix for ShowCdpNeighbors
        * Modified regex to accomodate various outputs
    * Modified ShowIsisDatabaseVerbose Parser
        * Converted flex algorithm parsing from a set of integers to a list of integers to enable JSON serialization capabilities

* iosxr
    * Modified fix for ShowL2vpnXconnectDetail
        * Modified parser to accomodate various outputs
    * Modified ShowIsisStatistics
        * Changed average_process_time_nsec key from schema to Optional.
        * Updated regex pattern r10, r11, r12, r13, r14, r15 to accommodate various outputs.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll
        * show platform hardware chassis power-supply detail switch {mode} all
        * show platform hardware chassis power-supply detail all
    * Added ShowControllersEthernetControllersPhyDetail
        * Added schema and parser for 'show controllers ethernet-controller {interface} phy detail'
    * Added TracerouteIpAddress
        * Added parser for 'traceroute {ip_address}'
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * parser for 'show platform hardware fed active qos queue stats interface {interface}'
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
        * parser for 'show platform hardware fed active qos queue stats interface {interface} clear'
    * Added ShowIpMfibStatus
        * Added 'show ip mfib status' command and schema for the command.
    * Added ShowIpv6MfibStatus
        * Added 'show ipv6 mfib status' command and schema for the command.

* nxos
    * Added ShowMacSecMkaStatsIntf
        * parser for 'show macsec mka statistics interface {interface}'
    * Added ShowMacSecPolicy
        * parser for 'show macsec policy'
    * Added ShowMacSecSecyStatistics
        * parser for 'show macsec secy statistics '



genie.telemetry
"""""""""""""""""
