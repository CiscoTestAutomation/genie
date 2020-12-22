.. __cli_dnac:

Genie DNAC
==========

`genie dnac` is an easy way to communicate through REST api to your DNAC host.
It sends rest api, parsed them with Genie parsers and write 

To see what functionality `genie dnac` offers, execute the following in your
linux terminal:

.. code-block:: bash

    Usage:
      genie dnac [commands] [options]
    
    Example
    -------
      genie dnac interface --testbed-file tb.yaml --output snapshot1
    
    Description:
      Command to learn DNAC features and save to file
    
          Available features: Interface, isis, ospf
    
    Dnac Options:
      feature               List of Feature to learn, comma separated, interface, isis; all can instead
                            be provided to learn all features
      --testbed-file TESTBED_FILE
                            specify testbed_file yaml
      --devices [DEVICES [DEVICES ...]]
                            List of devices, comma separated, if not provided it will learn on all
                            devices (Optional)
      --output OUTPUT       Which directory to store logs, by default it will be current directory
                            (Optional)
      --single-process      Learn one device at the time instead of in parallel (Optional)
      --via [VIA [VIA ...]]
                            List of connection to use per device "nxos-1:ssh"
    
    General Options:
      -h, --help            Show help
      -v, --verbose         Give more output, additive up to 3 times.
      -q, --quiet           Give less output, additive up to 3 times, corresponding to WARNING, ERROR,
                            and CRITICAL logging levels

Examples
--------

Let's see a scenario:

.. code-block:: bash

     genie dnac interface isis ospf --testbed-file dna.yaml --output initial 
     # Wait some time, to see if anything has changed on the devices
     genie dnac interface isis ospf --testbed-file dna.yaml --output modified
     genie diff initial modified 

If any devices has changed, the diff will let you know of the changes.

More examples can be found at: `github_dnac`_.

.. note::

    This feature is currently in prototype

.. _github_dnac: https://github.com/CiscoTestAutomation/DNAC-pyATS-Genie
