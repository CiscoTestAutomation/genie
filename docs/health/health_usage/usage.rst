Usage
=====
This page contains all the documentation needed to use `pyATS Health Check`.
Currently, `pyATS Health Check` is only supported via integrated mode (run via pyATS job). `Standalone` mode and more are coming in a future release!

Prerequisites
-------------
* sourced pyATS virtual environment
* testbed yaml
* health yaml

Integrated
----------
Running `pyATS Health Check` integrated with pyATS scripts is the way if a user wants to collect and monitor device status on a testbed through a pyATS job.

just add `--health-checks` then run this command::

    pyats run job <job file> --testbed-file <testbed file> --health-checks cpu memory logging core

Or once you have both the testbed yaml and health yaml for custom health checks then run this command. URL with token can be given like below example::

    pyats run job <job file> --testbed-file <testbed file> --health-file /path/to/health.yaml
    pyats run job <job file> --testbed-file <testbed file> --health-file "http://<url>/health.yaml"
    pyats run job <job file> --testbed-file <testbed file> --health-file "http://<token>@<url>/health.yaml"

.. note:

    `cpu`, `memory`, `logging` and `core` checks are pre-defined in /path/to/genielibs/pkgs/health-pkg/src/genie/libs/health/health_yamls/pyats_health.yaml. `--health-checks` uses this default pyats health file.

Standalone
----------
Coming in a future release.

pyATS Health Check YAML Validation
----------------------------------
To validate

Once you have a pyats health check yaml then run this command::

    pyats validate datafile /path/to/health.yaml
    pyats validate datafile "http://<url>/health.yaml"

pyATS Health Check Examples
---------------------------

pyATS Health Check examples can be found in our `Github repo
<https://github.com/CiscoTestAutomation/examples/tree/master/health>`_. 

Here is how to leverage those example for your case.
Let's look at `cpu/memory custom check
<https://github.com/CiscoTestAutomation/examples/tree/master/health/cpu_memory_custom_check>`_.

This example will check CPU load and Memory usage for BGP processes. If multiple processes are hit by regex `BGP.*`. The result value will be returned each process's cpu load percentage as python dictionary. (This behavior depends on which API is used)

All the examples has device `uut` or something else. To use these examples for your device, what you need to do is to change device name to yours. Device name or alias in testbed yaml needs to be given to the `device`.

And for `memory` section, added `OSPF.*` regex to select OSPF related processes addition to BGP ones. Based on API arguments, contents of pyATS Health Check are very customizable/flexible.

Most of Blitz actions support `include`/`exclude` to indicate what the criteria is for the action. In below case, by using `Dq`, `sum_value_operator('value', '<', 90)` means that sum up returned each process's percentage from API is expected to be less than 90.

.. code-block:: yaml

  pyats_health_processors:
    source:
      pkg: genie.libs.health
      class: health.Health
    test_sections:
      - cpu:
          - api:
              device: ASR1K-1 # <<< changed from `uut`
              function: health_cpu
              arguments:
                processes: ['BGP.*']
              include:
                - sum_value_operator('value', '<', 90)
      - memory:
          - api:
              device: ASR1K-1 # <<< changed from `uut`
              function: health_memory
              arguments:
                processes: ['BGP.*', 'OSPF.*']
              include:
                - sum_value_operator('value', '<', 90)

By default, pyATS Health Check will run these health checks every testcase/section. You might want to narrow down where pyATS Health Check runs. For example, above example is checking BGP processes CPU/Memory. So, let's narrow down to run only for related testcases/section.

.. code-block:: yaml

  pyats_health_processors:
    source:
      pkg: genie.libs.health
      class: health.Health
    test_sections:
      - cpu:
          - api:
              device: ASR1K-1
              function: health_cpu
              arguments:
                processes: ['BGP.*']
              include:
                - sum_value_operator('value', '<', 90)
              health_tc_groups: '.*bgp.*' # <<< use regex to match any BGP processes
      - memory:
          - api:
              device: ASR1K-1 # <<< changed from `uut`
              function: health_memory
              arguments:
                processes: ['BGP.*', 'OSPF.*']
              include:
                - sum_value_operator('value', '<', 90)
              health_tc_sections: 'bgp_full_route_check' # <<< specify exact section name

For `cpu` action, `health_tc_groups: '.*bgp.*'` is given to run the action only for testcases which the regex `.*bgp.*` match its group.
For `memory` action, `health_tc_sections: 'bgp_full_route_check'` is given. Exact section name without regex is provided, so the `memory` action will run only for the exact same section name but effective for all the testcases. Please check for the detail of pyATS Health Check arguments `health_tc_uids`/`health_tc_groups`/`health_tc_sections` from :ref:`Selecting Testcase/Section<select_testcase_section>`

pyATS Health Check is very flexible because you can leverage any features in Blitz. You can create your own Health Check by using any of the Blitz feature, give it a try! `Quick Trigger (Blitz)
<https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writeblitz/writeblitz.html>`_.

The examples repo is open-sourced. Any contributions for pyATS Health Check examples are encouraged!