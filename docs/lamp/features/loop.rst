Loop
=====

Every LAMP operator command takes an argument to do a basic task.
Loops can help simplify multiple calls for the same command with different arguments.

Basic usage
-----------

'$' is the loop operator. '$' can be appended over multiple arguments separated by ','
to pass them as a single argument to an operator command.

In an abstract sense,

``<command> <arg1>``
``<command> <arg2>``
``<command> <arg3>``

would become

``<command> $<arg1>,<arg2>,<arg3>``

Device looping
--------------

By specifying multiple device names(separated by ',') with '$' prepended to them, users can
perform any operator command such as ``execute`` on multiple devices.

Example:

.. code-block:: console

   (lamp-host1) device $host1,host2
   (lamp-host1,host2)
   (lamp-host1,host2) execute debug ip mrouting
   2024-08-01 10:23:49: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 10:23:49: %LAMP-INFO: :                            Execute loop, length=2                            :
   2024-08-01 10:23:49: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 10:23:49: %LAMP-INFO: +..............................................................................+
   2024-08-01 10:23:49: %LAMP-INFO: :                    Execute 'debug ip mrouting' on 'host1'                    :
   2024-08-01 10:23:49: %LAMP-INFO: +..............................................................................+

   2024-08-01 10:23:49,982: %UNICON-INFO: +++ host1 with via 'a': executing command 'debug ip mrouting' +++
   debug ip mrouting
   IP multicast routing debugging is on
   host1#
   2024-08-01 10:23:50: %LAMP-INFO: +..............................................................................+
   2024-08-01 10:23:50: %LAMP-INFO: :                    Execute 'debug ip mrouting' on 'host2'                    :
   2024-08-01 10:23:50: %LAMP-INFO: +..............................................................................+

   2024-08-01 10:23:50,332: %UNICON-INFO: +++ host2 with via 'a': executing command 'debug ip mrouting' +++
   debug ip mrouting
   IP multicast routing debugging is on
   host2#
   (lamp-host1,host2)

Notice that the prompt updates to show both devices, indicating that all subsequent
actions will be performed on both devices. Additionally, 'LAMP-INFO' messages always display
the loop length, providing clear feedback on the number of iterations.

LAMP generates a pyATS Blitz 'loop' action for device looping as shown below
for the above example:

.. code-block:: console

   (lamp-host1,host2) list 1
   - loop:
         loop_variable_name:
         - dev
         value:
         - [host1, host2]
         actions:
         - execute:
               device: '%VARIABLES{dev}'
               command: debug ip mrouting

Command looping
---------------

One can loop multiple commands by using '$' with a list of commands separated by ','.

Example:

.. code-block:: console

   (lamp-host1) execute $show ip route,show ipv6 route
   2024-08-01 11:42:51: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 11:42:51: %LAMP-INFO: :                            Execute loop, length=2                            :
   2024-08-01 11:42:51: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 11:42:51: %LAMP-INFO: +..............................................................................+
   2024-08-01 11:42:51: %LAMP-INFO: :                      Execute 'show ip route' on 'host1'                      :
   2024-08-01 11:42:51: %LAMP-INFO: +..............................................................................+

   2024-08-01 11:42:51,352: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ip route' +++
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
   2024-08-01 11:42:51: %LAMP-INFO: +..............................................................................+
   2024-08-01 11:42:51: %LAMP-INFO: :                     Execute 'show ipv6 route' on 'host1'                     :
   2024-08-01 11:42:51: %LAMP-INFO: +..............................................................................+

   2024-08-01 11:42:51,600: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ipv6 route' +++
   show ipv6 route
   host1#
   (lamp-host1)

To simplify this further, notice that the difference between the 2 commands
were only at the keywords 'ip' and 'ipv6'. Hence, the command could be reduced
to ``execute show $(ip,ipv6) route`` with parenthesis emphasizing the start and end
of the loop argument, with the values outside the parenthesis being the same
across all loop iterations.

As seen below, the minimalized command indeed invoked both the commands:

.. code-block:: console

   (lamp-host1) execute show $(ip,ipv6) route
   2024-08-01 11:54:29: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 11:54:29: %LAMP-INFO: :                            Execute loop, length=2                            :
   2024-08-01 11:54:29: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 11:54:29: %LAMP-INFO: +..............................................................................+
   2024-08-01 11:54:29: %LAMP-INFO: :                      Execute 'show ip route' on 'host1'                      :
   2024-08-01 11:54:29: %LAMP-INFO: +..............................................................................+

   2024-08-01 11:54:29,404: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ip route' +++
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
   2024-08-01 11:54:29: %LAMP-INFO: +..............................................................................+
   2024-08-01 11:54:29: %LAMP-INFO: :                     Execute 'show ipv6 route' on 'host1'                     :
   2024-08-01 11:54:29: %LAMP-INFO: +..............................................................................+

   2024-08-01 11:54:29,695: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ipv6 route' +++
   show ipv6 route
   host1#
   (lamp-host1)

Consider a more complex example consisting of 6 commands:

   * show ip mroute
   * show ip mfib
   * show ip mrib route
   * show ipv6 mroute
   * show ipv6 mfib
   * show ipv6 mrib route

All these commands would take 6 times to invoke separately, but considering the
similarities between all of them, loops can help simplify the process.

First, separate the IPv4 from IPv6 and try looping the IPv4 alone,
with IPv6 being invoked separately.

   * $show ip mroute,show ip mfib,show ip mrib route
   * $show ipv6 mroute,show ipv6 mfib,show ipv6 mrib route

Minimalizing the above 2 commands above using parenthesis:

   * show ip $(mroute,mfib,mrib route)
   * show ipv6 $(mroute,mfib,mrib route)

When using the '$' notation, the entire loop argument could be seen
identical to a string to further consider the possibility of multiple loops.
Let XXX represent $(mroute,mfib,mrib route). Now, the 2 commands become:

   * show ip XXX
   * show ipv6 XXX

Using normal loop principles from earlier, another loop could be created:

   * show $(ip,ipv6) XXX

Finally, substituting XXX brings us to a double loop:

   * show $(ip,ipv6) $(mroute,mfib,mrib route)

The result of 2 '$' and 2 hence loops would be the 'product' akin to a cartesian
product with (A,B) * (C,D) -> AC, AD, BC, BD. The length of the loop would be the
product of number of items in each loop; with the earlier example having 2 * 3 = 6 iterations
which is equal to the total number of required commands.

.. code-block:: console

   (lamp-host1) execute show $(ip,ipv6) $(mroute,mfib,mrib route)
   2024-08-01 12:02:58: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 12:02:58: %LAMP-INFO: :                            Execute loop, length=6                            :
   2024-08-01 12:02:58: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 12:02:58: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:02:58: %LAMP-INFO: :                     Execute 'show ip mroute' on 'host1'                      :
   2024-08-01 12:02:58: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:02:59: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:02:59: %LAMP-INFO: :                      Execute 'show ip mfib' on 'host1'                       :
   2024-08-01 12:02:59: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:02:59: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:02:59: %LAMP-INFO: :                   Execute 'show ip mrib route' on 'host1'                    :
   2024-08-01 12:02:59: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:02:59: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:02:59: %LAMP-INFO: :                    Execute 'show ipv6 mroute' on 'host1'                     :
   2024-08-01 12:02:59: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:03:00: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:03:00: %LAMP-INFO: :                     Execute 'show ipv6 mfib' on 'host1'                      :
   2024-08-01 12:03:00: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:03:00: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:03:00: %LAMP-INFO: :                  Execute 'show ipv6 mrib route' on 'host1'                   :
   2024-08-01 12:03:00: %LAMP-INFO: +..............................................................................+

   2024-08-01 12:03:00,559: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ipv6 mrib route' +++
   show ipv6 mrib route
   No matching routes in MRIB route-DB

   host1#
   (lamp-host1)

The same product rule applies when there is both command looping as well as device looping.

Consider a device loop across 2 devices:

   * device $host1,host2

Consider a command loop with 3 commands:

   * show ip $(mroute,mfib,mrib route)

The result of applying both loops would eventually create a loop of length (2 * 3 = 6)
with the 3 commands first applied on device 'host1' and then on 'host2':

