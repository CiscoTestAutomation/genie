Autocompletion
===============

Autocompletion assists in typing LAMP commands and their arguments. Press <TAB> to autocomplete.

If multiple completion options exist, pressing <TAB> once may not complete the command.
In such cases, press <TAB><TAB> to display the list of available options.

device
-------

LAMP supports autocompletion for ``device`` command with device names from the list of loaded devices.

The example below illustrates the list of available completions when two devices, 'host1' and 'host2',
are loaded in the shell. This could be observed by pressing <TAB><TAB> after typing ``device host``:

.. code-block:: console

   (lamp-host1) device host
   host1    host2

testbed & replay
-----------------

LAMP supports YAML filepath autocompletion for ``testbed load``, ``testbed save`` & ``replay`` commands.
Only '.yaml' files & directories will be listed.

.. code-block:: console

   (lamp-host1) testbed load testbeds/ios/
   ios_testbed.yaml    pnp-info/           pnp-tech/           
   (lamp-host1) testbed load testbeds/ios/

LAMP autocompletes device names for ``testbed remove`` similar to the ``device`` command:

.. code-block:: console

   (lamp-host1) testbed remove host
   host1    host2

api
---

LAMP supports both name-wise and module-wise autocompletion for the ``api`` command.

Name-wise autocompletion
^^^^^^^^^^^^^^^^^^^^^^^^

Name-wise autocompletion lists all API's that begin with a given prefix string.

The example below lists all API's that start with 'get_vrf' when <TAB><TAB> is pressed:

.. code-block:: console

   (lamp-host1) api get_vrf_
   get_vrf_interface              get_vrf_route_distinguisher    get_vrf_route_targets          get_vrf_vrfs
   (lamp-host1) api get_vrf_

Module-wise autocompletion
^^^^^^^^^^^^^^^^^^^^^^^^^^

Module-wise autocompletion helps autocomplete module names, submodule names within a module,
and all API names under a specific module and submodule.

The example below demonstrates autocompletion of module names starting with 'v' when
pressing <TAB><TAB> (An underscore character '_' is used to separate module names from API names):

.. code-block:: console

   (lamp-host1) api _v
   vdsl       verify     version    vlan       vpdn       vpn        vrf

The next example demonstrates autocompletion of submodule names within
the '_vrf' module when pressing <TAB><TAB>:

.. code-block:: console

   (lamp-host1) api _vrf
   configure    get          verify

The final example demonstrates the autocompletion of all APIs under the 'vrf'
module and 'configure' submodule when pressing <TAB><TAB>:

.. code-block:: console

   (lamp-host2) api _vrf configure
   configure_default_mpls_mldp                       configure_vrf_definition_family
   configure_default_vxlan                           configure_vrf_definition_stitching
   configure_ip_vrf_forwarding_interface             configure_vrf_description
   configure_mdt_auto_discovery_inter_as             configure_vrf_forwarding_interface
   configure_mdt_auto_discovery_inter_as_mdt_type    configure_vrf_rd_value
   configure_mdt_auto_discovery_mldp                 create_ip_vrf
   configure_mdt_auto_discovery_vxlan                delete_ip_vrf
   configure_mdt_data_mpls_mldp                      unconfigure_default_vxlan
   configure_mdt_data_threshold                      unconfigure_ip_vrf_forwarding_interface
   configure_mdt_data_vxlan                          unconfigure_mdt_auto_discovery_mldp
   configure_mdt_default                             unconfigure_mdt_auto_discovery_vxlan
   configure_mdt_overlay_use_bgp                     unconfigure_mdt_data_threshold
   configure_mdt_overlay_use_bgp_spt_only            unconfigure_mdt_data_vxlan
   configure_mdt_partitioned_mldp_p2mp               unconfigure_mdt_overlay_use_bgp
   configure_mdt_preference_under_vrf                unconfigure_vrf
   configure_mdt_strict_rpf_interface_vrf            unconfigure_vrf_definition_on_device
   configure_multicast_routing_mvpn_vrf              unconfigure_vrf_definition_stitching
   configure_rd_address_family_vrf                   unconfigure_vrf_description
   configure_scale_vrf_via_tftp                      unconfigure_vrf_forwarding_interface
   configure_vpn_id_in_vrf

