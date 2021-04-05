.. _topology_testbed:

Topology
========

In this section, users will learn how to create and use the ``Genie`` topology.

Introduction
------------

The Genie topology is based on the :pyats_topology:`pyats topology <http>`. There are two ways to
create the ``Genie`` topology:

 1. Automatically : By converting the ``pyATS`` Testbed object into the ``Genie`` Testbed 
 	object. This is the most common way to create the ``Genie`` topology.
 2. Manually: By creating each topology object and then interconnecting them
     using their corresponding APIs.  Whenever users manually create the ``Genie`` topology, 
     the APIs can enable topology modifications in runtime (ex: adding loopback interface).

Automatic Creation
------------------

The ``pyATS`` testbed topology is based on the `testbed` yaml file, converted 
to ``Genie`` testbed. All  devices, interfaces, and links defined in the 
`testbed` yaml file are created as part of the ``Genie`` testbed object.

In the example below, users will see that the `Genie.testbed` variable stores the
`Testbed` object as a class variable. This enables users to use the 
object in functions without having to pass it as parameter. 

.. code-block:: python

    # Import Genie Entry point
    from genie.conf import Genie

    # Using pyATS Testbed object, instantiate a Genie testbed object
    genie_testbed = Genie.init(testbed=pyats_testbed)

    # From this point
    assert Genie.testbed  == genie_testbed


Manual Creation
---------------

Instances where user manually create the ``Genie`` topology, the script can
create the `Genie` Testbed object, `device`, `link`, and its `interfaces` during runtime. 

.. code-block:: python

   # import modules
   from genie.conf.base import Testbed, Device, Interface, Link
   from pyats.datastructures.logic import And, Not, Or

   # Create a Testbed
   testbed = Testbed(name='myTestbed')

   # Create two devices
   # Adding testbed=testbed automatically bind the devices to the testbed.
   dev1 = Device(name='PE1', testbed=testbed, os='nxos')
   dev2 = Device(name='P1', testbed=testbed, os='nxos')

   # Let's add an interface for each device
   # Adding device=<dev object> automatically bind the interface to a device
   intf_dev1 = Interface(name='Ethernet3/7', device=dev1)
   intf_dev2 = Interface(name='Ethernet3/7', device=dev2)

   # Now some link to connect those 2 interfaces
   # A link must be part of a testbed
   link1 = Link(name='dev1-dev2-1', testbed=testbed)
   link1.connect_interface(intf_dev1)
   link1.connect_interface(intf_dev2)

   # We now have a testbed, which contains two devices.
   # Those two devices each contains an interface, that are interconnected
   >>> testbed.devices
   TopologyDict({'PE1': <Device object 'PE1' at 0xf6ef9cec>,
                 'P1': <Device object 'P1' at 0xf6e9e22c>})

   # Each device has 1 interface
   >>> testbed.devices['P1']
   <Device object 'P1' at 0xf6e9e22c>
   >>> testbed.devices['P1'].interfaces
   TopologyDict({'Ethernet3/7': 
   <EthernetInterface object 'Ethernet3/7' on 'P1' at 0xf6e5e1ec>})

   >>> testbed.devices['PE1']
   <Device object 'PE1' at 0xf6ef9cec>
   >>> testbed.devices['PE1'].interfaces
   TopologyDict({'Ethernet3/7':
   <EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6ea388c>})

   # Testbed has a link
   >>> testbed.links
   {<Link object 'dev1-dev2-1' at 0xf6e5e94c>}

   # Which connect two interfaces together
   >>> for link in testbed.links: link.interfaces
   WeakList([<EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6ea388c>,
             <EthernetInterface object 'Ethernet3/7' on 'P1' at 0xf6e5e1ec>])
   

.. _testbed:

Testbed Object
--------------

The `Testbed` object is the entry point of the ``Genie`` Topology. The 'Testbed` has
access to all of the objects of the topology. By using the `find_` method, 
the `Testbed` can also filter through all of the objects based
on the user's requirements.

For more information on the `find_<...>` APIs, users may consult the :ref:`find mechanism <find>`.

