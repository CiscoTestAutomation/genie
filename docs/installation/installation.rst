.. _installation:

Installation
============

Requirement
-----------

* ``Genie`` requires :pyats:`pyATS <http>` to be installed.
* It is highly recommended to install Genie and pyATS within a virtual environment. (Cisco engineers get this automatically with pyATS installation script).
* **Cisco only** make sure to request :permission:`permission <http>` to bitbucket.

Installation & Upgrade
----------------------

Within your virtual environment:

If you dont have pyats installed, this will install both pyats and genie:

.. code-block:: bash

    pip install pyats[library]

Or run this if pyats is already install in your environment:

.. code-block:: bash

    pip install genie

.. note::

   For Cisco employee, you might need to source the proxy first
   source /auto/pyats/bin/lab_proxy.csh (or .sh if bash)
 

This will install the follow packages:

    +-----------------------------+------------------------------------------------+
    | Genie packages              | Description                                    |
    +=============================+================================================+
    | genie                       | Genie main package                             |
    +-----------------------------+------------------------------------------------+
    | genie.libs.conf             | Libraries containing Conf objects              |
    +-----------------------------+------------------------------------------------+
    | genie.libs.ops              | Libraries containing Ops objects               |
    +-----------------------------+------------------------------------------------+
    | genie.libs.sdk              | Libraries containing Triggers, Verification    |
    |                             | and harness related                            |
    +-----------------------------+------------------------------------------------+
    | genie.libs.parser           | Libraries containing all the parsers           |
    +-----------------------------+------------------------------------------------+
    | genie.libs.robot            | Robot Library to interact with Genie           |
    +-----------------------------+------------------------------------------------+
    | genie.libs.filetransferutils| Library for file transfer operations on device |
    +-----------------------------+------------------------------------------------+
    | genie.telemetry             | Infrastructure for Telemetry                   |
    +-----------------------------+------------------------------------------------+

You are good to go :ref:`explore Genie<cookbook>`

.. _structure:

Code Structure
--------------

Genie code base is divided into two sections:

- Infrastructure 
- Feature libraries & SDK

Infrastructure
^^^^^^^^^^^^^^

The **infrastructure** is the core and baseclass of Genie and is released via
pip packages. For any question :mailto:`contact us <cisco.com>`.

Feature libraries & SDK
^^^^^^^^^^^^^^^^^^^^^^^

The **feature libraries & SDK** are user-community owned and developed. When
installing Genie, all the libraries are automatically installed with the latest version.
To contribute to the library, do the following:

*Contribute to Genie Parser*

1. git clone :genieparsergitclone:`.git`
2. cd genielibs
3. make develop

*Contribute to Genie Libs*

1. git clone :genielibsgitclone:`.git`
2. cd genielibs
3. make develop

Once this steps are done, you can develop any changes and send pull request.
Here are some rough steps. No exact steps can be given as every scenario is
different. Make sure you are familiar with git.

.. code-block:: bash

    git checkout -b <branch name>                                                  
    # Do the modifications on the file(s)
    git add <file>
    git commit -m "some message explaining the  change"
    git push origin branch_name

.. note::

    Make sure to understand how :setuptools:`develop mode <http>` works for setuptools.

`genie.libs.parser` code can be found in `genieparser/src/genie/libs/parser/`

`Genie.libs` code is divided in 4 main parts

* `pkgs/ops-pkg/src/genie/libs/ops/` - Operational state object
* `pkgs/conf-sdk/src/genie/libs/sdk/` - Triggers and Verifications
* `pkgs/conf-pkg/src/genie/libs/conf/` - Configuring device with Python object
* `pkgs/conf-robot/src/genie/libs/robot/` - RobotFramework libraries for Genie

Support Mailer
--------------

For support, question and training :mailto:`contact us <cisco.com>`.



.. _bitbucket: https://wiki.cisco.com/display/PYATS/Bitbucket+Repositories
.. _genie_libs: https://bitbucket-eng-sjc1.cisco.com/bitbucket/projects/PYATS-PROJ/repos/genie_libs/browse
.. _ASG-Team: http://wwwin-asg.cisco.com
.. _PRRQ: http://wwwin-tools.cisco.com/prrq/viewQueue.do?queueName=pyats-xbu-shared
.. _abstract: http://wwwin-pyats.cisco.com/cisco-shared/abstract/html/
.. _permission: https://wiki.cisco.com/display/PYATS/Bitbucket+Repo#BitbucketRepo-BitbucketMembership
.. _SSH: https://wiki.cisco.com/display/PYATS/Bitbucket+Repo#BitbucketRepo-SSHKeys
.. _Developer wiki: https://wiki.cisco.com/display/GENIE/Commit+guidelines

.. _develop mode: http://setuptools.readthedocs.io/en/latest/setuptools.html#develop-deploy-the-project-source-in-development-mode
.. _Genie Support Team: asg-genie-support@cisco.com
.. _PieStack: http://piestack.cisco.com
.. _pyATS virtual environment: https://wiki.cisco.com/pages/viewpage.action?pageId=80375302
.. _metaparser: http://wwwin-pyats.cisco.com/cisco-shared/metaparser/html/
.. _abstract: http://wwwin-pyats.cisco.com/cisco-shared/abstract/html/
.. _parsergen: http://wwwin-pyats.cisco.com/cisco-shared/parsergen/html/
.. _commit: https://wiki.cisco.com/display/GENIE/Commit+guidelines
.. _coding: https://wiki.cisco.com/display/GENIE/Coding+Guidelines
.. _connection pool: http://wwwin-pyats.cisco.com/documentation/latest/connections/manager.html#method-start-pool
