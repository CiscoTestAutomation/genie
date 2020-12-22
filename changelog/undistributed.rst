January 2021
=============

January xxth - Genie v21.1
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.1                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.1                          |
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

**genie**
* Fixed an issue using run_genie_sdk with only a connection defined for a device

--------

**genie.libs.clean**

--------

**genie.libs.conf**

--------

**genie.libs.filetransferutils**

--------

**genie.libs.ops**

--------

**genie.libs.parser**

--------

**genie.libs.robot**

--------

**genie.libs.sdk**

--------

**genie.telemetry**

--------

**genie.trafficgen**

--------

**genie.utils**




