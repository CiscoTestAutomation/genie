api
===

The ``api`` command invokes Genie APIs on the device loaded in the 
LAMP shell and automatically generates a pyATS Blitz *'api'* action 
snippet.

.. note::

   For comprehensive information on Genie APIs, refer to the 
   `API Documentation <https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/deviceapis.html#>`_.

Why use API
-----------

Genie APIs simplify complex network tasks by executing Python 
code that provides functionality beyond standard LAMP commands.
These APIs enable advanced device operations and configuration
management.

Basic usage
-----------

LAMP provides two methods to invoke Genie APIs:

1. **Module-based approach**: 
   ``api <MODULE_NAME> <SUBMODULE_NAME> <API_NAME>``
   
   This method uses module names to navigate to specific APIs.
   It helps organize APIs and makes discovering available
   options easier.

2. **Direct approach**: 
   ``api <API_NAME>``
   
   This method invokes an API directly using its name.

Both methods execute the same underlying Genie API code. The 
module-based approach provides better organization, with 
submodule names like 'get', 'configure', or 'verify' indicating
the specific functionality type.

The direct approach works best when the API name is already 
known or discovered using the 
`Genie API browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_.

The following example demonstrates how API works in LAMP.
The signature and docstring for a Genie *configure* API
'config_standard_acl_for_ip_pim' is shown in the following code block:

.. code-block:: python

   def config_standard_acl_for_ip_pim(
           device,
           acl_name,
           permission,
           host_ip,
           host_wildcard,
           vrf,
           rp_address,
           bir_enabled=False
   ):
       """ Configures a standard IP access list.
           Args:
               device ('obj'): device object
               acl_name ('str'): acl name
               permission ('str'): (permit | deny)
               host_ip ('str'): source start ip
               host_wildcard ('str'): increment step for source ip
               vrf ('str'): vrf name
               rp_address ('str'): mention the IP address of the rendezvous point for the group.
               bir_enabled ('boolean', optional): sets true if enabled.  Defaults to False.
           Returns:
               config
           Raises:
               SubCommandFailure: Failed to configure access-list
       """

Example argument values for invoking this API:

.. code-block:: python

    config_standard_acl_for_ip_pim(device=leaf2,
                                   acl_name='acl2',
                                   permission='deny',
                                   host_ip='30.0.0.2',
                                   host_wildcard='255.255.255.255',
                                   vrf='red',
                                   rp_address='3.3.3.3')

To invoke this API in LAMP, use the following command:

.. code-block:: console

   (lamp-leaf2) api config_standard_acl_for_ip_pim
   Configures a standard IP access list.
   Args:
       device ('obj'): device object
       acl_name ('str'): acl name
       permission ('str'): (permit | deny)
       host_ip ('str'): source start ip
       host_wildcard ('str'): increment step for source ip
       vrf ('str'): vrf name
       rp_address ('str'): mention the IP address of the rendezvous point for the group.
       bir_enabled ('boolean', optional): sets true if enabled.  Defaults to False.
   Returns:
       config
   Raises:
       SubCommandFailure: Failed to configure access-list
   <TRUNCATED>

After displaying the docstring, LAMP prompts for arguments one by one:

.. code-block:: console

   (lamp-leaf2) api config_standard_acl_for_ip_pim
   Configures a standard IP access list.
   <TRUNCATED>
   device: [<Device leaf2 at 0x7efd35aa2850>]
   acl_name: acl2
   permission: permit
   host_ip: 30.0.0.2
   host_wildcard: 255.255.255.255
   vrf: red
   rp_address: 3.3.3.3
   bir_enabled(False):
   <TRUNCATED>

The 'device' argument is automatically filled with the 
currently loaded device in the LAMP shell (switching to the 
target device before API invocation is required). For 
remaining parameters, enter each value when prompted.

LAMP uses AST (Abstract Syntax Tree) literal evaluation to 
determine actual argument values:

- Entering ``20`` creates integer 20
- Entering ``'20'`` creates string '20'

Default argument values appear in parentheses after parameter
names. Press <Enter> to accept default values.

After entering all arguments, LAMP displays informational 
messages showing the processed argument values (helpful for 
understanding how LAMP interpreted the input):

.. code-block:: console

   (lamp-leaf2) api config_standard_acl_for_ip_pim
   Configures a standard IP access list.
   <TRUNCATED>
   device: [<Device leaf2 at 0x7efd35aa2850>]
   acl_name: acl2
   permission: permit
   host_ip: 30.0.0.2
   host_wildcard: 255.255.255.255
   vrf: red
   rp_address: 3.3.3.3
   bir_enabled(False):
   2024-08-10 11:45:34: %LAMP-INFO: +..............................................................................+
   2024-08-10 11:45:34: %LAMP-INFO: :            Api 'config_standard_acl_for_ip_pim' with parameters:             :
   2024-08-10 11:45:34: %LAMP-INFO: :                                device: leaf2                                 :
   2024-08-10 11:45:34: %LAMP-INFO: :                               acl_name: 'acl2'                               :
   2024-08-10 11:45:34: %LAMP-INFO: :                             permission: 'permit'                             :
   2024-08-10 11:45:34: %LAMP-INFO: :                             host_ip: '30.0.0.2'                              :
   2024-08-10 11:45:34: %LAMP-INFO: :                       host_wildcard: '255.255.255.255'                       :
   2024-08-10 11:45:34: %LAMP-INFO: :                                  vrf: 'red'                                  :
   2024-08-10 11:45:34: %LAMP-INFO: :                            rp_address: '3.3.3.3'                             :
   2024-08-10 11:45:34: %LAMP-INFO: :                              bir_enabled: False                              :
   2024-08-10 11:45:34: %LAMP-INFO: +..............................................................................+
   
   2024-08-10 11:45:34,133: %UNICON-INFO: +++ leaf2 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   leaf2(config)#ip access-list standard acl2
   leaf2(config-std-nacl)#permit 30.0.0.2 255.255.255.255
   leaf2(config-std-nacl)#ip pim vrf red rp-address 3.3.3.3 acl2
   leaf2(config)#end
   leaf2#
   2024-08-10 11:45:34: %LAMP-INFO: +..............................................................................+
   2024-08-10 11:45:34: %LAMP-INFO: :                                 Api output:                                  :
   2024-08-10 11:45:34: %LAMP-INFO: +..............................................................................+
                                                                          None
   2024-08-10 11:45:34: %LAMP-INFO: +..............................................................................+
   (lamp-leaf2)

Include entries
---------------

To add an *include* entry, use ``api -i <API_NAME>`` with '-i'
preceding the API name or module name. This prompts for
*include* entries after displaying the API output. The type of
*include* entry depends on the API output data type:

.. list-table:: Include entry types by API output type
   :widths: 50 50
   :header-rows: 1

   * - API output type
     - Include entry type
   * - str
     - Exact string pattern from output
   * - dict
     - Dq query or line numbers
   * - int
     - Comparison expressions {==,>=,<=,<,>,!=}
   * - list
     - List element values
   * - bool
     - True/False values
   * - None
     - NOT PERMITTED

str
^^^

For string output, *include* entries match exact string content
from the API response.

Example:

.. code-block:: console

   (lamp-host1) api -i get_interface_ip_address
   Get interface ip_address from device
   
   Args:
       interface('str'): Interface to get address
       device ('obj'): Device object
       address_family ('str'): Used only for junos api
   
   Returns:
       None
       interface ip_address ('str')
   
   Raises:
       None
   
   device: [<Device host1 at 0x7f4b88a53370>]
   interface: Loopback0
   address_family(None):
   2024-08-08 07:55:22: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:55:22: %LAMP-INFO: :               Api 'get_interface_ip_address' with parameters:                :
   2024-08-08 07:55:22: %LAMP-INFO: :                                device: host1                                 :
   2024-08-08 07:55:22: %LAMP-INFO: :                            interface: 'Loopback0'                            :
   2024-08-08 07:55:22: %LAMP-INFO: :                             address_family: None                             :
   2024-08-08 07:55:22: %LAMP-INFO: +..............................................................................+
   
   2024-08-08 07:55:23,141: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ip interface brief Loopback0' +++
   show ip interface brief Loopback0
   Interface              IP-Address      OK? Method Status                Protocol
   Loopback0              1.1.1.1         YES NVRAM  up                    up
   host1#
   2024-08-08 07:55:23: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:55:23: %LAMP-INFO: :                                 Api output:                                  :
   2024-08-08 07:55:23: %LAMP-INFO: +..............................................................................+
                                                                       '1.1.1.1'
   2024-08-08 07:55:23: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:55:23: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:55:23: %LAMP-INFO: :                                   INCLUDE                                    :
   2024-08-08 07:55:23: %LAMP-INFO: +..............................................................................+
   Enter pattern to INCLUDE (Press enter for multiple patterns): 1.1.1.1
   (lamp-host1) list 1
   api:
     function: get_interface_ip_address
     arguments:
       device: host1
       interface: Loopback0
       address_family:
     include:
       - 1.1.1.1

dict
^^^^

For dictionary output, *include* entries must be Dq queries.
Refer to :doc:`parse` *include* entries for detailed examples.

int
^^^

For integer output, *include* entries use comparison expressions
with the format:

    {operator}{expected_value}

Available operators:

- ``==``: Equal to
- ``>=``: Greater than or equal to  
- ``<=``: Less than or equal to
- ``<``: Less than
- ``>``: Greater than
- ``!=``: Not equal to

Example:

.. code-block:: console

   (lamp-host1) api -i get_interface_mtu_size
   Get interface MTU
   
   Args:
       device (`obj`): Device object
       interface (`str`): Interface name
   
   Returns:
       None
       mtu (`int`): mtu bytes
   
   Raises:
       None
   
   device: [<Device host1 at 0x7f4b88a53370>]
   interface: Loopback0
   2024-08-08 07:56:54: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:56:54: %LAMP-INFO: :                Api 'get_interface_mtu_size' with parameters:                 :
   2024-08-08 07:56:54: %LAMP-INFO: :                                device: host1                                 :
   2024-08-08 07:56:54: %LAMP-INFO: :                            interface: 'Loopback0'                            :
   2024-08-08 07:56:54: %LAMP-INFO: +..............................................................................+
   
   2024-08-08 07:56:54,682: %UNICON-INFO: +++ host1 with via 'a': executing command 'show interfaces Loopback0' +++
   show interfaces Loopback0
   Loopback0 is up, line protocol is up
     Hardware is Loopback
     Internet address is 1.1.1.1/32
     MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec,
        reliability 255/255, txload 1/255, rxload 1/255
     Encapsulation LOOPBACK, loopback not set
     Keepalive set (10 sec)
     Last input 00:00:02, output never, output hang never
     Last clearing of "show interface" counters never
     Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
     Queueing strategy: fifo
     Output queue: 0/0 (size/max)
     5 minute input rate 0 bits/sec, 0 packets/sec
     5 minute output rate 0 bits/sec, 0 packets/sec
        0 packets input, 0 bytes, 0 no buffer
        Received 0 broadcasts (0 IP multicasts)
        0 runts, 0 giants, 0 throttles
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
        56221 packets output, 2535652 bytes, 0 underruns
        Output 0 broadcasts (0 IP multicasts)
        0 output errors, 0 collisions, 0 interface resets
        0 unknown protocol drops
        0 output buffer failures, 0 output buffers swapped out
   host1#
   2024-08-08 07:56:54: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:56:54: %LAMP-INFO: :                                 Api output:                                  :
   2024-08-08 07:56:54: %LAMP-INFO: +..............................................................................+
                                                                          1514
   2024-08-08 07:56:54: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:56:54: %LAMP-INFO: +..............................................................................+
   2024-08-08 07:56:54: %LAMP-INFO: :                                   INCLUDE                                    :
   2024-08-08 07:56:54: %LAMP-INFO: +..............................................................................+
   Enter pattern to INCLUDE (Press enter for multiple patterns):
   (INCLUDE)> >=1000
   (INCLUDE)> <2000
   (INCLUDE)>
   (lamp-host1) list 1
   api:
     function: get_interface_mtu_size
     arguments:
       device: host1
       interface: Loopback0
     include:
       - '>=1000'
       - <2000
   (lamp-host1)

list
^^^^

For list output, *include* entries check for specific elements
present in the returned list.

Example:

.. code-block:: console

   (lamp-host1) api -i get_vrf_interface
   Gets the subinterfaces for vrf
   
   Args:
       device ('obj'): device to run on
       vrf ('str'): vrf to search under
   
   Returns:
       interfaces('list'): List of interfaces under specified vrf
       None
   
   Raises:
       None
   
   device: [<Device host1 at 0x7fbf73857400>]
   vrf: red
   2024-08-08 08:12:21: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:12:21: %LAMP-INFO: :                   Api 'get_vrf_interface' with parameters:                   :
   2024-08-08 08:12:21: %LAMP-INFO: :                                device: host1                                 :
   2024-08-08 08:12:21: %LAMP-INFO: :                                  vrf: 'red'                                  :
   2024-08-08 08:12:21: %LAMP-INFO: +..............................................................................+
   
   2024-08-08 08:12:21,975: %UNICON-INFO: +++ host1 with via 'a': executing command 'show vrf red' +++
   show vrf red
     Name                             Default RD            Protocols   Interfaces
     red                              <not set>                         Lo99
                                                                        Lo100
   host1#
   2024-08-08 08:12:22: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:12:22: %LAMP-INFO: :                                 Api output:                                  :
   2024-08-08 08:12:22: %LAMP-INFO: +..............................................................................+
                                                             ['Loopback100', 'Loopback99']
   2024-08-08 08:12:22: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:12:22: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:12:22: %LAMP-INFO: :                                   INCLUDE                                    :
   2024-08-08 08:12:22: %LAMP-INFO: +..............................................................................+
   Enter elements of the list you would like to INCLUDE (Press enter for multiple entries):
   INCLUDE> Loopback99
   INCLUDE> Loopback100
   INCLUDE>
   (lamp-host1) list 1
   api:
     function: get_vrf_interface
     arguments:
       device: host1
       vrf: red
     include:
       - Loopback99
       - Loopback100
   (lamp-host1)

bool
^^^^

For boolean output, *include* entries check for True or False 
values.

Example:

.. code-block:: console

   (lamp-host1) api -i verify_interface_state_up
   Verify interface state is up and and line protocol is up
   
   Args:
       device (`obj`): Device object
       interface (`str`): Interface name
       max_time (`int`): max time
       check_interval (`int`): check interval
   Returns:
       result(`bool`): True if is up else False
   
   device: [<Device host1 at 0x7fbf73857400>]
   interface: Ethernet0/0
   max_time(60): 10
   check_interval(10): 10
   2024-08-08 08:07:50: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:07:50: %LAMP-INFO: :               Api 'verify_interface_state_up' with parameters:               :
   2024-08-08 08:07:50: %LAMP-INFO: :                                device: host1                                 :
   2024-08-08 08:07:50: %LAMP-INFO: :                           interface: 'Ethernet0/0'                           :
   2024-08-08 08:07:50: %LAMP-INFO: :                                 max_time: 10                                 :
   2024-08-08 08:07:50: %LAMP-INFO: :                              check_interval: 10                              :
   2024-08-08 08:07:50: %LAMP-INFO: +..............................................................................+
   
   2024-08-08 08:07:51,056: %UNICON-INFO: +++ host1 with via 'a': executing command 'show interfaces Ethernet0/0' +++
   show interfaces Ethernet0/0
   Ethernet0/0 is up, line protocol is up
     Hardware is AmdP2, address is aabb.cc00.0100 (bia aabb.cc00.0100)
     Internet address is 10.10.10.1/24
     MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec,
        reliability 255/255, txload 1/255, rxload 1/255
     Encapsulation ARPA, loopback not set
     Keepalive set (10 sec)
     ARP type: ARPA, ARP Timeout 04:00:00
     Last input 1w5d, output 00:00:00, output hang never
     Last clearing of "show interface" counters never
     Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
     Queueing strategy: fifo
     Output queue: 0/40 (size/max)
     5 minute input rate 0 bits/sec, 0 packets/sec
     5 minute output rate 0 bits/sec, 0 packets/sec
        22118 packets input, 3638622 bytes, 0 no buffer
        Received 22102 broadcasts (0 IP multicasts)
        0 runts, 0 giants, 0 throttles
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
        0 input packets with dribble condition detected
        39848 packets output, 4708267 bytes, 0 underruns
        Output 22125 broadcasts (0 IP multicasts)
        0 output errors, 0 collisions, 3 interface resets
        0 unknown protocol drops
        0 babbles, 0 late collision, 0 deferred
        0 lost carrier, 0 no carrier
        0 output buffer failures, 0 output buffers swapped out
   host1#
   2024-08-08 08:07:51: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:07:51: %LAMP-INFO: :                                 Api output:                                  :
   2024-08-08 08:07:51: %LAMP-INFO: +..............................................................................+
                                                                          True
   2024-08-08 08:07:51: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:07:51: %LAMP-INFO: +..............................................................................+
   2024-08-08 08:07:51: %LAMP-INFO: :                                   INCLUDE                                    :
   2024-08-08 08:07:51: %LAMP-INFO: +..............................................................................+
   Enter value to check (True/False): True
   (lamp-host1) list 1
   api:
     function: verify_interface_state_up
     arguments:
       device: host1
       interface: Ethernet0/0
       max_time: 10
       check_interval: 10
     include:
       - true
   (lamp-host1)

Exclude entries
---------------

To add an *exclude* entry, use ``api -e <API_NAME>`` with '-e'
preceding the API name or module name. This prompts for
*exclude* entries after displaying the API output. *Exclude*
entry types also vary based on the API output data type:

.. list-table:: Exclude entry types by API output type
   :widths: 50 50
   :header-rows: 1

   * - API output type
     - Exclude entry type
   * - str
     - Any string pattern
   * - dict
     - Dq query expressions
   * - int
     - NOT PERMITTED
   * - list
     - Values not present in list
   * - bool
     - True/False values
   * - None
     - Any specified value