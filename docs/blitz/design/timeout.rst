

Trigger timeout/interval ratio adjustments
=============================================

Each action performs verification to make sure it has performed as expected.
These timeouts can be modified with a ratio from the testbed datafile.
This feature is supported by actions ``api``, ``execute``, ``parse``, ``learn`` and ``rest``.

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
                        command: show version
                        include:
                          - 'w'
                        max_time: 5
                        check_interval: 1
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

Now the max_time and will half'd.

