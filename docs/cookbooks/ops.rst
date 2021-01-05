.. _book_ops:

.. raw:: html

   <h2>Genie Operational Recipes</h2>


.. note::

    This section assumes pyATS and Genie are :ref:`installed and ready to be
    used<book_genie>`.

.. note::

    It also assumes you have a :ref:`testbed file ready<book_setup_testbed>` to
    be used with a device.

.. _book_ops_summary:

1. Summary
----------

.. note::

    This section gives a summary of what is an Ops object. Dig into the documentation for more information.

Genie Ops learns everything that can be learn about a feature operational
state, and pack it into 1 structured object. This structure is common for all
OS.

Here are some use cases where these objects are useful:

1) Learn all interfaces on a device and their operation state
2) Learn any protocol state - Bgp, Ospf, Acl, Dot1x, lldp, ...
3) Device state - Platforms, linecards, ...

The technology has also been used for a non-networking purpose such as:

4) Learn website information to work with Selenium

All supported feature can be seen on our :models:`models page<http>`. Each
object follows a structure which can also be seen on the same page. Take a look
at the model page for the `ops` structure.

Here are some use cases where these objects can be used:

1) Learn a feature and retrieve some values out of the structure.
    a) Learn Interface object and check if a particular interface is up
    b) Learn Bgp object and check if the bgp has some peer policies

2) Learn a feature and use the :ref:`Find<book_ops_find>` object to navigate it
    a) Learn Ospf object and check which instances have nsr activated
    b) Learn Ospf object and check which instances have nsr activated
       and is connected with a particular interface.

3) Take a snapshot of the object and compare it at a later time
    a) Take a snapshot of the Interface object. Do some modifications to some
       interface. Retake a snapshot and compare that the changes are as expected.
    b) Same idea as above, but make sure nothing has been modified.

4) Take a snapshot and save it to a file. On another day, take the same
   snapshot and compare with the previous day snapshot. This provides assurance
   that your network has not changed over time.


2. Retrieve a snapshot of the Operation state of your device
------------------------------------------------------------

Learning a device feature is now easier than ever. ``Ops`` object learns
everything to know about the operation state of a device feature such as ospf,
interface, etc.

This sends multiple commands on the device and creates a structure for all the
information.

.. code-block:: python

    # The OS choices are - nxos; iosxr; iosxe - For this example, we will be
    # using nxos
    from genie import testbed
    from genie.libs.ops.interface.nxos.interface import Interface

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)

    # Find the uut device. Either the alias or the hostname of the device can 
    # be provided
    uut = testbed.devices['uut']
    uut.connect()

    # Instantiate the OPS object
    interface = Interface(device=uut)

    # This will send many show command to learn the operational state
    # of interfaces for this device
    interface.learn()

    import pprint
    pprint.pprint(interface.info)

    # The object is too big to print, here a snippet
    # {'Ethernet2/1': {'auto_negotiate': False,
    #                  'bandwidth': 1000000,
    #                  'counters': {'in_broadcast_pkts': 0,
    #                               'in_crc_errors': 0,
    #                               'in_errors': 0,
    #                               'in_mac_pause_frames': 0,
    #                               'in_multicast_pkts': 0,
    #                               'in_octets': 0,
    #                               'in_pkts': 0,
    #                               'in_unicast_pkts': 0,
    #                               'in_unknown_protos': 0,
    #                               'last_clear': 'never',
    #                               'out_broadcast_pkts': 0,
    #                               'out_discard': 0,
    #                               'out_errors': 0,
    #                               'out_mac_pause_frames': 0,
    #                               'out_multicast_pkts': 0,
    #                               'out_octets': 0,
    #                               'out_pkts': 0,
    #                               'out_unicast_pkts': 0,
    #                               'rate': {'in_rate': 0,
    #                                        'in_rate_pkts': 0,
    #                                        'load_interval': 0,
    #                                        'out_rate': 0,
    #                                        'out_rate_pkts': 0}},
    #                  'delay': 10,
    #                  'duplex_mode': 'full',
    #                  'enabled': True,
    #                  'encapsulation': {'encapsulation': 'arpa'},
    #                  'flow_control': {'receive': False, 'send': False},
    #                  'ipv4': {'10.0.1.2/24': {'ip': '10.0.1.2',
    #                                           'prefix_length': '24'}},
    #                  'mac_address': '0000.0000.002f',
    #                  'medium': 'broadcast',
    #                  'mtu': 1500,
    #                  'oper_status': 'up',
    #                  'phys_address': 'fa16.3eb3.07f1',
    #                  'port_channel': {'port_channel_member': False},
    #                  'port_speed': '1000',
    #                  'type': 'Ethernet',
    #                 'vrf': 'default'}, 
    # ...