.. code-block:: text

    +--------------------------------------------------------------------------+
    | Testbed object                                                           |
    +==========================================================================+
    | Attributes            | Description                                      |
    |-----------------------+--------------------------------------------------|
    | name                  | Testbed name, should be unique                   |
    | devices               | Dict of testbed devices                          |
    | interfaces            | Tuple of all interfaces in this testbed          |
    | links                 | Set of testbed links                             |
    | features              | List of all the features in this testbed         |
    | ipv4_cache            | Available ipv4 address                           |
    | ipv6_cache            | Available ipv6 address                           |
    | mac_cache             | Available mac address                            |
    +==========================================================================+
    | Methods               | Description                                      |
    |-----------------------+--------------------------------------------------|
    | add_device            | Adds a device (Device object) to this testbed.   |
    | remove_device         | Removes a device (Device object) from this       |
    |                       | testbed.                                         |
    | find_devices          | Returns device objects of this testbed with      |
    |                       | specific requirements.                           |
    | find_links            | Return links objects of this testbed with        |
    |                       | specific requirements.                           |
    | find_interface        | Returns interface objects of this testbed with   |
    |                       | requirements. It appends all the interfaces into |
    |                       | the same list.                                   |
    | find_features         | Returns features objects of this testbed with    |
    |                       | specific requirements. It appends all the        |
    |                       | features into the same list.                     |
    | build_config          | Builds and configures the whole testbed. Loops   |
    |                       | through each device, features, and link to       |
    |                       | configure it.                                    |
    | build_unconfig        | Builds and unconfigures the whole testbed.       |
    |                       | Loops through each device, features and list to  |
    |                       | configure it.                                    |
    | object_instances      | Returns a frozenset of all the instances of a    |
    |                       | particular type.           					             |
    | set_active_objects    | Froms a list of interfaces, set attributes       |
    |                       | `obj_state` of all devices, interfaces and       |
    |                       | and link as `active` and `inactive`.             |
    | squeeze               | Removes all unwanted devices, interfaces         |
    |                       | and links from this testbed.                     |
    +==========================================================================+


