testbed
=======

The ``testbed`` command enables device loading and management within
the LAMP shell environment.

Loading devices in the shell
----------------------------

LAMP supports two primary methods for loading devices:

   1. Using pyATS testbed YAML files
   2. Using device IP addresses with connection parameters

Loading devices from a testbed YAML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The LAMP shell supports loading devices from pyATS testbed YAML files
using the ``testbed load`` command.

For detailed information about pyATS testbed YAML schema, refer to the
comprehensive documentation available `here <https://pubhub.devnetcloud.com/media/pyats/docs/topology/schema.html#production-yaml-schema>`_.

To connect to all devices defined in a testbed YAML file, specify the
path to the file as an argument. Relative file paths are resolved
from the directory where LAMP was started.

As an example, the testbed YAML shown below includes 2 devices:

.. code-block:: yaml

    devices:
      host1:
        os: ios
        platform: iol
        connections:
          a:
            ip: 127.0.0.1
            port: 55551
            protocol: telnet
            arguments:
              learn_hostname: true
          defaults:
            class: unicon.Unicon
            via: cli
      host2:
        alias: h2
        os: ios
        platform: iol
        connections:
          a:
            ip: 127.0.0.1
            port: 55552
            protocol: telnet
            arguments:
              learn_hostname: true
          defaults:
            class: unicon.Unicon
            via: cli

Loading the above devices in the testbed YAML using 
``testbed load`` produces the following output:

.. code-block:: console

    (lamp) testbed load testbed.yaml 
    
    2025-08-27 10:48:11,569: %UNICON-INFO: +++ host1 logfile host1-cli-1756271891.log +++
    
    2025-08-27 10:48:11,572: %UNICON-INFO: +++ Unicon plugin ios (unicon.plugins.ios) +++
    
    2025-08-27 10:48:11,573: %UNICON-INFO: +++ host2 logfile host2-cli-1756271891.log +++
    
    2025-08-27 10:48:11,574: %UNICON-INFO: +++ Unicon plugin ios (unicon.plugins.ios) +++
    Trying 127.0.0.1...
    Connected to 127.0.0.1.
    Escape character is '^]'.
    
    2025-08-27 10:48:11,653: %UNICON-INFO: +++ connection to spawn: telnet 127.0.0.1 55551, id: 139702669476384 +++
    Trying 127.0.0.1...
    Connected to 127.0.0.1.
    Escape character is '^]'.
    
    2025-08-27 10:48:11,654: %UNICON-INFO: connection to host1
    
    2025-08-27 10:48:11,656: %UNICON-INFO: +++ connection to spawn: telnet 127.0.0.1 55552, id: 139702672686336 +++
    
    2025-08-27 10:48:11,657: %UNICON-INFO: connection to host2

    host2#host1#
    
    2025-08-27 10:48:13,242: %UNICON-INFO: Learned hostname(s): 'host1'.
    
    2025-08-27 10:48:13,243: %UNICON-INFO: +++ initializing handle +++
    
    2025-08-27 10:48:13,244: %UNICON-INFO: Learned hostname(s): 'host1'.
    
    
    2025-08-27 10:48:13,248: %UNICON-INFO: Learned hostname(s): 'host2'.
    
    2025-08-27 10:48:13,248: %UNICON-INFO: +++ initializing handle +++
    
    2025-08-27 10:48:13,249: %UNICON-INFO: Learned hostname(s): 'host2'.
    
    2025-08-27 10:48:13,371: %UNICON-INFO: +++ host1 with via 'a': executing command 'term length 0' +++
    
    2025-08-27 10:48:13,372: %UNICON-INFO: +++ host2(alias=h2) with via 'a': executing command 'term length 0' +++
    term length 0
    host1#term length 0
    host2#
    
    2025-08-27 10:48:13,575: %UNICON-INFO: +++ host1 with via 'a': executing command 'term width 0' +++
    
    2025-08-27 10:48:13,576: %UNICON-INFO: +++ host2(alias=h2) with via 'a': executing command 'term width 0' +++
    term width 0
    host2#term width 0
    host1#
    
    2025-08-27 10:48:13,787: %UNICON-INFO: +++ host2(alias=h2) with via 'a': executing command 'show version' +++
    
    2025-08-27 10:48:13,788: %UNICON-INFO: +++ host1 with via 'a': executing command 'show version' +++
    show version
    Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISE-M), Experimental Version
    Copyright (c) 1986-2024 by Cisco Systems, Inc.
    
    ROM: Bootstrap program is Linux
    
    host1 uptime is 19 minutes
    Last reload reason: Unknown reason
    
    Linux Unix (i686) processor with 259503K bytes of memory.
    Processor board ID 3625769011
    16 Ethernet interfaces
    8 Serial interfaces
    64K bytes of NVRAM.
    
    Configuration register is 0x0
    
    host1#show version
    Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISE-M), Experimental Version
    Copyright (c) 1986-2024 by Cisco Systems, Inc.
    
    ROM: Bootstrap program is Linux
    
    host2 uptime is 19 minutes
    Last reload reason: Unknown reason
    
    Linux Unix (i686) processor with 259503K bytes of memory.
    Processor board ID 3625769012
    16 Ethernet interfaces
    8 Serial interfaces
    64K bytes of NVRAM.
    
    Configuration register is 0x0
    
    host2#
    
    2025-08-27 10:48:13,865: %UNICON-INFO: +++ host1 with via 'a': configure +++
    
    2025-08-27 10:48:13,870: %UNICON-INFO: +++ host2(alias=h2) with via 'a': configure +++
    config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    host1(config)#config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    host2(config)#nno logging console
    host2(config)#line console 0
    o logging console
    host1(config)#line cohost2(config-line)#exec-timeout 0
    nsole 0
    host1(config-line)#ehost2(config-line)#lxec-timeout 0
    host1(config-line)#line vty 0 4
    host2(config-line)#exec-timeout 0
    ine vty 0 4
    host1(config-line)#exec-timhost2(config-line)#end
    eout 0
    host1(config-line)#enhost2#
    d
    host1#
    2025-08-27 10:48:14: %LAMP-INFO: +..............................................................................+
    2025-08-27 10:48:14: %LAMP-INFO: :                    Device 'host1' connected successfully'                    :
    2025-08-27 10:48:14: %LAMP-INFO: :                    Device 'host2' connected successfully'                    :
    2025-08-27 10:48:14: %LAMP-INFO: +..............................................................................+
    (lamp-h2) 

