Automation Primer
=================

This guide covers the essentials for building a pyATS automation script using LAMP,
from setting up your testbed to executing testcases.

.. note::

   Before proceeding with the steps below, it's recommended to read the
   :ref:`Blitz <blitz>` documentation to understand the Blitz framework.

Step 1: Set Up Your Project Structure
-------------------------------------

Create a project directory for your pyATS script and a subdirectory for testcases:

.. code-block:: bash

    $ mkdir pyats_script
    $ cd pyats_script && mkdir testcases

You need these files at the project root:

  - **job.py** — Defines the pyATS job
  - **job.tem** — Job template file
  - **main_trigger_datafile.yaml** — Lists testcases to run
  - **subsection_datafile.yaml** — Setup & cleanup sections

**job.py:**

.. code-block:: python

    from ats.datastructures.logic import And
    from genie.harness.main import gRun


    def main():
        gRun(
            trigger_datafile="main_trigger_datafile.yaml",
            subsection_datafile="subsection_datafile.yaml",
            trigger_uids=And(".*"),
        )

**job.tem:**

.. code-block:: yaml

    version: 1

    type: easypy

    tags:
      - devat_ignore

    arguments:
      crft-disable: true
      btrace-disable: true
      disable-image-md5: true
      disable-coverage: true
      disable-device-info: true

    profiles:
      default:
        description: |
          Default profile
        arguments:
          testbed-file: testbed.yaml

**main_trigger_datafile.yaml:**

.. code-block:: yaml

    extends: []

    order: []

**subsection_datafile.yaml:**

.. code-block:: yaml

    setup:
      sections:
        connect:
          method: genie.harness.commons.connect
      order:
        - connect

    cleanup:
      sections:
        disconnect:
          method: genie.harness.commons.disconnect
      order:
        - disconnect

Your final project structure:

.. code-block:: bash

    pyats_script/
    ├── job.py
    ├── job.tem
    ├── main_trigger_datafile.yaml
    ├── subsection_datafile.yaml
    └── testcases/

Step 2: Launch LAMP
-------------------

Activate your pyATS virtual environment, then launch LAMP at your project root:

.. code-block:: bash

    $ cd pyats_script
    $ genie lamp

Step 3: Add Devices & Save Testbed
----------------------------------

Add devices using the ``testbed add`` command:

.. code-block:: console

    (lamp) testbed add 150.0.0.1 --os iosxe --port 22 --credentials admin/password

See :ref:`testbed_add` for details. Once all devices are added, save the testbed:

.. code-block:: console

    (lamp) testbed save testbed.yaml

Alternatively, use ``testbed load testbed.yaml`` if you already have a testbed file.

Step 4: Generate Testcases
--------------------------

Build testcases by executing actions in LAMP. Each testcase is a sequence of actions
that define what your test should do—configure devices, verify output, parse results,
and check for expected behavior.

Start by selecting a device to work with, then execute actions interactively. LAMP
captures each action and generates corresponding YAML code that you'll save later.

**Available Actions**

.. list-table:: Available actions
   :widths: 60 40
   :header-rows: 1

   * - Action
     - LAMP Command
   * - Configure device CLI
     - ``configure``
   * - Verify output from show commands
     - ``execute``
   * - Parse command output
     - ``parse``
   * - Sleep/delay
     - ``sleep``

See :doc:`Operator Commands </lamp/commands/operators/index>` for additional supported
actions and detailed documentation.

**Working with Actions**

Example: Configuring an Interface

.. code-block:: console

    (lamp-device1) configure
    device1(config)# interface Ethernet0/0
    device1(config-if)# ip address 1.1.1.1 255.255.255.0
    device1(config-if)# no shutdown
    device1(config-if)# lamp

The ``lamp`` command exits configuration mode and returns to the LAMP prompt, where
your configuration commands are captured as a code snippet.

Example: Verifying show commands

.. code-block:: console

    (lamp-device1) execute -i show ip interface brief
    ...
    INCLUDE> 1.1.1.1

The ``-i`` flag lets you filter output with include patterns, useful for verification.

**Manage Generated Snippets**

As you execute actions, LAMP generates code snippets that you can view, modify, or remove:

.. list-table:: Snippet management commands
   :widths: 60 40
   :header-rows: 1

   * - Action
     - LAMP Command
   * - View generated code snippets
     - ``list``
   * - Remove unwanted snippets
     - ``remove``
   * - Add new test section
     - ``test_section``

See :doc:`Blitz Handlers </lamp/commands/blitz_handlers/index>` for detailed
documentation on these snippet management commands.

Example: List last generated snippet using the ``list 1`` command:

.. code-block:: console

    (lamp) list 1
    execute:
      device: device1
      command: show ip interface brief
      include:
        - 1.1.1.1

Example: Remove last generated snippet using the ``remove 1`` command:

.. code-block:: console

    (lamp) remove 1

Step 5: Save Testcases
----------------------

Once you've completed all actions for a testcase, save it under the **testcases/** directory:

.. code-block:: console

    (lamp) save testcases/tc_interface_config.yaml

This creates a Blitz YAML file. Create multiple testcases by saving different action
sequences to different files.

Step 6: Register Testcases in Main Trigger Datafile
---------------------------------------------------

Update **main_trigger_datafile.yaml** to register your testcases. Add
file paths to ``extends`` and testcase names to ``order``:

.. code-block:: yaml

    extends:
      - testcases/tc_interface_config.yaml
      - testcases/tc_routing_config.yaml
      - testcases/tc_verify_connectivity.yaml

    order:
      - tc_interface_config
      - tc_routing_config
      - tc_verify_connectivity

Step 7: Execute Your Script
---------------------------

Run your complete automation script:

.. code-block:: bash

    $ pyats run manifest job.tem --profile default

Monitor the output for errors. If issues arise, return to LAMP to refine your testcases.
