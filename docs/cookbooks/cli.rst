.. _book_cli:

.. raw:: html

   <h2>Genie Cli recipes</h2>

.. note::

    This section assumes pyATS and Genie are :ref:`installed and ready to be
    used<book_genie>`.

.. note::

    It also assumes you have a :ref:`testbed file ready<book_setup_testbed>` to
    be used with a device.

1. Summary
----------

Genie CLI is the easiest way to start with Genie. No need any automation or
Python knowledge. As long as Genie is installed, you can interact with the
Genie libraries with a Linux command.

Here's what you can do:

1. Parse show command into structured output
2. Learn whole device feature into structured outpu
3. Compare structured output taken at different time
4. Genie shell to load the testbed file and/or pickle file.
5. Run Genie Harness without any jobfile

:ref:`More detailed documentation on Genie CLI<genie_cli>`


2. Parse device output
----------------------

Any of the :parsers:`available parsers<http>` can be called directly called
with Genie cli.


.. code-block:: bash

    genie parse "show bgp vrf all all" --testbed-file tb.yaml --output output --devices nx-osv-1
    +==============================================================================+
    | Genie Parse Summary for nx-osv-1                                             |
    +==============================================================================+
    |  Connected to nx-osv-1                                                       |
    |  -  Log: x/connection_nx-osv-1.txt                                           |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show bgp vrf all all'                                       |
    |  -  Parsed structure: x/nx-osv-1_show-bgp-vrf-all-all_parsed.txt             |
    |  -  Device Console:   x/nx-osv-1_show-bgp-vrf-all-all_console.txt            |
    |------------------------------------------------------------------------------|


Execute on all the devices in the testbed file

.. code-block:: bash

    genie parse "show bgp vrf all all" "show ip ospf" --testbed-file tb.yaml --output x
    +==============================================================================+
    | Genie Parse Summary for csr1000v-1                                           |
    +==============================================================================+
    |  Connected to csr1000v-1                                                     |
    |  -  Log: x/connection_csr1000v-1.txt                                         |
    |------------------------------------------------------------------------------|
    |  Could not parse 'show bgp vrf all all'                                      |
    |  -  Exception:      x/csr1000v-1_show-bgp-vrf-all-all_exception.txt          |
    |  -  Device Console: x/csr1000v-1_show-bgp-vrf-all-all_console.txt            |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show ip ospf'                                               |
    |  -  Parsed structure: x/csr1000v-1_show-ip-ospf_parsed.txt                   |
    |  -  Device Console:   x/csr1000v-1_show-ip-ospf_console.txt                  |
    |------------------------------------------------------------------------------|
    +==============================================================================+
    | Genie Parse Summary for nx-osv-1                                             |
    +==============================================================================+
    |  Connected to nx-osv-1                                                       |
    |  -  Log: x/connection_nx-osv-1.txt                                           |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show bgp vrf all all'                                       |
    |  -  Parsed structure: x/nx-osv-1_show-bgp-vrf-all-all_parsed.txt             |
    |  -  Device Console:   x/nx-osv-1_show-bgp-vrf-all-all_console.txt            |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show ip ospf'                                               |
    |  -  Parsed structure: x/nx-osv-1_show-ip-ospf_parsed.txt                     |
    |  -  Device Console:   x/nx-osv-1_show-ip-ospf_console.txt                    |
    |------------------------------------------------------------------------------|
    
Parser all commands for all devices

.. code-block:: bash

    genie parse all --testbed-file tb.yaml --output all
    +==============================================================================+
    | Genie Parse Summary for csr1000v-1                                           |
    +==============================================================================+
    |  Connected to csr1000v-1                                                     |
    |  -  Log: all/connection_csr1000v-1.txt                                       |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show bgp all cluster-ids'                                   |
    |  -  Parsed structure: all/csr1000v-1_show-bgp-all-cluster-ids_parsed.txt     |
    |  -  Device Console:   all/csr1000v-1_show-bgp-all-cluster-ids_console.txt    |
    |------------------------------------------------------------------------------|
    |  Parsed command 'show stack-power' but it returned empty                     |
    |  -  Device Console: all/csr1000v-1_show-stack-power_console.txt
    .... (more than 300 parsers were executed!)


For each show command, 2 files are created. 

* One containing the device log (_console file).
* One containing the parser output in Json structure (_parsed file)

3. Learn device feature
-----------------------

Same idea as above, however it will learn whole feature and return an OS
Agnostic structure (Same structure for all OS).

Any of the :models:`available Ops object<http>` can be called directly called
with Genie cli.

.. code-block:: bash

    genie learn "ospf" --testbed-file tb.yaml --output output
    Learning '['ospf']' on devices '['csr1000v-1', 'nx-osv-1']'
    +==============================================================================+
    | Genie Learn Summary for device csr1000v-1                                    |
    +==============================================================================+
    |  Connected to csr1000v-1                                                     |
    |  -   Log: ./connection_csr1000v-1.txt                                        |
    |------------------------------------------------------------------------------|
    |  Learnt feature 'ospf'                                                       |
    |  -  Ops structure:  ./output/ospf_iosxe_csr1000v-1_ops.txt                   |
    |  -  Device Console: ./output/ospf_iosxe_csr1000v-1_console.txt               |
    |==============================================================================|



4. Snapshots and then compare before and after
----------------------------------------------

With the two previous recipes, it is now easy to take snapshots, save them to a
directory, update the configuration of your device and retake a new snapshot to
compare.



.. code-block:: bash

    genie learn "bgp" --testbed-file tb.yaml --output output1

Update device configuration


.. code-block:: bash

    genie learn "bgp" --testbed-file tb.yaml --output output2

.. code-block:: bash

    genie diff output output2

genie diff lets you know which fields has been modified.

.. code-block:: text

    more output/diff_bgp_nxos_nxos-osv-1_ops.txt
    --- output1/bgp_nxos_nxos-osv-1_ops.txt
    +++ output2/bgp_nxos_nxos-osv-1_ops.txt
    info:
     instance:
      default:
       vrf:
        default:
         neighbor:
          50.1.1.101:
           address_family:
            ipv4 multicast:
    +         session_state: active
    -         session_state: idle
            ipv4 unicast:
    +         session_state: active
    -         session_state: idle
    
The same idea can also be used as a monitor, to check if anything changes
overtime. Everyday takes a new snapshot and compare.


5. Collect device output - without parsing it
---------------------------------------------

Genie cli can be used to collect straight device output.

.. code-block:: bash

    genie parse "show version" --testbed-file tb.yaml --output output --raw
    +==============================================================================+
    | Genie Execute Summary for csr1000v-1                                         |
    +==============================================================================+
    |  Connected to csr1000v-1                                                     |
    |  -  Log: bla/connection_csr1000v-1.txt                                       |
    |------------------------------------------------------------------------------|
    |  Executed command 'show version'                                             |
    |  -  Device Console:   bla/csr1000v-1_show-version_console.txt                |
    |------------------------------------------------------------------------------|
