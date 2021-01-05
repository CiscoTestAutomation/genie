February 2019
=============

February 14th
-------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie.libs.robot``          | 3.1.8                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.libs.robot

Features:
^^^^^^^^^

**Genie.Libs.Robot**

* Changed pickle/unpickle imports from genie.harness to genie.utils
* Changelog can be checked :robotchangelog19:`here <FEBRUARY>`

February 12th
-------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie.utils``               | 3.1.4                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.utils

Features:
^^^^^^^^^

**Genie.Utils**

* ProfileSystem has been moved to genie utild module, can be called as a standalone outside the harness.

February 11th
-------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie.harness``             | 3.1.6                         |
+-------------------------------+-------------------------------+
| ``genie.libs.parser``         | 3.1.17                        |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.harness genie.libs.parser

Features:
^^^^^^^^^

**Genie.Harness**

* Fixed Genie standalone mode, calling Genie triggers within pyATS script
* Pushed a fix for '--devices' argument when using `Genie run`
* Added documentation for genie triggers available restore methods, get_ops feature and golden pts per branch abstraction

**Genie.Libs.Parser**

* Added the new `get_parser` feature

* IOSXE
    * Fixed ShowBgpAllDetail and ShowBgpAllNeighbors to cover all types of vrf(s) and next_hop(s)

* IOSXR
    * Add ShowRunningConfigNtp for 'show running-config ntp'
    * Fixed parser 'show interface detail' to support non utf8 characters

* NXOS
  * Fixed show_interface - ShowInterfaceSwitchport

* Changelog can be checked :parserchangelog19:`here <FEBRUARY>`

February 7th
------------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``genie.libs.sdk``            | 3.1.10                        |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.libs.sdk

Features:
^^^^^^^^^

**Genie.Libs.Sdk**

* Urgent release for the package (v3.1.9 contains dismantled directories)

* Changelog can be checked :sdkchangelog19:`here <FEBRUARY>`