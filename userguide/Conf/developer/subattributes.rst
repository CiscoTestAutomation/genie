.. _subattributes:

SubAttributes
=============

Introduction
------------

This section focuses on `SubAttributes`, `SubAttributesDict` and the concept of
attributes propagation.

.. _the_why:

The Whys
--------

``Genie`` allows the user to configure a `Feature` via object attributes.
However, `Feature` in a device are configured with a certain level of
hierarchy, and requires the attributes to also be this way. A hierarchy of
attributes is needed. Some configurations are only available when certain
configurations are already present on the device. For example, `feature ospf` on
nxos. Secondly, some configurations are only availably when inside other 
configuration. For example :

.. code-block:: text

    router rip1
     address-family ipv4 unicast
      default-metric 1

`address-family ipv4 unicast` is only available inside `router rip1`. 

`default-metric 1` is only available inside `address-family ipv4 unicast`.


``Genie`` object attributes need to respect the same logic and structure. This
same concept of hierarchy also brings the point of, some configuration can be
repeated, but for different values. For example, `default-metric` can be part
of both address family, ipv4 and ipv6.

.. code-block:: text


    router rip 1
     no shutdown
     address-family ipv4 unicast
      default-metric 1
      exit
     address-family ipv6 unicast
      default-metric 3
      exit

Let's evaluate line by line and see how we rationalize this configuration
and convert it into ``Genie`` object.

`router rip 1` is the feature.

`no shutdown` is an attribute into the feature.

`address-family ipv4 unicast` is a `SubAttributes` 

`default-metric 1` is an attribute for ipv4 address family `SubAttributes`

`address-family ipv6 unicast` is another `Subattributes`

`default-metric 3` is an attribute for ipv6 address family `SubAttributes`


`Address-family` came back twice with different values (ipv4, ipv6).
`default-metric`, but with different values. The value 1 for `ipv4` and 3 for
`ipv6`.

This is a small scale example, but a mechanism to handle this scenario is
needed.

Another scenario is to group attributes for each device. Some values for
device `PE1` and others for `P1` might/will need to be different.

SubAttributes
-------------

`SubAttributes` hold a subset of `Feature` configuration specified by a
certain context. This context can be `per device`, `per address family`, `per
vrf` and so on. A `SubAttributes` can also be subdivided into smaller
subsets.

`Subattributes` has 2 main responsabilities.

 1. Allows you to create a hierarchy inside a `feature`. It subdivides
    configurable attributes into smaller and into re-usable subgroups.
 2. Allow re-usable subgroups divided by specific keys to be stored into
    subattributesdict_.

In more technical terms, `SubAttributes` is a class , inside a `Feature` class
that holds attributes. This class has its own functions to build the device
configuration.  Many of `SubAttributes` can be chained together, for as many
levels as needed.  Many objects of this class can be instantiated, to create
similiar subgroup, but with different keys to ensure each `SubAttributes` may
be individually accessed in subattributesdict_.

Let's see an example :

.. code-block:: python

    from genie.conf.base import Feature
    from genie.conf.base.attributes import SubAttributes

    class MyFeature(Feature):

        class PerDeviceAttr(SubAttributes):
            pass

        def __init__(self, **kwargs):
            self.maximum_hop = None
            self.speed = None
            super().__init__(**kwargs)

`PerDeviceAttr` is a `SubAttributes`, where it can be further subdivided into
attributes based on each device.  This concent, and `SubattributesDict` will
allow to have different value for each device.

.. _subattributesdict:

SubAttributesDict
-----------------

`SubAttributes` wouldn't work, without an attribute inside `MyFeature` to glue
it all together.  `SubAttributesDict` ties multiple `SubAttributes` together
and the object containing them.

`SubAttributesDict` is a dictionary that inherits from defaultdict_  and
ordereddict_. It is instantiates by passing a `SubAttributes` class.  when a
key is requested, it verifies if the key exists. If it does, it returns the 
object associated with the key. If it does not, it instantiate an object of the
given `SubAttributes` class that was given, stores it in the dictionary and
returns it. This is a bit complex, but, no need to fully understand it
to use it

Let's work it out on an example :

.. code-block:: python

    from genie.conf.base import Feature
    from genie.conf.base.attributes import SubAttributes

    class MyFeature(Feature):

        class PerDeviceAttr(SubAttributes):

        def __init__(self, **kwargs):
            self.maximum_hop = None
            self.speed = None
            super().__init__(**kwargs)

