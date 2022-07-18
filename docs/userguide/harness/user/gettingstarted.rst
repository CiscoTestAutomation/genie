.. _getting_genie:

Getting You Started
===================

This section provides an overview for users about how to begin using the ``Genie`` harness. 
We recommend reading this section in order, to help users understand the fundamental
building blocks to begin using ``Genie``.

.. note::

    The examples below are runnable. The only additional requirement is for users to have 
    a pyATS testbed file with at least one device.

Set-up
------

The first step is to create a job file for executing the ``Genie`` `harness`.

.. code-block:: python

    # Import Genie run
    from genie.harness.main import gRun


    def main():

        # Set job file path to current directory
        test_path = os.path.dirname(os.path.abspath(__file__))

        gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'))

A pyATS script is derived from the information provided to the Genie Harness
with `gRun`.

An example of the mapping datafile contains:

.. code-block:: yaml

    devices:
        PE1:
         context: cli
         label: uut
         mapping:
            cli: vty
            yang: netconf

The pyATS YAML :testbed:`testbed <http>` file describes the testbed topology and the testbed's devices.
Any given device in the testbed topology can be configured to support various connection types such
as: Console, Network Mangement VTY, NETCONF(YANG), and more in the future. 

Each of those connections names are not standardize, so ``Genie`` cannot know
which one to use for which context. The mapping file allows this mapping.  It
also allows to specify the context (cli, yang, etc) to be specified per device.
In the above example, we are mapping the `vty` connection to be used for `cli`, and
`netconf` connection for `yang`. The device name can either be the hostname of the device
defined in the testbed file,  or the device alias. They must be unique for each
device.

Available mapping are : `cli`, `yang`, `rest`. More will be added in the future.

As ``Genie`` is event driven, the triggers are performed on a given device,
which is known as the `uut` (Unit Under Test) for ``Genie``.   The `uut` is
identified via the `label` field. 

The `context` drives the management interface that will be used to connect to
devices during execution. 

To run the example above, create the `mapping.yaml` file in the same directory
as the job file. Copy the code from example above and modify it to fit the
requirement of your testbed, alias, and the context. 

.. note::

    In the mapping file, the key `cli` is mandatory and `yang` is optional.

.. note::

    To have standardized mapping files between users, the first key under
    devices can either be the device hostname or the device alias given in the
    testbed file.

We can now execute the example with the following command:

.. code-block:: bash

    easypy job.py -testbed_file <pyats testbed location>

This job does the following:

* Runs common setup
* Connects to a device
* Executes 'show running-config'
* No testcase to run yet
* Runs common cleanup
* Executes 'show running-config'

The first 'show' command in the `common setup` takes a snapshot of the
configuration. The second 'show' command in the `common cleanup` takes another
snapshot and compares them together to ensure the configuration remained the
same.

.. _harness_configuration:

Device Configuration
--------------------

Genie supports multiple ways to apply configuration on the devices.

  1) Manually applied on the devices before the run starts (Done by user)

The user can connect manually to the devices and apply any configuration wanted.

  2) Automatically applied on the devices in the Common Setup/Cleanup with Tftp/Ftp/Scp

With the `config_datafile` argument, a `config.yaml` is provided. This file
contains what configuration to apply on which device.

  3) Automatically applied on the devices in the Common Setup/Cleanup using Jinja2 rendering

Using the `jinja2_config` argument, the configuration will be rendered with the key/value pairs from
`jinja2_arguments`. The Unicon ``configure()`` service will be used to apply the configuration.
You can pass additional arguments to the configure service using the `configure_arguments`
key in the config section, e.g. you can enable bulk configure. The configuration is rendered
using the `load_jinja_template` device API.

.. code-block:: bash

    gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
         runtime=runtime, config_datafile=os.path.join('configs.yaml'))

The `configs.yaml` datafile lists all of the configurations files.

.. code-block:: yaml

    devices:
        uut:
            1:
              config: /path/to/my/configuration
              sleep: 3
              invalid: ['overlaps', '(.*inval.*)']
            2:
              config: <full path>
              sleep: 2
              invalid: ['some words']
            3:
              jinja2_config: routing.j2
              jinja2_arguments:
                lstrip_blocks: true
                trim_blocks: true
                bgp_data:
                    bgp_as: 100
                    neighbor_ips: [
                        '1.1.1.1', '2.2.2.2'
                    ]
              configure_arguments:
                bulk: True
                timeout: 180

.. important::

    The configuration is applied in the numerical sequence specified in the
    YAML file, (1,2,..), as shown above.

    Configurations are applied to devices in parallel using multiprocessing.

