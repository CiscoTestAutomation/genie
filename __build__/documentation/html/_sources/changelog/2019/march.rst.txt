March 2019
==========

March 20th
----------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.harness``                 | 19.0.1                        |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 19.0.1                        |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.harness genie.examples


Features
^^^^^^^^

**Genie.Harness**

* :ref:`New Mechanism to run trigger/verification within pyATS!<pyats_harness>`

* :ref:`New Custom Mixed trigger<genie_harness_cluster>`. Allow to run multiple
  triggers and verifications within 1 trigger.

* Adding custom to the mapping datafile schema
.. code-block:: bash

    mapping:
        cli: vty
        custom:
            active: a
            standby: b

**Genie.Examples**

* New demo11 on how to run a clsuter Trigger (multiple triggers and verifications within 1
trigger)


March 12th
----------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``unicon``                        | 19.0.1                        |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade unicon


Features
^^^^^^^^

**Unicon**

* Fix bug where prompt recovery was not applied on initial connection during init command execution.
* Fix bug to ensure protocol is not required in connection block when command key is specified.


March 7th
---------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.ops``                     | 19.0.1                        |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.0.1                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.0.1                        |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.0.1                        |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.ops genie.telemetry genie.libs.parser genie.utils


Features
^^^^^^^^

**Genie.Ops**

* Enhancement in `async` call for py37 compatibility.


**Genie.Telemetry**

* Enhancement in `async` call for py37 compatibility.


**Genie.Utils**

* Enhancement in `re._pattern_type` call for py37 compatibility.


**Genie.Libs.Parser**

* Changelog can be checked :parserchangelog19:`here <MARCH>`


March 4th- Genie v19.0.0
------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.0.0                        |
+-----------------------------------+-------------------------------+
| ``unicon``                        | 19.0.0                        |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.examples genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

* New package version following PEP 440 guidelines.
* New GettingStarted guide.
* Genie support for 3.7!
* CiscoLive Genie :genie_workshop:`Workshop <http>`
* CiscoLive pyATS/Genie Ops & Parsers :pyats_genie_workshop:`Workshop <http>`

**Genie**

* Genie run
.. code-block:: bash

		genie run --testbed-file /path/to/testbed.yaml \
                  --trigger-uids="And('TriggerShutNoShutBgp$')" \
                  --verification-uids="And('Verify_BgpProcessVrfAll$')" \
                  --devices nxos-osv-1

* Genie parse
.. code-block:: bash

		genie parse all --testbed-file /path/to/testbed.yaml --devices uut

* Genie learn
.. code-block:: bash

		genie learn all --testbed-file /path/to/testbed.yaml --devices nx-osv-1 --output genie_learn_all

* Genie diff (Compare directories of learnt features in `genie learn` and `genie parse`)
.. code-block:: bash

		genie diff dir1 dir2 --output diff1

* Genie shell (Open a Genie interactive shell)
.. code-block:: bash

		genie shell --testbed-file tb.yaml

**Genie.Harness**

* Python Ixia Library :genie_traffic_gen:`GenieTrafficGen <http>`
* Randomized triggers for more testing scenarios!
* Profile the System with the device show commands!
* Mapping data file is now optional.

**Genie.Conf**

*  Package version change following PEP 440 guidelines.

**Genie.Examples**

* All Genie Examples are now runnable without need to the device.
* Changed name of all demos replay directories from Example_<demo number> to mock_device

**Genie.Libs.Conf**

* Changelog can be checked :confchangelog19:`here <MARCH>`

**Genie.Libs.Ops**

* Changelog can be checked :opschangelog19:`here <MARCH>`

**Genie.Libs.Parser**

* New `get_parser` feature for retrieving the parser class.
* Over 100 new IOS Parsers!
* Changelog can be checked :parserchangelog19:`here <MARCH>`

**Genie.Libs.Robot**

* Changelog can be checked :robotchangelog19:`here <MARCH>`

**Genie.Libs.Sdk**

* Changelog can be checked :sdkchangelog19:`here <MARCH>`

**Genie.Ops**

*  Package version change following PEP 440 guidelines.

**Genie.Utils**

* `Profile` new API for system profiling user passed features and compare at a later time.

**Unicon**

* Playback, records all interaction with any device and can be replayed later!
* device.parse for directly calling over than 580 Genie parsers as below;
.. code-block:: bash

	parsed_dictionary = device.parse('show version')

* device.learn new feature calling Genie networking models;
.. code-block:: bash

	ops_dictionary = device.learn(‘ospf’)