.. code-block:: python

   # import modules
   from genie.conf.base import Testbed, Device, Interface, Link
   from pyats.datastructures.logic import And, Not, Or

   # Create a Testbed
   testbed = Testbed(name='myTestbed')

   # Create two devices
   # Adding testbed=testbed automatically bind the devices to the testbed.
   dev1 = Device(name='PE1', testbed=testbed, aliases=['uut'], os='iosxe')
   dev2 = Device(name='P1', testbed=testbed, aliases=['helper'], os='iosxe')

   # Let's add an interface for each device
   # Adding device=<dev object> automatically bind the interface to a device
   intf_dev1 = Interface(name='Ethernet3/7', device=dev1, aliases=['PE1'])
   intf_dev2 = Interface(name='Ethernet3/7', device=dev2, aliases=['P1'])

   # Now some link to connect those 2 interfaces
   # A link must be part of a testbed
   link1 = Link(name='dev1-dev2-1', testbed=testbed, aliases=['used link'])
   link1.connect_interface(intf_dev1)
   link1.connect_interface(intf_dev2)

   # Un used link - No interface connected to this link
   link2 = Link(name='dev1-dev2-1', testbed=testbed, aliases=['unused link'])

   # For more information on find Apis, please visit the
   # Find Mechanism section, but here are some examples.
   >>> testbed.find_devices()
   [<Device object 'P1' at 0xf720de2c>,
    <Device object 'PE1' at 0xf720dacc>]
   >>> testbed.find_devices(name='P1')
   [<Device object 'P1' at 0xf720de2c>]

   # Now set all the interfaces on dev1 to be active, and the rest will
   # become inactive.
   >>> testbed.set_active_interfaces(dev1.interfaces)
   >>> testbed.find_interfaces(obj_state='active')
   [<EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6df160c>]
   # It also applies on devices
   >>> testbed.find_devices(obj_state='active')
   [<Device object 'PE1' at 0xf6f62b6c>]

   # And we can see the inactive devices
   >>> testbed.find_devices(obj_state='inactive')
   [<Device object 'P1' at 0xf6f072ac>]

   # Find are useful to find a particular type of object and filter
   # based on requirements.
   # 
   # API object_instances look through all the objects that have been
   # created and verified the type of them. If it matches,
   # it will be returned as a frozenset. By default, it will match all objects
   >>> testbed.object_instances()
   frozenset({<Link object 'dev1-dev2-1' at 0xf6df8d2c>,
              <Link object 'dev1-dev2-1' at 0xf6dfd7ac>,
              <Device object 'P1' at 0xf6f0e18c>,
              <EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6df85cc>,
              <EthernetInterface object 'Ethernet3/7' on 'P1' at 0xf6dfd60c>,
              <Device object 'PE1' at 0xf6f69bac>})
   >>> testbed.object_instances(cls=Interface)
   frozenset({<EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6df85cc>,
              <EthernetInterface object 'Ethernet3/7' on 'P1' at 0xf6dfd60c>})
   >>> testbed.object_instances(cls=Device)
   frozenset({<Device object 'P1' at 0xf6f0e18c>,
              <Device object 'PE1' at 0xf6f69bac>})

   # Let's find all of the interface which have status inactive
   testbed.find_interfaces(obj_state='inactive')
   [<EthernetInterface object 'Ethernet3/7' on 'P1' at 0xf6df664c>]
   >>> testbed.find_devices(obj_state='inactive')
   [<Device object 'P1' at 0xf6f072ac>]

   # Remove dev1 of the testbed
   >>> testbed.remove_device(dev1)
   >>> testbed.find_devices()
   [<Device object 'P1' at 0xf6f0e18c>]

   # Add it back
   >>> testbed.add_device(dev1)
   >>> testbed.find_devices()
   [<Device object 'P1' at 0xf6f0e18c>,
    <Device object 'PE1' at 0xf6f69bac>]

.. note::

    Testbed object inherits from :testbed:`pyats testbed <http>` hence having all its features and functionalities.


   # Use the squeeze functionality
   # extend_devices_from_links=True
   >>> testbed.squeeze('d1', 'l23', extend_devices_from_links=True)
   >>> [dev for dev in testbed.devices]
   ['d3', 'd2', 'd1']
   >>> [link.name for link in testbed.links]
   ['l23']
   # extend_devices_from_links=False
   >>> testbed.squeeze('d1', 'l23', extend_devices_from_links=False)
   >>> [dev for dev in testbed.devices]
   ['d1']
   >>> [link.name for link in testbed.links]
   []

.. _device:

Device Object
-------------

The `Device` object represents a physical or a virtual router, switch, traffic
generator, and so on.

For more information on the `find_<...>` APIs, users may consult the 
:ref:`find mechanism <find>`.

.. code-block:: text

    +--------------------------------------------------------------------------+
    | Device object                                                            |
    +==========================================================================+
    | Attributes       | Description                                           |
    |------------------+-------------------------------------------------------|
    | name             | Device name, should be unique                         |
    | aliases          | List of aliases for the device. Useful for            |
    |                  | recognizing specific devices                          |
    | roles            | List of devices' roles                                |
    | type             | Device type                                           |
    | interfaces       | Dict of interfaces                                    |
    | features         | List of features to configure on the device           |
    | obj_state        | State of the object device. Must be set manually.     |
    | testbed          | Parent testbed object. Internally it is a weakref     |
    | os               | Keeps track of the OS of the device                   |
    | mapping          | Keeps track of which connection to use for            |
    |                  | different abstraction tokens.                         |
    +==========================================================================+
    | Methods          | Description                                           |
    |------------------+-------------------------------------------------------|
    | add_interface    | Adds an interface (Interface object) to this device   |
    | remove_interface | Removes an interface (Interface object) from this     |
    |                  | device                                                |
    | parse            | Parses a command into structured format using Genie   |
    |                  | parsers
    | add_feature      | Adds a feature (Feature object) to this device        |
    | remove_feature   | Removes a feature (Feature object) from this device   |
    | find_interfaces  | Returns interfaces (Interface object) of this device  |
    |                  | with specific requirements                            |
    | find_features    | Returns features objects of this testbed with         |
    |                  | specific requirements.                                |
    | build_config     | Builds and configures the whole testbed. Loops through|
    |                  | each device, features, and link to configure it.      |
    | build_unconfig   | Builds and unconfigures the whole testbed. Loops      |
    |                  |through each device, features and link to configure it.|
    +==========================================================================+


