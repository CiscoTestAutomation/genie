.. _genie_harness_cluster:

Trigger Cluster
===============

Genie Harness allows you to execute any available :testcase:`Triggers <http>`
and :verifications:`Verifications <http>`. You can also group multiple Triggers
and Verification into 1 Cluster trigger!

In the Trigger datafile:

.. code-block:: text

    TriggerCombined:
        sub_verifications: ['Verify_BgpVrfAllAll']
        sub_triggers: [ 'TriggerSleep', 'TriggerShutNoShutBgp']
        sub_order: ['TriggerSleep', 'Verify_BgpVrfAllAll', 'TriggerSleep', 'TriggerShutNoShutBgp', 'Verify_BgpVrfAllAll']
        devices: ['uut']


Which will provide this

.. code-block:: text

    -- TriggerCombined.uut                                                   PASSED
       |-- TriggerSleep_sleep.1                                              PASSED
       |-- TestcaseVerificationOps_verify.2                                  PASSED
       |-- TriggerSleep_sleep.3                                              PASSED
       |-- TriggerShutNoShutBgp_verify_prerequisite.4                        PASSED
       |   |-- Step 1: Learning 'Bgp' Ops                                    PASSED
       |   |-- Step 2: Verifying requirements                                PASSED
       |   `-- Step 3: Merge requirements                                    PASSED
       |-- TriggerShutNoShutBgp_shut.5                                       PASSED
       |   `-- Step 1: Configuring 'Bgp'                                     PASSED
       |-- TriggerShutNoShutBgp_verify_shut.6                                PASSED
       |   `-- Step 1: Verifying 'Bgp' state with ops.bgp.bgp.Bgp            PASSED
       |-- TriggerShutNoShutBgp_unshut.7                                     PASSED
       |   `-- Step 1: Unconfiguring 'Bgp'                                   PASSED
       |-- TriggerShutNoShutBgp_verify_initial_state.8                       PASSED
       |   `-- Step 1: Verifying ops 'Bgp' is back to original state         PASSED
       `-- TestcaseVerificationOps_verify.9                                  PASSED


.. note::

    Make sure you run it with trigger_uids in the jobfile or argument.

You can take any existing Triggers and execute it in any order. This gives you
all the power to create your own Cluster Trigger!

Take a look at :ref:`Example 11 <example_11>` to see a real example of it!
