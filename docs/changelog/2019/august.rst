August 2019
===========

August 23th- Genie v19.8
-------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.8                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.8                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.examples genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

Creating testbed is now easier than ever!

* :ref:`It can be done from excel <book_genie_excel_tb>`
* :ref:`You can be prompted question which generated it <cli_create>`
* :ref:`It can be created from a dictionary <book_genie_dict_tb>`

450 New :apis:`network automation apis <http>`. Ready for you to use and
contribute to it.  Fully open sourced!

You can call them by doing

.. code-block:: python

    >>> device.apis.get_interface_mtu_size(device, 'Ethernet2/3')
    1500

:apis:`View all available apis<http>`.

**Genie**
* New Genie create cli command
  * Allow to create testbed from excel
  * Allow to create testbed question prompt
  * Allow to create testbed dictionary


**Genie.Ops**
* No change


**Genie.Conf**
* New device.learn('all')
* New device.parse('all')
* New device.api.<api>


**Genie.Utils**
* No change


**Genie.Harness**
* Extra error pattern for Unicon
* Fixed an issue where verificaton could pass even though command was invalid
* New trigger datafile argument - skip_global_verification

.. code-block:: python

   TriggerSleep:
       source:
           pkg: genie.libs.sdk
           class: triggers.sleep.sleep.TriggerSleep
       sleep_time: 5
       message_time: 3
       skip_global_verifications:
       - Verify_IpInterfaceBrief


**Genie.Examples**
* Deprecated in 19.7
* As a reminder, all examples can be found at: https://github.com/CiscoTestAutomation/

  
**Genie.Libs.Parser**
* 52 new IOSXE, IOS, NXOS & JunOS Parsers!
* Grand total of 1294 parsers
* Changelog can be checked :parserchangelog19:`here <AUGUST>`


**Genie.Libs.Ops**
* New OPS structures on IOS;
    * ACL
    * DOT1X
    * acl
    * dot1x
    * fdb
    * dot1x
    * vrf
    * route_policy
    * mld
    * igmp
    * mcast
    * stp
    * ospf
    * static_routing
    * routing
    * rip
    * vlan
    * lag
    * lldp
    * prefix_list
    * bgp
    * lisp
* Changelog can be checked :opschangelog19:`here <AUGUST>`


**Genie.Libs.Conf**
* No change!


**Genie.Libs.Sdk**
* 450 :apis:`network automation apis <http>` to interact with your devices
* Changelog can be checked :sdkchangelog19:`here <AUGUST>`


**Genie.Libs.Robot**
* No change!
* Changelog can be checked :robotchangelog19:`here <AUGUST>`


**Genie.Trafficgen**

* Fix for check_flow_groups_loss
* read multi-page 'GENIE' view values
* bugfix for pageSize for IxNetwork versions 7.40, 7.50, 8.10
* Enhanced logging on failure for start_traffic and stop_traffic
* Added get_traffic_item_statistics_table to print data for specific columns from 'Traffic Item Statistics' view
* Edit error message for CSV options
* updated default columns for 'Traffic Item Statistics' view table
* Enhancement to get_traffic_item_statistics_table to allow user to overwrite table columns
* Enhancement to create and print 'Flow Statistics' view table


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

August 8th - Genie v19.7.1
--------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.7.1                        |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.7.1                        |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.7.2                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.7.1b0                      |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.7.1b0                      |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.7.1b0                      |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.7.1                        |
+-----------------------------------+-------------------------------+
| ``rest.connector``                | 19.7.1                        |
+-----------------------------------+-------------------------------+

* REST implementation has been added to Genie Interface Conf object.
* Enhancemenets added on Genie Trafficgen.
* Fixed abstraction on rest.connector package.
* Fixed version dependency between Genie packages.
* Bugfix for processor results rollup