.. code-block:: python

   # import modules
   from genie.conf.base import Testbed, Device, Interface, Link

   # Create a Testbed
   testbed = Testbed(name='myTestbed')

   # Create two devices
   # Adding testbed=testbed automatically bind the devices to the testbed.
   dev1 = Device(name='PE1', testbed=testbed, aliases=['uut'], os='nxos')
   dev2 = Device(name='P1', testbed=testbed, aliases=['helper'], os='nxos')

   # Let's add a few interfaces to each device
   # Adding device=<dev object> automatically bind the interface to a device
   intf1_dev1 = Interface(name='Ethernet3/7', device=dev1, aliases=['PE1_1'])
   intf2_dev1 = Interface(name='Ethernet3/8', device=dev1, aliases=['PE1_2'])
   intf1_dev2 = Interface(name='Ethernet3/7', device=dev2, aliases=['P1'])
   intf2_dev2 = Interface(name='Ethernet3/8', device=dev2, aliases=['P1'])

   # Using find_interfaces
   # No requirements, so all are returned
   >>> dev1.find_interfaces()
   [<EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6e7522c>,
    <EthernetInterface object 'Ethernet3/8' on 'PE1' at 0xf6e1b98c>]

   # All the find commands previously shown can also be done for this object

   # Remove an interface
   >>> dev1.remove_interface(intf1_dev1)

   # Make sure it is gone
   >>> dev1.find_interfaces()
   [<EthernetInterface object 'Ethernet3/8' on 'PE1' at 0xf6e1b98c>]

   # Let's add it back
   >>> dev1.add_interface(intf1_dev1)
   >>> dev1.find_interfaces()
   [<EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6e7522c>,
    <EthernetInterface object 'Ethernet3/8' on 'PE1' at 0xf6e1b98c>]

   # let's do a parse
   >>> device.parse('show interfaces')

.. note::

    Device object inherits from :pyats_device:`pyats device <http>` hence having all its features and functionalities.


.. _interface:

Interface Object
----------------

The `Interface` object represents a physical or virtual device interface.
An `Interface` can have many subclasses, one for each particular type of
`Interface`. This is necessary, as each `Interface` may have a different
configuration and as such, different attributes may be necessary.

The infrastructure base classes include `Interface`, which is the base class
for all current and future `Interface` implementations.

`Interface` plays two roles in ``Genie``. The first role is as an object part of
the topology. This is what this section describes. Secondly, `Interface` plays
the role of configurable object base class. All interface configurable objects are
inherited from this class. These configurable objects are stored into
`genie_libs` git repository inside the `interface` directory. With the help of
`__new__` method inside the base class, users can locate the right interface.

The infrastructure provides `PhysicalInterface`, `VirtualInterface`,
`PseudoInterface`, `LoopbackInterface`, which users may use to as a baseclass to construct 
their own configurable interface in `genie_libs`.

Refer to the :ref:`find mechanism <find>` documentation for more
information on the `find_<...>` APIs..

