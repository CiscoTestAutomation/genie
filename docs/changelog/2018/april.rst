April 2018
==========

April 30th - Genie v3.0.0
--------------------------

Today, we are proud to make your wish becoming true: the availability of Genie v3.0.0! 

With plenty of infrastructure enhancements in the core, 200+ triggers and 280+ verifications spanning over 25 features, Genie v3.0.0 is here to make your mundane test automation exciting. 

* Simplifies the implementation of complex & comprehensive testing using Genie SDK
* Leverage any Genie triggers & verifications in your traditional pyATS test suites

Gone are the days where you have to write script-after-script: with Genie, we are aiming to shift the focus from scripting, to YAML-based, data file driven test automation, using repeatable & re-useable, platform-agnostic test case libraries.

Release Highlights:

*    Genie Harness - support for Stimulus, Events & Activity (SEA) based testing using 
     OS/Platform/(Cli/Yang/Xml) agnostic triggers & verifications 
*    Plethora of new features, parsers, conf & ops libraries, with traffic generator support
*    Robot Framework keyword support in Genie, pyATS and Unicon
*    Introduction of Genie telemetry: a plug & play framework that monitors your testbed devices during script run for crashes, core dumps, and any related performance & stability issues/metrics through plugins
*    Various core infrastructure enhancements:
    *    support for pyATS v4.1.0
    *    support for Python 3.5/3.6 (32/64bit) in addition to 3.4
    *    support for Mac OSX & WSL in addition to Linux
*    new examples that can be run on your own topologies or VIRL testbeds

With pyATS released through DevNet in Q2FY18, we made our first baby step towards enabling Cisco engineering teams to collaborate with end customers on transparent development of new test suites. However, we always knew that the power of any test automation infrastructure lies always with its libraries. As such -

Today, we announce the availability of Genie, and corresponding libraries, through Cisco DevNet.

What does this mean for you?

*    Use Genie libraries anywhere, anytime, for any reasons, internally and externally.
*    Share your Genie-based test suites with end-customers, leveraging all of the power of Genie, and its triggers & verifications library.
*    Invite customers to collaborate, and jointly develop [third-party] libraries and parsers

https://github.com/CiscoTestAutomation/genielibs
https://github.com/CiscoTestAutomation/genieparser



.. csv-table:: New Packages Versions
    :header: "Packages", "Versions"

    ``Genie``, 3.0.0
    ``Genie.ops``, 3.0.0
    ``Genie.conf``, 3.0.0
    ``Genie.harness``, 3.0.0
    ``Genie.utils``, 3.0.0

.. csv-table:: New Libraries Versions
    :header: "Libraries", "Versions"

    ``Genie.libs.ops``, 3.0.0
    ``Genie.libs.conf``, 3.0.0
    ``Genie.libs.sdk``, 3.0.0
    ``Genie.libs.robot``, 3.0.0

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

.. note::

    Genie comes with many new libraries/packages. The following will also be
    installed genie.metaparser, genie.parsergen, genie.abstract, genie.telemetry,
    genie.parsergen genie.predcore, genie.libs.filetransferutils

Features:
^^^^^^^^^

**Genie**


* Genie is growing! Many packages have been added to the Genie namespace
  (`abstract`, `parsergen`, `genietelemetry`, `predcore`, `metaparser`)

    * import abstract -> from genie import abstract
    * import parsergen -> from genie import parsergen
    * import predcore -> from genie import predcore
    * import metaparser -> from genie import metaparser
    * import genie_libs -> from genie import libs
    * from genie_libs import conf -> from genie.libs import conf
    * from genie_libs import ops -> from genie.libs import ops
    * from genie_libs import sdk -> from genie.libs import sdk

* :genietelemetry:`GenieTelemetry <http>` has been released! A framework that
  monitors your testbed devices during script run for crashes, core dumps, and
  any related performance & stability issues/metrics through plugins. It is fully
  :ref:`integrated within Genie <genietelemetry>`
* Following `pyATS` latest release, Genie now fully supports Python 3.4, 3.5+ and
  3.6+, and can now install and run on Mac OSX platforms
* `Unicon` is now the mandatory connection to use for ``Genie``, as `Csccon` is reaching its end of life and support

.. code-block:: python

  csr1000v-1:
      type: asr1k
      os: "iosxe"
      alias: helper
      tacacs:
          login_prompt: 'login:'
          password_prompt: 'Password:'
          username: cisco
      passwords:
          tacacs: cisco
          enable: cisco
          line: cisco
      connections:
          defaults:
            class: 'unicon.Unicon'
          a:
              protocol: telnet
              ip: xxx.xx.xx.xx
              port: xxxxx
      custom:
        abstraction:
          order: [os]

* 25 feature :models:`models <http>` to create agnostic script


**Genie.Conf**

