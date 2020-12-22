Feature
=======

In this section, users will learn how to add and configure a `Feature` in the ``Genie``
topology.

Introduction
------------

``Genie`` `conf` represents features via Python object. Those objects allow to
configure the feature through object attributes. The `Feature` object can be
added on a `Device`, an `Interface`, or a `Link`.  Whenever a `Feature` is
added on a `Link`, the `Feature` is configured on all `Devices` and
`Interfaces` connected to this `Link`.

.. _infrastructure:

Class 
-------

Before continuing with this section, user is encouraged to review and understand the Developer's Guide, which may be found at :ref:`Conf developer guide <dev>`. 

A `Feature` class has at least two functions: `build_config` and
`build_unconfig`, both of which will configure or unconfigure a `Feature` on
a `Device`.  The configurations applied on the `Device` depend on the
attributes of the `Feature` object.

Both of these functions,  `build_config` and `build_unconfig`, accept an argument called 
`attributes` which restrict which attributes to configure, by default all
attributes are configured.  

`managedattribute` enhances the attributes to the object by, quite simply,
giving additional powers to the attributes .  For example, a `managedattribute`
can a limited type, or make a variable read-only and so on. This helps with the
standardization of the class.  Please refer to :ref:`managed attributes
<managedattribute>` documentation for more information about the ways a
`managedattribute` may enhance the attributes to an object.

Users can apply a single ``Genie`` `Feature` object to configure a single
`Device` or  multiple `Devices`.  What's more, is that the configuration for
each `Device` may be identical, or different, depending on the user's needs.
This is controlled with the `device_attr`, which is always the first level of
any `Conf` object.
 
Genie's `Feature` object has a layering mechanism, which creates a hierarchy,
allowing each `Device` to be configured separately.  It can also create a
system of hierarchy which is similar to how a `Feature` is actually configured.
The feature hierarchy can have as many layers as the user desires.

`Feature` hierarchies are achieved with the help of ref:`attribute_helper`. 
This is an important subject and users should review this documentation carefully 
to fully undestand how to use these objects. 

.. _usage:

Usage
---------

This section will discuss how to use `Feature` objects and how to interconnect them
with ``Genie`` topology objects.

First, the  `Feature` object must be imported, and then an instance must be created. 

Below users will find an example for the feature `Rip`. 

.. note::

    The `genie_libs` code can change, so these examples may no longer run 
   	at the time you are reading this. However, the idea and its application 
   	will remain the same. 
   	
.. code-block:: python

    from genie.libs.conf.rip.rip import Rip
    rip = Rip()
    rip.distance = 10
    rip.maximum_paths = 15

Once created, the `Feature` object can be added on a `Device` or a `Link`
object.  Whenever the `Feature` object is added to a `Link`, it can quickly
propagate similar configurations throughout the topology. For example,
configuring a `Feature` on a `Link`, will configure all `Interfaces` and
`Devices` on and apart of the `Link`. However, if the `Feature` object is added
to a `Device`, the configuration is localized only to the particular `Device`. 

Following the example above, but this time using a `Device`:

.. code-block:: python

    # assuming two devices already exists,
    # adding the feature on the device
    >>> dev1.add_feature(rip)
    >>> dev2.add_feature(rip)

And this time, using a `Link`:

.. code-block:: python

    # assuming two devices already exists,
    # and connected via a link
    >>> link1.add_feature(rip)

This section has showcased how a `Feature` is applied in the ``Genie`` topology. 
Please refer to the :ref:`Conf developer guide <dev>` for further details. 
