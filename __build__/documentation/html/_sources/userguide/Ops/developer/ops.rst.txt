Develop Ops
===========

The section will discuss how users can develop a ``Genie`` `ops` object. Please 
review the :ref:`user guide<_ops_user_guide>` before beginning this section.

.. note::

    All code in this section is pseudo-code only.

Overview
--------

`Ops` object is a snapshot of a particular `feature` on a particular `device` at
a specific time.


Many commands like, Cli, Yang, and XML gather a `feature`s' state and store it into one object. 
Each command is parsed and then regrouped into one common structure. This structure is
compatible with various operating systems.

We created a :models:`wiki <http>` to help users write a common `feature` operational structure which
can be used across various `OS`. Many teams part of XR/XE and Nxos monitor the
:models:`wiki <http>` to review all of the structures posted. An `Ops` structure must mention
the attributes of the object, and any level of a dictionary. For more
guidelines and examples, please visit the :models:`wiki <http>`.

An `Ops` object is made by sending multiple commands, and merging the output
into 1 common structure stored in the object. Let's see how we merge the multiple
output into 1 common structure.

Let's imagine that the output of a few parsers all related to the same `feature`
looks like this:

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

.. code-block:: text

    intf:
        eth3/1:
            vrf:
                blue:
                    process_id:
                        1:
                            state:Up
                            ip_address:1.1.1.1
        eth3/4:
            vrf:
                orange:
                    process_id:
                        1:
                            state:Up
                            ip_address:1.1.1.2
        eth3/5:
            vrf:
                orange:
                    process_id:
                        2:
                            state:Up
                            ip_address:1.1.1.4

After looking at the `feature`, we develop the following structure:

.. _structure:

.. code-block:: text

    process_id:
        <id>
            vrf
                <vrf>
                    router_id:<value>
                    age:<value>
                    interface_attr
                        <interface>
                            state:<value>
                            ip_address:<value>


We see that both structures can be merged into the same common structure; we have modified
`id` to `router_id`. However, converting both outputs into this structure 
would require a lot of loops. To save time and reduce complexity while
creating these classes, we have created a new object called, :ref:`maker`. :ref:`maker` 
converts parser outputs into one common structure.

Before continuing with this section, please review :ref:`maker` documentation.

Creating the object
-------------------

Let's now use :ref:`maker` to create our object. Our `Ops` object begins as a
normal python class, which inherits from `Base`.

.. code-block:: python

    from genie.ops.base import Base

    class Ospf(Base):
        '''Ospf Ops Object'''
        pass

This class inherits all of the following arguments and functions for free:

.. code-block:: text

    +--------------------------------------------------------------------------+
    | Base Class                                                               |
    +==========================================================================+
    | Arguments             | Description                                      |
    |-----------------------+--------------------------------------------------|
    | device                | Device object                                    |
    | attributes            | Limit which field to learn                       |
    | maker                 | Maker object                                     |
    | ignored               | Ignore specific attributes when comparing        |
    |                       | two snapshots                                    |
    | callables             | Map callables strings to callable for all leafs  |
    |-----------------------+--------------------------------------------------|
    | Functions             | Description                                      |
    |--------------------------------------------------------------------------|
    | add_leaf              | Wrapper to self.maker.add_leaf                   |
    | maker                 | Wrapper to self.maker.make                       |
    | learn                 | Learn all the leafs                              |
    | diff                  | Compare two objects and show the differences     |
    | __eq__                | Allows equality , ==,  and return True/False     |
    +==========================================================================+


Now let's create our first `Ops` object with :ref:`maker` and `Base` object. We will 
use `Ospf` for this example: 

.. code-block:: python

    from genie.ops.base import Base

    class Ospf(Base):
        '''Cli Ops Ops object'''

        def learn(self):
            '''Learn Ospf Object'''

            # Step one, create our structure

            # Step two, place holder to make it more readable
            src_vrf = '[process_id][(?P<process_id>.*)][vrf][(?P<vrf>.*)]'
            src_int = '[intf][(?P<intf>.*)][vrf][(?P<vrf>.*)][process_id][(?P<process_id>.*)]

            dest_vrf = 'name[(?P<process_id>.*)][vrf_attr][(?P<vrf>.*)]'
            dest_int = 'name[(?P<process_id>.*)][vrf_attr][(?P<vrf>.*)][interface][(?P<intf>.*)]'

            # Step three, create our leafs (The structure could be placed directly
            # in the leaf too, but it is more readable if it is defined
            # at the top).
            self.add_leaf(cmd=<parser for ospf process>,
                          src=src_vrf+'[id]',
                          dest=dest_vrf+'[router_id]')

            self.add_leaf(cmd=<parser for ospf process>,
                          src=src_vrf+'[age]',
                          dest=dest_vrf+'[age]')

            self.add_leaf(cmd=<parser ospf interface>,
                          src=src_int,
                          dest=dest_int)
            self.make()


The above Ospf `ops` class creates the :ref:`structure` by merging two different
`Clis` together.

.. code-block:: python

    # Assuming we have already a connected device
    ospf = Ospf(device=device)

    ospf.learn()

    import pprint
    pprint.pprint(ospf.name)
    {'process_id': {'1': {'vrf': {'blue': {'age': 3,
                                           'interface': {'eth3/1': {'ip_address': '1.1.1.1',
                                                                    'state': 'up'}},
                                           'router_id': 2},
                                  'orange': {'age':6,
                                             'interface': {'eth3/2': {'ip_address': '1.1.1.2',
                                                                      'state': 'up'}},
                                            'router_id': 5}}},
                    '2':{'vrf': {'default': {'age': 13,
                                             'router_id': 12},
                                 'orange': {'age':6,
                                            'interface': {'eth3/5': {'ip_address': '1.1.1.4',
                                                                     'state': 'up'}},
                                            'router_id': 15}}}}}


We took two different parser outputs and then transposed them into the same structure
in just a few lines of code.

Hybrid
------

If from some reason :ref:`maker` does not respond to your needs, you may use the
hybrid method.

.. code-block:: python

    from genie.ops.base import Base

    class Ospf(Base):
        '''Ops Ops object'''

        def learn(self):
            '''Learn Ospf Object'''

            self.add_leaf(cmd=<parser for ospf process>,
                          src=[process_id]',
                          dest=process_id')

            self.make()

            # Do whatever action is needed with process_id
            for pid in self.process_id:
                ...
