.. _datafile:

Datafiles
=========

This section provides the users with the schema for each datafile. For
additional information about how to use the datafiles described in this page,
please refer to the :ref:`getting started guide <getting_genie>`.

.. note::

    The format for the regex keys is as follows:
    `(<some regex>)`
    For example: `(.*upti.*)`
    would match any sentence which has `upti` inside it.

.. _markup_datafile:

Markup in Datafiles
-------------------

For every datafile below you can use the markup syntax as seen
`here <https://pubhub.devnetcloud.com/media/pyats/docs/topology/creation.html#testbed-file-markups>`_
to allow variable substitution and references similar to the Django template language.

.. note::

    Your testbed datafile values are available using this syntax:
    `%{testbed.<path>.<path>}`

.. _verification_datafile:

Verification Datafile
---------------------

.. code-block:: yaml

    # Verification Datafile schema
    # ----------------------------
    #
    # Production schema with commentary from the devs

    extends: # Use this field to extend an existing yaml Verification file,
             # allowing you to create an inheritance hierarchy.
             # Supports full path/names or name of file in the same dir.
             # ``Genie`` provides a Master set of verifications for you to
             # extend from as a start. It is found at:
             # <$virtual_env>/lib/python3.4/site-packages/genie/infra/verifications.yaml

    variables: # Use this field to store any information as dict to be shared
               # within this datafile
               # Can be retrieved : %{variables.<field>}

    parameters: # same purpose with variables
                # Can be retrieved : %{parameters.<field>}

    uids:    # Mention which verifications to execute

    groups:  # Mention which verification group to execute

    <verification name>: # Verification name goes here

        source: # This section is used to let
                # Genie know where the verification class
                # is located.

            pkg: # Abstraction package.
                 # (Optional if no abstraction)
                 # (Example: genie_libs)

            class: # Location of the class that contains the verification.
                   # (Example: ops.ospf.ospf.Ospf)

        processors: # This section is used to let
                    # Genie know where the pyATS processors are located

            pre: # pre processors
                 # (Optional if no pre processors)
                 # Accepts a list of pre-processors
                 # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                 # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

            post: # post processors
                  # (Optional if no post processors)
                  # Accepts a list of post processors
                  # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                  # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

            exception: # exception processors
                       # (Optional if no exception processors)
                       # Accepts a list of exception processors
                       # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                       # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

        groups: # Execution group for this verification.
                # (Optional)

        count: # How many times to execute this verification.
               # (Default: 1)
               # (Optional)

        exclude: # Attributes to be ignored.
                 # (Optional)
                 # (Supports regex)

        iteration: # Tells Genie to rerun the verification in case
                   # the result is not valid.
                   # (Optional)

            attempt: # Number of iteration attempts.
                     # (Optional)
                     # (Default: 1)

            interval: # How long to sleep between rerun, in seconds.
                      # (Optional)
                      # (Default: 0)

        devices: # Devices list to execute the verification.
                 # Can either be an alias or device hostname
                 # as defined in the pyats testbed file.
                 # If there is no device, the verification will not execute.

        devices_attributes: # attributes for the devices
                            # (Optional)

            <device name>: # Name of the device; must be same as devices list

                iteration: # Tells Genie to rerun the verification in case
                           # the result is not valid.
                           # (Optional)

                    attempt: # Number of iteration attempts.
                             # (Optional)
                             # (Default: 1)

                    interval: # How long to sleep between rerun, in seconds.
                              # (Optional)
                              # (Default: 0)

              # Any extra key will be passed as a parameters to the verification
              <key>: <value>

        parameters: # (Optional if no parser parameters)
                    # Any key will be passed as a parser parameters
            <key>: <value>

        # Any extra key will be passed as a parameters to the verification
        <key>: <value>

    global_processors: # Section to let Genie where the pyATS processors is located
                       # These processors will run for all verifications
          pre: # pre processors
               # (Optional if no pre processors)
               # Accepts a list of pre-processors
               # (Example: [sdk.libs.prepostprocessor.sleep_processor])
               # or use abstraction and define optional parameters
              <processor name>: # Processor name goes here

                  pkg: # Abstraction package
                       # (Example: genie_libs)

                  method: # Location of the processor method
                          # (Example: sdk.libs.prepostprocessor.sleep_processor)

                  parameters: # (Optional if no parameters)
                              # Any key will be passed as a parameters
                              <key>: <value>

          post: # post processors
                # (Optional if no post processors)
                # Accepts a list of post processors
                # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                # or use abstraction and define optional parameters
              <processor name>: # Processor name goes here

                  pkg: # Abstraction package
                       # (Example: genie_libs)

                  method: # Location of the processor method
                          # (Example: sdk.libs.prepostprocessor.sleep_processor)

                  parameters: # (Optional if no parameters)
                              # Any key will be passed as a parameters
                              <key>: <value>

          exception: # exception processors
                     # (Optional if no exception processors)

                     # Accepts a list of exception processors
                     # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                     # or use abstraction and define optional parameters
              <processor name>: # Processor name goes here

                  pkg: # Abstraction package
                       # (Example: genie_libs)

                  method: # Location of the processor method
                          # (Example: sdk.libs.prepostprocessor.sleep_processor)

                  parameters: # (Optional if no parameters)
                              # Any key will be passed as a parameters
                              <key>: <value>

