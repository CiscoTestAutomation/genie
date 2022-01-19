Stage Template
==============

In this section you can find the skeleton code that all clean stages will start from. The class inheritance differs slightly depending on if you are writing an entirely new stage or abstracting an existing stage.

* `Entirely New Stage`_
* `Abstract an Existing Stage`_

Entirely New Stage
------------------

For entirely new stages, write a new class that inherits the `BaseStage` class from `genie.libs.clean`. Choose a short name that describes what the stage does. Finally, the class must contain three main sections (including the comments in the below example): `Stage Schema`, `Argument Defaults`, and `Execution order of Stage steps`.

For ease, just copy/paste this example, and change the name of the class.

.. code-block:: python
    :linenos:

    from genie.libs.clean import BaseStage

    class ChangeBootVariable(BaseStage):

        # ============
        # Stage Schema
        # ============
        schema = {

        }

        # =================
        # Argument Defaults
        # =================

        # ==============================
        # Execution order of Stage steps
        # ==============================
        exec_order = [

        ]

Abstract an Existing Stage
--------------------------

Say we have a current implementation of ChangeBootVariable that is designated as an IOSXE stage an IOSXE cat9k device that the existing implementation doesn't work with. What we can do is write a new class and inherit the IOSXE one. This allows us to reuse the code that works and overwrite the code that doesn't.

For ease, just copy/paste this example, change the import, and change the name of the class.

.. code-block:: python
    :linenos:

    from genie.libs.clean.stages.iosxe.stages import ChangeBootVariable as ChangeBootVariableIosxe

    class ChangeBootVariable(ChangeBootVariableIosxe):

        # ============
        # Stage Schema
        # ============
        schema = {

        }

        # =================
        # Argument Defaults
        # =================

        # ==============================
        # Execution order of Stage steps
        # ==============================
        exec_order = [

        ]