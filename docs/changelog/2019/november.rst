November 2019
=============

November 26th - Genie v19.11
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.11                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.11                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

22 New :apis:`network automation apis <http>`. Ready for you to use and
contribute to it.  Fully open sourced!

You can call them by doing

.. code-block:: python

    >>> device.apis.get_interface_mtu_size(device, 'Ethernet2/3')
    1500

45 new IOSXE, IOS and NXOS parsers!

:apis:`View all available apis<http>`.
:parsers:`View all available parsers<http>`.

**Genie.genie**
 * Fix bug where some device names was causing unexpected actions


**Genie.harness**
 * No change!


**Genie.conf**
 * Added feature that allows using device.parse when device is not connected if output is provided.


**Genie.utils**
 * No change!


**Genie.Ops**
 * Fixed a bug caused genie learn cli to crash if the feature to learn is not developed


**Genie.Libs.Parser**
 * 45 new IOSXE, IOS, NXOS & JunOS Parsers!
 * Grand total of 1542 parsers
 * Changelog can be checked :parserchangelog19:`here <NOVEMBER>`


**Genie.Libs.Ops**
 * New `IGMP` OPS structure on IOSXR
 * Updated ROUTING ops to support custom vrf, address_family, protocol, and route arguments (IOSXE & IOSXR)
 * Updated INTERFACE ops by excluding `uptime` key (NXOS)
 * Changelog can be checked :opschangelog19:`here <NOVEMBER>`


**Genie.Libs.Conf**
 * No change!
 * Changelog can be checked :confchangelog19:`here <NOVEMBER>`


**Genie.Libs.Sdk**
 * 22 new :apis:`network automation apis <http>` to interact with your devices
 * Updated current apis to support more arguments (increasing usability)
 * Changelog can be checked :sdkchangelog19:`here <November>`


**Genie.Libs.Robot**
 * No change!
 * Changelog can be checked :robotchangelog19:`here <NOVEMBER>`


**Genie.Libs.Telemetry**
 * No change!


**Genie.FileTransferUtils**
 * Added copy file support for remote linux devices
 * Added multi-home server support that automatically picks the first reachable address if multiple addresses are provided
 * Added compact copy option support for nxos
 * Added vrf prompt patterns for nxos
 * Added copy failure pattern
 * Enhanced exception handling logic


**Genie.Examples**
 * Deprecated in 19.7
 * As a reminder, all examples can be found at: https://github.com/CiscoTestAutomation/


**Genie.Abstract**
 * No change!


**Genie.Telemetry**
 * No change!


**Genie.Trafficgen**
 * No change!


**Genie.Parsergen**
 * No change!


**Genie.Metaparser**
 * No change!


**Genie.Predcore**
 * No change!