All supported feature can be seen on our :models:`models page<http>`.

.. raw:: html

    <script src="https://asciinema.org/a/FXMwC7w5SswKCYt5AOZODXOGN.js" id="asciicast-FXMwC7w5SswKCYt5AOZODXOGN" async></script>

.. note::

    More information can be found on the :ref:`Ops page<ops_user_guide>`.

.. tip::

	use ``device.learn('all')`` to learn all the supported features on the device, and the result will be returned in a dictionary
	format like: ``{'interface' : <Interface object at 0x7fcec85d8160>}``. If an exception occurred while learning a particular feature, then ``featureObject`` will become the exception object.


3. Get partial state of a feature - command based
-------------------------------------------------

The above recipe learns everything about this feature by sending many commands
the device. To reduce execution time, we can dictate to only learn from
specific commands.

.. code-block:: python

    # The OS choices are - nxos; iosxr; iosxe - For this example we will be
    # using nxos
    from genie import testbed
    from genie.libs.ops.interface.nxos.interface import Interface
    from genie.libs.parser.nxos.show_interface import ShowVrfAllInterface

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.connect()

    # Learn interface based only on 1 command
    interface = Interface(device=uut, commands=[ShowVrfAllInterface])

    interface.learn()

    import pprint
    pprint.pprint(interface.info)

    # {'Ethernet2/1': {'vrf': 'default'},
    # ...

To know which command is used for this `Ops` object, the code is needed to be
checked. All code is hosted in :genielibs_repo:`git <http>` in directories
pkgs/ops-pkg/src/genie/libs/ops.

.. raw:: html

    <script src="https://asciinema.org/a/qaGvB8rt1wSmNksYf8L1jiv4S.js" id="asciicast-qaGvB8rt1wSmNksYf8L1jiv4S" async></script>



4. Get partial state of a feature - Attribute based
----------------------------------------------------

Another way to save execution time is by providing the variables that you care
about. Only the commands related to these keys will be sent and learnt.

In this recipe, we only care about the variable `duplex_mode`.

.. code-block:: python

    # The OS choices are - nxos; iosxr; iosxe - For this example, we will be
    # using nxos
    from genie import testbed
    from genie.libs.ops.interface.nxos.interface import Interface

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.connect()

    # Learn all interface which has duplex mode as a key
    interface = Interface(device=uut, attributes=['info[(.*)][duplex_mode]'])

    interface.learn()

    import pprint
    pprint.pprint(interface.info)

    # {'Ethernet2/1': {'duplex_mode': 'full'},
    # 'Ethernet2/2': {'duplex_mode': 'full'},
    #  'mgmt0': {'duplex_mode': 'full'}}

In this case, only 2 commands out of 7 were sent to the device. This can be
massive time saver.

All supported feature and their variable structure can be seen on our
:models:`models page<http>`. All of them are to be used in the same way.

.. raw:: html

    <script src="https://asciinema.org/a/laX0ltkJTrVsNVnfs5wteQk8a.js" id="asciicast-laX0ltkJTrVsNVnfs5wteQk8a" async></script>

.. note::

    More information can be found on the :ref:`Ops page - Extra features<user_ops_extra_attributes>`.


5. Use ``Ops`` object to verify state is as expected.
-----------------------------------------------------

A great feature of Ops is the built-in verify mode. Learn a feature and verify
if it's as expected. If it is not then sleep for sometime and try again. This
is very useful after doing some actions on the device and expecting the device
to take some time to stabilize.