.. code-block:: console

   (lamp-host1) device $host1,host2
   (lamp-host1,host2) execute show ip $(mroute,mfib,mrib route)
   2024-08-01 12:10:43: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 12:10:43: %LAMP-INFO: :                            Execute loop, length=6                            :
   2024-08-01 12:10:43: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 12:10:43: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:10:43: %LAMP-INFO: :                     Execute 'show ip mroute' on 'host1'                      :
   2024-08-01 12:10:43: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:10:43: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:10:43: %LAMP-INFO: :                      Execute 'show ip mfib' on 'host1'                       :
   2024-08-01 12:10:43: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:10:44: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:10:44: %LAMP-INFO: :                   Execute 'show ip mrib route' on 'host1'                    :
   2024-08-01 12:10:44: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:10:44: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:10:44: %LAMP-INFO: :                     Execute 'show ip mroute' on 'host2'                      :
   2024-08-01 12:10:44: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:10:44: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:10:44: %LAMP-INFO: :                      Execute 'show ip mfib' on 'host2'                       :
   2024-08-01 12:10:44: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2024-08-01 12:10:45: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:10:45: %LAMP-INFO: :                   Execute 'show ip mrib route' on 'host2'                    :
   2024-08-01 12:10:45: %LAMP-INFO: +..............................................................................+

   2024-08-01 12:10:45,150: %UNICON-INFO: +++ host2 with via 'a': executing command 'show ip mrib route' +++
   show ip mrib route
   No matching routes in MRIB route-DB

   host2#
   (lamp-host1,host2)

Consider an example to loop different commands for two devices as follows:

   * host1: show ip route 1.1.1.1
   * host2: show ip route 2.2.2.2

There should be a device loop but the command needs to be modified based on the device
currently in iteration. To modify existing loop iteration values, use $[]:

   * $host1,host2: $[show ip route 1.1.1.1,show ip route 2.2.2.2]

The above command can be simplified to:

   * $host1,host2: show ip route $[1.1.1.1,2.2.2.2]

.. code-block:: console

   (lamp-host1,host2) execute show ip route $[1.1.1.1,2.2.2.2]
   2024-08-01 12:26:39: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 12:26:39: %LAMP-INFO: :                            Execute loop, length=2                            :
   2024-08-01 12:26:39: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-08-01 12:26:39: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:26:39: %LAMP-INFO: :                  Execute 'show ip route 1.1.1.1' on 'host1'                  :
   2024-08-01 12:26:39: %LAMP-INFO: +..............................................................................+

   2024-08-01 12:26:39,793: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ip route 1.1.1.1' +++
   show ip route 1.1.1.1
   Routing entry for 1.1.1.1/32
     Known via "connected", distance 0, metric 0 (connected, via interface)
     Routing Descriptor Blocks:
     * directly connected, via Loopback0
         Route metric is 0, traffic share count is 1
   host1#
   2024-08-01 12:26:39: %LAMP-INFO: +..............................................................................+
   2024-08-01 12:26:39: %LAMP-INFO: :                  Execute 'show ip route 2.2.2.2' on 'host2'                  :
   2024-08-01 12:26:39: %LAMP-INFO: +..............................................................................+

   2024-08-01 12:26:40,059: %UNICON-INFO: +++ host2 with via 'a': executing command 'show ip route 2.2.2.2' +++
   show ip route 2.2.2.2
   Routing entry for 2.2.2.2/32
     Known via "connected", distance 0, metric 0 (connected, via interface)
     Routing Descriptor Blocks:
     * directly connected, via Loopback1
         Route metric is 0, traffic share count is 1
   host2#
   (lamp-host1,host2)

To modify iteration values of a particular loop in case of multiple loops, mention the
'back-reference' number of the loop to modify in the format $<back_ref_no>[arg1,arg2].
Back reference numbers start from 1 and increment by 1 for each loop starting from the
device loop.

Shown below is an example of a device loop + command loop. To map '225.1.1.1' to 'host1' and
'232.2.2.2' to 'host2', a back-reference of '1' pointing to the device loop is used:

.. code-block:: console

   (lamp-host1,host2) execute show ip $(mroute,mfib) $1[225.1.1.1,232.2.2.2]
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   2025-09-19 14:29:40: %LAMP-INFO: :                            Execute loop, length=4                            :
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   2025-09-19 14:29:40: %LAMP-INFO: :                 Execute 'show ip mroute 225.1.1.1' on 'host1'                 :
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   2025-09-19 14:29:40: %LAMP-INFO: :                  Execute 'show ip mfib 225.1.1.1' on 'host1'                  :
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   2025-09-19 14:29:40: %LAMP-INFO: :                 Execute 'show ip mroute 232.2.2.2' on 'host2'                 :
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   2025-09-19 14:29:40: %LAMP-INFO: :                  Execute 'show ip mfib 232.2.2.2' on 'host2'                  :
   2025-09-19 14:29:40: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>

