bash_console
============

The ``bash_console`` command runs a command at bash shell on the
device loaded in the LAMP shell and automatically generates a pyATS
Blitz *'bash_console'* action snippet.

Basic usage
-----------

The ``bash_console`` command accepts a bash command as an argument
and executes it on the target device's bash prompt. The syntax is:

.. code-block:: console

   bash_console <command>

Where ``<command>`` is any valid bash command that the target device
supports.

Single command execution
^^^^^^^^^^^^^^^^^^^^^^^^

The following example demonstrates executing a single bash command
to check network interface information:

.. code-block:: console

   (lamp-n9kvp-sw-5) bash_console ifconfig phyEth1-4

This command will:

1. Connect to the device's bash console
2. Execute the ``ifconfig phyEth1-4`` command  
3. Display the interface configuration output
4. Return to the device's normal CLI mode

Command execution output:

.. code-block:: console

   2024-12-08 11:39:25: %LAMP-INFO: +..............................................................................+
   2024-12-08 11:39:25: %LAMP-INFO: :        Execute ['ifconfig phyEth1-4'] on bash console of 'n9kvp-sw-5'        :
   2024-12-08 11:39:25: %LAMP-INFO: +..............................................................................+

   2024-12-08 11:39:25,536: %UNICON-INFO: +++ n9kvp-sw-5(alias=v1) with via 'a': bash_console +++

   2024-12-08 11:39:25,661: %UNICON-INFO: +++ n9kvp-sw-5(alias=v1) with via 'a': configure +++
   config term
   Enter configuration commands, one per line. End with CNTL/Z.
   n9kvp-sw-5(config)# feature bash
   n9kvp-sw-5(config)# end
   n9kvp-sw-5#
   run bash
   bash-4.4$

   2024-12-08 11:39:26,042: %UNICON-INFO: +++ n9kvp-sw-5(alias=v1) with via 'a': executing command 'ifconfig phyEth1-4' +++
   ifconfig phyEth1-4
   phyEth1-4 Link encap:Ethernet  HWaddr 02:43:56:91:7e:07
             UP BROADCAST RUNNING PROMISC MULTICAST  MTU:9000  Metric:1
             RX packets:363221 errors:0 dropped:0 overruns:0 frame:0
             TX packets:246145 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:21793260 (20.7 MiB)  TX bytes:18579894 (17.7 MiB)

   bash-4.4$
   exit
   exit
   n9kvp-sw-5#

After executing the bash_console command, LAMP automatically
creates a pyATS Blitz *'bash_console'* action snippet as shown below:

.. code-block:: console

   (lamp-n9kvp-sw-5) list 1
   bash_console:
      device: n9kvp-sw-5
      commands:
         - ifconfig phyEth1-4
   (lamp-n9kvp-sw-5)

Multiple command execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To execute multiple bash commands in sequence, combine them using
bash operators:

- ``&&`` - Execute next command only if previous command succeeds
- ``;`` - Execute next command regardless of previous result  

The following example changes directory and lists files in one
command execution:

.. code-block:: console

   (lamp-n9kvp-sw-5) bash_console cd /bootflash && ls -l
   2024-12-08 11:42:46: %LAMP-INFO: +..............................................................................+
   2024-12-08 11:42:46: %LAMP-INFO: :           Execute 'cd /bootflash && ls -l' on bash console of 'n5'           :
   2024-12-08 11:42:46: %LAMP-INFO: +..............................................................................+

   2025-03-25 10:52:10,228: %UNICON-INFO: +++ n9kvp-sw-5(alias=n5) with via 'a': bash_console +++

   2025-03-25 10:52:10,354: %UNICON-INFO: +++ n9kvp-sw-5(alias=n5) with via 'a': configure +++
   config term
   Enter configuration commands, one per line. End with CNTL/Z.
   n9kvp-sw-5(config)# feature bash
   n9kvp-sw-5(config)# end
   n9kvp-sw-5#
   run bash
   bash-4.4$

   2025-03-25 10:52:10,693: %UNICON-INFO: +++ n9kvp-sw-5(alias=n5) with via 'a': executing command 'cd /bootflash && ls -l' +++
   cd /bootflash && ls -l
   total 5314112

   <TRUNCATED>

   (lamp-n9kvp-sw-5)
   (lamp-n9kvp-sw-5) list -a
   default:
     - bash_console:
         device: n9kvp-sw-5
         commands: cd /bootflash && ls -l