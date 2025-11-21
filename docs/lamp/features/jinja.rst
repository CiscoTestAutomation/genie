Jinja
=====

Jinja2 templates allow automated execution of commands or 
configuration application on network devices. The ``-j`` option 
enables this feature with ``execute`` and ``configure`` commands.
Templates work by substituting values from accompanying YAML files.

What is Jinja?
--------------

Jinja is a modern templating engine that simplifies network 
automation tasks. Templates provide a structured approach to 
managing complex command sequences and device configurations.

Benefits:

- Clear overview through YAML value files
- Reduced manual configuration effort  
- Minimized risk of configuration errors
- Reusable templates across multiple devices

Template Example
----------------

The following example demonstrates pagent traffic configuration
using Jinja2 templates. This template configures traffic streams
with L2 and L3 source and destination addresses.

**pagent_traffic.j2 Template:**

.. code-block:: jinja

   {% if pagent is defined %}
       {% for name, attr in pagent.items() %}
           # Traffic stream {{ name }}
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
       {% endfor %}
   {% endif %}

**Corresponding jinja_args.yaml Values File:**

The YAML file below provides configuration values for a traffic 
stream named 'ff07::1', including packet rate and L2/L3 addressing
details:

.. code-block:: yaml

   pagent:
     'ff07::1':
       rate: 5
       l2_src: 5254.0001.9765
       l2_dest: 3333.0000.0001
       l3_src: 4000::2
       l3_dest: ff07::1

**Executing the Template:**

Apply the Jinja template to a pagent device using the ``execute`` 
command with the ``-j`` flag passing the template and YAML file paths as 
arguments:

.. code-block:: console

   (lamp-p225) execute -j pagent_jinja.j2 jinja_args.yaml
   
   2024-08-01 14:10:43,092: %UNICON-INFO: +++ p225 with via 'a': executing command '!' +++
   !
   p225#
   
   2024-08-01 14:10:43,234: %UNICON-INFO: +++ p225 with via 'a': executing command '!' +++
   !
   p225#
   
   2024-08-01 14:10:43,264: %UNICON-INFO: +++ p225 with via 'a': executing command '# Traffic stream ff07::1' +++
   # Traffic stream ff07::1
   p225#
   
   2024-08-01 14:10:43,366: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn add IP' +++
   tgn add IP
   p225#
   
   2024-08-01 14:10:43,469: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn name ff07::1' +++
   tgn name ff07::1
   p225#
   
   2024-08-01 14:10:43,571: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn on' +++
   tgn on
   p225#
   
   2024-08-01 14:10:43,674: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn rate 5' +++
   tgn rate 5
   p225#
   
   2024-08-01 14:10:43,776: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn L2-src-addr 5254.0001.9765' +++
   tgn L2-src-addr 5254.0001.9765
   p225#
   
   2024-08-01 14:10:43,868: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn L2-dest-addr 3333.0000.0001' +++
   tgn L2-dest-addr 3333.0000.0001
   p225#
   
   2024-08-01 14:10:43,970: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn Layer 3 ipv6' +++
   tgn Layer 3 ipv6
   p225#
   
   2024-08-01 14:10:44,073: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn L3-src-addr 4000::2' +++
   tgn L3-src-addr 4000::2
   p225#
   
   2024-08-01 14:10:44,175: %UNICON-INFO: +++ p225 with via 'a': executing command 'tgn L3-dest-addr ff07::1' +++
   tgn L3-dest-addr ff07::1
   p225#
   
   2024-08-01 14:10:44,278: %UNICON-INFO: +++ p225 with via 'a': executing command '!' +++
   !
   p225#

**How It Works:**

When both template and YAML files are provided, LAMP processes 
the template by substituting YAML values and executes the 
resulting commands automatically on the target device.

**Generated Blitz Action:**

LAMP automatically generates a Blitz action snippet 
containing all executed commands from the Jinja template 
application:

.. code-block:: console

   (lamp-p225) list 1
   execute:
     device: p225
     command: |-
       !
       !
       # Traffic stream ff07::1
       tgn add IP
       tgn name ff07::1
       tgn on
       tgn rate 5
       tgn L2-src-addr 5254.0001.9765
       tgn L2-dest-addr 3333.0000.0001
       tgn Layer 3 ipv6
       tgn L3-src-addr 4000::2
       tgn L3-dest-addr ff07::1
       !
   (lamp-p225)