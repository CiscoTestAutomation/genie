.. _health:

pyATS Health Check
==================
By using pyATS Health Check, it is possible to check the CPU load, memory usage, detection of specific log messages, and whether or not the core file created in the event of a crash or malfunction is generated.

pyATS Health Check currently supports the following 4 checks by default.

.. list-table::
   :header-rows: 1

   * - health check
     - description
   * - cpu
     - cpu load check. check total of cpu load with threshold 90% by default.
   * - memory
     - memory usage check. check total of memory usage with threshold 90% by default.
   * - logging
     - keyword check in show logging output. default keywords are traceback, Traceback, TRACEBACK
   * - core
     - check if core file is generated on device. just check by default. Please use `--health-remote-device` to copy the core file to remote server.

.. note:

    `cpu`, `memory`, `logging` and `core` checks are pre-defined in /path/to/genielibs/pkgs/health-pkg/src/genie/libs/health/health_yamls/pyats_health.yaml. `--health-checks` uses this default pyats health file.

Using pyATS Health Check is very easy. Just list the above heath check names by adding `--health-checks` to the current pyats command.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core

If you want to check only cpu, please specify `cpu` to `--health-checks`. **The pyATS Health Check specified by `--health-checks` runs as a post-processor after each test case.**

The core file is the only detection that is by default. If you want to send it to TAC for analysis or move it to the remote server at the time of detection, you can enumerate the remote server information with `--health-remote-device` to copy the generated core file. To copy the file at the time of detection and delete the file from the device, specify the --health-remote-device argument.

The command example in that case is as follows.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-remote-device name:myserver path:/tmp/ protocol:http --health-mgmt-vrf iosxe:None

Note that in order to run the above example you need to have the server `myserver` in testbed yaml as below.

.. code-block:: yaml

    testbed:
      name: general_xe_xr_nx
      servers:
        myserver:
          dynamic: true
          protocol: http
          subnet: 192.168.255.0/24
          path: /tmp
          credentials:
            default:
              username: pyats
              password: "<password>"

.. note::

    The above example uses `Embedded pyATS File Transfer Server <https://pubhub.devnetcloud.com/media/pyats/docs/utilities/file_transfer_server.html>`_.

You can find more examples in our `Github repo <https://github.com/CiscoTestAutomation/examples/tree/master/health>`_. Any contributions for pyATS Health Check examples are encouraged!

FAQ
---

**1. What kind of protocols are supported for core file transfer? And how to adjust to my remote server info?**

`http`, `scp`, `tftp` and `ftp` are supported. It depends on what is supported by `Multiprotocol File Transfer Utilities <https://pubhub.devnetcloud.com/media/pyats/docs/utilities/file_transfer_utilities.html>`_. 

If VRF for transfer needs to be changed from common default ones (`Mgmt-intf`, `management`), please change via `--health-mgmt-vrf` argument. for default VRF, needs to specify `None` like `iosxe:None`.

example when using tftp and vrf `mgmt` for both iosxe and nxos

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-remote-device name:myserver path:/tmp/ protocol:scp --health-mgmt-vrf iosxe:mgmt nxos:mgmt

**2. How to change threshold for cpu load/memory usage?**

It can be done via `--health-threshold` argument.

example when specifying thresholds, cpu 75% and memory 80%

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-threshold cpu:75 memory:80

**3. How can I change which logging keywords I want to detect?**

By default, `logging` check detects only `traceback`, `Traceback` and `TRACEBACK`. The keywords can be overwritten via `--health-show-logging-keywords`.

example when changing to `Crash` and `CRASH` for both iosxr and nxos.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-show-logging-keywords "iosxr:['Crash', 'CRASH']" "nxos:['Crash', 'CRASH']"

**4. I want to change the location of where core files are searched for**

by default, it's pre-defined for each platform (iosxe, iosxr, nxos). If you want to look somewhere else, the location can be overwritten via `--health-core-default-dir`.

example to change to `harddisk0:/core` for iosxe.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-core-default-dir "iosxe:['harddisk0:/core']"

**5. How to run pyATS Health check against only certain devices?**

All checks will run against all connected devices in testbed yaml by default. To run checks against only specific devices, please use `--health-devices`.

example to run against only `R1_xe` device.

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-devices R1_xe

**6. Is it possible to send a webex notification?**

Yes. There is `--health-webex` argument to send a webex notification. The webex notification will be sent out only when health checks fail.
Webex token and space id or email need to be given via pyats.conf or webex arguments `--webex-token`, `--webex-space`, `--webex-email`.

example to send Webex notification to webex space by using webex arguments

.. code-block:: bash

    pyats run job <job file> --testbed-file /path/to/testbed.yaml --health-checks cpu memory logging core --health-webex --webex-token <webex token> --webex-space <webex space id>

.. note::

    Webex notification is done by pyATS Webex Plugin in `pyats.contrib` package. Please refer to `Webex Plugin README <https://github.com/CiscoTestAutomation/pyats.contrib/tree/master/src/pyats/contrib/plugins/webex_plugin>`_ for more detail.

++++

The above are all the easy ways to use pyATS Health Check. Also, please be aware that each of the above arguments can be used in combination. If you want to use custom pyATS Health Checks, please check the design chapter.

.. toctree::
   :maxdepth: 2

   health_design/design
   health_usage/usage
