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


Default Tokens
--------------

Sometimes you may want to define some default tokens to be added into your
lookup. These will allow you to specify which tokens you want to use when looking
up a package. This is especially important when using external abstracted
packages. You can set these default tokens in the pyATS Configuration file:

.. code-block::ini

    # configuration related to abstraction
    [abstract]
    default_origin = <value>
    default_os = <value>
    default_platform = <value>
    default_model = <value>
    default_submodel = <value>
    default_pid = <value>
    default_version = <value>
    default_os_flavor = <value>
    default_revision = <value>

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


