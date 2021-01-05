August 2017
===========

August 31th - Genie v2.1.0
--------------------------

Today, we are pleased to announce the release of Genie v2.1 with Genie SDK,
providing over 35+ Triggers and 60+ Verifications, featuring a collection of
base class templates, examples and guidelines for modelling devices, features
and testcases.   

Genie is the highly anticipated Python implementation of BEST that Cisco
engineers have been waiting for! Its modular designs enables the core
components to be used independently or collectively within pyATS testscripts
and/or testcases.

The core components of Genie include:

**Genie Conf**
configures topology through Python objects, using a common structure compatible
with all OS and management interfaces such as CLI/Yang/REST. 

**Genie Ops**
represents the operational state through object attributes. Just like Genie
Conf, Genie Ops is compatible with all operating systems and Management
Interfaces, supporting a variety of parsing technologies.

**Genie SDK**
provides engineers with a self-contained test library (a pool of triggers and
verifications) that, when combined, create numerous testcases and test
scenarios on any topology and configuration.

**Genie Harness**
fuses pyATS infrastructure with Genie Conf, Ops, and its SDK to
create a generic test automation framework, which promotes the Event Driven
testing paradigm.   

Genie aligns with Cisco's The.Network.Intuitive vision of providing a network
infrastructure that is fully programmable, frequently optimized and supports
digitalized applications to become inherently network's aware.

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 2.1.0                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

    cd $VIRTUAL_ENV/projects/genie_libs
    git pull origin master

    cd $VIRTUAL_ENV/projects/parser
    git pull origin master

Features:
^^^^^^^^^

**Genie_libs enhancements**

* Extended Object Models with BGP, Interface, HSRP, Mcast, Route-Map and
  VLAN.
* Extended the SDK Trigger and Verification(NX/XR/XE) to support above
  features: 

   * Clear
   * ShutNoShut
   * DisableEnable
   * UnconfigConfig
   * Modify
   * AddRemove
   * Sleep

* Added support for REST to the existing management interface (Cli, XML, YANG (Native, Openconfig)).  
* Extended Genie sample usecase section to showcase REST, CLI, XML, YANG and OpenConfig.  

**Genie infrastructure enhancements**

* Dynamically inject pre/post processors through datafiles
* Dynamically add/remove common setup subsections via datafiles
* Drive triggers/verifications input parameters via datafiles
* Data files are now schema-validated for errors
* Removed dependency to Tcl and TCL-ATS

For more information, make sure to go through the genie_ documentation.

August 9th
----------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 2.0.7                         |
+-------------------------------+-------------------------------+


Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

Also make sure you upgrade `genie_libs` and `parser` to the latest version.

.. code-block:: bash

    cd $VIRTUAL_ENV/projects/genie_libs
    git pull origin master

    cd $VIRTUAL_ENV/projects/parser
    git pull origin master

Features:
^^^^^^^^^

* Enhancement to for REST buffer. There was an issue where the buffer was too
  small for large configuration.
* Enhancement in maker code.

For more information, make sure to go through the genie_ documentation.

And make sure to visit our new ``Genie`` portal_.

.. _sections: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/harness/developer/subsections.html#using-subsections
.. _schemas: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/harness/user/datafile.html
.. _REST: http://wwwin-pyats.cisco.com/cisco-shared/rest/connector/latest/
.. _Triggers: https://wiki.cisco.com/display/GENIE/Triggers+Availability+in+Genie+SDK
.. _Verifications: https://wiki.cisco.com/display/GENIE/Verifications+Availability+in+Genie+SDK
.. _example: http://wwwin-genie.cisco.com/cisco-shared/genie/latest/installation/example.html
.. _portal: http://wwwin-genie.cisco.com/
.. _genie: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/
