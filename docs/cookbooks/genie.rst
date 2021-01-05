.. _book_genie:

.. raw:: html

   <h2>Genie Generic Recipes</h2>

1. How to install Genie
-----------------------

Internal employee:
``````````````````

    1. Install pyATS - Follow the information on the :pyatswiki:`pyATS wiki <http>`.
    2. Get libraries permission - Make sure to request :permission:`permission <http>` to bitbucket.
    3. If you are using a machine in the lab, source the proxy: source /auto/pyats/bin/lab_proxy.sh (.csh)
    4. Install Genie - pip install genie

DevNet
``````

   1. Install pyATS - Follow the information on :pyats_gettingstarted:`pyATS install guide <http>`.
   2. Install Genie - pip install genie

.. note::

    Visit :ref:`Genie installation<installation>` page for more information

.. note::

    Make sure to visit :pyats:`pyAts <http>`website for all information about pyATS.

.. note::

    It is recommended to create a virtual environment for any pyATS
    installation.


2. How to keep Genie up to date - How to upgrade Genie?
--------------------------------------------------------

One simple command:

.. code-block:: bash

    pip install genie --upgrade

This will give you the latest version of Genie

3. Summary of Genie Libraries and how to keep those up to date.
---------------------------------------------------------------

Genie is a modular package. It is divided into the following packages: 

.. code-block:: text

    genie                         Main Genie package
    genie.libs.conf               Libraries for Configuration object 
    genie.libs.filetransferutils  Libraries for File Transfer utils 
    genie.libs.ops                Genie core for Operation state object 
    genie.libs.parser             Libraries containing all the parsers 
    genie.libs.robot              Libraries containing all Robot keywords
    genie.libs.sdk                Libraries containing all Triggers and Verifications
    genie.telemetry               Genie Core for telemetry - Monitor testbed

Each is separate pip packages which can be updated at any time with the
following command:

.. code-block:: bash

    pip install <package name> --upgrade


For example:

.. code-block:: bash

    pip install genie.libs.robot --upgrade
    pip install genie.telemetry --upgrade

4. Genie Libraries and Recording
--------------------------------

Below Genie packages are Open source libraries.
Ready for your contribution!

.. csv-table:: Libraries git location
    :header: "Library", "Git repository"

    ``genie.libs.conf``, :genielibs_repo:`Genie.libs Repository <http>`
    ``genie.libs.ops``, :genielibs_repo:`Genie.libs Repository <http>`
    ``genie.libs.sdk``, :genielibs_repo:`Genie.libs Repository <http>`
    ``genie.libs.robot``, :genielibs_repo:`Genie.libs Repository <http>`
    ``genie.libs.parser``, :parser_repo:`Genie.libs.parser Repository <http>`
    ``genie.telemetry``, :telemetry_repo:`Genie.telemetry Repository <http>`
    ``genie.libs.filetransferutils``, :filetransferlibs_repo:`Genie.libs.filetransferutils Repository <http>`

**Recording**

Watch these recordings on how to install them and start contributing!

.. csv-table:: Recordings
    :header: "Subject", "Link", "password"

    Contribute to Genie - Getting started, `Link <https://cisco.webex.com/recordingservice/sites/cisco/recording/playback/379c20aa1b864aef9a4b07a93db93b40>`_, GenieTraining1
    Modify existing Trigger, `Link <https://cisco.webex.com/recordingservice/sites/cisco/recording/playback/bd08573eabd445648d2365aaa20c1c22>`_, GenieTraining1
    Create a new Trigger, `Link <https://cisco.webex.com/recordingservice/sites/cisco/recording/playback/836c1d32f2634427abb62c7efa148780>`_, GenieTraining1
    Genie.abstraction introduction, `Link <https://cisco.webex.com/cisco/ldr.php?RCID=7c81df3e847ac07e1485d5cc9742ebcd>`_, GenieTraining1
    Create a new trigger under new abstraction package, `Link <https://cisco.webex.com/cisco/ldr.php?RCID=e8208d31e7744c0960e3cb3618acdc9d>`_, GenieTraining1


.. _book_setup_testbed:

5. Set up your testbed file and connect to a device
---------------------------------------------------

Create your own Testbed file related to your device by following the :pyats_settestbed:`pyATS guide. <http>`

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
              cli:
                  protocol: telnet
                  ip: "172.25.192.90"
                  port: 17052

Here are a few important details to keep in mind:

1) The device name must match the hostname of the device, otherwise, the
connection will hang. 

2) At least one device need to have the alias 'uut' in the testbed yaml file.

Your testbed is now ready to be used within `Genie`.

.. code-block:: python

    from genie import testbed
    testbed = testbed.load('testbed.yaml')
    device = testbed.devices['nx-osv-1']
    device.connect()

.. raw:: html

    <script src="https://asciinema.org/a/NJQ0lqOqD5SFAh4tG7EqtWq9n.js" id="asciicast-NJQ0lqOqD5SFAh4tG7EqtWq9n" async></script>

.. note::

    More information on the :ref:`testbed <topology_testbed>` page.

.. note::

    Genie follows the same concept as pyATS. For more information
    visit :connectdevice:`pyATS website<http>`.

