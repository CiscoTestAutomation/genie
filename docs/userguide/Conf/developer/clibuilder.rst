.. _cli:

Cli Config Builder
==================

CliConfigBuilder
----------------

This section demonstrates how to use `CliConfigBuilder`, which allows for
clearer, and faster development time. `CliConfigBuilder` handles building
configuration and unconfiguration string for each `Device`. It follows these
main ideas :

One object that handles everything related to cli building, in a simple manner
without redundant code for the user. It creates its own indentation,
knows how to configure and unconfig for specific attributes, deals with
appending block of configuration together and much more. These functionality
are available with the help of a few new class/methods.

`submode_context` creates new a new block of configuration. Every configuration
following it will contains an indentation and will automatically add an `exit`
command.  `Submode_context` is used with the keyword `with`. Everything under
the `with` indentation is configured inside this block. To get many block of
configuration, many `submode_context` can be chained together.

`attributes.format` allows to remove many `if` statement, and will match
`{value}` with `self.value`, which reduces the chances of typo and further
minimalize the amount of typing required. Please see an example below.

`configuration.submode_unconfig` allows to quickly remove the whole block
of configurations if unconfiguration is wanted and no other `attributes` is
given.

Here are the difference in the code between the previous examples:

* Import `CliConfigBuilder`.
* Replace cfgs for configurations, which is an instance of
  `CliConfigBuilder`.
* `configurations.submode_context` to create a new block of
  indendated configurations.
* `attributes.format` to help with formatting the string in combination with
  `configurations.append_line` to append the configuration.
* Add `unconfig` argument
* Add submode_unconfig

.. code-block:: python

    #### Imports ####
    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie.conf.base.base import DeviceFeature
    from genie.conf.base.cli import CliConfigBuilder
    from genie.conf.base.attributes import DeviceSubAttributes,\
                                           SubAttributesDict,\
                                           AttributesHelper


    #### Vrf class ####
    class Vrf(DeviceFeature):
        class DeviceAttributes(DeviceSubAttributes):
            def build_config(self, devices=None, apply=True, attributes=None,
                             unconfig=False):
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
                return str(configurations)
        # __init__ of Vrf
        def __init__(self, name, *args, **kwargs):
            self.device_attr = SubAttributesDict(self.DeviceAttributes,
                                                 parent=self)
            self.name = name
            super().__init__(*args, **kwargs)
        # Adding a new build_config, to call
        def build_config(self, devices=None, apply=True, attributes=None,
                         unconfig=False):
            cfgs = {}
            attributes = AttributesHelper(self, attributes)
            if devices is None:
                devices = self.devices
            devices = set(dev.name for dev in devices)
            # Loop over all the items of 'self.device_attr', sort them,
            # and only care about the keys which are in keys.
            for key, sub, attributes2 in attributes.mapping_items(
                    'device_attr', keys=devices, sort=True):
                # For each, call their build_config with attributes as an argument.
                # attributes2 is only the attributes related to this particular
                # device, and its parent attributes. (To allow parent default
                # values)
                cfgs[key] = sub.build_config(apply=False, 
                                             attributes=attributes2,
                                             unconfig=unconfig)
            if apply:
                for device_name, cfg in sorted(cfgs.items()):
                    if cfg:
                        device = self.testbed.devices[device_name]
                        device.configure(cfg)
            else:
                return cfgs

    #### Main section ####
    # Set Genie Tb
    testbed = Testbed()
    Genie.testbed = testbed
    dev1 = Device(name='pe1', testbed=testbed, os='nxos')
    dev2 = Device(name='pe2', testbed=testbed, os='nxos')
    vrf1 = Vrf(name='blue')
    print(vrf1.build_config(devices=[dev1, dev2], apply=False))
    # {'pe2': 'vrf blue\n exit', 
    #  'pe1': 'vrf blue\n exit'}

    # Let's add a different description for both device
    vrf1.device_attr[dev1.name].description = 'Pe1 blue vrf'
    vrf1.device_attr[dev2.name].description = 'Pe2 super blue vrf'
    # And same RD for both, we can set it at the parent level as we want it
    # to be of the same value
    vrf1.rd = '800:1'
    print(vrf1.build_config(devices=[dev1, dev2], apply=False))
    # {'pe2': 'vrf blue\n description Pe2 super blue vrf\n rd 800:1\n exit',
    #  'pe1': 'vrf blue\n description Pe1 blue vrf\n rd 800:1\n exit'}

    # Let's see our new unconfig power that was given for free
    # As no attributes were given, it then removes the whole block
    vrf1.build_config(devices=[dev1, dev2], apply=False, unconfig=True)
    # {'pe2': 'no vrf blue',
    #  'pe1': 'no vrf blue'}

    # Let's only remove a particular attribute configuration
    vrf1.build_config(apply=False, devices=[dev1, dev2],
                      attributes={'device_attr':{'*':{'description':{''}}}}, unconfig=True)
    # {'pe1': 'vrf blue\n no description Pe1 blue vrf\n exit',
    #  'pe2': 'vrf blue\n no description Pe2 super blue vrf\n exit'}

    # And remove both description and rd
    vrf1.build_config(apply=False, devices=[dev1, dev2],
                      attributes={'device_attr':{'*':{'description':None 'rd':None}}}, unconfig=True)
    # {'pe1': 'vrf blue\n no description Pe1 blue vrf\n no rd 800:1\n exit',
    #  'pe2': 'vrf blue\n no description Pe2 super blue vrf\n no rd 800:1\n exit'}

