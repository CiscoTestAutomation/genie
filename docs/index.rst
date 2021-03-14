Genie Documentation
===================

.. figure:: genie.png
    :align: center

.. sidebar:: Quick References

    - :ref:`Installation<book_genie>`
    - :ref:`Explore Genie<cookbook>`
    - :mailto:`Contact us <cisco.com>`

``Genie`` is the :pyats:`pyATS <http>` **SDK** which contains all the tools
needed for Network Test Automation. Genie bundled with the modular architecture
of the :pyats:`pyATS <http>` framework accelerates and simplifies development
of network test automation, while leveraging all the perks of the Python
programming language and promoting the development of agnostic libraries. Genie
is redefining how network test scripters interact with devices through
libraries and avoiding functional programming.

.. code-block:: python

    # Import Genie
    from genie import testbed

    # Look at the bottom for an example of a testbed file
    testbed = testbed.load('testbed.yaml')

    # Find the device I want to connect to
    device = testbed.devices['nx-osv-1']

    # Connect to it
    device.connect()

    # Parse device output
    output = device.parse('show version')

    # Print it nicely
    import pprint
    pprint.pprint(output)

    {'platform': {'hardware': {'bootflash': '3184776 kB',
                               'chassis': 'NX-OSv Supervisor Module',
                               'device_name': 'nx-osv-1',
                               'model': 'NX-OSv',
                               'processor_board_id': 'TM00010000B',
                               'slots': 'None'},
    ...

.. note:: 

    :ref:`More information on the testbed file<book_setup_testbed>`

Genie is used internally within Cisco for automating network testing and has
also been released externally through Cisco :devnet:`DevNet <http>`. This means
that the same tests which are used internally at Cisco during product
development can also be executed externally on a customer setup. This is
massive news for automation within and outside of Cisco!

**Don't even need to know python to re-use its functionalities; Can be used directly in bash**

.. code-block:: bash

    genie parse "show version" --testbed-file testbed.yaml --devices nx-osv-1 --output explore1
    +==============================================================================+
    | Genie Parse Summary for nx-osv-1                                             |
    +==============================================================================+
    |  Connected to nx-osv-1                                                       |
    |  -  Log: explore-1/connection_nx-osv-1.txt                                   |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show version'                                               |
    |  -  Parsed structure: explore-1/nx-osv-1_show-version_parsed.txt             |
    |  -  Device Console:   explore-1/nx-osv-1_show-version_console.txt            |
    |------------------------------------------------------------------------------|


**Genie at a glance**

* :parsers:`2700+ Parsers that supports all OS<http>`
* :models:`Feature-centric object models<http>`
* Provides structured data by parsing devices configuration and operation data
  which are fully OS Agnostic (One common structure for all OS/Interface
  management)
* Apply configuration on all Cisco devices using a common structure for all
  OS/Platform/Cli/Yang
* :ref:`Test Harness <harness_overview>` to generate testscript and re-use
  existing :testcase:`testcases <http>`
* :genietelemetry:`Testbed Health Status Monitoring <http>` - Supports any
  pyATS script and can also be used as a standalone tool
* Ansible and Robot libraries https://developer.cisco.com/docs/pyats/#!integration-to-other-frameworks

-----------------------------------------------------------------------------------

.. toctree::
    :maxdepth: 1
    :caption: Getting started

    overview/introduction
    installation/installation
    cookbooks/index


.. toctree::
    :maxdepth: 1
    :caption: Documentation
    :titlesonly:

    userguide/index
    pyATS Clean <clean/index>
    blitz/index
    health/index
    cli/index
    solutions/index
    Internal Documentation <https://wiki.cisco.com/pages/viewpage.action?pageId=831194226>

.. toctree::
    :caption: Library
    :maxdepth: 1

    Available APIs <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>
    Available Clean Stages <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean>
    Available Models (Conf/Ops) <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models>
    Available Parsers <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>
    Available Triggers <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/triggers>
    Available Verifications <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/verifications>

.. toctree::
    :caption: Developer Docs
    :maxdepth: 1
    
    abstract/index
    metaparser/index
    parsergen/index
    predcore/index

.. toctree::
    :caption: Reference
    :maxdepth: 1

    roadmap/index
    changelog/index

.. _pyATS: https://developer.cisco.com/pyats/

