.. _maker:

Maker
=====

Overview
--------

`Maker` simplifies the process of mapping parsers' output to
the `ops` object attributes.

To help users understand exactly how `Maker` works, let's begin with an example.
Let's say we have a parser that returns the following dictionary:

.. code-block:: text

     process_id:
         1
             vrf
                 blue
                     id:2
                     age:3
                 orange
                     id:5
                     age:6
         2
             vrf
                 default
                     id:12
                     age:13
                 orange
                     id:15
                     age:16

Although this parser output is good, let's say we want to rename `id` to `router_id`.

.. code-block:: text

    <id>
        vrf
            <vrf>
                router_id:<value>
                age:<value>

To achieve this, we would likely use the following code:

.. code-block:: python

    # Copy dictionary, as we want to modify it, but we cannot modify a dictionary
    # we are looping over
    import copy
    dict_tmp = copy.deepcopy(output)

    for pid, pid_value in dict_tmp['process_id'].items():
        for vrf, vrf_value in  pid_value['vrf'].items():
            if 'id' in vrf_value:
                # Got the place, but we cannot modify the dictionary
                # But we took a copy, so we can modify the output itself with
                # the keys
                output['process_id'][pid]['vrf'][vrf]['router_id'] = vrf_value['id']
                del output['process_id'][pid]['vrf'][vrf]['id']

Users would need to rely on this boiler-type code for every name change. 

Now, let's imagine the user also wanted to change the received structure to look like this: 

.. code-block:: text

    <vrf>
        process_id
            <id>
                router_id:<value>
                age:<value>

This code is repetitive and difficult to maintain. Now, imagine merging two
structured outputs like this into one common structure, this becomes even more redundant 
and even more difficult to read than the previous example. 

Fortunately, `Maker` overcomes this repetition and redundancy. `Maker` can:

- Rename key names from parser outputs; 
- Modify a structure to any new structure; and
- Merge and modify multiple parser outputs into a specific object structure.

This quick example below shows how easily the previous code can be modified using `Maker`:

.. code-block:: python

    from genie.ops.base.maker import Maker

    # Create a class for MyFeature
    class MyFeature(object):
        def learn():
            m = Maker(parent=self)

            m.add_leaf(device=device,
                       cmd=<parser>,
                       src='[process_id][(?P<process>.*)][vrf][(?P<vrf>.*)][age]',
                       dest='process[(?P<process>.*)][vrf][(?P<vrf>.*)][age]')

            # Rename Id to router_id
            m.add_leaf(device=device,
                       cmd=<parser>,
                       src='[process_id][(?P<process>.*)][vrf][(?P<vrf>.*)][id]',
                       dest='process[(?P<process>.*)][vrf][(?P<vrf>.*)][router_id]')

            m.make()

    feature = MyFeature()
    feature.learn()

    print(feature.process)
    {'1':{'vrf':{'blue':{'router_id':2, 'age':3}}}}

add_leaf
--------

Using `leaf`, `Maker` can retrieve the parsed output, navigate the parsed
output, and create the values.

`add_leaf` supports the following arguments:

.. code-block:: text

    +--------------------------------------------------------------------------+
    | maker.add_leaf                                                           |
    +==========================================================================+
    | Arguments             | Description                                      |
    |-----------------------+--------------------------------------------------|
    | device                | Device object                                    |
    | cmd                   | Metaparser parser class                          |
    | src                   | Path of the values this leaf is interested into  |
    | dest                  | Location of where to store it into `parent`      |
    | callables             | Map callables strings to callable                |
    | action                | Action to take on the output                     |
    +==========================================================================+

`src` looks into the parsed output for values at a specific location. The output is stored 
and then placed at the `dest` location inside the `self` object.

In short, `src` is the parser structure and `dest` is the user-defined `feature` structure.

For example:

.. code-block:: python

    m = maker(parent=self)

    m.add_leaf(device=device,
               cmd=<parsers>,
               src='[process_id][1][vrf][blue][id]',
               dest='process[1][vrf][blue][router_id]')

    # Can then be retrieve via
    # m.process['1']['vrf']['blue']['router_id']

This example reads as follows: 

1. Look inside the returned parsed output of the parser for `['process_id']['1']['vrf']['blue']['id']` 
2. Store it inside the `feature` object as `['1']['vrf']['blue']['router_id']`
3. Which can be retrieved via `parent.process`, where process is the name given in `dest`.

However, `1` and `blue` are hardcoded. We can do better than this, and make it
**dynamic**. We use regex symbolic group name in `src` and `dest` to generate dynamic value.

