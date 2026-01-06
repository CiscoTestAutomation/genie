LAMP Basics
===========

This section introduces the basics of using LAMP with pyATS.
Each topic provides step-by-step instructions and examples.

Learning Prerequisites
----------------------

Basic knowledge of pyATS & pyATS Blitz is recommended.
Relevant information is available at:

    * `pyATS <https://developer.cisco.com/docs/pyats>`_
    * :ref:`pyATS Blitz <blitz>`

Load Testbed
-------------

LAMP operates on network devices and requires a pyATS testbed YAML
file to obtain device information.

As an example, the testbed YAML for two IOS devices 'dev1' & 'dev2' connected by a
single interface is shown below:

.. code-block:: yaml

   devices:
     dev1:
       os: iosxe
       type: iosxe
       platform: iol
       connections:
         a:
           ip: 127.0.0.1
           port: 22221
           protocol: telnet
         defaults:
           class: unicon.Unicon
           via: cli
     dev2:
       os: iosxe
       type: iosxe
       platform: iol
       connections:
         a:
           ip: 127.0.0.1
           port: 22222
           protocol: telnet
         defaults:
           class: unicon.Unicon
           via: cli

To provide this information to LAMP, use the ``testbed load`` command followed by the
path to the testbed YAML file. After loading the testbed YAML, LAMP connects to all listed
devices using the pyATS ``connect()`` API.

