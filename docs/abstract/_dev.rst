
INTRODUCTION
============

.. code-block:: python

    # Example
    # -------
    #
    #   with and without abstraction

    # typical non-abstracted script
    # -----------------------------
    # import the proper function through if statements
    if release == 'v2.1':
        if context == 'YANG':
            from my_library.v2_1.yang import configure_something
        else:
            from my_library.v2_1.cli import configure_something
    elif release == 'v2.2':
        if context == 'YANG':
            from my_library.v2_2.yang import configure_something
        else:
            from my_library.v2_2.cli import configure_something
    else:
        if context == 'YANG':
            from my_library.generic import configure_something
        else:
            from my_library.generic import configure_something

    # get result
    result = configure_something()

    # using abstraction & properly abstracted libraries
    # -------------------------------------------------
    from genie import abstract

    # build a lookup object and pass the release/context as tokens
    lookup = abstract.Lookup(release, context)

    # collect result by looking up the corresponding API
    result = lookup.my_library.configure_something()


As show above, through the use of ``abstract`` package, users can write
straightforward codes (single-source) that automatically invokes the right set
of library APIs (classes, functions, methods etc) based on given requirements,
without the repeated use of custom ``if..elif..elif..else`` statements
everywhere. This dynamic library referencing can be beneficial in many use
cases, including but not limited to:

    - handling minute release-to-release, image-to-image differences
    - running the same tests/scripts across a variety of hardware (os/platforms, etc)


Concept
=======

Abstract Mechanism
------------------


The ``abstract`` module works most of its magic at the Python ``import`` and
``getattr()`` level. It does so by dissecting each lookup into three distinct
parts:

    - **relative path**: the primary lookup path that makes the most sense from
      a functional perspective. This is what the user references directly, eg:
      ``my_library.routing.ospf``

    - **tokens**: the list of abstraction tokens currently known by the
      abstraction engine. This portion is registered through the ``Lookup``
      object. Eg: ``iosxr``, ``fretta``, ``xml``.

    - **target**: the module/class/function/variable user is looking for.

During runtime, the lookup engine dynamically pieces together the above
information into a list of possible candidate **absolute paths** (direct mapping
to python import statements). As the list of tokens is arbitrary, this candidate
list is built following the :ref:`abstract_search_algorithm`.






.. code-block:: python

    # Example
    # -------
    #
    #   relative path & absolute path explained

    # Given the following tokens:
    #    - iosxe
    #    - polaris_dev
    #    - yang
    os = 'iosxe'
    branch = 'polaris_dev'
    context = 'yang'

    # feed to to abstraction lookup engine.
    library = abstract.Lookup(os, branch, context)

    # the relative call to
    library.my_package.config.routing.ospf.Ospf()

    # could match, for example:
    #
    #    my_package.iosxe.config.polaris_dev.routing.ospf.yang.Ospf
    #         |       |      |       |          |     |     |    |
    #    abstraction  |   relative   |       relative |     |  class
    #      package    |     path     |         path   |   token
    #               token          token           relative
    #                                                path
    # which translates to:
    #   from my_package.iosxe.config.polaris_dev.routing.ospf.yang import Ospf
    #
    # where
    # -----
    #    relative path = config, routing, ospf
    #    tokens        = iosxe, polaris_dev, yang
    #    target        = Ospf()



.. _abstract_search_algorithm:

Search Algorithm
----------------

The search engine combines the user's **relative path** and currently known
**tokens** into possible **absolute paths** (python module names) and searches
through them. A match occurs when an implementation is found (ie the target
exists at the candidate relative path). Otherwise, the next combination is
tried. If no target is found, a ``LookupError`` would be thrown.

As the token names are not pre-defined, the search engine orders
all tokens in a pre-defined fashion:

    - token describes a set of *differences*
    - token positions are always fixed w.r.t. to its left (parent)
    - tokens on the right are more *specific* than tokens on the left
    - each token may only appear *once* in a combination
    - greedy match: more tokens matches is always better than less.

.. code-block:: text

    Given tokens: a, b, c and d, the preferred token combination would be:

        a b c d
        a b c
        a b
        a
        (no tokens)

