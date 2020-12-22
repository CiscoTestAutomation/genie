Abstraction
===========

In the previous sections, we learned how to create a new `ops` `Feature`.
However, we have not yet discussed the concept of abstraction. 


Before beginning this section, please review the ``pyats`` abstract_; particularly the part about
:lookupclass:`Lookup class <http>` as this is the core of abstraction in ``Genie`` `ops`.

Strategy
--------

There are primarily two reasons users rely on abstraction:

1) Device platform abstraction (Could be per OS type, or OS/Platform, etc.); and
2) Management interface abstract.

The :ref:`abstraction <abstract>` package and ``Genie`` `ops` make both of these easy for users to achieve.
Following the already defined directory :ref:`structure`, abstraction
determines which library to call depending on specific tokens.

Here is an example demonstrating what a section of the `genie_libs` directory looks
like:

.. code-block:: bash

  genie_libs
     `-- ops
         |-- __init__.py
         |-- tests
         |   `-- ospf -> ../ospf/tests
         `-- ospf
             |-- __init__.py
             |-- iosxe
             |   |-- __init__.py
             |   |-- ospf.py
             |   `-- yang
             |       |-- __init__.py
             |       `-- ospf.py
             |-- nxos
             |   |-- __init__.py
             |   |-- ospf.py
             |   `-- yang
             |       |-- __init__.py
             |       `-- ospf.py
             |-- iosxr
             |   |-- __init__.py
             |   |-- ospf.py
             |   `-- yang
             |       |-- __init__.py
             |       `-- ospf.py
             `-- tests
                 |-- __init__.py
                 `-- test_ospf.py

In this directory example, we have only given one level of OS abstraction,
but additional tokens may be given, if required. Then we have our Yang
directory abstraction.

Let's go through the `Yang` `Feature` implementation:

The `Cli` and `Yang` structure must be the same. This is achieve with
`Metaparser` which requires a schema, which is the same schema for `Cli` and
`Yang`. This means the code in `Ospf` `Cli` implementation is also valid for
`Yang` implementation; `metaparser` will return the same structure.  Whenever
the users calls `metaparser`, he or she must use the `Yang` function instead of
`Cli`.

Additionally, ``Genie`` supports a hybrid model. In this hybrid model, some commands are
sent via `Cli` and others are sent via `Yang`. This model is possible because of
the `self.context_manager`, which specifies which function to call in
`metaparser`, either `cli`, `yang` `rest`, or `xml`.

Let's take a look at the `nxos Ospf` implementation for `Yang`:

.. code-block:: python

    from genie.libs.ops.ospf.nxos.ospf import Ospf as b_ospf
    from genie.libs.ops.ops.base import Context
    from genie.libs.parser.nxos import show_ospf
    
    class Ospf(b_ospf):
        '''Ospf Ops Object'''
    
        # To keep short names
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.context_manager[show_ospf.ShowIpOspfVrfAll] = Context.yang
            self.context_manager[show_ospf.ShowIpOspfInterfaceVrfAll] = Context.yang
            self.context_manager[show_ospf.ShowIpOspfDatabase] = Context.Cli
            self.context_manager[show_ospf.ShowIpOspfNeighborsDetailVrfAll] = Context.yang

We want to use `Yang` for all commands, except for `ShowIpOspfDatabase`, which
uses the `Cli` command.  If the command does not exist in the context_manager,
it will use `Cli` as the default.
