Command line editing
=====================

LAMP utilizes the GNU command line editing interface through the
readline module. The readline module uses Emacs-style editing 
commands by default. However, switching to vi-style line editing
provides enhanced text manipulation capabilities.

Customization of readline behavior requires adding commands to
the readline initialization file. The file location is defined
by the 'INPUTRC' environment variable. When this variable is
unset, the default location becomes '~/.inputrc'.

Readline vi mode
----------------

To enable vi-style interface, add the following line to 
'~/.inputrc' (create the file if it does not exist):

.. code-block:: bash

   set editing-mode vi

Readline vi mode starts in *insertion* mode, similar to pressing 
'i' in the vi editor. Pressing <ESC> enters *normal* mode, 
enabling text editing with standard vi movement commands.
The 'k' key navigates to previous command history, while 'j' 
moves to subsequent commands.

.. list-table:: Useful vi key bindings for command line editing

   * - w/W/b/B
     - Move by one word forward/backward
   * - 0/$
     - Move to start/end of line
   * - daw/caw
     - Delete/Change a word
   * - cc
     - Change entire line
   * - f/F
     - Forward/Backward search for specific character

Example: Modifying ``execute show ip mrib route -i`` to 
``execute show ipv6 mrib route -i`` using the 'find' command:

.. list-table:: Cursor position in vi mode
   :header-rows: 1

   * - Keystroke
     - Command line (|| shows cursor position)
   * - <ESC>
     - execute -i show ip mrib rout|e|
   * - Fp
     - execute -i show i|p| mrib route
   * - av6
     - execute -i show ipv6 mrib route