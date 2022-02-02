Abstracted Stages
=================

Abstracted Stages allow us to reuse existing code and/or change the order of execution with minimal coding required.

Parent class (IOSXE ChangeBootVariable)
---------------------------------------

This is the parent class we will inherit for our cat9k implementation.

.. code-block:: python
    :linenos:

    from genie.metaparser.util.schemaengine import Optional
    from genie.libs.clean import BaseStage

    class ChangeBootVariable(BaseStage):
        """This stage configures boot variables of the device using the following steps:

        - Delete existing boot variables.
        - Configure boot variables using the provided 'images'.
        - Set the configuration-register using the provided 'config_register'.
        - Write memory.
        - Verify the boot variables are as expected.
        - Verify the configuration-register is as expected.

    Stage Schema
    ------------
    change_boot_variable:

        images (list): Image files to use when configuring the boot variables.

        timeout (int, optional): Execute timeout in seconds. Defaults to 300.

        config_register (str, optional): Value to set config-register for
            reload. Defaults to 0x2102.

        current_running_image (bool, optional): Set the boot variable to the currently
            running image from the show version command instead of the image provided.
            Defaults to False.

    Example
    -------
    change_boot_variable:
        images:
            - harddisk:/image.bin
        timeout: 150
    """

        # ============
        # Stage Schema
        # ============
        schema = {
            Optional('images'): list,
            Optional('timeout'): int,
            Optional('config_register'): str,
            Optional('current_running_image'): bool,
        }

        # =================
        # Argument Defaults
        # =================
        TIMEOUT = 300
        CONFIG_REGISTER = '0x2102'
        CURRENT_RUNNING_IMAGE = False

        # ==============================
        # Execution order of Stage steps
        # ==============================
        exec_order = [
            'delete_boot_variable',
            'configure_boot_variable',
            'set_configuration_register',
            'write_memory',
            'verify_boot_variable',
            'verify_configuration_register'
        ]

        def delete_boot_variable(self, steps, device):

            with steps.start("Delete any configure boot variables") as step:

                try:
                    device.configure("no boot system")
                except Exception as e:
                    step.failed("Failed to delete configured boot variables",
                                from_exception=e)

                step.passed("Successfully deleted configured boot variables")

        def configure_boot_variable(self, steps, device, images, timeout=TIMEOUT,
                                    current_running_image=CURRENT_RUNNING_IMAGE):

            with steps.start("Set boot variable to images provided for {}".format(
                    device.name)) as step:

                if current_running_image:
                    log.info("Retrieving and using the running image due to "
                             "'current_running_image: True'")

                    try:
                        output = device.parse('show version')
                        images = [output['version']['system_image']]
                    except Exception as e:
                        step.failed("Failed to retrieve the running image. Cannot "
                                    "set boot variables",
                                    from_exception=e)

                try:
                    device.api.execute_set_boot_variable(
                        boot_images=images, timeout=timeout)
                except Exception as e:
                    step.failed("Failed to set boot variables to images provided",
                                from_exception=e)
                else:
                    step.passed("Successfully set boot variables to images provided")

        def set_configuration_register(self, steps, device,
                                       config_register=CONFIG_REGISTER, timeout=TIMEOUT):
            with steps.start("Set config register to boot new image on {}".format(
                    device.name)) as step:

                try:
                    device.api.execute_set_config_register(
                        config_register=config_register, timeout=timeout)
                except Exception as e:
                    step.failed("Failed to set config-register",
                                from_exception=e)
                else:
                    step.passed("Successfully set config register")

        def write_memory(self, steps, device, timeout=TIMEOUT):
            with steps.start("Execute 'write memory' on {}".format(device.name)) as step:
                try:
                    device.api.execute_write_memory(timeout=timeout)
                except Exception as e:
                    step.failed("Failed to execute 'write memory'",
                                from_exception=e)
                else:
                    step.passed("Successfully executed 'write memory'")

        def verify_boot_variable(self, steps, device, images):
            with steps.start("Verify next reload boot variables are correctly set "
                             "on {}".format(device.name)) as step:

                if not device.api.verify_boot_variable(boot_images=images):
                    step.failed("Boot variables are NOT correctly set")
                else:
                    step.passed("Boot variables are correctly set")

        def verify_configuration_register(self, steps, device,
                                          config_register=CONFIG_REGISTER):
            with steps.start("Verify config-register is as expected on {}".format(
                    device.name)) as step:

                if not device.api.verify_config_register(
                        config_register=config_register, next_reload=True):
                    step.failed("Config-register is not as expected")
                else:
                    step.passed("Config-register is as expected")

