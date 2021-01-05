Abstraction
===========

In the previous sections, we've learn how to create a new `Feature`, though
the subject of abstraction hasn't been approached yet.

First make sure you have read ``pyats`` :ref:`abstract <abstract>`, especially the section on
:lookupdecorator:`Lookup Decorator <http>` as it is the core of abstraction in ``Genie`` `conf`.

Strategy
--------

The strategy is as follow:

1) Create a base class which holds the structure of the `Feature`
2) Create another version of this class for a or some tokens (could be OS,
   cli/yang/...) and implement the specific `build_config` for these
   tokens.

This allows to have the same structure and variable for all implementations,
while supporting different implementation for each token, or a series
of token.

Let's give an example, which is really close to the actual implementation
in ``Genie``.

.. code-block:: python

    from genie.abstract import lookup
    class Base(object):
        @lookup('os')
        def build_config(self, *args, **kwargs):
            '''Abstract method to build_config'''
            raise NotImplementedError
        @lookup('os')
        def build_unconfig(self, *args, **kwargs):
            '''Abstract method to build_unconfig'''
            raise NotImplementedError

    from genie.conf.base import ConfigurableBase
    from genie.decorator import managedattribute
    from genie.conf.base.config import CliConfig
    from genie.conf.base.attributes import DeviceSubAttributes,\
                                           SubAttributesDict,\
                                           AttributesHelper
    class MyFeature(ConfigurableBase):
    # Inheriting from Base (As all feature inherits from atleast one the
      Features classes)
        name = managedattribute(
                   name='name',
                   read_only=True,
                   doc='Name of the Feature')
        description = managedattribute(
                          name='description',
                          type=managedattribute.test_istype(str),
                          doc='Description of the Feature')
        class DeviceAttributes(DeviceSubAttributes):
            # And any other structure wanted
            pass
        def __init__(self, name, **kwargs):
            self._name = name
            self.device_attr = SubAttributesDict(self.DeviceAttributes,
                                                 parent=self)
            super().__init__(*kwargs)
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
                     if cfg:
                         device = self.testbed.devices[device_name]
                         device.configure(cfg)
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
                     if cfg:
                         device = self.testbed.devices[device_name]
                         device.configure(cfg)
             else:
                 return cfgs


So far, we have only created the structure of the Feature. It has
`DeviceAttributes`, it also contains 2 `managedattributes`. However
no configuration is part of it.

The configuration is inside a different file, inside a diferent directory, with
the token as directory name. For ``Genie``, the first token is `OS` name, so
`nxos`, `iosxr, `iosxe` and so on.

Let's now implement the configuration section of this `Feature`.

.. code-block:: python

    from genie.conf.base.config import CliConfig
    from genie.conf.base.cli import CliConfigBuilder
    from genie.conf.base.attributes import AttributesHelper
    class myFeature(object):
        class DeviceAttributes(object):
            def build_config(self, attributes=None, unconfig=False):
                attributes=AttributesHelper(self, attributes)
                configurations = CliConfigBuilder(unconfig=unconfig)
                with configurations.submode_context(
                                    attributes.format('feature {name}',
                                                       force=True)):
                    if unconfig and attributes.iswildcard:
                        configurations.submode_unconfig()
                    configurations.append_line(attributes.format('description {description}'))
                return CliConfig(device=self.device, unconfig=unconfig,
                                 cli_config=configurations)
            def build_unconfig(self, apply=True, attributes=None, **kwargs):
                return self.build_config(apply=apply, attributes=attributes,
                                         unconfig=True, **kwargs)

.. hint::

    This code is not executable, please see next section. This section
    only explains the concepts and the strategy.

This represents the configuration part of the code, which is in a different
files than the structure itself.

Let's revisit the structure of `genie_libs` now that we have this new
understanding.

.. code-block:: bash

  genie_libs
     `-- conf
         |-- __init__.py              <-- Package declaration
         `-- vrf                      <-- Feature Directory
             |-- __init__.py
             |-- vrf.py               <-- Structure file
             |-- iosxe                <-- Token
             |   |-- __init__.py      <-- Token declaration
             |   `-- vrf.py           <-- Configuration implementation
             |-- nxos                 <-- Token
             |   |-- __init__.py      <-- Token declaration
             |   `-- vrf.py           <-- Configuration implementation
             |-- iosxr                <-- Token
             |   |-- __init__.py      <-- Token declaration
             |   `-- vrf.py           <-- Configuration implementation
             `-- tests
                 `-- test_vrf.py

