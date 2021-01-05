October 2020
============

October 27th - Genie v20.10
---------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.10                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.10                         |
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
^^^^^^^^^^^^^^^^^^^^

* End of Support for Uniclean starting January - All clean should migrate to :ref:`Docs <clean>`.


**genie**

* Enhanced logging when loading of trigger fails

--------

**genie.utils**

* Enhanced genie diff to find diff of lists based on what added/removed instead of index comparison 
* Enhanced Dq to escape special characters on request
* Fixed Dq for the case when handling empty list

--------

**genie.libs.clean**

* COM
    * Moved all recovery code from clean/stages into clean/recovery
    * Modified recovery to handle prompt interactions with both kickstart and system image
    * Modified apply_configuration stage schema to support 'configure_replace'
    * Fixed clean failing after device_recovery recovers the device
    * Modified apply_configuration stage:
        * To support configure replace
        * To support hostname changes when configuring by file
    * Modified reload stage:
        * To use prompt-recovery when reconnecting
* STAGES
    * Modified connect stage:
        * Added max_timeout and interval parameters
        * Allows function to retry connection if it fails
* IOSXE
    * IOSXE Grub Menu are now supported for pyATS Clean
    * Added install_remove_inactive stage
    * Modified tftp_boot stage:
        * To properly wait for device to start reloading
        * Removed 'device_reload_sleep' argument
        * Removed stage skipping if device_recovery had already run
    * Modified install_image stage:
        * To fix script hanging due to regex mismatch
    * Modified install_packages stage:
        * To fix script hanging due to regex mismatch
    * Modified install_image_and_packages stage:
        * to use a modified timeout for 'install activate id' command
    * Modified device_recovery:
        * To handle edge case scenarios in rommon mode
        * To boot the correct image when using 'golden_image'
* IOSXR
    * Modified install_image_and_packages stage:
        * To fix script hanging due to different device output
    * Modified tftp_boot stage:
        * Removed stage skipping if device_recovery had already run
* NXOS
    * Added support for N3K platform
    * Modified tftp_boot stage:
        * Removed stage skipping if device_recovery had already run
* LINUX 
    * Added clean stage: revert_vm_snapshot

* PLEASE FOLLOW THE TEMPLATE.
* ADDED `PYATSDEVICECLEAN` MODULE FOR USE INSIDE `CLEANERS` SECTION OF THE CLEAN YAML. THIS ALLOWS USE OF BOTH PYATS CLEAN AND UNICLEAN SIMULTANEOUSLY.

--------

**genie.libs.health**

* pyATS Health Check
    * Added legacy_cli argument for easypy command
    * Removed restriction health args in health yaml
        * Now all the items under same section don't need to have health args
    * Added reconnect feature
        * pyATS Health Check reconnects device in case device crashes/reloads
    * Added to convert testbed object from pyATS to Genie for pyATS run:
    * Removed processor tag restriction in health.yaml:
        * mixed `pre`/`post`/etc under same section is possible
    * Enhanced to not show up the section in log which is not supposed to run
        * see executed sections only in log
    * Enhanced to run section with non-connected device
        * if both connected and non-connected devices in same section, only action with connected device will run

--------

**genie.libs.conf**

* IOSXR
    * changed class Interface to check for bundle
* IOSXE
    * Modified EthernetInterface:
        * Expanded list of interface name types
    * Modified EthernetInterface:
        * Expanded list of interface name types (tengige/TenGigE/twentyfivegige/TwentyFiveGigE/fortygige/FortyGigE)

--------

**genie.libs.filetransferutils**

* No change

--------

**genie.libs.ops**

* No change

--------

**genie.libs.parser**

* 72 new IOSXE, IOS, NXOS, IOSXE and Junos Parsers!
* Grand total of 2678 Parsers
* Changelog can be checked :parserchangelog20:`here <october>`

--------

**genie.libs.robot**

* No change

--------

**genie.libs.sdk**

* 37 new apis to use on your devices!
* Grand total of 1022 APIs
* Changelog can be checked :sdkchangelog20:`here <october>`

--------

**genie.telemetry**

* No change

--------

**genie.trafficgen**

 * Update create_flow_statistics_table to support csv_windows_path and csv_file_name
      as argument



