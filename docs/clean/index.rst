Introduction to pyATS Clean
===========================

.. toctree::
    :hidden:

    features
    supported_os_platform
    user_guide/index
    developer_guide/index
    Glossary <glossary>
    support

This topic provides a high-level overview of pyATS Clean framework driven by a YAML file with its flow defined by the
stages (steps) which are the building blocks of the clean process specific to device OS/Platform.

.. note::

    In the event you encounter terms or acronyms in this document you are unfamiliar with, there is a specialized
    :ref:`Clean-specific terms and acronym glossary <clean_doc_glossary>` to assist you.

What is a clean?
----------------
Clean is an operation to initialize a device with a specific software image and/or configuration regardless
of what was initially installed or in what state the device is in.

Do I need a clean?
------------------
Yes! Clean operations are required in number of different scenarios:

* In Automated regression/sanity testing for loading new software images for testing
* To recover devices and bring back to operational state from bad state.
* To re-initialize the configuration of a device to its base config, or to simply clean all unwanted files on the devices
* To re-initialize the device or bring up the device with new image

Why pyATS Clean?
----------------------------
pyATS Clean provides the framework and base libraries(Stages) to support device clean flow and requirement. Stages are
the main building blocks, they define the clean workflow and provide runtime control. pyATS Clean utilizes unicon as
the device connection library in the backend.

pyATS Clean is designed in a modular stage-based architecture driven by a YAML file. The end goal is to allow you 
to divide clean workflow into smaller stages which will help in debugging failures and have better control of runtime and
the flow requirement specific to device OS/Platform.

.. topic:: pyATS Clean framework provides:

    * Set of steps/stages and API which will be used in developing clean for different platforms
    * Set of commonly used utilities across platforms
    * Template and examples to define clean flow for a new platforms
    * CLI and APIs to execute clean and control the runtime environment

The modular architecture of stage-based design in pyATS clean allows easy customization of the clean by 
modifying the Clean YAML files suit your applications.

.. topic:: Here are a few clean scenarios:

    * Loading new image & applying new configuration on the device(s)
    * Write erase & reload the device
    * Verify connectivity to a specific server before executing the script
    * To recover a device when it in a bad state.
    * To purge any dangling or unwanted configurations on the device and bring device back to an operational state with a base configuration.
    * From a Sanity/Regression script execution point of view; it is mandatory to clean the device(s) before execution; as
      the state of the device is unknown. A purged device with a specific configuration and a specific image must be used as starting point.

To get started with pyATS Clean, many examples can be found at the `pyATS Clean example repository on GitHub
<https://github.com/CiscoTestAutomation/examples/tree/master/clean>`_. These examples are typical of most user’s
operational requirements and can be used as a base template for you to customize the clean flow based on your
platform need. You can easily create your own customized Clean YAML files and Clean Stages.

Refer to the existing pool of ready-to-use stages at `Clean Stage Browser <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean>`_.
