May 2020
========

May 26th - Genie v20.5
--------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.5                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.5                          |
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

    * - pyats parse
      - :ref:`Docs <cli_parse>`
      - | Enhanced to display suggestions if the search is ambiguous.
        ::

            > pyats parse 'sh a' --testbed-file tb.yaml

            Could not find parser for 'sh a'

            Details:

            Search for 'sh a' is ambiguous.
            Please be more specific in your keywords.

            Results matches:
            - show access-lists
            - show access-session
            - show archive
            - show arp

    * - pyats create testbed
      - :ref:`Docs <cli_create_testbed>`
      - | Added better error handling.
        | Will now show suggestions in the case of incorrect parameters.
        ::

            > pyats create testbed x --output x

            invalid option: x

            valid options:
            - ansible
            - file
            - interactive
            - netbox
            - template

    * - yaml markup
      - :ref:`Docs <markup_datafile>`
      - | Enhanced to retrieve real interface/device/link name
        ::

            # testbed yaml
            devices:
              my_device:
                alias: uut

            # trigger yaml
            MyTrigger:
              devices: %{testbed.devices.uut._name}    <<<< this returns 'my_device'

* Added AttributeHelper2 for specific cases to build_config against testbed/device
* Fixed processors to section to check specified section in datafile and the proceesors will run only for the section.
* Fixed more than 3 device snapshot issue in the harness
* Fixed device.parse() with output to raise SchemaError

--------

**genie.libs.clean**

* Now supports IOSXR (ASR9K)
* Numerous fixes and enhancements
* Changelog can be checked :cleanchangelog20:`here <MAY>`

--------

**genie.libs.conf**

* Bugfixes
* Changelog can be checked :confchangelog20:`here <MAY>`

--------

**genie.libs.filetransferutils**

* No change

--------

**genie.libs.ops**

* No change

--------

**genie.libs.parser**

* 40 new IOSXE, IOS, NXOS, IOSXE, Junos Parsers!
* Grand total of 2475 Parsers
* Changelog can be checked :parserchangelog20:`here <MAY>`

--------

**genie.libs.robot**

* No change

--------

**genie.libs.sdk**

* 26 new apis to use on your devices!
* Changelog can be checked :sdkchangelog20:`here <MAY>`

--------

**genie.telemetry**

* No change

--------

**genie.trafficgen**

* No change

