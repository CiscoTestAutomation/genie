.. _attribute_helper:

Attributes helper
=================

This section continues the evolution of our ``Genie`` configurable object,
and add `AttributesHelper` which make the `Feature` objects much more
powerful.

Attributes
----------

`AttributesHelper` replaces the boilerplate coding requirement for each
`feature` to deal with the attributes. It also takes care of requirement 1 and
2 from the previous section.

 1. Attributes of the `Feature` drive the configuration, unless argument
    `attributes` is passed to the method. Then `attributes` control what get
    configured.
 2. The same `feature` object can be associated with multiple objects, such as
    device, address families, this association allows any attributes set at the
    `feature`, or any level, to also propagate to the object the `feature` were
    associated with. 

The next example shows that `AttributesHelper` can do everything that was
possible in the previous section, while removing some extra code.

.. code-block:: python

    #### Imports ####
    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie.conf.base.base import DeviceFeature
    from genie.conf.base.attributes import AttributesHelper

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
            # New attribute helper
            attributes = AttributesHelper(self)
            # Make sure we remove duplicate device (in case)
            devices = set(devices)
            # Hold the configuration for each device in a separate key of the
            # dictionary.
            cfgs = {}
            for device in devices:
                # List containing configuration for this loop
                # will be added to cfg
                cfg = []
                # Configure vrf on the device
                cfg.append('vrf {name}'.format(name=attributes.value('name')))
                # Requirement 1
                # Let the configurable_attributes drive the configuration
                if attributes.value('description'):
                    # Configure description on the device
                    # with an indendation for the config
                    cfg.append(' description {description}'.
                                format(description=attributes.value('description')))
                if attributes.value('rd'):
                    # Configure rd on the device
                    # with an indendation for the config
                    cfg.append(' rd {rd}'.
                                format(rd=attributes.value('rd')))
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
    vrf1.description = 'blue_vrf'
    vrf1.rd = '800:1'
    print(vrf1.build_config(devices=[dev1], apply=False))
    # {'pe1': ['vrf blue', ' description blue_vrf', ' rd 800:1']}


The above code is similar as the previous example with some logic was removed,
we've kept what we had so far.  Let's now tackle our the second half of the
first requirement (in bold) with our new `AttributesHelper`.

 1. Attributes of the `Feature` drive the configuration, **unless argument
    `attributes` is passed to the method. Then `attributes` control what get
    configured.**

.. code-block:: python

    #### Imports ####
    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie.conf.base.base import DeviceFeature
    from genie.conf.base.attributes import AttributesHelper

    #### Vrf class ####
    class Vrf(DeviceFeature):
        def __init__(self, name, **kwargs):
            self.name = name
            super().__init__(**kwargs)
        def build_config(self, devices=None, attributes=None, apply=True):
            # Allow to pass a list of Devices,
            # then only those devices will be configured
            # Requirement 4
            if devices is None:
                devices = self.devices
            # New attribute helper
            attributes = AttributesHelper(self, attributes)
            # Make sure we remove duplicate device (in case)
            devices = set(devices)
            # Hold the configuration for each device in a separate key of the
            # dictionary.
            cfgs = {}
            for device in devices:
                # List containing configuration for this loop
                # will be added to cfg
                cfg = []
                # Configure vrf on the device
                cfg.append('vrf {name}'.format(name=attributes.value('name')))
                # Requirement 1
                # Let the configurable_attributes drive the configuration
                if attributes.value('description'):
                    # Configure description on the device
                    # with an indendation for the config
                    cfg.append(' description {description}'.
                                format(description=attributes.value('description')))
                if attributes.value('rd'):
                    # Configure rd on the device
                    # with an indendation for the config
                    cfg.append(' rd {rd}'.
                                format(rd=attributes.value('rd')))
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
    vrf1 = Vrf(name='blue', description = 'blue_vrf', rd='800:1')
    print(vrf1.build_config(devices=[dev1], apply=False))
    # {'pe1': ['vrf blue', ' description blue_vrf', ' rd 800:1']}

    # let's modify the description and re-apply only this section
    vrf1.description = 'blue_vrf_ver2'
    print(vrf1.build_config(devices=[dev1], apply=False,
                            attributes={'description':None,
                                        'name':None}))
    # {'pe1': ['vrf blue', ' description blue_vrf_ver2']}


`AttributesHelpers` does all the heavy work for us, all it took was adding one
argument to it and using it with `AttributesHelper`.