A 'loop' Blitz action snippet gets generated when using command looping.

Example:

.. code-block:: console

   (lamp-h2) execute -i show $(ip,ipv6) route
   2025-08-29 07:10:08: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:10:08: %LAMP-INFO: :                            Execute loop, length=2                            :
   2025-08-29 07:10:08: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:10:08: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:10:08: %LAMP-INFO: :                      Execute 'show ip route' on 'host2'                      :
   2025-08-29 07:10:08: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:10:08,764: %UNICON-INFO: +++ host2(alias=h2) with via 'a': executing command 'show ip route' +++
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

   host2#
   2025-08-29 07:10:08: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:10:08: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
   2025-08-29 07:10:08: %LAMP-INFO: +..............................................................................+
   Enter pattern to 'INCLUDE' (Press enter for multiple patterns): not set
   2025-08-29 07:10:10: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:10:10: %LAMP-INFO: :                     Execute 'show ipv6 route' on 'host2'                     :
   2025-08-29 07:10:10: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:10:10,345: %UNICON-INFO: +++ host2(alias=h2) with via 'a': executing command 'show ipv6 route' +++
   show ipv6 route
   host2#
   2025-08-29 07:10:10: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:10:10: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
   2025-08-29 07:10:10: %LAMP-INFO: +..............................................................................+
   Enter pattern to 'INCLUDE' (Press enter for multiple patterns):
   (INCLUDE)>
   (lamp-h2) list 1
   - loop:
         loop_variable_name:
         - cmd
         - inc
         value:
         - [ip, ipv6]
         - [[not set], []]
         actions:
         - execute:
               device: host2
               command: show %VARIABLES{cmd} route
               include: '%VARIABLES{inc}'

All *include*, *exclude* entries will be separate between the 2 commands as well.

Api parameter looping
---------------------

``api`` parameters can contain loops with multiple arguments seperated by ',' & prepended
by '$'. The same rules of minimalization apply to api parameters as well.

Example:

.. code-block:: console

   (lamp-host1) api get_vrf_interface
   Gets the subinterfaces for vrf

   Args:
      device ('obj'): device to run on
      vrf ('str'): vrf to search under

   Returns:
      interfaces('list'): List of interfaces under specified vrf
      None

   Raises:
      None

   device: host1
   vrf: $(red,blue)
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:15:12: %LAMP-INFO: :                              Api loop, length=2                              :
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:15:12: %LAMP-INFO: :                   Api 'get_vrf_interface' with parameters:                   :
   2025-08-29 07:15:12: %LAMP-INFO: :                               device: 'host1'                                :
   2025-08-29 07:15:12: %LAMP-INFO: :                                  vrf: 'red'                                  :
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:15:12,468: %UNICON-INFO: +++ host1 with via 'a': executing command 'show vrf red' +++
   show vrf red
   Name                             Default RD            Protocols   Interfaces
   red                              <not set>             ipv4        Lo89
   host1#
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:15:12: %LAMP-INFO: :                                  API Output                                  :
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
                                                                     ['Loopback89']
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:15:12: %LAMP-INFO: :                   Api 'get_vrf_interface' with parameters:                   :
   2025-08-29 07:15:12: %LAMP-INFO: :                               device: 'host1'                                :
   2025-08-29 07:15:12: %LAMP-INFO: :                                 vrf: 'blue'                                  :
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:15:12,855: %UNICON-INFO: +++ host1 with via 'a': executing command 'show vrf blue' +++
   show vrf blue
   % No VRF named blue
   host1#
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:15:12: %LAMP-INFO: :                                  API Output                                  :
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
                                                                        None
   2025-08-29 07:15:12: %LAMP-INFO: +..............................................................................+
   (lamp-host1) list 1
   - loop:
         loop_variable_name:
         - vrf
         value:
         - [red, blue]
         actions:
         - api:
               function: get_vrf_interface
               arguments:
               device: host1
               vrf: '%VARIABLES{vrf}'

The API in the above example was invoked with the following arguments:

   * get_vrf_interface( host1, $(red,blue) )

Removing minimalization in the API arguments:

   * get_vrf_interface( $(host1,red) , (host1,blue) )

Since, 'api $' is equal to invoking api multiple times, the above can be simplified to:

   * get_vrf_interface( host1,red  )
   * get_vrf_interface( host1,blue )