.. _trigger_datafile:

Trigger Datafile
----------------

.. code-block:: yaml

    # Trigger Datafile schema
    # -----------------------
    #
    # Production schema with commentary from the devs

    extends: # Use this field to extend an existing yaml Trigger file,
             # allowing you to create an inheritance hierarchy.
             # Supports full path/names or names of file in the the same dir.
             # ``Genie`` provides a master set of triggers for you to extend
             # from as a start. It is found at:
             # <$virtual_env>/lib/python3.4/site-packages/genie/infra/triggers.yaml

    variables: # Use this field to store any information as dict to be shared
               # within this datafile
               # Can be retrieved : %{variables.<field>}

    parameters: # same purpose with variables
                # Can be retrieved : %{parameters.<field>}

    uids:    # Mention which triggers to execute

    groups:  # Mention which trigger group to execute

    <trigger name>: &trigger_arguments # Trigger name goes here

        source: # This section is used to let
                # Genie know where the trigger class
                # is located.

            pkg: # Abstraction package.
                 # (optional if no abstraction)
                 # (Example: genie_libs)

            class: # Location of the class that contains the trigger.
                   # (Example: sdk.triggers.shutnoshut.shutnoshut.TriggerShutNoShutOspf)

        timeout: # (Optional) This section is used for timeout of trigger
            max_time: # (Optional) Maximum wait time for the trigger. in second.
            interval: # (Optional) Wait time between iteration when looping is needed. in second.

        processors: # This section is used to let
                    # Genie know where the pyATS processors is located

            pre: # pre processors
                 # (Optional if no pre processors)
                 # Accepts a list of pre-processors
                 # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                 # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

                order: # accepts a list of processors
                       # (Optional if no special ordering expected)
                       # This list will decide the execution order of processors
                       # any processors not defined here will be excluded

            post: # post processors
                  # (Optional if no post processors)
                  # Accepts a list of post processors
                  # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                  # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

                order: # accepts a list of processors
                       # (Optional if no special ordering expected)
                       # This list will decide the execution order of processors
                       # any processors not defined here will be excluded

            exception: # exception processors
                       # (Optional if no exception processors)

                       # Accepts a list of exception processors
                       # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                       # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

                order: # accepts a list of processors
                       # (Optional if no special ordering expected)
                       # This list will decide the execution order of processors
                       # any processors not defined here will be excluded

        groups: # Execution group for this trigger.
                # (Optional)

        count: # How many times to execute this trigger.
               # (Default: 1)
               # (Optional)

        devices: # Devices lists to execute the verification.
                 # Can either be an alias or device hostname
                 # as defined in the pyats testbed file.
                 # If there is no device, the verification will not execute.

        devices_attributes: # attributes for the devices
                            # (Optional)

            <device name>: # Name of the device; must be same as devices list

                # Any extra key will be passed as a parameter to the verification
                <key>: <value>

        verifications: # Local verification to execute

            <verification name>: # Verification name
                                 # It must match one of the names of a
                                 # existing verification in
                                 # the verification_datafile.

                devices: # Devices lists to execute the verification.
                         # Can either be an alias or device hostname
                         # as defined in the pyats testbed file.
                         # If there is no device, the verification will not execute.

                devices_attributes: # attributes for the devices
                                    # (Optional)

                  <device name>: # Name of the device; must be same as devices list

                      iteration: # Tells Genie to rerun the verification in case
                                 # the result is not valid.
                                 # (Optional)

                          attempt: # How many times to rerun.
                                   # (Optional)
                                   # (Default: 1)

                          interval: # How long to sleep between rerun, in seconds.
                                    # (Optional)
                                    # (Default: 0)

                iteration: # Tells Genie to rerun the verification in case
                           # the result is not valid.
                           # (Optional)

                    attempt: # How many times to rerun.
                             # (Optional)
                             # (Default: 1)

                    interval: # How long to sleep between rerun, in seconds.
                              # (Optional)
                              # (Default: 0)

                parameters: # (Optional if no parser parameters)
                            # Any key will be passed as a parser parameters
                    <key>: <value>

        sections: # Adding processor to some Trigger section
            <section name>: # Name of the section to add processor to

                parameters: # Optional
                    <key>: <value>  # Adding in the parameters key along with
                                    # key/values will allow you to pass in arguments
                                    # on a per-section basis. Arguments defined in
                                    # the main body of the trigger will be overridden
                                    # by these arguments

                processors: # This section is used to let
                            # Genie know where the pyATS processors is located

                    pre: # pre processors
                         # (Optional if no pre processors)
                         # Accepts a list of pre-processors
                         # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                         # or use abstraction and define optional parameters
                        <processor name>: # Processor name goes here

                            pkg: # Abstraction package
                                 # (Example: genie_libs)

                            method: # Location of the processor method
                                    # (Example: sdk.libs.prepostprocessor.sleep_processor)

                            parameters: # (Optional if no parameters)
                                        # Any key will be passed as a parameters
                                        <key>: <value>

                    post: # post processors
                          # (Optional if no post processors)
                          # Accepts a list of post processors
                          # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                          # or use abstraction and define optional parameters
                        <processor name>: # Processor name goes here

                            pkg: # Abstraction package
                                 # (Example: genie_libs)

                            method: # Location of the processor method
                                    # (Example: sdk.libs.prepostprocessor.sleep_processor)

                            parameters: # (Optional if no parameters)
                                        # Any key will be passed as a parameters
                                        <key>: <value>

                    exception: # exception processors
                               # (Optional if no exception processors)

                               # Accepts a list of exception processors
                               # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                               # or use abstraction and define optional parameters
                        <processor name>: # Processor name goes here

                            pkg: # Abstraction package
                                 # (Example: genie_libs)

                            method: # Location of the processor method
                                    # (Example: sdk.libs.prepostprocessor.sleep_processor)

                            parameters: # (Optional if no parameters)
                                        # Any key will be passed as a parameters
                                        <key>: <value>

        static: # Most trigger learn dynamically certain data.
                # This key allows to specify which value to use instead of learning.
                # (Optional will learn all the keys dynamically in the trigger)
                <key>: <value>
        num_values: # Most trigger learn dynamically certain data.
                    # This key allows to specify how many value of each type should be learnt
                    # (Optional by default will used the one in the trigger code)
                    # (Example:
                    #       interface 1
                    #        vlan: 'all'
                    <key>: <value>
        skip_global_verifications: # Skip global verifications
                                   # Accepts a list

        # Any extra key will be passed as a parameter to the trigger.
        <key>: <value>

    global_processors: # Section to let Genie where the pyATS processors is located
                       # These processors will run for all triggers
          pre: # pre processors
               # (Optional if no pre processors)
               # Accepts a list of pre-processors
               # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                # or use abstraction and define optional parameters
              <processor name>: # Processor name goes here

                  pkg: # Abstraction package
                       # (Example: genie_libs)

                  method: # Location of the processor method
                          # (Example: sdk.libs.prepostprocessor.sleep_processor)

                  parameters: # (Optional if no parameters)
                              # Any key will be passed as a parameters
                              <key>: <value>

          post: # post processors
                # (Optional if no post processors)
                # Accepts a list of post processors
                # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                # or use abstraction and define optional parameters
              <processor name>: # Processor name goes here

                  pkg: # Abstraction package
                       # (Example: genie_libs)

                  method: # Location of the processor method
                          # (Example: sdk.libs.prepostprocessor.sleep_processor)

                  parameters: # (Optional if no parameters)
                              # Any key will be passed as a parameters
                              <key>: <value>

          exception: # exception processors
                     # (Optional if no exception processors)

                     # Accepts a list of exception processors
                     # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                     # or use abstraction and define optional parameters
              <processor name>: # Processor name goes here

                  pkg: # Abstraction package
                       # (Example: genie_libs)

                  method: # Location of the processor method
                          # (Example: sdk.libs.prepostprocessor.sleep_processor)

                  parameters: # (Optional if no parameters)
                              # Any key will be passed as a parameters
                              <key>: <value>

    order: # accepts a list of triggers
        - <trigger name>
           # (Optional if no special ordering expected)
           # This list will decide the execution order of triggers
           # any trigger not defined here will be excluded

        # OR

           # A list of dictionaries for each trigger
           # with trigger arguments supported as above
        - <trigger name>: *trigger_arguments