Abstracted ChangeBootVariable (IOSXE cat9k)
------

Abstracted stages should redefine the three main sections (`Stage Schema`, `Argument Defaults`, and `exec_order`) and the docstring. This removes any doubts about what order steps run in, argument values, and changes to the schema.

In the example you can see we modified the `exec_order` by removing the `configure_config_register` and `verify_config_register` steps. You can also see we did not have to rewrite any steps because we are reusing the same steps from the IOSXE implementation that we inherited.

.. code-block:: python
    :linenos:
    :emphasize-lines: 55-58

    from genie.libs.clean.stages.iosxe.stages import ChangeBootVariable as ChangeBootVariableIosxe

    class ChangeBootVariable(ChangeBootVariableIosxe):
        """This stage configures boot variables of the device using the following steps:

        - Delete existing boot variables.
        - Configure boot variables using the provided 'images'.
        - Write memory.
        - Verify the boot variables are as expected.

    Stage Schema
    ------------
    change_boot_variable:

        images (list): Image files to use when configuring the boot variables.

        timeout (int, optional): Execute timeout in seconds. Defaults to 300.

        current_running_image (bool, optional): Set the boot variable to the currently
            running image from the show version command instead of the image provided.
            Defaults to False.

    Example
    -------
    change_boot_variable:
        images:
            - harddisk:/image.bin
        timeout: 150
    """

        # ============
        # Stage Schema
        # ============
        schema = {
            Optional('images'): list,
            Optional('timeout'): int,
            Optional('current_running_image'): bool,

            # Deprecated
            Optional('check_interval'): int,
            Optional('max_time'): int,
            Optional('write_memory'): bool,
        }

        # =================
        # Argument Defaults
        # =================
        TIMEOUT = 300
        CURRENT_RUNNING_IMAGE = False

        # ==============================
        # Execution order of Stage steps
        # ==============================
        exec_order = [
            'delete_boot_variable',
            'configure_boot_variable',
            'write_memory',
            'verify_boot_variable'
        ]

If we needed to overwrite `delete_boot_variable` to change the behaviour all we do is define the method again and write our new logic.

.. code-block:: python
    :linenos:
    :emphasize-lines: 61-62

    from genie.libs.clean.stages.iosxe.stages import ChangeBootVariable as ChangeBootVariableIosxe

    class ChangeBootVariable(ChangeBootVariableIosxe):
        """This stage configures boot variables of the device using the following steps:

        - Delete existing boot variables.
        - Configure boot variables using the provided 'images'.
        - Write memory.
        - Verify the boot variables are as expected.

    Stage Schema
    ------------
    change_boot_variable:

        images (list): Image files to use when configuring the boot variables.

        timeout (int, optional): Execute timeout in seconds. Defaults to 300.

        current_running_image (bool, optional): Set the boot variable to the currently
            running image from the show version command instead of the image provided.
            Defaults to False.

    Example
    -------
    change_boot_variable:
        images:
            - harddisk:/image.bin
        timeout: 150
    """

        # ============
        # Stage Schema
        # ============
        schema = {
            Optional('images'): list,
            Optional('timeout'): int,
            Optional('current_running_image'): bool,

            # Deprecated
            Optional('check_interval'): int,
            Optional('max_time'): int,
            Optional('write_memory'): bool,
        }

        # =================
        # Argument Defaults
        # =================
        TIMEOUT = 300
        CURRENT_RUNNING_IMAGE = False

        # ==============================
        # Execution order of Stage steps
        # ==============================
        exec_order = [
            'delete_boot_variable',
            'configure_boot_variable',
            'write_memory',
            'verify_boot_variable'
        ]

        def delete_boot_variable(self, steps, device):
            # Here we would write the new logic which would be
            # ran instead of the IOSXE implementation