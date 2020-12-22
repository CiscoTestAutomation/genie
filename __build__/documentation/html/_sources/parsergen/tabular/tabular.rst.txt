.. _oper_fill_tabular:

The Tabular Parser
==================
``parsergen`` is a generic parser for show commands. The goal is to make
it simple to create a parser for any given show command one time, and then
reuse this parser to create tests for any values found within the output.

The main functions of ``parsergen`` are:

  - Find and verify expected values in show command output.
  - Provide an OS agnostic common interface to OS specific show commands.
  - Create once (per command), use many times (throughout all of your pyATS
    test suites).
  - Maintain a per command cache for fast processing.
  - Only parse the parts of the output that the user is interested in, thus
    avoiding wasting precious real-time.

Column Based Results
--------------------

For column based table results one should use the
`oper_fill_tabular` class. To illustrate it's use we'll examine some standard
table results.


Full :command:`show arp` example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    RP/0/0/CPU0:one#show arp
    Fri Jan 22 15:39:49.731 EST

    -------------------------------------------------------------------------------
    0/0/CPU0
    -------------------------------------------------------------------------------
    Address         Age        Hardware Addr   State      Type  Interface
    11.11.11.1      -          0292.77d4.d5ee  Interface  ARPA  GigabitEthernet0/0/0/0
    10.10.10.1      -          02b7.a23a.e076  Interface  ARPA  GigabitEthernet0/0/0/1
    11.11.11.2      00:00:35   02e9.4522.5326  Dynamic    ARPA  GigabitEthernet0/0/0/0
    10.10.10.2      00:00:35   02db.ebba.ecc4  Dynamic    ARPA  GigabitEthernet0/0/0/1
    RP/0/0/CPU0:one#

.. Example: Output of show arp command.

We need to identify a few things in order to parse this output. First if there
are multiple tables we must identify what the title of each table is. In this
case the title is a card reference. Next we must identify the headers that
define the columns. For show arp the headers are ``Address``, ``Age``,
``Hardware Addr``, ``State``, ``Type``, and ``Interface``. Finally we need to
determine how to uniquely identify entries from the table. These are the
``index`` fields. For :command:`show arp` these would be the ``Address`` and
``Interface`` fields or columns 0 and 5. For this command that is all we need. ::

    def test_log_arp_results_1 (self):
        res = parsergen.oper_fill_tabular(device=device1,
                                          show_command="show arp",
                                          header_fields=
                                              [ "Address",
                                                "Age",
                                                "Hardware Addr",
                                                "State",
                                                "Type",
                                                "Interface" ],
                                          index = [ 0, 5 ],
                                          table_title_pattern = r"^(\d+/\d+/CPU\d+)")

        log.info("Tabular parse result:\n" + pprint.pformat(res.entries))


.. Example: First part of test_log_arp_results_1().

Now when we execute the test the following output is logged::

    Results:
    {'0/0/CPU0': {'10.10.10.1': {'GigabitEthernet0/0/0/1': {'Address': '10.10.10.1',
                                                            'Age': '-',
                                                            'Hardware Addr': '02b7.a23a.e076',
                                                            'Interface': 'GigabitEthernet0/0/0/1',
                                                            'State': 'Interface',
                                                            'Type': 'ARPA'}},
                  '10.10.10.2': {'GigabitEthernet0/0/0/1': {'Address': '10.10.10.2',
                                                            'Age': '00:00:14',
                                                            'Hardware Addr': '02db.ebba.ecc4',
                                                            'Interface': 'GigabitEthernet0/0/0/1',
                                                            'State': 'Dynamic',
                                                            'Type': 'ARPA'}},
                  '11.11.11.1': {'GigabitEthernet0/0/0/0': {'Address': '11.11.11.1',
                                                            'Age': '-',
                                                            'Hardware Addr': '0292.77d4.d5ee',
                                                            'Interface': 'GigabitEthernet0/0/0/0',
                                                            'State': 'Interface',
                                                            'Type': 'ARPA'}},
                  '11.11.11.2': {'GigabitEthernet0/0/0/0': {'Address': '11.11.11.2',
                                                            'Age': '00:00:14',
                                                            'Hardware Addr': '02e9.4522.5326',
                                                            'Interface': 'GigabitEthernet0/0/0/0',
                                                            'State': 'Dynamic',
                                                            'Type': 'ARPA'}}}}

.. Example: Output from first part of test_log_arp_results_1().

For multi-table results the n-level dictionary in self.entries is first indexed
by the match groups from the table_title_pattern, in this case that is the card
location. The rest of the indices are given by the values from the columns
identified in the index arg. Once all these indices are specified the result is
the actual entry dictionary. This dictionary is indexed by the header name of
the value you want.

