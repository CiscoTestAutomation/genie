Shell history
=============

LAMP permanently stores the history of commands invoked across multiple sessions
in the file '~/lamp_history.dat'. Users can view, search & rerun previously entered
LAMP shell commands by pressing <Up> & <Down>, as well as perform a reverse-i-search
using <ctrl-r> similar to bash.

Advanced history
----------------

LAMP stores advanced history into 5 categories each being independent of the others:

1. Command history
2. *include*, *exclude*, *save* entry history
3. ``api`` argument history
4. *'exec-prompt'* mode history
5. *'config-prompt'* mode history

Apart from command history, other categories are stored in the file
'~/lamp_adv_history.dat'.

Since the history is separated across different categories, a reverse-i-search
on an *include* entry would only use the *include*, *exclude*, *save* entry history.

Shown below is an example of reverse-i-search performed in the *include* entry prompt:

.. code-block:: console

   (lamp-host1) execute -i show ip route
   2024-08-01 09:41:53: %LAMP-INFO: +..............................................................................+
   2024-08-01 09:41:53: %LAMP-INFO: :                      Execute 'show ip route' on 'host1'                      :
   2024-08-01 09:41:53: %LAMP-INFO: +..............................................................................+
   
   2024-08-01 09:41:54,083: %UNICON-INFO: +++ host1 with via 'a': executing command 'show ip route' +++
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
   2024-08-01 09:41:54: %LAMP-INFO: +..............................................................................+
   2024-08-01 09:41:54: %LAMP-INFO: :                                   INCLUDE                                    :
   2024-08-01 09:41:54: %LAMP-INFO: +..............................................................................+
   (reverse-i-search)`3.': 3.3.3.3

.. note::

   It is recommended to remap <CAPS_LOCK> key to <ctrl-r> using keyboard
   customizers like 'karabiner-elements'. This helps in performing a quick
   reverse-i-search before typing the entire command.

'history' command
-------------------

The ``history`` command can be used to view, search & rerun previously entered
LAMP shell commands. See `History <https://cmd2.readthedocs.io/en/latest/features/history/#for-users>`_
for more information.

An example of ``history`` regex search:

.. code-block:: console

   (lamp) history -a api
     253  api _time_to_int
     448  api _time_to_int -s
     457  api _time_to_int
     487  api _get_running_config_dict -s
     508  api _get_running_config_dict -s
     530  api _int_to_mask
     <TRUNCATED>

An example of ``history`` run:

.. code-block:: console

   (lamp-host1) history -a "execute show"
     885  execute show interfaces stats
   (lamp-host1) history -r 885
   2024-09-17 14:55:45: %LAMP-INFO: +..............................................................................+
   2024-09-17 14:55:45: %LAMP-INFO: :                  Execute 'show interfaces stats' on 'host1'                  :
   2024-09-17 14:55:45: %LAMP-INFO: +..............................................................................+

   2024-09-17 14:55:45,429: %UNICON-INFO: +++ host1 with via 'a': executing command 'show interfaces stats' +++
   show interfaces stats
   Ethernet0/0