.. code-block:: python

    # The OS choices are - nxos; iosxr; iosxe - For this example, we will be
    # using nxos
    from genie import testbed
    from genie.libs.ops.interface.nxos.interface import Interface

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.connect()

    def verify_interface_status(obj):
        # Interface object that was learnt
        # Let's verify that at least one interface is up
        for intf in obj.info:
            if obj.info[intf].get('oper_status', None) and\
               obj.info[intf]['oper_status'] == 'up':
                return
        # If no interface was found to have an up oper_status, then
        # raise an exception
        raise Exception("Could not find any up interface")

    # Learn all interface which has duplex mode as a key
    interface = Interface(device=uut)

    # Try to verify up to 6 times that at least one interface is up
    # with sleep of 5 seconds between each attempt
    interface.learn_poll(verify=verify_interface_status, sleep=5, attempt=6)

.. note::

    More information can be found on the :ref:`Ops page - Polling<user_ops_polling>`.


.. _book_ops_diff:

6. Compare two feature snapshots - Diff two `ops` object.
---------------------------------------------------------

Want to know if the state of your network has changed over time? Take snapshots
at a different time, and compare them!

.. code-block:: python

    # The OS choices are - nxos; iosxr; iosxe - For this example, we will be
    # using nxos
    from genie import testbed
    from genie.libs.ops.interface.nxos.interface import Interface

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.connect()

    # Learn all interface
    interface = Interface(device=uut)

    interface.learn()

    # Let's modify one of the interface, so we can demonstrate the comparison
    # Find an up interface
    for intf in interface.info:
        if interface.info[intf].get('oper_status', None) and\
           interface.info[intf]['oper_status'] == 'up':
           up_interface = intf
           break
    else:
        # No up interface
        raise Exception("Could not find any up interface")

    uut.configure('''\\\
    interface {intf}
     shut'''.format(intf=up_interface))

    # let's take a new snapshot now and compare
    interface_after = Interface(device=uut)

    interface_after.learn()

    import pprint
    pprint.pprint(interface.info)
    diff = interface_after.diff(interface)
    print(diff)

    # info:
    #  loopback1:
    # +  enabled: False
    # -  enabled: True
    # +  oper_status: down
    # -  oper_status: up

    uut.configure('''\\\
    interface {intf}
     no shut'''.format(intf=up_interface))

.. raw:: html

    <script src="https://asciinema.org/a/fxXsA3uajzcH22ZYTFoXnM681.js" id="asciicast-fxXsA3uajzcH22ZYTFoXnM681" async></script>

This opens up the possibility of Testing and Assurance to the next level! 
This allows the script to check at any point if any part of the operational state
has changed.

.. note::

    More information can be found on the :ref:`Ops page - Diff<user_ops_extra_diff>`.

7. Save snapshot to file, and re-use them at a later time
---------------------------------------------------------

The previous recipe is perfect for within script comparison. This recipe allows
to save the object as a file, and compare it at a later date. Perfect for a weekly check of the operation state of your devices, 

.. code-block:: python

    # The OS choices are - nxos; iosxr; iosxe - For this example, we will be
    # using nxos
    from genie import testbed
    from genie.libs.ops.interface.nxos.interface import Interface

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.connect()

    # Learn all interface
    interface = Interface(device=uut)

    interface.learn()
    with open(file, 'wb') as f:
        f.write(interface.pickle(interface))


Then at a later time, you can do

.. code-block:: python

    from genie.ops.base import Base

    with open(file, 'rb') as f:
        interface = Base.unpickle(f.read())

Then once you get the object, you can do a normal comparison.

.. note::

    More information can be found on the :pickle:`official python<http>`
    documentation.

.. note::

    More information can be found on the :ref:`Ops page -
    Diff<user_ops_extra_diff>`.

8. Connection pool with ``Ops`` - Learn Faster!
-----------------------------------------------

Your time is valuable, hence Genie provides asynchronous execution methodology!
With the new connection pool mechanism, learning a feature can be done much
faster. Commands are sent in parallel to the device providing exceptional
performance.