We have our `SubAttributes` class inside `MyFeature`, though no way to access
it still.

.. code-block:: python

    from genie.conf.base import Feature
    from genie.conf.base.attributes import SubAttributes, SubAttributesDict

    class MyFeature(Feature):

        class PerDeviceAttr(SubAttributes):
            pass

        def __init__(self, **kwargs):
            self.maximum_hop = None
            self.speed = None
            super().__init__(**kwargs)

            self.device_attr = SubAttributesDict(self.PerDeviceAttr, self)

In this example, SubAttributesDict is added, and stored into an attributes
`self.device_attr`. Following on with the same example :

.. code-block:: python

    >>> myfeature = MyFeature()

    # device_attr is a SubAttributesDict, and key 'PE1' was requested. The key
    # PE1 does not exists, so an instance of PerDeviceAttr is created.
    # This can be done with the create api
    >>> myfeature.device_attr['PE1']
    <__main__.MyFeature.PerDeviceAttr object at 0x10c5bdb38>

    # The object is now created
    >>> myfeature.device_attr['P1']
    <__main__.MyFeature.PerDeviceAttr object at 0x10c5c6080>

    # A new object was created for P1. This means attributes set for one object
    # is not set for the other.
    >>> myfeature.device_attr['PE1'].speed = 5
    >>> myfeature.device_attr['PE1'].speed
    5
    >>> myfeature.device_attr['P1'].speed
    AttributeError: 'MyFeature' object has no attribute 'speed'

    # Lastly, no need to create it first,
    >>> myfeature.device_attr['PE2'].speed = 5
    >>> myfeature.device_attr['PE2'].speed
    5

The last line of the previous example demonstrate that there is no need
to instantiate a `SubAttributes` first, attributes inside can be declared right
away and the object will be instantiated on the go.

However, calling a dictionary that does not exist should raise a KeyError
exception.

.. code-block:: python

    # Standard dictionary 
    >>> mydict = {}
    >>> mydict['PE1']
    KeyError: 'PE1'

    # Genie dictionary
    >>> myfeature.device_attr['PE1']
    <__main__.MyFeature.PerDeviceAttr object at 0x10c5bdb38>

This works as ``Genie`` dicitonary inherits from defaultdict_ with some
modification on top of it. However, to make the code easier to read,
a function was added `create`

.. code-block:: python

    # With new create function
    >>> myfeature.device_attr['PE1'].create()

    # Does exactly the same as 
    >>> myfeature.device_attr['PE1']
    # But looks better and is easier to create.

.. _defaultdict: https://docs.python.org/3/library/collections.html#collections.defaultdict
.. _ordereddict: https://docs.python.org/3/library/collections.html#collections.OrderedDict

.. _attributes_propagation:

Attributes propagation
----------------------

This sections focuses on tying together all those concepts, to create a
mechanism to propagate attributes to other `SubAttributes`.

The benefit of attributes progation is that you can set default values, and
all subAttributes under this object will use those as default values. If those
subAttributes set their own attributes with the same name, then it overwrites
the default values.

Let's work it out on an example, using the same as earlier.

.. code-block:: python

    from genie.conf.base import Feature
    from genie.conf.base.attributes import SubAttributes, SubAttributesDict

    class MyFeature(Feature):

        class PerDeviceAttr(SubAttributes):
            pass

        def __init__(self, **kwargs):
            self.maximum_hop = None
            self.speed = None
            self.device_attr = SubAttributesDict(self.PerDeviceAttr, self)

            super().__init__(**kwargs)


    >>> myfeature = MyFeature()
    # Set the default for this feature speed to be 5
    >>> myfeature.speed = 5
    >>> myfeature.speed
    5
    # Verify it was propagated to the device_attr
    >>> myfeature.device_attr['PE1'].speed
    5
    # Though it can be changed
    >>> myfeature.device_attr['PE1'].speed = 8
    >>> myfeature.device_attr['PE1'].speed
    8
    # As it wasn't changed for P1, still use the default
    >>> myfeature.device_attr['P1'].speed
    5

This concept also can be chained, if there are many level of `SubAttributes`.

One last detail, is the `self` at the end of `SubAttributesDict` declaration.
It dictates the propagation relationship. It can be read like this :

Create a `SubAttributesDict` that contains class `PerDeviceAttr`, and when
requesting an unknown attribute in those class, verify if `self`
knowns about it.

