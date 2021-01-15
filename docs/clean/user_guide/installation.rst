.. _clean_doc_how_to_install:

Installation
============

This page contains all the documentation needed to install `pyATS Clean` for users.

Requirements
------------
* Python virtual environment

Installation Steps
------------------
#. Source the virtual environment. An example is below: ::

    source path/to/virtual/env/bin/activate

#. Install pyATS packages: ::

    # For non-cisco employees
    pip install pyats[full]

    # For cisco employees
    pip install ats[full]

Upgrading Steps (existing installation)
---------------------------------------
If pyATS Clean is already installed but you have an old version, follow the steps below to upgrade.

#. Source the virtual environment where pyATS is already installed. An example is below: ::

    source path/to/virtual/env/bin/activate

#. Upgrade pyATS packages to the latest version: ::

    # For non-cisco employees
    pip install --upgrade pyats[full]

    # For cisco employees
    pip install --upgrade ats[full]
