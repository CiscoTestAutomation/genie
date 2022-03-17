.. _yang action:

yang
^^^^

YANG, "Yet Another Network Generation", `RFC 6020`_, is a data modeling language used to
model configuration and state data on network devices. The model is represented
in a hierachal fashion and can be presented in many ways, one of which is the
"Xpath". The ``content`` of a simple YANG message can be boiled down to 3 required
components.

.. _RFC 6020: https://datatracker.ietf.org/doc/html/rfc6020

* Xpath based on `XML Path Language 1.0`_ identifying a resource

.. _XML Path Language 1.0: https://www.w3.org/TR/1999/REC-xpath-19991116/

* `Namespaces in XML 1.0`_

.. _Namespaces in XML 1.0: https://www.w3.org/TR/REC-xml-names/

* The value you wish to set the resource to

Several Xpath/value pairs can construct a complex message. This is the format the
``yang`` action follows when defining simple or complex messages.

Description of Available YAML Components
----------------------------------------

.. code-block:: YAML

    - yang:
        device: # device name or alias
        connection: # device interface connection (in testbed file)
        operation:  # YANG message operation (based on NETCONF but mapped to other protocols)
                    # * edit-config - see Content section "edit-op" for protocol mappings
                    # * get-config  - mapped to "get CONFIG mode" for gNMI and GET for RESTCONF
                    # * get         - mapped to "get STATE mode" for gNMI and GET for RESTCONF
                    # * subscribe
                    # * capabilities
        protocol: # [ netconf | gnmi | restconf ] - see Protocol Specifications section
        datastore: # YANG datastores (if not defined Blitz will choose from device capabilities)
        format: # Various fomat options (see Format options below)
        banner: # (optional) Prominant log message with borders
        log: # (optional) Log INFO message
        content: # Content of YANG message being sent (see Content section below)
        returns: # (optional) Expected return of YANG message (see Returns section below)

Protocol Specifications
-----------------------

YANG modeling is a definition of network device management APIs, not the actual source code that
interacts with those APIs.  3 messaging protocols are specified to actually send the management
requests to the modeled APIs.  The details of those protocols are too extensive to get into for
this documentation.  Each have their advantages and disadvantages. The `NETCONF protocol`_
has the most extensive functionality of all 3 protocols, but, it is transfered in XML format
which can be more taxing on network resources.  The `gNMI protocol`_ is more efficient and flexible
but does not have all the options available with NETCONF.  The `RESTCONF protocol`_ are basically
REST APIs that many engineers are comfortable with but it also does not have all the options
available with NETCONF.

The ``yang`` action, will take the basic YANG metadata and construct the properly formed message
according to the "protocol" parameter setting and send the message using the chosen protocol
libraries.

.. _NETCONF protocol: https://datatracker.ietf.org/doc/html/rfc6241
.. _gNMI protocol: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md
.. _RESTCONF protocol: https://datatracker.ietf.org/doc/html/rfc8040

Datastore Options
-----------------

YANG Datastores, `RFC 8342`_, are a fundamental concept binding network management data models to
network management protocols such as NETCONF `RFC 6241`_ and RESTCONF `RFC 8040`_.  It is up to the
YANG server implementation to decide which datastore to support.  Blitz supports several types.  The
default is an empty string which indicates the type will be determined by device capabilities.  If
the device supports "candidate", the candidate datastore is chosen for configuration operations.  If not
the "running" is chosen for configuration.  For all other operations, the "running" datastore is chosen.

.. _RFC 8342: https://datatracker.ietf.org/doc/html/rfc8342

.. _RFC 6241: https://datatracker.ietf.org/doc/html/rfc6241

.. _RFC 8040: https://datatracker.ietf.org/doc/html/rfc8040

.. code-block:: YAML

    datastore:
      type: ""    # [candidate, running, startup, intent, operational]
      lock: true  # [true | false] lock datastore before access
      retry: 40   # If lock is refused, retry N times pausing 1 second between each retry

Format Options
--------------

Some format options are available relating to the message and return handling. For example, if
the message is related to a ``subscribe`` operation, you will need to communicate the type of
subscription, or, you may expect the test to fail (referred to as a negative test).

.. code-block:: YAML

    format:
      request_mode:    # [STREAM, ONCE, POLL] gNMI subscription mode
      sub_mode:        # [ON_CHANGE, SAMPLE] gNMI subscription sub_mode
      encoding:        # [JSON, JSON_IETF] gNMI val encoding
      prefix:          # [true | false] gNMI message requires PATH prefix
      origin:          # [openconfig | rfc7951 | <device defined> ] gNMI origin
      base64:          # [true | false] gNMI set "val" requires Base64 encoding
      sample_interval: # number of seconds between sampling
      stream_max:      # seconds to stop stream (default: 0, no max)
      auto-validate:   # [true | false] automatically validate config messages
      negative-test:   # [true | false] expecting device to return an error
      pause:           # pause N seconds between each test (default: 0, no pause)
      sequence:        # [true | false] to check the return values and return sequence verified

Content
-------

As explained above, ``content`` contains a reference to namespaces followed by a list of
Xpath/value pairs (nodes).  Namespace with mapped prefix is defined at the top of the
YANG file.  There is also an option, "rpc", to use the string representation of the message.

