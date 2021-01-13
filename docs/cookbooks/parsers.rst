.. _book_parser:

.. raw:: html

   <h2>Genie Parser Recipes</h2>

1. Summary
----------

Genie.libs.parsers is a parser library. It takes device output and convert it
into a structured datatype (Json/dictionary)

.. code-block:: text

    --------------------------------------------------------------------------------
    Port   VRF          Status IP Address                              Speed    MTU
    --------------------------------------------------------------------------------

    --------------------------------------------------------------------------------
    Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
    Interface                                                                    Ch #
    --------------------------------------------------------------------------------
    Eth1/1        1       eth  routed up      none                       1000(D) --
    Eth1/2        --      eth  routed up      none                       1000(D) --
    Eth1/3        --      eth  routed up      none                       1000(D) --

And convert it into

.. code-block:: text

    # parsed_output
    # -------------
    # {'Eth1/1': {'Ethernet Interface': 'Eth1/1',
    #             'Mode': 'routed',
    #             'Port': '--',
    #             'Reason': 'none',
    #             'Speed': '1000(D)',
    #             'Status': 'up',
    #             'Type': 'eth',
    #             'VLAN': '1'},
    #  'Eth1/2': {'Ethernet Interface': 'Eth1/2',
    #             'Mode': 'routed',
    #             'Port': '--',
    #             'Reason': 'none',
    #             'Speed': '1000(D)',
    #             'Status': 'up',
    #             'Type': 'eth',
    #             'VLAN': '--'},
    #  'Eth1/3': {'Ethernet Interface': 'Eth1/3',
    #             'Mode': 'routed',
    #             'Port': '--',
    #             'Reason': 'none',
    #             'Speed': '1000(D)',
    #             'Status': 'up',
    #             'Type': 'eth',
    #             'VLAN': '--'}}


Once you have this structured data you can do so much with it:

    * Look for specific key/value
    * Verify if state is as expected
    * Compare between two dictionaries and verify if anything has changed

Once you have the data, the possibilities are really limitless.

2. Available parsers
--------------------

Visit our :parsers:`website to find all the available parsers<http>`.


3. How to execute a parser - Python
-----------------------------------

Parsers are easy to call.

You want to call it within python? First, you must have a :ref:`Genie Testbed
object<book_setup_testbed>`.

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

    You can also use the :ref:`Genie shell<book_explore_1>` command line for
    Python interactive shell

.. tip::

	use ``device.parse('all')`` to run all the available parsers on the device, and the output will be returned in a dictionary
	format: ``{'show command' : parsed_output}``. If an exception occurred during the execution a particular parser, then ``parsed_output`` will become the exception object.

3. How to execute a parser - Linux
----------------------------------

Parsers are easy to call even without knowing python. 

.. raw:: html

    <i class="fa fa-linux"></i>
    <span style='color:#6ab0de'>Bash</span>

.. code-block:: bash

    genie parse "show version" --testbed-file testbed.yaml --output explore1
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

.. note::

   You can find all the details in the :ref:`Genie Cli
   documentaiton<genie_cli>`

4. Get exclude keys for a parser - Python
-----------------------------------------

.. code-block:: python

    from genie.libs.parser.utils import get_parser_exclude
    get_parser_exclude('show interface', dev)
    ['in_unicast_pkts', 'out_unicast_pkts', 'in_octets', 'out_octets', 'in_pkts', 'out_pkts', ...]

5. Compare two parsers - Python
-------------------------------

.. code-block:: python

    from genie import testbed
    from genie.utils.diff import Diff
    from genie.libs.parser.utils import get_parser_exclude
    tb = testbed.load('tb.yaml')
    device = tb.devices['nx-osv-1']
    device.connect()
    output1 = device.parse('show version')
    ...
    output2 = device.parse('show version')
    # Without exclude keys
    diff = Diff(output1, output2)
    diff.findDiff()
    print(diff)
    platform:
     kernel_uptime:
    +  seconds: 15
    -  seconds: 3

    # With exclude keys
    diff = Diff(output1, output2, exclude=get_parser_exclude('show version', device))
    diff.findDiff()
    print(diff)

6. Executing parsers with fuzzy search - Python
-----------------------------------------------

Adding `fuzzy=True` when calling parse enables fuzzy search, which allows you to
use some regex syntax in your search and match multiple commands. By default, 
searching for command is done by exact match or prefix matching, if no ambiguity
exists.

.. code-block:: python

    from genie import testbed
    tb = testbed.load('tb.yaml')
    device = tb.devices['nx-osv-1']
    device.connect()
    output = device.parse('show bgp .*', fuzzy=True)
    ...


Fuzzy matching works by tokenizing your search query by spaces, and then 
comparing each token with each of the command's token to see if they are either
the same or is the prefix of the other. When it encounters the supported regex 
expressions, it will perform regex matching as expected and return the results. 
The search is done by best fit, meaning it will try its best to fit your query
with each command, and if it succeeds, it will be counted as a match. As a 
result, arguments are essentially wild cards, and using fuzzy will attempt to
fit your query with the arguments in any way possible. For instance, 
`sh .* abc .*` will match with `show vrf {vrf} detail`. In this case `abc` is 
simply an argument for `vrf`.

Fuzzy current supports the follow regex symbols and their combinations:

- *
- [a-zA-Z0-9]
- +
- ?
- \s\S\w\W\d\D
- [^a-zA-Z0-9]
- (a|b)
- a{3}
- .

However, since lookup is done by one token at a time, this will limit the use of 
more complex regex expressions such as lookahead and greedy. Moreover, space is 
used as a delimiter, so to incorporate space in your query, use `\s` instead.

Here are some example of matches: 

+----------------------------------------------------------------------------------+
| Search                       |                                    Sample Results |
+==================================================================================+
| sh .* tags                   |                                show ethernet tags |
+------------------------------+---------------------------------------------------+
| sh .* abc .* ext             |             show ospf vrf {vrf} database external |
+------------------------------+---------------------------------------------------+
| sh .* [a-z]* ext\S+          |                       show ted database extensive |
|                              |                    show ospf3 interface extensive |
|                              |     show ospf vrf all-inclusive database external |
|                              |                                               ... |
+------------------------------+---------------------------------------------------+

Fuzzy matching will return multiple parsed results in the form of a dictionary,
where the key indicates the command executed and the value is the output. In
some cases, commands that are not enabled on the device will be executed too,
and consequently throw an error in your script. To silence these exceptions, 
attach `continue_on_failure=True` to your parse call:

.. code-block:: python

    output = device.parse('show .*', fuzzy=True, continue_on_failure=True)
    ...

This will execute all the commands without raising an exception. Any silenced
errors can be accessed through `output['exceptions']`, which is a dictionary
of the command that failed mapped to its corresponding error message.