.. _config_datafile:

Configuration Datafile
----------------------

.. code-block:: yaml

    # Config Datafile schema
    # -----------------------
    #
    # Production schema with commentary from the devs

    extends: # Use this field to extend an existing yaml Trigger file,
             # allowing you to create an inheritance hierarchy.
             # Supports full path/names or names of file in the the same dir.
             # (Optional)

    variables: # Use this field to store any information as dict to be shared
               # within this datafile
               # Can be retrieved : %{variables.<field>}

    parameters: # same purpose with variables
                # Can be retrieved : %{parameters.<field>}

    devices: # Devices list to apply the configuration

        <device name>: # Name of the device.
                       # Can either be an alias or device hostname
                       # as defined in the pyats testbed file.

            <Number>: # This number will decide the order of
                      # the applied configurations on the device.

                type: # Type of configuration (setup or cleanup).
                      # (Optional, defaults to 'setup')

                config: # Full path of config file to apply on the device.
                        # (Optional)

                jinja2_config: # Full path of jinja2 config file
                               # (Optional)

                jinja2_arguments: # Arguments to be added into the jinja2 file
                                  # (Optional)
                        <key>: <value>  # Key/Value pair of arguments

                configure_arguments: # Arguments passed to unicon configure() service
                        <key>: <value>  # Key/Value pair of arguments

                sleep: # As device configurations take some time to
                       # stabilize, this sleep will tell Genie
                       # how long to wait before continuing, in seconds.
                       # (Optional)
                       # (Default: 0)

                invalid: # When applying configuration, we might see
                         # some errors or warnings. Any error or warning
                         # patterns specified in the `invalid` key will
                         # fail the configure subsection.
                         # (Optional)
                         # (Supports regex)

    exclude_config_check: # Configuration to be excluded
                          # in the check_config subsection.
                          # (Optional)
                          # (Supports regex)
                          # (Example: ['(.*uptime.*),]