.. code-block:: text

    +--------------------------------------------------------------------------+
    | Interface object                                                         |
    +==========================================================================+
    | Attributes               | Description                                   |
    |--------------------------+-----------------------------------------------|
    | name                     | Interface name, should be unique              |
    | alias                    | Interface alias, default to interface name    |
    | aliases                  | List of aliases for the interface. Useful for |
    |                          | recognizing interfaces                        |
    | links                    | List of link that this interface is part      |
    | obj_state                | State of the object interface. Must be        |
    |                          | set manually.                                 |
    | device                   | Weakref to device object containing the       |
    |                          | interface                                     |
    | features                 | List of features to configure on the device   |
    +==========================================================================+
    | Methods                  | Description                                   |
    |--------------------------+-----------------------------------------------|
    | _on_added_from_device    | Action to be taken when adding an interface   |
    |                          | to a device.                                  |
    | _on_removed_from_device  | Action to be taken when removing an interface |
    |                          | from a device.                                |
    | _on_added_from_link      | Action to be taken when adding an interface   |
    |                          | to a link.                                    |
    | _on_removed_from_link    | Action to be taken when removing an interface |
    |                          | from a link.                                  |
    | find_links               | Returns links objects of this testbed         |
    |                          | with specific requirements.                   |
    | find_features            | Returns features objects of this testbed with |
    |                          | specific requirements.                        |
    | build_config             | Builds and configures the interface based on  |
    |                          | attributes set on this interface object.      |
    | build_unconfig           | Builds and unconfigures the interface based on|
    |                          | attributes set on this interface object.      |
    | build_modify             | Only modifies a section of the configuration  |
    |                          | based on the kwargs passed to the function.   |
    | add_feature              | Adds a feature (Feature object) to            |
    |                          | this interface.                               |
    | remove_feature           | Removes a feature (Feature object) from       |
    |                          | this interface.                               |
    +==========================================================================+


.. code-block:: python

   # import modules
   from genie.conf.base import Testbed, Device, Interface, Link

   # Create a Testbed
   testbed = Testbed(name='myTestbed')

   # Create two devices
   # Adding testbed=testbed automatically bind the devices to the testbed.
   dev1 = Device(name='PE1', testbed=testbed, aliases=['uut'], os='nxos')
   dev2 = Device(name='P1', testbed=testbed, aliases=['helper'], os='nxos')

   # Let's add a few interfaces to each device
   # Adding device=<dev object> automatically bind the interface to a device
   # __new__ returns the right type depending on the name
   intf1_dev1 = Interface(name='Ethernet3/7', device=dev1, aliases=['PE1_1'])
   intf2_dev1 = Interface(name='loopback1', device=dev1, aliases=['PE1_2'])
   intf2_dev2 = Interface(name='vlan1', device=dev2, aliases=['P1'])

   >>> intf1_dev1
   <EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6e3f22c>
   >>> intf2_dev1
   <LoopbackInterface object 'loopback1' on 'PE1' at 0xf6de526c>
   >>> intf2_dev2
   <VlanInterface object 'vlan1' on 'P1' at 0xf6de5f8c>

.. note::

    An interface of the correct type for the right os must exist in
    genie_libs/conf/interface, otherwise `BaseInterface` will be
    returned.

.. note::

    Interface object inherits from :pyats_interface:`pyats interface <http>` hence having all its features and functionalities.


.. _link:

Link Object
-----------

The `Link` object is a connection between two or more `Interface` within
a `Testbed`. More than two `Interface` can be interconnected using a L2 switches.

.. code-block:: text

    +--------------------------------------------------------------------------+
    | Link object                                                              |
    +==========================================================================+
    | Attributes               | Description                                   |
    |--------------------------+-----------------------------------------------|
    | name                     | Links name, should be unique                  |
    | aliases                  | Lists of aliases for the link. Useful for     |
    |                          | recognizing links.                            |
    | features                 | Lists features to configure on the devices.   |
    | obj_state                | States of the object link. Must be            |
    |                          | set manually.                                 |
    | interfaces               | Weaklist of interfaces that are a part of     |
    |                          | this link.                                    |
    | testbed                  | Parent testbed object. Internally it          |
    |                          | is a weakref.                                 |
    | devices                  | Tuple of devices. Taken from the interfaces   |
    |                          | in the link                                   |
    +==========================================================================+
    | Methods                  | Description                                   |
    |--------------------------+-----------------------------------------------|
    | connect_interface        | Connects an interface to this link            |
    | disconnect_interface     | Disconnects an interface to this link         |
    | find_interfaces          | Returns interfaces (Interface object) of      |
    |                          | this link with specific requirements          |
    | find_features            | Returns features objects of this link with    |
    |                          | specific requirements.                        |
    | add_feature              | Adds a feature (Feature object) to            |
    |                          | this link.                                    |
    | remove_feature           | Removes a feature (Feature object) from       |
    |                          | this link.                                    |
    +==========================================================================+