.. code-block:: python

     def build_config(self, devices=None, attributes=None, apply=True):
         attributes = AttributesHelper(self, attributes)

We've added an argument named `attributes`, and passed it to
`AttributesHelper`. In the above example, description was modified, and only
this specific section was re-configured for this particular vrf.

.. hint::

    More to come... I recommend to go get some MORE coffee and take a break...
    (I know I needed it in order to write on)

.. _subattributes:

KeyedSubAttributes and SubAttributes
------------------------------------

A `Feature` in a `Device` is configured following a certain level of
hierarchy, mandating the attributes to be set in a certain fashion. Thus a
hierarchy of attributes is required. For example, some configuration is only
available when other configuration is present or when inside other block
of configuration.

.. code-block:: text

    router rip1
     address-family ipv4 unicast
      default-metric 1

`address-family ipv4 unicast` is only available inside `router rip1`.

`default-metric 1` is only available inside `address-family ipv4 unicast`.

This is what requirement 2 is all about.

 2. The same `feature` object can be associated with multiple objects, such as
    device, address families, this association allows any attributes set at the
    `feature`, or any level, to also propagate to the object the `feature` were
    associated with. 

Let's take the following configuration that we want on two devices.

.. code-block:: text

    PE1
     vrf Blue
      description PE1_blue_vrf
      rd 800:1
      address familly ipv4
       route-target import 1:1
      address familly ipv6
       route-target import 1:2

    PE2
     vrf Blue
      description PE2_blue_vrf
      rd 800:1
      address familly ipv4
       route-target import 1:1
      address familly ipv6
       route-target import 1:2

Let's list the requirements.

* Vrf Blue on both `Device`
* Different description on both device
* Same RD for both device
* Ipv4 and ipv6 configuration on both device
* A different ip address for each address familly and for each device

The idea to solve this is quite intuitive. Let's have a dictionary, where the
key represents a **unique identifier**, and the value is **another object**
holding the attributes for this object.

For example, the **unique identifier** could be the `Device` object, containing
a an `device_attr` object. Then this `device_attr` contains another dictionary
with `ipv4` key.

You can find below the structure that the object needs to hold to keep
all the information of the configuration.

.. code-block:: text

    # Object structure
    VRF Feature
     rd 800:1
     PE1
      description PE1_blue_vrf
      ipv4
       route-target import 1:1
      ipv6
       route-target import 1:2

     PE2
      description PE2_blue_vrf
      ipv4
       route-target import 1:1
      ipv6
       route-target import 1:2

.. code-block:: python

    # How to use it
    vrf1 = Vrf()
    # Attributes which is similar for all Vrf can be set at this level
    vrf1.rd = '800:1'

    # Dev1 Device attributes
    vrf1.device_attr[dev1.name].description = 'PE1_blue_vrf'
    # Dev1 Ipv4 attributes
    vrf1.device_attr[dev1.name].address_family['ipv4'].route_target = '1:1'
    # Dev1 Ipv6 attributes
    vrf1.device_attr[dev1.name].address_family['ipv6'].ip = '1:2'

    # Dev2 Device attributes
    vrf1.device_attr[dev2.name].description = 'PE2_blue vrf'
    # Dev2 Ipv4 attributes
    vrf1.device_attr[dev2.name].address_family['ipv4'].route_target ='1:1'
    # Dev2 Ipv6 attributes
    vrf1.device_attr[dev2.name].address_family['ipv6'].route_target = '1:2'

In the above example, we needed some object to hold these block of
attributes, we also needed a dictionary and a mechanism to propagate attributes
to children level. `KeyedSubAttributes` represent those objects, and
`KeyedSubAttributes` is the dictionary that ties everything together.

`KeyedSubAttributes` is a base class to hold the `blocks` of the above section.
This base class should be inherited and your own implementation should be
created from it. Inside the infrastructure of ``Genie`` we are also providing
two `KeyedSubAttributes` for script usage, `DeviceSubAttributes` and
`InterfaceSubAttributes`. An example of using `DeviceSubAttributes` can be found
below.

The next question is how do we all tie this back to the `feature` ?
`SubAttributesDict` comes to the rescue! It is a special dictionary that holds
multiple `blocks` of object. It basically works like this; when a key is
requested, it verify if it exists, if it does it returns the value, otherwise
it instantiate an object inherited from `KeyedSubAttributes` and stores it as a
value of this key. `SubAttributesDict` has a few more powers, but let's focus
on the base and the most important idea for now.

