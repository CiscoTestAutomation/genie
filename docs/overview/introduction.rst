.. _intro:

Introduction
============

``Genie`` is a Python library which contains all the tools needed for
Networking Test Automation.  Genie is the library solution for :pyats:`pyATS
<http>`.  The main goals of Genie is to facilitates rapid development,
encourage re-usable libraries and simplify writing test automation.

Genie leverages all of Python's perks in an object-oriented fashion, to most notably: 

1. Empower engineers to develop agnostic libraries and scripts equipped to
   handle the different OS/platform/feature/release and Management Interfaces
   without having to develop new script/library each time;

2. Enable community driven-development and promote efficiency by allowing
   engineers to share their work with other teams; and 
	
3. Encourage teams to re-use existing libraries in their automation.

Genie strategically uses :abstractiontokens:`abstraction tokens <http>`
and lookup algorithms to achieve these new, innovative results.

Genie libraries are open source and hosted at:

* :genielibs_repo:`genie.libs.(conf/ops) <http>`
* :parser_repo:`genie.libs.parser <http>`
* :telemetry_repo:`genie.libs.telemetry <http>`


The Motivation behind Genie
----------------------------

* pyATS provides the core but what about the libraries to
  * Parse device
  * Configure device
  * Action on the device
  * Regroup testcases into sharable re-usable testcases

* pyATS gives you all the tools to write your automation and guidelines
  * Writing script which are future proof is hard
* No need to re-invent the wheel. Have 1 libraries which contains all the
  functionalities.

Genie tackle this head on and create packages, libraries and convention on how
to write these and share them!

Architectural limitations are a recurrent issue for engineers working in
automation development. For instance, scripts with embedded static
configurations or specific TGN interfaces are difficult to develop and nearly
impossible to use on any other operating system, platform, release, or branch,
other than those for which they were initially intended.

These architectural limitations also hinder collaboration among teams by
preventing them from sharing their libraries with one another. 

To overcome these architectural limitations, engineers have traditionally
devoted significant time and energy to re-develop their existing libraries.
This traditional approach typically relies on outdated namespaces, functions,
and argument-driven coding techniques. 

Package overview
----------------

* Genie has 4 main functionalities:

  * Configure devices in an OS implementation agnostic way
  * Retrieve device operation state in an OS implementation agnostic way
  * Pool of libraries to re-use which includes Testcases.
  * Test Harness which ties it all together.


The fundamental four core objects of Genie include:

1. **Genie Conf**: Configures topology through Python object attributes,
   featuring a `common object structure <genie_libs/index.html>`_. These
   object's structures are compatible with all operating systems and Management
   Interfaces (such as CLI/Yang/REST, etc.). These structures represents the
   feature, not a specific implementation on an operating system.  As such,
   scripts can use these objects to configure their device, do some
   configuration changes and expect it to work across all their operating
   system, management interfaces. (Depending on libraries availabilities).

2. **Genie Ops**: Represents the operational state of the feature through
   object attributes, featuring a `common object structure <genie_libs/index.html>`_.
   Just like Genie Conf, Genie `Ops` is compatible with all operating systems
   and Management Interfaces. 

3. **Genie SDK**: provides engineers with a set of `test library <genie_libs/index.html>`_
   (a pool of triggers and verifications) that, when combined, create numerous
   testcases and test scenarios on any topology and configuration.
   Additionally, Genie `SDK` contains diverse libraries for triggers and
   verifications development.
   
4. **Genie Harness**: Genie Harness fuses pyATS
   infrastructure with Genie Conf, Genie Ops, and Genie SDK to create a generic
   test automation framework, which promotes the **Event Driven** testing
   paradigm. Instead of writing Testscript, testscript are built by choosing 
   Triggers, Verification from the SDK pools or your own pool of testcases.
   Genie Harness provides many features to enhance your testing, for example:
   Traffic generator integration, applying configuration on the device,
   Profiling the system to make sure only expected fields have been changed.

Importantly, the innovative modular design of the Core Components means they
may be used independently or collectively in pyATS testscripts and/or
testcases.

.. note::

    Genie empowers engineers to write agnostic libraries and scripts
    capable of handling a variety of differences between
    os/platform/feature/release and management interface, etc.

High-Level Features
-------------------

* **Agnostic**: Relying on the :ref:`Abstract <abstract>` module,
  Genie is interoperable, working among various operating systems, platform
  devices, and Mangement Interfaces. 

* **Dynamic**: Genie automatically locates the topology, configuration, and
  operational state of the operating system to construct the essential
  feature/platform/interface objects. 

* **Efficient**: Genie drastically reduces run times and development time.

* **Parser Independent**: Using the :ref:`MetaParser <metaparser>` module,
  Genie is completely independent from the backend parser libraries
  (CLI/Yang/REST/XML/...).

* **Portable and Flexible**: Genie is entirely deployable on any
  testbed, it seamlessly handles diverse topologies and configurations. 

* **YANG Compatible**: Wherever possible, Genie ``Conf`` and Genie
  `Ops` follow the YANG model structure to provide a robust, ready-to-use, set
  of libraries for YANG-based testing. 

* **Extensible**: The low coupling, modularity and high cohesion properties of
  Genie makes it prefect infrastructure for feature, and web application
  testing. 

Design Overview
---------------

.. toctree::
    :maxdepth: 1

    design/story
    design/design
