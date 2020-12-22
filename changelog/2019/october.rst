October 2019
============

October 25th - Genie v19.10
---------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.10                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.10                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

44 New :apis:`network automation apis <http>`. Ready for you to use and
contribute to it.  Fully open sourced!

You can call them by doing

.. code-block:: python

    >>> device.apis.get_interface_mtu_size(device, 'Ethernet2/3')
    1500

:apis:`View all available apis<http>`.


**Genie.genie**
 * Added support for creating yamls from excels in a directory in create testbed


**Genie.harness**
 * Updated run_genie_sdk in standalone to support overwriting trigger parameters


**Genie.conf**
 * Updated device.learn to use json file in genie ops
 * Updated device.api no longer requires to pass device object to the api function
 * Updated device in genie to support credentials
 * Added dir(device.api) to returns the list of apis available for the device


**Genie.genie**
 * Changed linux pipe character in show commands to english word pipe in genie parse when creating output file
 * New way to visualize parser with Genie Coloured Regex


**Genie.utils**
 * Diff can now exclude keys at any nested level


**Genie.Ops**
 * No change!


**Genie.Libs.Parser**
 * 92 new IOSXE, IOS, NXOS & JunOS Parsers!
 * Grand total of 1467 parsers
 * Changelog can be checked :parserchangelog19:`here <OCTOBER>`


**Genie.Libs.Ops**
 * New `ND` OPS structure on IOSXR
 * Updated Nd ops to support custom vrf, interface values (IOSXE & NXOS)
 * Updated LAG ops to prevent updating non-existent keys (IOSXR)
 * Fixed issue where exclude keys are not correctly inherited
 * Changelog can be checked :opschangelog19:`here <OCTOBER>`


**Genie.Libs.Conf**
 * Removed unsupported interface warning message
 * Allowed testbed to load with unsupported interfaces
 * Removed unsupported device warning message
 * Changelog can be checked :confchangelog19:`here <OCTOBER>`


**Genie.Libs.Sdk**
 * 44 new :apis:`network automation apis <http>` to interact with your devices
 * Added enhancement for deleting debug plugin after process restart (N7K)
 * Added enhancement for connecting to VDCs after reload.switchover (N7K)
 * Updated mapping for static keys to work properly when count key is provided
 * Changelog can be checked :sdkchangelog19:`here <OCTOBER>`


**Genie.Libs.Robot**
 * No change!
 * Changelog can be checked :robotchangelog19:`here <OCTOBER>`


**Genie.Libs.Telemetry**
 * No change!

**Genie.FileTransferUtils**
 * Added support for scp file transfer protocol for iosxe, iosxr, nxos and junos
 * Added support for sftp file transfer protocol for iosxe, iosxr and nxos
 * Changed file transfer command in junos from load merge to file copy


**Genie.Examples**
 * Deprecated in 19.7
 * As a reminder, all examples can be found at: https://github.com/CiscoTestAutomation/


**Genie.Abstract**
 * Fixed an issue where if an import error occured, the rest of lookup object
   tokens are corrupted
 * lookup/abstraction is now thread-safe


**Genie.Telemetry**
 * No change!


**Genie.Trafficgen**
 * Renamed generate_traffic_stream() to generate_traffic_streams()
 * Enhanced: generate_traffic_streams() to accept a list of traffic streams to regenerate
 * Enhanced: check_traffic_loss() to allow users to wait before checking streams for traffic loss/outage
 * Enhanced: check_traffic_loss() to allow users to enable/disable clearing traffic stats before checking for traffic loss/outage
 * Updated documentation to provide sample traffic generator device use cases


**Genie.Parsergen**
 * No change!


**Genie.Metaparser**
 * No change!


**Genie.Predcore**
 * No change!
