Cleaning Devices
================

For cleaning devices that are `unlike` each other (different os/platform/steps required) it is best to use the `devices`
block inside the ``Clean Yaml``. This block allows you to customize the clean on a per-device basis. The `devices`
block is an optional block (although most commonly used).

.. topic:: It is responsible for housing the clean information at a device-specific level such as:

    * Images to load
    * Stages to use
    * Order that the Stages should be executed in

.. topic:: The topics covered in this section are:

    * `Adding the Devices Block`_
    * `Adding a Device`_
    * `Adding Stages`_

Adding the Devices Block
------------------------

In the ``Clean YAML`` that has the `Cleaner Class` added, add the `devices` block as shown below.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 4, 6

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: []

    devices:

Adding a Device
---------------

Next, add the device to the ``Clean YAML`` in which we want to write a Clean for. This device must exist in your
Testbed YAML and for the purposes of this guide, the device is named `PE1`.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 4, 7

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1]

    devices:
        PE1:

It is supported to add any amount of devices under the devices block. Below shows how to add another device named `PE2`.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 4, 9

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1, PE2]

    devices:
        PE1:

        PE2:

Adding Stages
-------------

.. note::

    In the event you do not know what a stage is, what it does, and what arguments they accept, you can find that information
    in the :ref:`Intro to Stages <clean_doc_clean_stages>` document.

.. topic:: There are three steps in order to add a stage to the clean.

    #. Find a suitable stage from the `Clean Stage Browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean>`_.
    #. Choose which device to add the stage under.
    #. Choose the order the stage(s) will execute in.

Below is an example of adding the `connect <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean/connect>`_
stage under `PE1` in the ``Clean YAML``. This stage has a few arguments that are all optional. If in the case you are satisfied
with the default values, you can leave the value side of the key-value pair empty as shown in the example.

The `order` key must also be defined, even if there is only one stage.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 8, 10-11

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1, PE2]

    devices:
        PE1:
            connect:

            order:
            - connect

        PE2:

It is supported to add as many stages as needed. Below is an example of adding another stage called
`apply_configuration <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean/apply_configuration>`_
under `PE1` in the ``Clean YAML``. To pass any arguments for the stage, simply add it under the stage as shown in
the example.

It will run after the `connect` stage as defined under the `order` key.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 8, 10-11, 15

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1, PE2]

    devices:
        PE1:
            connect:

            apply_configuration:
                configuration: hostname PE1

            order:
            - connect
            - apply_configuration

        PE2:
