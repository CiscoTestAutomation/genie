January 2021
=============

January 27th - Genie v21.1
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 21.1                          |
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

.. code-block:: bash

   pyats version update

Features:
^^^^^^^^^
  
- Grand total of 1173 :apis:`network automation apis <http>`. Ready for you to use and
  contribute to it.  Fully open sourced!

You can call them by doing

.. code-block:: python

    >>> device.apis.get_interface_mtu_size(device, 'Ethernet2/3')
    1500

- Grand total of 2788 :parsers:`parsers<http>`.

.. code-block:: python

    >>> device.parse('show version')
        {'version': {'version_short': '16.9',
          'platform': 'Virtual XE',
          'version': '16.9.1',
          'image_id': 'X86_64_LINUX_IOSD-UNIVERSALK9-M',
          'os': 'IOS-XE',
          ...
        }}


**Genie**
 * Configuration datafile enhanced to allow for jinja2 template files
 * Discovery enhanced to avoid %VARIABLE to pick up device for Blitz testcase 


**Genie.Libs.Parser**
 * 84 new IOSXE, IOS, NXOS & IOSXR Parsers!
 * Grand total of 2788 parsers
 * Changelog can be checked :parserchangelog21:`here <january>`


**Genie.Libs.Ops**
 * No change!


**Genie.Libs.Conf**
 * No change!


**Genie.Libs.Sdk**
 * 72 new :apis:`network automation apis <http>` to interact with your devices
 * Grand total of 1173 APIs
 * Updated to current apis to support more arguments
 * Changelog can be checked :sdkchangelog21:`here <january>`


**Genie.Libs.Robot**
 * GENERIC
    * Modified Genierobot
        * Updated Datafile Warning Message


**Genie.Telemetry**
 * No change!


**Genie.Libs.Telemetry**
 * No change!


**Genie.FileTransferUtils**
 * No change!


**Genie.Examples**
 * Deprecated in 19.7
 * As a reminder, all examples can be found at: https://github.com/CiscoTestAutomation/


**Genie.Trafficgen**
 * No change!