.. code-block:: python

   # import modules
   >>> from genie.conf.base import Testbed, Device, Interface, Link

   # Create a Testbed
   >>> testbed = Testbed(name='myTestbed')

   # Create two devices
   # Adding testbed=testbed automatically bind the devices to the testbed.
   >>> dev1 = Device(name='PE1', testbed=testbed, aliases=['uut'], os='nxos')
   >>> dev2 = Device(name='P1', testbed=testbed, aliases=['helper'], os='nxos')

   # Let's add an interface for each device
   # Adding device=<dev object> automatically bind the interface to a device
   >>> intf_dev1 = Interface(name='Ethernet3/7', device=dev1, aliases=['PE1'])
   >>> intf_dev2 = Interface(name='Ethernet3/7', device=dev2, aliases=['P1'])

   # Now some link to connect those 2 interfaces
   # A link must be part of a testbed
   >>> link1 = Link(name='dev1-dev2-1', testbed=testbed, aliases=['used link'])
   >>> link1.connect_interface(intf_dev1)
   >>> link1.connect_interface(intf_dev2)

   # Check all interfaces under link
   >>> link1.find_interfaces()
   [<EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6f0c22c>,
    <EthernetInterface object 'Ethernet3/7' on 'P1' at 0xf6eb226c>]

   # Find an interface that has name Ethernet3/7, and is part of device PE1
   >>> link1.find_interfaces(name='Ethernet3/7', device__name='PE1')
   [<EthernetInterface object 'Ethernet3/7' on 'PE1' at 0xf6ed322c>]

   # Let's remove this interface
   >>> link1.disconnect_interface(link1.find_interfaces(name='Ethernet3/7',
                                                    device__name='PE1',
                                                    count=1)[0])

   # Check after disconnect
   >>> link1.find_interfaces()
   [<EthernetInterface object 'Ethernet3/7' on 'P1' at 0xf6eb226c>]

   # To add a feature, add_feature(<feature object>) would do it.

.. note::

    Link object inherits from :pyats_link:`pyats link <http>` hence having all its features and functionalities.


.. _find:

Find Api
--------

All of ``Genie``'s base classes include `find` mechanisms, which means users may lookup
particular objects that meet their specific requirements. This is a very powerful mechanism
for all users.

The ``Genie`` `find` method is a wrapper on top of :pyats_find:`pyats find <http>`, with extended
functionality. Please refer to the ``pyats`` documentation for a better understanding of  :pyats_find:`pyats find <http>` APIs.

Let's use the following topology as our playground to understand how the ``Genie`` `find`
method works.

.. figure:: find_topology.png
    :align: center
    :alt: find_topology

The following topology has three `Device`s, which have four `Interface`s each, and four
`Link`s interconnecting each `device`. Of course, this is all within a `Testbed`.
Let's represent it using ``Genie`` objects.