These combinations are then *multiplexed* to user's **relative path** into
potential **absolute paths** to search for, using the following rules:

    - absolute paths must always start with the abstracted package name.

    - the order of relative path sections (words divided by ``.``) must be
      preserved.

    - the order of token combinations must be preserved.

    - tokens may take place before and after each relative path section, and may
      appear in multiples together. (eg, ``library.iosxr.google.latest.mpls``)

    - the last resort option is to try with "no token", eg, matching the
      relative path directly.

Combining the above rules, the ideal solution would be a multi-combinatory
mathematical function, whose search complexity is ... *(insert math here)* ...
exponential.

.. code-block:: text

    Given Package: my_pkg
    Relative Path: X, Y
    Tokens: a, b
    Target: MyClass()

    We could have the following mathmatical combinational possibilities:

        1. my_pkg.a.X.b.Y.MyClass()
        2. my_pkg.a.X.Y.b.MyClass()
        3. my_pkg.X.a.Y.b.MyClass()
        4. my_pkg.X.a.b.Y.MyClass()
        5. my_pkg.X.Y.a.b.MyClass()
        6. my_pkg.a.X.Y.MyClass()
        7. my_pkg.X.a.Y.MyClass()
        8. my_pkg.X.Y.a.MyClass()
        9. my_pkg.X.Y.MyClass()

    And that's just with two tokens and two path sections!

The actual implementation internally is much simpler. When an an abstracted
package is defined/declared and the lookup object is created, the package and
all of its child modules are *recursively imported*. This allows the abstraction
engine to build an internal table of relative paths, their available token
combinations learnt from the import and its corresponding module. This reduced
**relative path + tokens** relationship effectively simplies the above
brute-force search algorithm into an ``O(n)`` lookup, where ``n`` is the number
of tokens.

.. code-block:: text

    Pseudo Lookup Table
    ===================

    Relative Path            Tokens Combos           Corresponding Module
    -------------            -------------           --------------------
         X.Y                      a, b                     X.a.Y.b
         X.Y                      a                        X.a.Y
         X.Y                      None                     X.Y

    (shown in order of preference, from top down)

This algorithm limits to only dealing with what's been defined in the user
library, instead of going through all possible permutations of **relative path**
and **tokens**. The system assumes that it is unlikely for users to make
redundant declarations, such as defining both ``from X.a.Y.b import target`` and
``from X.a.b.Y import target`` within the same library.

.. note::

    The learning process safeguards against these redundant scenarios.


.. _token_builder:

Token Builder
-------------

The token builder is a simple function that implements the token permutation
portion of the :ref:`abstract_search_algorithm`. The default token builder is
available as ``abstract.magic.default_builder()``.

.. csv-table:: default_builder Argument List
    :header: "Argument", "Description"

    ``tokens``, "list of tokens to permute"
    ``mandatory``, "list of tokens that must be used"

.. code-block:: python

    # Example
    # -------
    #
    #   pseudo code demonstrating the behavior of default token builder

    from abstract.magic import default_builder

    # without any mandatory tokens
    default_builder(tokens = ['nxos', 'n7k', 'c7003', 'yang', 'R8_1'])
    # [('nxos', 'n7k', 'c7003', 'yang', 'R8_1'),
    #  ('nxos', 'n7k', 'c7003', 'yang'),
    #  ('nxos', 'n7k', 'c7003'),
    #  ('nxos', 'n7k'),
    #  ('nxos',),
    #  ()]

    # a mandatory token is one that MUST be used in the search
    default_builder(tokens = ['nxos', 'n7k', 'c7003', 'yang', 'R8_1'],
                    mandatory = ['yang'])
    # [('nxos', 'n7k', 'c7003', 'yang', 'R8_1'),
    #  ('nxos', 'n7k', 'c7003', 'yang'),
    #  ('nxos', 'n7k', 'yang'),
    #  ('nxos', 'yang'),
    #  ('yang',)]

In essence, the "tokens" input parameter to the builder is a reflection of
the actual, longest possible chain of tokens under any given relative path. If
no target is found at this token/relative path combination, the next, reduced
set of tokens is tried. This reduction mechanism always reduces from the right.

