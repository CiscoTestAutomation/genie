November 2018
=============

November 29th
-------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 3.1.7                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 3.1.5                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 3.1.8                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.libs.sdk genie.libs.ops genie.libs.parser


Features
^^^^^^^^

* NTP is now available on IOSXE & IOS Os.
* Fix up mapping _populate_path when the requirements are callable.
* Enhancements for the NTP IOSXE & IOS parsers.

**Genie.Libs.Parser**

* Changelog can be checked :parserchangelog:`here <NOVEMBER>`

**Genie.Libs.Ops**

* Changelog can be checked :opschangelog:`here <NOVEMBER>`

**Genie.Libs.Sdk**

* Changelog can be checked :sdkchangelog:`here <NOVEMBER>`

November 27th
-------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.harness``                 | 3.1.4                         |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 3.1.2                         |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 3.1.2                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 3.1.6                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 3.1.4                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 3.1.3                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 3.1.5                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 3.1.7                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.harness
    pip install --upgrade genie.ops
    pip install --upgrade genie.utils
    pip install --upgrade genie.libs.sdk
    pip install --upgrade genie.libs.ops
    pip install --upgrade genie.libs.conf
    pip install --upgrade genie.libs.robot
    pip install --upgrade genie.libs.parser

**Genie.Harness**

•    Support asynchronous_configure_snapshot abstraction wised for getting commands.
•    Enhanced logging by providing summary table for each run section.
•    Added Golden PTS abstraction support, per image branch.

**Genie.Ops**

•    Enhanced logging by showing the learnt Ops show commands and their corresponding results.   

**Genie.Utils**

•    Added Summary class to use for summarizing different Genie run sections.

**Genie.Libs.Parser**

* Changelog can be checked :parserchangelog:`here <NOVEMBER>`

**Genie.Libs.Conf**

* Changelog can be checked :confchangelog:`here <NOVEMBER>`

**Genie.Libs.Ops**

* Changelog can be checked :opschangelog:`here <NOVEMBER>`

**Genie.Libs.Sdk**

* Changelog can be checked :sdkchangelog:`here <NOVEMBER>`

**Genie.Libs.Robot**

* Changelog can be checked :robotchangelog:`here <NOVEMBER>`


November 19th
-------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.harness``                 | 3.1.3                         |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 3.1.4                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 3.1.6                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 3.1.2                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 3.1.3                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 3.1.5                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 3.1.2                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.harness
    pip install --upgrade genie.telemetry
    pip install --upgrade genie.libs.parser
    pip install --upgrade genie.libs.conf
    pip install --upgrade genie.libs.ops
    pip install --upgrade genie.libs.sdk
    pip install --upgrade genie.libs.telemetry

**Genie.Harness**

•    Add os 'junos' for Juniper devices into the supported list.
•    Add os 'ios' for Juniper devices into the supported list.
•    Enhancement to 'static' key so it can support multiple classes.

**Genie.Telemetry**

•    GenieTelemetry logs enhancement.
•    Bug fix.

**Genie.Libs.Parser**

* Changelog can be checked :parserchangelog:`here <NOVEMBER>`

**Genie.Libs.Conf**

* Changelog can be checked :confchangelog:`here <NOVEMBER>`

**Genie.Libs.Ops**

* Changelog can be checked :opschangelog:`here <NOVEMBER>`

**Genie.Libs.Sdk**

* Changelog can be checked :sdkchangelog:`here <NOVEMBER>`

**Genie.Libs.Telemetry**

* Enhanced plugins logging messages.


November 15th
-------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.libs.parser``             | 3.1.5                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.libs.parser

New parsers for IOS and TRM NXOS ! 

•    17 new IOS Parsers (Interface and platform
•    8 new TRM NXOS parsers
•    Bug fixes on existing parsers

**Genie.Libs.Parser**

* Changelog can be checked :parserchangelog:`here <NOVEMBER>`


November 9th
------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.libs.ops``                | 3.1.2                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 3.1.4                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 3.1.3                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 3.1.4                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.libs.sdk 
    pip install --upgrade genie.libs.parser
    pip install --upgrade genie.libs.robot
    pip install --upgrade genie.libs.ops


NTP Feature has now been released !

* 2 new Verifications
 * Verify_NtpPeerStatus
 * Verify_NtpPeers

* 1 new PTS
 * NTP

* 1 new Ops object
 * NTP

* 2 new Robot keywords
* Verity NTP is synchronized with “<peer>” on device “uut”
* Verity NTP is synchronized on device “uut”

* 2 new Parsers
 * show ntp peer-status
 * show ntp peers


November 6th
------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.harness``                 | 3.1.2                         |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 3.1.1                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 3.1.1                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 3.1.3                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 3.1.2                         |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 3.1.3                         |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.harness
    pip install --upgrade genie.examples
    pip install --upgrade genie.libs.sdk 
    pip install --upgrade genie.libs.parser
    pip install --upgrade genie.libs.robot
    pip install --upgrade genie.libs.ops


Features:
^^^^^^^^^

* Modification to 'devices' attribute in the trigger, verification and PTS
  datafile. The devices are now passed as a list, and `device_attributes` is a
  dictionary for extra attributes. `device_attributes` is optional.
* Fix a Cython issue.

.. code-block:: python

    devices: ['uut', 'helper']
    devices_attributes:
        uut:
            exclude:
                - next_hello_time


* orderer list can now be filter by using Regex!

.. code-block:: python

    order: ['connect', 'configure', '(profile_*)', 'configuration_snapshot']

* Enhanced Robot Demos
