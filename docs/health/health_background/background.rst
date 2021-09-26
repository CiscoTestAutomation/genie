.. _Background-health-check:

Background Health Check
=======================

pyATS Background Health Check is a similar, nearly identical functionality to the traditional health check. However, where health check only runs in the post-processor section of a job, background health check will run continously parallel to the job.

Usage
-----
This page contains all the documentation needed to use `pyATS Health Background Check`.
Currently, `pyATS Health Background Check` is only supported via integrated mode (run via pyATS job).

Prerequisites
-------------
* sourced pyATS virtual environment
* testbed yaml
* health yaml (optional)

Integrated
----------
Running `pyATS Background Health Check` integrated with pyATS scripts is the way to collect and monitor device status on a testbed through a pyATS job.

just add `--health-bg-checks` to your `pyats run job` command::

    pyats run job <job file> --testbed-file <testbed file> --health-bg-checks cpu memory logging core

Or once you have both the testbed yaml and health yaml for custom health checks then run this command::

    pyats run job <job file> --testbed-file <testbed file> --health-bg-file /path/to/health.yaml --health-bg-checks cpu memory logging core
    pyats run job <job file> --testbed-file <testbed file> --health-bg-file "http://path.to/health.yaml" --health-bg-checks cpu memory logging core

.. note:

    `cpu`, `memory`, `logging` and `core` checks are pre-defined in /path/to/genielibs/pkgs/health-pkg/src/genie/libs/health/health_yamls/pyats_health.yaml. `--health-checks` uses this default pyats health file.


Identical to Health Check
-------------------------
Everything you can do in pyATS Health Check you can also do in Background Health Check. It has been built off of it to allow for a familiar experience and ease of use. The only major difference between the two functionalities is when they run. Background Health Check will constantly run throughout the entirety of the job, while Health Check will only run after each task has been completed.

Arguments
---------

Here is a list of arguments to use background health

.. list-table::

    * - Argument 
      - Description
      - Example
    * - --health-bg-file
      - Specify background health yaml file
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
      - Specify pyATS Health Check testbed connection (Cannot be telnet)
      - **--health-bg-connection ssh**
    * - --health-bg-v
      - Increase output verbosity
      - **--health-bg-v**

This information can also be found by running `pyats run job --help`