.. _book_explore:

.. raw:: html

   <h2>Explore Genie</h2>


This page gives a quick overview on how Genie can help you!

To make these demos more interactive you can first :ref:`install Genie
<book_genie>` then you can execute each of the exploration recipe.

We are also including :ref:`workshops<book_explore_workshop>` which we are
currently presenting at CiscoLive part of DevNet Workshop. It is highly
recommended for you to spend some time and go through them.

.. note::

    Genie is flexible and can be used in multiple ways. Pure python, Robot
    libraries and directly in Linux without even knowing any Python.

.. note::

Examples can be cloned_ from: `https://github.com/CiscoTestAutomation/examples/tree/master/libraries`.


.. _Clone: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

    To execute them: cd $VIRTUAL_ENV/examples/


.. _book_explore_1:

1. Parse devices' outputs into structured output
------------------------------------------------

Parsers allows you to parse show commands into structured output
(Json/Dictionary).

**Python Example**

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    genie shell --testbed-file testbed.yaml --replay mocked_devices

.. raw:: html

    <i class="fa fa-anchor"></i>
    <span style='color:#6ab0de'>Python</span>

.. code-block:: python

    testbed.devices['nx-osv-1'].connect()
    output = testbed.devices['nx-osv-1'].parse('show version')
    output
    # {'platform': {'hardware': {'bootflash': '3184776 kB',
    #    'chassis': 'NX-OSv Supervisor Module',
    #    'device_name': 'nx-osv-1',
    #    'model': 'NX-OSv',
    #    'processor_board_id': 'TM00010000B',
    #    'slots': 'None'},
    #   'kernel_uptime': {'days': 6, 'hours': 1, 'minutes': 12, 'seconds': 30},
    #   'name': 'Nexus',
    #   'os': 'NX-OS',
    #   'software': {'kickstart_compile_time': '1/11/2016 16:00:00 [02/11/2016 10:30:12]',
    #    'kickstart_image_file': 'bootflash:///titanium-d1-kickstart.7.3.0.D1.1.bin',
    #    'kickstart_version': '7.3(0)D1(1)',
    #    'system_compile_time': '1/11/2016 16:00:00 [02/11/2016 13:08:11]',
    #    'system_image_file': 'bootflash:///titanium-d1.7.3.0.D1.1.bin',
    #    'system_version': '7.3(0)D1(1)'}}}

.. note::

    Run the genie shell command first, which gives a python interpreter

**Linux Example**

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    genie parse "show version" --testbed-file testbed.yaml --replay mocked_devices --devices nx-osv-1 --output explore1
    +==============================================================================+
    | Genie Parse Summary for nx-osv-1                                             |
    +==============================================================================+
    |  Connected to nx-osv-1                                                       |
    |  -  Log: explore-1/connection_nx-osv-1.txt                                   |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show version'                                               |
    |  -  Parsed structure: explore-1/nx-osv-1_show-version_parsed.txt             |
    |  -  Device Console:   explore-1/nx-osv-1_show-version_console.txt            |
    |------------------------------------------------------------------------------|

There are over :parsers:`500+ Parsers<http>` existing right now for you to use!

More information on :ref:`Parser<book_parser>` and :ref:`Genie Cli <genie_cli>`.

2. Learn devices' features into structured output
-------------------------------------------------

Instead of learning a few cli at the time, you can learn the whole feature and
have it into 1 structured output (Json/Dictionary). This structure is agnostic
between all OS (Identical between all the OS).

**Python Mode**

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    genie shell --testbed-file testbed.yaml --replay mocked_devices

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Python</span>

.. code-block:: python

    testbed.devices['nx-osv-1'].connect()
    output = testbed.devices['nx-osv-1'].learn('ospf')
    import pprint
    pprint.pprint(output.info)
    # {
    # 'feature_ospf': True,
    # 'vrf': {
    #   'default': {
    #     'address_family': {
    #       'ipv4': {
    #         'instance': {
    #           '1': {
    #             'graceful_restart': {
    #               'ietf': {
    #                 'enable': True,
    #                 'restart_interval': 60,
    #                 'type': 'ietf',
    #                 },
    #               },
    #             'enable': True,
    #             'auto_cost': {
    # ...

**Linux Mode**

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    genie learn "ospf" --testbed-file testbed.yaml --replay mocked_devices --devices nx-osv-1
    # +==============================================================================+
    # | Genie Learn Summary for device nx-osv-1                                      |
    # +==============================================================================+
    # |  Connected to nx-osv-1                                                       |
    # |  -   Log: ./connection_nx-osv-1.txt                                          |
    # |------------------------------------------------------------------------------|
    # |  Learnt feature 'ospf'                                                       |
    # |  -  Ops structure:  ./ospf_nxos_nx-osv-1_ops.txt                             |
    # |  -  Device Console: ./ospf_nxos_nx-osv-1_console.txt                         |
    # |==============================================================================|

:models:`All available features<http>`

More information on :ref:`Ops<book_ops>` and :ref:`Genie Cli <genie_cli>`.

3. Configure devices feature with python object 
-----------------------------------------------

Genie Conf allows to configure a device with with python object following a
structured object model. This object model is agnostic between all OS.

**Python Mode**

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Python</span>

.. code-block:: bash

    genie shell --testbed-file testbed.yaml --replay mocked_devices

.. raw:: html

    <i class="fa fa-anchor"></i>
    <span style='color:#6ab0de'>Python</span>

