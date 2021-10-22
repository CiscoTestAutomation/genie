.. _robot_genie:

RobotFramework Guide
====================

.. sidebar:: Quick References

    - `RobotFramework`_
    - `Genie Keywords`_
    - `API Function Keywords`_

.. _RobotFramework: https://robotframework.org/
.. _Genie Keywords: ../robot.html
.. _API Function Keywords: ../robot_api.html

Robot Framework is generic Python/Java test automation framework that focuses
on acceptance test automation by through English-like keyword-driven test
approach.

Robot Framework support has been added through the optional ``robot``
sub-package under `Genie.libs` namespace. This enables RobotFramework
users to leverage key aspects of Genie without having to reinvent the wheel.
Robot Framework libraries have also been added for :pyats_robot:`pyATS <http>`
and Unicon.

`Genie keywords`_

Installation
------------

Robot Framework support is an optional component under Genie. To use it, you 
must install this package explicitly:

.. code-block:: bash

    pip install --upgrade genie.libs.robot


Features
--------
- run Genie :triggers:`Triggers <http>` and converting results to Robot
- run Genie :verifications:`Verifications <http>` and converting results to Robot
- Execute Genie Ops object to learn about a feature
- Metaparser support (Can re-use any existing :parser_repo:`parser <http>`)
- Custom verify functions, such as:
    * Verify x amount of bgp routes on a device
    * Verify x amount of up interfaces on a device
- Genie Device API support, all :apis:`API functions <http>` can be used as a keyword, simply replace the '_' to a space and put it in your .robot file with the arguments. Make sure to import `genie.libs.robot.GenieRobotApis` as a library.
- :ref:`Dq support<utils_overview>`

**Example of calling device APIs with robot**

.. code-block:: robotframework

	*** Settings ***
	# Importing test libraries, resource files and variable files.
	Library        ats.robot.pyATSRobot
	Library        genie.libs.robot.GenieRobot
	Library        genie.libs.robot.GenieRobotApis

	${testbed}    testbeds/my_tb.yaml

	*** Test Cases ***

	Initialize
		# Initializes the pyATS/Genie Testbed
		use genie testbed "${testbed}"

		# Connect to both device
		connect to device "PE1" via "cli"

	test
		shut interface   			Loopback0	device=PE1
		verify interface config shutdown    	Loopback	device=PE1
		unshut interface  			Loopback0	device=PE1
		verify interface config no shutdown 	Loopback0	device=PE1


.. note::

    Genie Robot librairies is open sourced under `genie.libs`, it can be
    enhanced to add additional keywords.

Keywords
--------

For the complete set of keywords supported by this package, refer to
`Genie Keywords`_.

Example
-------

.. code-block:: robotframework
    
    # Example
    # -------
    # 
    #   Demonstration of Genie Robot Framework Keywords

    ** Settings ***
    Library        ats.robot.pyATSRobot
    Library        genie.libs.robot.GenieRobot
    Library        unicon.robot.UniconRobot
    
    *** Variables ***
    # Defining variables that can be used elsewhere in the test data.
    # Can also be driven as dash argument at runtime
    ${testbed}     tb.yaml
    
    *** Test Cases ***
    # Creating test cases from available keywords.
    
    Connect
        use genie testbed "${testbed}"
        connect to devices "N95_1"
    
    parser show version
        ${output}=    parse "show module" on device "N95_1"

    Verify version
        dq query    data=${output}   filters=contains('lc').not_contains('2').get_values('slot/world_wide_name')

    
    Learn bgp
        ${output}=    learn "bgp" on device "N95_1"
    
    verify Bgp before trigger
        run verification "Verify_BgpAllNexthopDatabase" on device "N95_1"
    
    Trigger sleep
        run trigger "TriggerSleep" on device "N95_1" using alias "cli"
    
    verify Bgp after trigger
        run verification "Verify_BgpAllNexthopDatabase" on device "N95_1"
    
    verify bgp count
        verify count "6" "bgp neighbors" on device "N95_1"
    
    verify bgp routes
        verify count "100" "bgp routes" on device "N95_1"


.. note::

    Different location for `trigger_datafile` and `verification_datafile` can
    be provided within the Variables section. By default it uses these ones:

    ``${trigger_datafile}     $VIRTUAL_ENV/lib/python<version>/site-packages/genie/libs/sdk/genie_yamls/<uut os>/trigger_datafile_<uut os>.yaml``
    ``${verification_datafile}     ${VIRTUAL_ENV}/lib/python<version>/site-packages/genie/libs/sdk/geine_yamls/<uut os>/verification_datafile_<uut os>.yaml``
    

System Profiling
----------------
Robot user can now verify the testbed unchanged state by profiling the system at
different stages during the run and using those profiles as reference points at
later stages or even in other runs.

When the user profile the system and uses the option to store the profile on a
mount, actually two files get created at the run directory. One is json file
showing the full structure of the learnt features and the other is a pickled
version which can be used later for comparison as shown in details in the below
example.

.. code-block:: robotframework

    # Example
    # -------
    #
    #   Demonstration of Genie Robot Framework Keywords with System Profiling

    ** Settings ***
    Library        ats.robot.pyATSRobot
    Library        genie.libs.robot.GenieRobot
    Library        unicon.robot.UniconRobot

    *** Variables ***
    # Defining variables that can be used elsewhere in the test data.
    # Can also be driven as dash argument at runtime

    ${testbed}     tb.yaml
    ${PTS}         /path/file

    *** Test Cases ***
    # Creating test cases from available keywords.

    Connect
        use genie testbed "${testbed}"
        connect to devices "R1"

    # Profile bgp&ospf features and save the profile system on a mount
    Profile bgp & ospf on All
        Profile the system for "bgp;ospf" on devices "R1;R2" as "/path/file"

    Profile bgp & ospf on uut only
        Profile the system for "bgp;ospf" on devices "R1;R2" as "/path/file" using alias "uut"

    # Profile bgp&ospf features and compare to the previously stored profile
    Profile bgp & ospf on All and Compare to PTS
        Profile the system for "bgp;ospf" on devices "R1;R2" as "current"
        Compare profile "${PTS}" with "current" on devices "R1;R2"

    Profile bgp & ospf on All and Compare to another profile "later"
        Profile the system for "bgp;ospf" on devices "R1;R2" as "current"

    Run any testcase
        <Do some action>

    # Profile bgp&ospf features and compare to the previously stored profile "current"
    Profile bgp & ospf on All and Compare to another profile
        Profile the system for "bgp;ospf" on devices "R1;R2" as "later"
        Compare profile "later" with "current" on devices "R1;R2"

.. note::

    Different location for `pts_datafile` can be provided within the Variables
    section. By default it uses these ones:

    ``${datafile}    ${VIRTUAL_ENV}/genie_yamls/pts_datafile.yaml``

.. hint::

    Multiple snapshots can be saved within the same run and then compared.

.. note::

    Device configuration can also be snapshotted by adding the name config.
   
.. code-block:: robotframework

    Profile the system for "bgp;ospf;config" on devices "R1;R2" as "later"