.. code-block:: python

    from genie.conf.base import Testbed, Device, BaseInterface, Link
    testbed = Testbed()

    dev1 = Device(name='PE1', testbed=testbed, aliases=['uut'], os='nxos')
    dev2 = Device(name='PE2', testbed=testbed, aliases=['helper'], os='nxos')
    dev3 = Device(name='P1', testbed=testbed, aliases=['P'], os='nxos')

    intf1_dev1 = BaseInterface(name='Ethernet1/1', device=dev1)
    intf2_dev1 = BaseInterface(name='Ethernet1/2', device=dev1)
    intf3_dev1 = BaseInterface(name='Ethernet2/1', device=dev1)
    intf4_dev1 = BaseInterface(name='Ethernet2/2', device=dev1)

    intf1_dev2 = BaseInterface(name='Ethernet3/1', device=dev2)
    intf2_dev2 = BaseInterface(name='Ethernet3/2', device=dev2)
    intf3_dev2 = BaseInterface(name='Ethernet3/6', device=dev2)
    intf4_dev2 = BaseInterface(name='Ethernet3/7', device=dev2)

    intf1_dev3 = BaseInterface(name='Ethernet1/1', device=dev3)
    intf2_dev3 = BaseInterface(name='Ethernet1/5', device=dev3)
    intf3_dev3 = BaseInterface(name='Ethernet2/1', device=dev3)
    intf4_dev3 = BaseInterface(name='Ethernet2/2', device=dev3)

    link1 = Link(name='PE1-P1-1', testbed=testbed)
    link1.connect_interface(intf1_dev1)
    link1.connect_interface(intf1_dev3)

    link2 = Link(name='PE1-P1-2', testbed=testbed)
    link2.connect_interface(intf2_dev1)
    link2.connect_interface(intf2_dev3)

    link3 = Link(name='PE1-PE2-1', testbed=testbed)
    link3.connect_interface(intf3_dev1)
    link3.connect_interface(intf1_dev2)

    link4 = Link(name='PE1-PE2-2', testbed=testbed)
    link4.connect_interface(intf4_dev1)
    link4.connect_interface(intf2_dev2)

    link5 = Link(name='P1-PE2-1', testbed=testbed)
    link5.connect_interface(intf3_dev2)
    link5.connect_interface(intf3_dev3)

    link6 = Link(name='P1-PE2-2', testbed=testbed)
    link6.connect_interface(intf4_dev2)
    link6.connect_interface(intf4_dev3)

Now, let's use this topology to demonstrate how `find_...` method works.

.. code-block:: python

    # Testbed object containing this topology.
    >>> testbed
    <Testbed object None at 0xf764f0cc>

    # Let's find all the link on this testbed
    # 6 links as expected
    >>> testbed.find_links()
    [<Link object 'P1-PE2-2' at 0xf6df31ec>,
     <Link object 'P1-PE2-1' at 0xf6df318c>,
     <Link object 'PE1-PE2-1' at 0xf6df30cc>,
     <Link object 'PE1-P1-2' at 0xf6df302c>,
     <Link object 'PE1-PE2-2' at 0xf6df312c>,
     <Link object 'PE1-P1-1' at 0xf6df266c>]

    # And let's get the name of those links, just to verify
    >>> for link in testbed.find_links(): print(link.name)
    PE1-PE2-2
    PE1-P1-1
    P1-PE2-1
    P1-PE2-2
    PE1-P1-2
    PE1-PE2-1

    # All find can return a specific number of items via count
    >>> testbed.find_links(count=3)
    [<Link object 'P1-PE2-2' at 0xf6df31ec>,
     <Link object 'P1-PE2-1' at 0xf6df318c>,
     <Link object 'PE1-PE2-1' at 0xf6df30cc>]

    # I would not even try
    >>> testbed.find_links(count=-1)
    TypeError: count can only a positive number. -1 is not positive.

All of the previous examples are supported by all `find_` methods:  `find_links`,
`find_devices` and  `find_interfaces`. 

The next set of examples demonstrate how users may 
filter lists or dictionaries of objects contained inside the object which
owned the method.  For example, `find_devices` is owned by `Testbed`, and it
allows to filter the list or dictionary of `Device`.

.. code-block:: python

    # Requires the devices that has name 'PE1'
    >>> testbed.find_devices(name='PE1')
    [<Device object 'PE1' at 0xf6ee9aac>]

    # Requires a device name that does not exists
    >>> testbed.find_devices(name='NotReal')
    []

    # It also support pyATS logic
    from pyats.datastructures.logic import And, Not, Or

    >>> testbed.find_devices(name=Or('PE1', 'P1'))
    [<Device object 'PE1' at 0xf6ee9aac>,
     <Device object 'P1' at 0xf6e8e64c>]

    >>> testbed.find_devices(name=Not('PE1'))
    [<Device object 'PE2' at 0xf6e8e28c>,
     <Device object 'P1' at 0xf6e8e64c>]

    # You can ask for many requirements. It can be read like this
    # Find all the devices that have a name that is not PE1 and
    # their alias is helper
    >>> testbed.find_devices(name=Not('PE1'), aliases=['helper'])
    [<Device object 'PE2' at 0xf6e8e28c>]

    >>> testbed.find_devices(name=Not('PE1'), aliases=['uut'])
    []