The configuration file is a typical `show running` style. After each
configuration applied, a wait period is recommended to allow the configuration
to stabilize; this is achieved with the key `sleep`, specified in seconds.

When applying configurations, we may see some error or warning messages which
may or may not be safe to ignore. Any error or warning patterns specified in
the `invalid` key will cause the `configure` subsection to fail if matched.
The `invalid` key supports regex.

A server must be added to copy the configuration on the devices, the
`file_transfer_protocol`_ sections explain what to add to the testbed datafile.

As an example, let's create a sample device configuration file, named
`uut_config1`.

.. code-block:: text

   interface Ethernet0/1
       no shutdown

   interface Ethernet0/2
       no switchport

And modify the previously created `configs.yaml` file as follows:

.. code-block:: python

    devices:
        uut:
            1:
              config: <full/path/to/uut_config1>
              sleep: 3

.. note::

    In case you need multiple configuration files, the number provide
    the sequence of the configuration.

.. note::

    The configuration section is optional, as it can be prefered to manually
    configured the devices before the run is started.


3) Custom subsection to apply configuration on the device in any way

The :ref:`subsections section <subsections>` explains how to add your own subsection and performs any
action.

.. _check_config:

check_config
------------

Once the devices are configured, ``Genie`` learns the configured
state of the topology via `check_config`. The `check_config` subsection runs twice: 
first, during the common setup and then, during common cleanup. 

In the common setup, `check_config` executes the `show running` command on all of the 
devices in the topology to create a snapshot of the configured state of the topology. 
If devices are specified in subsection yaml file, it will only perform check on these devices.
example on sepecifying device for check_config in subsection yaml file:

.. code-block:: yaml

    setup:
        sections:
          check_config:
            method: genie.harness.commons.check_config
            parameters: 
                devices:
                  uut: None


In the common cleanup, `check_config` executes the `show running` command on
all devices in the topology once again to create a second snapshot of the
configured state of the topology. Afterwards, it compares the two snapshots to
ensure that the configuration of the devices remained intact during the
execution of the job.

Certain values, such as uptime, age, etc., collected in the `check_config` snapshots can dynamically change
during the execution of the job. Users can add the `exclude_config_check` argument to the 
`configs.yaml` file to ignore comparisons of certain configurations. 
This argument accepts a `String` or `Regular expression` expression as an input and 
then skips comparison of any configuration matching the expression.

Let's see an example of how to add the `exclude_config_check` argument:

.. code-block:: python

        devices:
            uut:
                1:
                    config: <full path to config file>
                    sleep: 5
                    invalid : ['(.*ERROR.*)']
        exclude_config_check: ['(.*description.*)']


.. _PTS:

PTS
---

As a recap, in the previous two sections we connected to our devices and then applied
various configurations. We also confirmed that the configurations were applied
without error.

Once the devices contain configurations, ``Genie`` can learn the state
of the topology via `PTS`. A first round of `profile` snapshots of each feature
are taken during the `common setup` and then a second round of `profile`
snapshots are taken during the `common cleanup`. These snapshots are compared
to those saved in the common setup to confirm that operational states did not
change during the job's execution.

`PTS` learns the configurations applied to a device by creating ``Genie``
:ref:`Ops <ops_guide>` objects or parsed dictionary. These objects are
snapshots of the operational state of the devices in the topology. Multiple
commands (sent by cli/yang/xml) are executed to collect a feature's
state/operational information.

The user can specify which configured features ``Genie`` should learn
using the `pts_features` argument. Each learned feature will create a subsection
in the common setup with prefix `profile_\<feature_name\>`.

Let's add the `pts_features` argument to `gRun` in our job file:

.. code-block:: python

    gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
         runtime=runtime, config_datafile=os.path.join('configs.yaml'),
         pts_features=['ospf', 'hsrp', 'show ip ospf interface',
                      'show ip ospf interface vrf default'])

By default PTS will only run on the `uut`. It can be modified in the 
`pts_datafile.yaml` file that maps devices to the features listed in the
`pts_datafile` argument as shown below.

Please copy the following code into a new file called `pts_datafile.yaml`.

.. code-block:: yaml

    extends: "%CALLABLE{genie.libs.sdk.genie_yamls.datafile(pts)}"

    ospf:
        devices: ['uut', 'helper']
        exclude:
            - age
            - uptime

    hsrp:
        devices: ['uut', 'helper']
        devices_attributes:
            uut:
                exclude:
                    - next_hello_time
            helper:
                exclude:
                    - next_hello_time
        exclude:
            - date

.. note::

    Be sure to provide devices to each PTS that you would like to execute.
    If no devices are provided, PTS will not run

Certain values taken in the `profile` snapshot for each feature can dynamically
change during execution of the script, such as `uptime`, `age` etc. The user
can choose to exclude comparisons of these values by specifying them with the
`exclude` key, as shown above. Each value can be excluded at the device level
or the feature level.

Let's add the `pts_datafile` argument to `gRun` in our job file.

.. code-block:: python

        gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
             runtime=runtime, config_datafile=os.path.join('configs.yaml'),
             pts_features=['ospf', 'hsrp'],
             pts_datafile=os.path.join(test_path, 'pts_datafile'))

.. _Golden:

.. note::

    Show command does not need to be added to the PTS file to run. By default
    they will use the same exclude keys as their Verification datafile
    corespondance.

Golden Config
-------------

In the previous sections, we configured our devices and learned the state of the
topology. However, how can we be certain that the state of the topology is
precisely the one we expected?

The `pts_golden_config` compares the `profiles` learned by PTS
in the current run to a profile that has been verified to be
a `golden` snapshot by your team. After each run, a file named `pts` is
generated and saved to the `pyATS` archive directory. This file can then be
saved to a fixed location. This file can then be provided as an argument to the
job file via `pts_golden_config`  argument as shown below.

Let's add the `pts_golden_config` argument to `gRun` in our job file:

.. code-block:: python

        gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
             runtime=runtime, config_datafile=os.path.join('configs.yaml'),
             pts_features=['ospf', 'hsrp'],
             pts_datafile=os.path.join(test_path, 'pts_datafile'),
             pts_golden_config='<path>/golden_pts')

.. _getting_verification:

Verifications
-------------

A verification is the execution of a command to retrieve the current state of a
device. The state can be retrieved by using `cli`, `yang`, `xml` and so on or a
mix of them.

There are two types of verifications: `Global` and `Local`.

`Global` verifications are run immediately after the `common setup`. At this
stage, the information retrieved is saved as a snapshots.  After each subsequent
trigger, the same set of verifications are executed again and their state is
compared to the previous snapshot.

`Local` verifications are independent of the `Global` verifications. They are
run as subsections of a trigger. A first set of snapshots are taken before
performing the trigger action. A second set of snapshots are taken after the
trigger action and then compared to the first set of snapshots.

The `verification_datafile` specifies which verifications ``Genie`` should run.
Let's create a  `verification_datafile.`

.. code-block:: yaml

    extends: verifications.yaml

    Verify_Ospf:
        groups: ['L3']
        devices: ['uut']
        iteration:
            attempt: 3
            interval: 10
        exclude: ['uptime']
        processors:
            # verification with pre processor
            pre:
                extra_sleep:
                    pkg: genie.libs.sdk
                    method: libs.prepostprocessor.sleep_processor
            # verification with post processor
            post:
                extra_sleep:
                    pkg: genie.libs.sdk
                    method: libs.prepostprocessor.sleep_processor

.. note::

    Be sure to provide a device for each verification that you want to execute.
    If no device is specified, the verification will not run

.. note::

    ``Genie`` libs contains available ready to use processors, For more
    information on how to use them, go to
    :ref:`harness developer <verifications>`.


Certain values taken in the verification snapshot can dynamically change during
execution of the script, such as uptime, age etc. The user can choose to
`exclude` comparison of these values by specifying them with the `exclude` key
as shown in the example above.

At times, configurations on the device require some time to reach a stable
state.  The `iteration` key tells ``Genie`` to rerun the verification for the
number of `attempt` specified while waiting for  `interval` seconds between each
attempt.

.. note::

    Verification failure handling: Whenever a verifications fails due to mismatched
    key values when comparing snapshots, it will mark the section as a failure. At
    this stage, ``Genie`` saves this new snapshot as the `latest` snapshot
    containing the updated key values. It then uses this new snapshot to compare
    verifications snapshots generated after the failure. This reduces
    the number of failing verifications in a run.

The ``Genie`` `SDK` is a community driven library containing verifications
which can be used by ``Genie``.

Let's add the `verification_datafile` argument to `gRun` in our job file in
order to execute Global verifications:

.. code-block:: python

        gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
             runtime=runtime, config_datafile=os.path.join('configs.yaml'),
             pts_features=['ospf', 'hsrp'],
             pts_datafile=os.path.join(test_path, 'pts_datafile'),
             pts_golden_config='<path>/pts',
             verification_datafile=os.path.join(test_path, 'verification_datafile'))


.. note::

    More information on verification in the developer guide.

