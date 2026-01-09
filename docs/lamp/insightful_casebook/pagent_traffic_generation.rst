Pagent Traffic Generation with Jinja Templates
===============================================

This guide explains how to use LAMP's Jinja2 templating support to generate traffic
stream configurations for Pagent traffic generators—far more efficient than manual
configuration.

Why Use Jinja for Traffic Generation?
-------------------------------------

- **Rapid Configuration**: Define traffic parameters once, generate multiple streams
- **Reusability**: Create templates for common traffic patterns
- **Parameter-Driven**: Adapt to different topologies by changing YAML arguments
- **Scalability**: Scale from a few streams to hundreds with minimal effort

Creating a Traffic Generation Template
---------------------------------------

Here's a Jinja2 template that supports both IPv4 and IPv6 traffic streams:

.. code-block:: jinja

    !
    {% if pagent is defined %}
        {% for name, attr in pagent.items() %}
            # Traffic stream {{ name }}
            tgn {{ iface }}
            tgn add IP
            tgn name {{ name }}
            tgn on
            {% if attr.rate is defined %}
                tgn rate {{ attr.rate }}
            {% else %}
                tgn rate 5
            {% endif %}
            {% if attr.l2_src is defined %}
                tgn L2-src-addr {{ attr.l2_src }}
            {% endif %}
            {% if attr.l2_dest is defined %}
                tgn L2-dest-addr {{ attr.l2_dest }}
            {% endif %}
            {% if attr.l3_src is defined %}
                {% if ':' in attr.l3_src %}
                    tgn Layer 3 ipv6
                {% else %}
                    tgn L3-version 4
                {% endif %}
                tgn L3-src-addr {{ attr.l3_src }}
            {% endif %}
            {% if attr.l3_dest is defined %}
                tgn L3-dest-addr {{ attr.l3_dest }}
            {% endif %}
            tgn on
        {% endfor %}
    {% endif %}
    !

Save this template to a file (e.g., ``pagent_traffic.j2``).

Creating Traffic Arguments
---------------------------

Create a YAML file (e.g., ``traffic_args.yaml``) with your traffic stream(s) parameters:

.. code-block:: yaml

    pagent:
      # Multicast IPv4 traffic stream
      '225.1.1.1':
        iface: Ethernet0/0
        rate: 1
        l2_src: 5254.0012.a648
        l2_dest: 0001.5e01.0101
        l3_src: 30.0.0.2
        l3_dest: 225.1.1.1
      
      # Multicast IPv6 traffic stream
      'ff03::4':
        iface: Ethernet0/0
        rate: 5
        l2_src: 5254.0012.a648
        l2_dest: 3333.0000.0004
        l3_src: 3000::2
        l3_dest: ff03::4
      
      # Unicast IPv4 traffic stream
      '10.0.0.0/24':
        iface: Ethernet0/1
        rate: 10
        l2_src: 5254.0012.a649
        l2_dest: 0001.5e00.0001
        l3_src: 192.168.1.1
        l3_dest: 10.0.0.1

**Parameter Reference**

- **Stream Name**: Identifier for each traffic stream
- **iface**: Pagent interface for traffic generation (e.g., ``Ethernet0/0``)
- **rate**: Traffic rate in packets per second or percentage. Defaults to 5 if unspecified
- **l2_src**: Layer 2 source MAC address
- **l2_dest**: Layer 2 destination MAC address
- **l3_src**: Layer 3 source IP address (IPv4 or IPv6)
- **l3_dest**: Layer 3 destination IP address (IPv4 or IPv6)

Executing Traffic Generation
-----------------------------

Use the ``execute`` command with the ``-j`` flag to process your Jinja template:

.. code-block:: console

    (lamp-pagent) execute -j pagent_traffic.j2 traffic_args.yaml

This will:

    1. Process the Jinja2 template with your parameters
    2. Generate all traffic stream configuration commands
    3. Execute them on the pagent device

Modifying Traffic Dynamically
------------------------------

To change traffic characteristics, edit your ``traffic_args.yaml`` file and re-run the
execute command with updated arguments:

.. code-block:: console

    (lamp-pagent) execute -j pagent_traffic.j2 traffic_args_high_load.yaml

This lets you quickly swap between different traffic profiles without modifying the template.

Advanced: Creating Reusable Traffic Templates
-----------------------------------------------

Build a library of Jinja templates for different scenarios:

- **Base traffic**: Simple unicast or multicast flows
- **High-load traffic**: Multiple streams with varying rates
- **Protocol-specific traffic**: MPLS, QoS, or specialized types
- **Convergence testing**: Rapid traffic changes for failover behavior

By maintaining a template library with corresponding argument files, you can generate
complex traffic scenarios reliably across multiple testbeds.
