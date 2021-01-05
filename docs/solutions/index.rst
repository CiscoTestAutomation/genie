.. _genie_solutions:

Genie Solutions
===============

This page contains typical real life problems which network engineers face in
their day-to-day activities and how Genie can help with this.

Continous Device Validation
---------------------------

Problem #1
^^^^^^^^^^

Verifying device output is one of the most common, yet the most critical task for
network engineers in executing their testplan. However, repeating this task for
100+ devices in a scaled topology introduces room for human errors.

Solution #1
^^^^^^^^^^^

`genie parse` CLI can execute and parse several show-commands on all devices within
a topology using just one linux command! ``Genie`` is capable of executing
all show-commands required as part of a network engineer's testplan and saving
the state of *all* devices by parsing the device output into Python datastructures.

These Python datastructures can then be re-generated periodically, and compared
against the first/golden previously validated `snapshot` of the devices using
`genie diff`.

``Genie`` has over 500+ parsers available to parse your device output across
several operating systems. Depending on your automation needs, there are many
ways to parse a device output.

The following in an example that demonstrates the solution above:

**Step1 Take initial snapshot**

.. code-block:: bash

    # Ensure your Python virtual environment is sourced

    # The --replay is needed as we are using our Mocked Device.
    # When Genie cli is used with real devices, it should be omitted.

    # Execute the required show commands and save the Python datastructures into
    # directory 'initial_snapshot'

    genie parse "show bgp process vrf all" \
          --testbed-file $VIRTUAL_ENV/examples/libraries/solutions/solution1/testbed.yaml \
          --device nx-osv-1 \
          --output initial_snapshot \
          --replay $VIRTUAL_ENV/examples/libraries/solutions/solution1/run1

    100%|############################################################| 1/1 [00:01<00:00,  1.62s/it]
    +======================================================================================+
    | Genie Parse Summary for nx-osv-1                                                     |
    +======================================================================================+
    |  Connected to nx-osv-1                                                               |
    |  -  Log: initial_snapshot/connection_nx-osv-1.txt                                    |
    |--------------------------------------------------------------------------------------|
    |  Parsed command 'show bgp process vrf all'                                           |
    |  -  Parsed structure: initial_snapshot/nx-osv-1_show-bgp-process-vrf-all_parsed.txt  |
    |  -  Device Console:   initial_snapshot/nx-osv-1_show-bgp-process-vrf-all_console.txt |
    |--------------------------------------------------------------------------------------|

**Step2 Take second snapshot**

After some period of time; you can now verify the state of your device based on
the previously taken snapshot!

.. code-block:: bash

    # The --replay is needed as we are using our Mocked Device.
    # When Genie cli is used with real devices, it should be omitted.

    # Execute the required show commands and save the Python datastructures into
    # directory 'current_snapshot'

    genie parse "show bgp process vrf all" \
    	  --testbed-file $VIRTUAL_ENV/examples/libraries/solutions/solution1/testbed.yaml \
    	  --device nx-osv-1 \
    	  --output current_snapshot \
          --replay $VIRTUAL_ENV/examples/libraries/solutions/solution1/run2

    100%|############################################################| 1/1 [00:01<00:00,  1.62s/it]
    +======================================================================================+
    | Genie Parse Summary for nx-osv-1                                                     |
    +======================================================================================+
    |  Connected to nx-osv-1                                                               |
    |  -  Log: current_snapshot/connection_nx-osv-1.txt                                    |
    |--------------------------------------------------------------------------------------|
    |  Parsed command 'show bgp process vrf all'                                           |
    |  -  Parsed structure: current_snapshot/nx-osv-1_show-bgp-process-vrf-all_parsed.txt  |
    |  -  Device Console:   current_snapshot/nx-osv-1_show-bgp-process-vrf-all_console.txt |
    |--------------------------------------------------------------------------------------|

**Step3 Compare both snapshots**

Execute `genie diff` to check the diffs between the first and second set of
device outputs

.. code-block:: bash

    (genie) bash-4.1$ genie diff current_snapshot initial_snapshot --output sol1_diff
    1it [00:01,  1.44s/it]
    +=======================================================================================+
    | Genie Diff Summary between directories current_snapshot/ and initial_snapshot/        |
    +=======================================================================================+
    |  File: nx-osv-1_show-bgp-process-vrf-all_parsed.txt                                   |
    |   - Diff can be found at sol1_diff/diff_nx-osv-1_show-bgp-process-vrf-all_parsed.txt  |
    |---------------------------------------------------------------------------------------|


    (genie) bash-4.1$ more sol1_diff/diff_nx-osv-1_show-bgp-process-vrf-all_parsed.txt
    --- current_snapshot/nx-osv-1_show-bgp-process-vrf-all_parsed.txt
    +++ initial_snapshot/nx-osv-1_show-bgp-process-vrf-all_parsed.txt
    
    +bgp_protocol_state: running
    -bgp_protocol_state: shutdown

The same idea can be done with :ref:`genie learn<cli_learn>`.