.. notes::

    ``Genie``'s infrastructure includes a set of verifications. These verifications are
    stored in the `extends` location.

..
  .. figure:: VerificationSDK.png
    :align: center
    :alt: They can talk

.. _getting_trigger:

Triggers
--------

A trigger is a set of actions and verifications that collectively constitute a
testcase. These actions can include removal/addition of configuration, flapping
protocols/interfaces, perform HA events, and any other actions that users may
want to apply to test their devices. Triggers can also include verifications that
check whether the above actions were performed correctly on the devices. We call these
triggers,  `local verifications`.

The `trigger_datafile` specifies which triggers ``Genie`` should run. Let's
create a  `trigger_datafile`:

.. code-block:: yaml

    extends: "%CALLABLE{genie.libs.sdk.genie_yamls.datafile(trigger)}"

    # Simple trigger which will run on the uut and part of the L3 group
    TriggerShutNoShutOspf:
        groups: ['L3']
        devices: ['uut']
        processors:
            # trigger with pre processor
            pre:
                extra_sleep:
                    pkg: genie.libs.sdk
                    method: libs.prepostprocessor.sleep_processor

    # A trigger with a local verification
    TriggerClearOspf:
        groups: ['L3']
        devices: ['uut']
        verifications:
          Verify_Ospf:
            devices: ['uut']
            devices_attributes:
              uut:
                iteration:
                  attempt: 6
                  interval: 10
            parameters:
                vrf: default
        processors:
            # trigger with post processor
            post:
                extra_sleep:
                    pkg: genie.libs.sdk
                    method: libs.prepostprocessor.sleep_processor
    order: ['TriggerClearOspf']

.. note::

    Be sure sure you specify a device for each trigger you would like to execute.
    If no device is specified, the trigger will not run

.. notes::

    The local verification name must match a verification which exists in the
    `verification_datafile`

.. notes::

    The local verification parameters defined here will overwrite existing
    parameter which exists in the `verification_datafile`

.. notes::

    The `order` key define the order of execution. If a trigger is not a part of
    the list, the trigger will still execute but in a arbitrary order as python
    dictionaries are unordered.

.. notes::

    ``Genie``'s infrastructure includes a set of triggers. These triggers are
    stored in the `extends` location.  For more information, please consult the
    :ref:`datafile page <datafile>`.

.. note::

    ``Genie`` libs contains available ready to use processors, For more
    information on how to use them, go to
    :ref:`harness developer <triggers>`.

The ``Genie`` `SDK` is a community driven library containing triggers which can
be used by ``Genie``.

Let's add the `trigger_datafile` argument to `gRun` in our job file.

.. code-block:: python

        gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
             runtime=runtime, config_datafile=os.path.join('configs.yaml'),
             pts_features=['ospf', 'hsrp'],
             pts_datafile=os.path.join(test_path, 'pts_datafile'),
             pts_golden_config='<path>/pts',
             verification_datafile=os.path.join(test_path, 'verification_datafile'),
             trigger_datafile=os.path.join(test_path, 'trigger_datafile'),
             trigger_uids=['TriggerShutNoShutOspf', 'TriggerClearOspf'])

..
  .. figure:: GenieTriggerSdk.png
    :align: center
    :alt: They can talk

.. _file_transfer_protocol:

File Transfer Protocol
----------------------

The file transfer protocol to be used during common setup copy configuration
section or during copy cores/crashdumps in later stages in the run can be set
by the user in the job file.

It is an optional argument, if user didn't provide it in the job file. The
protocol will be extracted from the testbed yaml file as shown below.

.. code-block:: yaml

    testbed:
      name: <testbed name>
      servers:
          <File Transfer Protocol>:
              address: <tftp server ip address>
              path: <tftpboot location>

The valid transfer protocols are 'tftp', 'ftp' and 'scp'.

Let's add the `filetransfer_protocol` argument to `gRun` in our job file:

.. code-block:: python

        gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
             runtime=runtime, config_datafile=os.path.join('configs.yaml'),
             pts_features=['ospf', 'hsrp'],
             pts_datafile=os.path.join(test_path, 'pts_datafile'),
             pts_golden_config='<path>/pts',
             filetransfer_protocol='tftp')

.. _harness_pool:

Connection Pool
---------------

Performance! Speed! With a connection pool commands on the same devices are not
send one after the other,  but in parallel!  User can provide `pool_size`
argument in the :ref:`Mapping datafile <mapping_datafile>` and will be able to start a pool of
connections during the genie script run.  Refer to pyATS
:connection-pool:`connection-pool <http>` for more details about connection
sharing.
