Usage
=====
This page contains all the documentation needed to use `GenieClean`.
There are two different methods of using `GenieClean` - Standalone or Integrated.

Prerequisites
-------------
* sourced pyATS virtual environment
* testbed yaml
* clean yaml

.. note::

    You can find clean templates for different usage types :ref:`here<base_clean_files>`.

Integrated
----------
Running `GenieClean` integrated with pyATS scripts is perfect if a user wants
to run a script on a testbed but wants to ensure the testbed has the correct
image and configuration.

Once you have both the testbed yaml and clean yaml then run this command::

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --clean-file /path/to/clean.yaml --invoke-clean

Standalone
----------
Running `GenieClean` as a standalone should be used if a user only wants
to clean devices. For example a developer may want to test features or
start developing but they need a cleaned device first.

Once you have both the testbed yaml and clean yaml then run this command::

    kleenex -testbed_file=/path/to/testbed.yaml -clean_file=/path/to/clean.yaml

.. note::

    pyats clean --testbed-file /path/to/testbed.yaml --clean-file
    /path/to/clean.yaml will be added next release

Clean Schema Validation
-----------------------
To validate

Once you have both the testbed yaml and clean yaml then run this command::

    pyats validate clean --testbed-file /path/to/testbed.yaml --clean-file /path/to/clean.yaml
