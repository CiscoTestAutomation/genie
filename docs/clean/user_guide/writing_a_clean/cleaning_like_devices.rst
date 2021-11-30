.. _clean_doc_cleaning_like_devices:

Cleaning Like Devices
=====================

This topic contains the information required to group devices together in order to perform a clean operation on
*multiple similar devices* in your testbed. The `groups` block is an optional block.

.. topic:: Devices can be grouped by:

    * Device - Manually provide a list of devices that belong to a group.
    * Platform - Provide the platform and all devices with that platform will be grouped together under this group.
    * OS - Provide the os and all devices with that os will be grouped together under this group.

.. note::

    Only one method is supported per group. You cannot combine group-by-device, group-by-platform and group-by-os in the same group.
    You can have multiple groups with each group using a different method (a sample is provided below showing this option).

Device groups **simplify** the ``Clean YAML``, by removing duplicate stages and arguments for devices that use a similar clean.

For example, if you have two devices in the `devices` block that use the same stages, arguments, and order, then you
could combine these devices under one group.

.. topic:: The topics covered in this section are:

    * `How to Specify Device Groups?`_
    * `How to add Stages to Device Groups?`_

How to Specify Device Groups?
-----------------------------

.. note::

    These examples only show the required Device/Platform/OS Group information part of the Clean YAML file,
    and not the entire file requirements.

.. topic:: Option 1: Device - Manually provide a list of devices that belong to a group.

    The following ``Clean YAML`` demonstrates how to create a group that contains `PE1` and `PE2`

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 6-8, 10-16

        cleaners:
            # This means to use the cleaner class `PyatsDeviceClean`
            PyatsDeviceClean:
                # The module is where the cleaner class above can be found
                module: genie.libs.clean
                # You can define many groups within the Clean YAML.
                # Any groups not in this list are not cleaned even if they are defined below.
                groups: [my_group_by_device]

        groups:
            # The group name can be anything
            my_group_by_device:
                # The 'devices' key takes a list of devices you want under this group
                devices:
                    - PE1
                    - PE2

.. topic:: Option 2: Platform - Provide the platform and all devices with that platform will be grouped together under this group.

    The following ``Clean YAML`` demonstrates how to create a group that contains all devices of the `n9k` platform.

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 6-8, 10-15

        cleaners:
            # This means to use the cleaner class `PyatsDeviceClean`
            PyatsDeviceClean:
                # The module is where the cleaner class above can be found
                module: genie.libs.clean
                # You can define many groups within the Clean YAML.
                # Any groups not in this list are not cleaned even if they are defined below.
                groups: [my_group_by_platform]

        groups:
            # The group name can be anything
            my_group_by_platform:
                # The 'platforms' key takes a list of all platforms you want under this group
                platforms:
                    - n9k

.. topic:: Option 3: OS - Provide the os and all devices with that os will be grouped together under this group.

    The following ``Clean YAML`` demonstrates how to create a group that contains all devices of the `iosxe` os.

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 6-8, 10-15

        cleaners:
            # This means to use the cleaner class `PyatsDeviceClean`
            PyatsDeviceClean:
                # The module is where the cleaner class above can be found
                module: genie.libs.clean
                # You can define many groups within the Clean YAML.
                # Any groups not in this list are not cleaned even if they are defined below.
                groups: [my_group_by_os]

        groups:
            # The group name can be anything
            my_group_by_os:
                # The 'os' key takes a list of all os you want under this group
                os:
                    - iosxe

.. topic:: Adding multiple groups to the same Clean YAML.

    The following ``Clean YAML`` demonstrates how to combine two groups, where one group uses `group-by-device` and the other
    uses `group-by-platform`.

    .. code-block:: yaml
        :caption: Clean YAML
        :linenos:
        :emphasize-lines: 6-8, 10-16, 18-22

        cleaners:
            # This means to use the cleaner class `PyatsDeviceClean`
            PyatsDeviceClean:
                # The module is where the cleaner class above can be found
                module: genie.libs.clean
                # You can define many groups within the Clean YAML.
                # Any groups not in this list are not cleaned even if they are defined below.
                groups: [my_group_by_device, my_group_by_platform]

        groups:
            # The group name can be anything
            my_group_by_device:
                # The 'devices' key takes a list of devices you want under this group
                devices:
                    - PE1
                    - PE2

            # The group name can be anything
            my_group_by_platform:
                # The 'platforms' key takes a list of all platforms you want under this group
                platforms:
                    - n9k

