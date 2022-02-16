.. _harness_arguments:
Arguments
=========

This page provides details about the customizable argument in ``Genie``.
Please visit the :ref:`Getting started guide <getting_genie>` if you are new to
``Genie`` harness.

Arguments
---------

``Genie`` is highly customizable and can be tailored to meet your testing
specifications and requirements. All arguments can either be provided in the
job file as an argument to `gRun` or as a `-` argument to easypy. 

All arguments are optionals.

.. csv-table:: Genie Standard Arguments
    :header: Argument, Description
    :widths: 30, 70

    ``--pts-features``, "List of features to execute PTS on"
    ``--pts-golden-config``, "Full path/name to previously verified PTS file"
    ``--verification-uids``, "Specifies the list of verifications uids to run (list or logic expression)"
    ``--verification-groups``, "Specifies the list of verifications groups to run (logic expression)"
    ``--trigger-uids``, "Specifies the list of triggers uids to run (list or logic expression)"
    ``--trigger-groups``, "Specifies the list of triggers groups to run (logic expression)"
    ``--devices``, "List of devices to connect to (in case of no mapping datafile)"
    ``--subsection-datafile``, "Full path/name or URL to the common_(setup/cleanup) subsection datafile"
    ``--mapping-datafile``, "Full path/name or URL to the mapping datafile"
    ``--verification-datafile``, "Full path/name or URL to the verification datafile"
    ``--trigger-datafile``, "Full path/name or URL to the trigger datafile"
    ``--config-datafile``, "Full path/name or URL to the config datafile"
    ``--pts-datafile``, "Full path/name or URL to the PTS datafile"
    ``--debug-plugin``, "Full path/name to the debug plugin (N7k)"
    ``--random``, "flag to enable trigger randomization"
    ``--random-seed``, "testcase randomization seed"  

.. tip::

    These arguments work on top of all existing easypy_ and aetest_
    arguments.

Below you will find additional information on each of those arguments:

``--pts-features``

    Which :models:`feature<http>` to profile the system. More info on PTS can be found
    :ref:`here <PTS>`.

    .. code-block:: bash

         --pts-features 'ospf bgp'

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(pts_features=['ospf', 'bgp'])

``--pts-golden-config``

    Specifies the location of the PTS golden configuration file. More information
    on the `pts-golden-config` can be found :ref:`here <Golden>`

.. note::

    If golden pts file is different for every run (ex: different per branch),
    user will need to create a directory per branch and place
    pts file inside it named as `golden_pts` then pass the directory path as
    an `genie run` argument or inside a job file.

    Example:
    User has two different `golden_pts` files per branch (hamilton, greensboro).

    User now needs to create two directories named hamilton and greensboro and
    place the `golden_pts` file under the corresponding directory then provide
    the directories' path (path holding the created directories) as below.


    .. code-block:: bash

         genie run /path/to/jobfile.py --pts-golden-config /path/pts

         or

         genie run /path/to/jobfile.py --pts-golden-config <path to the directory>

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(pts_golden_config='/path/pts')

         or

         gRun(pts_golden_config='<path to the directory>')


``--verification-uids``

    Specifies the list of verifications uids to be executed.
    This argument accepts a string in which each verification-uid is separated by space. 
    Also, it supports logical callable that determines which 
    verifications to execute by matching the verification uids to the
    pattern provided as input to the callable.
    
    A valid python syntax input is necessary whenever this argument in used in command line so that 
    :logic:`Logic <http>` String Inputs may evaluate it.

    .. code-block:: bash

         --verification-uids "Verify_IpOspfNeighborDetail_vrf_all Verify_IpRoute_protocol_bgp"

         or

         --verification-uids "Or('Verify_IpOspfNeighborDetail_vrf_all', 'Verify_IpRoute_protocol_bgp')"

    Or inside a job file, define the verifications to be executed as a list or logical callable

    .. code-block:: python

         # Inside a job file using list

         gRun(verification_uids=['Verify_IpOspfNeighborDetail_vrf_all', 'Verify_IpRoute_protocol_bgp'])

         or

         # Inside a job file using logic expression

         from pyats.datastructures.logic import Or

         gRun(verification_uids=Or('Verify_IpOspfNeighborDetail_vrf_all', 'Verify_IpRoute_protocol_bgp'))

.. note::

    The verification name is the name of a verification as seen in the
    verifications datafile.

``--verification-groups``

    Specify the group(s) of verifications to execute. This argument accepts a
    logical callable that determines which verifications to execute by matching
    the verification groups to the pattern provided as input to the callable.

    A valid python syntax input is necessary whenever this argument in used in command line so that 
    :logic:`Logic <http>` String Inputs may evaluate it.

    .. code-block:: bash

        genie run /path/to/jobfile.py --verification-groups="And(Or('group1','group2'), 'group3')"

    .. code-block:: python

        # aetest.main() example using datastructure logic
        from pyats.datastructures.logic import Or, And
        gRun(verification_groups=And(Or('group1','group2'), 'group3'))

