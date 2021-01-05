April 2020
==========

April 28th - Genie v20.4
-------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.4                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.4                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

Note that this will leave older v19.12 packages around in pip list, but it will
not impact anything (visual only).  An update command can be used to clean up
these packages

.. code-block:: bash

   pyats version update

Features:
^^^^^^^^^

This month we are releasing a brand new package within the pyATS libraries
Umbrella.

Built on top of the pyATS Kleenex infrastructure, the new pyATS clean library
enables you to restore your testbed’s devices to a known-good state by loading
your specified image and configuration. It can be added to any existing pyATS
script with using just a few additional arguments.

Build like Lego building blocks, pyATS clean is highly modular. You can add,
remove and modify any stages, including customizing your own clean stage
anywhere in the process! This gives it the flexibility to support a variety of
platforms, each with its own tailored clean process/portfolio.

pyATS Clean is simplistic, the library is designed so you can use one clean
yaml structure for all your devices - regardless of operating system and
platforms.

It currently supports IOSXE and NXOS with IOSXR coming next month.

For the first time, Clean logs are now easy to view and debug thanks to Xpresso
and our pyATS Logviewer. The logs and results can be viewed live as the run
happens by adding the ``--liveview`` argument to the pyats run command and
visiting http://localhost:8080/.

pyATS Clean is the official Cleaner and it is replacing Uniclean, and older Tcl
cleans (easypyclean, ngclean). These cleans are now End Of Life and End Of
Support.

You can find many examples in our `Github repo
<https://github.com/CiscoTestAutomation/examples/tree/master/clean>`_.

For more information you can visit our :ref:`website<clean>` or reach out to us
at: pyats-support@cisco.com

**Genie**

* device.parse support short form clis, for example: `show ver` for show version
* device.parse supports fuzzy search, for example `show bgp.*` to execute all
  show commands which begins with show bgp

.. code-block:: python
   
   # No need to send the specific show command, you can
   # abbreviate like on the devices!
   device.parse('show ver')

   # Use fuzzy for even more powerful parsers
   # Send all parser which starts with show bgp
   # Will return a dictionary of all show commands with their values
   device.parse('show bgp.*', fuzzy=True)

* Dq handles regex query inputs
* Dq - removed 'contains_key_value_in_list' and
  'not_contains_key_value_in_list' as those are now handled within contains
* Dq - Updated to return empty in case index for get_values is out of range

.. code-block:: python

  # Check if the module in line card #4 contains a status
  # and its value is ok or active
  >>> output.q.contains('lc').contains('4').contains_key_value('status', 'ok|active', value_regex=True)
  {'lc': {'4': {'NX-OSv Ethernet Module': {'status': 'ok'}}}})

Full examples in our `DQ documentation
<https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_.

* Fixed discovery for sections in trigger
* Updated loader.py to be able to call devices by their alias in markup.
* Support verbose option for Genie
  * Added verbose option for diff command by adding -v
  * Added verbose support to show parsed_output in Parser by adding -v
  * Added verbose support to show ops structure in Ops by adding -v
* Changed to accept both trigger/verification_uids and _groups. When both are
  provided, filtering trigger/verification by using both.
* Extended datafile are now shown in full in the archive (.zip)
* New support for netconf, restconf and gnmi support for Genie Harness
* Can now run/skip testcase depending on CDET state (Cisco Employee only) with
  processor pre_setup_skip_if_cdet_not_resolved
* New nested Diff representation for list and tuple
* Enhanced Diff to show diff strings without formatting
* Added support for testbed object in other datafile using the markup syntax
* Updated to load only triggers/verifications that will be executed
* Enhance debug_plugin logic to only copy on the device specified in multiple debug plugin scenario.
* Updated Timeout to support max_time=None and interval=None
* Added 'ops_schema' to the exclude for pts comparison
* New pyats.contrib - Allow to create testbed file from other system
  https://github.com/CiscoTestAutomation/pyats.contrib

pyats.contrib can create pyATS testbed out of Ansible, Netbox, Excel, CSV and prompts. Here is an example:

.. code-block:: bash

    bash$ pyats run job /path/to/jobfile.py --testbed-file source:netbox --netbox-token=token --netbox-url=url

**Genie.Libs.Parser**

 * ``Dq()`` is now by default a ``device.parse()`` return object type
 * 823 new IOSXE, IOS, NXOS, IOSXR, Junos and F5  Parsers! (700 are F5)
 * Grand total of 2435 parsers
 * Changelog can be checked :parserchangelog20:`here <APRIL>`

**Genie.Libs.Sdk**

 * 49 new apis to use on your devices!
 * Moved delete plugin step in HA triggers to the CommonCleanup section
 * Changelog can be checked :sdkchangelog20:`here <APRIL>`

**Genie.Libs.Ops**

 * Changelog can be checked :opschangelog20:`here <APRIL>`

**Genie.Libs.Conf**

 * Changelog can be checked :confchangelog20:`here <APRIL>`

**Genie.Libs.Filetransferutils**

 * No change

**Genie.Libs.Robot**

 * Changelog can be checked :robotchangelog20:`here <APRIL>`

**Genie.Telemetry**

 * No change

**Genie.Trafficgen**

 * No change
