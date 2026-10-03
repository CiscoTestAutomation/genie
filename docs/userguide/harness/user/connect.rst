.. _connect:

Connect Functionality
====================

The ``connect`` subsection in the Genie harness is responsible for establishing connections to all devices defined in the mapping file during the common setup phase.

Overview
--------

The ``connect`` function is a critical component in the Genie harness that establishes connections to the devices in your testbed. It supports both parallel and sequential connection modes and includes retry capabilities for handling intermittent connection issues that often occur in testing environments.

Parameters
---------

The ``connect`` function accepts the following parameters:

.. list-table::
   :widths: 20 10 10 60
   :header-rows: 1

   * - Parameter
     - Type
     - Default
     - Description
   * - parallel
     - Boolean
     - True
     - When True, device connections are established in parallel; when False, connections are established sequentially
   * - retry
     - Boolean
     - False
     - When set to True, enables automatic retry of connection attempts
   * - retry_max_time
     - Integer
     - 300
     - Maximum time in seconds to attempt connection retries
   * - retry_interval
     - Integer
     - 30
     - Time interval in seconds between retry attempts

Usage
-----

In a subsection datafile:

.. code-block:: yaml

    setup:
        sections:
            connect:
                method: genie.harness.commons.connect
                parameters:
                    parallel: True
                    retry: True
                    retry_max_time: 300
                    retry_interval: 30

In Python code:

.. code-block:: python

    from genie.harness.commons import connect

    connect(self, testbed, steps, parallel=True, retry=True, 
            retry_max_time=300, retry_interval=30)

Connection Modes
---------------

Parallel Mode
~~~~~~~~~~~~

By default, the ``connect`` function attempts to establish connections to all devices in parallel, which reduces the overall time required to connect to multiple devices.

.. code-block:: python

    # Connect to devices in parallel (default behavior)
    connect(self, testbed, steps, parallel=True)

Sequential Mode
~~~~~~~~~~~~~

In some scenarios, you may need to connect to devices sequentially, especially when there are resource constraints or when troubleshooting connection issues:

.. code-block:: python

    # Connect to devices sequentially
    connect(self, testbed, steps, parallel=False)

Retry Functionality
-----------------

When retry is enabled:

1. If a connection attempt fails, the system will log a warning and wait for ``retry_interval`` seconds
2. The system will continue retrying until:
   
   * The connection succeeds, or
   * The total retry time exceeds ``retry_max_time``
   
3. If all retries fail, an appropriate error message is logged

Examples
-------

.. code-block:: python

    # Example 1: Default connection behavior (parallel, no retry)
    connect(self, testbed, steps)

    # Example 2: Enable retry with 5 minutes maximum retry time and 10 second intervals
    connect(self, testbed, steps, retry=True, retry_max_time=300, retry_interval=10)

    # Example 3: Sequential connections with retry enabled
    connect(self, testbed, steps, parallel=False, retry=True, retry_max_time=300, retry_interval=30)

Best Practices
-------------

- **Parallel vs. Sequential**: Use parallel mode (default) when connecting to multiple devices to save time. Use sequential mode when troubleshooting connection issues or when devices have resource constraints.

- **Retry Settings**: When working with unstable network environments, enable retry functionality with appropriate timeout values. For most cases, the default values (300 seconds max time, 30 seconds interval) are reasonable.

- **Error Handling**: Always check the connection status after the connect function completes, as some devices may still fail to connect despite retry attempts.