.. note::

    A verification can be associated to a particular group in the
    `verification_datafile`. With this association, ``Genie``
    can filter execution of verifications based on which groups they are
    associated with. A verification can have many groups associated with it.

``-trigger-uids``

    Specifies the list of triggers to be executed. 
    This argument accepts a string in which each trigger-uid is separated by space. 
    Also, it supports pattern matching by logical callable, that is, 
    it determines which triggers to execute by matching
    the triggers uids to the pattern provided as input to the callable

    A valid python syntax input is necessary whenever this argument is used in command line so that 
    :logic:`Logic <http>` String Inputs may evaluate it.

    .. code-block:: bash

         genie run /path/to/jobfile.py --trigger-uids "TriggerUnconfigConfigBgp TriggerShutNoShutEthernetInterface"

         or

         genie run /path/to/jobfile.py --trigger-uids "Or('TriggerUnconfigConfigBgp', 'TriggerShutNoShutEthernetInterface')"

    Or inside a job file, define the triggers to be executed as a list or logical callable

    .. code-block:: python

         # Inside a job file using list

         gRun(trigger_uids=['TriggerUnconfigConfigBgp', 'TriggerShutNoShutEthernetInterface'])

         or

         # Inside a job file using logic expressions

         from pyats.datastructures.logic import Or

         gRun(trigger_uids=Or('TriggerUnconfigConfigBgp', 'TriggerShutNoShutEthernetInterface'))

.. note::
    
    uid is the name of a trigger as seen in the triggers datafile.

``-trigger-groups``

    Specifies the group(s) of triggers to execute. This argument accepts a
    logical callable that determines which triggers to execute by matching
    the triggers' groups to the pattern provided as input to the callable

    A valid python syntax input is necessary whenever this argument in used in command line so that 
    :logic:`Logic <http>` String Inputs may evaluate it.

    .. code-block:: bash

        genie run /path/to/jobfile.py --trigger-groups="And(Or('group1','group2'), 'group3')"

    .. code-block:: python

        # aetest.main() example using datastructure logic
        from pyats.datastructures.logic import Or, And
        gRun(trigger_groups=And(Or('group1','group2'), 'group3'))

.. note::

    A trigger can be associated with a particular group in the
    `trigger_datafile`. This association allows ``Genie``
    to filter execution of triggers based on the groups they are
    associated with. A trigger can have many groups associated with it.

``--mapping-datafile``

    Specifies the location of the mapping configuration file. This argument
    is optional to run ``Genie``.

    More details on the syntax of the datafile can be found in the
    :ref:`datafile <mapping_datafile>` section.
    URL with token can be given like below example.

    .. code-block:: bash

         --mapping-datafile /path/mapping.pts
         --mapping-datafile "http://<url>/mapping.pts"
         --mapping-datafile "http://<token>@<url>/mapping.pts"

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(mapping_datafile='/path/mapping.pts')

.. important::

    This argument is optional. ``Genie`` will connect to all devices by default
    if no mapping datafile is provided

``--verification-datafile``

    Specifies the location of the verification datafile. More details on the
    syntax for the file can be found in the :ref:`datafile <verification_datafile>`
    section.
    URL with token can be given like below example.

    .. code-block:: bash

         --verification-datafile /path/verificationdatafile.yaml
         --verification-datafile "http://<url>/verificationdatafile.yaml"
         --verification-datafile "http://<token>@<url>/verificationdatafile.yaml"

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(verification_datafile='/path/verificationdatafile.yaml')

.. note:: 

    By default Genie uses $VIRTUAL_ENV/lib/python<version>/site-packages/genie/libs/sdk/genie_yamls/<uut os>/verification_datafile_<uut os>.yaml

``--trigger-datafile``

    Specifies the location of the trigger datafile. More details on the syntax
    for the file can be found in the :ref:`datafile <trigger_datafile>` section.
    URL with token can be given like below example.

    .. code-block:: bash

         pyats run job --trigger-datafile /path/triggerdatafile.yaml
         pyats run job --trigger-datafile "http://<url>/triggerdatafile.yaml"
         pyats run job --trigger-datafile "http://<token>@<url>/triggerdatafile.yaml"

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(trigger_datafile='/path/triggerdatafile.yaml')

.. note:: 

    By default Genie uses $VIRTUAL_ENV/lib/python<version>/site-packages/genie/libs/sdk/genie_yamls/<uut os>/trigger_datafile_<uut os>.yaml