.. code-block:: python

    from genie.conf.base import Interface
    uut = testbed.devices['uut']
    uut.connect()
    # Create an NXOS interface
    nxos_interface = Interface(device=uut, name='Ethernet4/3')
    # Add some configuration
    nxos_interface.ipv4 = '200.1.1.2'
    nxos_interface.ipv4.netmask ='255.255.255.0'
    nxos_interface.shutdown = False
    # Verify configuration generated
    print(nxos_interface.build_config(apply=False))
    # interface Ethernet4/3
    #  no shutdown
    #  ip address 200.1.1.2 255.255.255.0
    #  exit
    nxos_interface.build_config() # To apply on the device
    nxos_interface.build_unconfig() # To remove configuration

:models:`All available features<http>`

More information on :ref:`Conf<book_conf>`.

4. Device API functions
-----------------------
Genie has a set of built in :apis:`API functions <http>` that can be used to perform various actions including config, verify, get, analyze, and more on the device.
They can be accessed directly with the `device.apis` method. To use them, simply find
the API name you need, then call the API with it's argument as:
`device.api.api_name(args_1, args_2, ....)`

Example
```````
.. code-block:: python

	device=testbed.devices['My_device']
	device.connect(via='cli')
	device.api.shut_interface(interface='Loopback0')


The above would perform the following action on the device:

.. code-block:: none

	config term
	Enter configuration commands, one per line.  End with CNTL/Z.
	My_device(config)#interface Loopback0
	My_device(config-if)#shutdown
	My_device(config-if)#end
	My_device


5. RobotFramework Library
--------------------------

Familiar with `RobotFramework`_ ? Genie comes with its own :ref:`Genie
RobotFramework library<robot_genie>`.

.. _RobotFramework: http://robotframework.org/

Robot example can also be found in our :ref:`example` page as Example 5.

6. Run Testcases
----------------

Genie comes with a harness to execute triggers on your devices.

.. raw:: html

    <i class="fa fa-anchor"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    genie run --testbed-file testbed.yaml \
              --trigger-uids="And('TriggerShutNoShutBgp$')" \
              --verification-uids="And('Verify_BgpProcessVrfAll$')" \
              --html_logs . \
              --replay run_mocked_devices 

:testcase:`All avaible triggers <http>`

More information on :ref:`Harness<book_harness>`.

  .. note::

      Full log can be accessed from here :download:`TaskLog.html <TaskLog.html>`.

7. Write parsers
----------------

:ref:`Parsergen <parsergen>` allows to write parser from scratch with just one api call.

.. raw:: html

    <i class="fa fa-anchor"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    genie shell --testbed-file testbed.yaml --replay mocked_devices

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    from genie import parsergen
    uut = testbed.devices['uut']
    uut.connect()
    output = uut.execute('show interface brief')
    result = parsergen.oper_fill_tabular(
                    header_fields= [['Ethernet', 'VLAN', 'Type', 'Mode', 'Status', 'Reason', 'Speed', 'Port'],
                                    ['Interface', '', '', '', '', '', '', 'Ch \#']],
                    label_fields= ['Ethernet Interface', 'VLAN', 'Type', 'Mode', 'Status', 'Reason', 'Speed', 'Port'],
                    device_output= output,
                    device_os= 'nxos',
                    index= [0])
    import pprint
    pprint.pprint(result.entries)
    # {'Eth2/1': {'Ethernet Interface': 'Eth2/1',
    #             'Mode': 'routed',
    #             'Port': '--',
    #             'Reason': 'none',
    #             'Speed': '1000(D)',
    #             'Status': 'up',
    #             'Type': 'eth',
    #             'VLAN': '--'},
    #  'Eth2/10': {'Ethernet Interface': 'Eth2/10',
    #              'Mode': 'routed',
    #              'Port': '--',
    #              'Reason': 'Administratively down',
    #              'Speed': 'auto(D)',
    #              'Status': 'down',
    #              'Type': 'eth',
    #  ...

More information on :ref:`Parser<book_parser>` and :ref:`Genie Cli <genie_cli>`.


8. Possible ways to use Genie
-----------------------------

Here are a few inspiration on how Genie can be useful


**Test Automation oriented examples**

* Parse device output that can be used within script to verify certain state of the devices.
* Re-use any of the available :testcase:`testcases <http>` to test your devices/images.
* Future-proof design which works across connection (Cli/Yang/Xml/OpenConfig/Native models/...)
* One script which works across platforms, spend time writing good libraries and less into modifying scripts
* Verify Cli outputs with Yang and xml outputs! 


**DevNet oriented examples**

* Connect to your devices and make sure that all devices are up, running and pingable between each other
* Connect to your devices and retrieve information about the state of your network
* Collect snapshot of your network and compare with the initial snapshot
* Parse device output and stored snapshot. Every <time> rerun same commands are
  compare state to make sure nothing has changed.
* Take a snapshot of your network and compare the snapshot once a new image has been applied to verify the state of the network
* Re-use any of the available :testcase:`testcases <http>` to test your Topologies after image upgrade.
* Perform action such as Reload Devices, Perform Switchover, ShutNoShutBgp, ConfigUnconfigOspf, etc
* Verify your topology is stable


* And many more! Once you have the libraries, everything can be automated!

:mailto:`Contact us<cisco.com>` to discuss how Genie can help you!

.. _book_explore_workshop:

9. Workshops
------------

Here is two workshop to get you started with Genie.

1. https://github.com/CiscoTestAutomation/CL-DevNet-2595
2. https://github.com/RunSi/DEVWKS-2601

All the devices (They are mocked devices, python scripts which simulate
devices) and needed information are on the github.


