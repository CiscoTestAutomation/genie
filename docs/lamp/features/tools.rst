Tools
===========

Several commands assist with tasks such as retrieving information, checking metadata,
and exploring configurations. These commands are grouped under the 'Tools' category.

Info
----

The ``info`` command provides a centralized way to explore internal code and metadata
within the LAMP environment. Current functionalities include:

- **Parser Code Viewer**: View parser implementations for ``show`` commands.
- **API Code Viewer**: Display API function definitions and usage details.
- **API Search**: Find APIs by name and locate their module paths.

Additional capabilities will be added, making ``info`` a valuable tool for
introspection, debugging, and development in LAMP.

Parser code viewer
^^^^^^^^^^^^^^^^^^^

To view parser code, provide the show command as an argument to ``info parser``.
This prints a link to the code repository where the corresponding parser class
is located.

Example:

.. code-block:: console

    (lamp-host1) info parser show ip mroute
    ╭────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser/ios/show_mcast.py#L22 │
    ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    (lamp-host1)

Api code viewer
^^^^^^^^^^^^^^^^

Api code can be viewed using ``info api <API_NAME>`` or ``info api _<MODULE_NAME> <SUBMODULE_NAME> <API_NAME>``.

Example:

.. code-block:: console

    (lamp-h4) info api get_running_config_dict
    ╭──────────────────────────────────────────────────────────────────────────────────────────────────╮
    │    1 def get_running_config_dict(device, option=None, output=None, lstrip=False):                │
    │    2     """ Get show running-config output                                                      │
    │    3                                                                                             │
    │    4         Args:                                                                               │
    │    5             device (`obj`): Device object                                                   │
    │    6             option (`str`): option command                                                  │
    │    7             output (`str`): output of show running-config                                   │
    │    8             lstrip (`bool`): Boolean to use lstrip on config lines                          │
    │    9         Returns:                                                                            │
    │   10             config_dict (`dict`): dict of show run output                                   │
    │   11     """                                                                                     │
    │   12     if output:                                                                              │
    │   13         out = output                                                                        │
    │   14     else:                                                                                   │
    │   15         if option:                                                                          │
    │   16             cmd = "show running-config {}".format(option)                                   │
    │   17         else:                                                                               │
    │   18             cmd = "show running-config"                                                     │
    │   19         try:                                                                                │
    │   20             out = device.execute(cmd)                                                       │
    │   21         except SubCommandFailure as e:                                                      │
    │   22             raise SubCommandFailure(                                                        │
    │   23                 "Could not get running-config information "                                 │
    │   24                 "on device {device}".format(device=device.name)                             │
    │   25             )                                                                               │
    │   26                                                                                             │
    │   27     # Remove any noise from show run command                                                │
    │   28     out = re.sub(r'Building configuration...\s*Current configuration : \d+ bytes', '', out) │
    │   29                                                                                             │
    │   30     config_dict = get_config_dict(out, lstrip=lstrip)                                       │
    │   31     return config_dict                                                                      │
    │   32                                                                                             │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
    (lamp-h4)

Api search
^^^^^^^^^^^

APIs can be searched by name using ``info api-search <SEARCH_STRING>``. The command also displays the
module path to help locate the API code within the Genie repository.

Example:

.. code-block:: console

    (lamp-h4) info api-search reload
                                    APIs matching search string 'reload'                                 
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ API name                                        ┃ Module Path                                     ┃
    ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
    │ write_erase_reload_device                       │ genie.libs.sdk.apis.iosxe.platform.utils        │
    │ verify_last_reload_reason                       │ genie.libs.sdk.apis.iosxe.platform.verify       │
    │ execute_install_package_reload_fast             │ genie.libs.sdk.apis.iosxe.install.execute       │
    │ unconfigure_global_dual_active_recovery_reload_ │ genie.libs.sdk.apis.iosxe.stackwise_virtual.con │
    │ disable                                         │ figure                                          │
    │ execute_reload                                  │ genie.libs.sdk.apis.execute                     │
    │ reload_issu_slot                                │ genie.libs.sdk.apis.iosxe.issu.configure        │
    │ configure_graceful_reload                       │ genie.libs.sdk.apis.iosxe.platform.configure    │
    │ execute_reload_fast                             │ genie.libs.sdk.apis.iosxe.platform.execute      │
    │ configure_global_dual_active_recovery_reload_di │ genie.libs.sdk.apis.iosxe.stackwise_virtual.con │
    │ sable                                           │ figure                                          │
    │ write_erase_reload_device_without_reconfig      │ genie.libs.sdk.apis.iosxe.platform.utils        │
    │ execute_event_manager_run_with_reload           │ genie.libs.sdk.apis.iosxe.platform.execute      │
    │ execute_redundancy_reload                       │ genie.libs.sdk.apis.iosxe.redundancy.execute    │
    │ hw_module_sub_slot_reload                       │ genie.libs.sdk.apis.iosxe.hw_module.execute     │
    │ configure_graceful_reload_interval              │ genie.libs.sdk.apis.iosxe.platform.configure    │
    └─────────────────────────────────────────────────┴─────────────────────────────────────────────────┘