``--config-datafile``

    Specifies the location of the configuration datafile. Configuration
    datafile contains the path of configuration file to apply on the device.
    
    More details on the syntax for the file can be found in the :ref:`datafile
    <config_datafile>` section.
    URL with token can be given like below example.

    .. code-block:: bash

         --config-datafile /path/config_datafile.yaml
         --config-datafile "http://<url>/config_datafile.yaml"
         --config-datafile "http://<token>@<url>/config_datafile.yaml"

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(config_datafile='/path/config_datafile.yaml')


``--subsection-datafile``

    Specifies the location of the CommonSetup/CommonCleanup subsection datafile.

    More details on the syntax for the CommonSetup/CommonCleanup subsection
    datafile can be found in the :ref:`datafile <subsection_datafile>` section.
    URL with token can be given like below example.

    .. code-block:: bash

         pyats run job /path/to/jobfile.py --subsection-datafile /path/subsection_datafile.yaml
         pyats run job /path/to/jobfile.py --subsection-datafile "http://<url>/subsection_datafile.yaml"
         pyats run job /path/to/jobfile.py --subsection-datafile "http://<token>@<url>/subsection_datafile.yaml"

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(subsection_datafile='/path/subsection_datafile.yaml')

.. note::

    If no `subsection_datafile` is provided, it will use the default ``Genie``
    one which includes `connect`, `config` `check_config`.

``--pts-datafile``

    Specifies the location of the PTS datafile.

    More details on the syntax for the PTS datafile can be found in the :ref:`datafile
    <pts_datafile>` section.
    URL with token can be given like below example.

    .. code-block:: bash

         pyats run job /path/to/jobfile.py --pts-datafile /path/pts_datafile.yaml
         pyats run job /path/to/jobfile.py --pts-datafile "http://<url>/pts_datafile.yaml"
         pyats run job /path/to/jobfile.py --pts-datafile "http://<token>@<url>/pts_datafile.yaml"

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(pts_datafile='/path/pts_datafile.yaml')


``--debug-plugin``

    Specifies the location of the debug plugin

    .. code-block:: bash

        # In case of single debug plugin in the run
         genie run /path/to/jobfile.py --debug-plugin /path/debug_plugin

        # In case of multiple debug plugins in the run (differnet device types)
         genie run /path/to/jobfile.py --debug-plugin /path/

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         # In case of single debug plugin in the run
         gRun(debug_plugin='/path/debug_plugin')

         # Inside a job file
         # In case of multiple debug plugins in the run (differnet device types)
         gRun(debug_plugin='/path/')

.. note::

    In case of multiple debug plugins, user needs to pass the debug plugin itself
    in the testbed yaml file under the corresponding device under custom section as below;
        custom:
            debug_plugin: n7700-s2-debug-sh.8.4.1.gbin


``--devices``

    List of devices to connect to in case of no mapping datafile is passed
    to ``Genie`` and user wants to connect to multiple devices.

    If not provided and no mapping datafile provided, ``Genie`` will connect
    all the devices in the testbed yaml file

    .. code-block:: bash

         genie run /path/to/jobfile.py --devices ['N95_1', 'N95_2']

    Or inside a job file

    .. code-block:: python

         # Inside a job file
         gRun(devices=['N95_1', 'N95_2'])

``--random``

    flag to enable triggers randomization, allowing a script’s testcase orders
    to be randomly shuffled before execution. To learn more about testcase
    randomization, refer to Testcase Randomization.

    .. code-block:: python
    
        gRun(pts_features=['platform', 'bgp', 'interface'],
             verification_uids=['Verify_IpInterfaceBrief', 'Verify_IpRoute_vrf_all'],
             trigger_uids=['TriggerUnconfigConfigBgp.uut', 'TriggerShutNoShutBgpNeighbors', 'TriggerModifyLoopbackInterfaceIp.uut', 'TriggerShutNoShutEthernetInterface'],
             random=True)

``--random-seed``

    randomization seed integer, used to fix the randomizer and re-generate the
    same triggers sequence, useful for debugging purposes. Requires triggers
    randomization to be turned on first.

    The seed can be found in the log `Testcase randomization is enabled, seed:
    1868797651672894108`

    .. code-block:: python
    
        gRun(pts_features=['platform', 'bgp', 'interface'],
             verification_uids=['Verify_IpInterfaceBrief', 'Verify_IpRoute_vrf_all'],
             trigger_uids=['TriggerUnconfigConfigBgp.uut', 'TriggerShutNoShutBgpNeighbors', 'TriggerModifyLoopbackInterfaceIp.uut', 'TriggerShutNoShutEthernetInterface'],
             random=True, randomize_seed=1868797651672894108)
    
