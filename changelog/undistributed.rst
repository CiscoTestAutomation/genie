November 2020
=============

November XXth - Genie v20.11
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.11                         |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.11                         |
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

* Enhanced mapping datafile to pass netconf_poolsize as argument for NetConf connections.
* Enhancement to Standalone to support non UUT testbed
* Updated genie device error pattern to propagate into device settings 
* Enhanced mapping datafile to pass netconf_poolsize as argument for NetConf connections.
* Fixed API abstraction for platform specific APIs

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

* Removed python sorted method in genie diff in instances where tuple could have different types



