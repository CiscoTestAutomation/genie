.. _utils_overview:

Useful Libraries
================

This section contains many useful apis to help with the development of Genie
Triggers or pyATS testscripts.

Dq
--

Dictionary query allow to question Python dictionary in a very
intuitive syntax.

Find all the bgp neighbors which are `Established`.

.. code-block:: python

  # Find all the bgp neighbors which are Established
  >>> output = device.parse('show bgp neighbors')
  >>> output.q.contains('Established').get_values('neighbor')

  # effectively, device.parse() API returns a modified parsed dictionary
  # enabling you to make quick accesses to the Dq object without having to be
  # explicit. This is equivalent to:

  >>> from genie.utils import Dq
  >>> output = device.parse('show bgp neighbors')
  >>> Dq(output).contains('Established').get_values('neighbor')
  ['10.2.2.2']

This navigate the dictionary nested structure, find all the keys and value
which contains the `established`, return a list of neighbor.

Find all the routes which are `connected`.

.. code-block:: python

  >>> output = device.parse('show ip route')
  # Find all the routes which are Connected
  output.q.contains('connected').get_values('routes')
  ['10.0.1.0/24', '10.1.1.1/32', '10.11.11.11/32', '172.16.21.0/24']

Find all the `ospf` routes.

.. code-block:: python

  # Find all the routes for Ospf
  output.q.contains('ospf').get_values('routes')
  ['10.0.2.0/24', '10.2.2.2/32']

**Typically to do the same, you would need for loops, if statement, and so on. Dq
simplify the whole process!**

Last but not least Dq supports regex (regular expression).

.. code-block:: python

  # Check if the module in line card #4 contains a status 
  # and its value is ok or active
  output.q.contains('lc').contains('4').contains_key_value('status', 'ok|active', value_regex=True)
  {'lc': {'4': {'NX-OSv Ethernet Module': {'status': 'ok'}}}})


Dq support multiple Api, where each chain with each other. Dq builds its own
datastructure, which is a :pyats:`ListDict <http>`, you can reconstruct it as a real
dictionary with the matching requirements with the api `reconstruct`.

Dq supports the following chain'd action.

contains
^^^^^^^^

Filters down the dictionary and only keep the paths which contains the provided
value. It will not keep anything else.

.. code-block:: python

  >>> output = dev.parse('show module')
  >>> output.q.contains('lc')
  >>> output.q.contains('lc').contains('4')

To make contains work with a regex input all you have to do is to set the regex
variable to ``True`` within the contains api arguments, as shown in examples below

.. code-block:: python

  >>> output = dev.parse('show module')
  >>> output.q.contains('[1,2]', regex=True)
  >>> output.q.contains('.*ware', regex=True)

To do a case insensitive comparison in contains you have to set both regex and ignore_case variables to ``True``.

.. code-block:: python

  >>> output = dev.parse('show module')
  # Ignores case sensitive for the value Model
  >>> output.q.contains('Model', regex=True, ignore_case=True)

By giving `level`, grab information from upper/lower level. In case of `level=-1`, it means information from 1 above level will be collected.

.. code-block:: python

  >>> output = dev.parse('show module')
  >>> output.q.contains('.*ware', regex=True, level=-1)

not_contains
^^^^^^^^^^^^

Only keep the paths which does not contains the provided value. Very useful to
remove unwanted path, and have a dictionary which only have the desired
keys/paths.

.. code-block:: python

  >>> output = dev.parse('show module')
  # Remove all linecard information from the parsed output
  >>> output.q.not_contains('lc')
  # Remove all linecard number 4 information from the parsed output
  >>> output.q.contains('lc').not_contains('4')
  # Remove all linecard number 4information from the parsed output and save as
  # a new dictionary
  >>> new_dict = output.q.contains('lc').not_contains('4').reconstruct()

Again, you can exclude the unwanted paths, with entering a regular expression
input. 

.. code-block:: python

  >>> output = dev.parse('show module')
  # Remove all the keywrods that has address or number in them 
  >>> output.q.not_contains('.*(address|number).*', regex=True)
  # Remove all the linecards and router processor that has the id 1 or 4
  # As well as remove all the keywords that ends with phrase ware.
  >>> output.q.not_contains('1|4', regex=True).not_contains('.*ware', regex=True)

As same as `contains`, `level`, `ignore_case` argument can be passed to `not_contains`.

.. note::

    `level` argument is supported only for `contains` and `not_contains`

get_values
^^^^^^^^^^

Return a list of the values of the key.

.. code-block:: python

  >>> dev.parse('show module').q.contains('ok').get_values('lc')
  ['2', '3', '4']

