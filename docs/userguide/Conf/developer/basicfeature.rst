.. _new_feature:

First Steps
===========

This section focuses on developing a brand new configurable `Feature`.

A `Feature` is a device component that can be configured. The configuration of
this `Feature` is driven via object attributes.

Read each section in order, as each new concepts builds on top of previously
explained concept.

This documentation is meant to be interactive. Every block of code is
executable in your pyATS virtual environment. All you need to do is activate
your virtual environment, and make sure ``Genie`` is installed. Then go in
python interactive shell to paste the code in there.  This allow to read,
and run the code to get a better understanding. You can also modify the code
and learn this way.

Configurable Feature
--------------------

A `Feature` is stored into a python module, which contains a class with the
specific `Feature` name. This class must inherit from either `LinkFeature`,
`InterfaceFeature` or `DeviceFeature`, or any combination of those classes.

* `LinkFeature` is used when this `Feature` can be applied on a link.
* `DeviceFeature` is used when this `Feature` can be applied on a Device.
* `InterfaceFeature` is used when this `Feature` can be applied on an
  Interface.

.. code-block:: python

    from genie.conf.base.base import DeviceFeature, LinkFeature
    # A Vrf is a feature that is configured on a device
    class Vrf(DeviceFeature):
        pass

    # Ldp can be configured on a single device, or
    # on all devices connected to this link
    class Ldp(DeviceFeature, LinkFeature):
        pass

.. hint::

    All code in those examples are executable. This allows you to play
    with the code as you read. When the code is too long to be
    posted on the website, a download location is provided.

.. hint::

    To execute those example, source your virtual environment,
    type python, and paste the code in there.

Let's add some attributes to our `Vrf` `Feature`. The simplest way is to add
`__init__` method which only contains the configurable attributes for this
`Vrf`. By default all of them should be set to `None`, unless there is a
reason to assign them to another value. As an extra functionality to the
`Feature` objects, any `**kwargs` passed to `__init__` will be automatically
stored into the `Vrf` object.

.. code-block:: python

    #### Imports ####
    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie.conf.base.base import DeviceFeature

    #### VRF class ####
    class Vrf(DeviceFeature):
        def __init__(self, name, **kwargs):
            self.name = name
            self.description = None
            self.vrf = None
            # Call back parent's __init__
            super().__init__(**kwargs)

    #### Main section ####
    # Set Genie Tb
    from genie.conf import Genie
    testbed = Testbed()
    Genie.testbed = testbed
    dev1 = Device(name='pe1', testbed=testbed, os='nxos')
    vrf1 = Vrf(name='blue')
    vrf1.description
    # None
    vrf1.description = 'vrf_blue'
    vrf1.description
    # vrf_blue
    vrf1 = Vrf(name='blue', description='vrf_blue',
               extra_args=13)
    vrf1.description
    # vrf_blue
    vrf1.extra_args
    # 13

.. warning::

    `Feature` __init__ must call its parent class with `super`, otherwise some
    functionalities will be lost.

Now, that we have seen how to set attributes in `__init__`, let's discuss how
to use those attributes to configure and unconfigure our `Feature`. For
the next sections, only configuring will be used to keep everything simple,
but exactly the same concept apply to unconfig. Final example with unconfig
is available in :ref:`managedattribute`

``build_config`` is a method that generates and adds configuration for a
specific `Feature`. It must satisfy a few requirements :

.. _requirement:

All attributes of the feature is used to build the feature, unless specific
argument are passed via the `Attributes`. Then only those are used.

 1. Attributes of the `Feature` drive the configuration, unless argument
    `attributes` is passed to the method. Then `attributes` control what get
    configured. (See note below)
 2. Mechanism to propagate attribute through multiple object level.
 3. By Default, the configuration will be applied on the devices when the api
    is called. Using `apply=False` will instead return a dictionary.
 4. Mechanism to configure only specific devices.

.. note::

    Regarding the first requirement, the argument `attributes` is used to
    modify the `Feature` instead of reconfiguring the whole `Feature`. Please
    refer to the :ref:`attributes` section for more information.

With these requirement in mind, here is how to write a basic ``build_config``
for a `Feature`, fully implemented in Python, without any magic .... yet.

.. code-block:: python

    #### Imports ####
    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie.conf.base.base import DeviceFeature

    #### Vrf class ####
    class Vrf(DeviceFeature):
        def __init__(self, name):
            self.name = name
        def build_config(self, devices=None, apply=True):
            # Allow to pass a list of Devices,
            # then only those devices will be configured
            # Requirement 4
            if devices is None:
                devices = self.devices
            # Make sure we remove duplicate device (in case)
            devices = set(devices)
            # Hold the configuration for each device in a separate key of the
            # dictionary.
            cfgs = {}
            for device in devices:
                # List containing configuration for this loop
                # will be added to cfgs
                cfg = []
                # Configure vrf on the device
                cfg.append('vrf {name}'.format(name=self.name))
                # Requirement 1
                # Let the configurable_attributes drive the configuration
                if hasattr(self, 'description') and self.description:
                    # Configure description on the device
                    # with an indendation for the config
                    cfg.append(' description {description}'.
                                format(description=self.description))
                if hasattr(self, 'rd') and self.rd:
                    # Configure rd on the device
                    # with an indendation for the config
                    cfg.append(' rd {rd}'.
                                format(rd=self.rd))
                cfgs[device.name] = cfg
            # Requirement 3
            if apply:
                for device in devices:
                    if cfgs[device.name]:
                        device.configure(cfgs[device.name])
            else:
                return cfgs

    #### Main section ####
    # Set Genie Tb
    testbed = Testbed()
    Genie.testbed = testbed
    dev1 = Device(name='pe1', testbed=testbed, os='nxos')
    vrf1 = Vrf(name='blue')
    print(vrf1.build_config(devices=[dev1], apply=False))
    # {'pe1': ['vrf blue']}

    # Let's add a description
    vrf1.description = 'vrf_blue'
    vrf1.rd = '800:1'
    print(vrf1.build_config(devices=[dev1], apply=False))
    # {'pe1': ['vrf blue', ' description vrf_blue', ' rd 800:1']}

The above example satisfy most of the above requirement for ``build_config``,
except requirement 1 and 2 which are not fully satisfied.

 1. Attributes of the `Feature` drive the configuration, unless argument
    `attributes` is passed to the method. Then `attributes` control what get
    configured.
 2. The same feature object can be associated with multiple objects, such as
    device, address families, this association allows any attributes set at the
    feature, or any level, to also propagate to the object the feature were
    associated with. 

The next section will demonstrated how to do so.

.. important::

    Take a moment to understand fully the above example and run it once in your
    terminal, it is the foundation that we will build the rest of Genie
    configuration `Feature` object on.
