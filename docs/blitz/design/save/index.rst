.. _save_index:



Save action outputs
===============


.. toctree::
    :maxdepth: 4
    :hidden:

    filters


Another very useful feature that Blitz has, is the ability to save the output of actions or a variation of it.
You can either save values to a variable name and later use that variable in other actions or export to a file that will be saved in the directory where the script was executed. 
There are different ways to save the output and also different ways to reuse them:

* Save the entire output of an action.
* Save a part of the output of an action.


*Blitz* provides 3 forms of filters that can be applied to an action output and extract a part of the output to be saved

* :ref:`Dq filter<filters>`: This filter is named after our JSON querying tool `Dq <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_. It will apply a query on JSON output and save it as a part of a dictionary.

* :ref:`Regex filter<filters>`: For actions that have string outputs you can apply a regex filter. If regex matches the output, the grouped value, that has a variable name specified like ``(?P<variable_name>)``, will be stored.

* :ref:`Regex findall<filters>`: For actions that have string outputs you can apply a regex findall filter. It returns a list of all matches in the output, or an empty list if no match is found.

* :ref:`List filter<filters>`: It is a specific filter that can only be applied to action outputs that are lists.


Examples of saving outputs with or without applying a filter on the action output can be found :ref:`here<filters>`


Re-use variables
===================

The following `example` is showing how to use our specific markup language
to load a saved variable in another action. In this example we save the output
of the *get_interface_mtu_size* api and later use it within the command
of the action ``configure``.

.. code-block:: YAML

    - apply_configuration:
          - api:
              device: PE1
              function: get_interface_mtu_size
              save:
                - variable_name: api_output
              arguments:
                interface: GigabitEthernet1
          - configure:
              device: PE1
              command: |
                router bgp '%VARIABLES{api_output}'

Another example of how to use our markup language is provided below. In this example, the output of the ``learn``
action is saved on variable  *main_learn_output*. Also, a filter is applied on this output and is saved
in variable  *filtered_learn_output*. We later check the inclusion of the *filtered_learn_output*
in action ``execute`` output and print the *main_learn_output* into the console.

.. code-block:: YAML

    - apply_configuration:

          - learn:
              device: PE1
              feature: bgp
              save:
                - variable_name: main_learn_output
                - variable_name: filtered_learn_output
                    filter: raw("[info][instance][default][vrf][default][cluster_id]")
          - execute:
              device: PE1
              command: show version
              include:
                - "w"
                - "%VARIABLES{filtered_learn_output}"
          - print:
              print_item1: "%VARIABLES{main_learn_output}"

.. note::

    Both filter and include/exclude features are using our dictionary querying tool `Dq
    <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_.



Save variables in testscript level
===================================

Up until this point all the examples of saving variables is to save a variable to be able to re-use in other actions but in the same section of the same testcase.
None of those examples shows how to save a variable and later re-use it in another action within another testcases. Examples are provided here that show you how to save variables
that are re-usable every other testcases in the testscript.

In the following example a variable is saved to the variable name `testscript.part` within test1 and later in test 2 it is being re-used
by using ``"%VARIABLES{testscript.part}"``.

.. note::

    It is necessary to name your variable with the prefix ``testscript.`` in order to be able to later on reuse it in other testcase.
    If naming convention is not followed properly the variable cannot be re-used later on.

.. code-block:: YAML

  test1:
      source:
          pkg: genie.libs.sdk
          class: triggers.blitz.blitz.Blitz
      test_sections:
          - global_save:
              - parse:
                  device: PE1
                  command: show version
                  save:
                      - variable_name: testscript.part
                        filter: get_values("rtr_type")
  test2:
  
      source:
          pkg: genie.libs.sdk
          class: triggers.blitz.blitz.Blitz
      test_sections:
          - global_reuse:
            - api:
                function: get_list_items
                common_api: True
                arguments:
                  input: "%VARIABLES{testscript.part}"
                save:
                  - variable_name: item


Save action outputs to files
===================================

Action results can be saved in both variables and files and all filters applicable to variables can also be applied when saving to files.
To save the result of an action to a file, you need to use the `file_name` argument. An example can be seen below:

.. note::

    A file with the name informed in file_name will be created in the runinfo directory.

.. code-block:: YAML

  testsave:
      source:
          pkg: genie.libs.sdk
          class: triggers.blitz.blitz.Blitz
      test_sections:
          - apply_configuration:
                - parse:
                      command: show version
                      device: R1_xe
                      save:
                          - file_name: file.txt
                            filter: get_values("rtr_type")


Moreover, it is possible to save multiple results in the same file. For this to happen, you 
must also use `append: True`. The output (or the result of a filter) will be appended to an existing file or create it if it does not yet exist.

In the example below, you can see how this can be achieved. 
The parsed output of `show version` is saved to a variable named `parse_output` and also saved to a file named `file.txt`.
After that, the parsed output is filtered using `get_values("rtr_type")` and the result of this operation is appended to the same file.

.. code-block:: YAML

  testsave:
      source:
          pkg: genie.libs.sdk
          class: triggers.blitz.blitz.Blitz
      test_sections:
          - apply_configuration:
                - parse:
                      command: show version
                      device: R1_xe
                      save:
                          - variable_name: parse_output
                            file_name: file.txt
                          - file_name: file.txt
                            filter: get_values("rtr_type")
                            append: True