Use the ``mandatory`` input argument when you absolutely require some tokens to
be present in any token permutations during abstraction. This can be useful when
you do not want the system to automatically fallback using the above logic and
remove it. This ensures the proper "set" of libraries is picked.




.. _abstract_lookup_cls:

Lookup Class
============

``Lookup`` class is the main feature of ``abstract`` package. It implements
:ref:`Abstraction Concepts <abstraction_concepts>` in a user-friendly fashion,
and allows users to perform dynamic lookups just as if they were accessing
object attributes.

.. code-block:: text

                                    .------> TokenX.Y implementation
                                   /
    UserScript -> Lookup Target --+--------> Token X implementation
                  (func/cls/var)   \
                                    `------> Default (no token) implementation


Usages
------

When instanciated with a list of :ref:`abstraction_tokens`, ``Lookup`` class
allows the user to reference any :ref:`abstraction_pkg` available in the current
namespace scope. This behavior can be generally summarized into the following:

- at miminum, a list of :ref:`abstraction_tokens` is required in order to
  instanciate a new ``Lookup`` object.

- by default, all :ref:`Abstraction-Enabled Packages <abstraction_pkg>` imported
  and available at the scope where ``Lookup()`` is called, gets discovered and
  registered internally.

- if an package is a part of a parent package, it needs to be imported
  directly into the current namespace.

  .. code-block:: python

      # instead of
      import parent_package.my_abstracted_package

      # you must import it directly
      from parent_package import my_abstracted_package

- users can provide a dictionary of ``name: package`` to ``Lookup()`` and
  override the default discovery behavior. ``name`` is the alias to refer to
  the given package.

  .. code-block:: python

      import parent.my_package

      lookup = Lookup(*tokens, packages = {'pkg': parent.my_package})

- perform library lookups as if you were referencing attributes of an object.

  .. code-block:: python

      import my_abstracted_library

      lookup = Lookup(*tokens)

      # always start with the name of the library you want to search from
      lookup.my_abstracted_library.some_module.some_other_module.Target()

- the default :ref:`token_builder` supports specifying mandatory tokens. This
  generator can be overwritten with ``builder`` argument to ``Lookup()`` (very
  advanced functionality).

  .. code-block:: python

      from genie import abstract
      from my_library import my_builder

      # use your default builder
      lookup = Lookup(*tokens, builder = my_builder)


- in addition, this global default builder setting can be modified by setting
  ``abstract.magic.DEFAULT_BUILDER`` to a builder of your liking. This will
  affect **all** newly created ``Lookup()`` object from this point onwards.

  .. code-block:: python

      from genie import abstract
      from my_library import my_default_builder

      # overwrite the default builder
      abstract.magic.DEFAULT_BUILDER = my_default_builder

      # any lookup object created hereonward will take on your builder
      lookup = Lookup(*tokens)


.. code-block:: python

    # Example
    # -------
    #
    #   Lookup() class examples & features

    # import the class from abstract
    from genie.abstract import Lookup

    # import any abstraction-enabled packages you need
    import my_abstracted_library
    from xbu_shared import genie, parser

    # create the lookup object and provide it with tokens
    # this auto discovers and registers the above imported packages:
    #     my_abstracted_library, genie, parser
    lookup = Lookup('iosxr')

    # now use the lookup object and reference the above imported
    # libraries using attribute queries. Eg:

    result = lookup.my_abstracted_library.my_abstracted_function()
    # runtime absolute path translation:
    #   from my_abstracted_library.iosxr import my_abstracted_function
    #   result = my_abstracted_function()

    ospf = lookup.genie.conf.ospf.Ospf()
    # runtime absolute path translation:
    #   from xbu_shared.genie.conf.ospf.iosxr import Ospf
    #   ospf = Ospf()

    output = lookup.parser.ShowVersion(device = device)
    # runtime absolute path translation:
    #   from xbu_shared.parser.iosxr import ShowVersion
    #   output = ShowVersion()

    # --------------------------------------------------------------------------

    # create new Lookup() instances if tokens requirements change
    # you can also change the set of packages available for it,
    # as well as its base reference name.
    lookup = Lookup('token_a', 'token_b', '...', 'etc',
                    packages = {'lib_1': my_abstracted_library,
                                'lib_2': genie',
                                'lib_3': parser})

    # as new names are tokens are provided, we can now do:
    result = lookup.lib_1.my_abstracted_function()
    ospf = lookup.lib_2.conf.ospf.Ospf()
    output = lookup.lib_3.ShowVersion(device = device)

.. tip::

    always use meaningful package names.

.. csv-table:: Lookup Class Argument List
    :header: "Argument", "Description"

    ``*token``, "list of tokens to be used as input requirements for to this
    lookup"
    ``packages``, "dictionary of name/abstraction package to lookup from
    (optional)"
    ``builder``, "token permutation builder (optional)"
    ``**builder_kwargs``, "any keyword arguments/values to be passed to the
    builder (optional)"


Integration with Topology
-------------------------

``Lookup()`` class also features a classmethod constructor that enables it to
understand pyATS topology module's ``Device()`` object, and subsequently, create
lookup objects based on the tokens specified under ``Device.custom.abstraction``
field.

.. code-block:: yaml

    # Example
    # -------
    #
    #   example pyATS topology device yaml

    device:
        my-example-device:
            type: router
            os: iosxe
            series: asr1k
            custom:
                abstraction:
                    order: [os, series, context]
                    context: yang

.. code-block:: python

    # Example
    # -------
    #
    #   using the above testbed definition with abstraction

    from pyats import topology
    testbed = topology.loader.load('/path/to/above/testbed.yaml')
    device = testbed.devices['my-example-device']

    # create abstraction
    from genie.abstract import Lookup

    lookup = Lookup.from_device(device)
    # eg, the above is equivalent to:
    # os = device.custom.abstraction.get('os', device.os)
    # series = device.custom.abstraction.get('series', device.series)
    # context = device.custom.abstraction.get('context')
    # lookup = Lookup(os, series, context)

In the above testbed YAML file, we defined a custom abstraction definition,
specifying the expected token list ``[os, series, context]``, and the expected
``context = 'yang'``.

When ``Lookup.from_device()`` method is called, the tokens associated with that
device is automatically extracted following these rules:

    - ``device.custom.abstraction`` is a dictionary
    - ``device.custom.abstraction['tokens']`` specifies the list of attributes
      to read from this device object, and converted into token values.
    - the code prefers to read the attributes from
      ``device.custom.abstraction[attrbute]``, and falls back to
      ``device.<attribute>`` if needed.

All other arguments to ``Lookup()``, such as ``builder, packages,
builder_kwargs`` also applies to this classmethod.

If however you would like to not specify the ``device.custom.abstraction`` block
in your testbed YAML file all the time, you can provide ``default_tokens`` as a
list to ``Lookup.from_device()``. Any tokens specified there would be looked-up
from the provided device attribute.

.. code-block:: python

    # Example
    # -------
    #
    #   Lookup.from_device using defaults

    lookup = Lookup.from_device(device, default_tokens = ['os', 'series'])
    # eg, the above is equivalent to:
    # os = device.os
    # series = device.serie
    # lookup = Lookup(os, series)

.. note::

    note that when using ``default_tokens``, the lookup from device attribute
    is non-strict, eg: if tokens ``a``, ``b``, ``c`` are specified, and only
    ``a``, ``c`` exists, it will not error and just use these values instead.


Tips & Tricks
-------------

Typically, abstraction should be used when the end library needs to handle
differences (such as OS/Release/Mgmt Interface) etc. This leads to a per-device
lookup model, where the set of :ref:`abstraction-tokens` per device differs.
The best, pythonic method to tackle this is to follow the natural patterns
of Python/pyATS programming:

- ``import`` all your packages at the top of your script/code, including all
  :ref:`Abstraction-Enabled Packages <abstraction_pkg>`.

- inside AEtest ``CommonSetup`` section, as soon as you have connected to your
  testbed devices and learnt about what they are, create your ``Lookup()``
  objects and assign them as an attribute to each ``Device`` instance.

.. code-block:: python

    # Example
    # -------
    #
    #   an example AEtest script with abstraction enabled

    # import everything at the top
    import logging
    from genie import abstract
    from pyats import aetest

    # eg, these are my abstraction libraries
    import my_abstracted_library
    from xbu_shared import genie, parser

    logger = logging.getLogger(__name__)

    class CommonSetup(aetest.CommonSetup):

        @aetest.subsection
        def connect_to_testbed(self, testbed):
            for name, device in testbed.devices.items():
                device.connect()
                logger.info('connected to device %s' % device.name)

        @aetest.subsection
        def create_abstraction_lookup_objects(self, testbed, context):
            '''create_abstraction_lookup_objects

            Subsection to create abstraction Lookup object and assigns it to
            each corresponding device object as 'device.lib' attribute.

            In this example, we are using device object's attribute 'os', 'type'
            (from testbed YAML file) and script input parameter 'context' as
            tokens.
            '''
            for device in testbed.devices.values():
                device.lib = Lookup(device.os, device.type, context)

        # ... other subsections

    # from here onwards, you can refer to libraries dynamically.

    class Configure_Ospf(aetest.Testcase):

        @aetest.setup
        def setup(self, testbed):
            # iterate through all devices and configure device...
            for device in testbed.devices.values():
                device.lib.my_abstracted_library.configure_ospf(arg_1 = '...',
                                                                arg_2 = '...',
                                                                etc = '...')

        @aetest.test
        def test(self, testbed):
            for device in testbed.devices.values():
                output = device.lib.parser.ShowOspf(device = device)

                # validate values... etc
                # ...


.. _abstract_lookup_decorator:

Lookup Decorator
================

``LookupDecorator`` is a feature extension to :ref:`abstract_lookup_cls`.
Whereas the ``Lookup`` class allows users to write **different** classes,
functions and variables in tokenized modules and dynamically reference them, the
lookup decorator operates at the class method level, allowing users to write
a **single class** with different method implementations per each token variance
combination.

.. code-block:: text

                                                    .--> TokenX.Y class method
                                                   /
    UserScript -> import cls -> call cls method --+----> TokenX class method
                                                   \
                                                    `--> Default (no token)
                                                           class method

