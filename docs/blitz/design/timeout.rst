

Action verification timeouts
============================

Trigger timeout/interval ratio adjustments
------------------------------------------

Each action performs verification to make sure it has performed as expected.
These timeouts can be modified with a ratio from the testbed datafile.
This feature is supported by actions ``api``,``execute``,``parse``,``learn``and``rest``.

.. code-block:: YAML

    # Name of the testcase
    Testcase1:

        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz

        # Field containing all the sections
        test_sections:

            # Section name - Can be any name, it will show as the first section
            # of the testcase
                - apply_configuration:
                    - execute:
                        device: PE2
                        command: show version
                        include:
                          - 'w'
                        max_time: 10
                        check_interval: 2
        ...

.. code-block:: YAML

  devices:
    PE2:
      connections:
        ssh:
          ip: 10.255.1.17
          protocol: ssh
      credentials:
        default:
          password: cisco
          username: cisco
        enable:
          password: cisco
      custom:
        max_time_ratio: '0.5'
        check_interval_ratio: 0.5
      os: iosxe
      type: CSR1000v

Blitz applies the ratios before verification. This example uses a five-second
timeout and a one-second check interval.

.. _blitz-final-sample:

Final sample at the deadline
----------------------------

Set ``final_sample: true`` alongside ``max_time`` and ``check_interval`` to
allow one final verification attempt at the deadline. Blitz still checks the
initial output immediately and stops retrying as soon as the check matches. An
attempt already running at the deadline counts as the final sample. The default
for ``final_sample`` is ``false``.

This option applies to output checks in ``api``, ``execute``, ``parse``,
``learn``, ``rest``, ``bash_console``, and ``yang``, and to ``scope`` and
``extract`` in ``execute``. Specify a finite, nonnegative ``max_time`` and a
finite, positive ``check_interval``, both in seconds. For actions that apply
testbed ratios, these limits apply after scaling. A zero ``max_time`` uses the
initial output as the final sample.

.. code-block:: yaml

    - execute:
        device: router
        command: show ip bgp neighbors 192.0.2.1
        include:
          - 'BGP state = Established'
        max_time: 30
        check_interval: 5
        final_sample: true
