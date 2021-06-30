.. _book_genie:

.. raw:: html

   <h2>Genie FAQs</h2>

1. External Parsers / APIs
--------------------------

Genie Library is Open Source
This is a general reminder that Genie Library is open source.

Within Cisco, the development of Genie Libs happen at in the internal GitHub repo:

Parsers: https://wwwin-github.cisco.com/pyATS/genieparser
Triggers, Verifications, APIs, etc: https://wwwin-github.cisco.com/pyATS/genielibs


And an equivalent mirror externally for the open-source community on public GitHub:

https://github.com/CiscoTestAutomation/genieparser
https://github.com/CiscoTestAutomation/genielibs

The content of the repos are the exact same - just the ref points (commits) and branching history is different at the moment. 

As part of the Cisco Engineering team, you should be using only the internal repo for commits. This gives pyATS/Genie maintenance team the opportunity to review and/or remove any sensitive materials before it gets pushed to the external mirror.

Confidential/Sensitive Content:
```````````````````````````````

Often times you may need to create new Parsers and APIs in the Genie Library for the next release, or a new feature that is not yet publicly announced/ready. In such cases, do not publish your library contributions to the official Genie repo! 

Commit your private libraries elsewhere, and use the Genie library override mechanism to "include" these local/private libraries as part of the standard Genie library runtime - as if they were all co-located within the same sources.

This mechanism is provided as a standard for Polaris DevAT test automation - a local package location is pre-created and pre-loaded for you as part of `activating your Polaris DevAT environment <https://cisco.sharepoint.com/sites/PolarisDevAT/SitePages/SDK%20Knowledge%20bank.aspx#option-1-using-devat-activate-script>`_.

What is an external parser/api?
```````````````````````````````

In short, they are parsers and apis which have been contributed to Genie that are not yet ready for open-source releases.


Where to store local Genie Parsers/API for SDK?
```````````````````````````````````````````````

Under `$BINOS_ROOT/atests/cisco/pyats/libs/genie/`:
    
Use the following folders for override/private/local parsers:

    For local parser: external_parser
    For local api: external_api


Step-By-Step Guide For Local Genie Library Implementation:
``````````````````````````````````````````````````````````

1. Under $BINOS_ROOT/atests/cisco/pyats/libs/genie, make sure the "external_parser" and "external_api" folders are created - depending on which one you are implementing

.. code-block:: bash

    # $BINOS_ROOT is the path to polaris binos folder eg: /nobackup/<CEC ID>/polaris/binos

    mkdir -p $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser
    mkdir -p $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_api


