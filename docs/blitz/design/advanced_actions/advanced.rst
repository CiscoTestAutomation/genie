.. _advanced:

parallel
^^^^^^^^^

In some testcases executing actions in parallel can save huge amount of time.
In this section we will discuss how to execute multiple actions in parallel.

You can run multiple actions concurrently by defining your actions after the keyword `parallel` within
your *trigger_datafile*. Below you can see an example of of configuring multiple devices in parallel.

.. code-block:: YAML

            - verify_configuration
                - parallel:
                    - configure:
                        device: PE1
                        command: feature bgp
                    - configure:
                        device: PE2
                        command: feature bgp
                    - configure:
                        device: xe_rx
                        command: feature bgp
        ...

While you can execute actions in parallel to make the execution of a *trigger_datafile* faster,
you can still run some other actions in the same sequential manner. In below example action ``execute``
gets executed first and then two actions ``api`` and ``parse`` start their work in parallel, and finally
the action ``sleep`` start its work for 5 seconds.

.. code-block:: YAML

            # Actions 'execute' and 'sleep' are being executed on a sequential manner
            # While 'api' and 'parse' are executed at the same time
            - apply_configuration:
                - execute:
                    device: PE1
                    command: show version
                - parallel:
                    - api:
                        device: PE1
                        function: get_interface_mtu_config_range
                        arguments:
                          device: P2
                          interface: GigabitEthernet1
                    - parse:
                        command: show bgp process vrf all
                        device: P1
                - sleep:
                    sleep_time: 5
        ...

.. note::

  Please note that you cannot save a variable in parallel and immediately use it in another action
  that is being executed in the same parallel block. However, you still can save a variable in an action
  that being executed in a parallel block, and use it outside that parallel block later. If you want to use a
  variable in an action that is being executed in parallel, you need to save that variable beforehand in an
  action outside of that parallel block.

In below `example` value ``min`` and ``max`` are saved from the output of the *get_interface_mtu_config_range*
api action and later is being used in *get_interface_mtu_size* api that is going to be executed in parallel
along with a ``configure`` action. Within the same parallel block the output of the action ``configure`` is being saved
to be used later in other actions.

.. code-block:: YAML

    test_sections:
        - apply_configuration:

            - api:
                device: PE2
                function: get_interface_mtu_config_range
                save:
                - variable_name: min
                  filter: contains('min')
                - variable_name: max
                  filter: contains('max')
            - parallel:
                - api:
                    device: PE1
                    function: get_interface_mtu_size
                    arguments:
                      interface: GigabitEthernet1
                    include:
                      - ">= %VARIABLES{min} && <= %VARIABLES{max} "
                - configure:
                    device: PE1
                    save:
                      - variable_name: another_configure_output
                    command: |
                        router bgp 65000
            - execute:
                  device: PE1
                  command: show interface
                  include:
                    - "%VARIABLES{another_configure_output}"


.. note::
  
  You can run multiple actions on one device in parallel. However to make sure that actions are actually
  running in parallel you need to have multiple sessions of your device open. You can learn how to have multiple sessions open on a device bt following this `link <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/harness/user/datafile.html#mapping-datafile>`_.  

loop
^^^^^

In *Blitz*, a loop is a sequence of actions that is iterated until a certain terminating condition is reached.
Looping allows the development of more dynamic testcases.

Lets take a look at a basic examples of looping before diving deeper into looping in Blitz.
In the below *Blitz* section, the loop is above an execute action.

The goal is to run this action twice on the same device using 2 different commands, without writing two separate execute
actions with 2 different commands. This can be achieved simply by using loop like below.
In the below example The loop_variable_name will be the name of the loop value that will be reused in the action.
The value here is a list of show commands. Here each show commands get saved into the variable_name “command” and in the execute action would be loaded as the actual command.
The execute action would run twice once executing show version command and once executing show vrf command both times on the device PE1.

.. note::

  An iteration here means, one execution of all the actions below the keyword loop. In below example we have 2 iterations.

.. code-block:: YAML

    - apply_config:
        - loop:
            loop_variable_name: command
            value:
              - show version
              - show vrf
            actions:
              - execute:
                  alias: execute_
                  device: PE1
                  command: "%VARIABLES{command}"

Each loop can contains the following keywords as explained in the table: 

.. image:: table.png
   :width: 260%

.. note::

    A loop can only have one of the ``value``, ``range``, ``until``, ``do_until``.


There are a lot of use cases for looping with various features. Examples can be found below.

**Example-1: Loop over dictionary/hash**

Each dictionary is a collection of key value pairs.
To use the keys and values of the dictionary you can use the keywords ``._keys`` and ``._values``

.. code-block:: YAML

    - loop:
        # looping over a dictionary and applying values within action in same level and actions that re in the nested loop
        loop_variable_name: l_dict
        value:                          # l_dict will represent each item upon iteration in this dictionary
          inventory_save: inventory
          module_save: vrf
        actions:
            - execute:
                device: PE1
                command: show %VARIABLES{l_dict._values}            # l_dict.values will be inventory and vrf in order
                save:                                               # The output of the action gets saved respectively in the specified values.
                  - variable_name: "%VARIABLES{l_dict._keys}"       # l_dict.keys will be inventory_save and module_save in order.
                include:
                  - "state"

