Supported Platforms and PowerCyclers
====================================

.. note::

    pyATS Clean is designed modular to enable community-based contribution model. It is expected user communities will
    contribute to the pyATS clean stage/steps for support specifics of their given OS/Platform/Powercycler or to
    close the gap on an any features.

    Refer to the :ref:`Developer Guide <clean_doc_developer_guide>` documentation to get started in your development.

.. _clean_doc_supported_os:

Supported OS/Platforms
----------------------

The following table specifies the current set of OS and Platform types supported by pyATS Clean.

.. csv-table::
    :header: Product, os, platform

    ASR 1000, iosxe,
    ASR 1000v, iosxe,
    ISR, iosxe,
    Catalyst 9000, iosxe, cat9k
    Catalyst 8000v, iosxe, c8kv
    Nexus 7000, nxos, n7k
    Nexus 9000, nxos, n9k
    Nexus 9000v, nxos, n9k
    Nexus 9000 (aci mode), nxos, aci
    NCS 5500, iosxr,
    ASR 9000 x64, iosxr,
    ASR 9000 px, iosxr,
    APIC, apic,
    Catalyst WS-C3560CX, ios, cat3k

To use this table, locate the `Product` that corresponds with your device and fill the `os` and `platform` keys
into your Testbed YAML.

For example, if the device was a `Catalyst 9000`, then the Testbed YAML should be as follows:

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 3-7

    devices:
      catalyst-9000:
        os: iosxe
        platform: cat9k
        custom:
          abstraction:
            order: [os, platform]


.. _clean_doc_supported_pc:

Supported Power Cyclers
-----------------------

Power cyclers connection to devices are important to auto-recover the device by force reset/power off/on the devices when
they have lost connectivity. pyATS Clean provides a feature for recovering devices in the testbed if they are in a
hung state. Recovery is invoked if connecting to the device fails, or if an exception is thrown while the device is being upgraded.

.. topic:: As a brief overview, recovery includes the following steps:

    * Connect to Power Cycler and perform power cycle.
    * Connect to device and break the boot sequence, in order to bring the device to loader/rommon prompt.
    * Boots the devices with ‘golden_image’ provided as part of clean file.
    * Pass control back to pyATS Clean.

The following table specifies the current set of PowerCycler types supported by pyATS Clean.

