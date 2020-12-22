GenieTelemetry Guide
====================

In order to integrate ``GenieTelemetry`` with ``Genie``, User needs to follow
the below steps;

1. **GenieTelemetry config file**: ``GenieTelemetry`` needs a config file where
   the user specifies the following:

   a - `<plugin name>`: plugin name as created in the genietelemetry_libs

   b - `interval`: time interval for the plugin to run

   c - `module`: plugin location on genietelemetry_libs side

   d - `devices`: devices the plugin to run on
       (Optional, by default plugin will run on all devices in the testbed yaml
       file)

The supported schema is as following:

.. code-block:: yaml

    plugins:                # top level key for plugins

        HelloWorldPlugin:   # this is the plugin name we defined
                            # enabled, module and order keys are
                            # mandatory. Any additional key/values are
                            # used as arguments to the plugin class
                            # constructor.

          enabled: True           # flag marking it as "enabled"
                                  # set to False to disable a plugin

          module: module.where.plugin.is.defined      # module path where this
                                                      # plugin can be imported

          interval: 30              # defines the interval of execution of
                                    # plugins, in seconds only.
          devices: []               # device filter list: if not defined, the
                                    # plugin will be applied to all devices,
                                    # otherwise, only the included devices will
                                    # be applied.

.. code-block:: yaml

    # Example
    # -------
    #
    #   example genietelemetry configuration file for plugins

    plugins:
        crashdumps:
            interval: 30
            enabled: True
            module: genietelemetry_libs.plugins.crashdumps
            devices: ['R1','R2']
        tracebackcheck:
            interval: 30
            enabled: True
            module: genietelemetry_libs.plugins.tracebackcheck
            devices: ['R3']

2. **Call genie_telemetry**: an attribute 'genie_telemetry' controls the run of
   `GenieTelemetery` within the trigger, enabled by default (No need to pass it
   for every trigger unless needed to be disabled as illustrated below).

.. code-block:: yaml

    # Example
    # -------
    #
    #   In trigger data file

    global_processors:
      post:
        test_case_genie_telemetry:
          method: genie.harness.libs.prepostprocessor.genie_telemetry

    TriggerSleep:
        groups: []
        sleep_time: 5
        message_time: 1
        count: 1
        devices:
           uut: None

genie_telemetry argument can be passed to the trigger information to deactivate it

.. code-block:: python

    TriggerSleep:
        groups: []
        sleep_time: 5
        message_time: 1
        count: 1
        devices:
           uut: None
        genie_telemetry: False   < ----------- (False:Disable, True: Enable)

3. **Pass the built config file**: User needs to pass the built configuration
   file during the pyats run.

.. code-block:: yaml

    # Example
    # -------
    #
    #   When triggering pyats run

    pyats run <path>/job.py --testbed-file <path>/tb_file.yaml
    --genietelemetry <$VIRTUAL_ENV>/<path>/config.yaml

4. **Pass the GenieTelemetry arguments**: User needs to pass the arguments to
   perform different actions.

.. note::

  `GenieTelemetry` plugins are argument-driven user customized plugins.
  Plugin author defines the terminology of the plugin functionality and the
  corresponding arguments to drive that functionality.

.. code-block:: python

    # Example
    # -------
    #
    #   When triggering pyats run

    pyats run <path>/job.py --testbed-file <path>/tb_file.yaml
    --genietelemetry <$VIRTUAL_ENV>/<path>/config.yaml
    --crashdumps_upload True

Plugins arguments can also be passed in the plugin yaml file (Step 1).

.. code-block:: yaml

    plugins:
        crashdumps:
            interval: 30
            enabled: True
            module: genietelemetry_libs.plugins.crashdumps
            devices: ['R1','R2']
            plugin_arguments:
              crashdumps_upload: True

All `GenieTelemetry` arguments and details can be found in the :genietelemetry:`documentation <http>`.