**Example-2: Loop over a list of device names**

Loop over a list of device names, and run actions 
on the various devices without duplicating that action.

.. code-block:: YAML


    - loop:
        # A loop that runs one action over different devices
        loop_variable_name: devices
        value:         # a list of device names
          - PE1
          - PE2
        parallel: True
        actions:
          - configure:
              # The action name
              alias: execute_
              device: "%VARIABLES{devices}" 
              command: feature bgp

.. note::

  In **Example-2** script would configure 2 devices with same command in parallel, without writing duplicate blocks of text.

**Example-3: Executing actions until the api output is passed** 

Loop over actions for maximum time of 5 seconds, execute actions once (one iteration).
If the result of first action was not equal to "passed",
terminate the loop, else continue until the condition is met or
max_time is reached


.. code-block:: YAML


    - loop:
        # Loop over an action at least running it once and if a condition met terminate the loop
        do_until: "%VARIABLES{api_mtu_size} != passed"
        max_time: 5
        actions:
              - api:
                  alias: api_mtu_size
                  description: get the api value and verify the output
                  device: "%{testbed.devices.PE1.alias}"
                  function: get_interface_mtu_size
                  save:
                    - variable_name: nbc
                  arguments:
                    interface: GigabitEthernet1
              - execute:
                  command: show vrf
                  device: PE2

**Example-4: Executing actions until the api output is passed** 

Looping over an action twice (two iteration) since the range is 2, and each time,
and run a couple of actions in parallel
Also after each parallel call sleep for amount of the range value, so once for one second and the other for two seconds.

.. code-block:: YAML


    - loop:
        range: 2
        loop_variable_name: range_name
        actions:
          - parallel:
            - parse:
                device: PE1
                command: show version
            - execute:
                device: PE2
                command: show version
        - sleep:
            sleep_time: "%VARIABLES{range_name}"

**Example-5: Synchronizing with every_seconds**

The keyword ``every_seconds`` is defined so users can manage their loop and if possible run it with synchronized timing.
If the execution of an iteration of a loop exceeds the time assigned for every_seconds, the loop would still continue its work but a warning would be
printed into the log. **Example-5** shows how ``every_seconds`` work.

This action is looping over a list of size two, hence two iteration and each iteration should take 8 seconds
if the iteration ends in less than 8 seconds, the loop would sleep for the remaining of that time and after reaching 8 seconds
it would execute the other iteration. The total time of execution in this case would be 16 seconds.

.. note::

  Keep in mind if an iteration takes more than 8 seconds the action will continue, it will not terminate after 8 seconds.
  The 8 second is the minimal interval between the loop.

.. code-block:: YAML


    - loop:
        loop_variable_name: banana
        value:
          - version
          - vrf
        every_seconds: 8
        actions:
                - execute:
                    alias: execute_
                    device: uut
                    command: show %VARIABLES{banana}
                - parse:
                    alias: parse_
                    device: uut
                    command: show version

**Example-6: Looping over multiple values**

In case that the goal is to loop over more than one iterable at the same time (over 2 or more list, a combination of lists or dict etc.),
you can define your ``loop_variable_name`` to have a list of variable names along with a list of iterables. Blitz then would zip each iterable to its variable name
accordingly, and use items of multiple iterable within your actions that are iterating.

Below example attempts to reuse items of 3 different lists and print each list item. variable name ``a`` is going to represent list ``[1,2]``, ``b`` is going to represent list ``['d', 'e']``,
and ``c`` will map to [0, 98] 

This way you are iterating over 3 different lists at the same using one single loop.

.. code-block:: YAML

    - loop:
        loop_variable_name: ['a', 'b', 'c']
        value:
            - [1, 2]
            - ['d', 'e']
            - [0, 98]
        actions:
            - print:
                item_a:
                    value: "%VARIABLES{a}"
                item_b:
                    value: "%VARIABLES{b}"
                item_c:
                    value: "%VARIABLES{c}"


The print action here would print ``[1, 'd', 0]`` in the first iteration and in the next iteration it print ``[2, 'e', 98]``.


.. note::

  Make sure that you have a variable name for each iterable that you are defining. Failure to do so would results in failure of the testcase.


**Example-7: Nested looping in Blitz**

There are cases that the users might want to iterate over
various values. Using nested loop would provide users with that functionality. Below shows the example of how you can implement nested loops
in your script.

in this example, the first loop has a dictionary value. The item of the second loop that is nested
in the first loop have access to both the values of the dictionary in the first loop and the list in the second loop.