.. _pts_datafile:

PTS Datafile
------------

.. code-block:: yaml

    # PTS Datafile schema
    # -------------------
    #
    # Production schema with commentary from the devs

    extends: # Use this field to extend an existing yaml PTS file,
             # allowing you to create an inheritance hierarchy.
             # Supports full path/names or names of file in the the same dir.
             # ``Genie`` provides a master set of PTS for you to extend
             # from as a start. It may be found at:
             # <$virtual_env>/lib/python3.4/site-packages/genie/infra/pts.yaml

    variables: # Use this field to store any information as dict to be shared
               # within this datafile
               # Can be retrieved : %{variables.<field>}

    parameters: # same purpose with variables
                # Can be retrieved : %{parameters.<field>}

    <feature name>: # Feature name to profile goes here.

        source: # This section is used to let
                # Genie know where the profile class
                # is located.

            pkg: # Abstraction package.
                 # (optional if no abstraction)
                 # (Example: genie_libs)

            class: # Location of the class.
                   # (Example: ops.ospf.ospf.Ospf)

        exclude: # Attributes to be ignored.
                 # (Optional)
                 # (Supports regex)

        devices: # Devices list to execute the verification.
                 # Can either be an alias or device hostname
                 # as defined in the pyats testbed file.
                 # If there is no device, the verification will not execute.

        devices_attributes: # attributes for the devices
                            # (Optional)

            <device name>: # Name of the device; must be same as devices list

                # Any extra key will be passed as a parameter to the verification
                <key>: <value>