.. code-block:: YAML

    content:
      namespace:
        # prefix: namespace examples:
        ios: http://cisco.com/ns/Cisco-IOS-XE-native
        config-mda-cfg: http://cisco.com/ns/yang/Cisco-IOS-XR-config-mda-cfg
        oc-if: http://openconfig.net/yang/interfaces
      nodes: # List of:
      - nodetype: # YANG defined statement such as leaf, container, etc.
        default: # Default value if not specifically set by client
        value:   # Value Xpath points to which must match the defined datatype
        edit-op: # (Optional) Applies only to edit-config (default: merge)
                 # These are mapped to gNMI and RESTCONF functionality.
                 #  ---------------------------------
                 # | NETCONF | RESTCONF | gNMI       |
                 #  ---------------------------------
                 # | create  | POST     | set/update |
                 # | merge   | PATCH    | set/update |
                 # | replace | PUT      | set/replace|
                 # | delete  | DELETE   | set/delete |
                 # | remove  | DELETE   | set/delete |
                 #  ---------------------------------
        xpath: # Xpath based on `XML Path Language 1.0`_ identifying a resource

The "rpc" option can be any well-formed valid XML NETCONF rpc message.

.. code-block:: YAML

    content:
      rpc: |
      <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
        <get>
          <filter>
            <interfaces xmlns="http://openconfig.net/yang/interfaces">
              <interface>
                <state/>
              </interface>
            </interfaces>
          </filter>
        </get>
      </rpc>

The "rpc" option can also accept a well-formed valid dictionary representing a gNMI message.

.. code-block:: YAML

    content:
      rpc: {
        "subscribe": {
          "prefix": {
            "origin": "rfc7951"
          },
          "subscription": [
            {
              "path": {
                "elem": [
                  {
                    "name": "Cisco-IOS-XE-lldp-oper:lldp-entries"
                  },
                  {
                    "name": "lldp-intf-details",
                    "key": {
                      "if-name": "TenGigabitEthernet1/0/1"
                    }
                  }
                ]
              },
              "mode": "SAMPLE",
              "sampleInterval": "5000000000"
            }
          ],
          "encoding": "JSON_IETF"
        }
      }

Returns
-------

Expected return values can also be defined with the fexibility of approximation. The return
values are identified by the Xpath derived from the return message (without prefixes because
return prefixes may differ). The ``op`` is an operation performed between returned value and
expected value.

    * ``==`` equals
    * ``!=`` not equal
    * ``<`` less than
    * ``>`` greater than
    * ``<=`` less than or equal
    * ``>=`` greater than or equal
    * ``1 - 10`` range (example)

.. code-block:: YAML

    returns:
      - id:       # for referencing only
        name:     # name of field for referencing only
        op:       # operation performed between returned value and expected value (choices above)
        selected: # set this to ``false`` and field is ignored making it like a placeholder
        datatype: # datatype of field for general verification
        value:    # expected value to compare to returned value
        xpath:    # Xpath to field in YANG model (without prefixes)

Using Variables
---------------

You should think about the portability of your test. Using variables to refer
to parameters in the ``yang`` action will allow you to run the same set of tests
over different protocols by only changing a couple variables or changing the
file that contains your content. A variable can be defined by wrapping a YAML
location inside ``%{ my.variable }`` and find the value at "my: variable: value".
The location can also exist in a different file by adding ``extends: mydata.yml``
at the top of the test file.


Example of variables in external data file:

.. code-block:: YAML

    extends: data_test_file.yml

    - yang:
        device: '%{ data.device }'
        connection: '%{ data.connection }'
        operation: edit-config
        protocol: '%{ data.protocol }'
        datastore: '%{ data.datastore }'
        banner: YANG EDIT-CONFIG MESSAGE
        content: '%{ data.content.1 }'


Content in data_test_file.yml:

.. code-block:: YAML

  data:
    device: uut1
    connection: gnmi
    protocol: gnmi
    content:
      1:
        namespace:
          ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
        nodes:
          - value: 10.10.10.2
            xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            edit-op: merge


Examples
--------

- edit-config negative test using NETCONF

.. code-block:: YAML

    - yang:
        device: uut2
        connection: netconf
        operation: get-config
        protocol: netconf
        banner: NETCONF EDIT-CONFIG MESSAGE
        log: Negative test case
        format:
          auto-validate: false
          negative-test: true
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            value: '10.10.10.2'
            edit-op: delete
        returns:
          - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id


- Same edit-config using variables

.. code-block:: YAML

  extends: data_test_file.yml

    - yang:
        device: '%{ data.device }'
        connection: '%{ data.connection }'
        operation: edit-config
        protocol: '%{ data.protocol }'
        datastore: '%{ data.datastore }'
        format: '%{ data.format.1 }'
        banner: YANG EDIT-CONFIG MESSAGE
        content: '%{ data.contents.1 }'
        banner: NETCONF EDIT-CONFIG MESSAGE
        log: Negative test case


.. code-block:: YAML

  # data_test_file.yml contents

  data:
    device: uut2
    connection: netconf
    protocol:netconf
    datastore: candidate

    format:
      1:
        auto-validate: false
        negative-test: true
    contents:
      1:
        namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
        nodes:
        - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            value: '10.10.10.2'
            edit-op: delete
    returns:
      1:
        - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id


- get CONFIG state using gNMI with expected returns

.. code-block:: YAML

    - yang:
        device: uut2
        connection: gnmi
        operation: get-config
        protocol: gnmi
        banner: gNMI GET-CONFIG MESSAGE
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
        returns:
          - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id
            

- gNMI subscribe testing a config change

.. code-block:: YAML

    - configure:
        commmand:
          - l2vpn router-id 10.10.10.1
    - sleep:
        sleep_time: 5
    - yang:
        device: uut2
        connection: gnmi
        operation: subscribe
        protocol: gnmi
        banner: gNMI SUBCRIBE MESSAGE
        format:
          request_mode: STREAM
          sub_mode: SAMPLE
          encoding: JSON_IETF
          sample_interval: 5
          stream_max: 20       # test completes after 20 seconds
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
        returns:
          - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id
    - sleep:
        sleep_time: 5
    # following event will trigger a returns check
    - configure:
        commmand:
          - l2vpn router-id 10.10.10.2