Hence, the API gets invoked twice with the different arguments of 'red' & 'blue' for the
'vrf' parameter.

Consider a complex example with multiple loops:

   * configure_ip_igmp_join_group_source(host3, Loopback89, 225.1.1.1, 30.0.0.1)
   * configure_ip_igmp_join_group_source(host3, Loopback89, 225.1.1.1, 30.0.0.2)
   * configure_ip_igmp_join_group_source(host3, Loopback89, 226.1.1.1, 30.0.0.1)
   * configure_ip_igmp_join_group_source(host3, Loopback89, 226.1.1.1, 30.0.0.2)

Moving the addresses '225.1.1.1' & '226.1.1.1' into a loop:

   * configure_ip_igmp_join_group_source( host3, Loopback89, $(225.1.1.1,226.1.1.1), 30.0.0.1 )
   * configure_ip_igmp_join_group_source( host3, Loopback89, $(225.1.1.1,226.1.1.1), 30.0.0.2 )

Let $(225.1.1.1,226.1.1.1) = XXX to simplify the command & check for further loops:

   * configure_ip_igmp_join_group_source( host3, Loopback89, XXX, 30.0.0.1 )
   * configure_ip_igmp_join_group_source( host3, Loopback89, XXX, 30.0.0.2 )

Applying a loop for the source address:

   * configure_ip_igmp_join_group_source( host3, Loopback89, XXX, $(30.0.0.1,30.0.0.2) )

Finally, substituting the value of XXX yields:

   * configure_ip_igmp_join_group_source( host3, Loopback89, $(225.1.1.1,226.1.1.1), $(30.0.0.1,30.0.0.2) )

Invoking this api on LAMP gives the exact same API invocation equivalent to the individual
invocations as shown below:

.. code-block:: console

   (lamp-host3) api multicast configure configure_ip_igmp_join_group_source
   Configures ip igmp join-group to an vlan interface
   Example : ip igmp join-group 239.100.100.101 source 4.4.4.4

   Args:
      device ('obj'): device to use
      interface ('str'): interface or Vlan number (Eg. ten1/0/1 or vlan 10)
      group_address ('str'): IP group addres
      source_address ('str', optional): IP source address

   Returns:
      None

   Raises:
      SubCommandFailure

   device: host3
   interface: Loopback89
   group_address: $225.1.1.1,226.1.1.1
   source_address(''): $30.0.0.1,30.0.0.2
   2025-08-29 07:18:40: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:40: %LAMP-INFO: :                              Api loop, length=4                              :
   2025-08-29 07:18:40: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:40: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:40: %LAMP-INFO: :          Api 'configure_ip_igmp_join_group_source' with parameters:          :
   2025-08-29 07:18:40: %LAMP-INFO: :                               device: 'host3'                                :
   2025-08-29 07:18:40: %LAMP-INFO: :                           interface: 'Loopback89'                            :
   2025-08-29 07:18:40: %LAMP-INFO: :                          group_address: '225.1.1.1'                          :
   2025-08-29 07:18:40: %LAMP-INFO: :                          source_address: '30.0.0.1'                          :
   2025-08-29 07:18:40: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:18:40,937: %UNICON-INFO: +++ host3 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   host3(config)#interface Loopback89
   host3(config-if)#ip igmp join-group 225.1.1.1 source 30.0.0.1
   host3(config-if)#end
   host3#
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: :                                  API Output                                  :
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
                                                                        None
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: :          Api 'configure_ip_igmp_join_group_source' with parameters:          :
   2025-08-29 07:18:41: %LAMP-INFO: :                               device: 'host3'                                :
   2025-08-29 07:18:41: %LAMP-INFO: :                           interface: 'Loopback89'                            :
   2025-08-29 07:18:41: %LAMP-INFO: :                          group_address: '225.1.1.1'                          :
   2025-08-29 07:18:41: %LAMP-INFO: :                          source_address: '30.0.0.2'                          :
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:18:41,234: %UNICON-INFO: +++ host3 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   host3(config)#interface Loopback89
   host3(config-if)#ip igmp join-group 225.1.1.1 source 30.0.0.2
   host3(config-if)#end
   host3#
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: :                                  API Output                                  :
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
                                                                        None
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: :          Api 'configure_ip_igmp_join_group_source' with parameters:          :
   2025-08-29 07:18:41: %LAMP-INFO: :                               device: 'host3'                                :
   2025-08-29 07:18:41: %LAMP-INFO: :                           interface: 'Loopback89'                            :
   2025-08-29 07:18:41: %LAMP-INFO: :                          group_address: '226.1.1.1'                          :
   2025-08-29 07:18:41: %LAMP-INFO: :                          source_address: '30.0.0.1'                          :
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:18:41,526: %UNICON-INFO: +++ host3 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   host3(config)#interface Loopback89
   host3(config-if)#ip igmp join-group 226.1.1.1 source 30.0.0.1
   host3(config-if)#end
   host3#
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: :                                  API Output                                  :
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
                                                                        None
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:41: %LAMP-INFO: :          Api 'configure_ip_igmp_join_group_source' with parameters:          :
   2025-08-29 07:18:41: %LAMP-INFO: :                               device: 'host3'                                :
   2025-08-29 07:18:41: %LAMP-INFO: :                           interface: 'Loopback89'                            :
   2025-08-29 07:18:41: %LAMP-INFO: :                          group_address: '226.1.1.1'                          :
   2025-08-29 07:18:41: %LAMP-INFO: :                          source_address: '30.0.0.2'                          :
   2025-08-29 07:18:41: %LAMP-INFO: +..............................................................................+

   2025-08-29 07:18:41,816: %UNICON-INFO: +++ host3 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   host3(config)#interface Loopback89
   host3(config-if)#ip igmp join-group 226.1.1.1 source 30.0.0.2
   host3(config-if)#end
   host3#
   2025-08-29 07:18:42: %LAMP-INFO: +..............................................................................+
   2025-08-29 07:18:42: %LAMP-INFO: :                                  API Output                                  :
   2025-08-29 07:18:42: %LAMP-INFO: +..............................................................................+
                                                                        None
   2025-08-29 07:18:42: %LAMP-INFO: +..............................................................................+

