Execution Order
===============

Now that we have all the logic defined, we need to specify the order of which the stage steps execute in. The `exec_order` list is the variable used to specify this and will be read first-to-last. The list should contain the method names we wrote in the previous sections. Any methods not in the list will not execute. If the list contains an invalid name (a method that does not exist) a test will fail letting you know.

In this example the methods will execute in the following order:

1. delete_boot_variable
2. configure_boot_variable
3. set_configuration_register
4. write_memory
5. verify_boot_variable
6. verify_configuration_register

.. note::

    This documentation did not show the development of the remaining steps, though, they have been added for completeness. Please note that we have also updated the exec_order to accommodate the new steps.

.. code-block:: python
    :linenos:
    :emphasize-lines: 27-32, 35, 47, 74, 88, 98, 107

    from genie.metaparser.util.schemaengine import Optional
    from genie.libs.clean import BaseStage

    class ChangeBootVariable(BaseStage):

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