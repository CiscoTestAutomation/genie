Creating New Clean Stages
=========================

New Clean Stages can be written and contributed to add functionality if pyATS Clean does not currently meet your cleaning
requirements.

.. topic:: The following steps outline how to create a new Clean Stage.

    #. `Determine what OS and Platform the new Clean Stage is designed for`_
    #. `Create a new python function inside the correct stages.py file`_
    #. `Adding stage arguments and schema`_
    #. `Add a docstring to the Clean Stage`_
    #. `Adding the python code the stage requires`_
    #. `Testing the new Stage`_
    #. `Contributing the new Stage into the repository`_

Determine what OS and Platform the new Clean Stage is designed for
------------------------------------------------------------------

Determine if the Clean Stage will work for all OSs and Platforms (therefore, would be designated as a ‘Common’ Clean
Stage vs. one written for a specific device type). This is required to determine what `stages.py` file the clean stage
would belong in.

* | Common Clean Stages reside in the `stages/stages.py` file.
  | For example, the Common Clean Stages belong `here <https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/clean-pkg/src/genie/libs/clean/stages/stages.py>`_.
* | OS-specific Clean Stages reside in the `stages/<os>/stages.py` file.
  | For example, the IOSXE specific Clean Stages belong `here <https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/clean-pkg/src/genie/libs/clean/stages/iosxe/stages.py>`_.
* | Platform-specific Clean Stages reside in the `stages/<os>/<platform>/stages.py` file.
  | For example, the IOSXE CAT9K Clean Stages belong `here <https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/clean-pkg/src/genie/libs/clean/stages/iosxe/cat9k/stages.py>`_.

Create a new python function inside the correct stages.py file
--------------------------------------------------------------

The function needs to be an `aetest.test` section. The required arguments for any Clean Stage is are `section`, `steps`,
and `device`.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,2

    @aetest.test
    def verify_running_image(section, steps, device):

Adding stage arguments and schema
---------------------------------

The schema defines what arguments the stage can accept and what format they follow. In this example we want to pass a
list of `images` to the stage.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1-3, 5

    @clean_schema({
        Optional('images'): list
    })
    @aetest.test
    def verify_running_image(section, steps, device, images):

Add a docstring to the Clean Stage
----------------------------------

The below code block is just an example however, the docstring should follow the same format.

.. code-block:: python
    :linenos:
    :emphasize-lines: 6-19

    @clean_schema({
        Optional('images'): list
    })
    @aetest.test
    def verify_running_image(section, steps, device, images):
        """ This stage verifies the currently running image is the expected image.

        Stage Schema
        ------------
        verify_running_image:
            images (list): Images that are expected to be running

        Example
        -------
        verify_running_image:
            images:
                - test_image.gbin

        """

Adding the python code the stage requires
-----------------------------------------

The below code block is just an example. The code is dependant on what the stage should accomplish.

.. code-block:: python
    :linenos:
    :emphasize-lines: 21-33

    @clean_schema({
        Optional('images'): list
    })
    @aetest.test
    def verify_running_image(section, steps, device, images):
        """ This stage verifies the currently running image is the expected image.

        Stage Schema
        ------------
        verify_running_image:
            images (list): Images that are expected to be running

        Example
        -------
        verify_running_image:
            images:
                - test_image.gbin

        """

        log.info("Section steps:\n1- Verify the running image on the device")

        # Verify running image on the device
        with steps.start("Verify running image on device {}".\
                         format(device.name)) as step:
            try:
                device.api.verify_current_image(images=images)
            except Exception as e:
                step.failed("Unable to verify running image on device {}\n{}".\
                               format(device.name, str(e)))
            else:
                section.passed("Successfully verified running image on device {}".\
                               format(device.name))

Testing the new Stage
---------------------

In order to test or even use the newly developed Clean Stage, it needs to be accessible to pyATS Clean. To do this you must
execute `make json` from the root folder of the cloned `genielibs` repository.

This command will update a json file that contains the information required for pyATS Clean to find clean stages.

After running the command, you can add the clean stage to your Clean YAML file and run it as normal.

Contributing the new Stage into the repository
----------------------------------------------

Once satisfied with the Clean Stage, you may commit your changes and open a pull request against the genielibs repository.
We will review the pull request and once satisfied we will merge the Clean Stage.

This stage will be available in the next official release.