.. code-block:: python

    # Example
    # -------
    #
    #  a simple lookup decorator example

    # my_library/config.py
    # --------------------

    # import the decorator
    # (note the lowercase 'lookup')
    from abstract import lookup

    # define a class using the decorator on its methods
    class ConfigureRouting(object)
        def __init__(self, os):
            self.os = os

        # apply the decorator on methods to be abstracted
        @lookup('os')
        def apply_config(self):
            # ... insert generic/non-os specific code here


    # my_library/nxos/config.py
    # -------------------------
    from ..config import ConfigureRouting as BaseConfigRouting

    # inherit the parent class
    class ConfigureRouting(BaseConfigRouting):

        # define the same method specific to this token
        def apply_config(self):
            # ... insert nxos specific code here

The main benefit of using ``LookupDecorator`` is that it allows the user to
perform standard python ``import`` and deal with only one class instance.
During runtime, the engine looks up the class's attributes and forms a list of
tokens based on these values, and replaces the decorated methods during with a
"more" appropriate one from a tokenized search
(see :ref:`abstract_search_algorithm`).

.. code-block:: python

    # Example
    # -------
    #
    #   using the above code

    # import the main entry class directly
    from my_library.config import ConfigureRouting

    # use it as you would naturally
    obj = ConfigureRouting(os = 'nxos')

    # when a decorated method is called, the lookup occurs and the
    # most appriorate method from one of its subclasses is called instead.
    result = obj.apply_config()
    # lookup information
    # ------------------
    #   attributes to read: os
    #   attribute value: os = 'nxos'
    #
    # thus, the search result equivalence is:
    #   from my_library.nxos.config import ConfigureRouting
    #   result = ConfigureRouting.apply_config(obj)