So far we've seen it saves development time, and gives cleaner code. One new
functionality is that it includes unconfiguration with it. It takes advantage
of the fact that most configuration can be removed with `no` in front of it.
In corner cases, users can provide `unconfig_cmd` to provide the cli to remove
the configuration to use. For example :

.. code-block:: python

    with configurations.submode_context(
        attributes.format('vrf {name}', force=True),
                           unconfig_cmd='no vrf'): 
        configurations.append_line(attributes.format('rd {rd}'),
                                   unconfig_cmd='no rd')
    
One last useful api that can be useful is `append_block`. It appends a block of
line into configurations.

`raw` is another argument which can be given. It guarantee that the string
given will not be modified. So no automatic string substitution, and no
automatic unconfiguration. `raw` accepts `True` or `False` as value.

CliConfig
---------

So far, at the end of the `build_config`, we've always returned the
configuration string. However, this mean to apply the configuration to the
device, we would need to keep track which configuration goes with which device.
Instead, let's create an object that does this for us.

`CliConfig` accepts the following arguments:

* `device` must be a `device object`
* `unconfig` must be `True`/`False`, depending if it is configuring or not
* `cli_config` must be the configuration `str`

`__str__` has been overwritten to return the `cli_config` string.

.. code-block:: python

   from genie.conf.base.config import CliConfig

   if apply:
       for device_name, cfg in sorted(cfgs.items()):
           if cfg:
               device = self.testbed.devices[device_name]
               device.configure(cfg)
   else:
       return CliConfig(device=self.device, unconfig=unconfig,
                        cli_config=cfgs)

YangConfig
---------

It is exactly the same a `CliConfig`, but related to `Yang` and `Ydk`.

`YangConfig` accepts the following arguments:

* `device` must be a `device object`
* `unconfig` must be `True`/`False`, depending if it is configuring or not
* `ncp` must be a `NetconfServiceProvider` object
* `crud_service` must be a `CrudService` object

.. code-block:: python

   from genie.conf.base.config import YangConfig

   if apply:

       # create netconf connection
       ncp = NetconfServiceProvider(self.device)


       if unconfig:
           crud_service.delete(ncp, ydk_obj)
       else:
           crud_service.create(ncp, ydk_obj)
   else:
       if unconfig:
           return YangConfig(device=self.device,
                             ydk_obj=ydk_obj,
                             ncp=NetconfServiceProvider,
                             crud_service=crud_service.delete)
       else:
           return YangConfig(device=self.device,
                             ydk_obj=ydk_obj,
                             ncp=NetconfServiceProvider,
                             crud_service=crud_service.create)

