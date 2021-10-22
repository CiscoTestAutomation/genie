.. _example:

Examples
========

The below 11 examples demonstrate the flow of ``Genie`` and how it can be used
in testing different features and frameworks.

Examples can be cloned_ from: `https://github.com/CiscoTestAutomation/examples/tree/master/libraries`.


.. _Clone: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

.. note::

    - If you are running examples as a devnet user, add the argument `--html-logs` 
      at the end of the run command and this will generate an HTML formatted, 
      user-friendly run log file inside the job results folder.

    - All Genie examples now don't require real devices to run, thanks to the
      playback feature recently added by Genie team under Unicon.

    - Each examples contains README.md file, which explain how to use the
      playback feature

**How to bring up Virtual testbed**

All the below examples can be run on virtual devices. We will refer to the
already brought up VIRL topology as `virl.yaml`.

You can bring up a virtual topology by following one of the below two options;

1- Use Cisco DevNet Sandbox Remote labs;

  * :reserve:`Reserve a Multi-IOS Cisco Test Network Sandbox <http>`.
  * :launch:`Launch Genie VIRL simulation <http>`.

2- Refer to :ref:`VIRL <virl>` for detailed steps to bring up VIRL topology.

**Example 1**

This example is an introduction to `Genie`.

It does the following:

  * Connect to the devices defined in the testbed file.
  * Execute a Sleep Trigger. Will sleep for 5 seconds.
  * Terminate the run

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/harness_simple/

      pyats run job demo1_harness_simple_job.py --testbed-file virl.yaml

  .. note::

      Full log can be accessed from here :download:`TaskLog_demo1.html <TaskLog_demo1.html>`.

**Example 2**

This script demonstrates the Triggers and Verifications concept in Genie.
Triggers and verifications are plug and play Testcase to create any combination
of tests. It does the following:

  * Connect to the devices defined in the testbed file.
  * Execute the first round of `verifications`. These verifications take a snapshot
    of the state of these commands. Future round of verifications is compared with
    these initial snapshot.
  * Execute the first trigger `TriggerClearCountersInterfaceAll`.
  * Execute the second round of verifications. Those are compared with the first round.
  * Execute the second trigger `TriggerShutNoShutBgpNeighbors`.
  * Repeat until all triggers are executed.
  * Terminate the run

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/harness_triggers/

      pyats run job demo2_harness_triggers_job.py --testbed-file virl.yaml

  .. note::

      Full log can be accessed from here :download:`TaskLog_demo2.html <TaskLog_demo2.html>`.

**Example 3**

This script demonstrates the Triggers and Verifications with Healthcheck.
The Healthcheck is called `Genie Telemetry`. It allows to collect any kind of
information in the execution, act on it and create a report at
the end of the run. For example, verify if any core was created
after each trigger, verify cpu usage, traceback, etc.

It does the following:

  The execution flow will be the same as demo2_harness_triggers, with the
  following addition:

    * At the end of CommonSetup, all Triggers and at the begining of CommonCleanup,
      it is verified if there is any core on the device and any traceback.

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/harness_telemetry/

      pyats run job demo3_harness_telemetry_job.py --testbed-file virl.yaml --genietelemetry telemetry.yaml

  .. note::

      Full log can be accessed from here :download:`TaskLog_demo3.html <TaskLog_demo3.html>`.

**Example 4**


This script demonstrates how to add your own `Trigger` to execute with existing
triggers. A trigger is a pyATS testcase which tests some specific action. Look
inside the file `$VIRTUAL_ENV/examples/libraries/harness_custom_trigger/trigger.py`. 
Once created, the python path of the trigger must be added to the 
`$VIRTUAL_ENV/examples/libraries/harness_custom_trigger/trigger_datafile_demo.yaml`.  
Lastly, the `demo4_harness_custom_trigger_job.py` was modified to add the new 
trigger to the `trigger_uids`.

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/harness_custom_trigger/

      pyats run job demo4_harness_custom_trigger_job.py --testbed-file virl.yaml

  .. note::

      Full log can be accessed from here :download:`TaskLog_demo4.html <TaskLog_demo4.html>`.

**Example 5**

`RobotFramework` is an opensource test automation framework which provides automation,
without having to write code. It is `Keyword` driven. Libraries provide
Keywords to interact. `Genie` and `pyATS` provide keywords, to execute
Triggers and Testcases, parse commands, learn device features and many more. It also uses
`Genie` `Operational` object, to verify if we have a right amount of Routes, up
interfaces, etc.

  .. note::

      1) Make sure you have robotframework installed.

      2) Open the $VIRTUAL_ENV/examples/libraries/robot/demo5.robot file, and
         modify the testbed variable to point to your testbed file.

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/robot/

      robot demo5.robot

**Example 6**

Genie uses Configuration and Operational objects to drive its configuration and
operation state. The configuraiton object, `conf`, are object that once some
variable are set,  configuration is build and apply on the device. Those objects
follow Models (IETF, OpenConfig, Cisco Native Models) to make them OS agnostic.

It does the following:

  * Connect to a list of devices
  * Retrieve the operational state for each device
  * Apply Ospf configuration
  * Retrieve the operational state for each device and compare with step 2
  * Unconfig Ospf configuration

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/config_ops/

      python demo6_config_ops.py -testbed_file virl.yaml


**Example 7**

This script demonstrates how to include any `Genie` Triggers and Verifications
within any existing `pyATS` script. Triggers and verifications are pyATS
Testcase.

:ref:`More details <pyats_harness>`

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/trigger_within_pyats/

      pyats run job job/demo7_trigger_within_pyats_job.py --testbed-file virl.yaml

  .. note::

      Full log can be accessed from here :download:`TaskLog_demo7.html <TaskLog_demo7.html>`.


**Example 8**

This script carries the knowledge of demo6. This time, it is uses within a
pyATS script. This script is a pyATS scripts, which uses those objects to
configuration and make sure the devices are configured correctly. This script
works on all platform.

  .. note::

      This scripts requires the device to not be configured, as the configuration
      is done by the script. Make sure you are using the unconfigured virl devices
      here :download:`example_testbed_empty.virl <example_testbed_empty.virl>`.

Here's how to add them to any pyATS script:

  * Import the Trigger/Verification
  * Create a class which inherits from this Triggers/Verification
  * Add the decorator
  * If its a verification, add an uid which is not used yet, and child variable like in the example.
  * Add to the datafile information about this trigger. This information can be found in the Trigger datafile
    ($VIRTUAL_ENV/lib/python<version>/site-packages/genie/libs/sdk/genie_yamls/<uut os>/trigger_datafile_<uut os>.yaml)

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/pyats_conf_ops/

      pyats run job job/demo8_pyats_conf_ops_job.py --testbed-file virl.yaml --datafile datafile.yaml

**Example 9**

This script demonstrates how to compare show commands information between two
contexts (cli/xml). It first sends a show command with cli, then do the same
with xml, and compares the fields to make sure they are equal.

  .. note::

      This scripts requires the device to not be configured, as the configuration
      is done by the script. Make sure you are using the unconfigured virl devices.

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/context_comparator/

      pyats run job job/demo9_context_comparator_job.py --testbed-file virl.yaml

.. note::

    Converting pyats objects to Genie objects should always happen before connection.

    1. convert
        from genie import testbed
        testbed = testbed.load(testbed)
    2. Get the device (below assumes device alias in yaml is uut)
        uut = testbed.devices['uut']
    3. Now connect
        uut.connect()
    4. Overwrite the testbed parameters
        self.parameters['testbed'] = testbed

.. note::

    The device under testing must have an alias `uut` in the testbed yaml file.

    *Example**:
      devices:
        R1:
          alias: 'uut'

  .. note::

      Full log can be accessed from here :download:`TaskLog_demo9.html <TaskLog_demo9.html>`.

**Example 10**

Example to demonstrates more Advanced functionality of Robot.


.. _example_11:

**Example 11**

This script demonstrate how to run multiple triggers and verifications within 1
trigger; a Cluster trigger.

  .. code-block:: bash

      cd $VIRTUAL_ENV/examples/libraries/harness_cluster/

      pyats run job demo11_harness_cluster_job.py --testbed-file virl.yaml --replay mock_device

  .. note::

      Full log can be accessed from here :download:`TaskLog_demo11.html <TaskLog_demo11.html>`.


:ref:`More details<genie_harness_cluster>`
