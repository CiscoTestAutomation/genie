Stage Docstring
===============

The final part to developing a clean stage is writing the docstring. The docstring is used in the `clean stage browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean>`_ to let users know what the stage does, what arguments are available, and what the arguments default to. It also provides an example of using the stage in the clean YAML file.

The docstring should adhere to this general format:

.. code-block:: bash

    """<description>

    Stage Schema
    ------------
    <schema>

    Example
    -------
    <example>
    """

This a complete example of a docstring for the stage we wrote in the previous sections. Be mindful of the indentation as multiline strings will contain leading whitespace if they exist which will then be rendered in the stage browser (which we dont want). Please use the same formatting for the schema.

.. code-block:: python
    :linenos:
    :emphasize-lines: 5-35

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