January 2020
=============

February 4th - Genie v20.1
----------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.1                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.1                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

Note that this will leave older v19.12 packages around in pip list, but it will
not impact anything (visual only).  An update command can be used to clean up
these packages

.. code-block:: bash

   pyats version update

Features:
^^^^^^^^^

- The following packages:

  *  `genie.parsergen`,
  *  `genie.metaparser`,
  *  `genie.abstract`,
  *  `genie.predcore`
  *  `genie.ops`
  *  `genie.conf`
  *  `genie.harness`
  *  `genie.utils`

  have all been merged within `genie` package. No more separate pip packages
  for each of them.

- `genie` command line is now deprecated. All functionalities has been merged
  to `pyats` command line.

- Genie `Blitz` is a new way to write quick Trigger. All driven via `YAML` file, no
  need to write python, allowing quick Trigger/Testcase development. :blitz:`Full
  documentation on Blitz<http>`.

This is a whole testcase

.. code-block:: yaml

  TestBgpShutdown:
      # Location of the blitz trigger
      source:
        pkg: genie.libs.sdk
        class: triggers.blitz.blitz.Blitz
  
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
                  output:
                      - "[bgp_protocol_state][shutdown]"
  
- Grand total of 574 :apis:`network automation apis <http>`. Ready for you to use and
  contribute to it.  Fully open sourced!

You can call them by doing

.. code-block:: python

    >>> device.apis.get_interface_mtu_size(device, 'Ethernet2/3')
    1500

- Grand total of 1585 :parsers:`parsers<http>`.

.. code-block:: python

    >>> device.parse('show version')
        {'version': {'version_short': '16.9',
          'platform': 'Virtual XE',
          'version': '16.9.1',
          'image_id': 'X86_64_LINUX_IOSD-UNIVERSALK9-M',
          'os': 'IOS-XE',
          ...
        }}


**Genie**
 * Modification to the pip packages


**Genie.Libs.Parser**
 * 25 new IOSXE, IOS, NXOS & IOSXR Parsers!
 * Grand total of 1585 parsers
 * Changelog can be checked :parserchangelog20:`here <JANUARY>`


**Genie.Libs.Ops**
 * New `ISIS`, OPS structures on IOSXR, IOS, NXOS and IOSXE(cat9k)
 * Changelog can be checked :opschangelog20:`here <JANUARY>`


**Genie.Libs.Conf**
 * No change!
 * Changelog can be checked :confchangelog20:`here <JANUARY>`


**Genie.Libs.Sdk**
 * 9 new :apis:`network automation apis <http>` to interact with your devices
 * Updated to current apis to support more arguments
 * Changelog can be checked :sdkchangelog20:`here <JANUARY>`


**Genie.Libs.Robot**
 * No change!


**Genie.Telemetry**
 * No change!


**Genie.Libs.Telemetry**
 * No change!


**Genie.FileTransferUtils**
 * No change!


**Genie.Examples**
 * Deprecated in 19.7
 * As a reminder, all examples can be found at: https://github.com/CiscoTestAutomation/


**Genie.Trafficgen**
 * Enhancements for corner cases where tx_rate, rx_rate, loss % columns in
   'Traffic Item Statistics' are either empty ('') or star ('*')
 * Added 'remove_configuration' to remove configuration from Ixia device

