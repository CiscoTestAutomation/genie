July 2019
=========

July 31th- Genie v19.7.1
----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie.harness``                 | 19.7.1                        |
+-----------------------------------+-------------------------------+

* Bug fix for abstraction

July 30th- Genie v19.7
----------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.abstract``                | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.conf``                    | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.examples``                | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.harness``                 | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.telemetry``          | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.metaparser``              | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.ops``                     | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.parsergen``               | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.predcore``                | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.utils``                   | 19.7                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 19.7                          |
+-----------------------------------+-------------------------------+
| ``unicon``                        | 19.7                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie genie.abstract genie.conf genie.examples genie.harness genie.libs.conf genie.libs.filetransferutils genie.libs.ops genie.libs.parser genie.libs.robot genie.libs.sdk genie.libs.telemetry genie.metaparser genie.ops genie.parsergen genie.predcore genie.telemetry genie.utils unicon genie.trafficgen


Features
^^^^^^^^

**Genie**
* No change!


**Genie.Ops**
* Updated learn_poll to pass kwargs to ops.learn()


**Genie.Conf**
* No change!


**Genie.Utils**
* Remove genie.utils.command_line.tabber 
* Remove genie.utils.command_line.question_mark 


**Genie.Harness**
* Updated processor.py, added start_reporter() and stop_reporter() functions


**Genie.Examples**
* Removed `genie.examples` modules
  examples are moved to https://github.com/CiscoTestAutomation/ as a repository

  
**Genie.Libs.Parser**
* Over 10 new IOSXE, IOS, NXOS & JunOS Parsers!
* Changelog can be checked :parserchangelog19:`here <JULY>`


**Genie.Libs.Ops**
* New OPS structures on IOS;
    * ACL
    * DOT1X
* Changelog can be checked :opschangelog19:`here <JULY>`


**Genie.Libs.Conf**
* No change!
* Changelog can be checked :confchangelog19:`here <JULY>`


**Genie.Libs.Sdk**
* Update on HA triggers' excpetion handling!
* Changelog can be checked :sdkchangelog19:`here <JULY>`


**Genie.Libs.Robot**
* No change!
* Changelog can be checked :robotchangelog19:`here <JULY>`


**Genie.Trafficgen**
* Save and export "Flow Statistics" data as a CSV snapshot
* Check traffic loss for each flow group of parent traffic stream
* Disconnect/automatically reconnect when Ixia connection is reset
* Enable/disable assigning physical ports to virtual ::ixNet:: ports
* Enhanced logging for check_traffic_loss for traffic streams
* Get packet size per traffic stream or per flow group
* Get packet rate per traffic stream or per flow group
* Get layer2 bit rate per flow group or per flow group
* Get line rate per flow group or per flow group
* Find Traffic Stream, Flow Group and Quick Flow Group, QuickTest ::ixNet:: objects from name
* Enhancement for set packet size to enable/disable starting traffic after change
* Enhancement for set packet rate to enable/disable starting traffic after change
* Enhancement for set line rate to enable/disable starting traffic after change
* Enhancement for set layer2 bit rate to enable/disable starting traffic after change
* Get QuickTest results attributes
* Bugfix: Traffic streams with exact same "name" not printing in logs
* Bugfix: Get multi-page statistics data for custom "GENIE" view


**Genie.FileTransferUtils**
* Added support for IOS


**Genie.Libs.Telemetry**
* No change!


**Genie.Abstract**
* Added ``Lookup.from_device(default_tokens=[])`` argument to support default
  device attributes to lookup from, in case ``device.custom.abstraction`` block
  is not defined
* Fixed a bug related to ``Lookup().from_device()`` crashing when tokens are 
  only defined in ``custom/abstraction`` block


**Genie.Telemetry**
* No change!


**Genie.Parsergen**
* No change!


**Genie.Metaparser**
* No change!


**Genie.Predcore**
* No change!


**Unicon**
* core
  * fix StateTransition do_transitions to return correct output
  * fix dialogs with multi thread to send command to correct connection
  * inherit base Connection from Lockable and add RLock for BaseService
  * improve performance by enhancing pty_backend to support different modes in match_buffer.
    By default, match_mode_detect is enabled. Detect rules are as below:
    * search whole buffer with re.DOTALL if:
      * pattern contains any of: \\r, \\n
      * pattern equals to any of: .*, ^.*$, .*$, ^.*, .+, ^.+$, .+$, ^.+
    * Else if pattern ends with $, will only match last line
    * In other situations, search whole buffer with re.DOTALL
  * improve performance by compiling regex patterns first in dialog_processor
  * improve performance by removing re.search again in truncate_trailing_prompt
  * add connection "host" in SSHTunnel and topology adapter


* added credential support
  * When pyATS integration is used,
    * If a ``default`` credential is supplied, then a credential of any other
      name is looked up explicitly and is not found, the ``default`` credential
      is used instead.
    * credentials supplied to the connection contain any credentials defined
      at the device and testbed levels as well.

  * If one or more credentials are supplied:
    * The ``tacacs`` and ``passwords`` pyATS testbed keys are ignored.
    * Use of any of the following `unicon.Unicon.Connection` arguments cause a
      deprecation warning to be raised :
      * ``username``
      * ``password``
      * ``enable_password``
      * ``tacacs_password``
      * ``line_password``

    * The following credential names are expected to be defined explicitly:
      * ``enable`` : This credential defines the password to be sent when
        bringing routing devices to their enable mode.
      * ``sudo`` : The fsos/ftd plugin expects this credential to contain
        the sudo password.
      * ``ssh`` : When setting up an sshtunnel against a server specified in
        a pyATS testbed servers block, this credential must be defined against
        that server block.
    * The ``login_creds`` argument (specified either in pyATS connection
      block or as a `unicon.Unicon.Connection` parameter), now controls
      the order credentials are applied when username/password prompts are
      received while connecting to the device.
    * The ``prompts/login`` and ``prompts/password`` parameters are now
      expected to be explicitly set in the pyATS connection block or
      as `unicon.Unicon.Connection` parameters.
    * The switchover service now accepts a ``switchover_creds`` parameter that
      allows users to define what credentials to use should a username or
      password prompt occur during switchover.
    * The reload service now accepts a ``reload_creds`` parameter that
      allows users to define what credentials to use should a username or
      password prompt occur during reload.
  * The execute service no longer responds to username/password requests,
    users are expected to pass in their own dialog if this kind of handling
    is required.

* generic plugin
  * add flatten_splitlines_command method in generic utils to flatten commands
  * add get_handle method in BaseService for all services to reuse
  * add bulk argument for Configure service to send commands in one sendline
  * refactor generic Configure service, and now HaConfigureService inherits from Configure
  * fix several bugs in BaseService and generic HaExecService

* iosxr plugin
  * fix potential bugs in iosxr execute and configure related services
  * add HaAdminExecute and HaAdminConfigure services for iosxr
  * fix asr9k plugin services admin_execute, admin_configure and admin_bash_console on 64-bit asr9k
  * added dual RP support to iosxr/spitfire plugin.

* junos plugin
  * fix junos plugin configure service

* nxos plugin
  * added VDC related robot commands.

* asa plugin
  * added warning to ASA plugin patterns.

* ios plugin
  * added vrf support in ios plugin ping service. It now accepts vrf as input and passes it as part of the ping command