.. _book_genie_excel_tb:

Create a Testbed from an Excel sheet
````````````````````````````````````
You can also create a testbed yaml from an excel sheet with `pyats create testbed` command, here's an example:

Here is an excel sheet containing device data:

	.. figure:: Excel_book.png
		:alt: Sample Excel file

we can turn it into a testbed yaml file by running the following command:

.. code-block:: bash

	[genie] demo:373> pyats create testbed file --path my_devices.xls --output yaml/my_testbed.yaml
	... Testbed file generated: yaml/my_testbed.yaml

This will give us the below yaml:

.. code-block:: yaml

	devices:
	  R1:
		connections:
		  cli:
			ip: 172.25.192.101
			port: 17013
			protocol: ssh
		credentials:
		  default:
			password: cisco
			username: admin
	      enable:
			password: cisco
		os: iosxe
		type: iosxe
	  R2:
		connections:
		  cli:
			ip: 172.25.192.102
			port: 17015
			protocol: ssh
		credentials:
		  default:
			password: cisco
			username: admin
		  enable:
			password: cisco
		os: iosxr
		type: iosxr
	  R3:
		connections:
		  cli:
			ip: 172.25.192.103
			port: 17019
			protocol: ssh
		credentials:
		  default:
			password: cisco
			username: admin
	      enable:
			password: cisco
		os: nxos
		type: nxos

For more info on creating a testbed from Excel, please read :ref:`Create Testbed <cli_create>`.


.. _book_genie_dict_tb:

Create a Testbed from a Dictionary
``````````````````````````````````

Genie testbed also support creating a testbed directly from a dictionary without a yaml file. This feature is
convenient for quick testing without complicated configurations, and it allows seamless transition from json if
the device data obtained from a remote server.

The below code shows the minimum data required for a successful creation, please consult :ref:`pyats create testbed <cli_create_testbed>`
for the minimum key requirement.

.. note::
	``port`` here is an optional key and it is separate from the ip address.


.. code-block:: python

	from genie.testbed import load
	o =  {"devices":{
			"R1_xe":{
				"ip":"172.25.192.104",
				"port": 17005,
				"protocol": "telnet",
				"username": "admin",
				"password": "cisco",
				"os": "iosxe",
		}
	 }}
	testbed = load(o)
	device=testbed.devices['R1_xe']
	device.connect()


.. _book_genie_extra_connection:

6. Extra connections!
---------------------

There are multiple ways to connect to a device. Using Telnet, ssh, Rest, Yang,
etc.

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
              a:
                  protocol: telnet
                  ip: "172.25.192.90"
                  port: 17052
              vty:
                  protocol: telnet
                  ip: "10.1.3.2"

To connect with these connections:

.. code-block:: python

    # Default to 'a'
    device.connect()
    device.execute('show version')

    # Use Telnet
    device.connect(via=vty, alias='vty')
    device.vty.execute('show version')

For Genie, it needs to know which connection to use for each device.

.. code-block:: python

    device.mapping['cli'] = 'vty'

.. note::

    the supported keys are: cli, xml, rest and yang.


.. _book_genie_connection_control:

7. Control devices' connections!
--------------------------------

If no mapping datafile provided or `devices` passed in the job
file/command line argument, Genie by default will connect to all the devices in
the testbed yaml file.

If user wants to control the connection method per device, this can be controlled by;

  A) Using the mapping datafile explained :ref:`here <mapping_datafile>`

  B) Passing argument `devices` in the job file/command line argument,
     check here for :ref:`details <harness_arguments>`

     In that case, each device passed in the `devices` list argument need to either;

     1 - Have a single connection defined in the testbed yaml file

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
                        ip: "100.100.100.100"
                        port: 17052

     2 - Have multiple connections defined in the testbed yaml file but at least one of them named `cli`

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
                        ip: "100.100.100.100"
                        port: 17052
                    cli:      ------ > Here it is required to be named `cli`
                        protocol: telnet
                        ip: "172.25.192.90"
                        port: 17052


8. Parse device output
----------------------

Parsing a device output is as easy as just asking for it.

.. code-block:: python

    # Default to 'a'
    device.connect()
    output = device.parse('show version')

    import pprint
    pprint.pprint(output)

    {'platform': {'hardware': {'bootflash': '3184776 kB',
                               'chassis': 'NX-OSv Supervisor Module',
                               'device_name': 'nx-osv-1',
                               'model': 'NX-OSv',
                               'processor_board_id': 'TM00010000B',
                               'slots': 'None'},
    ...

:parsers:`List of all available parsers<http>`.


9. Learn device feature
-----------------------

Learning a whole device feature is also very easy.

.. code-block:: python

    # Default to 'a'
    device.connect()
    output = device.learn('ospf')

    import pprint
    pprint.pprint(output)

    {
    'feature_ospf': True,
    'vrf': {
      'default': {
        'address_family': {
          'ipv4': {
            'instance': {
              '1': {
                'nsr': {
                  'enable': True,
                  },
                'enable': True,
                'auto_cost': {
    ...

:models:`List of all available feature<http>`.

:ref:`More information on Ops<book_ops_summary>`.