`get_values` is very powerful, as it allows to collect all the values of a
specific key. It also supports the nested index.

.. code-block:: python

  >>> dev.parse('show interface').q.get_values('[0]')
  ['mgmt0', 'Ethernet2/1', 'Ethernet2/2', 'Ethernet2/3', 'Ethernet2/4', 'Ethernet2/5']

Only one value can be collected by using `index` and it returns without list.
And slicing in `index` is also possible. Slicing is exact same with what we can 
do with list in Python.

.. code-block:: python

  >>> dev.parse('show interface').q.get_values('[0]', 0)
  'mgmt0'

  >>> dev.parse('show interface').q.get_values('[0]', '[0:2]')
  ['mgmt0', 'Ethernet2/1']

get_value does not return a Dq object, considered a "Final" api.

contains_key_value
^^^^^^^^^^^^^^^^^^

Similar to `contains` except instead of only the expected value the parent key is also
provided. `contains_key_value` accept two arguments. One is the parent key, and
the key. Both must be following each other. The difference with `contains` is
that the value can be anywhere in the nested dictionary.

It is very useful for common value, which can be present at multiple location
in the dictionary.

.. code-block:: python

  >>> output = dev.parse('show module')
  # Filter down on the first rp.
  >>> output.q.contains_key_value('rp', '1')
  >>> dev.parse('show interface').q.contains_key_value('enabled', True).get_values('[0]')
  ['mgmt0', 'Ethernet2/1', 'Ethernet2/2', 'loopback0', 'loopback1']

To input regular expression values, if looking for keys with a regex pattern you need to set
``key_regex`` to True. For applying regex pattern on values, you need to set ``value_regex`` variable
to True. Examples below elaborate this functionality

.. code-block:: python

  >>> output = dev.parse('show module')
  # If only searching for a value with regex
  >>> output.q.contains_key_value('model', 'N7K.*', value_regex=True)
  # If only searching for a key with regex
  >>> output.q.contains_key_value('[1,2,3]', 'NX-OSv Ethernet Module', key_regex=True)
  # If searching for both key and value using regex
  >>> output.q.contains_key_value('slot/world_wide_name|mac.*|model', '[a-zA-Z0-9\-\s]+', key_regex=True, value_regex=True)

Similar to ``contains`` here also you can do case insensitive comparison.
- If the ``key`` has to be case insensitive then you have to set ``key_regex`` and ``ignore_case_key`` as True.
- If the ``value`` has to be case insensitive then you have to set ``value_regex`` and ``ignore_case_value`` as True.

.. code-block:: python

  >>> output = dev.parse('show module')
  # Ignores case sensitive for key CHECKSUM and value 0x1abc
  >>> output.q.contains_key_value('CHECKSUM', '0x1abc', key_regex=True, ignore_case_key=True,\
      value_regex=True, ignore_case_value=True)

not_contains_key_value
^^^^^^^^^^^^^^^^^^^^^^

The opposite of contains_key_value. Only keep the path which does not contains
the provided value.

.. code-block:: python

  >>> output = dev.parse('show module')
  # Filter down on all the other module than rp 1
  >>> output.q.not_contains_key_value('rp', '1')

Similar rules for regex is applied as what was already explained for contains_key_value
api.

.. code-block:: python

  >>> output = dev.parse('show module')
  # if applying regex only for value set value_regex=True
  >>> output.q.not_contains_key_value('lc', '(3|4)', value_regex=True)

This one also supports both ``ignore_case_key`` and ``ignore_case_value`` which was already explained for contains_key_value api.

value_operator
^^^^^^^^^^^^^^

Filter down based on the value of a certain key with {==, !=,  >=, <=, >, <}

.. code-block:: python

   # Get all path which has crc_error greater than 100
   >>> output = dev.parse('show interfaces')
   >>> output.q.value_operator('in_crc_errors', '>', 100).get_values('[0]')
   []

sum_value_operator
^^^^^^^^^^^^^^^^^^

Filter down based on the value of a certain key and sum up the values and evaluate with {==, !=,  >=, <=, >, <} against the total value.
Comparing to value_operator, this allows you to sum up the values from structure data and create new value as total. This operator helps you to reduce steps to calculate the values in your python code. For example, below snipped code gathers all 'in_rate' from 'show interfaces' and you will be able to check how much incoming rate has on the device instead of checking per interface.

.. code-block:: python

   # sum up all path which has in_rate and check if the total value is greater than 100
   # and then get the total value via get_value()
   >>> output = dev.parse('show interfaces')
   >>> output.q.sum_value_operator('in_rate', '>', 100).get_values('[0]')
   145000.0

count
^^^^^

Count how many element match the requirement.