* Genie objects now inherits from the pyats objects to cover the pyats objects
  features along with all the Genie functionalities;

* _pyats_<object> is now done as follow:

.. code-block:: python

	testbed._pyats_testbed.<variable>      -> testbed.<variable>
	device._pyats_device.<variable>        -> device.<variable>
	interface._pyats_interface .<variable> -> interface.<variable>
	link._pyats_link.<variable>            -> link.<variable>

* <object>_map is now done as follow:

.. code-block:: python

	devices_map    -> devices (now returns dict of devices)
	interfaces_map -> interfaces (now returns dict of interfaces)
	links_map      -> links (now returns dict of links)

.. hint:: 

      If you still require a list, you can do it with .values()

* Testbed object now returns the following:

.. code-block:: python

	devices         -> Now returns a dict of devices
	add_link        -> Retuns None
	remove_link     -> Retuns None

* Device object changes:

.. code-block:: python

	interfaces   -> Now returns a dict of interfaces
	device.links -> Now returns a set of links

* No change for Interface object

* Link object changes

.. code-block:: python

		interfaces -> Now returns a dict of links

* Genie loader has been implemented to directly load the yaml file into Genie
  objects
* Modification in the Testbed Converter

**Genie.Ops**

* Now supports kwargs to be passed to parser
* Bug fix for Maker

**Genie.Harness**

* PTS now generates a human readable json format stored in the archive file
* Genie.harness now supports :ref:`traffic generator Harness <traffic_harness>`. 
* Subsection can be added/removed dynamically with the help of subsection datafile
* Local and Global processors can be added to Trigger, Verifications and Common_setup/Common_cleanup
* Argument can be defined for processors within the datafiles
* Enhance logger for genie.harness
* Genie.harness learns the management interface, and will not pick it for executing Triggers, unless wanted
* New error pattern for Unicon support
* New :ref:`Timeout <utils_overview>` functionality
* Enhancement for trigger and verification datafile to support abstraction
* Modification of Mapping interaction within Genie
* Major rework of pyats `Find` api. Allows to ask and collect multiple requirements at once
* Enhancement to Diff
* The connect subsection can now re-use the same via for multiple context
* Enhancement to accept easypy plugins processor (eg; Cflow Plugin)

**Genie.examples**

* 9 Brand new examples demonstrating all functionalities of Genie. They can be run on your own topologies or on provided Virl_ device. 

**Genie.libs.Ops**

* New Ops object with coresponding parser

    * Vrf 
    * Prefix-list 
    * Igmp 
    * Vlan 
    * Pim 
    * mld
    * ospf 
    * static_route 
    * routing 
    * stp 
    * lldp 
    * acl 

**Genie.libs.Conf**

* New Conf object

    * Mcast 
    * vrf 
    * prefix-list 
    * igmp 
    * vlan 
    * pim 
    * mld
    * ospf 
    * static_route 
    * routing 
    * stp 
    * lldp 
    * acl 

* New connection implementation for Ixia

**Genie.libs.SDK**

* Over 200+ :triggers:`triggers <http>` within these categories:

    * AddRemove
    * Clear
    * DisableEnable
    * Modify
    * ProcessRestart
    * Reload device
    * Reload linecard
    * ShutNoShut
    * Switchover
    * Sleep
    * UnconfigConfig

* Over 280+ :verifications:`verifications <http>` to verify the state of the topology
* Major re-work to Mapping, Normalize and configure
* `Mapping` now use Timeout functionality
* Better error handling within Triggers
* Improve Trigger messages and logs
* New subsections added (Save boot variable, learn system default, initialize traffic)
* Triggers are now skipped when prerequisites aren't found to save execution time

**Genie.libs.robot**

* A new addition to Genie. :robotframework:`RobotFramework <http>` is a
  keyword-driven testframework which allows simple testscript creating. New Genie
  :robot:`robot librarires<http>` allow to re-use any ``Genie`` Trigger,
  Verification, Ops and Parser to create powerful easy to read scripts. 

.. note::

    Robot keyword has also been added to pyATS and Unicon.

For more information, make sure to go through the genie_ documentation.

.. _sections: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/harness/developer/subsections.html#using-subsections
.. _schemas: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/harness/user/datafile.html
.. _REST: http://wwwin-pyats.cisco.com/cisco-shared/rest/connector/latest/
.. _Triggers: https://wiki.cisco.com/display/GENIE/Triggers+Availability+in+Genie+SDK
.. _Verifications: https://wiki.cisco.com/display/GENIE/Verifications+Availability+in+Genie+SDK
.. _example: http://wwwin-genie.cisco.com/cisco-shared/genie/latest/installation/example.html
.. _portal: http://wwwin-genie.cisco.com/
.. _genie: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/
.. _Virl: https://wiki.cisco.com/display/GENIE/VIRL+Instructions+Genie+Examples
