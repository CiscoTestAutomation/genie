Final Version
=============

Final
-----

Here you can find the final version of what we have seen. It is very similar to
the one in :ref:`managedattribute`, but it contains `build_unconfig` method and
abstraction.

It is highly recommended to use this as a template for your first `Feature`
development. The following steps will guide you through it.  

.. code-block:: bash

    cd <pyats_root>/genie_libs/conf
    mkdir Template
    cd Template
    touch __init__.py
    touch vrf.py

Open this new file with your favourite editor. (Hopefully its vim). Let's first
create the structure of this Vrf `Feature`.

.. code-block:: python

    #### Imports ####
    from genie.decorator import managedattribute
    from genie.conf.base.config import CliConfig
    from genie.conf.base.base import DeviceFeature
    from genie.conf.base.attributes import DeviceSubAttributes,\
                                           SubAttributesDict,\
                                           AttributesHelper

    #### Vrf class ####
    class Vrf(DeviceFeature):
        class DeviceAttributes(DeviceSubAttributes):
            pass
        # Create the subAttributesDict for device_att
        # We want it readonly, as the dict shouldn't never be changed,
        # only the key/value.
        device_attr = managedattribute(
                          name='device_attr',
                          read_only=True,
                          doc=DeviceAttributes.__doc__)
        # When the variable is first created, it creates a subAttributesDict
        @device_attr.initter
        def device_attr(self):
            return SubAttributesDict(self.DeviceAttributes, parent=self)
        name = managedattribute(
                   name='name',
                   read_only=True,
                   doc='Name of the Vrf')
        description = managedattribute(
                          name='description',
                          type=managedattribute.test_istype(str),
                          doc='Description of the Vrf')
        rd = managedattribute(
                 name='rd',
                 type=managedattribute.test_istype(str),
                 doc='Rd of the Vrf')
        def __init__(self, name, *args, **kwargs):
            self._name = name
            super().__init__(*args, **kwargs)
        # Adding a new build_config, to call
        def build_config(self, devices=None, apply=True, attributes=None):
            cfgs = {}
            attributes = AttributesHelper(self, attributes)
            if devices is None:
                devices = self.devices
            devices = set(devices)
            # Loop over all the items of 'self.device_attr', sort them,
            # and only care about the keys which are in keys.
            for key, sub, attributes2 in attributes.mapping_items(
                    'device_attr', keys=devices, sort=True):
                # For each, call their build_config with attributes as an argument.
                # attributes2 is only the attributes related to this particular
                # device, and its parent attributes. (To allow parent default
                # values)
                cfgs[key] = sub.build_config(apply=False,
                                             attributes=attributes2)
            if apply:
                for device_name, cfg in sorted(cfgs.items()):
                    self.testbed.config_on_devices(cfg, fail_invalid=True)
            else:
                return cfgs
        def build_unconfig(self, devices=None, apply=True, attributes=None):
            cfgs = {}
            attributes = AttributesHelper(self, attributes)
            if devices is None:
                devices = self.devices
            devices = set(devices)
            # Loop over all the items of 'self.device_attr', sort them,
            # and only care about the keys which are in keys.
            for key, sub, attributes2 in attributes.mapping_items(
                    'device_attr', keys=devices, sort=True):
                # For each, call their build_config with attributes as an argument.
                # attributes2 is only the attributes related to this particular
                # device, and its parent attributes. (To allow parent default
                # values)
                cfgs[key] = sub.build_unconfig(apply=False,
                                             attributes=attributes2)
            if apply:
                for device_name, cfg in sorted(cfgs.items()):
                    self.testbed.config_on_devices(cfg, fail_invalid=True)
            else:
                return cfgs

Alright,  let's now create the configuration section of it. Please do those
steps in your terminal.

.. code-block:: bash

    mkdir nxos
    cd nxos
    touch __init__.py
    touch vrf.py

For this example, `nxos` is used, but it could be any other os. We first
need to hook up `nxos` as a token in the `__init__.py` file. Open it and add
the following lines.