.. _mapping_datafile:

Mapping Datafile
----------------

Mapping datafile is not mandatory in Genie, it is required when user desires to
control the connection per device.

By Default (if not provided);
``Genie`` will connect all the devices in the testbed yaml file as soon as
they have either;

* A single connection defined

.. code-block:: python

    connections:
        defaults:
            class: 'unicon.Unicon'
        a:
            protocol: telnet
            ip: "100.100.100.100"
            port: 1234


* A connection named `cli` within provided multiple connections

.. code-block:: python

    connections:
        defaults:
            class: 'unicon.Unicon'
        a:
            protocol: telnet
            ip: "100.100.100.100"
            port: 1234
        cli:
            protocol: telnet
            ip: "200.200.200.200"
            port: 5678


.. code-block:: yaml

    # Mapping Datafile schema
    # -----------------------
    #
    # Production schema with commentary from the devs

    variables: # Use this field to store any information as dict to be shared
               # within this datafile
               # Can be retrieved : %{variables.<field>}

    parameters: # same purpose with variables
                # Can be retrieved : %{parameters.<field>}

    devices: # Devices

        <device name>: # Name of the device.
                       # Can either be an alias or device hostname
                       # as defined in the pyats testbed file.

            context: # Context to priotize for the Genie execution.

            pool_size: # Connection pool size, in case of using pyATS connection
                       # pool feature.
                       # Optional, `harness` will issue single connection if it
                       # is not provided.

            label:  # One device in the testbed must be designated as the `uut`
                    # for ``Genie``.  If no device is already named `uut`, then
                    # you must map it via `label` field, as shown in the example
                    # above. In the event that the device is already named uut
                    # via `alias` in the testbed file, then there is no need to
                    # use label field.

            mapping: #

                cli: # Which connection to use for Cli commands.
                yang: # Which connection to use for Yang commands.
                xml: # Which connection to use for xml commands.
                rest: # Which connection to use for rest commands.

    topology: # Topologies

        links: # Links

            <link name>: # Name of the link

                label: # Label to override the alias of the specified link

        <device name>: # Name of the device for interfaces

            interfaces: # The device's interfaces

                <interface name>: # Name of the interface

                    label: # Label to override th alias of the specified interface


* Different connections using Mapping datafile:

