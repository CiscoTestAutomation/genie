..
.. December 2010, Stefano Ferrari
.. December 16 2012, Christian Hopps <chopps@cisco.com>
.. February 13 2015, Myles Dear <mdear@cisco.com>
..
.. Copyright (c) 2012-2015 by cisco Systems, Inc.
.. All rights reserved.
..

.. _core_markup:

Core documentation
==================

*************
Markup Syntax
*************

CLI output parsing rules may be specified using a marked-up text input that is 
divided into ``OS`` sections and then further subdivided into 3-5 sub-sections.
By default, the supported ``OS`` values are : 
``IOX``, ``IOS``, ``NXOS`` and ``LINUX``.  
The supported sub-subsections are ``CMD``, ``SHOWCMD``, ``PREFIX``, ``ACTUAL``
and ``MARKUP``. The ``ACTUAL`` subsection is optional and is used to simply 
store the unmarked up raw show output.  

An example of a simple marked-up file is as follows::

  OS: NXOS
  CMD: SHOW_MRIB_ROUTE
  SHOWCMD: show ip mroute
  PREFIX: mrib-route
  ACTUAL:

  (13.13.13.4/32, 232.0.0.1/32), uptime: 00:00:43, igmp pim ip
    Incoming interface: Ethernet2/1, RPF nbr: 11.11.11.2^M
    Outgoing interface list: (count: 1)^M
      Ethernet2/2, uptime: 00:00:43, igmp^M

  MARKUP:
  (XP<source>X13.13.13.4/32, XP<group>X232.0.0.1/32), uptime: XT<uptime>X00:00:43, 
    XR<protos>Xigmp pim ip
    Incoming interface: XI<ingress-intf>XEthernet2/1, RPF nbr: XA<rpf>X11.11.11.2
    Outgoing interface list: (count: XN<egress-count>X1)
      XI<egress-intf>XEthernet2/2, uptime: XT<egress-uptime>X00:00:43, XR<egress-protos>Xigmp

The above is used to tell :mod:`core` the details of how to go 
about parsing the ``show ip mroute`` command on a NXOS router.

.. _markup-os-section-index:

The ``OS`` Section
^^^^^^^^^^^^^^^^^^

Multiple OS architectures are supported. The ``OS`` section tells 
:mod:`core` which OS the following show commands (and their 
resulting `regular expressions<re>`) are for. The currently supported operating
systems are ``IOS``, ``IOX``, ``NXOS`` and ``LINUX``.

.. _markup-cmd-section-index:

The ``CMD`` Sub-Section
^^^^^^^^^^^^^^^^^^^^^^^

The ``CMD`` section is a single line that records the symbolic name for the
show command, this name is passed to :mod:`core` so that it can 
look up the correct actual show command for the given ``OS``. If this section 
is not specified then it will be created by uppercasing the ``SHOWCMD`` value 
and converting spaces and dashes to underscores.

.. _markup-showcmd-section-index:

The ``SHOWCMD`` Sub-Section
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``SHOWCMD`` section is a single line that records the show command that
generated the output that will follow.

.. _markup-prefix-section-index:

The ``PREFIX`` Sub-Section
^^^^^^^^^^^^^^^^^^^^^^^^^^

The prefix section indicates the prefix that should be used to identify all
regular expressions when accessing :mod:`core` parsing classes.


.. _markup-actual-section-index:

The ``ACTUAL`` Sub-Section
^^^^^^^^^^^^^^^^^^^^^^^^^^

One typically copies and pastes the output from a show command into the 
``ACTUAL`` section, which is simply a place to keep an unmodified copy of the 
show command output.

.. _markup-markup-section-index:

The ``MARKUP`` Sub-Section
^^^^^^^^^^^^^^^^^^^^^^^^^^

One typically copies the ``ACTUAL`` output into the ``MARKUP`` section and then
uses an ``XxX`` or ``Xx<name>X`` notation to tell :mod:`core` what type 
of value follows.  The markup notation allows for instructing 
:mod:`core` what to name the value as well. If the name is omitted then 
:mod:`core` takes a guess as to the name by using text immediately before or after the value.  A warning is generated if duplicate names are detected.

The following are the available values for ``x`` in the ``XxX`` notation:

- A - IPv4 or IPv6 address.
- B - Value terminated with a close brace, bracket, or parenthesis.
- C - Value terminated with a comma.
- F - Floating point number.
- H - Hexidecimal number.
- I - Interface name.
- M - Mac address.
- N - Decimal number.
- R - everything else to the newline.
- P - IPv4 or IPv6 prefix.
- Q - Value terminated by a double quote.
- S - Non-space value.
- T - Time (00:00:00)
- W - A word.

.. note::  Additionally if one uses lower case rather than upper case for ``x``
    then the value is matched with a regular expression but no tag is 
    created.  This allows for specifying a single line multiple times in order
    to omit various values that may only optionally be present. 

