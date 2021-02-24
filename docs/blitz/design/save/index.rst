.. _save_index:



Save variables
===============


.. toctree::
    :maxdepth: 4
    :hidden:

    filters


Another very useful feature that Blitz has, is the ability to save actions output or a variation of the output.
You can save values to a variable name and later use that variable in other actions. 
There are different ways to save values to a variable and also different ways to reuse them:

* Save the entire output of an action to a variable name.
* Save a part of the output of an action to a variable name.


*Blitz* provides 3 forms of filters that can be applied to an action output and extract a part of the output to be saved

* :ref:`Dq filter<filters>`: This filter is named after our JSON querying tool `Dq <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_. It will apply a query on JSON output and saves a part of a dictionary into a variable.

* :ref:`Regex filter<filters>`: For actions that has string outputs you can apply a regex filter. If regex matches the output, the grouped value, that has a variable name specified like ``(?P<variable_name>)``, will be stored into that variable_name. Below you can find related examples.

* :ref:`List filter<filters>`: It is a specific filter that only can be applied on action outputs that are a list.


Examples of saving variables with or without applying a filter on the action output can be found :ref:`here<filters>`


Re-use variables
===================

The following `example` is showing how to use our specific markup language
to load the saved variable in another action. In this example we save the output
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

Another example of how to use our markup language is provided below. In this example the output of the ``learn``
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


