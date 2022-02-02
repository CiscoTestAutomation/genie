Schema and Arguments
====================

Develop a Schema
----------------

After defining the class in the correct file and inheriting the correct parent class the next step is to develop the schema. The schema of a stage defines what arguments the stage accepts, what arguments are optional or mandatory, and whether an argument is an integer or a string. It also defines the structure of arguments passed using the clean YAML file.

When writing a schema you want to think about how you can drive the stage by using arguments. In the following example of our ChangeBootVariable stage we specified these arguments in the schema:

* images: the image to use as the boot variable
* timeout: Execute timeout in seconds
* config_register: Value to set config-register for reload
* current_running_image: Flag to set the running image as the boot variable

.. code-block:: python
    :linenos:
    :emphasize-lines: 1, 10-13

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

        # ==============================
        # Execution order of Stage steps
        # ==============================
        exec_order = [

        ]

Set Default Values for Optional Arguments
-----------------------------------------

In most cases we want to provide a default value for optional arguments. In this case we will skip the `images` argument because it can be nothing if `current_running_image` is set to True.

Argument defaults should be the same name from the schema, UPPER CASE, and kept under the `Argument Defaults` section.

.. code-block:: python
    :linenos:
    :emphasize-lines: 19-21

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

In later sections you will discover how argument defaults are used.