For example consider if the ``uptime`` and ``protos`` values were optional in 
the output from ``show ip mroute`` on ``NXOS``::

  (XP<source>X13.13.13.4/32, XP<group>X232.0.0.1/32)
  (Xp<source>X13.13.13.4/32, Xp<group>X232.0.0.1/32), uptime: XT<uptime>X00:00:43
  (Xp<source>X13.13.13.4/32, Xp<group>X232.0.0.1/32), uptime: Xt<uptime>X00:00:43, 
  XR<protos>Xigmp pim ip

This generates the following dictionary output::

  'mrib-route.source': '\(([A-Fa-f0-9/:\.]+),\s+[A-Fa-f0-9/:\.]+\)',
  'mrib-route.group' : '\([A-Fa-f0-9/:\.]+,\s+([A-Fa-f0-9/:\.]+)\)',
  'mrib-route.uptime': '\([A-Fa-f0-9/:\.]+,\s+[A-Fa-f0-9/:\.]+\), 
    uptime:\s+(\d{2}:\d{2}:\d{2})',
  'mrib-route.protos': '\([A-Fa-f0-9/:\.]+,\s+[A-Fa-f0-9/:\.]+\), 
    uptime:\s+\d{2}:\d{2}:\d{2},\s+([^\r\n]+)',

You can see above that ``uptime`` and ``protos`` are not present on the first 
and second lines because they do not need to be present for ``source`` or 
``group`` to match. 

A second markup notation which allows for specifying the exact regex to parse 
the value is allowed for cases where none of the above predefined value types
works. This notation takes the form ``XXX<regex>XXX`` or
``XXX<regex><name>XXX``. So using this notation in place of XSX would look like
this::

  XXX<\S+>XXXsome-non-space-value-to-parse

.. note::
    Manual regex specification via ``XXX`` does not support the use of the
    repetition operators {m} and {m, n}.


.. _core_example:

Parsing Example
---------------

The following example shows how a user can specify marked-up text, and then
use :mod:`core` to parse both tabular and non-tabular elements in
a piece of show command output:

Sample Parsing Script
^^^^^^^^^^^^^^^^^^^^^

The following script illustrates the parsing of show command output that
contains both tabular and non-tabular content.  It also shows the automatic
validation of non-tabular content.  Notice the use of a tuple in the
**values** field to indicate multiple acceptable matches.  Notice also that
in the cases where the user does not specify the field name, a name is
automatically chosen based on surrounding text(``table-id``)::

    bgp_summ_actual_output="""
    BGP router identifier 192.168.0.12, local AS number 100
    BGP generic scan interval 60 secs
    BGP table state: Active
    Table ID: 0xe0000000   RD version: 8
    BGP main routing table version 8
    BGP scan interval 60 secs

    BGP is operating in STANDALONE mode.

    Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
    Speaker               8          8          8          8           8           8

    Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
    50.1.0.2          0   100      63      55        8    0    0 00:51:24        100
    50.1.0.3          0   200      63      55        8    0    0 00:40:16        200
    """

    bgp_summ_marked_up_output="""
    OS: IOX
    CMD: BGP_SUMMARY
    SHOWCMD: show bgp summary
    PREFIX: bgp

    MARKUP:

    BGP router identifier XA<router-id>X192.168.0.12, local AS number XN<local-as>X100
    BGP generic scan interval XN<gen-scan-interval>X60 secs
    BGP table state: XW<table-state>XActive
    Table ID: XHX0xe0000000   RD version: 8
    BGP main routing table version 8
    BGP scan interval XN<scan-interval>X60 secs

    BGP is operating in XW<oper-mode>XSTANDALONE mode.

    Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
    Speaker               8          8          8          8           8           8

    Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
    50.1.0.2          0   100      63      55        8    0    0 00:51:24        100
    50.1.0.3          0   200      63      55        8    0    0 00:40:16        200
    """
    #
    # Parse non-tabular data
    #
    from genie.parsergen.core import extend_markup
    extend_markup(bgp_summ_marked_up_output)

    from genie.parsergen.core import _parser_gen_t
    from genie.parsergen import core
    parse_key = 'rtr1'
    parsergen.core.text_to_parse[parse_key] = bgp_summ_actual_output

    print ("Parsing CLI show command output: ...")
    tags_to_parse =     [
                         'bgp.local-as',             (100, 101),
                         'bgp.router-id',            None,
                         'bgp.gen-scan-interval',    None,
                         'bgp.table-state',          None,
                         'bgp.table-id',             None,
                         'bgp.scan-interval',        None,
                         'bgp.oper-mode',            None]
    pg = _parser_gen_t('IOX', tags_to_parse[::2], tags_to_parse[1::2], fill = True,
                       parse_key=parse_key)
    (validate, dictio, msg) = pg._parser_validate()
    print("     Parser's fill report :\n          validate={}," + 
          " \n          dictio={}, \n          msg={}\n".
        format(validate, dictio, msg))
    parsed_output = parsergen.core.ext_dictio[parse_key]

    #
    # Parse tabular data
    #
    from genie.parsergen.core import column_table_result_core_t
    header = ['Neighbor', 'Spk', 'AS', 'MsgRcvd', 'MsgSent', 
              'TblVer', 'InQ', 'OutQ', 'Up/Down', 'St/PfxRcd']
    labels = ['neighbor', 'spk', 'as', 'msg_rcvd', 'msg_sent' ,
              'tbl_ver', 'in_q', 'out_q', 'time', 'prefixes']
    tabular_parse_result = column_table_result_core_t(
                                header, label_fields=labels, index=[0,2], 
                                right_justified=True, parse_key=parse_key);
    parsed_output['bgp.neighbor-table'] = tabular_parse_result.entries

    print ("CLI parse results for combination tabular/non-tabular data:")
    import pprint
    pprint.pprint(parsed_output, indent=5)

    print ("\n\nTesting COMPARE mode for non-tabular data: ...")

    tags_to_parse =     [
                         'bgp.local-as',             (100,101),
                         'bgp.router-id',            '192.168.0.12',
                         'bgp.gen-scan-interval',    60,
                         'bgp.table-state',          'Active',
                         'bgp.table-id',             '0xe0000000',
                         'bgp.scan-interval',        60,
                         'bgp.oper-mode',            'STANDALONE']
    pg = _parser_gen_t('IOX', tags_to_parse[::2], tags_to_parse[1::2], 
            fill = False, parse_key=parse_key)
    (validate, dictio, msg) = pg._parser_validate()

    print("     Expected parser output     :\n      {}\n".format(tags_to_parse))
    print("     Actual parser output       :\n      {}\n".format(parsergen.core.ext_dictio[parse_key]))
    print("     Parser's comparison report :\n      validate={}," + 
        " \n          dictio={}, \n          msg={}\n".
        format(validate, dictio, msg))

