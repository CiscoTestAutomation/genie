Defining a Device to Clean
==========================

In this section we will be defining our first device to clean using the cleaner class we previously added. There is no
limit to the number of devices that can be defined, however since this is a *quick start* guide, we will only be adding one.

To add a device inside the `Clean YAML` there are two different steps.

First we must add a top-level key called `devices`. Under that key we can add the device name. **Please note:** this
device must exist in your Testbed YAML.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 7-8

    cleaners:
        # This means to use the cleaner class `PyatsDeviceClean`
        PyatsDeviceClean:
            # The module is where the cleaner class above can be found
            module: genie.libs.clean

    devices:
        PE1:

Second, we must add a key inside the cleaners block called `devices` where the value is a list of the devices added.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 6-8

    cleaners:
        # This means to use the cleaner class `PyatsDeviceClean`
        PyatsDeviceClean:
            # The module is where the cleaner class above can be found
            module: genie.libs.clean
            # You can define many devices within the Clean YAML.
            # Any that are not in this list are not cleaned even if they are defined below.
            devices: [PE1]

    devices:
        PE1: