.. _clean_doc_usage_and_args:
Executing a Clean
=================

This page contains the information required to execute pyATS Clean and its available arguments. There are two different
methods of using pyATS Clean – Integrated or Standalone.

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

.. _clean_doc_image_cli:

Passing images through CLI
--------------------------

.. topic:: Providing the images through CLI arguments

    * Can provide a new image at every run without modifying the Clean YAML file.
    * Can provide the image to a specific device or all devices with a specific platform.

    .. code-block:: bash

        # Example of passing an image to a device called 'PE1'
        pyats clean --clean-image PE1:</path/to/image.bin> --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

        # Example of passing an image to all devices with the 'nxos' os
        pyats clean --clean-platform nxos:</path/to/image.bin> --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>#

        # Example of passing an image and packages
        pyats clean --clean-image R1:image:</path/to/image.bin> --clean-image R1:packages:/path/to/package1 --clean-image R1:packages:/path/to/package2 --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

    Both of these methods can be used with the Callable Markup which will be replaced by the return value of the callable

    .. code-block:: bash

        # Example of passing an image to a device called 'PE1' using a callable
        pyats clean --clean-image 'PE1:%CALLABLE{path.to.callable(args)}' --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

        # Example of passing an image to all devices with the 'nxos' os using a callable
        pyats clean --clean-platform 'nxos:%CALLABLE{path.to.callable(args)}' --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

Clean Schema Validation
-----------------------

Validating your clean datafile is very useful when writing a new clean as it gives immediate feedback.

Run with this command::

    pyats validate clean --testbed-file /path/to/testbed.yaml --clean-file /path/to/clean.yaml

