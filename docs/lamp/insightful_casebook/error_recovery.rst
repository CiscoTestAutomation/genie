Error Recovery Techniques
==========================

Devices sometimes enter unexpected states—wrong modes, disconnections, or hung prompts. Rather than exiting LAMP
and losing your work, use built-in recovery techniques to get back to a working state quickly.

Recovering a Single Device
---------------------------

When a device becomes disconnected or enters an erroneous state, use the ``reconnect_device`` API:

.. code-block:: console

    (lamp) api reconnect_device

LAMP prompts you interactively for connection parameters:

.. code-block:: bash

    device: [<Device host1 at 0x7fd3f7f1ed60>]
    max_time(300):
    interval(30): 1
    sleep_disconnect(30): 1
    via(None):

**Key Parameters**

    - **max_time**: Maximum reconnection attempt duration in seconds (default: 300)
    - **interval**: Connection check frequency in seconds (default: 30)
    - **sleep_disconnect**: Wait time after disconnection (default: 30)

The API establishes a fresh connection to the device with your specified parameters.

Recovering an Entire Testbed
-----------------------------

When multiple devices are unresponsive, quickly restore by disconnecting and reloading:

.. code-block:: console

    (lamp) testbed remove -a
    (lamp) testbed load testbed.yaml

**If testbed was added dynamically (via 'testbed add')**

If the testbed was created dynamically using ``testbed add`` rather than loaded from a YAML file, save it first before reloading:

.. code-block:: console

    (lamp) testbed save tb.yaml
    (lamp) testbed remove -a
    (lamp) testbed load tb.yaml

This preserves your testbed configuration for future recovery operations.