.. code-block:: python

   >>> output = dev.parse('show interfaces')
   # Count how many interfaces which has in_crc_error greater than 100
   >>> output.q.value_operator('in_crc_errors', '>', 100).count()
   0

Does not return a Dq object, considered a "Final" api.

raw
^^^

Straight dictionary access.

.. code-block:: python

   >>> mod.raw('[slot][rp][1][NX-OSv Supervisor Module][model]')
   'N7K-SUP1'

Does not return a Dq object, considered a "Final" api.

reconstruct
^^^^^^^^^^^

Rebuilds a dictionary from a Dq object once filtered down.

.. code-block:: python

   >>> output = dev.parse('show interfaces')
   # Count how many interfaces which has in_crc_error greater than 100
   >>> new_dict = output.q.value_operator('in_crc_errors', '>', 100).reconstruct()

Variable `new_dict` is now a dictionary which contains all the interfaces which
have an in_crc_error greater than 100.

Example
^^^^^^^^

Here is an examples on how to use it

1) Get ntp associated server

.. code-block:: python

    # Get testbed file
    >>> from genie.testbed import load
    >>> tb = load('testbed.yaml')
    >>> dev = tb.devices['nx-osv-1']
    >>> dev.connect()
    >>> parsed_output = dev.parse('show ntp associations')
    >>> parsed_output.q.contains('mode').get_values('peer')
    ['192.168.1.10']

2) Get all interfaces which have in_crc_errors

.. code-block:: python

   >>> new_dict = output.q.value_operator('in_crc_errors', '>', 100).get_values('[0]')
   ['Ethernet2/1']

It is very easy to verify any keys like this with Dq.

query_validator
^^^^^^^^^^^^^^^

Dq accepts query strings (Method ``str_to_dq_query``) and can be verified with query_validator.
If it is valid it will return True, otherwise False. It is a staticmethod, hence it can be used without instantiate Dq.

Example
^^^^^^^

.. code-block:: python

    >>> from genie.utils import Dq
    >>> s = "contains_key_value('a', 'b')"
    >>> Dq.query_validator(s)
    True
    >>> s = "dont_exists('a', 'b')"
    >>> Dq.query_validator(s)
    False


str_to_dq_query
^^^^^^^^^^^^^^^

This function accepts a string and convert it to the proper DQ query, 
create a Dq object, create the query and call the functions, and returns the output.
It is a staticmethod, hence it can be used without instantiate Dq.

Example
^^^^^^^^

.. code-block:: python

    # mod is a valid dictionary object
    >>> Dq.str_to_dq_query(mod, "contains('rp')")
    {'rp': {'1': {'NX-OSv Supervisor Module': {'ports': '0', 'model': 'N7K-SUP1', 'status': 'active', 'software': '7.3(0)D1(1)', 
    'hardware': '0.0', 'slot/world_wide_name': '--', 'mac_address': '5e-00-40-01-00-00 to 5e-00-40-01-07-ff', 
    'serial_number': 'TM40010000B'}}}}

.. code-block:: python

    # mod is a valid dictionary object
    >>> Dq.str_to_dq_query(mod, "contains('lc').not_contains('2').get_values('slot/world_wide_name')")
    ['--', 1, 2, 3]

Timeout
-------

In any kind of automation, there is a need of polling. Try to do a
check/action, verify if expected result is there, otherwise, sleep for a defined time
and repeat up to a defined maximum time.

Class `Timeout` was made to do this.

.. code-block:: python

    from genie.utils.timeout import Timeout
    # Try up to 60 seconds, and between interval wait 10 seconds, display timeout logs
    timeout = Timeout(max_time = 60, interval = 10, disable_log = False)

    while timeout.iterate():
        ret = do_something(**kwargs)
        if ret is None:
            return
        # Didn't get expected result, keep trying
        timeout.sleep()


When the maximum time is reached, an `TimeoutError` is raised. Timeout can be
used to time limit a trigger, to time limit a specific action.

This api is very useful for any kind of polling.

TempResult
----------

`TempResult` stores a temporary result. This is useful to keep in memory the
result, without committing it to the testcase yet. `TempResult` follows the
:pyats_rollup:`pyATS Rollup <http>` concept. Once ready, the result can
be applied on the container, either to a section or to a step.

.. code-block:: python

    # Starts with no result, let's assume we are within a step container is a
    # step, however it also work at a section level.
    from genie.utils.timeout import TempResult

    with steps.start('the first step') as step:
        temp = TempResult(container=step)

        # Set result to be passed. If we did temp.result() the step result would be
        # passed
        temp.passed('Some pass message')

        # Set result to be errored. If we did temp.result() the step result would be
        # errored
        temp.errored('Some error message')

        # Errored + passed = Error, so temp result is still errored
        temp.passed('Some pass message')

        # The step has final result of errored.
        temp.result()

