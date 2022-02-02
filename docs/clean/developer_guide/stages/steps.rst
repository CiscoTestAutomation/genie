Stage Steps
===========

Stage steps are the bread and butter of the clean stage as they do all the heavy lifting.

Lets continue with the `ChangeBootVariable` example you've seen in the previous pages. To change the boot variable on an IOSXE device I would have to take these steps:

* Delete any existing boot variables
* Configure my new boot variables
* Configure the config-register
* Write memory
* Verify the boot variables were set correctly
* Verify the config-register was set correctly

You can see there are six steps to changing and verifying the boot variable on an IOSXE device.

.. note::

    It's important to keep the steps to a stage small and manageable. This allows us to overwrite small sections of a stage and reuse the rest (for example cat9k doesn't use the config register).

Adding a step into the clean stage is simple. Lets go through it step-by-step for the first time.

Define a new method and give it a name that clearly describes the step. There are three arguments that will always be defined (`self`, `steps`, and `device`) but there may be more if you are passing arguments to the stage.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3

    class ChangeBootVariable(BaseStage):

        def delete_boot_variable(self, steps, device):

.. note::

    We have temporarily removed the schema, argument defaults, and exec_order for these examples.


Inside the method we always start with the steps object. Create a step and give it a descriptive title as it will be shown in the logs.

.. code-block:: python
    :linenos:
    :emphasize-lines: 5

    class ChangeBootVariable(BaseStage):

        def delete_boot_variable(self, steps, device):

            with steps.start("Delete any configure boot variables") as step:

Finally write Python code to complete any actions required.

If you need to fail the step because an exception was caught, make sure to pass the exception object to the `step.failed()` call using the `from_exception` argument like in the example. This will ensure the exception traceback is logged for ease of debugging.

.. code-block:: python
    :linenos:
    :emphasize-lines: 7-13

    class ChangeBootVariable(BaseStage):

        def delete_boot_variable(self, steps, device):

            with steps.start("Delete any configure boot variables") as step:

                try:
                    device.configure("no boot system")
                except Exception as e:
                    step.failed("Failed to delete configured boot variables",
                                from_exception=e)

                step.passed("Successfully deleted configured boot variables")

Adding back the schema, argument defaults, and exec_order, this is what you should have so far.

.. code-block:: python
    :linenos:

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

        ]

        def delete_boot_variable(self, steps, device):

            with steps.start("Delete any configure boot variables") as step:

                try:
                    device.configure("no boot system")
                except Exception as e:
                    step.failed("Failed to delete configured boot variables",
                                from_exception=e)

                step.passed("Successfully deleted configured boot variables")

Passing Step Arguments
----------------------

To pass arguments to a clean step, add the arguments to the method and if there's a default, set it equal to that. Here's an example were we pass `images`, `timeout`, and `current_running_image`. You can see we provided the defaults by using:

`timeout=TIMEOUT` `current_running_image=CURRENT_RUNNING_IMAGE`

During runtime these values will be overwritten with user provided values (if provided). You can then use these arguments like you would in any other Python method.

.. code-block:: python
    :linenos:
    :emphasize-lines: 23, 25, 46-47

    import logging

    from genie.metaparser.util.schemaengine import Optional
    from genie.libs.clean import BaseStage

    log = logging.getLogger(__name__)

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