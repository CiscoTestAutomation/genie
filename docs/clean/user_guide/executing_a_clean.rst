.. _clean_doc_usage_and_args:
Executing a Clean
=================

This page contains the basic arguments required to use pyATS Clean. There are two different methods of using pyATS Clean
– Integrated or Standalone.

Prerequisites
-------------

To use pyATS clean with either method, the following is required:

* Testbed YAML file
* Clean YAML file

Running before a pyATS Script
-----------------------------

Running before a pyATS script is designed to make sure the device is in a good state, has the correct image, and the
expected configuration.

Run with this command::

    pyats run job </path/to/job.py> --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml> --invoke-clean

.. _clean_doc_standalone:

Running without a pyATS Script
------------------------------

Running without a pyATS script is designed to only clean the device; there isn't a need to run a pyATS Script after.

Run with this command::

    pyats clean --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

Passing images through CLI
--------------------------

.. topic:: Providing the images through CLI arguments

    * Can provide a new image at every run without modifying the Clean YAML file.
    * Can provide the image to a specific device or all devices with a specific platform.

    .. code-block:: bash

        # Example of passing an image to a device called 'PE1'
        pyats clean --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml> --clean-image PE1:</path/to/image.bin>

        # Example of passing an image to all devices with the 'n9k' platform
        pyats clean --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml> --clean-platform n9k:</path/to/image.bin>


Clean Schema Validation
-----------------------

Validating your clean datafile is very useful when writing a new clean as it gives immediate feedback.

Run with this command::

    pyats validate clean --testbed-file /path/to/testbed.yaml --clean-file /path/to/clean.yaml