LAMP establishes connections to all devices in the testbed file
in parallel, maximizing connection efficiency.

**Loading specific devices**

To load only certain devices from the testbed YAML file, use the
'-d' option followed by a comma-separated list of device names.

Using the previous testbed YAML example, the following demonstrates
loading only the device 'host1' while excluding device 'host2':

.. code-block:: console

   (lamp) testbed load testbed.yaml -d host1
   2025-03-18 11:28:25: %LAMP-INFO: +------------------------------------------------------------------------------+
   2025-03-18 11:28:25: %LAMP-INFO: :                        Loading testbed 'testbed.yaml'                        :
   2025-03-18 11:28:25: %LAMP-INFO: +------------------------------------------------------------------------------+
   <TRUNCATED>
   2025-03-18 11:28:27: %LAMP-INFO: +..............................................................................+
   2025-03-18 11:28:27: %LAMP-INFO: :                      Connected to 'host1' successfully                       :
   2025-03-18 11:28:27: %LAMP-INFO: +..............................................................................+
   (lamp-host1)

This selective loading approach enables working with a subset of 
devices while retaining the advantages of testbed YAML configuration.

Multiple devices can also be selected by separating their names with
commas as in ``testbed load <file> -d <name1>,<name2>``.

Loading devices using IP
^^^^^^^^^^^^^^^^^^^^^^^^

The LAMP shell supports loading devices using their management or 
telnet IP address through the ``testbed add`` command.

The ``testbed add`` command supports various options for connecting 
to different types of devices:

.. list-table:: Options for ``testbed add`` command
   :widths: 10 90
   :header-rows: 1

   * - Option
     - Description
   * - -p
     - Port number
   * - -c
     - Credentials in the format "username/password"
   * - -o
     - Device OS (Can be 'ios', 'iosxe', 'nxos' or 'linux')
   * - -n
     - Desired name for the device in LAMP (Can differ from hostname)
   * - -ix
     - Commands to execute once connected to the device

