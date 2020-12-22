Installation
============
This page contains all the documentation needed to install `pyATS Health Check`

Requirements
------------
* Python virtual environment
* pyATS and Genie installed within the Python virtual environment

Installation Steps
------------------
#. Source the virtual environment. An example is below: ::

        source pyats/bin/activate

#. Install the `pyATS Health Check` package with **one** of the two following options:

 A. If pyATS is **not installed**, install everything required with: ::

        # For external users
        pip install pyats[full]

        # For internal users
        pip install ats[full]

 B. If pyATS is **already installed**, then install just `pyATS Health Check` with: ::

        pip install genie.libs.health