Let's jump into an example to demonstrate how all of these new concepts work.
We will modify our previous example to support configuration for multiple
`Device` in the same `Feature`.

Here are the changes that are needed :

* Import `DeviceSubAttributes` and `SubAttributesDict`
* Create a new DeviceAttributes Class which inherits from `DeviceSubAttributes`
* Add to the `__init__` of `Vrf` `SubAttributesDict`
* Add `build_config` and `build_unconfig` to loop each `Device` to configure.
* To loop over each `Device`, `attributes.mapping_items` is used. It's a new
  from `AttributesHelper`, which allow to loop over the dictionary and has a
  few extra functionality.

.. hint::

    All code in those examples are executable. This allows you to play
    with the code as you read. When the code is too long to be
    posted on the website, a download location is provided.

.. hint::

    To execute those example, source your virtual environment,
    type python, and paste the code in there.

.. code-block:: python

    #### Imports ####
    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie.conf.base.attributes import DeviceSubAttributes,\
                                           SubAttributesDict,\
                                           AttributesHelper
    from genie.conf.base.base import DeviceFeature

    #### Vrf class ####
    class Vrf(DeviceFeature):
        class DeviceAttributes(DeviceSubAttributes):
            def build_config(self, devices=None, apply=True, attributes=None):
                # List containing configuration for this loop
                # will be added to cfgs
                cfg = []
                # Configure vrf on the device
                cfg.append('vrf {name}'.format(name=self.name))
                # Requirement 1
                # Let the configurable_attributes drive the configuration
                if attributes.value('description'):
                    # Configure description on the device
                    # with an indendation for the config
                    cfg.append(' description {description}'.
                                format(description=attributes.value('description')))
                if attributes.value('rd'):
                    # Configure rd on the device
                    # with an indendation for the config
                    cfg.append(' rd {rd}'.
                                format(rd=attributes.value('rd')))
                return cfg
        # __init__ of Vrf
        def __init__(self, name, *args, **kwargs):
            self.device_attr = SubAttributesDict(self.DeviceAttributes,
                                                 parent=self)
            self.name = name
            super().__init__(*args, **kwargs)
        # Adding a new build_config, to call
        def build_config(self, devices=None, apply=True, attributes=None):
            cfgs = {}
            attributes = AttributesHelper(self, attributes)
            if devices is None:
                devices = self.devices
            #devices = set(dev.name for dev in devices)
            devices = set(devices)
            # Loop over all the items of 'self.device_attr', sort them,
            # and only care about the keys which are in keys.
            for key, sub, attributes2 in attributes.mapping_items(
                    'device_attr',
                    keys=devices, sort=True):
                # For each, call their build_config with attributes as an argument.
                # attributes2 is only the attributes related to this particular
                # device, and its parent attributes. (To allow parent default
                # values)
                cfgs[key] = sub.build_config(apply=False, attributes=attributes2)
            if apply:
                for device_name, cfg in sorted(cfgs.items()):
                    if cfg:
                        device = self.testbed.devices_map[device_name]
                        device.configure(cfg)
            else:
                return cfgs

    #### Main section ####
    # Set Genie Tb
    from genie.conf import Genie
    testbed = Testbed()
    Genie.testbed = Testbed()
    dev1 = Device(name='pe1', testbed=testbed, os='nxos')
    dev2 = Device(name='pe2', testbed=testbed, os='nxos')
    vrf1 = Vrf(name='blue')
    print(vrf1.build_config(devices=[dev1, dev2], apply=False))
    # {'pe1': ['vrf blue'],
    #  'pe2': ['vrf blue']}

    # Let's add a different description for both device
    vrf1.device_attr[dev1].description = 'PE1_blue_vrf'
    vrf1.device_attr[dev2].description = 'PE2_blue_vrf'
    # And same RD for both, we can set it at the parent level as we want it
    # to be of the same value
    vrf1.rd = '800:1'
    print(vrf1.build_config(devices=[dev1, dev2], apply=False))
    # {'pe1': ['vrf blue', ' description PE1_blue_vrf', ' rd 800:1'],
    #  'pe2': ['vrf blue', ' description PE2_blue_vrf', ' rd 800:1']}


All the above concepts scale, and can create many levels of structure. For
example, we could've put `AdressFamilyAttributes` as another level in our `Vrf`
example , which would have been placed under `DeviceAttributes`.

In the next section, we will demonstrate how configuration is created in a
scalable fashion.