.. code-block:: python

    # Enable abstraction using this directory name as the abstraction token
    try:
        from genie import abstract
        abstract.declare_token(__name__)
    except Exception as e:
        warnings.warn('Could not declare abstraction token: ' + str(e))

Once done, open the `vrf.py` file inside the `nxos` directory. This represent
the configuration.

.. code-block:: python

    #### Imports ####
    from genie.decorator import managedattribute
    from genie.conf.base.cli import CliConfigBuilder
    from genie.conf.base.attributes import AttributesHelper

    #### Vrf class ####
    class Vrf(object):
        class DeviceAttributes(object):
            def build_config(self, devices=None, apply=True, attributes=None,
                             unconfig=False):
                attributes = AttributesHelper(self, attributes)
                # List containing configuration for this loop
                # Instantiate configurations
                configurations = CliConfigBuilder(unconfig=unconfig)
                # Create Vrf Submode context
                with configurations.submode_context(
                                    attributes.format('vrf {name}',
                                                      force=True)):
                    if unconfig and attributes.iswildcard:
                        configurations.submode_unconfig()
                    configurations.append_line(attributes.format('description {description}'))
                    configurations.append_line(attributes.format('rd {rd}'))
                return CliConfig(device=self.device, unconfig=unconfig,
                                 cli_config=configurations)
            def build_unconfig(self, apply=True, attributes=None, **kwargs):
                return self.build_config(apply=apply, attributes=attributes,
                                         unconfig=True, **kwargs)


All done,  let's test it out now.

.. code-block:: python

    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie_libs.conf.Template.vrf import Vrf
    # Set Genie Tb
    testbed = Testbed()
    Genie.testbed = testbed
    dev1 = Device(name='pe1', testbed=testbed, os='nxos')
    dev2 = Device(name='pe2', testbed=testbed, os='nxos')
    vrf1 = Vrf(name='blue')

    # Let's add a specific description for dev1 and a default one
    vrf1.device_attr[dev1.name].description = 'Pe1 blue vrf'
    vrf1.description = 'Default description'

    #vrf1.device_attr[dev2].description = 'Pe2 super blue vrf'
    # And same RD for both, we can set it at the parent level as we want it
    # to be of the same value
    vrf1.rd = '800:1'
    print(vrf1.build_config(devices=[dev1, dev2], apply=False))
    # {'pe2': 'vrf blue\n description Pe2 super blue vrf\n rd 800:1\n exit',
    #  'pe1': 'vrf blue\n description Pe1 blue vrf\n rd 800:1\n exit'}

    # And for unconfiguring
    vrf1.build_unconfig(devices=[dev1, dev2], apply=False)
    # {'pe2': 'no vrf blue', 'pe1': 'no vrf blue'}

    # Let's do it for only a few specific attributes
    vrf1.build_config(devices=[dev1, dev2], apply=False,
                      attributes={'device_attr':{'*':{'description':None}}})
    # {'pe1': 'vrf blue\n description Pe1 blue vrf\n exit',
    #  'pe2': 'vrf blue\n description Default description\n exit'}
    # And now unconfig
    vrf1.build_unconfig(devices=[dev1, dev2], apply=False,
                        attributes={'device_attr':{'*':{'description':None}}})
    # {'pe1': 'vrf blue\n no description Pe1 blue vrf\n exit',
    #  'pe2': 'vrf blue\n no description Default description\n exit'}

    help(Vrf)

With this, you are on your way to create your own `Feature`. Always keep an eye
in `genie_libs` repository to see what the community is cooking up!

Yang
----

The previous sections demonstrated the coding style which ``Genie`` encourages.
The same concepts applies for any other configuration method, for example
`Yang`.

For any `Yang` development we are encouraging to use :ydk:`ydk <http>`. It is a Cisco tool,
which allows to configure and read operational data with objects. You can find
example on how to develop it under :
`genie_libs/conf/vrf/iosxe/yang/vrf.py`
