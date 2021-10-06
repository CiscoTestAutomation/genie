.. _pyats_harness:

Genie within pyATS
==================

Every :triggers:`triggers <http>` and :verifications:`Verifications <http>` can
be re-used within any pyATS testscript with GenieStandalone and run_genie_sdk.

There are two ways to do it:

1. :ref:`Run any verification and trigger as a pyATS Testcase<pyats_harness_tc>`
2. :ref:`Run any verification and trigger within a pyATS section<pyats_harness_section>`

.. _pyats_harness_tc:

**1. Run any verification and trigger as a pyATS Testcase**

.. code-block:: text

    |-- tc_genie_trigger                                                     PASSED
       |-- TriggerShutNoShutBgp_verify_prerequisite.1                        PASSED
       |   |-- Step 1: Learning 'Bgp' Ops                                    PASSED
       |   |-- Step 2: Verifying requirements                                PASSED
       |   `-- Step 3: Merge requirements                                    PASSED
       |-- TriggerShutNoShutBgp_shut.2                                       PASSED
       |   `-- Step 1: Configuring 'Bgp'                                     PASSED
       |-- TriggerShutNoShutBgp_verify_shut.3                                PASSED
       |   `-- Step 1: Verifying 'Bgp' state with ops.bgp.bgp.Bgp            PASSED
       |-- TriggerShutNoShutBgp_unshut.4                                     PASSED
       |   `-- Step 1: Unconfiguring 'Bgp'                                   PASSED
       |-- TriggerShutNoShutBgp_verify_initial_state.5                       PASSED
       |   `-- Step 1: Verifying ops 'Bgp' is back to original state         PASSED
       `-- TriggerSleep_sleep.6                                              PASSED

Adding a trigger and a verification to a pyATS script is very easy.

Within your pyATS add the following:

.. code-block:: python

    # Import needed to run any Verification and Trigger
    from genie.harness.standalone import GenieStandalone


    #####################################################################
    ####                 Genie Harness information                    ###
    #####################################################################
    # Enter the name of the verification and trigger name which you want to run
    class GenieTriggerVerification(GenieStandalone):
        # This will run in this order
        # Verify_BgpVrfAllAll
        # TriggerShutNoShutBgp
        # Verify_BgpVrfAllAll
        # TriggerSleep
        # Verify_BgpVrfAllAll
        triggers = ['TriggerShutNoShutBgp', 'TriggerSleep']
        verifications = ['Verify_BgpVrfAllAll']

    class GenieTriggerVerification_order(GenieStandalone):
        # This will run in this order; as specified
        # TriggerShutNoShutBgp
        # Verify_BgpVrfAllAll
        # TriggerSleep
        triggers = ['TriggerShutNoShutBgp', 'TriggerSleep']
        verifications = ['Verify_BgpVrfAllAll']
        order = ['TriggerShutNoShutBgp', 'Verify_BgpVrfAllAll', 'TriggerSleep']
        custom_arguments = {
            'TriggerSleep': {
                'devices': ['uut', 'P1'],
                'sleep_time': 8
            },
            'TriggerShutNoShutBgp': {
                'devices': ['uut', 'P1'],
                'count': 2,
                'timeout': {
                    'max_time': 20,
                    'interval': 10
                }
            }
        }

Note that the class must inherits from GenieStandalone, which itself inherits from the pyATS `Testcase`, and
everything provided in `custom_arguments` will overwrite the information in the trigger datafile.

:ref:`Example <example>` 7 demonstrates it in action.

.. _pyats_harness_section:

**2. Run any verification and trigger within a pyATS section**

.. code-block:: text

    -- tc_pyats_genie                                                       PASSED
       |-- simple_test_1                                                    SKIPPED
       |   |-- Step 1: Verify_BgpVrfAllAll                                   PASSED
       |   |-- Step 2: TriggerSleep                                          PASSED
       |   |-- Step 3: TriggerShutNoShutBgp                                 SKIPPED
       |   |-- Step 3.1: Learning 'Bgp' Ops                                  PASSED
       |   |-- Step 3.2: Verifying requirements                             SKIPPED
       |   `-- Step 3.3: Merge requirements                                 SKIPPED
       `-- simple_test_2                                                    PASSED


Triggers and Verification can also be executed as :steps:`steps <http>` within
a sections! 

.. code-block:: python

    # You can also call Triggers and Verifications within a pyATS section
    class tc_pyats_genie(aetest.Testcase):
        # First test section
        @ aetest.test
        def simple_test_1(self, steps):
            """ Sample test section. Only print """
            log.info("First test section ")

            # Run genie triggers and verifications
            run_genie_sdk(self,
                          steps, [
                              'Verify_BgpVrfAllAll', 'TriggerSleep',
                              'TriggerShutNoShutBgp', 'TriggerSleep',
                              'Verify_BgpVrfAllAll'
                          ],
                          parameters={
                              'TriggerSleep': {
                                  'devices': ['uut', 'P1'],
                                  'sleep_time': 8
                              },
                              'TriggerShutNoShutBgp': {
                                  'devices': ['uut', 'P1'],
                                  'count': 2,
                                  'timeout': {
                                      'max_time': 20,
                                      'interval': 10
                                  }
                              }
                          })

`run_genie_sdk` allows to run any triggers and verifications. `self` and
`steps` must be passed, then a list of what to execute. The device on which to
execute the testcase can also be modified by providing the device
name `uut='nx-osv-1'`. A `parameters` argument can also be provided to overwrite the data in the trigger datafile.

If any of them fails, then the step rollup will also fail the testcase.

Custom trigger and verification datafile can be provided with the
`--trigger-datafile` and `--verification-datafile` arguments.

