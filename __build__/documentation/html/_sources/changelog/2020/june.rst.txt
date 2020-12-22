June 2020
========

July 7th - Genie v20.6
--------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.6                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.6                          |
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

.. list-table::
    :header-rows: 1

    * - Feature
      - Docs
      - Whats New

    * - Dq
      - :ref:`Docs <utils_overview>`
      - | Dq makes it very easy to query dictionary and collect values
        ::

            >>> new_dict = Dq(dev.parse('show interfaces')).value_operator('in_crc_errors', '>', 0)
                ['Ethernet2/1', 'Ethernet2/2']

            Details:

            Quick query for dictionary, no need to know the structure, just what you are looking for.
            Support Regex, very powerful!


--------

**genie.libs.clean**

.. list-table::
    :header-rows: 1

    * - Feature
      - Docs
      - Whats New

    * - Clean
      - :ref:`Docs <clean>`
      - | Wipe the device configuration, apply new a new image, apply base configuration, pyATS Clean get your device ready for your script execution!

        You can find many examples in our `Github repo <https://github.com/CiscoTestAutomation/examples/tree/master/clean>`_.

* Numerous fixes and enhancements
* Changelog can be checked :cleanchangelog20:`here <JUNE>`

--------

**genie.libs.conf**

* No change

--------

**genie.libs.filetransferutils**

* Enhancement for ease of use to the libraries

--------

**genie.libs.ops**

* No change

--------

**genie.libs.parser**

* 14 new IOSXE, IOS, NXOS, IOSXE and Junos Parsers!
* Grand total of 2489 Parsers
* Changelog can be checked :parserchangelog20:`here <JUNE>`

--------

**genie.libs.robot**

.. list-table::
    :header-rows: 1

    * - Feature
      - Docs
      - Whats New

    * - Robot
      - :ref:`Docs <robot_genie>`
      - | Query Dq from RobotFramework - For example
        ::

            dq query    data=${data}   filters=contains('lc').not_contains('2').get_values('slot/world_wide_name')

* Fixed feature discovery for classes with an underscore in the name
* Changelog can be checked :robotchangelog20:`here <JUNE>`

--------

**genie.libs.sdk**

* 56 new apis to use on your devices!
* Changelog can be checked :sdkchangelog20:`here <JUNE>`

--------

**genie.telemetry**

* No change

--------

**genie.trafficgen**

* No change

--------

**genie.utils**

* Dq keyword contains_key_value now supports Regex

