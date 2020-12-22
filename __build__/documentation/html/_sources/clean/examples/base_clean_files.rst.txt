.. _base_clean_files:

Base Clean Files
================

Provided on the page are Base clean files for different
scenarios that can be used and modified.

Now that we know the basics, below are some base clean files that can be
used and modified to your specifications. They are meant as the base
building block.

--------

Sanity
------
The `Sanity` base clean file will:

#. Connect to the devices
#. Copy image onto the device
#. Set the boot variables to the new image
#. Erase the NVRAM
#. Reload the device
#. Apply provided configuration
#. Verify the running image

All these steps are done in parallel.

.. note::

    Users will have to replace '<device>' and '<image>' with their own information

.. code-block:: yaml

    cleaners:
      DeviceClean:
        module: genie.libs.clean
        devices: [<device>]

    devices:
      <device>:
        images:
          - <image>
          # Example:
          # - /auto/my_image.bin

        device_recovery:
          break_count: 5
          console_activity_pattern: "\\.\\.\\.\\."
          timeout: 600
          recovery_password: <pass>
          golden_image:
            - bootflash:/golden_image.bin

        connect:

        copy_to_linux:
          destination:
            directory: /home/temp/images

        copy_to_device:
          origin:
            hostname: tftp
          destination:
            directory: 'flash:/'
          vrf: Mgmt-vrf
          protocol: tftp
          check_file_stability: True
          min_free_space_percent: 50
          overwrite: True

        change_boot_variable:

        write_erase:

        reload:

        apply_configuration:
          configuration: |
            hostname router1

        verify_running_image:

        order:
          - 'connect'
          - 'copy_to_device'
          - 'change_boot_variable'
          - 'write_erase'
          - 'reload'
          - 'apply_configuration'
          - 'verify_running_image'

--------

Developer
---------
The `Developer` base clean file will:

#. Connect to the device
#. Copy an image to the device
#. Set the boot variables to the new image
#. Reload the device
#. Verify the running image

.. note::

    Users will have to replace '<device>' and '<image>' with their own information

.. code-block:: yaml

    cleaners:
      DeviceClean:
        module: genie.libs.clean
        devices: [<device>]

    devices:
      <device>:
        images:
          - <image>
          # Example:
          # - /auto/my_image.bin

        connect:

        copy_to_device:
          origin:
            hostname: tftp
          destination:
            directory: 'flash:/'
          vrf: Mgmt-vrf
          protocol: tftp
          check_file_stability: True
          min_free_space_percent: 50
          overwrite: True

        change_boot_variable:

        reload:

        verify_running_image:

        order:
          - 'connect'
          - 'copy_to_device'
          - 'change_boot_variable'
          - 'reload'
          - 'verify_running_image'

--------

External User
-------------
The `External User` base clean file will:

#. Connect to the device
#. Erase the NVRAM
#. Apply provided configuration

.. note::

    Users will have to replace '<device>' and '<image>' with their own information

.. code-block:: yaml

    cleaners:
      DeviceClean:
        module: genie.libs.clean
        devices: [<device>]

    devices:
      <device>:
        images:
          - <image>
          # Example:
          # - /auto/my_image.bin

        connect:

        write_erase:

        apply_configuration:
          configuration: |
            hostname router1

        order:
          - 'connect'
          - 'write_erase'
          - 'apply_configuration'