2. Create __init__.py under the root folder (if it doesn't exist)

.. code-block:: bash

    # the following example is for parsers - follow the same steps for external_api folder
    cd $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser
    vim __init__.py

    # inside the __init__.py file
    # declare the package with genie abstract
    from genie import abstract
    abstract.declare_package(__name__)


3. Create specific os subfolder under root folder

.. code-block:: bash

    # the following example is for parsers - follow the same steps for external_api folder

    # eg, for iosxe parser
    mkdir iosxe
    cd iosxe/

    # for c9300 platform under iosxe
    mkdir -p iosxe/c9300


4. Create __init__.py under the os folder (and platform) folder

.. code-block:: bash

    # the following example is for parsers - follow the same steps for external_api folder

    cd iosxe/
    vim __init__.py

    # inside the __init__.py file
    # declare the device os token with genie abstract
    from genie import abstract
    abstract.declare_token(__name__)

    # do the same for platform folder
    cd c9300/
    vim __init__.py

    # declare the device platform token with genie abstract
    from genie import abstract
    abstract.declare_token(__name__)


5. Create or overwrite libraries under the corresponding os folder
        
    Refer to the official Genie documentation for how to develop parsers and apis:
        how to write a parser:  https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writeparser/writeparser.html
        genie parser github repo: https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser
        current available parsers: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers
        
    Refer to the following links to write apis:
        api guideline: https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/apis/index.html
        genie api github repo: https://github.com/CiscoTestAutomation/genielibs/tree/master/pkgs/sdk-pkg/src/genie/libs/sdk/apis
        current available apis: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis

    
External parser tree structure example:

.. code-block:: bash

    # inside $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser
    .
    ├── __init__.py
    ├── iosxe
    │   ├── __init__.py
    │   ├── c9300
    │   │   ├── __init__.py
    │   │   └── show_platform.py
    │   └── show_clock.py
    └── iosxr
        ├── __init__.py
        └── show_clock.py

    
6. Export the parser root folder name and path to environment variable PYATS_LIBS_EXTERNAL_PARSER and PYTHONPATH or use pyats.conf file to include the external package
NOTE: this is already done for you if you are using the `DevAT Activate Script <https://cisco.sharepoint.com/sites/PolarisDevAT/SitePages/SDK%20Knowledge%20bank.aspx#option-1-using-devat-activate-script>`_.

    a. use environment variable

    .. code-block:: bash
            
        export PYTHONPATH=$BINOS_ROOT/atests/cisco/pyats/libs/genie:$PYTHONPATH
        export PYATS_LIBS_EXTERNAL_PARSER='external_parser'
        export PYATS_LIBS_EXTERNAL_API='external_api'

    b. use pyats.conf file, this file is located at ~/.pyats/ folder, if you don't have it, please create one

    .. code-block:: bash

        export PYTHONPATH=$BINOS_ROOT/atests/cisco/pyats/libs/genie:$PYTHONPATH

        cd ~/.pyats/
        vim pyats.conf

        # Inside pyats.conf file, add the following settings
        [pyats.libs]
        external.parser = external_parser
        external.api = external_api

And that's it! From here onwards, you should be able to use these libraries.

    
Using Local/Private/Overwrite Genie Libraries:
``````````````````````````````````````````````
When following the above steps, your local override/private libraries (part of the external_api/parser folder) should be automatically picked up by Genie library infrastructure. These "overrides" will work as if they are directly part of the library system, no additional work necessary.

.. code-block:: bash

    # calling device parsers
    output = device.parse('show version')

    # calling device apis
    output = device.api.configure_cdp(...)
    
Follow the standard Genie library usage/guidelines for how apis and parsers are invoked.

https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/index.html#explore-genie


Do not importing them directly in your script as it will cause an ImportError since the parsers are not in your PYTHONPATH. That is, do not do the following:

.. code-block:: bash
        
    from cisco.pyats.libs.genie.external_parser.iosxe.some_useful_parsers import some_parser


Writing Unit Tests for Local/Private/Override Libraries:
````````````````````````````````````````````````````````
    
More information on unittests can be found here: `Unit Test Structure <https://wiki.cisco.com/display/PYATS/Unit+Test+Structure>`_.

Unittests are run with the `folder_parsing_job.py` file found in

.. code-block:: bash

    $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser/tests

It will run the tests found in the OS folders contained in there. Folder structure should follow this format: `Unit Test Structure#Breakdown <https://wiki.cisco.com/display/PYATS/Unit+Test+Structure#UnitTestStructure-Breakdown>`_

.. code-block:: bash

    .
    └── tests/
        └── <OS>
            └── <Class Name>/
                └── cli/
                    ├── empty/
                    │   └── empty_output_output.txt
                    └── equal/
                        ├── <golden_output>_output.txt
                        └── <golden_output>_expected.py

    
To run all unittests, run these commands

.. code-block:: bash

    cd $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser/tests
    pyats run job folder_parsing_job.py -e $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser


Subsets of unittests can be run as well like so:

.. code-block:: bash

    ## Run a specific OS
    cd $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser/tests
    pyats run job folder_parsing_job.py -e $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser -o <OS>

    ## Run a specific class
    cd $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser/tests
    pyats run job folder_parsing_job.py -e $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser -c <CLASS_NAME>


Note: If `folder_parsing_job.py` doesn't exist, you can create it with

.. code-block:: bash

    cd $BINOS_ROOT/atests/cisco/pyats/libs/genie/external_parser/tests
    echo "from genie.libs.parser.utils.unittests import main" > folder_parsing_job.py


Promoting Libraries/Getting Ready For Official Release:
```````````````````````````````````````````````````````

Local libraries (eg, external_api and external_parser) that are not part of main Genie release should be considered as a limited-use feature: do not abuse it for non-reason. At the end of the day, if it's not part of the primary Genie library release, it should be viewed as a technical debt.

It is the responsibility of the original code author/team to make sure a patch/local/override library piece makes it to the official Genie library release. 

The following matrix gives you a high-level guideline of what to do in case you are:

    1. Using local libs for a quick-turnaround time to commit your script without waiting for official Genie release
        a. For all your local additions/modifications, create official Pull Request to Genie repositories in the corresponding `internal Genie GitHub repo <https://wwwin-github.cisco.com/pyATS/genieparser>`_ (eg for parsers).
        b. You are responsible of ensuring that your code changes and PR follows the library development guidelines, rules, and passes the Genie PR process, merging into the next release as-soon-as-possible.
        c. When the next SDK release is ready (and includes your changes in the SDK's Genie library version), raise a new PR to Polaris-Git and remove your local/override library/parser file.
        
    2. Using local libs for next-release/sensitive new features
        a. Continue using the Polaris Github feature development/throttle branch during the R&D phase of this feature
        b. After release CCO (eg, available for customers and no longer sensitive), you are responsible of taking all the internal libraries you've developed, and commit them to official Genie library through the standard PR process.
        c. When the next SDK release is available, 'polaris-dev' branch should include your changes, and you can raise a PR to Polaris-Github to remove your overrides.

    
In summary:

    - make sure your local overrides are eventually pushed to Genie mainstream library set, as soon as possible.
    - as a good developer, you are responsible of releasing your changes

    
The general Genie contribution guidelines are avaialble at: https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/contribute/contribute.html#


Release Handling In Libraries:
``````````````````````````````

Genie library abstraction system has built-in support for OS/platform and release variants. 

For example, you can introduce the following structure:

.. code-block:: bash

    genie/libs/parsers/
    genie/libs/parsers/iosxe
    genie/libs/parsers/iosxe/asr1k
    genie/libs/parsers/iosxe/asr1k/17_7

Note that you cannot use a DOT(.) in python module name, and since Genie abstraction requires modules that are at least importable, use underscore _ to substitute release numbers.

In the above example, you can create 17.7 release specific parsers that extend existing (default) parsers for iosxe/asr1k. 