.. list-table::
    :header-rows: 1

    * - PowerCycler
      - Arguments

    * - raritan-px
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    type: raritan-px
                    connection_type: snmp
                    host (str): Ip address for Powercycler.
                    outlets (list): Power ports associated with your device.
                    read_community (str, optional): 'private' or 'public'.
                        Defaults to 'public'.
                    write_community (str, optional): 'private' or 'public'.
                        Defaults to 'private'.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: raritan-px
                      connection_type: snmp
                      host: 127.0.0.1
                      outlets: [20]

    * - raritan-px2 (snmp)
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: raritan-px2
                      connection_type: snmp
                      host (str): Ip address for Powercycler.
                      outlets (list): Power ports associated with your device.
                      read_community (str, optional): 'private' or 'public'.
                          Defaults to 'public'.
                      write_community (str, optional): 'private' or 'public'.
                          Defaults to 'private'.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: raritan-px2
                      connection_type: snmp
                      host: 127.0.0.1
                      outlets: [20]

    * - raritan-px2 (snmpv3)
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: raritan-px2
                      connection_type: snmpv3
                      host (str): Ip address for Powercycler.
                      outlets (list): Power ports associated with your device.
                      username (str): username for Powercycler.
                      auth_key (str): authentication password.
                      auth_protocol (str): authentication protocol.
                      priv_key (str): private protocol password.
                      priv_protocol (str): private protocol type.
                      security_level (str): Different security levels.

              Snmpv3 supports three security levels:
                1. AuthPriv (Authentication and privacy)
                2. AuthNoPriv (Authentication)
                3. NoAuthNoPriv (None)

              Snmpv3 supported authentication protocols:
               'md5', 'sha', 'sha224', 'sha256, 'sha384', 'sha512'

              Snmpv3 supported private protocols:
               'des', '3des',  'aes128',  'aes192', 'aes256'

            Testbed Example
            ---------------
            Type 1: (AuthPriv)

            devices:
                PE1:
                  peripherals:
                    power_cycler:
                        type: raritan-px2
                        connection_type: snmpv3
                        host: pdu_host
                        outlets: [15]
                        username: test_user
                        auth_key: ****
                        auth_protocol: md5
                        priv_key: ****
                        priv_protocol: aes128
                        security_level: authpriv

              Type 2: (AuthNoPriv)

              devices:
                PE1:
                  peripherals:
                    power_cycler:
                        type: raritan-px2
                        connection_type: snmpv3
                        host: pdu_host
                        outlets: [15]
                        username: test_user
                        auth_key: ****
                        auth_protocol: md5
                        security_level: authnopriv

              Type 3: (NoAuthNoPriv)

              devices:
                PE1:
                  peripherals:
                    power_cycler:
                        type: raritan-px2
                        connection_type: snmpv3
                        host: pdu_host
                        outlets: [15]
                        username: test_user
                        security_level: noauthnopriv

    * - generic-cli
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: generic-cli
                      host (str): Ip address for Powercycler.
                      connection_type: ssh
                      outlets (list, optional): Power ports associated with your device.
                      commands (dict):
                          power_on (str): Command to power on the Powercycler
                          power_off (str): Command to power off the Powercycler

            Description
            -----------

              Commands argument takes in any power_on and power_off commands,
              which are mandatory.

              Example: 1 (If outlets are used)

              These commands should have outlet string on it, if the power cycle
              is based on oulet. For example

                  commands:
                        power_on: "power outlets {outlet} on"
                        power_off: "power outlets {outlet} off"

              It is mandatory to specify the {outlet} as this string format.

              Example: 2 (If device names are used)

              If the device name is used to powercycle. Please refer
              the example below:

                  commands:
                        power_on: "power-tool %{self} on"
                        power_off: "power-tool %{self} off"

              Here %{self} takes the device name from the testbed.


            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: generic-cli
                      host: 127.0.0.1
                      connection_type: ssh
                      outlets: [6]
                      commands:
                          power_on: "power outlets {outlet} on"
                          power_off: "power outlets {outlet} off"

    * - Raritan
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: Raritan
                      host (str): Ip address for Powercycler.
                      connection_type: ssh
                      outlets (list): Power ports associated with your device.

            Description
            -----------
              The power_on and power_off commands for Raritan are added by default.
              The user needs to pass the outlets.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                      - type: Raritan
                        host: 127.0.0.1
                        connection_type: telnet
                        outlets: [7]

    * - apc
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: apc
                      connection_type: snmp
                      host (str): Ip address for Powercycler.
                      outlets (list): Power ports associated with your device.
                      read_community (str, optional): 'private' or 'public'.
                          Defaults to 'public'.
                      write_community (str, optional): 'private' or 'public'.
                          Defaults to 'private'.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: apc
                      connection_type: snmp
                      host: 127.0.0.1
                      outlets: [20]

    * - apc-rpdu
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: apc-rpdu
                      connection_type: snmp
                      host (str): Ip address for Powercycler.
                      outlets (list): Power ports associated with your device.
                      read_community (str, optional): 'private' or 'public'.
                          Defaults to 'public'.
                      write_community (str, optional): 'private' or 'public'.
                          Defaults to 'private'.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: apc-rpdu
                      connection_type: snmp
                      host: 127.0.0.1
                      outlets: [20]

    * - dualcomm
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: dualcomm
                      connection_type: snmp
                      host (str): Ip address for Powercycler.
                      outlets (list): Power ports associated with your device.
                      read_community (str, optional): 'private' or 'public'.
                          Defaults to 'public'.
                      write_community (str, optional): 'private' or 'public'.
                          Defaults to 'private'.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: dualcomm
                      connection_type: snmp
                      host: 127.0.0.1
                      outlets: [20]

    * - cyberswitching
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: cyberswitching
                      connection_type: telnet
                      host (str): Cyberswitching device from Testbed YAML.
                      outlets (list): Lines associated with your device.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: cyberswitching
                      connection_type: telnet
                      host: my-cyberswitching
                      outlets: [20]

              my-cyberswitching:
                # Fill out the rest of this device as normal
                # such as connection info, credentials, etc

    * - ESXi
      - .. code-block:: yaml

            Testbed Schema
            --------------
            devices:
              <device>:
                peripherals:
                  power_cycler:
                    - type: esxi
                      connection_type: ssh
                      host (str): ESXi device from Testbed YAML.
                      outlets (list): VM IDs associated with your device.

            Testbed Example
            ---------------
            devices:
              PE1:
                peripherals:
                  power_cycler:
                    - type: esxi
                      connection_type: ssh
                      host: my-esxi
                      outlets: [20]

              my-esxi:
                # Fill out the rest of this device as normal
                # such as connection info, credentials, etc

To use this table, locate the `PowerCycler` that corresponds with yours and fill the arguments into your Testbed YAML
under the device peripherals key.

For example, if the PowerCycler was a `dualcomm` connected to PE1, then the Testbed YAML should be modified as follows:

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 3-8

    devices:
      PE1:
        peripherals:
          power_cycler:
            - type: dualcomm
              connect_type: snmp
              host: 127.0.0.1
              outlets: [22]

You could have more than one PowerCyclers connected to your device. For example, if you have two PowerCycler with `dualcomm` type connected to PE1,
then the Testbed Yaml looks like this:


.. code-block:: yaml
    :linenos:
    :emphasize-lines: 3-8

    devices:
      PE1:
        peripherals:
          power_cycler:
            - type: dualcomm
              connect_type: snmp
              host: 127.0.0.1
              outlets: [22]
            - type: dualcomm
              connect_type: snmp
              host: 127.0.0.2
              outlets: [20]


See :ref:`Device Recovery <clean_doc_device_recovery>` for additional information.
