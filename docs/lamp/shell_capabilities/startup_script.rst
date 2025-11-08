Startup script
==============

LAMP executes a startup script located at '~/.lamprc' when the
shell begins. This script enables permanent storage of aliases,
macros, and settings within the shell environment. The startup
script also supports loading testbeds, importing parameters, and
executing other initialization tasks automatically.

Usage
-----

To configure startup commands for LAMP, create a '.lamprc' file 
in the home directory and add the required LAMP commands. Use '#'
to add comments within the file for documentation purposes.

The example below demonstrates a typical '.lamprc' configuration:

.. code-block:: text

   ###############################
   # General
   ###############################

   # Convenient shortcuts for common commands
   alias create la list -a
   alias create ra remove -a
   alias create tb testbed

   # Command history shortcuts
   alias create ha history -a
   alias create hr history -r

   # Quick access to edit startup script within LAMP
   alias create lamprc edit ~/.lamprc

   ###############################
   # Settings
   ###############################

   set blitz_continue False

LAMP automatically loads '~/.lamprc' and executes all commands
before displaying the shell prompt, as demonstrated below:

.. code-block:: console
   
   🎃 LAMP shell started
   
   Alias 'la' created
   Alias 'ra' created
   Alias 'tb' created
   Alias 'ha' created
   Alias 'hr' created
   Alias 'lamprc' created
   blitz_continue - was: True
   now: False
   (lamp)