We can see it loop through each device part of this testbed, verify if
there is an attribute `name` and make sure it equals the right value, or the
callable is `True`. Of course many attributes can be requested, and all those
have to be `True` or equal to the right values.

We will see more advanced requirements in the examples below: 

.. code-block:: python

    # Let's see an example, where we will chain the request.
    # We want to find all links that have an interface belonging to device PE1

    # This requirement cannot be figured out by just checking the link itself,
    # but needs to verify link.interfaces[x].device.name , where x loops through
    # all interfaces. However, you cannot pass this as a keyword
    # argument. So a new syntax was born.

    # interfaces[x].device.name = interfaces__device__name
    # This syntax is smart enough to recognize list, if it is
    # then it will loop through each element.

    # Return all the link that has at least an interface
    # that is part of device PE1
    >>> testbed.find_links(interfaces__device__name='PE1')
    [<Link object 'PE1-PE2-2' at 0xf6df312c>,
     <Link object 'PE1-P1-2' at 0xf6df302c>,
     <Link object 'PE1-P1-1' at 0xf6df266c>,
     <Link object 'PE1-PE2-1' at 0xf6df30cc>]

    # As another example;
    # Let's find all the device that have an interface part of PE1-P1-1
    >>> testbed.find_devices()
    [<Device object 'PE1' at 0xf6ee9aac>,
     <Device object 'PE2' at 0xf6e8e28c>,
     <Device object 'P1' at 0xf6e8e64c>]

This new syntax can be chained and it can retrieve any arguments.

Lastly, let's explore the `R` class which stands for `Requirement`. `R` allows
a user to create many requirements, where each requirement must be true for an
object be a part of the return list. For example, let's say the user wants to
find a link that is a part of `Device` PE1 and `Device` P1. This requirement
cannot be done using the current syntax, but requires to mention; I need a
`Link` that has `device.name = Pe1` and `device.name = P1`, which are two
requirements, in order to 
achieve this result.

Now let's see `R` in action:

.. code-block:: python

    # Let's find all the links that are part of PE1 and P1
    from pyats.utils.objects import R

    # The first R will get all the links that contains PE1
    # The second R will get all the links that contains P1
    # And then lastly only the intersection of both list will be returned
    >>> testbed.find_links(R(interfaces__device__name='PE1'),
                           R(interfaces__device__name='P1'))
    [<Link object 'PE1-P1-2' at 0xf6df302c>,
     <Link object 'PE1-P1-1' at 0xf6df266c>]

    # In case you are wondering, those will not work
    # This will raise an exception; a function cannot be called
    # with the same arguments.
    >>> testbed.find_links(interfaces__device__name='PE1',
                           interfaces__device__name='P1')
    SyntaxError: keyword argument repeated


    # This will return the links that have an interface that are part of PE1
    # OR part of P1, but not an intersection
    >>> testbed.find_links(interfaces__device__name=Or('PE1', 'P1'))
    [<Link object 'P1-PE2-2' at 0xf6df31ec>,
     <Link object 'P1-PE2-1' at 0xf6df318c>,
     <Link object 'PE1-PE2-1' at 0xf6df30cc>,
     <Link object 'PE1-P1-2' at 0xf6df302c>,
     <Link object 'PE1-PE2-2' at 0xf6df312c>,
     <Link object 'PE1-P1-1' at 0xf6df266c>]

    # This will return the links that have an interface that are part of
    # PE1 and P1,  which is none.
    >>> testbed.find_links(interfaces__device__name=And('PE1', 'P1'))
    []


