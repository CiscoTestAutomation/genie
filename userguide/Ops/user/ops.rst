.. _user_ops:

Ops Use
========

This section describes how ``Genie`` `ops` collects
operational data from features already configured on the testbed.

Introduction
------------

``Genie`` `Ops` represents a device/feature's operational state/data through Python
object. Each `feature` on each device is represented via a single `Ops` object
instance, where state/status information is stored as an object attribute.

.. note::

    A feature can be any Protocol (L2/L3) and also any hardware (Linecard,...).

`Ops` objects are snapshots of a particular `feature` on a particular `device` at
a specific time.

A `feature`'s  state/operational information are gathered with the help of
many commands, like Cli, Yang, and XML. This information is stored in
one `feature` object. Each command executed for collecting the required
information in building the `Feature` object are then parsed; specific
information is collected and re-grouped into one common structure within
the `Feature` object, common to all operating systems.

``Genie`` objects work across multiple operating systems and management protocols.
We refer to the different management protocols as `context`.  This is
done with the :ref:`abstract <abstract>` package and the right :ref:`directory
structure<structure>`. 

The application and use of ``Genie`` `ops` can be summed up in three steps:

1. Create an abstract object;
2. Instantiate an `ops` object with the specific `device`; and
3. Learn the `Feature`.

After the final step, you can generate an object which contains all the states and the status of
the `Feature` on this particular `Device` for a particular os type, and
management type.

Let's demonstrate this using an example:

.. code-block:: python

    # Let's assume we have a device object
    >>> device
    <Device w at 0xf76a4fac>

    # And a variable holding context, which can hold Cli, Yang, or XML.
    # The default value is Cli
    >>> device.context
    'cli'

    # Step 1 - Abstract
    >>> from genie.abstract import Lookup
    >>> from genie.libs import ops

    # Create the abstract object following device os, management protocol
    >>> lookup = Lookup(device.os, device.context)

    # Step 2
    >>> ospf = lookup.ops.ospf(device=device)

    # Step 3
    >>> ospf.learn()

    # ... retrieve information from ospf
    >>> ospf.name
    ...

.. _user_ops_polling:

Polling Mechanism
-----------------

``Genie`` also provides a polling mechanism to verify if the `feature` is in
the expected state. This can be useful when a `feature` has been recently configured and is not
yet stable. `learn_poll` accepts a `verify` function that verifies the state
of the object.  `learn_poll` works like this:

1. Learn the `Feature`;
2. Call the `verify` function; and
3. a) If there is no exception, then the `feature` has been learnt.
   b) If there is an exception at either step (1) or (2), then sleep for a
      period of time and try again.

`learn_poll` accepts the following arguments:

* `sleep` must be an `int`, representing the time to sleep between attempts,
  in seconds.
* `attempt` must be an `int`, representing how many attempts to do.
* `verify` must be a `callable`. This `callable` will receive the `feature` as an
  argument. If no exception is raised, then it has passed. If any exception is
  raised, then it will try again.
* `kwargs` any extra argument will be sent as passthrough to the `verify`
  function.

.. code-block:: python

    def verify_function(obj, arg1, arg2):
        # Obj is the feature object which is being learnt
        # <Verify information about the obj>
        # Make sure the name was learnt
        assert obj.name

    # Let's assume we have a device object
    >>> device
    <Device w at 0xf76a4fac>

    # And a variable holding context, which can hold Cli, Yang, or XML.
    >>> context
    'cli'

    # Step 1 - Abstract
    >>> from genie.abstract import Lookup
    >>> from genie.libs import ops

    # Create the abstract object following device os, management protocol
    >>> lookup = Lookup(device.os, context)

    # Step 2
    >>> ospf = lookup.ops.ospf(device=device)

    # Step 3
    # Will learn ospf and verify if it was learnt correctly with
    # verify_function. It will try up to 5 times, and sleep 30 seconds between
    # each attempt.
    >>> ospf.learn_poll(verify=verify_function, sleep=30, attempt=5,
                        arg1=1, arg2=2)

    # retrieve information from ospf
    >>> ospf.name
    ...


Extra Features
--------------

There a few other features available for `ops` objects.

.. _user_ops_extra_diff:

