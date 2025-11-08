Command reference
===================

To view the list of all commands in LAMP, type the ``help`` command or ``?`` as shown below:

.. code-block:: console

   (lamp-h2) ?
   
   Documented commands (use 'help -v' for verbose/'help <topic>' for details):
   
   I. Management
   =============
   close  device  testbed
   
   II. Operators
   =============
   api  bash_console  configure  dialog  execute  parse  python  replay  sleep
   
   III. Storage
   ============
   parameter  variable
   
   IV. Blitz handlers
   ==================
   list  remove  save  test_section
   
   V. Built-in commands
   ====================
   alias  help     macro         run_script  shell    
   edit   history  run_pyscript  set         shortcuts
   
   VI. Tools
   =========
   info
   
   VII. Documentation
   ==================
   documentation

To get a short help message for each command, use the '-v' option:

.. code-block:: console

   (lamp-h2) ? -v