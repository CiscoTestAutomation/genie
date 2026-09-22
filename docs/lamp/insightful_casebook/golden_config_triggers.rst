Golden Configurations as Blitz Triggers
========================================

Golden configurations define the standard or reference configuration for a network topology.
Traditionally, they're created by saving a manually configured device's running configuration and re-applied using
'configure replace'.

However, this approach has limitations: poor automation, difficult parameterization, and no built-in verification.
Instead, use Blitz YAML triggers to define golden configurations with these advantages:

  - **Unified Configuration File**: All device configurations within a single file, as opposed to separate per-device configuration files
  - **Direct Application**: Apply through LAMP shell without test scripts
  - **Parameterizable**: Adapt configurations to different testbeds
  - **Built-in Verification**: Include validation checks within the same file
  - **Reusable**: Change parameters to work with different topologies

How It Works
------------

The workflow is straightforward:

1. **Configure each device**: Create a ``configure`` action for each device
2. **Verify state**: Add ``execute`` actions to verify successful application

Design Principles
-----------------

Follow these best practices when creating golden configurations:

**1. Device-by-Device Configuration**

Apply configuration to one device at a time. Keep all configuration for a single device within one ``configure`` action if possible:

.. code-block:: yaml

    - configure:
        device: device1
        command: |-
          interface Ethernet0/0
          ip address 10.0.0.1 255.255.255.0
          no shutdown
          exit
          !
          interface Loopback0
          ip address 1.1.1.1 255.255.255.255
          exit

**2. Use Parameters for Topology-Specific Values**

Parameterize values that change across testbeds (interface names, device names).
Avoid parameterizing constant values (IP addresses, protocol numbers).
Dump parameters in the trigger to adapt the configuration easily:

.. code-block:: yaml

    parameters:
      device1_to_device2: Ethernet0/0
      device2_to_device1: Ethernet0/1
      # Good: interface names (vary across testbeds)
      # Avoid: IP addresses like 10.0.0.1 vs 20.0.0.1 (no logical difference)

**3. Include Verification Sections**

Add verification steps to confirm the configuration applied successfully and the devices are in steady state:

.. code-block:: yaml

    - verify_configuration:
        - sleep:
            sleep_time: 60
        - execute:
            device: device1
            command: show ip route
            include:
              - C\s*1.1.1.1
              - O\s*2.2.2.2

Complete Example: OSPF Topology with Loopbacks
-----------------------------------------------

Here's a complete golden configuration for a 2-device topology with OSPF and loopback interfaces:

.. code-block:: yaml

    parameters:
      d1_to_d2: Ethernet0/0
      d2_to_d1: Ethernet0/0

    tc:
      source:
        pkg: genie.libs.sdk
        class: triggers.blitz.blitz.Blitz

      devices:
        - device1
        - device2

      test_sections:
        - configure_devices:

            # Configure device1
            - configure:
                device: device1
                command: |-
                  interface %{parameters.d1_to_d2}
                  ip address 10.0.0.1 255.255.255.0
                  ip ospf 10 area 0
                  no shutdown
                  exit
                  !
                  interface Loopback0
                  ip address 1.1.1.1 255.255.255.255
                  ip ospf 10 area 0
                  exit
                  !

            # Configure device2
            - configure:
                device: device2
                command: |-
                  interface %{parameters.d2_to_d1}
                  ip address 10.0.0.2 255.255.255.0
                  ip ospf 10 area 0
                  no shutdown
                  exit
                  !
                  interface Loopback0
                  ip address 2.2.2.2 255.255.255.255
                  ip ospf 10 area 0
                  exit
                  !

        # Verify configuration was applied successfully
        - verify_configuration:

            # Wait for OSPF convergence
            - sleep:
                sleep_time: 60

            # Verify device1 learned routes
            - execute:
                device: device1
                command: show ip route
                include:
                  - C\s*1.1.1.1
                  - O\s*2.2.2.2
                  - L\s*10.0.0.1
                max_time: 100
                check_interval: 10

            # Verify device2 learned routes
            - execute:
                device: device2
                command: show ip route
                include:
                  - C\s*2.2.2.2
                  - O\s*1.1.1.1
                  - L\s*10.0.0.2
                max_time: 100
                check_interval: 10

Applying Golden Configurations from LAMP
-----------------------------------------

Apply your golden configuration from the LAMP shell using the ``replay`` command:

.. code-block:: console

    (lamp) replay golden_ospf_topology.yaml
