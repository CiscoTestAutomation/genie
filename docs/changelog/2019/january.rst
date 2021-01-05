January 2019
============

January 29th
------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie.libs.sdk``            | 3.1.9                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.libs.sdk

Features:
^^^^^^^^^

**Genie.Libs.Sdk**

* Libs
    * Generic
        * Update the class UpdateLearntDatabase to not execute commands when
          there are no previous verifications/pts
        * Create libs.utils.triggeractions.verify_ops_or_logic to support check
          Or logic for triggers mapping requirements in verify_ops
* NXOS
    * Update TriggerReloadActiveRp to have one active|ok|standby LC

* Changelog can be checked :sdkchangelog19:`here <JANUARY>`


January 25th
------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie.libs.ops``            | 3.1.7                         |
+-------------------------------+-------------------------------+
| ``genie.libs.parser``         | 3.1.16                        |
+-------------------------------+-------------------------------+
| ``genie``                     | 3.1.3                         |
+-------------------------------+-------------------------------+
| ``genie.examples``            | 3.1.3                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.libs.ops genie.libs.parser

Features:
^^^^^^^^^

**Genie.Libs.Ops**

* Mandatory pump version number to avoid conflict with pypi
* Changelog can be checked :opschangelog19:`here <JANUARY>`

**Genie.Libs.Parser**

* Mandatory pump version number to avoid conflict with pypi
* Fix for parser `show ip arp` under NXOS.
* Changelog can be checked :parserchangelog19:`here <JANUARY>`

**Genie**

* Bug fix

**Genie.Examples**

* All Genie examples now don't require real devices to run, thanks to the
  playback feature recently added by Genie team under Unicon.
* New solutions runnable examples have been added demonstrating the power of
  Genie in test automation!

January 24th
------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie.ops``                 | 3.1.5                         |
+-------------------------------+-------------------------------+
| ``genie.libs.ops``            | 3.1.6                         |
+-------------------------------+-------------------------------+
| ``genie.libs.parser``         | 3.1.14                        |
+-------------------------------+-------------------------------+


Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.ops genie.libs.ops genie.libs.parser

Features:
^^^^^^^^^

**Genie.Ops**

* Enhancements on `get_ops` API.

**Genie.Libs.Ops**

* ARP Ops libraries on IOSXE, NXOS & IOSXR are now available!
* Genie.ops enhancement required StaticRouting class name modification,
  backward compatible
* Changelog can be checked :opschangelog19:`here <JANUARY>`

**Genie.Libs.Parser**

* Added parsers.json file required for the new Genie search index.
* Changelog can be checked :parserchangelog19:`here <JANUARY>`


January 23rd
------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie``                     | 3.1.2                         |
+-------------------------------+-------------------------------+
| ``genie.harness``             | 3.1.5                         |
+-------------------------------+-------------------------------+
| ``genie.libs.robot``          | 3.1.7                         |
+-------------------------------+-------------------------------+
| ``genie.libs.parser``         | 3.1.13                        |
+-------------------------------+-------------------------------+
| ``unicon``                    | 3.4.6                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.harness genie.libs.robot genie.libs.parser unicon

Features:
^^^^^^^^^

**Genie**

* Changes to genie <cmd> --help.

**Genie.Harness**

* Mapping datafile is now an optional argument to control connection per device,
  otherwise `Genie` will connect to all devices in the testbed yaml file.
* Compatibility changes with latest pyAts v5.1.0.

**Genie.Libs.Robot**

* Bug fix where it wouldnt show multiple Ops object failing; only the first on
* Changelog can be checked :robotchangelog19:`here <JANUARY>`

**Genie.Libs.Parser**

* Parsers are now made indexable by the show command
* Updated all parsers to parse custom "output"
* Added NTP parsers on IOSXR
* Changelog can be checked :parserchangelog19:`here <JANUARY>`

**Unicon**

* New plugin: ACI

* Generic plugin

  - Update connect statements to handle setup prompts

  - press enter on 'kerberos no realm message' with username prompt

  - Added log_file service.

* Updated hostname learning to strip ansi escape codes from learned hostname

* Fix robot keyword error pattern handling in config keyword

* Added error pattern to linux plugin to catch 'No such file or directory' errors


January 16th
------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie``                     | 3.1.1                         |
+-------------------------------+-------------------------------+
| ``genie.ops``                 | 3.1.4                         |
+-------------------------------+-------------------------------+
| ``genie.libs.conf``           | 3.1.4                         |
+-------------------------------+-------------------------------+
| ``genie.libs.parser``         | 3.1.12                        |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.ops genie.libs.conf genie.libs.parser

Features:
^^^^^^^^^

**Genie**

* Embrace yourself, Genie cli is coming out opening up tons of automation
  opportunities for Linux folks!

**Genie.Ops**

* Developed `get_ops` Api, returning abstracted genie Ops class as per the
  device passed.

**Genie.Libs.Conf**

* Changelog can be checked :confchangelog19:`here <JANUARY>`

**Genie.Libs.Parser**

* Changelog can be checked :parserchangelog19:`here <2019> <JANUARY>`
