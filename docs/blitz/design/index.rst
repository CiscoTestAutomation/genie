
Design
======

Each *Blitz*  testcase consists of various sections and each section itself contains various actions.
Actions are blocks of command that each perform a task as part of the testcase and report the results, as Passed, Failed, Errored etc.
Each section and action will run in the order given within the testcase.

Blitz yaml
-----------

To create a Blitz testcase, go to your Trigger datafile, or create a new yaml file if you dont have one,
and add below example into it. This example is a BGP ShutNoShut Testcase.
The yaml is commented out explaining what each section does. See example below.

.. code-block:: YAML

  # Name of the testcase
  TestBgpShutdown:
      # Location of the blitz trigger - always this same location for all blitz trigger
      source:
        pkg: genie.libs.sdk
        class: triggers.blitz.blitz.Blitz

      # Devices to run on - Default is uut
      devices: ['uut']

      # Field containing all the Testcase sections
      test_sections:

        # Section name - Can be any name, it will show as the first section of
        # the testcase
          - apply_configuration:
              # List of actions
              - configure:
                  device: R3_nx
                  command: |
                    router bgp 65000
                    shutdown
              - sleep:
                  sleep_time: 5

          # Second section name
          - verify_configuration:
              # Action #1
              # Send show command to the device and verify if part
              # of a string is in the output or not
              - execute:
                  device: R3_nx
                  command: show bgp process vrf all
                  include:
                      # Verify Shutdown is within the show run output
                    - 'Shutdown'
                  exclude:
                      # Verify Running is not within the show run output
                    - 'Running'
              # Action #2
              # Send show command and use our available parsers to make sure
              # the bgp protocol state is shutdown
              - parse:
                  device: R3_nx
                  # All action supports banner field to add to the log
                  banner: Verify bgp process is shutdown
                  command: show bgp process vrf all
                  include:
                    - get_values('shutdown')
                  exclude:
                    - not_contains('running')
          - Revert_configuration:
              # Configure action, which accepts command as an argument
              - configure:
                  device: R3_nx
                  banner: Un-Shutting down bgp 65000
                  command: |
                    router bgp 65000
                    no shutdown
          - verify_revert:
              # Send show command and verify if part of a string is in the output or not
              - execute:
                  device: R3_nx
                  command: show bgp process vrf all
                  include:
                      # Verify Running is within the show run output
                      - 'Running'
                  exclude:
                      # Verify Shutdown is not within the show run output
                      - 'Shutdown'
              # Send show command and use our available parsers to make sure
              # it is the bgp protocol state which is running
              - parse:
                  device: R3_nx
                  command: show bgp process vrf all

.. note::

  Make sure you read the comments above! After this all will make sense!



.. toctree::
    :maxdepth: 4

    design