.. code-block:: python

    # The OS choices are - nxos; iosxr; iosxe - For this example, we will be
    # using nxos
    from genie import testbed
    from genie.libs.ops.interface.nxos.interface import Interface

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']

    # With connection pool, its important to provide an alias. More information
    # on this in the note below.
    uut.start_pool(alias='a', size = 1)

    # Learn all interface
    interface = Interface(device=uut)

    interface.learn()

To fully utilize this functionality, a management port should be used which can
accept multiple connections.

.. code-block:: bash

    devices:
      nx-osv-1:
          alias: 'uut'
          type: 'Nexus'
          os: 'nxos'
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
              a:
                  protocol: telnet
                  ip: "172.25.192.90"
                  port: 17052
              vty:
                  protocol: telnet
                  ip: "10.1.1.2"

The `vty` connection has been added to connect to the management port of the
device.

.. code-block:: python

    # Same as earlier
    # ...
    uut.start_pool(alias='vty', size = 10)

    # Learn all interface
    interface = Interface(device=uut)

Connection pool increases the performance of `Ops` by using multiple
connections to the device.


.. note::

    More information can be found on the :connection-pool:`Connection
    pool<http>` documentation.

.. note::

    More information can be found on the :ref:`Ops page - Pool connection
    <user_ops_connection_pool>`.


9. One script across all platform! - `abstract package`
-------------------------------------------------------

In an earlier recipe, we've used this kind of import

.. code-block:: python

    from genie.libs.ops.interface.nxos.interface import Interface

Why not have one script which works across all devices? Not a dream anymore!
With `Genie.abstract` and `Genie.ops` you write it **once** for all platforms.

.. code-block:: python

    from genie import testbed
    # Import the main level of the library
    from genie.libs import ops
    # Import Abstract library
    from genie.abstract import Lookup

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.start_pool(alias='vty', size = 10)

    lookup = Lookup.from_device(uut)
    Interface = lookup.ops.interface.interface.Interface
    # Interface is now -> <class 'genie.libs.ops.interface.nxos.interface.Interface'>
    # More information on this below

    interface = Interface(uut)
    interface.learn()

Abstract will look for the device os and find the corresponding library. As Ops
structure are identical across all platforms, the same script can be used! 

Amazed enough?! Here is even better news!

For `ops` we can use the newly implemented `get_ops` API which returns the
abstracted ops class without even calling Lookup as above.

.. code-block:: python

    # import testbed and get_ops
    from genie import testbed
    from genie.ops.utils import get_ops

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.connect()

    # Get the Ops objecet
    Interface = get_ops('interface', uut)

    # Learn all interfaces
    interface.learn()

.. note:: 

    More :abstract_topology:`granular abstract <http>` can be provided if
    needed.

10. One script across all Interface management (Cli/Yang/Xml/...)
-----------------------------------------------------------------

Following the same design as the previous recipe, the same concept is applied
for different interface management.

.. code-block:: python

    from genie import testbed
    # Import the main level of the library
    from genie.libs import ops
    # Import Abstract library
    from genie.abstract import Lookup

    # Load Genie testbed which contains a Xml connection
    # With xml added in the abstraction section
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    # This is needed only when multiple interface management are used.
    uut.mapping['cli'] = 'vty'
    uut.mapping['xml'] = 'vty'
    uut.start_pool(alias='vty', size = 10)

    lookup = Lookup.from_device(uut)
    bgp = lookup.ops.bgp.bgp.Bgp
    # Bgp is now -> <class 'genie.libs.ops.bgp.nxos.xml.bgp.bgp'>

    bgp = Bgp(uut)
    Bgp.learn()


Example of Testbed file with Xml Support. Same idea for all the context
interface management.

.. code-block:: yaml

    devices:
      nx-osv-1:
          alias: 'uut'
          type: 'Nexus'
          os: 'nxos'
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
              context: 'xml'

This will send all the supported commands using XML, and the rest will be sent
using Cli and merged together.

.. _book_ops_find:

11. Navigate `Ops` object with your needs - The `Find` object
-------------------------------------------------------------