The user can connect with different connections using the following schema.

``Note``: The user can either use this new schema or the one mentioned above.
``Note``: via and alias keywords are mandatory when using new mapping schema.

.. code-block:: python

    devices:
      uut:
        mapping:
          context:
              cli:
               - via: cli
                 alias: cli
                 pool_size: 5
                 sleep: 3
               - via: ssh
                 alias: cli2
              yang:
                - via: yang
                  alias: netconf


.. code-block:: yaml

    # New Mapping Datafile schema for different connections
    # -------------------------------------------------

    variables: # Use this field to store any information as dict to be shared
               # within this datafile
               # Can be retrieved : %{variables.<field>}
    parameters: # same purpose with variables
                # Can be retrieved : %{parameters.<field>}

    devices: # Devices

        <device name>: # Name of the device.
                       # Can either be an alias or device hostname
                       # as defined in the pyats testbed file.

                label:  # One device in the testbed must be designated as the `uut`
                        # for ``Genie``.  If no device is already named `uut`, then
                        # you must map it via `label` field, as shown in the example
                        # above. In the event that the device is already named uut
                        # via `alias` in the testbed file, then there is no need to
                        # use label field.

              mapping: # To map which connection to use for in the context.

                  context: # Context for the Genie execution.

                            via: #Specify the connection to use. Eg. cli, ssh, yang etc

                            alias: #The alias name of the connection. Eg. my_connection

                            pool_size: # Connection pool size, in case of using pyATS connection
                                       # pool feature.
                                       # Optional, `harness` will issue single connection if it
                                       # is not provided.

                            sleep: #Take a nap after making connection. By default 5 seconds for yang, gnmi, restconf,
                                   netconf.

.. _subsection_datafile:

Subsection datafile
-------------------

