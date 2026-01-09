NX-OS Specific Considerations
=============================

This article describes practical considerations and recommendations for using LAMP on Cisco NX-OS devices.

Verifying 'show' command outputs in JSON format
-------------------------------------------------

The Blitz framework does not natively support parsing structured JSON output from
Cisco NX-OS ``show ... | json`` commands. The ``execute_and_parse_json`` API bridges
this gap by executing a command that returns JSON output, parsing the JSON into a
dictionary, and returning it so that it can be queried using Dq expressions.

**API Overview:**

.. code-block:: python

    def execute_and_parse_json(device, command):
        ''' execute the specified command on the device which must return output in JSON format.
            The JSON is parsed into a dict.

            Args:
                device (`obj`): Device object
            Return:
                output (`dict`): parsed JSON output from command on device as a dict
        '''

**Practical example**

In this example, we use ``execute_and_parse_json`` to run ``show vrf default | json``,
parse the JSON response, and then apply a Dq query to confirm that the VRF ID in
the output matches the expected value (``vrf_id = 1``):

.. code-block:: console

    (lamp-uit-tor13) api -i execute_and_parse_json
    execute the specified command on the device which must return output in JSON format.
    The JSON is parsed into a dict.

    Args:
        device (`obj`): Device object
    Return:
        output (`dict`): parsed JSON output from command on device as a dict 

    device: uit-tor13
    command: show vrf default | json
    2026-01-06 14:39:12: %LAMP-INFO: +..............................................................................+
    2026-01-06 14:39:12: %LAMP-INFO: :                Api 'execute_and_parse_json' with parameters:                 :
    2026-01-06 14:39:12: %LAMP-INFO: :                             device: 'uit-tor13'                              :
    2026-01-06 14:39:12: %LAMP-INFO: :                      command: 'show vrf default | json'                      :
    2026-01-06 14:39:12: %LAMP-INFO: +..............................................................................+

    2026-01-06 14:39:13,149: %UNICON-INFO: +++ uit-tor13 with via 'cli': executing command 'show vrf default | json' +++
    show vrf default | json
    {"TABLE_vrf": {"ROW_vrf": {"vrf_name": "default", "vrf_id": "1", "vrf_state": "Up", "vrf_reason": "--"}}}
    uit-tor13# 
    2026-01-06 14:39:13: %LAMP-INFO: +..............................................................................+
    2026-01-06 14:39:13: %LAMP-INFO: :                                  API Output                                  :
    2026-01-06 14:39:13: %LAMP-INFO: +..............................................................................+
                                                            {                                                       
                                                                'TABLE_vrf': {                                      
                                                                    'ROW_vrf': {                                    
                                                                        'vrf_name': 'default',                      
                                                                        'vrf_id': '1',                              
                                                                        'vrf_state': 'Up',                          
                                                                        'vrf_reason': '--'                          
                                                                    }                                               
                                                                }                                                   
                                                            }                                                       
    2026-01-06 14:39:13: %LAMP-INFO: +..............................................................................+
    2026-01-06 14:39:13: %LAMP-INFO: +..............................................................................+
    2026-01-06 14:39:13: %LAMP-INFO: :                          Collecting INCLUDE Entries                          :
    2026-01-06 14:39:13: %LAMP-INFO: +..............................................................................+
    ROOT
    └── (1) TABLE_vrf
        └── (2) ROW_vrf
            ├── (3) vrf_name: default
            ├── (4) vrf_id: 1
            ├── (5) vrf_state: Up
            └── (6) vrf_reason: --
    Enter Dq item (or) line numbers (Press enter for multiple entries): vrf_id='1'
    contains_key_value('vrf_id', '1')
    {'TABLE_vrf': {'ROW_vrf': {'vrf_id': '1'}}}
    Do you wish to add this Dq query (Y/n): 

The final generated Blitz action snippet for the above example is as follows:

.. code-block:: yaml

    - api:
        function: execute_and_parse_json
        arguments:
            device: uit-tor13
            command: show vrf default | json
        include:
            - contains_key_value('vrf_id', '1')
