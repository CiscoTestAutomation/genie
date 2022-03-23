Run Stages Inside a Testscript
==============================

All genie device objects have a `<device_object>.api` attribute. This attribute traditionally allows access to any APIs defined in the `API Browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_.

The clean package extends upon it to add the `<device_object>.api.clean` sub-attribute. This new attribute allows quick access to any stage found in the `Clean Stages Browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean>`_ using the following syntax.

.. code-block::

    device.api.clean.<stage>(<stage_arguments>)

Example
-------

For this example the IOSXE implementation of the `install_image` stage will be used. Below is a snapshot of the docstring found in the `Clean Stages Browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean>`_. Any key/value pairs in the schema are the possible arguments to be passed.

.. code-block:: txt

    This stage installs a provided image onto the device using the install
    CLI. It also handles the automatic reloading of your device after the
    install is complete.

    Stage Schema
    ------------
    install_image:
        images (list): Image to install

        save_system_config (bool, optional): Whether or not to save the system
            config if it was modified. Defaults to False.

        install_timeout (int, optional): Maximum time in seconds to wait for install
            process to finish. Defaults to 500.

        reload_timeout (int, optional): Maximum time in seconds to wait for reload
            process to finish. Defaults to 800.

    Example
    -------
    install_image:
        images:
          - /auto/some-location/that-this/image/stay-isr-image.bin
        save_system_config: True
        install_timeout: 1000
        reload_timeout: 1000



Get the device object that the clean stage will run on. Call the stage using the following method while passing any arguments as needed: `<device_object>.api.clean.install_image`

.. code-block:: python
    :linenos:
    :emphasize-lines: 11-13

    from pyats import aetest

    class MyTestcase(aetest.Testcase):

        @aetest.test
        def my_test(self, steps, testbed):

            device = testbed.devices['uut']
            device.connect()

            device.api.clean.install_image(
                images=['bootflash:/image.bin'],
                save_system_config=True)

When running the script you will see the steps of the clean stage being logged to console.

.. code-block:: txt

    %EASYPY-INFO: Starting task execution: Task-1
    %EASYPY-INFO:     test harness = pyats.aetest
    %EASYPY-INFO:     testscript   = /Users/pyATS/testscript.py
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: |                           Starting testcase Test                           |
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: |                        Starting section my_section                         |
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: +..................................................+
    %AETEST-INFO: :    Starting STEP 1: Delete all boot variables    :
    %AETEST-INFO: +..................................................+

    (snip)

    %AETEST-INFO: +..........................................................................+
    %AETEST-INFO: :    Starting STEP 2: Configure system boot variable for 'install mode'    :
    %AETEST-INFO: +..........................................................................+

    (snip)

    %AETEST-INFO: +......................................................................+
    %AETEST-INFO: :    Starting STEP 3: Save the running config to the startup config    :
    %AETEST-INFO: +......................................................................+

    (snip)

    %AETEST-INFO: +............................................................................+
    %AETEST-INFO: :    Starting STEP 4: Verify next reload boot variables are correctly set    :
    %AETEST-INFO: +............................................................................+

    (snip)

    %AETEST-INFO: +................................................................+
    %AETEST-INFO: :    Starting STEP 5: Installing image 'bootflash:/image.bin'    :
    %AETEST-INFO: +................................................................+

    (snip)

    %AETEST-ERROR: Failed reason: Failed to install the image.
    %AETEST-INFO: The result of STEP 5: Installing image 'bootflash:/image.bin' is => FAILED
    %AETEST-INFO: The result of section my_section is => PASSED
    %AETEST-INFO: The result of testcase Test is => PASSED

    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: |                            Task Result Summary                             |
    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: Task-1: testscript.Test                                                 PASSED
    %EASYPY-INFO:
    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: |                            Task Result Details                             |
    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: Task-1: testscript
    %EASYPY-INFO: `-- Test                                                                PASSED
    %EASYPY-INFO:     `-- my_section                                                      PASSED

.. note::

    There are two **default but extremely important** behaviours to note:

        * Results from the stage do not roll-up to affect the testscript
        * The steps of the stage will not appear in the `Task Result Details`

    Both of these behaviours can be observed in the above snippet.

To enable this roll-up, pass the steps object which is automatically created by the pyATS infrastructure as shown below (nested steps also work).

.. code-block:: python
    :linenos:
    :emphasize-lines: 6,12

    from pyats import aetest

    class MyTestcase(aetest.Testcase):

        @aetest.test
        def my_test(self, steps, testbed):

            device = testbed.devices['uut']
            device.connect()

            device.api.clean.install_image(
                steps=steps
                images=['bootflash:/image.bin'],
                save_system_config=True)

Now the stage result will affect the testscript result. The steps will also appear in the `Task Result Details` section. Observe this new behaviour in the below snippet.

.. code-block:: txt

    %EASYPY-INFO: Starting task execution: Task-1
    %EASYPY-INFO:     test harness = pyats.aetest
    %EASYPY-INFO:     testscript   = /Users/pyATS/testscript.py
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: |                           Starting testcase Test                           |
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: |                        Starting section my_section                         |
    %AETEST-INFO: +----------------------------------------------------------------------------+
    %AETEST-INFO: +..................................................+
    %AETEST-INFO: :    Starting STEP 1: Delete all boot variables    :
    %AETEST-INFO: +..................................................+

    (snip)

    %AETEST-INFO: +..........................................................................+
    %AETEST-INFO: :    Starting STEP 2: Configure system boot variable for 'install mode'    :
    %AETEST-INFO: +..........................................................................+

    (snip)

    %AETEST-INFO: +......................................................................+
    %AETEST-INFO: :    Starting STEP 3: Save the running config to the startup config    :
    %AETEST-INFO: +......................................................................+

    (snip)

    %AETEST-INFO: +............................................................................+
    %AETEST-INFO: :    Starting STEP 4: Verify next reload boot variables are correctly set    :
    %AETEST-INFO: +............................................................................+

    (snip)

    %AETEST-INFO: +................................................................+
    %AETEST-INFO: :    Starting STEP 5: Installing image 'bootflash:/image.bin'    :
    %AETEST-INFO: +................................................................+

    (snip)

    %AETEST-ERROR: Failed reason: Failed to install the image.
    %AETEST-INFO: The result of STEP 5: Installing image 'bootflash:/image.bin' is => FAILED
    %AETEST-INFO: The result of section my_section is => FAILED
    %AETEST-INFO: The result of testcase Test is => FAILED

    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: |                            Task Result Summary                             |
    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: Task-1: testscript.Test                                                 FAILED
    %EASYPY-INFO:
    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: |                            Task Result Details                             |
    %EASYPY-INFO: +----------------------------------------------------------------------------+
    %EASYPY-INFO: Task-1: testscript
    %EASYPY-INFO: `-- Test                                                                FAILED
    %EASYPY-INFO:     `-- my_section                                                      FAILED
    %EASYPY-INFO:         `-- STEP 1: Delete all boot variables                           PASSED
    %EASYPY-INFO:         `-- STEP 2: Configure system boot variable for 'install  ...    PASSED
    %EASYPY-INFO:         `-- STEP 3: Save the running config to the startup conf  ...    PASSED
    %EASYPY-INFO:         `-- STEP 4: Verify next reload boot variables are correc ...    PASSED
    %EASYPY-INFO:         `-- STEP 5: Installing image 'bootflash:/image.bin'             FAILED