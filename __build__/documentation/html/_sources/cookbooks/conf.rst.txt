.. _book_conf:

.. raw:: html

   <h2>Genie Configuration Recipes</h2>

.. note::

    This section assumes pyATS and Genie are :ref:`installed and ready to be
    used<book_genie>`.

1. Summary
----------

.. note::

    This section gives a summary of what is an Conf object. Dig into the
    documentation for more information.

Using a python object, set some attributes and the configuration is generated
for you.  With Genie you configure a device by only thinking of the network by
following a common structure which works across mutliple platforms.  Each
object follows a structure which is based on the feature.

Here are some use cases where these objects are useful:

1. Have to configure multiple devices of different operating system.
2. Maintain one script which works across multiple operating system. 
3. Drive configuration with Python object


2. Configure a device without using any command - ``Conf`` object
-----------------------------------------------------------------

Think of what you want to apply on your device, not how to do it on this
platform. Genie `conf` provides a structure which is feature based and not
platform based. This mean, it stays the same for all platform and figure out
how to apply on the device.

.. code-block:: python

    from genie import testbed
    from genie.conf.base import Interface
    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.connect()
    # Create an NXOS interface
    nxos_interface = Interface(device=uut, name='Ethernet4/3')
    # Add some configuration
    nxos_interface.ipv4 = '200.1.1.2'
    nxos_interface.ipv4.netmask ='255.255.255.0'
    nxos_interface.switchport_enable = False
    nxos_interface.shutdown = False
    # Verify configuration generated
    print(nxos_interface.build_config(apply=False))
    # interface Ethernet4/3
    #  no shutdown
    #  no switchport
    #  ip address 200.1.1.2 255.255.255.0
    #  exit
    nxos_interface.build_config() # To apply on the device
    nxos_interface.build_unconfig() # To remove configuration

Doing the same for IOSXE, will generate iosxe configuration.

.. code-block:: python

    iosxe_interface = Interface(device=iosxe_device, name='Ethernet4/3')
    # Add some configuration
    iosxe_interface.ipv4 = '200.1.1.2'
    iosxe_interface.ipv4.netmask ='255.255.255.0'
    iosxe_interface.switchport_enable = False
    iosxe_interface.shutdown = False
    # Verify configuration generated
    print(iosxe_interface.build_config(apply=False))
    # interface Ethernet4/3
    #  ip address 200.1.1.2 255.255.255.1
    #  no shutdown
    #  exit

Every one of those configuration object are driven with such attributes
following a :models:`specific structure<http>`.

.. raw:: html

    <script src="https://asciinema.org/a/YOhsurNyG4kXNGiQy65ycqxP6.js" id="asciicast-YOhsurNyG4kXNGiQy65ycqxP6" async></script>


3. Configure single/partial attributes on a device with ``Conf`` object
------------------------------------------------------------------------

By default, all attributes set will generate configuration on the device.

Passing argument `attributes` limits which what configuration will be generated
for the device.

Let's revisit a similar example as seen above.

.. code-block:: python

    # Instantiate IOSXE interface conf object
    iosxe_interface = Interface(device=iosxe_device, name='Ethernet2/1')

    # Lets set multiple attributes of this Interface Conf object
    iosxe_interface.mtu = 2500
    iosxe_interface.switchport_enable = True
    iosxe_interface.ipv4 = '200.1.1.2'
    iosxe_interface.ipv4.netmask ='255.255.255.0'
    iosxe_interface.shutdown = False

    # Lets generate configuration for specific attribute 'ipv4' only
    temp_config1 = iosxe_interface.build_config(apply=False, attributes={'ipv4': None})
    print(temp_config1)
    # interface Ethernet2/1
    #  ip address 200.1.1.2 255.255.255.0
    #  exit

    # Lets generate configuration for specific attribute 'switchport_enable' only
    temp_config2 = iosxe_interface.build_config(apply=False, attributes={'switchport_enable': None})
    print(temp_config2)
    # interface Ethernet2/1
    #  switchport
    #  exit

    # Lets generate configuration for multiple specific attributes 'mtu' and 'shutdown'
    temp_config3 = iosxe_interface.build_config(apply=False, attributes={'mtu': None, 'shutdown': None})
    print(temp_config3)
    # interface Ethernet2/1
    #  mtu 2500
    #  no shutdown
    #  exit

    # Lets unconfigure specific attribute 'mtu' only
    temp_config4 = iosxe_interface.build_unconfig(apply=False, attributes={'mtu': None})
    print(temp_config4)
    # interface Ethernet2/1
    #  no mtu 2500
    #  exit

    # Lets unconfigure multiple specific attributes 'ipv4' and 'switchport'
    temp_config5 = iosxe_interface.build_unconfig(apply=False, attributes={'ipv4': None, 'switchport_enable': None})
    print(temp_config5)
    # interface Ethernet2/1
    #   no ip address 200.1.1.2 255.255.255.0
    #   no switchport
    #   exit

    # Generate config strings from all attributes set above and apply to device
    iosxe_interface.build_config()

    # Generate un-config strings from all attributes set above and remove from device
    iosxe_interface.build_unconfig() # To remove configuration