.. code-block:: python

    m = maker(parent=self)
    m.add_leaf(device=device,
               cmd=<parsers>,
               src='[process_id][(?P<process>.*)][vrf][(?P<vrf>.*)][id]',
               dest='process[(?P<process>.*)][vrf][(?P<vrf>.*)][router_id]')

    m.make()

    print(self.process)
    {'1': {'vrf': {'blue': {'router_id': '2',},
                   'orange': {'router_id':'3'}}},
     '2': {'vrf': {'default': {'router_id': '12',},
                   'orange': {'router_id':'13'}}}}

Whenever necessary, users may restructure the `feature` object so that it is
independent of the parser structure with the regex group name.

For example:

.. code-block:: python

    m.add_leaf(device=device,
               cmd=<parsers>,
               src='[process_id][(?P<process>.*)][vrf][(?P<vrf>.*)][id]',
               dest='vrf[(?P<vrf>.*)][process][(?P<process>.*)][router_id]')

    m.make()

    print(self.vrf)
    {'orange': {'process': {'1': {'router_id': '2',},
                            '2': {'router_id':'13'}}},
     'blue': {'process': {'1': {'router_id': '2',}}},
     'default': {'process': {'2': {'router_id': '12',}}}}

In this example, we changed the entire structure of the dictionary by swapping `vrf` and 
`process_id` static keys, and the two regex keys.

Regex follows the following guidelines:

1. A group used in `src` does not need to be used in `dest`. However, it must
   only return one branch of value. `Maker` cannot know which branch to return,
   nor can it merge it, as some keys could be identical.
2. If a group is used in `dest`, it must exist in `src`.
3. If a group is used in `dest` and exists in `src`, the regex has to be
   exactly the same.

`Maker` also uses the callable function to modify certain keys. 
For example, let's say we want to modify all vrf names in our parser to add a prefix 
`vrf-`, like this `vrf-default`.

.. code-block:: python

    m = maker(parent=self)
    m.add_leaf(device=device,
               cmd=<parsers>,
               src='[process_id][(?P<process>.*)][vrf][(?P<vrf>{vrf})][id]',
               dest='process[(?P<process>.*)][vrf][(?P<vrf>{vrf})][router_id]',
               callables={vrf=self.vrf})

    # Lambda are also welcomed, instead of functions :)
    def vrf(self, item):
        # takes a key as input, and return any other string
        return 'vrf-'+item

    m.make()

    print(self.process)
    {'1': {'vrf': {'vrf-blue': {'router_id': '2',},
                   'vrf-orange': {'router_id':'3'}}},
     '2': {'vrf': {'vrf-default': {'router_id': '12',},
                   'vrf-orange': {'router_id':'13'}}}}

You can see from the `vrf=self.vrf`, the keyword `vrf` matches the regex group
`vrf` that we wanted to modify. `Callables` is extremely powerful; it can modify and
transform any key. Instead of setting the `callables` for each `leaf`, a global
one can be set. Then all `leafs` can use this `callables`.

.. code-block:: python

    m = maker(parent=self)
    # Global callable
    self.callables = {'vrf':self.vrf}

    # Then no need to use calables in here
    m.add_leaf(device=device,
               cmd=<parsers>,
               src='[process_id][(?P<process>.*)][vrf][(?P<vrf>{vrf})][id]',
               dest='process[(?P<process>.*)][vrf][(?P<vrf>{vrf})][router_id]')

    def vrf(self, item):
        # takes a key as input, and return any other string
        return 'vrf-'+item

    m.make()

    print(self.process)
    {'1': {'vrf': {'vrf-blue': {'router_id': '2',},
                   'vrf-orange': {'router_id':'3'}}},
     '2': {'vrf': {'vrf-default': {'router_id': '12',},
                   'vrf-orange': {'router_id':'13'}}}}


Now let's visit one last argument, `action`. `action` allows users to modify the value
which will be stored at the `dest` location.

.. code-block:: python

    m = maker(parent=self)

    # Action function
    def keys(item):
        return item.keys()

    m.add_leaf(device=device,
               cmd=<parsers>,
               src='[process_id][(?P<process>.*)][vrf]',
               dest='process[(?P<process>.*)][vrf],
               action=keys)


    m.make()

    print(self.process)
    {'1': {'vrf': dict_keys(['blue', 'orange'])},
     '2': {'vrf': dict_keys(['default', 'orange'])}}

We understand that `callables` and `action` can be confusing, so let's make sure their
purpose is clear.

**`callables` is an argument to modify a key of the dictionary. `Action` allows
users to modify the output which is stored at the `dest` location.**

make
----

Api `make` takes all of the previously created `leafs`, sends the necessary commands
to the `Device`, and then builds the object from those `leafs`. If a :ref:`pool of
device <connection>` is given to the Ops object, then it will send the
commands in parallel.
