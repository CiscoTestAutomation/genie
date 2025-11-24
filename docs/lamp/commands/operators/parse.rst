parse
=====

The ``parse`` command parses a command on the device loaded in LAMP
shell using Genieparser and automatically generates a pyATS Blitz 
*'parse'* action snippet.

.. note::

   For more information on Genieparsers, refer to Genie's
   `Parser documentation <https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/parsers.html#>`_.

Why use parse
-------------
The ``parse`` command provides significant advantages over the 
``execute`` command for verifying command outputs:

* **Speed and Efficiency**: Parsing outputs is faster than using the 
  ``execute`` command with regex patterns.

* **Maintainability**: Regular expression (regex) patterns for checking 
  outputs are complex, difficult to maintain, and hard to understand.

* **Accuracy**: Parsed dictionary structures provide more precise 
  verification capabilities compared to regex pattern matching.

* **Reliability**: Dictionary-based verification offers better accuracy 
  and faster processing than traditional regex approaches.

Basic usage
------------

To parse any command, provide the command as arguments to ``parse``.
The system displays both the command execution output from the device 
console and the parsed dictionary output on the terminal screen.

Example:

.. code-block:: console

   (lamp-host1) parse show ip route
   2024-07-28 10:09:58: %LAMP-INFO: +..............................................................................+
   2024-07-28 10:09:58: %LAMP-INFO: :                       Parse 'show ip route' on 'host1'                       :
   2024-07-28 10:09:58: %LAMP-INFO: +..............................................................................+
   
   2024-07-28 10:09:58,684: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ip route' +++
   show ip route
   Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
          D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
          N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
          E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
          n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
          i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
          ia - IS-IS inter area, * - candidate default, U - per-user static route
          H - NHRP, G - NHRP registered, g - NHRP registration summary
          o - ODR, P - periodic downloaded static route, l - LISP
          a - application route
          + - replicated route, % - next hop override, p - overrides from PfR
          & - replicated local route overrides by connected
   
   Gateway of last resort is not set
   
         1.0.0.0/32 is subnetted, 1 subnets
   C        1.1.1.1 is directly connected, Loopback0
   host1#
   2024-07-28 10:09:58: %LAMP-INFO: +..............................................................................+
   2024-07-28 10:09:58: %LAMP-INFO: :                                Parse output:                                 :
   2024-07-28 10:09:58: %LAMP-INFO: +..............................................................................+
                                     {
                                       'vrf': {
                                         'default': {
                                           'address_family': {
                                             'ipv4': {
                                               'routes': {
                                                 '1.1.1.1/32': {
                                                   'route': '1.1.1.1/32'
                                                   'active': True
                                                   'source_protocol_codes': 'C'
                                                   'source_protocol': 'connected'
                                                   'next_hop': {
                                                     'outgoing_interface': {
                                                       'Loopback0': {
                                                         'outgoing_interface': 'Loopback0'
                                                       }
                                                     }
                                                   }
                                                 }
                                               }
                                             }
                                           }
                                         }
                                       }
                                     }
   2024-07-28 10:09:58: %LAMP-INFO: +..............................................................................+
   (lamp-host1)

LAMP automatically generates the Blitz *'parse'* action snippet as shown below:

.. code-block:: console

   (lamp-host1) list 1
   parse:
     device: host1
     command: show ip route

Include entries
---------------

