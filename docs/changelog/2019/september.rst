September 2019
==============

September 24th - Genie v19.9
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.9                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.9                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

46 New :apis:`network automation apis <http>`. Ready for you to use and
contribute to it.  Fully open sourced!

You can call them by doing

.. code-block:: python

    >>> device.apis.get_interface_mtu_size(device, 'Ethernet2/3')
    1500

:apis:`View all available apis<http>`.


**Genie.genie**
* Added create testbed --template to generate template excel files
* Fixed bug that gives an error with there are slashes in the show command in genie parse with --output


**Genie.Ops**
* No change!


**Genie.Conf**
* No change!


**Genie.utils**
* Fixed bug in timeout not executing the last attempt when time remaining is less than interval


**Genie.harness**
* Fixed filetransfer HA call in case debug plugin argument passed
* Integration with new pyATS reporting mechanism


**Genie.Examples**
* Deprecated in 19.7
* As a reminder, all examples can be found at: https://github.com/CiscoTestAutomation/

  
**Genie.Libs.Parser**
* 35 new IOSXE, IOS, NXOS & JunOS Parsers!
* Grand total of 1375 parsers
* Changelog can be checked :parserchangelog19:`here <SEPTEMBER>`


**Genie.Libs.Ops**
* New OPS structures on IOS;
    * MSDP
    * HSRP
    * EIGRP
* Changelog can be checked :opschangelog19:`here <SEPTEMBER>`


**Genie.Libs.Conf**
* Fixed Genie Interface conf attributes.
* Changelog can be checked :confchangelog19:`here <SEPTEMBER>`


**Genie.Libs.Sdk**
* 46 new :apis:`network automation apis <http>` to interact with your devices
* Added support to perform process restart on multiple VDCs (N7K)
* Support for multiple debug plugins (N7K)
* Fixed single debug plugin test cases
* Changelog can be checked :sdkchangelog19:`here <SEPTEMBER>`


**Genie.Libs.Robot**
* No change!
* Changelog can be checked :robotchangelog19:`here <SEPTEMBER>`


**Genie.Trafficgen**
* Enhanced clear_statistics() to control which commands to execute for clearing statistics
* Enhanced check_traffic_loss corner case to recreate "GENIE" view if deleted by previously executed command
* Bugfix: corner case for setting outage_seconds to 0 when frames_delta is "*" or empty string


**Genie.FileTransferUtils**
* No change!


**Genie.Libs.Telemetry**
* No change!


**Genie.Abstract**
* No change!


**Genie.Telemetry**
* No change!


**Genie.Parsergen**
* No change!


**Genie.Metaparser**
* No change!


**Genie.Predcore**
* No change!