Usages
------

To use ``LookupDecorator``, start with writing your abstraction-enabled library
as you normally would. When arriving at defining classes that requires methods
level abstraction, simply apply the decorator onto each method that needs to be
abstracted. Behaviors:

- Lookup decorator can be imported as ``lookup`` (note the lowercase), or as
  ``decorator.LookupDecorator``. They are exactly the same, but some may prefer
  one name over the other.

  .. code-block:: python

      from abstract import lookup
      from abstract.decorator import LookupDecorator

- The usage of lookup decorator does not mandate a top-level
  :ref:`abstraction_pkg` declaration. It only requires :ref:`abstraction_tokens`
  definitions under the module where the lookup decorator is used.

  .. code-block:: text

      Example:
        if LookupDecorator is used in on class X under module A.B,
        tokens should be defined as child modules under A.B.

- Lookup decorator takes in a list of **attributes names** as arguments. During
  runtime, the engine will lookup the given class instance for these attributes
  to be used as tokens. This mechanism is called an *attribute getter*. The
  default attribute getter looks up both the class instance and
  ``instance.device`` (if exists) for the named attribute.

  .. code-block:: python

      class MyClass(object):

          @lookup('attr_1', 'attr_2')
          def some_func(self):
              # ...

      # equivalent to
      #     obj = MyClass()
      #     token_1 = getattr(obj, 'attr_1', getattr(obj.device, 'attr_1'))
      #     token_2 = getattr(obj, 'attr_2', getattr(obj.device, 'attr_2'))