How to add Stages to Device Groups?
-----------------------------------

.. note::

    In the event you do not know what a stage is, what it does, and what arguments they accept, you can find that information
    in the :ref:`Clean Stages <clean_doc_clean_stages>` document.

Adding a stage to a group is the same as adding a stage to a device under the `devices` block.

.. topic:: There are three steps in order to add a stage to the clean.

    #. Find a suitable stage from the `Clean Stage Browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean>`_.
    #. Choose which device to add the stage under.
    #. Choose the order the stage(s) will execute in.

Below is an example of adding the `connect <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean/connect>`_
stage under `my_group_by_device` and `my_group_by_platform` in the ``Clean YAML``. This stage has a few arguments that are
all optional. If in the case you are satisfied with the default values, you can leave the value side of the key-value
pair empty as shown in the example.

The `order` key must also be defined, even if there is only one stage.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 18, 20-21, 29, 31-32

    cleaners:
        # This means to use the cleaner class `PyatsDeviceClean`
        PyatsDeviceClean:
            # The module is where the cleaner class above can be found
            module: genie.libs.clean
            # You can define many groups within the Clean YAML.
            # Any groups not in this list are not cleaned even if they are defined below.
            groups: [my_group_by_device, my_group_by_platform]

    groups:
        # The group name can be anything
        my_group_by_device:
            # The 'devices' key takes a list of devices you want under this group
            devices:
                - PE1
                - PE2

            connect:

            order:
                - connect

        # The group name can be anything
        my_group_by_platform:
            # The 'platforms' key takes a list of all platforms you want under this group
            platforms:
                - n9k

            connect:

            order:
                - connect

It is supported to add as many stages as needed. Below is an example of adding another stage called
`apply_configuration <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean/apply_configuration>`_
under `my_group_by_device` and `my_group_by_platform` in the ``Clean YAML``. To pass any arguments for the stage,
simply add it under the stage as shown in the example.

It will run after the `connect` stage as defined under the `order` key.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 20-23, 27, 37-40, 44

    cleaners:
        # This means to use the cleaner class `PyatsDeviceClean`
        PyatsDeviceClean:
            # The module is where the cleaner class above can be found
            module: genie.libs.clean
            # You can define many groups within the Clean YAML.
            # Any groups not in this list are not cleaned even if they are defined below.
            groups: [my_group_by_device, my_group_by_platform]

    groups:
        # The group name can be anything
        my_group_by_device:
            # The 'devices' key takes a list of devices you want under this group
            devices:
                - PE1
                - PE2

            connect:

            apply_configuration:
                configuration: |
                    interface GigabitEthernet1
                    shutdown

            order:
                - connect
                - apply_configuration

        # The group name can be anything
        my_group_by_platform:
            # The 'platforms' key takes a list of all platforms you want under this group
            platforms:
                - n9k

            connect:

            apply_configuration:
                configuration: |
                    interface GigabitEthernet1
                    shutdown

            order:
                - connect
                - apply_configuration

.. note::

    Every Clean Stage under the group applies to all devices in the specified group but can be overwritten by
    specifying a stage under a specific device in the `devices` block.

    For example, in this ``Clean YAML`` the highlighted lines overwrite the `apply_configuration` stage on `line 20` to
    `no shutdown` instead of `shutdown` interface GigabitEthernet1 on the `PE1` device.

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 46-51

        cleaners:
            # This means to use the cleaner class `PyatsDeviceClean`
            PyatsDeviceClean:
                # The module is where the cleaner class above can be found
                module: genie.libs.clean
                # You can define many groups within the Clean YAML.
                # Any groups not in this list are not cleaned even if they are defined below.
                groups: [my_group_by_device, my_group_by_platform]

        groups:
            # The group name can be anything
            my_group_by_device:
                # The 'devices' key takes a list of devices you want under this group
                devices:
                    - PE1
                    - PE2

                connect:

                apply_configuration:
                    configuration: |
                        interface GigabitEthernet1
                        shutdown

                order:
                    - connect
                    - apply_configuration

            # The group name can be anything
            my_group_by_platform:
                # The 'platforms' key takes a list of all platforms you want under this group
                platforms:
                    - n9k

                connect:

                apply_configuration:
                    configuration: |
                        interface GigabitEthernet1
                        shutdown

                order:
                    - connect
                    - apply_configuration

        devices:
            PE1:
                apply_configuration:
                    configuration: |
                        interface GigabitEthernet1
                        no shutdown
