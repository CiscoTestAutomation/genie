.. _types:


JSON
^^^^^

To query JSON outputs users can take advantage of a tool called Dq. You can find the complete
tutorial of Dq by following this `link
<https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`__.

Actions ``parse``, ``learn`` and ``api`` are benefiting from this feature the most, as they are
the one that are most likely to have a JSON output. You can query a JSON using Dq
and see whether the result of a query is included or excluded in our output.

Below you can see an `example` of using include and exclude on the parsed output of the
command ``show version``.

.. code-block:: YAML

    - apply_configuration:
              - parse:
                  command: show version
                  device: PE2
                  include:

                    # we want to se if the result of this query
                    # is not a empty dictionary
                    - contains('WebUI[\S\s]+', regex=True)
                  exclude:

                    # The output of the query is 'VIRTUAL XE'
                    # but we hope that the key 'platform' has no value
                    # or does not exist within the dictionary by using
                    # the exclude keyword
                    - get_values('platform')

Below you can see an `example` of calling the *get_interface_mtu_config_range* api
within the *trigger_datafile* and checking if certain query results are included or excluded in the output.

.. code-block:: YAML

    - apply_configuration:
        - api: #
            function: get_interface_mtu_config_range
            arguments:
                interface: GigabitEthernet1
            include:

                # Check if the output of this query is not an empty dictionary
                - contains('max')

                # Check if the key 'range' has the value of <1200, 1800>
                - contains_key_value('range', <1200, 1800>)
            exclude:

                # Check if the output of these queries are actually an empty dictionary
                - contains('min-max')

.. note::

    There is no need to use Dq to validate if a dictionary output is equal to an expected dictionary.
    See below example.

.. code-block:: YAML

    # Description: This would check whether the output of the parser is equal to the specified dictionary.
    # No Dq query is needed to perform such validation.

    - parse:
        device: 'N93_3'
        command: 'show module'
        save:
            - variable_name: banana
              filter: contains('lc')
        include:
            -  {'slot': {'lc': {'2': {'40G Ethernet Expansion Module': {'ports': '12',
                'model': 'N9K-M12PQ',
                'status': 'ok',
                'software': 'NA',
                'hardware': '1.2',
                'slot/world_wide_name': 'GEM',
                'mac_address': '88-1d-fc-71-de-38 to 88-1d-fc-71-de-43',
                'serial_number': 'SAL1928K4EG',
                'online_diag_status': 'Pass'}}},
                'rp': {'1': {'1/10G SFP+ Ethernet Module': {'ports': '48',
                   'model': 'N9K-C9396PX',
                   'status': 'active',
                   'software': '9.3(3)IDI9(0.509)',
                   'hardware': '2.2',
                    'slot/world_wide_name': 'NA',
                    'mac_address': '84-b8-02-f0-83-90 to 84-b8-02-f0-83-c7',
                   'serial_number': 'SAL1914CNL6',
                   'online_diag_status': 'Pass'}}}}}
            - contains('lc')
            - get_values('rp')


List
^^^^^
It is also possible to check and see if certain items exist within a output that is a list.

.. code-block:: YAML

  - api:
      device: PE1
      function: get_list_items
      arguments:
          name: [1,2,3,4,5,6,7]       # the output is [1,2,3,4,5,6,7]
      include:
          - 5                         # checks if 5 is in the list
      exclude:
          - 99                        # checks if 99 is NOT in the list

Additionally, you can set a regex and see if that regex matches any item within the list output.

.. code-block:: YAML


  - api:
      device: PE1
      function: get_platform_logging
      include:
          - \*Dec 10 03:2.*     # Check if any item within a list matches this regex
          - "23:31:16.651"
      exclude:
          - name                # Check if any item within a list not matches this regex
          - \*Dec 10 03:2.*


Numerical
^^^^^^^^^^

At this moment, it is only action `api` that supports this feature, as it is the only
action that have ``integer`` and ``float`` outputs.

In below `example` , we want to verify that the numerical output of *get_interface_mtu_size* is
smaller or equal 2000

.. code-block:: YAML

    # code_block_5

    - api: # ACTION
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - <= 2000
        ...

For numerical outputs we support all the common mathematical operations ``{=, >=, <=, >, <, !=}``.

You also can check whether a value is within a certain range. Below
is an `example` of this feature. We want to see if the action output is
greater than 1200 and smaller or equal 1500.

.. code-block:: YAML

    - api: # ACTION
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - ">1200  && <=1500"


If you use the keyword include without specifying any operation the default operation would be
set to ``==`` and by using keyword exclude the operation would be set to ``!=``.
Below you can see an `example` of this.

.. code-block:: YAML

    - api: # ACTION
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - 1500
        exclude:
            - 9999


Boolean
^^^^^^^^

For the actions that have boolean output, it is possible to verify if
the output of the action is equal True/False.

In below `example`, we want to verify if the apis' output is True.

.. code-block:: YAML

    # code_block_5

    - api: # ACTION
        function: verify_device_is_active
        arguments:
            device: PE1
        include:
            - True
        ...
