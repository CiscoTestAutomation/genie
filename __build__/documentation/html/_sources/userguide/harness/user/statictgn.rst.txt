.. _statictgn:

Statictgn
=========

``Genie`` can connect to Ixia traffic generator devices that are running
IxNetwork API Server versions 7.40 or higher. Refer to the User Guide below for
detailed information on using ``Genie`` to control Ixia using a Cisco internal
TCL-based Ixia connection library called "PSAT"


System Requirements
-------------------

1. Ixia chassis - version 
2. IxNetwork API Server - version 7.40+ (standalone or within Ixia chassis)

.. note::

    For more information on IxNetwork API server versions, refer to
    :ixiasupport:`Ixia Available Versions Support<http>`


Ixia Libraries
^^^^^^^^^^^^^^

It is recommended to check the :ixiasupport:`Ixia Versions Support <http>` page
to download the Ixia libraries corresponding to the user's Ixia chassis and the
version of the IxNetwork API server application they are running.

For further information, please reach out to your Ixia representative.


Adding Ixia device
------------------

An Ixia traffic generator `device` can be specified in the ``testbed`` YAML file
as shown in the example below:

.. code-block:: yaml

    devices:
      IXIA:
        type: tgn
        os: 'statictgn'
        connections:
          tgn:
            class: genie.libs.conf.device.statictgn.connection.GenieTgn
            address: 172.25.195.91 8012
            controller: 172.27.101.96
            handle: 8012
            port_list: "9/6 9/7"
            tgn_type: IXIA
            session_up: False


It is mandatory to specify the connection class implementation information in
the testbed YAML file as shown in the example above.

OS `statictgn` uses a Cisco internal TCL-based Ixia connection library (PSAT):
`genie.libs.conf.device.statictgn.connection.GenieTgn`

.. tip::

    1. The `type` key must be set to "tgn".
    2. The `os` key specifies which OS implementation to use to connect to this
       device. Use "statictgn" for PSAT Ixia library.
    3. The `connections` key specifies the connection label.

The following are mandatory keys to be provided in the `testbed` YAML while
defining an Ixia `device`:

.. code-block:: text

    +--------------------------------------------------------------------------+
    | Ixia Testbed YAML Parameters                                             |
    +==========================================================================+
    | Argument                 | Description                                   |
    |--------------------------+-----------------------------------------------|
    | class                    | Connection class implementation information.  |
    |--------------------------+-----------------------------------------------|
    | address                  | IP address of server running IxNetwork EA     |
    |                          | App/GUI. Can be running within chassis or on  |
    |                          | standalone server.                            |
    |--------------------------+-----------------------------------------------|
    | controller               | IP address of Ixia chassis.                   |
    |--------------------------+-----------------------------------------------|
    | handle                   | TCL port of IxNetwork API server.             |
    |--------------------------+-----------------------------------------------|
    | port_list                | List of Ixia ports for testbed topology to be |
    |                          | used by Genie.                                |
    |--------------------------+-----------------------------------------------|
    | tgn_type                 | Specify to PSAT library the type of traffic   |
    |                          | generator used (Ixia/Spirent etc.)            |
    |--------------------------+-----------------------------------------------|
    | session_up               | Flag to set IxNetwork API server as previously|
    |                          | configured or not configured.                 |
    +==========================================================================+

.. note::

    If Ixia is not the preferred traffic generator, users can also write a new
    connection class implementation for their traffic generator device.


Connect to Ixia device
----------------------

After specifying the Ixia `device` in the `testbed` YAML file, we can connect to
the device using the `connect()` method:

.. code-block:: python

    # Load testbed containing Ixia traffic generator
    >> from genie.conf import Genie
    >> testbed = Genie.init('/path/to/testbed_with_tgn.yaml')

    # Specify the Ixia traffic generator
    >> tgn_device = testbed.devices['IXIA']

    # Connect to Ixia traffic generator


Traffic Generator Methods
-------------------------

The following table contains a list of methods available to the user to 
perform actions on the traffic generator device in ``Genie`` using statictgn
connection implementation.


.. code-block:: text    

    +--------------------------------------------------------------------------+
    | Traffic Generator Methods                                                |
    +==========================================================================+
    | Methods                   | Description                                  |
    |---------------------------+----------------------------------------------|
    | connect                   | Connects to the traffic generator device and |
    |                           | loads the specified configuration file.      |
    |---------------------------+----------------------------------------------|
    | learn_traffic_streams     | Learns the configuration of traffic streams  |
    |                           | configured on the device.                    |
    |---------------------------+----------------------------------------------|
    | start_routing             | Starts the routing engine on the device.     |
    |---------------------------+----------------------------------------------|
    | initialize_tgn_ArpNdPim   | Initializes ARP, ND and PIM on the device.   |
    |---------------------------+----------------------------------------------|
    | start_traffic             | Starts the traffic on the device.            |
    |---------------------------+----------------------------------------------|
    | stop_traffic              | Stops the traffic on the device.             |
    |---------------------------+----------------------------------------------|
    | get_current_packet_rate   | Get the current packet rate of all traffic   |
    |                           | streams configured on the device.            |
    |---------------------------+----------------------------------------------|
    | get_reference_packet_rate | Get the referemce packet rate of all traffic |
    |                           | streams configured on the device.            |
    |---------------------------+----------------------------------------------|
    | check_traffic_loss        | Check if any traffic loss has occurred on    |
    |                           | traffic streams configured on the device and |
    |                           | also verify traffic loss is within expected  |
    |                           | tolerance percentage.                        |
    |---------------------------+----------------------------------------------|
    | calculate_absolute_outage | Calculate the absolute traffic loss observed |
    |                           | on the device.                               |
    |---------------------------+----------------------------------------------|
    | poll_traffic_until_traffic| Keep polling for the traffic streams on the  |
    | _resumes                  |                                              |
    |                           | device to converge to steady state *AFTER*   |
    |                           | traffic loss is observed.                    |
    |---------------------------+----------------------------------------------|
    | clear_stats               | Clear all statistics on the device.          |
    |---------------------------+----------------------------------------------|
    | send_arp_on_interface     | Senf ARP to traffic generator device         |
    |                           | interfaces.                                  |
    +==========================================================================+


The methods listed above can be executed directly on an Ixia traffic generator
device from a Python prompt or within ``Genie`` and ``pyATS`` scripts.


Traffic Generator Usage
-----------------------

This sections covers sample usage of executing available Ixia traffic generator
methods (actions) mentioned in the previous section.

.. code-block:: python

    # Load the testbed
    >> from genie.conf import Genie
    >> testbed = Genie.init('/path/to/testbed_with_tgn.yaml')

    # Specify the Ixia device
    >> device = testbed.devices['IXIA']

    # Example1: Connect to the Ixia device
    >> device.tgn_skip_configuration = True
    >> device.connect(alias='tgn', via='tgn')

    # Example2: Connect to the device & load the configuration file
    >> device.tgn_skip_configuration = False
    >> device.connect(alias='tgn', via='tgn', config='/path/to/tgn1.ixncfg')

    # Start traffic on the device
    >> device.tgn.start_traffic()

    # Stop traffic on the device
    >> device.tgn.stop_traffic()

    # Clear stats on the device
    >> device.tgn.clear_stats()


Genie Traffic Subsections
-------------------------

``Genie`` bundles the different steps involved with Ixia setup and configuration
into controllable subsections that can be executed within ``Genie`` harness.

The harness provides the following subsections:
    1. common_setup: initialize_traffic
    2. common_clean: stop_traffic

To add/remove execution of the above mentioned subsections simply "enable" or
"disable" them by adding/removing the subsection name from the execution order
key, as shown below:

.. code-block:: yaml

    setup:
      sections:
        connect:
          method: genie.harness.commons.connect
        configure:
          method: genie.harness.commons.configure
        configuration_snapshot:
          method: genie.harness.commons.check_config
        save_bootvar:
          method: genie.libs.sdk.libs.abstracted_libs.subsection.save_bootvar
        learn_system_defaults:
          method: genie.libs.sdk.libs.abstracted_libs.subsection.learn_system_defaults
        initialize_traffic:
          method: genie.harness.commons.initialize_traffic
        profile_traffic:
          method: genie.harness.commons.profile_traffic

      order: ['connect', 'configure', initialize_traffic', 'profile_traffic']

    cleanup:
      sections:
        stop_traffic:
          method: genie.harness.commons.stop_traffic

      order: ['stop_traffic']


TCL Environment Settings for Traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cisco ATS TCL Tree
""""""""""""""""""

The current implementation of the ``Genie`` native traffic generator connection
class leverages several TCL based IXIA libraries. It is therefore required to
have a Cisco ATS TCL tree in order to use the TCL based IXIA libraries.

To install a new Cisco ATS TCL Tree please follow the steps listed
:ref:`here<atstcltree>`.

TCL Environment Variables
"""""""""""""""""""""""""

Once your ATS TCL tree has been successfully installed, or if you already have
an existing ATS TCL tree containing all the required TCL packages, please set
the following environment variables prior to executing your ``Genie`` run with a
traffic generator `device`:

.. code-block:: bash

    # For bash users

    source /path/to/ats/tcltree/env.sh
    export TCL_PKG_PREFER_LATEST=1
    export ENA_TESTS=$AUTOTEST/ena-tests
    export XBU_SHARED=$AUTOTEST/lib/xBU-shared
    export LD_LIBRARY_PATH=/auto/ttsw/ActiveTcl/8.4.19/lib:/usr/X11R6/lib

    # The following variable values are an example
    # These values will be different for each user's individual setup

    export IXIA_VERSION=8.10
    export IXIA_HOME=/auto/nostgAuto/ixia_upgrade/ixia_latest/hlapi/8.10.10.4/
    export IXIA_HLTAPI_LIBRARY=/auto/nostgAuto/ixia_upgrade/ixia_latest/hlapi/8.10.10.4/
    export TCLLIBPATH=/auto/nostgAuto/ixia_upgrade/ixia_latest/hlapi/8.10.10.4lib/

    # For csh users

    source /path/to/ats/tcltree/env.csh
    setenv TCL_PKG_PREFER_LATEST 1
    setenv ENA_TESTS $AUTOTEST/ena-tests
    setenv XBU_SHARED $AUTOTEST/lib/xBU-shared
    setenv LD_LIBRARY_PATH /auto/ttsw/ActiveTcl/8.4.19/lib:/usr/X11R6/lib

    # The following variable values are an example
    # These values will be different for each user's individual setup

    setenv IXIA_VERSION 8.10
    setenv IXIA_HOME /auto/nostgAuto/ixia_upgrade/ixia_latest/hlapi/8.10.10.4/
    setenv IXIA_HLTAPI_LIBRARY /auto/nostgAuto/ixia_upgrade/ixia_latest/hlapi/8.10.10.4/
    setenv TCLLIBPATH /auto/nostgAuto/ixia_upgrade/ixia_latest/hlapi/8.10.10.4lib/


The following is a summary of all the environment variables that need to be set
in order to use the ``Genie`` native traffic generator connection class
implementation:

.. code-block:: text

    +-------------------------------------------------------------------+
    | TCL Environment Variables                                         |
    +===================================================================+
    | Variable              | Description                               |
    |-----------------------+-------------------------------------------|
    | AUTOTEST              | Set by sourcing TCL ATS tree.             |
    | ATS_EASY              | Set by sourcing TCL ATS tree.             |
    | TCL_PKG_PREFER_LATEST | Should be set to 1 for latest TCL version.|
    | ENA_TESTS             | Location for TCL based traffic libraries. |
    | XBU_SHARED            | cAAs TCL libraries.                       |
    | LD_LIBRARY_PATH       | Mandatory LIB path.                       |
    | IXIA_VERSION          | IxNetwork version.                        |
    | IXIA_HOME             | Location for IXIA HLTAPI libraries.       |
    | IXIA_HLTAPI_LIBRARY   | Location for IXIA HLTAPI libraries.       |
    | TCLLIBPATH            | Location for IXIA HLTAPI "lib" folder.    |
    +===================================================================+

The IXIA specific environment variables mentioned above are always specific to
the user's IXIA chassis and the version of the IxNetwork application they are
running.

It is highly recommended to check if the environment variables have been
correctly set prior to executing a ``Genie``run. Do a quick check for each
environment variable as shown below:

.. code-block:: bash

    bash-4.1$ python
    >>> import os
    >>> os.environ['AUTOTEST']
    '/ws/tonystark-sjc/ats5.3.0'
    >>> os.environ['ENA_TESTS']
    '/ws/tonystark-sjc/ats5.3.0/ena-tests'


Genie Harness Traffic Generator Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below is a list of arguments that can be configured by the user to control
traffic generator subsections in ``Genie`` harness.

User's can specify arguments to control the ``Genie`` harness subsections via:

    1. Through gRun in the job file as shown below:

.. code-block:: python

    gRun(config_datafile=os.path.join(test_path, 'config_datafile.yaml'),
         tgn_enable=True,
         tgn_skip_configuration=True,
         tgn_traffic_loss_tolerance_percentage=15.0,
         )

    2. Through easypy in command line as shown below:

.. code-block:: bash

    easypy job.py --testbed-file <testbed yaml> \
                  --tgn_enable=True \
                  --tgn_skip_configuration=False \
                  --tgn_traffic_loss_tolerance_percentage=20.0


.. code-block:: text

    +--------------------------------------------------------------------------+
    | Genie Harness Traffic Generator Arguments                                |
    +==========================================================================+
    | Argument                              | Description                      |
    |---------------------------------------+----------------------------------|
    | tgn_enable                            | Enable execution of subsection   |
    |                                       | `initialize_traffic`.            |
    |---------------------------------------+----------------------------------|
    | tgn_skip_configuration                | Allows user to skip loading the  |
    |                                       | configuration on TGN if it has   |
    |                                       | been configured before Genie run.|
    |---------------------------------------+----------------------------------|
    | tgn_traffic_convergence_threshold     | Wait time (seconds) to allow     |
    |                                       | traffic streams to coverge       |
    |                                       | to steady state.                 |
    |---------------------------------------+----------------------------------|
    | tgn_reference_rate_threshold          | Wait time (seconds) before       |
    |                                       | checking traffic stream rates to |
    |---------------------------------------+----------------------------------|
    |                                       | create profile snapshot.         |
    | tgn_first_sample_threshold            | Wait time (seconds) before       |
    |                                       | collecting the first sample of   |
    |                                       | traffic stream rates.            |
    |---------------------------------------+----------------------------------|
    | tgn_disable_traffic_post_execution    | Allows user to stop traffic      |
    |                                       | **after** ``Genie`` has completed|
    |                                       | execution. This is useful for    |
    |                                       | manual debugging after Genie     |
    |                                       | runs complete.                   |
    |---------------------------------------+----------------------------------|
    | tgn_traffic_loss_recovery_threshold   | Wait time (seconds) for allowing |
    |                                       | traffic to recover to steady     |
    |                                       | state AFTER a traffic loss was   |
    |                                       | observed.                        |
    |---------------------------------------+----------------------------------|
    | tgn_traffic_loss_tolerance_percentage | Maximum allowable traffic loss   |
    |                                       | percentage during Genie run.     |
    |---------------------------------------+----------------------------------|
    | tgn_enable_traffic_loss_check         | Enable checking of traffic loss  |
    |                                       | after every trigger that is      |
    |                                       | executed by Genie.               |
    |---------------------------------------+----------------------------------|
    | tgn_config_post_device_config         | Configure TGN device ONLY AFTER  |
    |                                       | device configuration is          |
    |                                       | successfully applied.            |
    |---------------------------------------+----------------------------------|
    | tgn_profile_snapshot_threshold        | Wait time (seconds) to collect   |
    |                                       | reference rate while creating    |
    |                                       | traffic snapshot profile.        |
    |---------------------------------------+----------------------------------|
    | tgn_routing_threshold                 | Wait time (seconds) after        |
    |                                       | enabling TGN routing engine and  |
    |                                       | before starting traffic.         |
    |---------------------------------------+----------------------------------|
    | tgn_port_list                         | List of ports ``Genie`` should   |
    |                                       | connect to in `initialize_tgn`.  |
    |---------------------------------------+----------------------------------|
    | tgntcl_enable_arp                     | Send ARP to TGN device.          |
    |---------------------------------------+----------------------------------|
    | tgntcl_learn_after_n_samples          | Create traffic profile after     |
    |                                       | user specified (N) number of     |
    |                                       | samples.                         |
    |---------------------------------------+----------------------------------|
    | tgntcl_stream_sample_rate_percentage  | Specifies percentage tolerance   |
    |                                       | that two samples of the same     |
    |                                       | stream group must be within to   |
    |                                       | be considered "the same".        |
    |---------------------------------------+----------------------------------|
    | tgntcl_wait_multiplier                | Multiplier to increase the wait  |
    |                                       | time for creating a traffic      |
    |                                       | profile snapshot. This  argument |
    |                                       | multiples the value of argument  |
    |                                       | "tgn_profile_snapshot_threshold. |
    +==========================================================================+


common_setup: initialize_traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``Genie`` harness is capable of connecting to a traffic generator device and
loading a static configuration file onto the device. Additionally, it can
check that all configured traffic streams have traffic flowing successfully
with no packet loss and also creates a profile/snapshot of the configured
traffic streams after loading configuration.

``Genie`` harness packages all these functionalities within the
`initialize_traffic` subsection. It does the following steps in order:

    1. Connect to traffic generator device.
    2. Load the traffic generator device with the associated configuration file
       specified in the `configuration_datafile.yaml`.
    3. Learns all the traffic stream data configured on the device.
    4. Initializes the ARP, ND and PIM for the device (if needed).
    5. Starts the routing engine.
    6. Starts the traffic (sending packets).
    7. Verifies all traffic streams don't have traffic loss beyond specified
       threshold rate.
    8. Creates a profile snapshot of the traffic stream rates for reference.


common_cleanup: stop_traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the traffic is **not** stopped on the traffic generator `device`
after ``Genie`` execution completes. This is useful for manual debugging after
``Genie`` has completed execution and the user would like to log into the
traffic generator `device` to perform manual checks and/or actions.

However, if the argument `tgn_disable_traffic_post_execution` is set to True,
``Genie`` will stop the traffic in the common cleanup subsection `stop_traffic`.

If this flag is not set to True, ``Genie`` will skip execution of subsection
`stop_traffic` and allow the traffic to continue flowing on the traffic
generator `device` after ``Genie`` execution completes.


Genie Traffic Processors
------------------------

A :processors:`processor <http>` is a specific action that can be performed
before or after ``Genie`` triggers. Actions performed before a trigger are known
as "pre processors" and actions that are performed after a trigger are known as
"post processors".


``Genie`` provides processors that are useful for performing checks and/or
actions on a traffic generator `device` before or after executing triggers.


Enabling Processors
^^^^^^^^^^^^^^^^^^^

Enabling execution of ``Genie`` trigger processors can be specified in the
trigger YAML datafile in two ways - either as global processors or local
processors.


Global Processors
"""""""""""""""""

In order to run a processor before/after *all* triggers, user's can mark the
processor as a "global" processor.

This will ensure that the processor runs after every single trigger specified in
the `trigger_group` or `trigger_uids`. This prevents the user from having to
manually list all the processor to execute for each trigger in the
`trigger_datafile` YAML.

Global processors can be specified as follows in the `trigger_datafile` YAML:

.. code-block:: yaml

    global_processors:
      pre:
        clear_traffic_statistics:
          method: genie.harness.libs.prepostprocessor.clear_traffic_statistics
      post:
        check_traffic_loss:
          method: genie.harness.libs.prepostprocessor.check_traffic_loss


Local Processors
""""""""""""""""

In order to run a processor before/after *specific* triggers, users can mark the
processor as a "local" processor.

This will ensure that the processor runs after only the specific triggers that
have procesors listed for them.

Local processors can be specified as follows in the `trigger_datafile` YAML:

.. code-block:: yaml

    TriggerShutNoShutBgp:
      groups: ['bgp']
      processors:
        pre:
          clear_traffic_statistics:
            method: genie.harness.libs.prepostprocessor.clear_traffic_statistics
        post:
          check_traffic_loss:
            method: genie.harness.libs.prepostprocessor.check_traffic_loss
      devices: ['uut']


Disabling Processors
^^^^^^^^^^^^^^^^^^^^

Sometimes pre/post processors are specified as global processors, thereby
informing ``Genie`` harness to execute those processors for all triggers.


It would be tedious and time-consuming if a user wanted to disable a specific
global processor for 1 or a handful of triggers but execute them for all other
triggers. It would require the user to manually add local processors to every
trigger they want to execute.

Instead, users can simply set a trigger level argument `check_traffic` to
"False" to disable execution of any global pre/post traffic processors for that
trigger.

An example of disabling processor 'clear_traffic_statistics' after
TriggerClearBgp is shown below:


.. code-block:: yaml

    global_processors:
      pre:
        clear_traffic_statistics:
          method: genie.harness.libs.prepostprocessor.clear_traffic_statistics
      post:
        check_traffic_loss:
          method: genie.harness.libs.prepostprocessor.check_traffic_loss

    # Disable pre-processor `clear_traffic_statistics` for this trigger

    TriggerClearBgp:
      groups: ['bgp']
      check_traffic: False
      devices: ['uut']

In order to disable local processors, simply remove them from the trigger
definition within the `trigger_datafile` YAML.


processor: verify_traffic
"""""""""""""""""""""""""

`verify_traffic` is a ``Genie`` post-trigger processor that checks if traffic
loss was observed on a traffic generator `device` as a consquence of executing
the trigger. The user can set the amount of traffic loss to expect (in seconds)
after a trigger is executed, in the `trigger_datafile.yaml`.

If a configured traffic stream reports traffic loss beyond the expected amount,
``Genie`` marks the trigger as `failed`. ``Genie`` then polls for a user
specified amount of time until all configured traffic streams converge to a
steady state. Once a steady state has been reached, ``Genie`` then creates a new
snapshot to be used as a reference for comparison in subsequent triggers.

The `verify_traffic` post-trigger processor has the following arguments:

1. [mandatory] tgn_max_outage: Maximum allowed traffic outage (seconds)
2. [optional]  tgn_timeout: Time for traffic streams to converge to steady state
                              if traffic loss is expected (seconds)
3. [optional]  tgn_delay: Wait time when polling to check if traffic streams
                            have converged to steady state (seconds)

User's can set the arguments for the `verify_traffic` post-trigger processor at
the trigger level in the `trigger_datafile.yaml` as shown below:

.. code-block:: yaml

    TriggerShutNoShutBgp:
      tgn_max_outage: 120
      tgn_timeout: 300
      tgn_delay: 10
      devices: ['uut']


Processor: check_traffic_stats
""""""""""""""""""""""""""""""

`clear_traffic_stats` is a ``Genie`` pre-trigger processor that clears all
statistics on a traffic generator `device` before a trigger is executed.
