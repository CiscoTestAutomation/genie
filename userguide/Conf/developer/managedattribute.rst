.. _managedattribute:

Managed Attribute
=================


`managedattribute` allows finer controls on how attributes are created, while
taking care of mundane and repetitive actions :

* Automatically document your code (provided the `doc` argument is used)
* Restricts value of the variables to be of certain types (makes the code more
  resistant)
* Mechanism to set variable to be read-only
* Defaults value for the variable
* ...

Let's play with some examples. It is highly encouraged to try
it in your own terminal and experience it yourself.

.. code-block:: python

    from genie.decorator import managedattribute
    class Test(object):
        # Create pid attribute
        pid = managedattribute(
                  name='pid',
                  doc='Pid of some application')
        # Create a name, which is read-only
        name = managedattribute(
                  name='name',
                  read_only=True,
                  doc='Name of some application')
        # Create speed with a default of 1000
        # and the type of the value must be an int
        speed = managedattribute(
                    name='speed',
                    default=1000,
                    type=managedattribute.test_istype(int),
                    doc='Speed of the application')


    test = Test()

    # Let's test pid
    # It behaves exactly the same as a normal attribute
    test.pid = 5
    print(test.pid)
    # 5
    test.pid = 9
    print(test.pid)
    # 9

    # Read-only attribute. It cannot be modified via the
    # attribute name itself. It has to be done via _attribute
    test.name = 'myApp'
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File ".../genie/src/genie/decorator.py", line 714, in __set__
    #     raise AttributeError('can\'t set attribute')
    # AttributeError: can't set attribute
    # Now it can be modified via the _name
    test._name = 'myApp'
    print(test.name)
    # myApp

    test.speed
    # 1000
    test.speed = 'not an int'
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File ".../genie/src/genie/decorator.py", line 718, in __set__
    #     return fset(inst, value)
    #   File ".../genie/src/genie/decorator.py", line 512, in _default_setter
    #     value = self._transform(value, self.__type)
    #   File ".../genie/src/genie/decorator.py", line 477, in _transform
    #     raise ValueError('{}: {}'.format(value, ' '.join(exceptions)))
    # ValueError: not an int: Not of type int.
    test.speed = 9
    test.speed
    # 9

    # Finally, automatic documentation
    help(Test)

.. hint::

    All code in those examples are executable. This allows you to play
    with the code as you read.

.. hint::

    To execute those example, source your virtual environment,
    type python, and paste the code in there.

Important details about `managedattribute`.

* `name` has to be exactly the same as the variable name.
* `Read-only` attributes cannot be modified, however it can be modified by
  adding a `_` in front of the variable name. This assure that it wouldn't be
  modified by mistake, but always on purpose. (Look at the `name` example)
* Many type can be given via tuple; for example:
  `type=(None, managedattribute.test_is(False),
  managedattribute.test_istype(str),)`.

Let's re-write our previous example with `manageattribute`.

.. code-block:: python

    #### Imports ####
    from genie.conf import Genie
    from genie.conf.base import Device
    from genie.conf.base import Testbed
    from genie.decorator import managedattribute
    from genie.conf.base.config import CliConfig
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

                return CliConfig(device=self.device, unconfig=unconfig,
                                 cli_config=configurations)
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
        # __init__ of Vrf
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

    # Let's add a specific description, and a default one
    vrf1.device_attr[dev1.name].description = 'Pe1 blue vrf'
    vrf1.description = 'Default description'

    # And same RD for both, we can set it at the parent level as we want it
    # to be of the same value
    vrf1.rd = '800:1'
    print(vrf1.build_config(devices=[dev1, dev2], apply=False))
    # {'pe2': 'vrf blue\n description Default description\n rd 800:1\n exit',
    #  'pe1': 'vrf blue\n description Pe1 blue vrf\n rd 800:1\n exit'}

    help(Vrf)

We've seen the following arguments :

* name : Must match the name of the variable
* default : Default value for this variable
* read_only : The variable cannot be written to, except using `_` in front of it it also cannot have a type.
* doc : Set documentation
* The use of `initter` to initialize class for using `SubAttributesDict`
