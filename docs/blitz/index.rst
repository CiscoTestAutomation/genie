.. _blitz:

pyATS Blitz
================

The *Blitz* is a YAML-driven template that makes it easy for you to run
a test case without having to know any knowledge of programming. This tool is called
*Blitz* because it's lightning fast --- does the following actions:

* Configure a device.
* Parse the device output to verify if the device state is as expected.
* Unconfig or modify the initial configuration.
* Learn a feature and verify the result of the action
* Calling different apis and use their outputs on other actions and other devices
* Yang integration
* It is fully customizable and new actions can be added
* Many more features that will be discussed thoroughly in the upcoming sections


To use the *Blitz*, add the `YAML` content to a
`trigger datafile <https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writetrigger/writetrigger.html#create-a-new-trigger-datafile>`_, or create a new yaml file if you dont have one. Using a `job <https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html>`__ file execute tests in the given order.

Each *trigger datafile* can contains of multiple testcases.

.. code-block:: YAML

    # Template of a blitz testcase
    # ----------------------------

    # Name of the testcase
    Testcase1:

        # Leave this as is for most use cases
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz

        # Field containing all the sections
        test_sections:

            # Section name - Can be any name, it will show as the first section
            # of the testcase
            - section_one:
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"

            - section_two:
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"
        ...


.. toctree::
    :hidden:
    :maxdepth: 4

    design/index
    usage/usage
