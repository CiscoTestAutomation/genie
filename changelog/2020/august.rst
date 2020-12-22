August 2020
========

August 25th - Genie v20.8
--------------------------

+-----------------------------------+-------------------------------+
| Module                            | Versions                      |
+===================================+===============================+
| ``genie``                         | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 20.8                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 20.8                          |
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

Features highlights:
^^^^^^^^^^^^^^^^^^^

* Fixed api abstraction in cases where the common and platform specific api exists but the os level does not
* Updated genie conf device to set the default alias to 'cli' if 'os' is not provided
* Harness connection now logs ModuleNotFoundError tracebacks
* Fixed using markup inside testbed files that referenced items in the testbed

* Genie Blitz added converter to convert maple scripts into Blitz testscripts
* Genie Blitz added looping functionality and conditional statement to help with writing more dynamic test scripts

* 46 new IOSXE, IOS, NXOS, IOSXE and Junos parsers with a grand total of 2561 parsers
* 86 new apis to use on your devices. Grand total of 911 APIs

* New Feature `pyATS Health Check` released
* Monitor/Collect device status as pre/post processors to section during test run

* Added 'ruamel.yaml' dependency to genielibs, to install it use: 'pip install ruamel.yaml'


**genie**

 * Fixed api abstraction in cases where the common and platform specific api exists but the os level does not

 * update genie conf device to set the default alias to 'cli' if 'os' is not provided

 * Harness connection now logs ModuleNotFoundError tracebacks

 * Fixed using markup inside testbed files that referenced items in the testbed

--------

**genie.libs.clean**

.. list-table::
    :header-rows: 1

    * - Feature
      - Docs
      - Whats New

    * - Stage 'reload'
      - `Reload Stage <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/clean/reload>`_
      - | Schema is changed to allow all unicon reload service arguments. See below:
        ::

                Clean yaml file schema:
                -----------------------
                devices:
                  <device>:
                    reload:
                      reload_service_args: (Optional, if not specified defaults below are used)
                        timeout: <reload timeout value, default 800 seconds. 'int'> (Optional)
                        reload_creds: <Credential name defined in the testbed yaml file to be used during reload, default 'default'. 'str'> (Optional)
                        prompt_recovery: <Enable/Disable prompt recovery feature, 'bool'> (Optional)
                        <Key>: <Value> (Any other key:value pairs that the unicon reload service allows for)

                      check_modules:
                        check: <Enable/Disable checking of modules after reload, default 'True'. 'bool'> (Optional)>
                        timeout: <timeout value to verify modules are in stable state, default 180 seconds. 'int'> (Optional)
                        interval: <interval value between checks for verifying module status, default 30 seconds. 'int'> (Optional)


* Stages 'copy_to_device' and 'copy_to_linux' now dynamically trim the server path configured under testbed.servers.<server>.path if it exists. Before it automatically trimmed 'tftpboot/'.

  The path key should be used if the server has a default path configured for initial connection.
  Example: my image is located at '/path/to/my/image.bin' and when I log into my tftp server I am at '/path/to'. So I need to configure the testbed.servers.tftp_server.path = '/path/to'.

* Removed 'reload_file' argument from 'reload' stage. This feature is now the new 'install_image' stage.
* Modified connect stage to use prompt_recovery
* Updated copy_to_linux added 'rename_images' argument to rename images
* Fixed stage not being able to use more than once
* Fixed the exit code in case clean fails
* Modified ImageHandlers to have better error messages if the structure of images is invalid   

* [IOSXE] Added install_image and install_packages stages
* [IOSXE] Modified change_boot_variable to save run to start after deleting existing variables

--------

**genie.libs.conf**

* No change

--------

**genie.libs.filetransferutils**

* No change

--------

**genie.libs.ops**

* Fixed IOSXR Routing:
  * To get all VRFs routing table by default

--------

**genie.libs.parser**

* 46 new IOSXE, IOS, NXOS, IOSXE and Junos Parsers!
* Grand total of 2561 Parsers
* Changelog can be checked :parserchangelog20:`here <AUGUST>`

--------

**genie.libs.robot**

* No change

--------

**genie.libs.sdk**

* 86 new apis to use on your devices!
* Grand total of 911 APIs
* Changelog can be checked :sdkchangelog20:`here <AUGUST>`

--------

**genie.telemetry**

* No change

--------

**genie.trafficgen**

* remove_vlan added to check_flow_groups_loss method to avoid VLAN:VLAN-ID check.

--------

**genie.utils**

* No change