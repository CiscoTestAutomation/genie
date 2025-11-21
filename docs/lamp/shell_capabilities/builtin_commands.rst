Builtin commands
================

These commands work at the shell & OS level to enhance user working experience.

alias
-----
Having alises for commands prevents unnecessary typing for frequently used commands.

Consider, as an example, the difficulty to frequently type the command
``execute show ip interface brief`` to check interface information. In such cases,
it would be better to create an alias named 'int' for the *show* command and invoke
``int`` rather than the full command.

Create aliases using ``alias create``:

.. code-block:: console

   (lamp-leaf2) alias create int execute show ip interface brief
   Alias 'int' created

Invoke the alias using the alias name:

.. code-block:: console

   (lamp-leaf2) int
   2024-08-10 13:24:46: %LAMP-INFO: +..............................................................................+
   2024-08-10 13:24:46: %LAMP-INFO: :                 Execute 'show ip interface brief' on 'leaf2'                 :
   2024-08-10 13:24:46: %LAMP-INFO: +..............................................................................+
   <TRUNCATED>

<TAB> autocompletes words beyond the alias automatically, as shown below:

.. code-block:: console

   (lamp-host1) int

   COMMAND            Description
   <cr>               <cr>
   ACR                Virtual ACR interface
   Analysis-Module    Cisco network analysis service module
   AppNav-Compress    Service-Context Virtual Interface Compress
   AppNav-UnCompress  Service-Context Virtual interface UnCompress
   Async              Async interface

See created aliases using ``alias list``:

.. code-block:: console

   (lamp-leaf2) alias list
   alias create int execute show ip interface brief
   (lamp-leaf2)

Delete created aliases using ``alias delete``:

.. code-block:: console

   (lamp-leaf2) alias delete int
   Alias 'int' deleted
   (lamp-leaf2) int
   int is not a recognized command, alias, or macro
   (lamp-leaf2)

macro
------

It is similar to the ``alias`` command in functionality but can contain
argument placeholders. Arguments are expressed when creating a macro
using '{#}' notation where '{1}' means the first argument.

Consider, as an example, the ``testbed add`` command to add a device
to the shell. For easy addition of NXOS devices, a macro can be created
with the following placeholders:

* testbed add {1} -o nxos -c {2}

where {1} is the device name and {2} is the credentials.

Create the macro using ``macro create``:

.. code-block:: console

   (lamp-host1) macro create nxtb testbed add {1} -o nxos -c {2}
   Macro 'nxtb' created
   (lamp-host1)

Invoke the macro using the macro name followed by the arguments:

.. code-block:: console

   (lamp-host1) nxtb 10.1.8.2 admin/lab123

   2025-09-23 10:28:17,973: %UNICON-INFO: +++ 10.1.8.2 logfile 10.1.8.2-cli-1758603497.log +++

   2025-09-23 10:28:17,974: %UNICON-INFO: +++ Unicon plugin nxos (unicon.internal.plugins.nxos) +++
   Warning: Permanently added '10.1.8.2' (RSA) to the list of known hosts.

   2025-09-23 10:28:18,456: %UNICON-INFO: +++ connection to spawn: ssh -l admin 10.1.8.2 -p 22, id: 139763795448736 +++
   <TRUNCATED>
   2025-09-23 10:28:20: %LAMP-INFO: +..............................................................................+
   2025-09-23 10:28:20: %LAMP-INFO: :                      Device 'A6-NXOS' connected successfully                 :
   2025-09-23 10:28:20: %LAMP-INFO: +..............................................................................+
   (lamp-A6-NXOS)

To view all macros, use ``macro list``:

.. code-block:: console

   (lamp-host1) macro list
   macro create nxtb testbed add {1} -o nxos -c {2}
   (lamp-host1)

To delete a particular macro, use ``macro delete``:

.. code-block:: console

   (lamp-host1) macro delete nxtb
   Macro 'nxtb' deleted
   (lamp-host1) nxtb 1.1.1.1 admin/lab123
   nxtb is not a recognized command, alias, or macro
   (lamp-host1)

edit
-----
Edit a file using the default editor:

.. code-block:: console

   (lamp-host1) edit pyats/parameters.yaml

Both relative and absolute paths can be used to specify the file to edit.
Relative paths are resolved based on the directory where LAMP was started.

shell
------
Execute a command as if at the OS prompt.

For example, to view files using 'ls', ``shell ls`` could be used:

.. code-block:: console

   (lamp-host1) shell ls ../../alternate_msdp/
   destroy_iol					   mvpn-inter-as-ut-topo  nvram_00014	vimsession.vim
   extra						   NETMAP		  pnp-info
   nvram_00011		  pnp-tech	xwrapper
   iol-linux-manual-startup			   nvram_00012		  testbed.yaml		
   nvram_00013		  undo.undo
   (lamp-host1)

shortcuts
----------
Shortcuts are default 'aliases' created & inbuilt in the shell. ``shortcuts``
command lists them.

.. code-block:: console

   (lamp-host1) shortcuts
   Shortcuts for other commands:
   !: shell
   %: parameter list
   ?: help
   @: run_script
   @@: _relative_run_script
   ^: variable list
   (lamp-host1)

An example of ``shell`` command invoked via the shortcut ``!``:

.. code-block:: console

   (lamp) shell clock --verbose
   clock from util-linux 2.32.1
   System Time: 1756283676.752083
   Trying to open: /dev/rtc0
   No usable clock interface found.
   clock: Cannot access the Hardware Clock via any known method.
   (lamp)
   (lamp) 
   (lamp) !clock --verbose
   clock from util-linux 2.32.1
   System Time: 1756283686.492618
   Trying to open: /dev/rtc0
   No usable clock interface found.
   clock: Cannot access the Hardware Clock via any known method.
   (lamp) 

set
---
Used to modify settings in the LAMP shell.

List of all settings:

.. code-block:: console

   (lamp) set -v
   blitz_continue: True             # Value to be set for Blitz's 'continue' field
   blitz_expected_failure: DISABLED # Controls the generation of Blitz 'expected_failure' field
   blitz_group: DISABLED            # Controls the addition of Blitz 'groups' field on saving testcases
   blitz_retry: '0/0'               # Set values for Blitz fields 'max_time' & 'check_interval'
   console_logs_dir: None           # Console logs directory path
   device_aliases: DISABLED         # Controls the creation of device aliases

Modify a setting by invoking ``set <SETTING_NAME> <VALUE>``:

.. code-block:: console

   (lamp) set blitz_continue false
   blitz_continue - was: True
   now: False
   (lamp) 

run_script
----------
Executes a set of LAMP shell commands from a file. Scripts help automate tasks
by grouping related commands.

Consider, for example, a script that can bring up the testbed 'vxlan_tb.yaml',
fetches parameters from 'vxlan_params.yaml', and performs an additional
terminal setup operation all in one go. Shown below is the content of the script
that does this, saved in a file named 'vxlan_script':

.. code-block:: text

   # vxlan_script
   testbed load vxlan_tb.yaml
   parameter import vxlan_params.yaml
   device $mod1-a1,mod1-a2,mod1-a3
   execute terminal length 0

To invoke it, use the ``run_script`` command or the ``@`` shortcut with the script path:

.. code-block:: console

   (lamp) @/path/to/vxlan_script
