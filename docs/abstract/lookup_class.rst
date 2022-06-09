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

When instantiated with a dict of :ref:`abstraction_tokens` and a reference to
an imported :ref:`abstraction_pkg`, the ``Lookup`` class enables performing
library lookups as if you were referencing attributes of an object.

  .. code-block:: python

      import my_abstracted_library

      lookup = Lookup(tokens_dict, package=my_abstracted_library)

      lookup.some_module.some_other_module.Target()


..note::

    if an package is a part of a parent package, it needs to be imported
    directly into the current namespace.

    .. code-block:: python

        # instead of
        import parent_package.my_abstracted_package

        # you must import it directly
        from parent_package import my_abstracted_package


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

    # create the lookup objects for each package and provide it with tokens
    my_lookup = Lookup({'os': 'iosxr'}, package=my_abstracted_library)
    genie_lookup = Lookup({'os': 'iosxr'}, package=genie)
    parser_lookup = Lookup({'os': 'iosxr'}, package=parser)

    # now use the lookup objects referencing the above imported libraries using
    # attribute queries. Eg:

    result = my_lookup.my_abstracted_function()
    # runtime absolute path translation:
    #   from my_abstracted_library.iosxr import my_abstracted_function
    #   result = my_abstracted_function()

    ospf = genie_lookup.conf.ospf.Ospf()
    # runtime absolute path translation:
    #   from xbu_shared.genie.conf.ospf.iosxr import Ospf
    #   ospf = Ospf()

    output = parser_lookup.ShowVersion(device = device)
    # runtime absolute path translation:
    #   from xbu_shared.parser.iosxr import ShowVersion
    #   output = ShowVersion()

    # --------------------------------------------------------------------------

    # create new Lookup() instances if tokens requirements change
    lookup = Lookup({'token_a': 'value_a', 'token_b': 'value_b'},
                    package = my_abstracted_library)

.. csv-table:: Lookup Class Argument List
    :header: "Argument", "Description"

    ``tokens``, "dict of tokens to be used as input requirements for to this
    lookup"
    ``packages``, "abstraction package to lookup from"


.. _abstract_topology:

Integration with Topology
-------------------------

``Lookup()`` class also features a classmethod constructor that enables it to
understand pyATS topology module's ``Device()`` object, and subsequently, create
lookup objects based on the token values retrieved from the device's attributes.

.. code-block:: yaml

    # Example
    # -------
    #
    #   example pyATS topology device yaml
    testbed:
        abstraction:
            revision: 1
    device:
        my-example-device:
            os: iosxe
            platform: asr1k
            version: v5
            abstraction:
                my_abstracted_library:
                    version: v7
                other abstracted_library:
                    version: v4

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
    # lookup = Lookup({'os': 'iosxe',
                       'platform': 'asr1k',
                       'version': ['v7', v5],
                       'revision': 1},
                      package=my_abstracted_library)

The token order defined in the abstract package is used to retrieve token values
from available device attributes. Additional values can also be specified in an
``abstraction`` dict under the device.

When ``Lookup.from_device()`` method is called, the tokens associated with that
device is automatically extracted following these rules:

    - ``device.abstraction`` is a dictionary if it exists
    - ``abstract.declare_package(['tokens'])`` in the abstract package specifies
      the list of attributes to read from this device object, and converted into
      token values.
    - all values from ``device.abstraction[attribute]``, ``device.<attribute>``,
      and ``testbed.abstraction[attribute]`` are used as token values in lists.
    - ``device.abstraction.<abstract_package>.<attribute>`` can be used to
      specify token values that should only be used with that specific abstract
      package.


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

            Subsection to create abstraction Lookup objects and assign to
            each corresponding device object as 'device.libs' attribute.
            '''
            for device in testbed.devices.values():
                device.libs = {'my_abstracted_library': Lookup.from_device(device, package=my_abstracted_library),
                               'genie': Lookup.from_device(device, package=genie),
                               'parser': Lookup.from_device(device, package=parser)}

        # ... other subsections

    # from here onwards, you can refer to libraries dynamically.

    class Configure_Ospf(aetest.Testcase):

        @aetest.setup
        def setup(self, testbed):
            # iterate through all devices and configure device...
            for device in testbed.devices.values():
                device.libs['my_abstracted_library'].configure_ospf(arg_1 = '...',
                                                                    arg_2 = '...',
                                                                    etc = '...')

        @aetest.test
        def test(self, testbed):
            for device in testbed.devices.values():
                output = device.libs['parser'].ShowOspf(device = device)

                # validate values... etc
                # ...


