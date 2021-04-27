April 2021
==========

April 27th - Genie v21.4
------------------------

+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.4                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.4                          |
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
                                New
--------------------------------------------------------------------------------

* Genie schemaengine
    * Add ListOf to schema validation
* Genie make_json
    * Sort tokens
* New feature to remove configuration part of common cleanup
* Genie Conf Interface
    * Added `alias` to Genie Conf Interface object

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* Fixed an issue with run_genie_sdk to run multiple testcases
* Enhancement to have callable to verify configuration has been configured correctly and stabilized correctly
* testbed initialization
    * Fixed the quick-testbed referenced here: https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/genie.html#create-a-testbed-from-a-dictionary
* testbed conversion
    * Fixed bug with non pyATS/Genie device classes
* Device settings in topology
    * Moved Genie default error pattern implementation to Unicon
    * Moved device custom timeout attributes implementation to Unicon
* Genie Diff
    * Overhauled the existing code base to clean it up
    * Fixed reported issues where the diff was not correct
* UTILS
    * Fixed issue with function json loading by moving load time from import to first call
* testbed conversion
    * Fixed bug with non pyATS/Genie interface classes
* Fixed trafficgen argument
    * Fixed bug that `--tgn-traffic-streams-data` was not properly handled from CLI


genie.libs.health
"""""""""""""""""

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* Health
    * Modified internal functions
        * To handle Blitz loop against devices properly
        * To handle `common_api` key in case no device in action


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* Health Plugin
    * added `--health-config` to pyats command
        * To load health setting from health_config.yaml
    * create `health_results.json`
        * To have health data from results.json separately
        * Add `health_settings` to health_results.json from health config

* Health
    * Modified `add_result_as_extra` decorator in Blitz
        * Moved health data to health_results.json and have minimum data in extra
        * Added `health_data` to store each health action result in health_results.json


genie.libs.clean
""""""""""""""""

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* COM
    * Modified connect stage
        * Corrected the schema to support the current arguments
    * Modified Device Recovery
        * To fix an edge-case where clean should have continued after the device connection was verified.


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* COM
    * Modified copy_to_device stage
        * Added copy_attempts_sleep argument for sleeping between copy attempts
    * Modified copy_to_linux stage
        * Added copy_attempts_sleep argument for sleeping between copy attempts


genie.libs.conf
"""""""""""""""

No changes.

genie.libs.filetransferutils
""""""""""""""""""""""""""""

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* Filetranferutils package
    * Modified FileUtils
        * Added `Permission denied` to error pattern


genie.libs.ops
""""""""""""""

No changes.

genie.libs.parser
"""""""""""""""""

--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* ASA
    * Modified ShowRoute
        * Added regex pattern <p5_1> to accommodate newer outputs.

* IOSXE
    * Modified ShowSslProxyStatistics
        * Updated schema to accommodate the 17.5 release output.
    * Modified ShowTcpProxyStatistics
        * Updated schema to accommodate the 17.5 release output.
    * Modified ShowInterfaces
        * Update schema to include optional line protocol err-disabled state if it exists
        * Update condition to display line protocol err-disabled state if it exists
        * Update 3 of the existing golden_output2_expected to accomodate schema changes
        * Add folder based unittests
    * Modified ShowInventory
        * Modified regex pattern <p1_6> to accommodate various outputs.
    * Modified ShowWlanAll
        * Added Optional keys <wifi_direct_policy>, <multicast_buffer_frames>, <dual_neighbor_list>, <client_scan_report_11k_beacon_radio_measurement>, <request_on_association>, and <request_on_roam> into the schema.
        * Changed <multicast_buffer_size> from schema to Optional.
        * Updated regex pattern <p_multi_buffer_frames> to correctly accommodate outputs.
    * Modified ShowBgp
        * Update cli_command list to display address family correctly
    * Modified ShowWirelessMobilitySummary
        * Updated regex pattern <pmtu> to accommodate various outputs.
    * Modified
        * Modified show_interface.py to fix a bug in ShowInterfacesSwitchport
        * Also modified iosxe current tests because they were wrong

* NXOS
    * Modified ShowIpRoute
        * Added sorting of next_hop_list
        * ShowIpv6Route, ShowRouting are affected by this change as well
    * Modified ShowPortChannelDatabase
        * Support for 'on' activity of interface member
    * Modified ShowRunningConfigNvOverlay
        * added support for multisite_ingress_replication_optimized under l3 vni in nve interface
    * Modified ShowVlan
        * Updated regex pattern <p1> to accommodate various outputs.
    * Modified ShowIpv6PrefixList
        * Support for 'af' argument of cli command

* IOSXR
    * Modified ShowBgp
        * Add try/except when assigning <remote_as> as an int
    * Modified ShowIsisInterface
        * Now capable of handling CLNS MTU field with an error message
        * Correctly handles the 'protocol_state' field under each AF / Topology
    * Modified ShowPlatform
        * Update regex p1 - to accept additional states for 'show platform' command
        * Update logic to include missing subslots
        * Add folder based unittests

* Utils
    * Modified Unittesting
        * Unittests have more features for testing
        * Fixed all broken unittests

* UTILS
    * Fixed issue with parser json loading by moving load time from import to first call

* IOS
    * Modified
        * Modified show_interface.py to fix a bug in ShowInterfacesSwitchport
        * Also modified ios current tests because they were wrong


--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* Comware
    * Added DisplayInterfaces for:
        * 'display interface'
        * 'display interface <interface>'

* IOSXE
    * Added ShowSdwanAppqoeFlowAll
        * 'show sdwan appqoe flow all'
    * Added ShowIox
        * show iox-service
    * Added ShowApphostingInfra
        * show app-hosting infra

* Check Point Gaia OS
    * New platform added called 'gaia'
        * Note This name aligns with with netmiko driver name ('gaia') and is similar to the napalm driver ('gaiaos')
    * Included parsers
        * show interface
        * show users
        * show ntp
        * show arp
        * show version
    * Parsers are for clish commands only. Expert mode commands are not currently supported.
    * Tested under Check Point Gaia R80.40
    * All parsers include tests, and all module tests passing.

* JUNOS
    * Added ShowMplsLdpParameters
        * show mpls ldp parameters

* IOSXR
    * Added ShowMplsLdpBindings
        * show mpls ldp bindings
    * Added ShowProtocols
        * show protocols {protocol}
        * folder based unittests
    * Added ShowBgpNexthops
        * Add Show command 'show bgp nexthops {ipaddress}'
    * Added ShowArmIpv4Conflicts
        * show arm ipv4 conflicts
    * Added ShowCefDetail
        * show cef {afi} {prefix} detail
        * folder based unittests

* UTILS
    * Modified Common
        * Added ParserNotFound custom exception class when parser is not found
    * Modified Common
        * Added 'tu' 'Tunnel' to convert list of interfaces

* APIC
    * Added ShowVersion
        * added parser for `show version`
    * refactored unittests to be folder based

* Junos
    * Added ShowMplsLdpDiscoveryDetail
        * show mpls ldp discovery detail
        * folder based unittests


genie.libs.robot
""""""""""""""""

