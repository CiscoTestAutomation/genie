Console log files
==================

LAMP can generate a separate log file for each device in a testbed, recording all actions
performed on that device. To enable this feature, set the 'console_logs_dir' setting to
specify the directory where log files will be saved. Once configured, log files are created
in the format '<DEVICE_NAME>.log'.

In the example shown below, setting 'console_logs_dir' to 'msdp_logs/' would
create the log files 'msdp_logs/leaf2.log' and 'msdp_logs/spine.log'
for the devices 'leaf2' and 'spine', respectively:

.. code-block:: console

   (lamp-leaf2) set console_logs_dir msdp_logs/

   2024-08-06 16:13:22,419: %UNICON-INFO: +++ logfile: msdp_logs/leaf2.log +++

   2024-08-06 16:13:22,447: %UNICON-INFO: +++ logfile: msdp_logs/spine.log +++
   console_logs_dir - was: None
   now: 'msdp_logs/'
   (lamp-leaf2)

Once the directory for console logs is set, any operation (such as 'execute' or 'configure')
performed on any device will automatically write the output to the corresponding log file.

The following example shows the output of 'show ip route' appearing in
the device's log file after the command is run in the LAMP shell:

.. code-block:: console

   (lamp-leaf2) execute show ip route
   2024-08-06 16:14:35: %LAMP-INFO: +..............................................................................+
   2024-08-06 16:14:35: %LAMP-INFO: :                      Execute 'show ip route' on 'leaf2'                      :
   2024-08-06 16:14:35: %LAMP-INFO: +..............................................................................+

   2024-08-06 16:14:35,547: %UNICON-INFO: +++ leaf2 with via 'a': executing command 'show ip route' +++
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
   O        1.1.1.1 [110/3] via 20.1.1.1, 00:15:33, GigabitEthernet1/0/1
   leaf2#
   (lamp-leaf2)
   (lamp-leaf2) shell cat msdp_logs/leaf2.log
   [2024-08-06 16:14:35,547] +++ leaf2 with via 'a': executing command 'show ip route' +++
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
   O        1.1.1.1 [110/3] via 20.1.1.1, 00:15:33, GigabitEthernet1/0/1
   leaf2#
   (lamp-leaf2)

Another example highlighting configuration logs:

.. code-block:: console

   (lamp-leaf2) configure no logging console
   2024-08-06 16:16:53: %LAMP-INFO: +..............................................................................+
   2024-08-06 16:16:53: %LAMP-INFO: :                  Configure 'no logging console' on 'leaf2'                   :
   2024-08-06 16:16:53: %LAMP-INFO: +..............................................................................+

   2024-08-06 16:16:53,242: %UNICON-INFO: +++ leaf2 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   leaf2(config)#no logging console
   leaf2(config)#end
   leaf2#
   (lamp-leaf2)
   (lamp-leaf2) shell cat msdp_logs/leaf2.log
   [2024-08-06 16:14:35,547] +++ leaf2 with via 'a': executing command 'show ip route' +++
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
   O        1.1.1.1 [110/3] via 20.1.1.1, 00:15:33, GigabitEthernet1/0/1
   leaf2#
   [2024-08-06 16:16:53,242] +++ leaf2 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   leaf2(config)#no logging console
   leaf2(config)#end
   leaf2#
   (lamp-leaf2)