**1. Comparing two ops objects**

As the `ops` objects are snapshots taken at a specific time, we can take a snapshot
before doing an action, and another after the action. Then we can
compare both snapshots to see if they are equal and what, if anything, has been 
modified.

``Genie`` `ops` objects can be compared simply by using the `==` sign, the python
equality operator.

.. code-block:: python

    pre_ospf = Ospf(device=device)
    pre_ospf.learn()
    # Do some action
    post_ospf = Ospf(device=device)
    post_ospf.learn()

    pre_ospf == post_ospf
    # True/False depending on the action

This returns `True/False`.

We are also providing a more complete `diff` tool, to compare those objects.

.. code-block:: python

    pre_ospf = Ospf(device=device)
    pre_ospf.learn()
    # Do some action
    post_ospf = Ospf(device=device)
    diff = pre_ospf.diff(post_ospf)

    print(diff)
    # It will show a diff between pre_ost and post_ospf following this syntax
    #   <variables>:
    #     [key]:
    # -     [more keys]:previous value
    # +     [more keys]:new value

    # For example
    #   process_id:
    #     1:
    #       vrf:
    #         blue:
    # -         age: 3
    # +         age: 5

    # And so on...

With `diff` object, you can also retrieve a list of `diff items` which were
added, modified or removed. These lists can be printed to return
the strings which were modified.

.. code-block:: python

    pre_ospf = Ospf(device=device)
    pre_ospf.learn()
    # Do some action
    post_ospf = Ospf(device=device)
    diff = pre_ospf.diff(post_ospf)

    # It will return a list of the diff items.
    items = diff.diffs
    for item in items:
        print(item)
    # + process_id:
    # +   1:
    # +     vrf:
    # +       blue:
    # +         value: 5


For both cases, (using `==` or `diff`), attribute `diff_ignore` can 
restrict which keys to compare. It is a list where each item of the list is a
string which has almost the same syntax as `src` and `dest`. The only
difference is the regex syntax is simplified, even though the most verbose one
with group is still accepted.


.. code-block:: python

    pre_ospf = Ospf(device=device)
    pre_ospf.learn()
    # Do some action
    post_ospf = Ospf(device=device)
    post_ospf.learn()

    pre_ospf == post_ospf
    # Let's assume age is a dynamic value, which keep changing and shouldn't
    # be compared

    pre_ospf.diff_ignore.append('name[process_id][(.*)][vrf][(.*)][age]')
    post_ospf.diff_ignore.append('name[process_id][(.*)][vrf][(.*)][age]')

    pre_ospf == post_ospf
    # True

.. _user_ops_extra_attributes:

**2. Restrict which attributes/keys of the object will be created**

In some scenarios, we may not need to learn all the `Feature`
attributes/keys, but only need specifics ones (as it takes execution time).
When creating the `ops` object, argument `attributes` can be given to 
specify which attributes/keys we want to create. Only the
commands(cli/Yang/Xml) related to the attribute(s)/key(s) will be sent to the
`Device`.

`Attributes` is a list, where each item represents a specific location that
we want to create in the `osp` object. The syntax is the same as
dictionary lookup, where the quotes are removed, and the first
word of the string represents the variable name. It also supports regexp
syntax, so many matching keys can be built.

.. code-block:: python

    # Only build ospf.name
    # For all process id, all vrf, only interface.
    ospf = Ospf(device=device,
                attributes=['name[process_id][(.*)][vrf][(.*)]['interface'])
    ospf.learn()
    print(ospf.name)

    {'process_id': {'1': {'vrf': {'blue': {'interface': {'eth3/1': {'ip_address': '1.1.1.1',
                                                                    'state': 'up'}}},
                                  'orange': {'interface': {'eth3/2': {'ip_address': '1.1.1.2',
                                                                      'state': 'up'}}}}},
                    '2':{'vrf':{'orange': {'age':6,
                                           'interface': {'eth3/5': {'ip_address': '1.1.1.4',
                                                                    'state': 'up'}},
                                           'router_id': 15}}}}}


We can see all the information not related to interface has not been built.
Only the commands related to interface has been sent to the `Device`.  The big
advantage is to save execution time, when only specific values are desired.