No changes.

genie.libs.sdk
""""""""""""""

--------------------------------------------------------------------------------
                                      New
--------------------------------------------------------------------------------

* NXOS, NXOS/ACI
    * added `get_show_tech` API
    * added `copy_to_script_host` API
    * added `is_connected_via_vty` API

* IOSXE
    * added `get_show_tech` API
    * added `copy_to_script_host` API
    * added `is_connected_via_vty` API
    * Added API `health_cpu`
    * Added API `health_memory`
    * Added API `health_logging`
    * Added API `health_core`

* IOSXR
    * added `get_show_tech` API
    * added `copy_to_script_host` API
    * added `is_connected_via_vty` API
    * Added API `health_cpu`
    * Added API `health_memory`
    * Added API `health_logging`
    * Added API `health_core`

* APIC
    * added `get_show_tech` API
    * added `copy_to_script_host` API

* Linux
    * Added `socat_relay` API

* SDK libs
    * Updated `post_execute_command` processor to support device API calls

* FileServer
    * Added `http` protocol support to FileServer

* Common
    * Added `get_local_ip` API to lookup local IP address

* NXOS
    * health APIs for pyATS Health Check
        * Added API `health_cpu`
        * Added API `health_memory`
        * Added API `health_logging`
        * Added API `health_core`

* API Utils
    * Add get_single_interface API
        * To Get Single Interface Via Link In Testbed Yaml


--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* Junos
    * Fixed API `default_interface`
        * changed from raising exception to returning boolean

* IOSXE
    * Modified API `get_platform_cpu_load_detail`
        * Updated to use API `health_cpu`
    * Modified API `get_platform_memory_usage_detail`
        * Updated to use API `health_memory`
    * Modified API `get_platform_logging`
        * Updated to use API `health_logging`
    * Modified API `get_platform_core`
        * Updated to use API `health_core`
    * Modified API `get_platform_cpu_load_detail`
        * Updated to use API `health_cpu`
    * Modified API `get_platform_memory_usage_detail`
        * Updated to use API `health_memory`
    * Modified API `get_platform_logging`
        * Updated to use API `health_logging`
    * Modified API `get_platform_core`
        * Updated to use API `health_core`

* IOSXR
    * Modified API `get_platform_cpu_load_detail`
        * Updated to use API `health_cpu`
    * Modified API `get_platform_memory_usage_detail`
        * Updated to use API `health_memory`
    * Modified API `get_platform_logging`
        * Updated to use API `health_logging`
    * Modified API `get_platform_core`
        * Updated to use API `health_core`
    * Modified get_available_space
        * Added handling of the unit (kbytes/bytes) and convert.
    * Modified verify_file_exists
        * Add support of empty folder corner case
    * Modified Install_Image_And_Packages in clean-pkg
        * Fixed Regex Error
        * Add support for complex filepath (using several folders)

* Common API
    * Modified API `verify_device_connection_state`
        * Added handling in case device object doesn't have attribute `is_ha`

* Blitz
    * Modified decorator in Blitz for pyATS Health Check
        * Added handling for new pyATS Health Check data format
    * Modified `callback_blitz_dispatcher_gen`
        * To pass `name` info from section with loop to action
    * Modified blitz.py
        * Fixed error where failures in a parallel call wouldn't end the testcase when `continue false` is set
    * Fixed `custom_verification_message` handling
    * Modified notify_wait to recognize a device gnmi connection.
    * NETCONF subsccribe operation was forming invalid RPC message.
    * The rpc-error was not printing in log.
    * The selected flag was ignored checking return values.

* nxos
    * Modified ReloadFabricModule
        * changed the extended class from TriggerReloadLC to  TriggerReloadFabric

* API utils
    * common API `get_interface_from_yaml`
        * removed `*args` and changed to `testbed_topology`


genie.telemetry
"""""""""""""""

No changes.

genie.trafficgen
""""""""""""""""

* ixianative.py
    * Modified check_traffic_loss:
        * enhanced code so it handles tx_frame_rate being 0.0 (Handled DivisionByZero error)