An *include* entry in a ``parse`` command verifies whether specific 
data is present in the parsed output dictionary. This verification 
uses a Dq query format. For detailed information on Dq, refer to the
`Dq documentation <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_.

To add an *include* entry, use ``parse -i <CMD>``. This command 
prompts for the *include* entries after displaying the parsed 
dictionary output on the terminal.

A detailed example for an *include* entry with Dq query follows:

Given parse dictionary output:

.. code-block:: python

    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }

The Dq query to verify if the route '1.1.1.1/32' is from 
interface 'Loopback0' would be:

.. code-block:: python

   contains('1.1.1.1/32').contains_key_value('outgoing_interface', 'Loopback0')

Adding this Dq query as an *include* entry to the Blitz action 
verifies the query against the parsed output dictionary and adds it 
to the Blitz action's *'include'* field as shown below:

.. code-block:: console

    (lamp-host1) parse -i show ip route
    2025-08-27 12:11:46: %LAMP-INFO: +..............................................................................+
    2025-08-27 12:11:46: %LAMP-INFO: :                       Parse 'show ip route' on 'host1'                       :
    2025-08-27 12:11:46: %LAMP-INFO: +..............................................................................+

    2025-08-27 12:11:46,692: %UNICON-INFO: +++ host1 with via 'cli': executing command 'show ip route' +++
    show ip route
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
           n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
           i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, * - candidate default, U - per-user static route
           H - NHRP, G - NHRP registered, g - NHRP registration summary
           o - ODR, P - periodic downloaded static route, l - LISP
           a - application route
           + - replicated route, % - next hop override, p - overrides from PfR
           & - replicated local route overrides by connected

    Gateway of last resort is not set

          1.0.0.0/32 is subnetted, 1 subnets
    C        1.1.1.1 is directly connected, Loopback0
    host1#
    2025-08-27 12:11:46: %LAMP-INFO: +..............................................................................+
    2025-08-27 12:11:46: %LAMP-INFO: :                                Parsed output                                 :
    2025-08-27 12:11:46: %LAMP-INFO: +..............................................................................+
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    2025-08-27 12:11:46: %LAMP-INFO: +..............................................................................+
    2025-08-27 12:11:46: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
    2025-08-27 12:11:46: %LAMP-INFO: +..............................................................................+
    ROOT
    └── (1) vrf
        └── (2) default
            └── (3) address_family
                └── (4) ipv4
                    └── (5) routes
                        └── (6) 1.1.1.1/32
                            ├── (7) route: 1.1.1.1/32
                            ├── (8) active: True
                            ├── (9) source_protocol_codes: C
                            ├── (10) source_protocol: connected
                            └── (11) next_hop
                                └── (12) outgoing_interface
                                    └── (13) Loopback0
                                        └── (14) outgoing_interface: Loopback0
    Enter Dq item (or) line numbers (Press enter for multiple entries): contains('1.1.1.1/32').contains_key_value('outgoing_interface', 'Loopback0')
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    Do you wish to add this Dq query (Y/n): 
    (lamp-host1)

When providing a Dq query as an *include* entry, LAMP reconstructs a 
dictionary from the query and displays it for validation before 
accepting it. The reconstructed dictionary represents the actual data 
from the parsed output dictionary that matches the Dq query. If the 
reconstructed dictionary is empty ({}), the query does not match the 
given parse dictionary.

The autogenerated Blitz action snippet for this example appears below:

.. code-block:: console

    (lamp-host1) list 1
      - parse:
          device: host1
          command: show ip route
          include:
            - contains('1.1.1.1/32').contains_key_value('outgoing_interface', 'Loopback0')
    (lamp-host1) 

Multiple Dq queries can be added as *include* entries to verify more 
than one value by pressing <ENTER> when prompted.

Dq query shorthand
^^^^^^^^^^^^^^^^^^

LAMP provides a shorthand syntax as an alternative to typing complete 
Dq queries. The syntax mapping follows this pattern (with multiple 
individual elements separated by ',' similar to '.' in Dq queries):

.. _dq_query_shorthand:

.. list-table:: Shorthand syntax to Dq query mapping
   :widths: 50 50
   :header-rows: 1

   * - Shorthand syntax
     - Dq query
   * - a
     - contains('a')
   * - !a
     - not_contains('a')
   * - a=b
     - contains_key_value('a', 'b')
   * - !a=b
     - not_contains_key_value('a', 'b')
   * - a>1
     - value_operator('a', '>', 1)
   * - +a>1
     - sum_value_operator('a', '>', 1)
   * - g(a) | g(a).x
     - get_values('a') | get_values('a', 'x')
   * - c()
     - count()
   * - r([a][b])
     - raw('[a][b]')

An example highlighting the mapping:

Dq query:

.. code-block:: python

    contains('1.1.1.1/32').contains_key_value('outgoing_interface', 'Loopback0')

Equivalent shorthand:

.. code-block:: console

    1.1.1.1/32,outgoing_interface=Loopback0

Using this shorthand syntax instead of the actual Dq query produces 
the same result in the Blitz action generated by LAMP. The Blitz 
action will still contain the actual Dq query in the *'include'* field 
as shown below:

.. code-block:: console

    (lamp-host1) parse -i show ip route
    2025-08-27 12:21:02: %LAMP-INFO: +..............................................................................+
    2025-08-27 12:21:02: %LAMP-INFO: :                       Parse 'show ip route' on 'host1'                       :
    2025-08-27 12:21:02: %LAMP-INFO: +..............................................................................+

    2025-08-27 12:21:02,834: %UNICON-INFO: +++ host1 with via 'cli': executing command 'show ip route' +++
    show ip route
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
           n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
           i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, * - candidate default, U - per-user static route
           H - NHRP, G - NHRP registered, g - NHRP registration summary
           o - ODR, P - periodic downloaded static route, l - LISP
           a - application route
           + - replicated route, % - next hop override, p - overrides from PfR
           & - replicated local route overrides by connected

    Gateway of last resort is not set

          1.0.0.0/32 is subnetted, 1 subnets
    C        1.1.1.1 is directly connected, Loopback0
    host1#
    2025-08-27 12:21:02: %LAMP-INFO: +..............................................................................+
    2025-08-27 12:21:02: %LAMP-INFO: :                                Parsed output                                 :
    2025-08-27 12:21:02: %LAMP-INFO: +..............................................................................+
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    2025-08-27 12:21:02: %LAMP-INFO: +..............................................................................+
    2025-08-27 12:21:02: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
    2025-08-27 12:21:02: %LAMP-INFO: +..............................................................................+
    ROOT
    └── (1) vrf
        └── (2) default
            └── (3) address_family
                └── (4) ipv4
                    └── (5) routes
                        └── (6) 1.1.1.1/32
                            ├── (7) route: 1.1.1.1/32
                            ├── (8) active: True
                            ├── (9) source_protocol_codes: C
                            ├── (10) source_protocol: connected
                            └── (11) next_hop
                                └── (12) outgoing_interface
                                    └── (13) Loopback0
                                        └── (14) outgoing_interface: Loopback0
    Enter Dq item (or) line numbers (Press enter for multiple entries): 1.1.1.1/32,outgoing_interface=Loopback0
    contains('1.1.1.1/32').contains_key_value('outgoing_interface', 'Loopback0')
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    Do you wish to add this Dq query (Y/n): 
    (lamp-host1) list 1
      - parse:
          device: host1
          command: show ip route
          include:
            - contains('1.1.1.1/32').contains_key_value('outgoing_interface', 'Loopback0')
    (lamp-host1) 

When provided with shorthand syntax for an *include* entry, LAMP 
automatically displays the corresponding Dq query along with the 
reconstructed dictionary output that matches the query.

As observed from the output of ``list 1``, even though shorthand 
syntax was provided, the *'include'* field contains only the 
corresponding actual Dq query.

For values provided in the shorthand that doesn't match any key-value
in the parsed dictionary, LAMP automatically adds the value as a regex
to try and match it.

The example below illustrates this scenario:

.. code-block:: console

    2025-08-27 13:07:00: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:07:00: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
    2025-08-27 13:07:00: %LAMP-INFO: +..............................................................................+
    ROOT
    └── (1) vrf
        └── (2) default
            └── (3) address_family
                └── (4) ipv4
                    └── (5) routes
                        └── (6) 1.1.1.1/32
                            ├── (7) route: 1.1.1.1/32
                            ├── (8) active: True
                            ├── (9) source_protocol_codes: C
                            ├── (10) source_protocol: connected
                            └── (11) next_hop
                                └── (12) outgoing_interface
                                    └── (13) Loopback0
                                        └── (14) outgoing_interface: Loopback0
    Enter Dq item (or) line numbers (Press enter for multiple entries): 1.1.1.1,outgoing_interface=Loopback0
    contains('.*1.1.1.1.*', regex=True).contains_key_value('outgoing_interface', 'Loopback0')
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    Do you wish to add this Dq query (Y/n): 
    (lamp-host1) list 1
      - parse:
          device: host1
          command: show ip route
          include:
            - contains('.*1.1.1.1.*', regex=True).contains_key_value('outgoing_interface', 'Loopback0')
    (lamp-host1) 

As shown above, since '1.1.1.1' does not match exactly any value in the 
output dictionary, LAMP automatically adds the "regex=True" syntax and 
then reconstructs the dictionary output that matches the query. The 
``list 1`` output also reflects the *'include'* field added with a Dq 
query containing regex patterns.

Line numbers
^^^^^^^^^^^^

Since Dq query concepts can be challenging to understand, LAMP also 
provides the *'line number method'* to generate Dq queries based on 
the location of key-value pairs in the dictionary.

When ``parse -i <CMD>`` is invoked, the parse output dictionary 
displays again with every key and value assigned a line number 
starting from 1. To match a particular key or value, simply use the 
corresponding number associated with it.

The following example illustrates this concept:

.. code-block:: console

    2025-08-27 13:07:00: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:07:00: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
    2025-08-27 13:07:00: %LAMP-INFO: +..............................................................................+
    ROOT
    └── (1) vrf
        └── (2) default
            └── (3) address_family
                └── (4) ipv4
                    └── (5) routes
                        └── (6) 1.1.1.1/32
                            ├── (7) route: 1.1.1.1/32
                            ├── (8) active: True
                            ├── (9) source_protocol_codes: C
                            ├── (10) source_protocol: connected
                            └── (11) next_hop
                                └── (12) outgoing_interface
                                    └── (13) Loopback0
                                        └── (14) outgoing_interface: Loopback0

To verify that the route '1.1.1.1/32' contains 'Loopback0' as the 
'outgoing_interface' in the above dictionary output, line number *13* 
(matching 'Loopback0') is sufficient. To provide a line number as an 
*include* entry to LAMP, prefix the number with '#'. The complete 
terminal output for this example is shown below:

.. code-block:: console

    (lamp-host1) parse -i show ip route
    2025-08-27 13:15:24: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:15:24: %LAMP-INFO: :                       Parse 'show ip route' on 'host1'                       :
    2025-08-27 13:15:24: %LAMP-INFO: +..............................................................................+

    2025-08-27 13:15:24,600: %UNICON-INFO: +++ host1 with via 'cli': executing command 'show ip route' +++
    show ip route
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
           n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
           i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, * - candidate default, U - per-user static route
           H - NHRP, G - NHRP registered, g - NHRP registration summary
           o - ODR, P - periodic downloaded static route, l - LISP
           a - application route
           + - replicated route, % - next hop override, p - overrides from PfR
           & - replicated local route overrides by connected

    Gateway of last resort is not set

          1.0.0.0/32 is subnetted, 1 subnets
    C        1.1.1.1 is directly connected, Loopback0
    host1#
    2025-08-27 13:15:24: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:15:24: %LAMP-INFO: :                                Parsed output                                 :
    2025-08-27 13:15:24: %LAMP-INFO: +..............................................................................+
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    2025-08-27 13:15:24: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:15:24: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
    2025-08-27 13:15:24: %LAMP-INFO: +..............................................................................+
    ROOT
    └── (1) vrf
        └── (2) default
            └── (3) address_family
                └── (4) ipv4
                    └── (5) routes
                        └── (6) 1.1.1.1/32
                            ├── (7) route: 1.1.1.1/32
                            ├── (8) active: True
                            ├── (9) source_protocol_codes: C
                            ├── (10) source_protocol: connected
                            └── (11) next_hop
                                └── (12) outgoing_interface
                                    └── (13) Loopback0
                                        └── (14) outgoing_interface: Loopback0
    Enter Dq item (or) line numbers (Press enter for multiple entries): #13
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    Do you wish to add this line number (Y/n): 
    (lamp-host1) list 1
      - parse:
          device: host1
          command: show ip route
          include:
            - 
    contains('Loopback0').contains('outgoing_interface').contains('next_hop').contains('1.1.1.1/32').contains('routes')
    .contains('ipv4').contains('address_family').contains('default').contains('vrf')
    (lamp-host1) 

The corresponding Dq queries derived from line numbers are added as a 
list under the Blitz *'include'* field. Similar to Dq query inputs, 
LAMP reconstructs a dictionary from the query based on the line number 
and presents it for validation before accepting it. The difference 
between these line numbers and a user-provided Dq query is that, since 
the important keys to access the data downstream are unknown, all 
parent keys are included in the Dq query.

To add multiple line numbers to verify multiple key/values 
simultaneously, separate the line numbers with commas:

    * #<line-number-1>,<line-number-2>,...
    * #1,3,5

To add consecutive line numbers instead of typing each one 
individually, use '-' to specify only the start and end of the range:

    * #<line-number-start>-<line-number-end>
    * #13-17
    * #13-17,19

Exclude entries
---------------

*Exclude* entries work the same way as *include* entries, except they 
verify whether a specified Dq query **DOES NOT** match the ``parse`` 
dictionary output. To add *exclude* entries, use ``parse -e <CMD>``. *Exclude* 
entries should also be in the format of Dq queries.

Example:

.. code-block:: console

    (lamp-host1) parse -e show ip route
    2025-08-27 13:20:58: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:20:58: %LAMP-INFO: :                       Parse 'show ip route' on 'host1'                       :
    2025-08-27 13:20:58: %LAMP-INFO: +..............................................................................+

    2025-08-27 13:20:59,189: %UNICON-INFO: +++ host1 with via 'cli': executing command 'show ip route' +++
    show ip route
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
           n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
           i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, * - candidate default, U - per-user static route
           H - NHRP, G - NHRP registered, g - NHRP registration summary
           o - ODR, P - periodic downloaded static route, l - LISP
           a - application route
           + - replicated route, % - next hop override, p - overrides from PfR
           & - replicated local route overrides by connected

    Gateway of last resort is not set

          1.0.0.0/32 is subnetted, 1 subnets
    C        1.1.1.1 is directly connected, Loopback0
    host1#
    2025-08-27 13:20:59: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:20:59: %LAMP-INFO: :                                Parsed output                                 :
    2025-08-27 13:20:59: %LAMP-INFO: +..............................................................................+
    {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'active': True,
                                'source_protocol_codes': 'C',
                                'source_protocol': 'connected',
                                'next_hop': {
                                    'outgoing_interface': {'Loopback0': {'outgoing_interface': 'Loopback0'}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    2025-08-27 13:20:59: %LAMP-INFO: +..............................................................................+
    2025-08-27 13:20:59: %LAMP-INFO: :                          Collecting EXCLUDE Entries                          :
    2025-08-27 13:20:59: %LAMP-INFO: +..............................................................................+
    Enter Dq item (Press enter for multiple entries): contains('2.2.2.2/32')
    {}
    Do you wish to add this Dq query (Y/n): 
    (lamp-host1)

Since '2.2.2.2/32' does not match the above dictionary output, the 
reconstructed dictionary returns an empty dictionary ({}) which is the 
expected result for an *exclude* entry. A non-empty dictionary raises 
an error with LAMP prompting to double-check the Dq query before 
adding it.

Shorthand syntax can also be used instead of Dq queries in *exclude* 
entries.