September 2020
========

September 29th - Genie v20.9
--------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.9                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.9                          |
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

Features highlights:
^^^^^^^^^^^^^^^^^^^


**genie**

* Added support for `pyats learn <command> --learn-hostname --learn-os`
* Added support for `pyats parse <command> --learn-hostname --learn-os`
* Enhanced Dq to grab information from upper or lower level by using `level` argument
* Enhanced Discovery to pick up one of devices for Blitz and pyATS Health Check
* Enhanced pyats parse to support --rest to send REST get and collect JSON
* Testcase description can be passed as a variable in the trigger datafile
* Enhanced Genie Testscript to support uid assignment


--------

**genie.libs.clean**

* COM
    * Modified apply_configuration stage
        * to support reading a configuration from a file then applying it on the device
    * Modified copy_to_device stage:
        * to support testbed.servers without credentials specified.
    * Modified copy_to_linux stage:
        * to skip verification for scp as scp does not support file listing.

* IOSXR
    * Added install_image_and_packages stage

--------

**genie.libs.health**

* Enhanced pyATS Health Check to have capability to select testcases/sections
    * Added pyats arguments `--health-uids`, `--health-groups` and `--health-sections`

--------

**genie.libs.conf**

* NXOS
    * Updated NXOS interface conf:
        * Added fabric_forwarding_mode to configure attribute
    * Implemented config line `no ip redirect` and `no ipv6 redirect`

--------

**genie.libs.filetransferutils**

* No change

--------

**genie.libs.ops**

* IOSXE
    * Added platform ops for asr900

* NXOS
    * Added class Lldp:
        * Added statement to check if port_id existed

--------

**genie.libs.parser**

* 45 new IOSXE, IOS, NXOS, IOSXE and Junos Parsers!
* Grand total of 2606 Parsers
* Changelog can be checked :parserchangelog20:`here <SEPTEMBER>`

--------

**genie.libs.robot**

* No change

--------

**genie.libs.sdk**

* 74 new apis to use on your devices!
* Grand total of 985 APIs
* Changelog can be checked :sdkchangelog20:`here <SEPTEMBER>`

--------

**genie.telemetry**

* No change

--------

**genie.trafficgen**

* Added traffic and stream statistics table for TRex
* Added disable_tracking and disable_port_pair arguments for 
  create_genie_statistics_view, check_traffic_loss and create_traffic_streams_table

--------

**genie.utils**

* New disable_log keyword added to timeout - configures timeout object to not generate logging messages