So for example if we want to see the ARP entry's MAC address for the IP
``10.10.10.2`` on one's ``GigabitEthernet0/0/0/1`` interface we would take the
above results and use the following code::

    addr = '10.10.10.2'
    intf = 'GigabitEthernet0/0/0/1'
    card = '0/0/CPU0'
    macaddr = res.entries[card][addr][intf]['Hardware Addr']
    log.info( addr + " on 0/0/CPU0 " + intf + " has MAC " + macaddr)

.. Example: Second part of test_log_arp_results_1().

The following output is produced::

    10.10.10.2 on GigabitEthernet0/0/0/1 has MAC 02db.ebba.ecc4

.. Example: Output from second part of test_log_arp_results_1().

A Simpler :command:`show arp` Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's worth recognizing that in most cases the IP address alone is enough to
uniquely identify an entry. Let's use that knowledge and additionally specify a
card location in our show command, as that will greatly simply the returned
results. ::

    RP/0/0/CPU0:one#show arp location 0/0/CPU0
    Thu May 13 11:59:18.909 EDT

    Address         Age        Hardware Addr   State      Type  Interface
    10.10.10.1      -          02b7.a23a.e076  Interface  ARPA  GigabitEthernet0/0/0/1
    11.11.11.1      -          0292.77d4.d5ee  Interface  ARPA  GigabitEthernet0/0/0/0
    10.10.10.2      00:00:31   02db.ebba.ecc4  Dynamic    ARPA  GigabitEthernet0/0/0/1
    11.11.11.2      00:00:31   02e9.4522.5326  Dynamic    ARPA  GigabitEthernet0/0/0/0
    RP/0/0/CPU0:one#

.. Example: Simpler output for show arp command.

Now for the test code.::

    def test_log_arp_results_2 (self):
        res = parsergen.oper_fill_tabular(device=device1,
                                      show_command="show arp location 0/0/CPU0",
                                      header_fields =
                                        [ "Address",
                                          "Age",
                                          "Hardware Addr",
                                          "State",
                                          "Type",
                                          "Interface" ])
        log.info("Results:\n" + pprint.pformat(res.entries))

.. Example: First part of test_log_arp_results_2().

Notice we eliminate the index arg (by default column zero is considered the
index column), as well as the table_title_pattern argument. Below we show the
logged output from the above code. ::

    Results:
    {'12.12.12.1': {'Address': '12.12.12.1',
                    'Age': '-',
                    'Hardware Addr': '0292.77d4.d5ee',
                    'Interface': 'GigabitEthernet0/0/0/0',
                    'State': 'Interface',
                    'Type': 'ARPA'},
     '12.12.12.2': {'Address': '12.12.12.2',
                    'Age': '00:47:27',
                    'Hardware Addr': '02e9.4522.5326',
                    'Interface': 'GigabitEthernet0/0/0/0',
                    'State': 'Dynamic',
                    'Type': 'ARPA'},
     '13.13.13.1': {'Address': '13.13.13.1',
                    'Age': '-',
                    'Hardware Addr': '02b7.a23a.e076',
                    'Interface': 'GigabitEthernet0/0/0/1',
                    'State': 'Interface',
                    'Type': 'ARPA'},
     '13.13.13.2': {'Address': '13.13.13.2',
                    'Age': '00:47:27',
                    'Hardware Addr': '02db.ebba.ecc4',
                    'Interface': 'GigabitEthernet0/0/0/1',
                    'State': 'Dynamic',
                    'Type': 'ARPA'}}
    TEST 2010-01-22 16:26:41,113: PASS: example_suite_t.test_log_arp_results_2

.. Example: Output from first part of test_log_arp_results_2().

As you can see now we simply have to index using the IP to get at the actual
entry dictionary. So to view the MAC address and interface for IP ``10.10.10.2``
we use the following code. ::

    addr = '10.10.10.2'
    macaddr = res.entries[addr]['Hardware Addr']
    intf = res.entries[addr]['Interface']
    exec_logger.info(twoaddr + " on " + intf + " has MAC addr " + macaddr)

.. Example: Second part of test_log_arp_results_2().

Resulting in the following output::

    10.10.10.2 on GigabitEthernet0/0/0/1 has MAC addr 02db.ebba.ecc4

.. Example: Output from second part of test_log_arp_results_2().