.. code-block:: console

   (lamp) testbed load testbed.yaml
   2025-03-22 16:02:29: %LAMP-INFO: +------------------------------------------------------------------------------+
   2025-03-22 16:02:29: %LAMP-INFO: :                        Loading testbed 'testbed.yaml'                        :
   2025-03-22 16:02:29: %LAMP-INFO: +------------------------------------------------------------------------------+

   2025-03-22 16:02:29,636: %UNICON-INFO: +++ dev2 logfile /tmp/dev2-cli-20250322T160229635.log +++

   2025-03-22 16:02:29,639: %UNICON-INFO: +++ Unicon plugin iosxe (unicon.internal.plugins.iosxe) +++

   2025-03-22 16:02:29,639: %UNICON-INFO: +++ dev1 logfile /tmp/dev1-cli-20250322T160229638.log +++

   2025-03-22 16:02:29,645: %UNICON-INFO: +++ Unicon plugin iosxe (unicon.internal.plugins.iosxe) +++
   /nobackup/araradha/pyats/lib/python3.8/site-packages/unicon/bases/routers/connection.py:97: DeprecationWarning: Arguments 'username', 'enable_password','tacacs_password' and 'line_password' are now deprecated and replaced by 'credentials'.
     warnings.warn(message = "Arguments 'username', "
   Trying 127.0.0.1...
   Connected to 127.0.0.1.
   Escape character is '^]'.

   2025-03-22 16:02:29,678: %UNICON-INFO: +++ connection to spawn: telnet 127.0.0.1 33332, id: 139678878698896 +++

   2025-03-22 16:02:29,678: %UNICON-INFO: connection to dev2
   Trying 127.0.0.1...
   Connected to 127.0.0.1.
   Escape character is '^]'.

   2025-03-22 16:02:29,681: %UNICON-INFO: +++ connection to spawn: telnet 127.0.0.1 33331, id: 139678878669120 +++

   2025-03-22 16:02:29,682: %UNICON-INFO: connection to dev1

   dev1#
   dev2#

   2025-03-22 16:02:31,447: %UNICON-INFO: +++ dev1 with via 'a': executing command 'show version | include operating mode' +++

   2025-03-22 16:02:31,450: %UNICON-INFO: +++ dev2 with via 'a': executing command 'show version | include operating mode' +++
   show version | include operating mode
   dev1#show version | include operating mode
   dev2#

   2025-03-22 16:02:31,699: %UNICON-INFO: +++ dev1 with via 'a': executing command 'term length 0' +++

   2025-03-22 16:02:31,704: %UNICON-INFO: +++ dev2 with via 'a': executing command 'term length 0' +++
   term length 0
   dev1#term length 0
   dev2#

   2025-03-22 16:02:31,967: %UNICON-INFO: +++ dev2 with via 'a': executing command 'term width 0' +++
   term width 0

   2025-03-22 16:02:31,971: %UNICON-INFO: +++ dev1 with via 'a': executing command 'term width 0' +++
   dev2#term width 0
   dev1#

   2025-03-22 16:02:32,346: %UNICON-INFO: +++ dev2 with via 'a': configure +++

   2025-03-22 16:02:32,351: %UNICON-INFO: +++ dev1 with via 'a': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   dev2(config)#config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   dev1(config)#no logging console
   dev1(config)#line console 0
   dev1(config-line)#exec-timeout 0
   dev1(config-line)#line vty 0 4
   dev1(config-line)#exec-timeout 0
   dev1(config-line)#end
   dev1#
   no logging console
   dev2(config)#line console 0
   dev2(config-line)#exec-timeout 0
   dev2(config-line)#line vty 0 4
   dev2(config-line)#exec-timeout 0
   dev2(config-line)#end
   dev2#
   2025-03-22 16:02:32: %LAMP-INFO: +..............................................................................+
   2025-03-22 16:02:32: %LAMP-INFO: :                      Connected to 'dev1' successfully                       :
   2025-03-22 16:02:32: %LAMP-INFO: :                      Connected to 'dev2' successfully                       :
   2025-03-22 16:02:32: %LAMP-INFO: +..............................................................................+
   (lamp-dev1)

Switch between devices
----------------------

Once a testbed is successfully loaded in the LAMP shell, one device from the
testbed is designated as the active device. Any operation performed in the LAMP shell
applies only to the active device.

The LAMP shell prompt reflects the hostname of the currently *active* device in the format:
``(lamp-<ACTIVE_DEVICE_HOSTNAME>)``.

Switch between devices in the testbed using the ``device`` command. To switch from 'dev1'
to 'dev2', run ``device dev2``:

.. code-block:: console

    (lamp-dev1) device dev2
    (lamp-dev2)

After running the device command, the LAMP prompt changed from 'dev1' to 'dev2',
indicating that 'dev2' is now the active device in the shell.

Basic device operations
-----------------------

Two basic operations are available for any device:

    * Configure  : Configures CLI commands.
    * Execute    : Runs commands in the device's exec prompt

Configure
^^^^^^^^^

To configure any CLI on a device, first switch to the target device using the
``device`` command. Then, invoke the ``configure`` command to enter the *config-prompt*
mode, which mimics the device's configuration terminal prompt. Apply configurations as needed.
Type *'lamp'* to exit and return to the LAMP shell prompt.

Here's an example for a loopback interface configuration done via ``configure``:

.. code-block:: console

   (lamp-dev1) configure
   dev1(config)# interface Loopback0
   dev1(config-if)# ip address 1.1.1.1 255.255.255.255
   dev1(config-if)# lamp
   (lamp-dev1)

Execute
^^^^^^^

To execute a command on a device, first switch to the target device using the ``device``
command. Then, invoke the ``execute`` command to enter the *exec-prompt* mode,
which mimics the device's exec prompt. Run commands as on the device.
Enter *'lamp'* to exit and return to the LAMP shell prompt.

Here's an example of using the ``execute`` command to view the output of a 'show' command:

.. code-block:: console

   (lamp-dev1) execute
   dev1# show ip route

   2024-10-03 09:50:46,782: %UNICON-INFO: +++ dev1 with via 'a': executing command 'show ip route' +++
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
         20.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
   C        20.0.0.0/24 is directly connected, Ethernet0/0
   L        20.0.0.1/32 is directly connected, Ethernet0/0
   dev1#
   dev1# lamp
   (lamp-dev1)

View generated Blitz snippets
-----------------------------

Each ``execute`` and ``configure`` command generates a Blitz snippet.
The ``list`` command displays these snippets; ``list -a`` shows all
generated snippets.

Autogenerated *'configure'* and *'execute'* action snippets for the
previous examples are shown below:

.. code-block:: console

   (lamp-dev1) list -a
   default:
     - configure:
         device: dev1
         command: |-
           !
           interface Loopback0
             ip address 1.1.1.1 255.255.255.255
     - execute:
         device: dev1
         command: show ip route
   (lamp-dev1)

Validate execute outputs
------------------------

Validations in testcases require more than command execution. Blitz supports
*'include'* and *'exclude'* entries for these:

    * An *'include'* entry checks if a specific pattern appears in the output
    * An *'exclude'* entry checks if a specific pattern **DOES NOT** appear in the output

The inclusion of *include* & *exclude* entries linked to an ``execute`` output
enables Blitz to verify specific values within the output, forming the foundation
of any verification.

Include entries
^^^^^^^^^^^^^^^^

An *include* entry is used to check if a particular pattern appears in the output
of the command execution. For ``execute`` command outputs, they are provided in the form
of regex patterns.

Add *include* entries to an ``execute`` command output using ``execute -i <CMD>``.
This executes the command normally and then prompts to add *include* entries
to be associated with the execution output.

Verification that '1.1.1.1' appears in the output of 'show ip route' can be
performed by specifying '1\\.1\\.1\\.1' as an *include* entry shown below:

.. code-block:: console

   (lamp-dev1) execute -i show ip route
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+
   2024-10-03 09:51:41: %LAMP-INFO: :                      Execute 'show ip route' on 'dev1'                       :
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+

   2024-10-03 09:51:41,355: %UNICON-INFO: +++ dev1 with via 'a': executing command 'show ip route' +++
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
   dev1#
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+
   2024-10-03 09:51:41: %LAMP-INFO: :                       Collecting INCLUDE Entries                             :
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+
   Enter pattern to INCLUDE (Press enter for multiple patterns): 1\.1\.1\.1
   (lamp-dev1)

When an include entry is added, LAMP verifies the pattern and adds it to the Blitz snippet
under the *'include'* field.

Here's the autogenerated Blitz action snippet for the *include* entry example shown earlier,
observed via the ``list 1`` command (``list <n>`` displays the last 'n' autogenerated
action snippets in that order):

.. code-block:: console
  
   (lamp-dev1) list 1
     - execute:
         device: dev1
         command: show ip route
         include:
           - 1\.1\.1\.1

Multiple include entries are added by pressing <ENTER> at the prompt,
entering each pattern one by one. Press <ENTER> again to exit.

Here is an example consisting of multiple *include* entries:

.. code-block:: console

   (lamp-dev2) execute -i show ip route
   2024-07-26 17:38:07: %LAMP-INFO: +..............................................................................+
   2024-07-26 17:38:07: %LAMP-INFO: :                      Execute 'show ip route' on 'dev2'                       :
   2024-07-26 17:38:07: %LAMP-INFO: +..............................................................................+
   
   2024-07-26 17:38:07,900: %UNICON-INFO: +++ dev2 with via 'a': executing command 'show ip route' +++
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
         2.0.0.0/32 is subnetted, 1 subnets
   C        2.2.2.2 is directly connected, Loopback1
         3.0.0.0/32 is subnetted, 1 subnets
   C        3.3.3.3 is directly connected, Loopback2
   dev2#
   2024-07-26 17:38:08: %LAMP-INFO: +..............................................................................+
   2024-07-26 17:38:08: %LAMP-INFO: :                        Collecting INCLUDE entries                            :
   2024-07-26 17:38:08: %LAMP-INFO: +..............................................................................+
   Enter pattern to INCLUDE (Press enter for multiple patterns):
   (INCLUDE)> 1\.1\.1\.1
   (INCLUDE)> 2\.2\.2\.2
   (INCLUDE)> 3\.3\.3\.3
   (INCLUDE)>
   (lamp-dev2)

The generated Blitz action snippets for this case would look like:

.. code-block:: console

   (lamp-dev2) list 1
     - execute:
         device: dev2
         command: show ip route
         include:
           - 1\.1\.1\.1
           - 2\.2\.2\.2
           - 3\.3\.3\.3

Exclude entries
^^^^^^^^^^^^^^^^

An *exclude* entry is used to check if a particular pattern **DOES NOT** appear in the output
of the command execution. For ``execute`` command outputs, they are also provided in the form
of regex patterns, only this time they are expected to not match the output.

Add *exclude* entries to an ``execute`` command output using ``execute -e <CMD>``.
This executes the command normally and then prompts for *exclude* entries
to be associated with the execution output.

Verification that '30.30.30.30' is not present in the output of 'show ip route'
can be performed by specifying '30\\.30\\.30\\.30' as an *exclude* entry shown below:

.. code-block:: console

   (lamp-dev1) execute -e show ip route
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+
   2024-10-03 09:51:41: %LAMP-INFO: :                      Execute 'show ip route' on 'dev1'                       :
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+

   2024-10-03 09:51:41,355: %UNICON-INFO: +++ dev1 with via 'a': executing command 'show ip route' +++
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
   dev1#
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+
   2024-10-03 09:51:41: %LAMP-INFO: :                       Collecting EXCLUDE Entries                             :
   2024-10-03 09:51:41: %LAMP-INFO: +..............................................................................+
   Enter pattern to EXCLUDE (Press enter for multiple patterns): 30\.30\.30\.30
   (lamp-dev1)

When an *exclude* entry is added, LAMP verifies the pattern and adds it to the Blitz snippet
under the *'exclude'* field.

Here's the autogenerated Blitz action snippet for the *exclude* entry example observed
from the output of ``list 1`` command:

.. code-block:: console
  
   (lamp-dev1) list 1
     - execute:
         device: dev1
         command: show ip route
         exclude:
           - 30\.30\.30\.30

Multiple *exclude* entries are added by pressing <ENTER> at the prompt,
entering each pattern one by one. Press <ENTER> again to exit.

Save snippets as Blitz testcase
-------------------------------

Configuring multiple CLI commands and verifications across devices
generates Blitz snippets, which together form a basic Blitz test case.

As an example, consider the following testcase requirements:

    * Configure a loopback interface with IP address '1.1.1.1/32'.
    * Check the routing table for the presence of a route to '1.1.1.1/32' via the loopback.
    * Unconfigure the loopback interface.

The LAMP commands equivalent to performing the above set of actions would be:

    - configure
        - interface Loopback0
        - ip address 1.1.1.1 255.255.255.255
        - lamp
    - execute -i show ip route
        - INCLUDE> 1\.1\.1\.1
    - configure
        - no interface Loopback0
        - lamp

Below is the LAMP terminal output performing the above in order:

.. code-block:: console

    (lamp-dev2) configure
    dev2(config)# interface Loopback0
    dev2(config-if)# ip address 1.1.1.1 255.255.255.255
    dev2(config-if)# lamp
    (lamp-dev2) 
    (lamp-dev2) execute -i show ip route
    2025-08-27 20:49:30: %LAMP-INFO: +..............................................................................+
    2025-08-27 20:49:30: %LAMP-INFO: :                      Execute 'show ip route' on 'dev2'                       :
    2025-08-27 20:49:30: %LAMP-INFO: +..............................................................................+

    2025-08-27 20:49:31,018: %UNICON-INFO: +++ dev2(alias=dev2) with via 'a': executing command 'show ip route' +++
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
    dev2#
    2025-08-27 20:49:31: %LAMP-INFO: +..............................................................................+
    2025-08-27 20:49:31: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
    2025-08-27 20:49:31: %LAMP-INFO: +..............................................................................+
    Enter pattern to 'INCLUDE' (Press enter for multiple patterns): 1\.1\.1\.1
    (lamp-dev2)
    (lamp-dev2) configure
    dev2(config)# no interface Loopback0
    dev2(config)# lamp
    (lamp-dev2)
    (lamp-dev2) list -a
      - default:
          - configure:
              device: dev2
              command: |-
                interface Loopback0
                  ip address 1.1.1.1 255.255.255.255
          - execute:
              device: dev2
              command: show ip route
              include:
                - 1\.1\.1\.1
          - configure:
              device: dev2
              command: no interface Loopback0
    (lamp-dev2) 

When the ``list -a`` output matches expectations, all Blitz action snippets
can be combined into a Blitz testcase using the ``save`` command with the desired
filepath.

For example, ``save pyats/testcases/TC1.yaml`` saves the Blitz YAML file in the
'pyats/testcases/' directory:

.. code-block:: console

   (lamp-dev2) save pyats/testcases/TC1.yaml
   2024-07-26 15:30:54: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-07-26 15:30:54: %LAMP-INFO: :              File 'pyats/testcases/TC1.yaml' saved successfully              :
   2024-07-26 15:30:54: %LAMP-INFO: +------------------------------------------------------------------------------+
   (lamp-dev2)

'TC1.yaml' would contain a Blitz trigger 'TC1' with the generated action snippets as shown
below:

.. code-block:: yaml

   # TC1.yaml
   # 03 October 2024
   # LAMP Generated testcase
   TC1:
     source:
       pkg: genie.libs.sdk
       class: triggers.blitz.blitz.Blitz
     devices:
       - dev1
     test_sections:
       - default:
          - configure:
              device: dev2
              command: |-
                interface Loopback0
                  ip address 1.1.1.1 255.255.255.255
          - execute:
              device: dev2
              command: show ip route
              include:
                - 1\.1\.1\.1
          - configure:
              device: dev2
              command: no interface Loopback0

Adding 'TC1.yaml' to any pyATS *main_trigger_datafile* integrates the test case
into a pyATS AUT script.

Quitting LAMP
-------------

The ``close`` command exits the LAMP shell and disconnects all loaded devices:

.. code-block:: console

   (lamp-dev2) close
   2024-07-26 15:31:21: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-07-26 15:31:21: %LAMP-INFO: :                  Disconnecting from all devices in testbed                   :
   2024-07-26 15:31:21: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-07-26 15:31:21: %LAMP-INFO: :                      Disconnecting from device 'dev1'                        :
   2024-07-26 15:31:21: %LAMP-INFO: :                      Disconnecting from device 'dev2'                        :
   2024-07-26 15:31:21: %LAMP-INFO: +------------------------------------------------------------------------------+

   🎃 Thank you for using LAMP

What's next
------------

After learning the basics, explore individual LAMP commands and features
to enhance workflows and meet requirements.

Continue exploring to make the most of LAMP. Happy learning!