parse
-----

LAMP provides command autocompletion using the available list of parsers.
Symbols enclosed in curly braces (e.g., {protocol} and {route} in the example
below) are placeholders for the actual values that need to be provided
by the user.

.. code-block:: console

   (lamp-host1) parse show ip route
   summary           supernets-only    vrf               {protocol}        {route}
   (lamp-host1) parse show ip route

execute
-------

For ``execute`` command, LAMP does command autocompletion at device's exec shell by
transmitting and receiving the '?' symbol using 'Unicon' API's.

Autocompletion list for the command ``execute show ip``:

.. code-block:: console

   (lamp-leaf2) execute show ip

   COMMAND              Description
   ==========================================================================
   access-lists         List IP access lists
   accounting           The active IP accounting database
   admission            Network Admission Control information
   aliases              IP alias table
   amt                  Show AMT protocol parameters
   arp                  IP ARP table
   as-path-access-list  List AS path access lists
   bgp                  BGP information
   cache                IP fast-switching route cache
   cef                  Cisco Express Forwarding
   community-list       List community-list
   ddns                 Dynamic DNS
   dhcp                 Show items in the DHCP database
   dns                  Show DNS information
   eigrp                Show IPv4 EIGRP
   explicit-paths       Show IP explicit paths
   extcommunity-list    List extended-community list
   helper-address       helper-address table
   host-list            Host list
   <TRUNCATED>

.. note::

   Sending '?' to the device takes time to receive a response & hence displaying the
   autocompletion results might be delayed. It is recommended to avoid pressing
   <TAB> if the device is connected over a slow network or is located far away
   from the server running LAMP.

configure
---------

Autocompletion for CLI are available in *'config-prompt'* mode:

.. code-block:: console

   leaf2(config)# ip pim

   CONFIG                 Description
   ==============================================================================
   accept-register        Registers accept filter
   accept-rp              RP accept filter
   allow-rp               Sparse-Mode RP addresses to be allowed
   autorp                 Configure AutoRP global operations
   bidir-enable           Enable Bidir-PIM
   bidir-offer-interval   DF election offer message interval
   bidir-offer-limit      number of unanswered offers before becoming DF
   bsr-candidate          Candidate bootstrap router (candidate BSR)
   cache                  PIM cache configuration
   dm-fallback            Fallback group mode is Dense
   fast-register-stop     Immediately send register-stops on registers
   log-neighbor-changes   Log PIM neighbor up/down and DR changes
   maximum                Maximum state limits
   mpls                   pim mpls commands
   old-register-checksum  Generate Register checksum on whole packet
   register-rate-limit    Rate limit for PIM data registers
   register-source        Source address for PIM Register
   rp-address             PIM RP-address (Rendezvous Point)
   rp-announce-filter     Auto-RP announce message filter
   rp-candidate           To be a PIMv2 RP candidate
   rp-proxy-join          RP always proxy joins for sources
   send-rp-announce       Auto-RP send RP announcement
   send-rp-discovery      Auto-RP send RP discovery message (as RP-mapping agent)
   sparse                 This command is specific to PIM-Sparse Mode
   spt-threshold          Source-tree switching threshold
   ssm                    Configure Source Specific Multicast
   state-refresh          PIM DM State-Refresh configuration
   v1-rp-reachability     Send PIMv1 RP-reachability packet
   vrf                    Select VPN Routing/Forwarding instance

list & remove
-------------

``list -n`` and ``remove -n`` can autocomplete with the added test section names:

.. code-block:: console

   (lamp-leaf2) remove -n
   default    new        new_2