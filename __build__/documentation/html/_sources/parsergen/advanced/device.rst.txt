Parse using device output
=========================
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