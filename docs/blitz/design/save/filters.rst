.. _filters:



Save with No filter
^^^^^^^^^^^^^^^^^^^^

Below you can find examples of how to save the entire output to a variable name and/or a file.

.. code-block:: YAML

    # Description: Saving the entire output of an execute action into a variable
    # The type of output is string

    - Execute:
        device:  '%{testbed.devices.uut.alias}'
        command: show platform
        save:
          - variable_name: execute_output

.. code-block:: YAML

    # Description: Saving the entire output of an execute action into a variable
    # The type of output is dictionary/JSON data.

    - parse:
        device:  '%{testbed.devices.uut.alias}'
        command: show platform
        save:
          - variable_name: execute_output

In the example below, the same action output is saved to a file. 
All you need to do is provide the file name using the argument `file_name`.

.. code-block:: YAML

    # Description: Saving the entire output of an execute action into a file
    # The type of output is dictionary/JSON data.

    - parse:
        device:  '%{testbed.devices.uut.alias}'
        command: show platform
        save:
          - file_name: testfile.txt

Save with Dq filter
^^^^^^^^^^^^^^^^^^^^

Below you can see an example of Dq filter.

.. code-block:: YAML

    # **Description: Applying a dq query and save the outcome into the variable parse_output.**
    # Later on checking if that value exist in action execute output.
    # Dq query only works on outputs that are dictionary

    - apply_configuration:
          - parse:
              command: show module
              device: PE2
              save:
                - variable_name: parse_output
                  filter: contains('ok').get_values('lc', index=2)
                  # The output is '4'
          - execute:
              device: PE1
              command: show version
              include:
                - "w"
                # check if '4' exists within the result of this action
                - "%VARIABLES{parse_output}"

Save with Regex filter
^^^^^^^^^^^^^^^^^^^^^^^

Below you can see an example of regex filter.

.. code-block:: YAML

    # first saving values from execute action output
    # later on printing those values

    - execute:
        device: N93_3
        command: show version
        save:
        - filter: BIOS:\s+version\s+(?P<bios>[0-9A-Za-z()./]+).*                        # bios version is 07.33
          regex: true
        - filter: bootflash:\s+(?P<bootflash>[0-9A-Za-z()./]+)\s+(?P<measure>\w+).*     # bootflash is  51496280 and measure is KB
          regex: true
    - print:
        bios:
          value: "The bios version is %VARIABLES{bios}"
        bootflash:
          value: "The bootflash is %VARIABLES{bootflash} and %VARIABLES{measure}"

Save with Regex findall filter
^^^^^^^^^^^^^^^^^^^^^^^

Below you can see an example of regex_findall.
In this example, execute_output would contain a list of strings such as: 
['172.16.1.254', '10.1.1.1', '10.2.2.2', '10.3.3.3', '10.4.4.4']

.. code-block:: YAML

    # saves a list of values from execute action output

    - execute:
        device: PE1
        command: show ip interface brief
        save:
        - variable_name: execute_output
          regex_findall: (\d+\.\d+\.\d+\.\d+)   # returns a list of IP addresses

Save with List filter
^^^^^^^^^^^^^^^^^^^^^^

For actions that has list outputs you can get an index or a part of a list and save it into a list with a desired variable_name.
You can also specify a regex value and match it against all the items within that list, and get a list of
all the matched items.

Below you can see an example of list filter.

.. code-block:: YAML

    # saves various items of a list with a variable

    - api:
        device: PE1
        function: get_list_items
        arguments:
            name: [{'a': 1}, {'d': {'c': 'name1'}}, [1,2,34], {'e': ['a', 'b', 'c']}]
            index: 0
            index_end: 5
        save:
            - variable_name: list_int5          # the output is [{'a': 1}, {'d': {'c': 'name1'}}, [1,2,34], {'e': ['a', 'b', 'c']}]
              list_index: "[0:2]"               # saves items 0,1 from the above array of itmes => [{'a': 1}, {'d': {'c': 'name1'}}]
                                                # into a list named list_int5

            - variable_name: list_int7          # saves item #2 in the array =>[[1,2,34]] into a list name list_int7
              list_index: 2

            - variable_name: list_int8          # saves the entire array in a list named list_int8

    - api:
        device: PE1
        function: get_platform_logging
        save:
            # apply regex filter to items and save a list of matches
            - variable_name: platform_log                                   # The output to save value from is a list of platform logs
              filter: Oct\s+15[\S\s]+Configured from console by console$    # checks if any item in the list matches this filter and
                                                                            # save it in a list named platform_log

