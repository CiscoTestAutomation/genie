March 2021
==========

March 30h - Genie v21.3
-----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.3                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.3                          |
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

**genie**

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* testbed conversion
    * Fixed bug with non pyATS/Genie interface classes
    * Fixed bug with non pyATS/Genie device classes

* Fixed trafficgen argument
    * Fixed bug that `--tgn-traffic-streams-data` was not properly handled from CLI

* Genie Conf Interface
    * Added `alias` to Genie Conf Interface object

* Device settings in topology
    * Moved Genie default error pattern implementation to Unicon
    * Moved device custom timeout attributes implementation to Unicon


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* Genie schemaengine
    * Add ListOf to schema validation

* Genie make_json
    * Sort tokens


