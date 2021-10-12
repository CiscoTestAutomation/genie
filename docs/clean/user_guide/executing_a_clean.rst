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
    * Can provide the image to a specific device, to all devices in a group, to all devices with a given OS, or all devices with a specific platform.
    * `--clean-device-image`, `--clean-os-image`, `--clean-group-image` and `--clean-platform-image` can all be specified simultaneously. Conflicts are resolved by `device > group > platform > os`.
    * Images specified with the CLI override images specified in the YAML file, i.e. `CLI device > CLI group > CLI platform > CLI os > YAML device > YAML group > YAML platform > YAML os`

    .. code-block:: bash

        # Example of passing an image to a device called 'PE1'
        pyats clean --clean-device-image PE1:</path/to/image.bin> --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

        # Example of passing an image to all devices with the 'nxos' os
        pyats clean --clean-os-image nxos:</path/to/image.bin> --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

        # Example of passing an image to all devices belonging to a group called 'group1'
        pyats clean --clean-group-image group1:</path/to/image.bin> --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

        # Example of passing an image to all devices with the 'n9k' platform
        pyats clean --clean-platform-image n9k:</path/to/image.bin> --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

    Image names can use Callable Markup which will be replaced by the return value of the callable

    .. code-block:: bash

        # Example of passing an image to a device called 'PE1' using a callable
        pyats clean --clean-device-image 'PE1:%CALLABLE{path.to.callable(args)}' --testbed-file </path/to/testbed.yaml> --clean-file </path/to/clean.yaml>

.. topic:: CLI image format

    * Single image

    .. code-block:: bash

        --clean-device-image PE1:/path/to/image.bin

    is equivalent to the following in Clean YAML:

    .. code-block:: yaml

        images:
        - /path/to/image.bin

    * URL image

    .. code-block:: bash

        --clean-device-image PE1:http://<url>:21/path/to/image.bin

    is equivalent to the following in Clean YAML:

    .. code-block:: yaml

        images:
        - http://<url>:21/path/to/image.bin

    * List of images

    .. code-block:: bash

        --clean-device-image PE1:/path/to/image.bin PE1:/path/to/optional_package1

    is equivalent to the following in Clean YAML:

    .. code-block:: yaml

        images:
        - /path/to/image.bin
        - /path/to/optional_package1

    * Key structure

    .. code-block:: bash

        --clean-device-image PE1:image:file:/path/to/image.bin PE1:packages:file:/path/to/optional_package1 PE1:packages:file:/path/to/optional_package2

    is equivalent to the following in Clean YAML:

    .. code-block:: yaml

        images:
          image:
            file:
            - /path/to/image.bin
          packages:
            file:
            - /path/to/optional_package1
            - /path/to/optional_package2


Clean Schema Validation
-----------------------

Validating your clean datafile is very useful when writing a new clean as it gives immediate feedback.

Run with this command::

    pyats validate clean --testbed-file /path/to/testbed.yaml --clean-file /path/to/clean.yaml
