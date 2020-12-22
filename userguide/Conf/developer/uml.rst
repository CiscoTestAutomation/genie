.. _uml:

UML
===

This section demonstrate how the infrastructure is built. This section goes
into quite a bit of details, and is a suplement to help reading the actual
source code of ``Genie``.

Base
----

The infrastructure base classes are setup like this.

.. figure:: uml.png
    :align: center
    :alt: Genie

The following APIs are used to control the topology of the Testbed.

1. Base for all Genie objects, contains `__init__` and `__repr__`.
2. Base for all Genie `conf` objects. Contains `__init__` which is setting
   all extra `kwargs` to the object. instantiates the `__instances` dictionary
   which contains a weakref to all the Genie objects. `testbed` property is
   defined at this level.
3. Contains `build_config` and `build_unconfig` functions which are
   decorated via `@lookup('os', 'context')`. This enables :ref:`abstraction <abstract>`
   based on `device.os` and `device.context` for `conf` objects when either of
   these two methods are called
4. Contains default methods for all future features objects.
5. Base class for all Device-based feature object. What to when it is added,
   removed and so on.
6. Base class for all Interface-based feature object. What to when it is
   added,removed and so on.
7. Base class for all Link-based feature object.  What to when it is
   added,removed and so on.
8. Contains all the APIs to manipulate a `link`, and to add `features` to
   it.
9. Contains all the APIs to manipulate the `testbed`, add topology objects to
   it and also `features`.
10. Contains all the APIs to manipulate a `device`, and to add `features` to
    it.
11. Contains all the APIs to manipulate an `interfaces`, and to add `features`
    to it.

The following APIs are used to control the way the user interact with the
objects attributes, and the structured objects.

12. Base object which allows to inherits attributes from parent object.
    Overwrites `__setattr__, `__getattr__`, and `__delattr__`. Can also
    verify if a particular attribute is inherited.
13. Base class fo subattributes classes. It addeds testbed property.
14. Go through the API doc for this one,  cannot be sum up in a few lines.
15. Implementation of a KeyedSubattributes for a particular devices.
16. Implementation of a KeyedSubattributes for a particular interfaces.
