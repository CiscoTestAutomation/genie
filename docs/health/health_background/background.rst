.. _Background-health-check:

Health Check Background
=======================

pyATS Health Check Background is a similar, nearly identical functionality to the traditional health check. However, where health check only runs in the post-processor section of a job, Health Check Background will run continously parallel to the job.

Usage
-----
This page contains all the documentation needed to use `pyATS Health Check Background`.
Currently, `pyATS Health Check Background` is only supported via integrated mode (run via pyATS job).

Prerequisites
-------------
* sourced pyATS virtual environment
* testbed yaml
* health yaml (optional)

Integrated
----------
Running `pyATS Health Check Background` integrated with pyATS scripts is the way to collect and monitor device status on a testbed through a pyATS job.

just add `--health-bg-checks` to your `pyats run job` command::

    pyats run job <job file> --testbed-file <testbed file> --health-bg-checks cpu memory logging core

For more advanced users, you are able to provide your own health yaml file. This can be provided with the `--health-bg-file` argument like so::
URL with token can be given like below example.

    pyats run job <job file> --testbed-file <testbed file> --health-bg-file /path/to/health.yaml --health-bg-checks cpu memory logging core
    pyats run job <job file> --testbed-file <testbed file> --health-bg-file "http://<url>/health.yaml" --health-bg-checks cpu memory logging core
    pyats run job <job file> --testbed-file <testbed file> --health-bg-file "http://<token>@<url>/health.yaml" --health-bg-checks cpu memory logging core

In case of URL, token for http can be given like below:

    pyats run job <job file> --testbed-file <testbed file> --health-bg-file "http://<token>@<url>/health.yaml" --health-bg-checks cpu memory logging core

.. note:

    `cpu`, `memory`, `logging` and `core` checks are pre-defined in /path/to/genielibs/pkgs/health-pkg/src/genie/libs/health/health_yamls/pyats_health.yaml. `--health-bg-checks` uses this default pyats health file.


Identical to Health Check
-------------------------
Everything you can do in pyATS Health Check you can also do in Health Check Background. It has been built off of it to allow for a familiar experience and ease of use. This includes the health yaml file as well. It has been designed so that you can take your health yaml file and seemlessly use it with Health Check Background. The only major difference between the two functionalities is when they run. Health Check Background will constantly run throughout the entirety of the job, while Health Check will only run after each task has been completed.

Arguments
---------

Here is a list of arguments to use Health Check Background

.. list-table::

    * - Argument 
      - Description
      - Example
    * - --health-bg-file
      - Specify background health.yaml file
      - **--health-bg-file health_check.yaml**
    * - --health-bg-interval-time
      - Specify background sleep interval per process in seconds
      - **--health-bg-interval-time cpu:30 memory:60**
    * - --health-bg-devices
      - Specify background device connection
      - **--health-bg-devices uut uut2 uut3**
    * - --health-bg-checks
      - Specify checks to run
      - **--health-bg-checks cpu memory core logging**
    * - --health-bg-config
      - Specify pyATS Health Check configuration yaml file
      - **--health-bg-config health_config.yaml**
    * - --health-bg-connection
      - Specify pyATS Health Check testbed connection (Cannot be console connection)
      - **--health-bg-connection ssh**
    * - --health-bg-v
      - (1) Print Blitz information to stdout. (2) Print command output to stdout
      - **--health-bg-v**

This information can also be found by running `pyats run job --help`

Examples
--------
Get cpu and memory information::

    pyats run job job.py --health-bg-check cpu memory

Run cpu check every 30 seconds and memory check every 60 seconds::

    pyats run job job.py --health-bg-check cpu memory --health-bg-interval cpu:30 memory:60

Use ssh connection on devices::

    pyats run job job.py --health-bg-check cpu memory --health-bg-connection ssh

Run bg health on only uut::

    pyats run job job.py --health-bg-check cpu memory --health-bg-devices uut

Supply a custom health.yaml file::

    pyats run job job.py --health-bg-check cpu memory --health-bg-file health.yaml