Device command aliases
======================

LAMP can create shell aliases for ``device`` command automatically from device alias names.
Aliases can be defined in the testbed YAML file under the 'alias' key,
or specified with the '-n' option in the ``testbed add`` command. If not defined,
the device name is used as the alias.

To enable this feature, set ``device_aliases`` to 'ENABLED':

.. code-block:: console

    (lamp) set device_aliases ENABLED 
    device_aliases - was: DISABLED
    now: 'ENABLED'
    (lamp) 

Once enabled, aliases are created for each device loaded with the ``testbed``
command. New aliases are generated as additional devices are added,
and removed when devices are deleted.

For example, in the testbed YAML below, 'host1' has the alias 'h1',
while 'host2' does not have an alias. When the testbed is loaded, LAMP creates
the alias 'h1' for 'host1'. For 'host2', the device name itself is used as
the alias. The output of the ``alias list`` command reflects these assignments:

.. code-block:: yaml

   devices:
    host1:
      alias: h1
      os: iosxe
      type: iosxe
      platform: iol
      connections:
        a:
          ip: 127.0.0.1
          port: 33331
          protocol: telnet
        defaults:
          class: unicon.Unicon
          via: cli
    host2:
      os: iosxe
      type: iosxe
      platform: iol
      connections:
        a:
          ip: 127.0.0.1
          port: 33332
          protocol: telnet
        defaults:
          class: unicon.Unicon
          via: cli

.. code-block:: console

   (lamp) testbed load t.yaml
   2024-11-29 19:57:33: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-11-29 19:57:33: %LAMP-INFO: :                           Loading testbed 't.yaml'                           :
   2024-11-29 19:57:33: %LAMP-INFO: +------------------------------------------------------------------------------+

   <TRUNCATED>

   2024-11-29 19:57:39: %LAMP-INFO: +------------------------------------------------------------------------------+
   2024-11-29 19:57:39: %LAMP-INFO: :                      Connected to 'host1' successfully                       :
   2024-11-29 19:57:39: %LAMP-INFO: :                      Connected to 'host2' successfully                       :
   2024-11-29 19:57:39: %LAMP-INFO: +------------------------------------------------------------------------------+
   Alias 'h1' created
   Alias 'host2' created
   (lamp-host1)
   (lamp-host1) alias list
   alias create h1 device host1
   alias create host2 device host2
   (lamp-host1)

The next example shows how an alias is created for a device using the '-n'
option in the ``testbed add`` command:

.. code-block:: console

   (lamp-host1) testbed add 127.0.0.1 -p 33333 -n h3

   <TRUNCATED>

   2025-03-23 15:52:55: %LAMP-INFO: +..............................................................................+
   2025-03-23 15:52:55: %LAMP-INFO: :                      Connected to 'host3' successfully                       :
   2025-03-23 15:52:55: %LAMP-INFO: +..............................................................................+
   Alias 'h3' created
   (lamp-host3)
   (lamp-host3) alias list
   alias create h1 device host1
   alias create host2 device host2
   alias create h3 device h3
   (lamp-host3)

When devices are removed, their aliases are deleted as shown below:

.. code-block:: console

   (lamp-h3) testbed remove h3
   2025-03-23 15:56:50: %LAMP-INFO: +..............................................................................+
   2025-03-23 15:56:50: %LAMP-INFO: :                        Disconnecting from device 'h3'                        :
   2025-03-23 15:56:50: %LAMP-INFO: +..............................................................................+
   Alias 'h3' deleted
   (lamp-host1)
   (lamp-host1) testbed remove -a
   2025-03-23 15:56:55: %LAMP-INFO: +..............................................................................+
   2025-03-23 15:56:55: %LAMP-INFO: :                      Disconnecting from device 'host1'                       :
   2025-03-23 15:56:55: %LAMP-INFO: :                      Disconnecting from device 'host2'                       :
   2025-03-23 15:56:55: %LAMP-INFO: +..............................................................................+
   Alias 'host1' deleted
   Alias 'h2' deleted
   (lamp)
   (lamp) alias list
   (lamp)
