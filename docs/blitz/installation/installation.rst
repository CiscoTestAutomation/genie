Installation
============
This page contains all the documentation needed to install *Blitz*

Requirements
------------
* Python virtual environment
* pyATS and Genie installed within the Python virtual environment

Installation Steps
------------------
#. Source the virtual environment. An example is below: ::

        source pyats/bin/activate

#. Install the *Blitz* package with **one** of the two following options:

 A. If pyATS is **not installed**, install everything required with: ::

        # For external users
        pip install pyats[full]

        # For internal users
        pip install ats[full]

 B. If pyATS is **already installed**, then install just `genie` with: ::

        pip install genie


