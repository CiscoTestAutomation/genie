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
      request_mode:     # [STREAM, ONCE, POLL] gNMI subscription mode
      sub_mode:         # [ON_CHANGE, SAMPLE] gNMI subscription sub_mode
      encoding:         # [JSON, JSON_IETF, PROTO, ASCII] gNMI val encoding
      prefix:           # [true | false] gNMI message requires PATH prefix
      origin:           # [openconfig | rfc7951 | module | <device defined> ] gNMI origin
      base64:           # [true | false] gNMI set "val" requires Base64 encoding
      sample_poll:      # number of seconds between SAMPLE sub_mode or POLL request_mod
      stream_max:       # seconds to stop stream (default: 120, no max)
      auto-validate:    # [true | false] automatically validate config messages
      negative_test:    # [true | false] expecting device to return an error
      pause:            # pause N seconds between each test (default: 0, no pause)
      transaction_time: # number of seconds that determines the maximum time that can pass between sending a request and receiving a response
      updates_only:     # only for Subscribe requests, determines if only updates should be received (default: false)

request_mode
~~~~~~~~~~~~

`gNMI subscriptions`_ are open gRPC channels to a device which receive telemetry updates associated to
a resource on the device.  The yang action subscribes to that resource.

- STREAM - the channel stays open and receives data until *stream_max* times out.
- ONCE - the channel stays open and receives data until the first response is complete.
- POLL - the channel stays open and receives data only when a POLL message is sent to the device.

.. _gNMI subscriptions: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#35-subscribing-to-telemetry-updates

sub_mode
~~~~~~~~

gNMI subscriptions can have sub-modes associated to a request_mode.

- ON_CHANGE - data is sent when the resource on the device has changed state either by a config change
or a device runtime change depending on which resource you are monitoring.
- SAMPLE - data is sent in the specified sample_interval.

encoding
~~~~~~~~

gNMI messaging can request different structured datatypes.

- JSON - defined in `RFC 7159`_
- JSON_IETF - defined in `RFC 8259`_
- PROTO - defined in gNMI specification `2.3.3`_
- ASCII - defined in gNMI specification `2.3.4`_

.. _RFC 7159: https://datatracker.ietf.org/doc/html/rfc7159
.. _RFC 8259: https://datatracker.ietf.org/doc/html/rfc8259
.. _2.3.3: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#233-protobuf
.. _2.3.4: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#234-ascii

prefix
~~~~~~

gNMI messages contain a Path component that points to a specific resourse(s) on the device.  It is possible
to define a common Path called a `prefix`_.  If the prefix is defined, any Path definitions in the message
will be appended to this prefix.

.. _prefix: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#241-path-prefixes

origin
~~~~~~

gNMI messages, as well as having a specified encoding, can also structured following a specific schema referred to
as the `origin`_.

- openconfig - the default schema
- rfc7951 - follows the JSON schema
- module - the schema is the YANG module that defines the resource that is the target of the message
- device defined - any value that the specific device and client understand

.. _origin: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#222-paths

base64
~~~~~~

gNMI JSON or JSON_IETF encoded messages can contain a `val`_ parameter.  This represents the body of the message
that a Path is pointing to.  Some clients compress the val into a Base64 encoding which allows for a more efficiant
use of badnwidth.  The device must be able to decode the Base64 val if this parameter is set.

.. _val: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#231-json-and-json_ietf

sample_poll
~~~~~~~~~~~

gNMI STREAM subscriptions can ask for a sampling interval in which messages are sent.  The device will only send
data at these intervals.  Make sure STREAM sub_mode "SAMPLE" is less than the stream_max. For POLL it indicates how many seconds between POLL requests. 
For SAMPLE sub_mode the field is equivalent to the `sample_interval`_ field but value is defined in seconds. Default value is 5.

.. _sample_interval: https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#35152-stream-subscriptions

stream_max
~~~~~~~~~~

gNMI STREAM subscriptions will last as long as the gRPC channel is open.  Without this parameter set,
the test may never end.  The parameter is set in seconds.

auto-validate
~~~~~~~~~~~~~

This is a general setting that instructs the infrastructure to automatically send a get related NETCONF or
gNMI message to ensure that any configuration message was successful.

negative_test
~~~~~~~~~~~~~

This is a general setting that instructs the infrastructure that the message sent is expected to return an
error.  The structure of the error can be defined in the return.  If the error is encountered, the test is
condidered successful.

pause
~~~~~

This is a general setting that instructs the infrastructure to stop between each message sent to the device.
The parameter is set in seconds.  It is primarily used to slow down test execution and is really just for
debugging purposes.  If a device needs you to slow down, it is not handling the messaging properly and this
should be further investigated.

transaction_time
~~~~~~~~~~~~~~~~
For a GET, the maximum time that can elapse between sending a request and the response completing.
For gNMI subscriptions in STREAM mode, this is the time between a response arriving and the response completing. If time is exceeded, the test will fail.

updates_only
~~~~~~~~~~~~	
A boolean that causes the server to send only updates to the current state. For STREAM subscriptions, an update occurs upon the next sample 
(in the case of SAMPLE subscriptions), or upon the next value change for ON_CHANGE subscriptions. For POLL and ONCE subscriptions, 
the target should send only the sync_response message, before proceeding to process poll requests (in the case of POLL) or closing the RPC (in the case of ONCE).

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
          negative_test: true
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
        negative_test: true
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