The autogenerated Blitz *'loop'* action snippet is shown below:

.. code-block:: console

   (lamp-host3) list 1
   - loop:
         loop_variable_name:
         - group_address
         value:
         - [225.1.1.1, 226.1.1.1]
         actions:
         - loop:
               loop_variable_name:
               - source_address
               value:
               - [30.0.0.1, 30.0.0.2]
               actions:
               - api:
                     function: configure_ip_igmp_join_group_source
                     arguments:
                     device: host3
                     interface: Loopback89
                     group_address: '%VARIABLES{group_address}'
                     source_address: '%VARIABLES{source_address}'

.. note::

   If one of the commands failed in a loop, LAMP stops executing & would not autogenerate
   any snippet, including for the passed ones earlier.

Repeat looping
--------------

To execute an operator command multiple times, LAMP provides the '-r' option.
This option specifies how many times the command should be repeated.

For example, the following command executes "clear ip route" three times:

.. code-block:: console

   (lamp-host1) execute -r 3 clear ip route *

The output below illustrates the command being repeated:

.. code-block:: console

   (lamp-host1) execute -r 3 clear ip route *
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: :                                Repeat count=1                                :
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: :                    Execute 'clear ip route *' on 'host1'                     :
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+

   2025-04-22 10:02:50,222: %UNICON-INFO: +++ host1 with via 'a': executing command 'clear ip route *' +++
   clear ip route *
   host1#
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: :                                Repeat count=2                                :
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: :                    Execute 'clear ip route *' on 'host1'                     :
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+

   2025-04-22 10:02:50,474: %UNICON-INFO: +++ host1 with via 'a': executing command 'clear ip route *' +++
   clear ip route *
   host1#
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: :                                Repeat count=3                                :
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+
   2025-04-22 10:02:50: %LAMP-INFO: :                    Execute 'clear ip route *' on 'host1'                     :
   2025-04-22 10:02:50: %LAMP-INFO: +..............................................................................+

   2025-04-22 10:02:50,739: %UNICON-INFO: +++ host1 with via 'a': executing command 'clear ip route *' +++
   clear ip route *
   host1#
   (lamp-host1)

Using '-r' generates a Blitz *'loop'* action snippet with the *'range'* field.
Shown below is the snippet created for the above example:

.. code-block:: console

   (lamp-host1) list 1
   - loop:
         range: 3
         loop_variable_name: _range
         actions:
         - execute:
               device: host1
               command: clear ip route *