.. note::

    container can also be a section, in this case just pass container=self


Diff
----

Genie comes with a very useful `dict` and `object` diff tool. Provided two
dictionaries, or object, it will go through every branch and compare all the
keys. At the end, it provides a Linux look-a-like diff.

.. code-block:: python

        >>> from genie.utils.diff import Diff
        >>> a = {'a':5, 'b':7, 'c':{'ca':8, 'cb':9}}
        >>> b = {'a':5, 'f':7, 'c':{'ca':8, 'cb':9}}

        >>> dd = Diff(a,b)
        >>> dd.findDiff()
        >>> print(dd)
        +f: 7
        -b: 7

It also supports an exclude key, for the keys that shouldn't be compared.

.. code-block:: python

        >>> from genie.utils.diff import Diff

        >>> a = {'a':1, 'b':2, 'c':{'ca':9}}
        >>> c = {'a':2, 'c':3, 'd':7, 'c':{'ca':{'d':9}}}

        >>> dd = Diff(a, c, exclude=['d'])
        >>> dd.findDiff()
        >>> print(dd)
        -b: 2
        +a: 2
        -a: 1
        c:
        + ca:
        +  d: 9
        - ca: 9

You can also only see which one were added

.. code-block:: python

        >>> dd = Diff(a, c, mode='add')
        >>> dd.findDiff()
        >>> print(dd)
        +d: 7

Or Removed

.. code-block:: python

        >>> dd = Diff(a, c, mode='remove')
        >>> dd.findDiff()
        >>> print(dd)
        -b: 2

Or modified, which mean it existed, but the value was modified

.. code-block:: python

        >>> dd = Diff(a, c, mode='modified')
        >>> dd.findDiff()
        >>> print(dd)
        +a: 2
        -a: 1
        c:
        + ca:
        +  d: 9
        - ca: 9

If you need a string representation of added items without diff labeling, you can do

.. code-block:: python

        >>> a = {'a': 1, 'w': 5, 'p': {'q': {'a': 6}}}
        >>> c = {'b': 2, 'c': {'d': {'e': {'f': 2, 'g': 5}}}}
        >>> dd = Diff(a, c)
        >>> dd.findDiff()
        >>> print(dd.diff_string('+'))
        b 2
        c
         d 
          e 
           f 2
           g 5

Similarly, you can get a string for the removed items

.. code-block:: python

        >>> dd = Diff(a, c)
        >>> dd.findDiff()
        >>> print(dd.diff_string('-'))
        a 1
        p
         q
          a 6
        w 5

To print unchanged entries in a list or tuple, you can specify the `verbose`
option like so

.. code-block:: python
        
        >>> a = { 'key': {'value': [1, 2, 3, 4]}}
        >>> b = { 'key': {'value': [1, 3, 3, 4]}}
        >>> dd = Diff(a, b, verbose=True)
        >>> dd.findDiff()
        >>> print(dd)
        key:
         value:
          index[0]: 1
        - index[1]: 2
        + index[1]: 3
          index[2]: 3
          index[3]: 4

Diff is used everywhere within Genie, for the `PTS` comparison, ops comparison,
within Triggers. It is another important key component of Genie.

The same can be done with objects. Currently it supports `Genie.conf` and
`Genie.ops` objects.

Config
------

`Config` object store device `show-running` outputs into structure data. This
structure data can then be used to compare show-running over time.

.. code-block:: python

    from genie.utils.config import Config
    cfg = '''\
    service unsupported-transceiver
    hostname PE1
    clock timezone PDT -7
    exception pakmem on
    exception sparse off
    exception kdebugger enable
    logging buffered 120000000
    telnet vrf default ipv4 server max-servers 10
    cdp
    line template vty
     timestamp disable
     exec-timeout 0 0'''
    
    config = Config(cfg)
    config.tree()
    
    >>> pprint.pprint(config.config)
    {'cdp': {},
     'clock timezone PDT -7': {},
     'exception kdebugger enable': {},
     'exception pakmem on': {},
     'exception sparse off': {},
     'hostname PE1': {},
     'line template vty': {' exec-timeout 0 0': {}, ' timestamp disable': {}},
     'logging buffered 120000000': {},
     'service unsupported-transceiver': {},
     'telnet vrf default ipv4 server max-servers 10': {}}

This dictionary can then be used with the diff tool to compare two configuration.

Find
----

The `Find` api is the a very important of Genie. It's such a great tool, that
it was provided to pyATS. Read on it on the :pyats_find:`pyATS website <http>`.