- edit-config negative test RPC error check using NETCONF

.. code-block:: YAML

    - yang:
        device: uut2
        connection: netconf
        operation: edit-config
        protocol: netconf
        banner: NETCONF EDIT-CONFIG MESSAGE
        log: Negative test case
        format:
          auto-validate: false
          negative_test: true
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            value: '10.10.10.2'
            edit-op: create
        returns:
          - id: 1
            name: error-tag
            op: ==
            selected: true
            value: data-exists
            xpath: /rpc-reply/rpc-error/error-tag


- Same edit-config RPC error check using variables

.. code-block:: YAML

  extends: data_test_file.yml

    - yang:
        device: '%{ data.device }'
        connection: '%{ data.connection }'
        operation: edit-config
        protocol: '%{ data.protocol }'
        datastore: '%{ data.datastore }'
        format: '%{ data.format.2 }'
        banner: YANG EDIT-CONFIG MESSAGE
        content: '%{ data.contents.1 }'
        returns: '%{ data.returns.1 }'
        banner: NETCONF EDIT-CONFIG MESSAGE
        log: Negative test case


.. code-block:: YAML

  # data_test_file.yml contents

  data:
    device: uut2
    connection: netconf
    protocol:netconf
    datastore: running

    format:
      1:
        auto-validate: true
        negative_test: false
        pause: 0
        timeout: 30
      2:
        auto-validate: false
        negative_test: true
    contents:
      1:
        namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
        nodes:
        - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
          value: '10.10.10.2'
          edit-op: create
    returns:
      1:
        - id: 1
          name: error-tag
          op: ==
          selected: true
          value: data-exists
          xpath: /rpc-reply/rpc-error/error-tag


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
            

- gNMI STREAM subscribe testing IPv4 statistic values >= n.

.. code-block:: YAML

    - yang:
        banner: YANG SUBSCRIBE STREAM SAMPLING
        connection: gnmi
        operation: subscribe
        protocol: gnmi
        datastore:
          lock: true
          retry: 40
          type: ''
        device: uut
        format:
          encoding: JSON
          request_mode: STREAM
          sample_interval: 5
          stream_max: 20
          auto_validate: false
          negative_test: false
          pause: 0
          timeout: 30
        log:
          category: test
          module: Cisco-NX-OS-device
          name: nx-ipv4-stats
          revision: '2021-12-14'
        content:
          namespace:
            top: http://cisco.com/ns/yang/cisco-nx-os-device
          nodes:
          - datatype: ''
            default: ''
            edit-op: ''
            nodetype: container
            value: ''
            xpath: /top:System/top:ipv4-items/top:inst-items/top:iptrafficstat-items
        returns:
        - id: '1'
          name: consumed
          op: '>='
          selected: true
          value: '17852'
          xpath: /System/ipv4-items/inst-items/iptrafficstat-items/consumed
        - id: '22'
          name: received
          op: '>='
          selected: true
          value: '452581'
          xpath: /System/ipv4-items/inst-items/iptrafficstat-items/received
        - id: '23'
          name: sent
          op: '>='
          selected: true
          value: '13102'
          xpath: /System/ipv4-items/inst-items/iptrafficstat-items/sent


- gNMI ON_CHANGE subscribe testing config changes to a boolean.
**NOTE:**
For ON_CHANGE the returns must contain the base value of the resource as well
as any changes to the resource setup in the test.

.. code-block:: YAML

    - configure:
        banner: CONFIG SETUP FOR ON_CHANGE
        device: uut
        command: ip igmp heavy-template
    - yang:
        banner: YANG SUBSCIBE ON_CHANGE
        connection: gnmi
        content:
          namespace:
            top: http://cisco.com/ns/yang/cisco-nx-os-device
          nodes:
          - datatype: boolean
            nodetype: leaf
            xpath: /top:System/top:igmp-items/top:inst-items/top:heavyTemplate
        datastore:
          lock: true
          retry: 40
          type: 'running'
        device: uut
        format:
          encoding: JSON
          request_mode: STREAM
          sub_mode: ON_CHANGE
          stream_max: 10
          auto_validate: false
          negative_test: false
          pause: 0
          timeout: 30
        log:
          category: test
          module: Cisco-NX-OS-device
          name: on_change
          revision: '2021-12-14'
        operation: subscribe
        protocol: gnmi
        returns:
        - id: '0'
          name: heavyTemplate
          op: ==
          selected: true
          value: true                                         # the base value
          xpath: /System/igmp-items/inst-items/heavyTemplate
        - id: '1'
          name: heavyTemplate
          op: ==
          selected: false                                     # the change value
          value: true
          xpath: /System/igmp-items/inst-items/heavyTemplate
    - configure:
        banner: CONFIG CHANGE FOR ON_CHANGE
        device: uut
        command: no ip igmp heavy-template
    - configure:
        banner: CONFIG CHANGE FOR ON_CHANGE
        device: uut
        command: ip igmp heavy-template
    - configure:
        banner: CONFIG CHANGE FOR ON_CHANGE
        device: uut
        command: no ip igmp heavy-template
