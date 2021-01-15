.. _clean_doc_glossary:

Glossary of pyATS Related Terms
===============================

This glossary provides an alphabetical list of Clean-specific terms, acronym expansions, and alternate term names
used the pyATS Clean documentation. Also refer to the following web resources for terms and acronyms not defined
in this glossary.

.. todo: link other docs

.. topic:: Cleaner

    A Clean class (referenced as `PyatsDeviceClean` in the Clean file) that inherits the BaseCleaner
    class from Kleenex. The Cleaner is responsible for loading the testbed devices and starting the clean testcase.

.. topic:: Clean YAML file

    The Clean YAML file (also truncated to just Clean File), is the YAML-based input file used by pyATS Clean that
    contains the details of how to prepare and clean the devices in your testbed such as Clean Stage tasks, schema
    requirements, and device recovery details.

    You can view many example pyATS Clean YAML files from the pyATS Clean repository on GitHub that meets most
    operational requirements for cleaning devices; or alternatively, you can easily create your own Clean YAML file
    to meet your specific needs.

.. topic:: Golden Configuration

    A Golden configuration file is used to specify how to configure the device with a good and stable configuration.
    This file specifies for instance, the device host name, the IP address to reach the TFTP (or FTP) file server,
    username, and password.

.. topic:: Golden Image

    A Golden Image is a known good/validated image (binary file) that is kept on a device.

.. topic:: Stage (pyATS Clean Stage)

    Stages are the building blocks to pyATS Clean. When grouped together, Clean Stages define the clean workflow and
    used to clean the devices in a testbed. A collection of steps contributes to a Clean stage.