As seen in the examples above, by explicitly specifying the attributes we want,
``Genie`` builds configuration strings only for those specific attributes which
can then be applied or removed from the device accordingly.


4. Configure multiple device with ``Conf`` object
-------------------------------------------------

You can also apply configuration from a testbed point of view instead of per
feature or device level.


.. code-block:: python

    # To verify what will applied on the devices
    testbed.build_config(apply=False)
    # And to apply on the devices
    testbed.build_config()

This can be useful for driving multiple devices. If there is more than 1
device, then the configuration is applied in parallel on the devices.

.. raw:: html

    <script src="https://asciinema.org/a/jOMe7lxpsrDEBvaOeAECegqVL.js" id="asciicast-jOMe7lxpsrDEBvaOeAECegqVL" async></script>


5. Configure a device with different context. (Cli, Yang, ...)
---------------------------------------------------------------

The greatness of Genie Conf is the structure remains agnostic of the OS, or the
interface management. 

The following code generates different output depending of the device but the
code itself does not change.

.. code-block:: python

    iosxe_interface = Interface(device=iosxe_device, name='GigabitEthernet0/0/1')
    # Add some configuration
    iosxe_interface.ipv4 = '200.1.1.2'
    iosxe_interface.ipv4.netmask ='255.255.255.0'
    iosxe_interface.shutdown = False
    # Verify configuration generated
    print(iosxe_interface.build_config(apply=False))
    # interface Ethernet4/3
    #  ip address 200.1.1.2 255.255.255.0
    #  no shutdown
    #  exit

With the following testbed, then the Yang configuration is generated.

.. code-block:: yaml

    devices:
      nx-osv-1:
          alias: 'uut'
          type: 'Iosxe'
          os: 'iosxe'
          tacacs:
              login_prompt: "login:"
              password_prompt: "Password:"
              username: "admin"
          passwords:
              tacacs: Cisc0123
              enable: admin
              line: admin
          connections:
              defaults:
                class: 'unicon.Unicon'
              vty:
                  protocol: telnet
                  ip: "172.25.192.90"
          custom:
            abstraction:
              order: [os, context]
              context: 'yang'

Then this configuration is generated:

.. code-block:: text

    <edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
       <target>
         <running></running>
       </target>
       <config>
         <GigabitEthernet xmlns="...">
           <name>0/0/1</name>
           <ip>
             <address>
               <primary>
                 <address>1.2.3.4</address>
                 <mask>255.255.255.252</mask>
               </primary>
             </address>
           </ip>
           <shutdown xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="delete"/>
         </GigabitEthernet>
       </config>
     </edit-config>

6. Quickly find what you are looking for with the `find` object
---------------------------------------------------------------

Want to find an Ethernet interface which connect two devices dynamically?  The
find api is what you are looking for! Take a :ref:`quick read<book_ops_find>`
on how it works for dictionary and Ops object.

Then go over the :ref:`find<find>` documentation!

7. Where are the object models located ?
----------------------------------------

All the objects models are displayed on our :models:`models page <http>`.

8. How to contribute
--------------------

To contribute to the code of Genie, take a look at our :commit:`commit <http>`
guideline! 

To contribute to the Conf object models, visit the :conf:`Conf contribution`
page.