The following examples demonstrate these option values for 
connecting to different types of devices:

.. list-table:: ``testbed add`` examples
   :widths: 50 50
   :header-rows: 1

   * - Device type
     - Command
   * - Virtual IOS on port 55551
     - ``testbed add 127.0.0.1 -p 55551 -o ios``
   * - Physical IOS-XE device
     - ``testbed add 10.18.1.3 -c admin/lab -o iosxe``
   * - Physical NXOS device 'r1'
     - ``testbed add 10.13.13.1 -c admin/lab -o nxos -n r1``

The OS option '-o' is mandatory for specifying the device's 
operating system.

When the device name is not specified using the '-n' option, LAMP 
defaults to using the device's hostname as its name within the LAMP 
shell.

The virtual IOS example is demonstrated below:

.. code-block:: console

    (lamp)
    (lamp) testbed add 127.0.0.1 -p 55551 -o ios

    2025-08-27 10:54:46,043: %UNICON-INFO: +++ 127.0.0.1 logfile 127.0.0.1-cli-1756272286.log +++

    2025-08-27 10:54:46,044: %UNICON-INFO: +++ Unicon plugin ios (unicon.plugins.ios) +++
    Trying 127.0.0.1...
    Connected to 127.0.0.1.
    Escape character is '^]'.

    2025-08-27 10:54:46,101: %UNICON-INFO: +++ connection to spawn: telnet 127.0.0.1 55551, id: 139702669544416 +++

    2025-08-27 10:54:46,102: %UNICON-INFO: connection to 127.0.0.1

    host1#

    2025-08-27 10:54:47,697: %UNICON-INFO: Learned hostname(s): 'host1'.

    2025-08-27 10:54:47,698: %UNICON-INFO: +++ initializing handle +++

    2025-08-27 10:54:47,822: %UNICON-INFO: +++ host1(alias=127.0.0.1) with via 'cli': executing command 'term length 0' +++
    term length 0
    host1#

    2025-08-27 10:54:48,025: %UNICON-INFO: +++ host1(alias=127.0.0.1) with via 'cli': executing command 'term width 0' +++
    term width 0
    host1#

    2025-08-27 10:54:48,221: %UNICON-INFO: +++ host1(alias=127.0.0.1) with via 'cli': executing command 'show version' +++
    show version
    Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISE-M), Experimental Version

    ROM: Bootstrap program is Linux

    host1 uptime is 26 minutes
    Last reload reason: Unknown reason

    Linux Unix (i686) processor with 259503K bytes of memory.
    Processor board ID 3625769011
    16 Ethernet interfaces
    8 Serial interfaces
    64K bytes of NVRAM.

    Configuration register is 0x0

    host1#

    2025-08-27 10:54:48,300: %UNICON-INFO: +++ host1(alias=127.0.0.1) with via 'cli': configure +++
    config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    host1(config)#no logging console
    host1(config)#line console 0
    host1(config-line)#exec-timeout 0
    host1(config-line)#line vty 0 4
    host1(config-line)#exec-timeout 0
    host1(config-line)#end
    host1#
    2025-08-27 10:54:48: %LAMP-INFO: +..............................................................................+
    2025-08-27 10:54:48: %LAMP-INFO: :                    Device 'host1' connected successfully                     :
    2025-08-27 10:54:48: %LAMP-INFO: +..............................................................................+
    (lamp-host1)

Loading devices using proxy
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For devices connected through a proxy, use the 
``testbed add-via-proxy`` command to load them into the LAMP shell.

First, load the proxy device in the shell either via ``testbed add`` 
or from a testbed YAML via ``testbed load``. Then, pass the proxy 
device's name as an argument to the ``testbed add-via-proxy`` command,
along with the '-x' option to specify the command that executes on 
the proxy device to access the target device's console.

Additionally, the device's name, OS, and credentials can be specified
using the '-n', '-o', and '-c' options, just as in ``testbed add``. 
When the name is not provided, LAMP attempts to learn the hostname 
automatically.

See the example below for connecting to a device named 'ACR' in a CML
virtual machine using the CML server as proxy:

.. code-block:: console

   (lamp-a8) testbed add 20.47.31.35 -n cml -o linux -c admin/lab

   2025-03-22 10:34:43,541: %UNICON-INFO: +++ Unicon plugin linux (unicon.internal.plugins.linux) +++

   2025-03-22 10:34:44,590: %UNICON-INFO: +++ connection to spawn: ssh -l admin 20.47.31.35 -p 22, id: 140642056095536 +++

   2025-03-22 10:34:44,591: %UNICON-INFO: connection to cml
   admin@20.47.31.35's password:

   ****
   CML2 Console Server
   Copyright (c) 2019-2022 Cisco Systems, Inc. and/or its affiliates
   ****

   tab completion works
   list available nodes and node labels / IDs with "list"
   it's also possible to do a "open /Lab at Wed 22:21 PM/iosv-0/0" command
   (e.g. lab name followed by node name and line number

   consoles>

   2025-03-22 10:34:45,231: %UNICON-INFO: +++ initializing handle +++
   2025-03-22 10:34:45: %LAMP-INFO: +..............................................................................+
   2025-03-22 10:34:45: %LAMP-INFO: :                       Connected to 'cml' successfully                        :
   2025-03-22 10:34:45: %LAMP-INFO: +..............................................................................+
   (lamp-cml)
   (lamp-cml) testbed add-via-proxy cml -x open /test/ACR/0 -o iosxe
   2025-03-22 10:35:10,315: %UNICON-INFO: +++ Unicon plugin generic (unicon.plugins.generic) +++

   2025-03-22 10:35:10,315: %UNICON-INFO: connection via proxy cml

   2025-03-22 10:35:10,319: %UNICON-INFO: +++ connection to spawn: ssh -l admin 20.47.31.35 -p 22, id: 140642057015200 +++

   2025-03-22 10:35:10,320: %UNICON-INFO: connection to cml
   admin@20.47.31.35's password:

   ****
   CML2 Console Server
   Copyright (c) 2019-2022 Cisco Systems, Inc. and/or its affiliates
   ****

   tab completion works
   list available nodes and node labels / IDs with "list"
   it's also possible to do a "open /Lab at Wed 22:21 PM/iosv-0/0" command
   (e.g. lab name followed by node name and line number

   consoles>

   2025-03-22 10:35:11,148: %UNICON-INFO: +++ initializing handle +++

   2025-03-22 10:35:11,149: %UNICON-INFO: connection to cml_open_/test/ACR/0

   2025-03-22 10:35:11,149: %UNICON-INFO: Learning device cml_open_/test/ACR/0 os
   consoles> open /test/ACR/0
   Connecting to console for ACR
   Connected to terminalserver.
   Escape character is '^]'.

   ACR#

   <TRUNCATED>

   2025-03-22 10:35:15,672: %UNICON-INFO: +++ initializing handle +++

   2025-03-22 10:35:15,796: %UNICON-INFO: +++ ACR(alias=cml_open_/test/ACR/0) with via 'cli': executing command 'term length 0' +++
   term length 0
   ACR#

   2025-03-22 10:35:16,103: %UNICON-INFO: +++ ACR(alias=cml_open_/test/ACR/0) with via 'cli': executing command 'term width 0' +++
   term width 0
   ACR#

   <TRUNCATED>

   2025-03-22 10:35:16,692: %UNICON-INFO: +++ ACR(alias=cml_open_/test/ACR/0) with via 'cli': configure +++
   config term
   Enter configuration commands, one per line.  End with CNTL/Z.
   ACR(config)#no logging console
   ACR(config)#line console 0
   ACR(config-line)#exec-timeout 0
   ACR(config-line)#line vty 0 4
   ACR(config-line)#exec-timeout 0
   ACR(config-line)#end
   ACR#
   2025-03-22 10:35:17: %LAMP-INFO: +..............................................................................+
   2025-03-22 10:35:17: %LAMP-INFO: :                       Connected to 'ACR' successfully                        :
   2025-03-22 10:35:17: %LAMP-INFO: +..............................................................................+
   (lamp-ACR)

Removing devices
----------------

Certain scenarios require removing devices from LAMP:

   1. Release telnet port connections
   2. Prevent name conflicts when adding new devices
   3. Free up LAMP device space when migrating to a new testbed

LAMP provides the ``testbed remove`` command, which unloads devices
from the shell and disconnects them.

Removing individual devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To remove a single device from the LAMP shell, use the 
``testbed remove`` command followed by the device name:

.. code-block:: console

   (lamp-host1) testbed remove host1
   2025-03-18 11:41:47: %LAMP-INFO: +..............................................................................+
   2025-03-18 11:41:47: %LAMP-INFO: :                      Disconnecting from device 'host1'                       :
   2025-03-18 11:41:47: %LAMP-INFO: +..............................................................................+
   (lamp-host2)

Removing multiple devices
^^^^^^^^^^^^^^^^^^^^^^^^^

Remove several devices simultaneously by providing a comma-separated
list of device names:

.. code-block:: console

   (lamp-host2) testbed remove host1,host2
   2025-03-18 11:44:27: %LAMP-INFO: +..............................................................................+
   2025-03-18 11:44:27: %LAMP-INFO: :                      Disconnecting from device 'host1'                       :
   2025-03-18 11:44:27: %LAMP-INFO: :                      Disconnecting from device 'host2'                       :
   2025-03-18 11:44:38: %LAMP-INFO: +..............................................................................+
   (lamp-host3)

Removing all devices
^^^^^^^^^^^^^^^^^^^^

For quick removal of all connected devices, use the '-a' option:

.. code-block:: console

   (lamp-host1) testbed remove -a
   2025-03-18 11:45:38: %LAMP-INFO: +..............................................................................+
   2025-03-18 11:45:38: %LAMP-INFO: :                      Disconnecting from device 'host1'                       :
   2025-03-18 11:45:38: %LAMP-INFO: :                      Disconnecting from device 'host2'                       :
   2025-03-18 11:45:38: %LAMP-INFO: :                      Disconnecting from device 'host3'                       :
   2025-03-18 11:45:49: %LAMP-INFO: +..............................................................................+
   (lamp)

Saving device configuration as testbed YAML
-------------------------------------------

The configuration of all devices loaded in the LAMP shell can be
saved together into a pyATS testbed YAML file using the 
``testbed save`` command. This allows later reconnection to a 
specific set of devices together and in parallel without needing 
to add them again using ``testbed add``.

See example below:

.. code-block:: console

   (lamp) testbed add 127.0.0.1 -p 33331

   <TRUNCATED>

   2025-03-22 11:27:05: %LAMP-INFO: +..............................................................................+
   2025-03-22 11:27:05: %LAMP-INFO: :                      Connected to 'host1' successfully                       :
   2025-03-22 11:27:05: %LAMP-INFO: +..............................................................................+
   (lamp-host1)
   (lamp-host1) testbed add 127.0.0.1 -p 33332

   <TRUNCATED>

   2025-03-22 11:27:15: %LAMP-INFO: +..............................................................................+
   2025-03-22 11:27:15: %LAMP-INFO: :                      Connected to 'host2' successfully                       :
   2025-03-22 11:27:15: %LAMP-INFO: +..............................................................................+
   (lamp-host2)
   (lamp-host2) testbed save iol_tb.yaml
   2025-03-22 11:27:21: %LAMP-INFO: +------------------------------------------------------------------------------+
   2025-03-22 11:27:21: %LAMP-INFO: :                Testbed YAML 'iol_tb.yaml' saved successfully                 :
   2025-03-22 11:27:21: %LAMP-INFO: +------------------------------------------------------------------------------+
   (lamp-host2)

The generated testbed YAML file, 'iol_tb.yaml', appears as shown
below. Even when the hostname was not specified during device 
addition to the LAMP shell, LAMP detects it during connection and 
adds it to the device configuration.

.. code-block:: yaml

   devices:
     host1:
       os: ios
       connections:
         cli:
           protocol: telnet
           ip: 127.0.0.1
           port: 33331
           settings:
             GRACEFUL_DISCONNECT_WAIT_SEC: 0
             POST_DISCONNECT_WAIT_SEC: 0
           arguments:
             learn_hostname: true
     host2:
       os: ios
       connections:
         cli:
           protocol: telnet
           ip: 127.0.0.1
           port: 33332
           settings:
             GRACEFUL_DISCONNECT_WAIT_SEC: 0
             POST_DISCONNECT_WAIT_SEC: 0
           arguments:
             learn_hostname: true