.. _core-non-tabular-parser-subclass-example:

Use of Subclassing with the Tabular Parser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A subclass can define a class dictionary variable ``field_mapping``
whose keys are field names and whose value is the type of that
field. When the results are parsed the value is cast to the given
type.  Values can also take the form of a generic mapping function.

A subclass can define a class list variable ``table_title_mapping``
which is a list of mapping functions for table title value keys.
If specified, this list has an entry for each matching group present in
`table_title_pattern`.

A subclass can also override the function ``cleanup_entry_field`` to
cleanup a field value prior to it being stored. This is called prior
to the mapping being done.

`Sub-class Example`::

    from genie.parsergen import core
    parse_key = ''
    core.text_to_parse[parse_key]  = '''
    RP/0/0/CPU0:iox#show isis database
    Wed Dec 16 09:48:55.017 EST

    IS-IS ring (Level-1) Link State Database
    LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime  ATT/P/OL
    iox.00-00           * 0x00000008   0xf9fd        1003            0/0/0
    ioxbfd.00-00          0x00000004   0x8f36        862             0/0/0

    Total Level-1 LSP count: 4     Local Level-1 LSP count: 1

    IS-IS ring (Level-2) Link State Database
    LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime  ATT/P/OL
    iox.00-00           * 0x00000009   0x351a        1003            0/0/0
    iox.01-00             0x00000002   0x0ead        922             0/0/0

    Total Level-2 LSP count: 4     Local Level-2 LSP count: 1
    '''

    def _hexint (val):
        return int(val, 16)

    def cleanupLspId (field):
        return field

    from core import column_table_result_core_t

    class my_isis_database_column_parser_t (column_table_result_core_t):
        field_mapping = {
            'LSPID'       :   str,   
            'LSP Seq Num' :   _hexint,
            'LSP Checksum':   _hexint,
            'LSP Holdtime':   None,
            }

        table_title_mapping = [ int ]

        def __init__ (self):
            headers = ["LSPID", "LSP Seq Num", "LSP Checksum", 
            "LSP Holdtime",  "ATT/P/OL"]
            labels = headers

            column_table_result_core_t.__init__(
             self, 
             headers,
             "Total Level-[12] LSP count:",
             table_title_pattern = 
             r"IS-IS (?:[-\w]+ )?\(?Level-([12])\)? Link State Database:?",
             label_fields = labels)

        def cleanup_entry_field (self, header, field):
            if header == "LSPID":
                # Strip the "*" off the LSPID for the router's own LSPID.
                return cleanupLspId(field)
            else:
                return field

    result = my_isis_database_column_parser_t()
    print (result.entries[2]['iox.01-00']['LSP Holdtime'])
    922