Tabular parsing support for delimited Multi-line header tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Paresergen supports parisng delimited tables with multi-line headers as
illustrated in the below example. ::

    sysadmin-vm:0_RP0# show controller sfe driver rack 0
    Sun Apr  23 21:24:51.773 UTC-07:00

    =========================================================================
    SFE Driver information
    =========================================================================

    Driver Version: 1   (1.1)

    Functional role: Active,   ISSU role: NA
    Rack: 0/RP0, Type: lcc, Number: 0, IP Address: 192.1.0.1
    Startup time       : 2017 Apr 15 04:04:32.117
    Availability Masks :
         Card: 0x1       Asic: 0xF       Exp Asic: 0xF
    Unicast/Multicast (ratio) : 0
    +----------------------------------------------------------------+
    |Process  | Connection | Registration| Connection | DLL          |
    |/Lib     | status     | status      | requests   | registration |
    +----------------------------------------------------------------+
    | PM      |  Active    |  n/a        |           1|  n/a         |
    | PL-LOCAL|  Active    |  Active     |           1|  n/a         |
    | FSDB    |  Active    |  Active     |           1|  n/a         |
    | FGID    |  Active    |  Active     |           1|  n/a         |
    | CM      |  Active    |  Active     |           1|  n/a         |
    | CCC     |  Active    |  n/a        |           1|  n/a         |
    | GASPP   |  n/a       |  n/a        |         n/a|  n/a         |
    | CIH     |  n/a       |  n/a        |         n/a|  Yes         |
    +----------------------------------------------------------------+

    Asics :
    HP - HotPlug event,  PON - Power ON reset,     WB - Warm Boot,  A - All
    HR - Hard Reset,     DC  - Disconnect signal,  DL - DownLoad
    +-----------------------------------------------------------------------------------+
    | Asic inst.|card|HP|Asic| Asic  | Admin|plane| Fgid| Asic State |DC| Last  |PON|HR |
    |  (R/S/A)  |pwrd|  |type| class | /Oper|/grp | DL  |            |  | init  |(#)|(#)|
    +-----------------------------------------------------------------------------------+
    | 0/FC0/0   | UP | 1| s13|  FE1600| UP/UP| 0/0 | DONE| NRML       | 0| PON   |  1|  0|
    | 0/FC0/1   | UP | 1| s13|  FE1600| UP/UP| 0/1 | DONE| NRML       | 0| PON   |  1|  0|
    | 0/FC0/2   | UP | 1| s13|  FE1600| UP/UP| 0/2 | DONE| NRML       | 0| PON   |  1|  0|
    | 0/FC0/3   | UP | 1| s13|  FE1600| UP/UP| 0/3 | DONE| NRML       | 0| PON   |  1|  0|
    +-----------------------------------------------------------------------------------+

.. Example: Delimited multi-header table.

We will parse the second table. We only need to pass the delimiter so
parsergen will be able to identify the table columns borders.

Now for the test code.::

    def test_tabular_parser_12(self):
        result = oper_fill_tabular(device=device1,
                                    show_command="show controller sfe driver rack 0",
                                    refresh_cache=True,
                                    header_fields=
                                    [['Asic inst\.',
                                      'card',
                                      'HP',
                                      'Asic',
                                      'Asic',
                                      'Admin',
                                      'plane',
                                      'Fgid',
                                      'Asic State',
                                      'DC',
                                      'Last',
                                      'PON',
                                      'HR'],
                                    ['\(R/S/A\)',
                                     'pwrd',
                                     '',
                                     'type',
                                     'class',
                                     '/Oper',
                                     '/grp',
                                     'DL',
                                     '',
                                     '',
                                     'init',
                                     '\(#\)',
                                     '\(#\)']],
                                    label_fields=
                                    [ "Asic inst. (R/S/A) ",
                                      "card pwrd",
                                      "HP",
                                      "Asic type",
                                      "Asic class",
                                      "Admin /Oper",
                                      "plane /grp",
                                      "Fgid DL",
                                      "Asic State",
                                      "DC",
                                      "Last init",
                                      "PON State (#)",
                                      "HR (#)" ],
                                    index = [ 0, 12 ],
                                    delimiter = '|')

        log.info("Results:\n" + pprint.pformat(res.entries))

.. Example: Test_tabular_parser_12().

Below we show the parsed output from the above code. ::

    Results:
    {'0/FC0/0': {'Admin /Oper': 'UP/UP',
                 'Asic State': 'NRML',
                 'Asic class': 'FE1600',
                 'Asic inst. (R/S/A) ': '0/FC0/0',
                 'Asic type': 's13',
                 'DC': '0',
                 'Fgid DL': 'DONE',
                 'HP': '1',
                 'HR (#)': '0',
                 'Last init': 'PON',
                 'PON State (#)': '1',
                 'card pwrd': 'UP',
                 'plane /grp': '0/0'},
     '0/FC0/1': {'Admin /Oper': 'UP/UP',
                 'Asic State': 'NRML',
                 'Asic class': 'FE1600',
                 'Asic inst. (R/S/A) ': '0/FC0/1',
                 'Asic type': 's13',
                 'DC': '0',
                 'Fgid DL': 'DONE',
                 'HP': '1',
                 'HR (#)': '0',
                 'Last init': 'PON',
                 'PON State (#)': '1',
                 'card pwrd': 'UP',
                 'plane /grp': '0/1'},
     '0/FC0/2': {'Admin /Oper': 'UP/UP',
                 'Asic State': 'NRML',
                 'Asic class': 'FE1600',
                 'Asic inst. (R/S/A) ': '0/FC0/2',
                 'Asic type': 's13',
                 'DC': '0',
                 'Fgid DL': 'DONE',
                 'HP': '1',
                 'HR (#)': '0',
                 'Last init': 'PON',
                 'PON State (#)': '1',
                 'card pwrd': 'UP',
                 'plane /grp': '0/2'},
     '0/FC0/3': {'Admin /Oper': 'UP/UP',
                 'Asic State': 'NRML',
                 'Asic class': 'FE1600',
                 'Asic inst. (R/S/A) ': '0/FC0/3',
                 'Asic type': 's13',
                 'DC': '0',
                 'Fgid DL': 'DONE',
                 'HP': '1',
                 'HR (#)': '0',
                 'Last init': 'PON',
                 'PON State (#)': '1',
                 'card pwrd': 'UP',
                 'plane /grp': '0/3'}}

Parse using device output
-------------------------

``Parsergen`` now supports working without passing the device as an argument,
user can pass the device output (as a string) along with the `OS` (for
abstraction purpose) instead.

.. code-block:: python

    def test_non_tabular_parser(self):

        """
            Test non tabular parser when passing a device output
            and device os only and compare against selected tags.
        """

        pure_cli = dedent(self.showCommandOutput1)

        attrValPairsToCheck = [
            ('show.intf.if_name',                       'MgmtEth0/0/CPU0/0'),
            ('show.intf.line_protocol',                 'up'),
            ('show.intf.ip_address',                    '10.30.108.132'),
            ('show.intf.mtu',                           1514),
            ('show.intf.admin_state',                   'up'),
        ]

        device_os = 'iosxr'

        pgcheck = oper_check (
                    attrvalpairs = attrValPairsToCheck,
                    show_command = \
                        ('show_interface_<WORD>', [], {'ifname':'MgmtEth0/0/CPU0/0'}),
                    refresh_cache=True,
                    device_output = pure_cli,
                    device_os = device_os)

        result = pgcheck.parse()
        self.assertTrue(result)
        self.assertEqual(parsergen.ext_dictio['device_name'], self.outputDict2)

.. code-block:: python

    def test_tabular_parser(self):

        """
            Test tabular parser when passing a device output
            and device os only.
        """

        pure_cli='''
            Interface              IP-Address      OK? Method Status                Protocol
            GigabitEthernet0/0     10.1.10.20      YES NVRAM  up                    up
            GigabitEthernet1/0/1   unassigned      YES unset  up                    up
            GigabitEthernet1/0/10  unassigned      YES unset  down                  down
        '''
        device_os = 'iosxe'

        res = parsergen.oper_fill_tabular(header_fields=
                                            [ "Interface",
                                              "IP-Address",
                                              "OK\?",
                                              "Method",
                                              "Status",
                                              "Protocol" ],
                                          label_fields=
                                            [ "Interface",
                                              "IP-Address",
                                              "OK?",
                                              "Method",
                                              "Status",
                                              "Protocol" ],
                                          index=[ 0, 5 ],
                                          device_output = pure_cli,
                                          device_os = device_os)

        self.assertEqual(res.entries, outputDict4)

        outputDict4 = {
            'GigabitEthernet0/0':
                {'up':
                    {'IP-Address': '10.1.10.20',
                     'Interface': 'GigabitEthernet0/0',
                     'Method': 'NVRAM',
                     'OK?': 'YES',
                     'Protocol': 'up',
                     'Status': 'up'}},
            'GigabitEthernet1/0/1':
                {'up':
                    {'IP-Address': 'unassigned',
                     'Interface': 'GigabitEthernet1/0/1',
                     'Method': 'unset',
                     'OK?': 'YES',
                     'Protocol': 'up',
                     'Status': 'up'}},
            'GigabitEthernet1/0/10':
                {'down':
                    {'IP-Address': 'unassigned',
                     'Interface': 'GigabitEthernet1/0/10',
                     'Method': 'unset',
                     'OK?': 'YES',
                     'Protocol': 'down',
                     'Status': 'down'}}}

.. note::
    Here is the list of the supported OSes: 
    [ 'ios', 'iosxr', 'iosxe', 'nxos', 'calvados', 'iox',
      'pix', 'asa', 'sanos', 'dcos', 'aireos', 'linux' ]