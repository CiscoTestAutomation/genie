December 2019
=============

December 17th - Genie v19.12
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.12                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.12                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

3 New :apis:`network automation apis <http>`. Ready for you to use and
contribute to it.  Fully open sourced!

You can call them by doing

.. code-block:: python

    >>> device.apis.get_interface_mtu_size(device, 'Ethernet2/3')
    1500

18 new IOSXE, IOS and NXOS parsers!

:apis:`View all available apis<http>`.
:parsers:`View all available parsers<http>`.

**Genie.genie**
 * Updated create testbed syntax to use %ASK{} and %ENC{}


**Genie.harness**
 * Updated trigger_datafile schema to support integer or float for 'tgn_max_outage'
 * Fixed processor reporting mechanism


**Genie.conf**
 * Fixed a bug in Genie.init that caused abstraction definition missing from the device weakref in device.api when loaded from a dict
 * Updated dir(device.api) to only return the available apis but not methods in API class


**Genie.utils**
 * No change!


**Genie.Ops**
 * No change!


**Genie.Libs.Parser**
 * 18 new IOSXE, IOS, NXOS & IOSXR Parsers!
 * Grand total of 1560 parsers
 * Changelog can be checked :parserchangelog19:`here <DECEMBER>`


**Genie.Libs.Ops**
 * New `MSDP`, `ISIS`, `ACL`, `FDB` and `PLATFORM` OPS structures on IOSXR, IOS, NXOS and IOSXE(cat9k)
 * Updated `ACL` ops under IOSXE
 * Updated verifications under IOSXR
 * Changelog can be checked :opschangelog19:`here <DECEMBER>`


**Genie.Libs.Conf**
 * No change!
 * Changelog can be checked :confchangelog19:`here <DECEMBER>`


**Genie.Libs.Sdk**
 * 3 new :apis:`network automation apis <http>` to interact with your devices
 * Updated current apis to support more arguments (increasing usability)
 * Changelog can be checked :sdkchangelog19:`here <DECEMBER>`


**Genie.Libs.Robot**
 * No change!
 * Changelog can be checked :robotchangelog19:`here <DECEMBER>`


**Genie.Telemetry**
 * No change!


**Genie.Libs.Telemetry**
 * No change!


**Genie.FileTransferUtils**
 * Added `use-kstack` copy option support for nxos
 * Enhanced error message handling logic, it now checks line by line instead of the entire output


**Genie.Examples**
 * Deprecated in 19.7
 * As a reminder, all examples can be found at: https://github.com/CiscoTestAutomation/


**Genie.Abstract**
 * No change!


**Genie.Trafficgen**
 * Bug fix for corner case of `rx_rate` being empty in `check_traffic_loss`


**Genie.Parsergen**
 * Placed a fix for the IOSXR OS parsers directly calling the core functionalities


**Genie.Metaparser**
 * No change!


**Genie.Predcore**
 * Updated collections imports

