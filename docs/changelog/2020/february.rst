February 2020
=============

February 25th - Genie v20.2
---------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.2                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.2                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

Note that this will leave older v19.12 packages around in pip list, but it will
not impact anything (visual only).  An update command can be used to clean up
these packages

.. code-block:: bash

   pyats version update

Features:
^^^^^^^^^

**Genie**

 * New Dq! Dictionary Query to easily question dictionaries!
 * Removed new device os dependency
 * New support for netconf, restconf and gnmi support for Genie Harness
 * Can now run/skip testcase depending on CDET state (Cisco Employee only) with process pre_setup_skip_if_cdet_not_resolved
 * Added python 3.8 support
 * New nested Diff representation
 * Added support for testbed object in other datafile using the markup syntax
 * Updated Timeout to support max_time=None and interval=None
 * Updated to load only triggers/verifications that will be executed
 * :blitz:`New Blitz functionality<http>` - pyATS Testcase yaml file driven

**Genie.Libs.Conf**

 * No change

**Genie.Libs.Filetransferutils**

 * No change

**Genie.Libs.Ops**

 * Changelog can be checked :opschangelog20:`here <FEBRUARY>`

**Genie.Libs.Robot**

 * No change

**Genie.Libs.Sdk**

 * 61 new apis to use on your devices!
 * Changelog can be checked :sdkchangelog20:`here <FEBRUARY>`

**Genie.Libs.Parser**

 * 9 new IOSXE, IOS, NXOS & IOSXR Parsers!
 * Grand total of 1594 parsers
 * Changelog can be checked :parserchangelog20:`here <FEBRUARY>`

**Genie.Telemetry**

 * No change

**Genie.Trafficgen**

 * Added save_configuration to save current traffic generator config
 * Changelog can be checked :trafficgenchangelog20:`here <february>`