- The search for matching token combinations always begins at this class's
  module declaration level onwards. It will match for the same **relative path**
  as the current module, and the same class name (or names in nested class defs)
  and target method.

  .. code-block:: text

      Example:
        a search originating from: moduleX.moduleY.classA.classB.some_func()
        may match: moduleX.moduleY.tokenJ.tokenK.classA.classB.some_func()

- the default *attribute getter* can be replaced by providing a new function
  through ``attr_getter`` argument. The provided function must take in two
  arguments: ``obj`` and ``attr`` for both the object under scrutiny and the
  attribute to lookup

.. code-block:: python

    # Examples
    # --------
    #
    #   lookup decorator usage

    # assuming we had a lookup-decorator enabled library
    # my_library.my_module.ConfigureOspf

    # import it regularly
    from my_library.my_module import ConfigureOspf

    # instaciate it naturally
    # (in this case our class requires argument 'os' and mgmt_context)
    routing = ConfigureOspf(os = 'iosxr', mgmt_context = 'yang')

    # if we call a decorated method, say, apply_configuration
    # eg, code snippet:
    #       @lookup('os', 'mgmt_context')
    #       def apply_configuration(self):
    #           # ... code

    routing.apply_configuration()
    # the engine translates this to:
    #    token_os = routing.os = 'iosxr'
    #    token_mgmt_context = routing.mgmt_context = 'yang'
    # and the resulting lookup equivalent could be:
    #    from my_library.my_module.iosxr.yang import ConfigureOspf
    #    result = ConfigureOspf.apply_configuration(routing)

    # note
    # ----
    #   after lookup is performed, notice that the found target class's method
    #   is called directly with the original class instance as first argument.
    #   This is a python property: class methods can be treated as "functions"
    #   if you pass in a "similar" class instance as the first argument.
    #   See: https://docs.python.org/3.4/tutorial/classes.html#method-objects

.. csv-table:: LookupDecorator Class Argument List
    :header: "Argument", "Description"

    ``*attrs``, "list of attributes to be used read as input tokens for lookup"
    ``attr_getter``, "class instance attribute getter (optional)"
    ``builder``, "token permutation builder (optional)"
    ``**builder_kwargs``, "any keyword arguments/values to be passed to the
    builder (optional)"

Lookup From Device Decorator
============================

``LookupDecorator.from_device`` is a feature extension to ``LookupDecorator``.
The lookup.from_device decorator operates at the runtime, allowing users to
write a **single class** with different method implementations and dynamically
based on the token variance combination from device's custom abstraction or
pre-defined at class method level.

.. code-block:: python

    # Example
    # -------
    #
    #  a simple lookup.from_device decorator example

    # my_library/config.py
    # --------------------

    # import the decorator
    # (note the lowercase 'lookup')
    from abstract import lookup

    # define a class using the decorator on its methods
    class ConfigureRouting(object)
        def __init__(self, os):
            self.os = os

        # apply the decorator on methods to be abstracted dynamically based on
        # custom abstraction data
        @lookup.from_device
        def apply_config(self):
            # ... insert generic/non-os specific code here

        # apply the decorator on methods to be abstracted dynamically based on
        # custom abstraction data or fallback to token 'os'
        @lookup.from_device('os')
        def check_config(self):
            # ... insert generic/non-os specific code here