.. code-block:: yaml

    # Subsection Datafile schema
    # --------------------------
    #
    # Production schema with commentary from the devs

    extends: # Use this field to extend an existing yaml Subsection data file,
             # allowing you to create an inheritance hierarchy.
             # Supports full path/names or name of file in the the same dir.

    variables: # Use this field to store any information as dict to be shared
               # within this datafile
               # Can be retrieved : %{variables.<field>}

    parameters: # same purpose with variables
                # Can be retrieved : %{parameters.<field>}

    setup: # CommonSetup subsections
           # (optional if common setup)

        sections: # Subsections
                  # (Optional if no new subsection)

            <subsection name>: # Name of the Subsection.

                method: # Location of the subsection methods
                        # (Example: genie_libs.sdk.libs.subsections.my_subsection)

                parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>
                processors: # This section is used to let
                                # Genie know where the pyATS processors is located

                        pre: # pre processors
                        # (Optional if no pre processors)
                        # Accepts a list of pre-processors
                        # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                        # or use abstraction and define optional parameters
                        <processor name>: # Processor name goes here

                                pkg: # Abstraction package
                                # (Example: genie_libs)

                                method: # Location of the processor method
                                        # (Example: sdk.libs.prepostprocessor.sleep_processor)

                                parameters: # (Optional if no parameters)
                                        # Any key will be passed as a parameters
                                        <key>: <value>

                        post: # post processors
                        # (Optional if no post processors)
                        # Accepts a list of post processors
                        # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                        # or use abstraction and define optional parameters
                        <processor name>: # Processor name goes here

                                pkg: # Abstraction package
                                # (Example: genie_libs)

                                method: # Location of the processor method
                                        # (Example: sdk.libs.prepostprocessor.sleep_processor)

                                parameters: # (Optional if no parameters)
                                        # Any key will be passed as a parameters
                                        <key>: <value>

                        exception: # exception processors
                                # (Optional if no exception processors)

                                # Accepts a list of exception processors
                                # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                                # or use abstraction and define optional parameters
                        <processor name>: # Processor name goes here

                                pkg: # Abstraction package
                                # (Example: genie_libs)

                                method: # Location of the processor method
                                        # (Example: sdk.libs.prepostprocessor.sleep_processor)

                                parameters: # (Optional if no parameters)
                                        # Any key will be passed as a parameters
                                        <key>: <value>

        order: # accepts a list of subsections
               # (Optional if no special ordering expected)
               # This list will decide the execution order of subsections
               # any subsection not defined here will be excluded

        processors: # Processors
                    # (Optional; only if want processor for common_setup)

            pre:  # pre processors
                  # (Optional if no pre processors)
                  # Accepts a list of pre processors
                  # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                  # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

            post: # post processors
                  # (Optional if no post processors)
                  # Accepts a list of post processors
                  # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                  # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

            exception: # exception processors
                       # (Optional if no exception processors)

                       # Accepts a list of exception processors
                       # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                       # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>


    cleanup: # CommonSetup subsections
             # (optional if common cleanup)

        sections: # Subsections
                  # (Optional if no new subsection)

            <subsection name>: # Name of the Subsection.

            method: # Location of the subsection methods
                    # (Example: genie_libs.sdk.libs.subsections.my_subsection)

            parameters: # (Optional if no parameters)
                        # Any key will be passed as a parameters
                        <key>: <value>
            processors: # This section is used to let
                        # Genie know where the pyATS processors is located

                pre: # pre processors
                     # (Optional if no pre processors)
                     # Accepts a list of pre-processors
                     # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                     # or use abstraction and define optional parameters
                    <processor name>: # Processor name goes here

                        pkg: # Abstraction package
                             # (Example: genie_libs)

                        method: # Location of the processor method
                                # (Example: sdk.libs.prepostprocessor.sleep_processor)

                        parameters: # (Optional if no parameters)
                                    # Any key will be passed as a parameters
                                    <key>: <value>

                post: # post processors
                      # (Optional if no post processors)
                      # Accepts a list of post processors
                      # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                      # or use abstraction and define optional parameters
                    <processor name>: # Processor name goes here

                        pkg: # Abstraction package
                             # (Example: genie_libs)

                        method: # Location of the processor method
                                # (Example: sdk.libs.prepostprocessor.sleep_processor)

                        parameters: # (Optional if no parameters)
                                    # Any key will be passed as a parameters
                                    <key>: <value>

                exception: # exception processors
                           # (Optional if no exception processors)

                           # Accepts a list of exception processors
                           # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                           # or use abstraction and define optional parameters
                    <processor name>: # Processor name goes here

                        pkg: # Abstraction package
                             # (Example: genie_libs)

                        method: # Location of the processor method
                                # (Example: sdk.libs.prepostprocessor.sleep_processor)

                        parameters: # (Optional if no parameters)
                                    # Any key will be passed as a parameters
                                    <key>: <value>

        order: # accepts a list of subsections
               # (Optional if no special ordering expected)
               # This list will decide the execution order of subsections
               # any subsection not defined here will be excluded

        processors: # Processors
                    # (Optional; only if want processor for common_cleanup)

            pre:  # pre processors
                  # (Optional if no pre processors)
                  # Accepts a list of pre processors
                  # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                  # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

            post: # post processors
                  # (Optional if no post processors)
                  # Accepts a list of post processors
                  # (Example: [sdk.libs.prepostprocessor.sleep_processor])
                  # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>

            exception: # exception processors
                       # (Optional if no exception processors)

                       # Accepts a list of exception processors
                       # (Example: [sdk.libs.prepostprocessor.sleep_processor])

                       # or use abstraction and define optional parameters
                <processor name>: # Processor name goes here

                    pkg: # Abstraction package
                         # (Example: genie_libs)

                    method: # Location of the processor method
                            # (Example: sdk.libs.prepostprocessor.sleep_processor)

                    parameters: # (Optional if no parameters)
                                # Any key will be passed as a parameters
                                <key>: <value>
