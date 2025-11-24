device
======

The ``device`` command sets a specific device as the *active*
device from all devices loaded in the LAMP shell.

Overview
--------

The ``device`` command switches between multiple devices within
the LAMP shell environment. This command is essential for device
management because all operator commands (``execute``,
``configure``, etc.) operate only on the currently *active*
device.

Basic Usage
-----------

Switch the active device context with this command:

.. code-block:: console

   device <name>

The ``<name>`` parameter represents the device name specified in:

- Testbed YAML files when loaded via ``testbed load <file>``
- The name specified with ``-n`` flag in ``testbed add -n <name>`` or
  the hostname if the ``-n`` flag is not specified.

Active device indicator
^^^^^^^^^^^^^^^^^^^^^^^^

The LAMP shell prompt displays the currently active device using
the format ``(lamp-<name>)``. This visual indicator shows which
device is currently *active* in the shell.

Switching between devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of switching from device 'host1' to 'host2':

.. code-block:: console

   (lamp-host1) device host2
   (lamp-host2)

The prompt updates automatically to reflect the new *active* device.

.. note::

   When no devices are loaded, the shell prompt displays as
   ``(lamp)``. This indicates that no device is currently
   active. After loading devices in the shell, the prompt will
   update to indicate the *active* device.