.. code-block:: YAML

    - loop:
        # looping over a dictionary and applying values within action in same level and actions that re in the nested loop
        loop_variable_name: l_dict
        value:
          inventory_save: inventory
          module_save: vrf
        actions:
          - api:
              device: PE2
              function: get_interface_mtu_config_range
              arguments:
                interface: GigabitEthernet1
              save:
                - variable_name: max
                  filter: get_values('max')
          - loop:
              # Looping on a range of value, this instance it runs twice, you still can use the range number in your actions
              value:
                - show version
                - show vrf
              loop_variable_name: list_name
              actions:
                - parallel:
                  - execute:
                      device: PE1
                      command: show %VARIABLES{l_dict._values}
                      save:
                        - variable_name: "%VARIABLES{l_dict._keys}"
                      include:
                        - "state"
                - execute:
                    command: "%VARIABLES{list_name}"
                    device: PE2


run_condition
^^^^^^^^^^^^^^

It is possible to run (or not run) a set of actions with regards to a conditional statement.
This can be achieved by running actions below the keyword run_condition.
To run actions with a conditional statement, *Blitz* expects:

* An if statement with boolean value (True or False statement).

* A set of actions (e.g parse, execute etc.) that would be specified under keyword ``actions``.

* (Optional) A function that can be the result of all the actions under run_condition if the boolean condition is equal **True**.

* (Optional) A description for logging purposes

The function can be one from this list ``[passed, failed, aborted, skipped, blocked, errored, passx]``.

.. note::

  The function will be applied only if the if statement is equal True, otherwise actions will be running normally.

**Example-1: if statment == True**

All the actions that are under this keyword will be executed

.. code-block:: YAML

    - run_condition:

        if: "2000 == 2000"  
        actions:
          - api:            
              device: "%{testbed.devices.PE1.alias}"
              function: get_interface_mtu_size
              save:
                - variable_name: nbc
              arguments:
                interface: GigabitEthernet1
              include:
                - ">= 1400 && <= 1600"
          - sleep: 
              sleep_time: 1

**Example-2: if statment == False**

All the actions that are under this keyword wont be executed

.. code-block:: YAML

  - run_condition:
    if: "2000 != 2000"  
    actions:
      - api:
          device: "%{testbed.devices.PE1.alias}"
          function: get_interface_mtu_size
          save:
            - variable_name: nbc
          arguments:
            interface: GigabitEthernet1
          include:
            - ">= 1400 && <= 1600"
      - sleep:         # will sleep for a sec
          sleep_time: 1


Using the run_condition, users can evaluate various conditional statements before running their actions.
Examples are provided below for these conditional statements.

**Example-3: running an action if another section has passed**

.. code-block:: YAML

  test:
      source:
          pkg: genie.libs.sdk
          class: triggers.blitz.blitz.Blitz
      devices: ['uut']
      test_sections:
          - plain_actions: 
              - sleep:
                  sleep_time: 10
          - apply_config:
              - run_condition:
                     if: "%VARIABLES{plain_actions} == passed" 
                     actions:
                       - execute:
                           command: show version
                           device: uut
                       - sleep:
                           sleep_time: 1


**Example-3: running an action if another action has passed**

.. code-block:: YAML

    test:
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz
        devices: ['uut']
        test_sections:
            - apply_config:
                - execute:  
                    alias: execute_alias
                    command: show vrf
                    device: uut
                    include:
                        - parser
                - run_condition:
                       if: "%VARIABLES{execute_alias} == passed"
                       actions:
                         - parse:
                             command: show version
                             device: uut
                         - sleep:
                             sleep_time: 1

**Example-4: running an action if another saved_variable has the appropriate output**


.. code-block:: YAML

    # Description: You can check whether if a saved_variable has the appropriate output

    test:
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz
        devices: ['uut']
        test_sections:
            - apply_config:
                - api:                                              # api output is equal to 1500
                     device: uut
                     function: get_interface_mtu_size
                     save:
                       - variable_name: gims_output                 # the 1500 is stored in gims_output
                     arguments:
                       interface: GigabitEthernet1
                - run_condition:
                       if: "%VARIABLES{gims_output} == 1500"        
                       actions:
                         - parse:
                             command: show version
                             device: uut
                         - sleep:
                             sleep_time: 1


**Example-5: check multiple conditional statement**

.. code-block:: YAML

    test:
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz
        devices: ['uut']
        test_sections:
            - apply_config:
                - api:                                              # api output is equal to 1500
                     device: uut
                     function: get_interface_mtu_size
                     save:
                       - variable_name: gims_output                 # the 1500 is stored in gims_output
                     arguments:
                       interface: GigabitEthernet1
                - api:                                              # api output is equal to 1500
                     device: uut
                     function: get_interface_mtu_size
                     save:
                       - variable_name: gims_output_1                 # the 2500 is stored in gims_output
                     arguments:
                       interface: GigabitEthernet10
                - run_condition:
                       if: "%VARIABLES{gims_output} == 1500 and %VARIABLES{gims_output} == 2500"       
                       actions:
                         - parse:
                             command: show version
                             device: uut
                         - sleep:
                             sleep_time: 1