Tired of using many levels of `for loops` to navigate large structure? Us too!
Instead, let us know what you want, and we will find it.


.. code-block:: python

    from genie import testbed
    # Import the main level of the library
    from genie.libs import ops
    # Import Abstract library
    from genie.abstract import Lookup

    # Load Genie testbed
    testbed = testbed.load(testbed=<path of testbed file>)
    uut = testbed.devices['uut']
    uut.start_pool(alias='a', size = 10)

    lookup = Lookup.from_device(uut)
    Interface = lookup.ops.interface.interface.Interface
    # Interface is now -> <class 'genie.libs.ops.interface.nxos.interface.Interface'>
    # More information on this below

    interface = Interface(uut)
    interface.learn()

    # Let's get all the up interfaces
    from pyats.utils.objects import R, find
    req1 = R(['info', '(.*)', 'oper_status', 'up'])

    find(interface, req1, filter_=False)
    # [('up', ['info', 'loopback1', 'oper_status']),
    #  ('up', ['info', 'mgmt0', 'oper_status']),
    #  ('up', ['info', 'loopback0', 'oper_status']),
    #  ('up', ['info', 'Ethernet2/1', 'oper_status']),
    #  ('up', ['info', 'Ethernet2/2', 'oper_status'])]


Find has taken the requirement, which is based on the structure of the object,
and found what we were looking for; which were the interfaces name which were up.

.. code-block:: python

    req2 = R(['info', '(.*)', 'duplex_mode', 'full'])

    find(interface, req2, filter_=False)
    # [('full', ['info', 'Ethernet2/2', 'duplex_mode']),
    #  ('full', ['info', 'Ethernet2/1', 'duplex_mode']),
    #  ('full', ['info', 'mgmt0', 'duplex_mode'])]

We can take these two requirements, and merge their result together.

.. code-block:: python

    req3 = [R(['info', '(?P<interface>.*)', 'oper_status', 'up']),
            R(['info', '(?P<interface>.*)', 'duplex_mode', 'full'])]

    find(interface, *req3, filter_=False)
    # [('up', ['info', 'Ethernet2/2', 'oper_status']),
    #  ('up', ['info', 'Ethernet2/1', 'oper_status']),
    #  ('up', ['info', 'mgmt0', 'oper_status'])]

    # Do the same thing but see results from both requirements

    find(interface, *req3, filter_=False, all_keys=True)
    # [[('up', ['info', 'Ethernet2/2', 'oper_status']),
    #   ('up', ['info', 'Ethernet2/1', 'oper_status']),
    #   ('up', ['info', 'mgmt0', 'oper_status'])],
    # [('full', ['info', 'Ethernet2/2', 'duplex_mode']),
    # ('full', ['info', 'Ethernet2/1', 'duplex_mode']),
    # ('full', ['info', 'mgmt0', 'duplex_mode'])]]

Any amount of requirements can be provided; find will take care of merging
the results together. There can be as many regexes as needed, and 

.. note::

    We are using python Named groups :regex:`regex <http>` concept, to know which key to merge together. As many named groups can be provided. Right now we only have 1.

.. raw:: html

    <script src="https://asciinema.org/a/iOGqjMAIJHeCAGbwfhaUy5v2p.js" id="asciicast-iOGqjMAIJHeCAGbwfhaUy5v2p" async></script>

.. note::

    Find works for all Ops objects and all dictionaries.

12. Where are the object models located?
-----------------------------------------

All the objects models are displayed on our :models:`models page <http>`.

13. How to contribute
---------------------

To contribute to the code of Genie, take a look at our :commit:`commit <http>`
guideline! 

To contribute to the Ops object models, visit the :ops:`Ops contribution` page.


14. Get exclude keys for an ops object
---------------------------------------

.. code-block:: python

    from genie.ops.utils import get_ops_exclude
    get_ops_exclude('interface', dev)
    ['in_discards', 'in_octets', 'in_pkts', 'last_clear', 'out_octets', 'out_pkts', 'in_rate', 'out_rate', 'in_errors', 'in_crc_errors', 'in_rate_pkts', ...]
