July 2020
========

July 28th - Genie v20.7
--------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.7                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.7                          |
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

* Fixed Dq reconstruct issue
* Enhanced Dq query validation regex to support strings with round brackets
* Enhanced pyATS learn & parse logic and summary table to be more readable

* Genie Clean

  * Added support for CAT9K HA reload
  * Enhanced image_handler to support the 'file' key for dynamic images
  * Fixed image not copying to standby issue for HA stacks

* 26 New Parsers for a grand total of 2515 parsers
* 59 New Apis for a grand total of 825



**genie**

.. list-table::
    :header-rows: 1

    * - Feature
      - Docs
      - Whats New

    * - pyATS learn & parse cli commands
      - :ref:`Docs <cli_learn>`
      - | Fixed logic not to terminate the run if connection failed for one of the testbed devices.
        | Summary table will now show failed device's connection.
        ::

            > pyats parse 'show version' --testbed-file tb.yaml --output .

            100%|███████████████████████████████████████████████████████████████████████████████████| 1/1 [00:03<00:00,  3.74s/it]
            +==============================================================================+
            | Genie Parse Summary for genie-n9k                                            |
            +==============================================================================+
            |  Connected to genie-n9k                                                      |
            |  -  Log: ./connection_genie-n9k.txt                                          |
            |------------------------------------------------------------------------------|
            |  Parsed command 'show version'                                               |
            |  -  Parsed structure: ./genie-n9k_show-version_parsed.txt                    |
            |  -  Device Console:   ./genie-n9k_show-version_console.txt                   |
            |------------------------------------------------------------------------------|
            100%|███████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 96.78it/s]
            +==============================================================================+
            | Genie Parse Summary for genie-csr1000v                                       |
            +==============================================================================+
            |  Failed to connect to genie-csr1000v                                         |
            |  -  Log: ./connection_genie-csr1000v.txt                                     |
            |------------------------------------------------------------------------------|
            |  Could not parse 'show version'                                              |
            |  -  Exception:      ./genie-csr1000v_show-version_exception.txt              |
            |  -  Device Console: ./genie-csr1000v_show-version_console.txt                |
            |------------------------------------------------------------------------------|

--------

**genie.libs.clean**

* Added support for CAT9K HA reload
* Enhanced image_handler to support the 'file' key for dynamic images
* Fixed image not copying to standby issue for HA stacks
* Changelog can be checked :cleanchangelog20:`here <JULY>`

--------

**genie.libs.conf**

* No change

--------

**genie.libs.filetransferutils**

* No change

--------

**genie.libs.ops**

* No change

--------

**genie.libs.parser**

* 26 new IOSXE, IOS, NXOS, IOSXE and Junos Parsers!
* Grand total of 2515 Parsers
* Changelog can be checked :parserchangelog20:`here <JULY>`

--------

**genie.libs.robot**

* No change

--------

**genie.libs.sdk**

* 59 new apis to use on your devices!
* Grand total of 825 APIs
* Changelog can be checked :sdkchangelog20:`here <JULY>`

--------

**genie.telemetry**

* No change

--------

**genie.trafficgen**

* No change

--------

**genie.utils**

* Fixed Dq reconstruct issue
* Enhanced Dq query validation regex to support strings with round brackets
