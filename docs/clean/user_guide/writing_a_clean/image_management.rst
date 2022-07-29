.. _clean_doc_image_management:

Image Management
================

pyATS Clean has a feature that can manage passing images between stages to help reduce the size and complexity of the
``Clean YAML``. Images can be defined in the ``Clean YAML`` or can be passed via command line arguments
(See :ref:`Passing images through CLI <clean_doc_image_cli>`).

To illustrate the difference, please see the ``Clean YAML`` below without using `Image Management`. The highlighted lines
are the lines that `Image Management` would automatically populate if used.

.. note::

    Some stage arguments may be missing in order to be brief. This is not a working example.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 11-12, 20, 26-27, 32-33

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1]

    devices:
        PE1:
            connect:

            copy_to_linux:
                origin:
                    files: /path/to/image.bin
                destination:
                    directory: /tftp-server
                    hostname: 127.0.0.1
                unique_number: 12345

            copy_to_device:
                origin:
                    files: /tftp-server/image_12345.bin
                    hostname: 127.0.0.1
                destination:
                    directory: 'bootflash:'

            change_boot_variable:
                images:
                - bootflash:/image_12345.bin

            reload:

            verify_running_image:
                images:
                - bootflash:/image_12345.bin

            order:
            - connect
            - copy_to_linux
            - copy_to_device
            - change_boot_variable
            - reload
            - verify_running_image

Now with `Image Management` used, see how the image only needs to be provided once, rather than in each stage that
requires it. pyATS Clean will pass the correct image value automatically between stages.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 9-10

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1]

    devices:
        PE1:

            images:
            - /path/to/image.bin

            connect:

            copy_to_linux:
                destination:
                    directory: /tftp-server
                    hostname: 127.0.0.1
                unique_number: 12345

            copy_to_device:
                origin:
                    hostname: 127.0.0.1
                destination:
                    directory: 'bootflash:'

            change_boot_variable:

            reload:

            verify_running_image:

            order:
            - connect
            - copy_to_linux
            - copy_to_device
            - change_boot_variable
            - reload
            - verify_running_image

Images key structure for Image Management
-----------------------------------------

Different platforms require different structures for the images key. See the below table to find the correct structure.
Some platforms may support multiple structure types.

.. list-table::
    :header-rows: 1

    * - os
      - platform
      - schema

    * - iosxe
      -
      - .. code-block:: yaml

            Structure #1
            ------------
            images:
            - /path/to/image.bin
            - /path/to/optional_package1
            - /path/to/optional_package2

            Structure #2
            ------------
            images:
              image:
              - /path/to/image.bin
              packages:   <<< optional
              - /path/to/optional_package1
              - /path/to/optional_package2

            Structure #3
            ------------
            images:
              image:
                file:
                - /path/to/image.bin
              packages:  <<< optional
                file:
                - /path/to/optional_package1
                - /path/to/optional_package2

    * - iosxr
      -
      - .. code-block:: yaml

            Structure #1
            ------------
            images:
            - /path/to/image.bin
            - /path/to/optional_package1
            - /path/to/optional_package2

            Structure #2
            ------------
            images:
              image:
              - /path/to/image.bin
              packages:   <<< optional
              - /path/to/optional_package1
              - /path/to/optional_package2

            Structure #3
            ------------
            images:
              image:
                file:
                - /path/to/image.bin
              packages:  <<< optional
                file:
                - /path/to/optional_package1
                - /path/to/optional_package2

    * - nxos
      - aci
      - .. code-block:: yaml

            Structure #1
            ------------
            images:
            - /path/to/switch_image.bin

            Structure #2
            ------------
            images:
              switch:
              - /path/to/switch_image.bin

            Structure #3
            ------------
            images:
              switch:
                file:
                - /path/to/switch_image.bin

    * - apic
      -
      - .. code-block:: yaml

            Structure #1
            ------------
            images:
            - /path/to/controller_image.bin
            - /path/to/switch_image.bin

            Structure #2
            ------------
            images:
              controller:
              - /path/to/controller_image.bin
              switch:
              - /path/to/switch_image.bin

            Structure #3
            ------------
            images:
              controller:
                file:
                - /path/to/controller_image.bin
              switch:
                file:
                - /path/to/switch_image.bin

    * - nxos
      - n3k
      - .. code-block:: yaml

            Structure #1
            ------------
            images:
            - /path/to/image.bin

            Structure #2
            ------------
            images:
              system:
              - /path/to/image.bin

            Structure #3
            ------------
            images:
              system:
                file:
                - /path/to/image.bin

    * - nxos
      - n9k
      - .. code-block:: yaml

            Structure #1
            ------------
            images:
            - /path/to/image.bin

            Structure #2
            ------------
            images:
              system:
              - /path/to/image.bin

            Structure #3
            ------------
            images:
              system:
                file:
                - /path/to/image.bin

    * - nxos
      - n7k
      - .. code-block:: yaml

            Structure #1
            ------------
            images:
            - /path/to/kickstart.bin
            - /path/to/system.bin

            Structure #2
            ------------
            images:
              kickstart:
              - /path/to/kickstart.bin
              system:
              - /path/to/system.bin

            Structure #3
            ------------
            images:
              kickstart:
                file:
                - /path/to/kickstart.bin
              system:
                file:
                - /path/to/system.bin


Images override behavior
------------------------

By default, the image(s) specified under a stage will be overridden by the image management service.

For `IOSXE`, this behavior can be modified with below configuration. This has not yet been implemented
for other operating systems such as NXOS or IOSXR.

This behavior can be changed by adding a configuration stage called `image_management` with setting
``override_stage_images`` set to ``False``. This overrides the default behavior and allows
stages to keep their image configuration as specified in the clean yaml file.

Example clean yaml file with default behavior.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 9, 13

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1]

    devices:
        PE1:
            images:
            - /path/to/image.bin

            change_boot_variable:
                images:
                - bootflash:/image_12345.bin


with the above configuration, the image specified on line 13, will be overridden by the value on line 9.

Example clean yaml with updated configuration setting.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 8-9, 16

    cleaners:
        PyatsDeviceClean:
            module: genie.libs.clean
            devices: [PE1]

    devices:
        PE1:
            image_management:
              override_stage_images: False

            images:
            - /path/to/image.bin

            change_boot_variable:
                images:
                - bootflash:/image_12345.bin

With the above configuration, the image specified on line 16 will be used as is.
