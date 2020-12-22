.. _util:

Utility Class
=============

Introduction
------------
``util`` module is located in ``metaparser`` package `util` directory along with 
few other utility modules like ``schemaengine`` and ``exceptions``. This module 
defines a set of methods that perform common, often re-used functions to help 
parser developers in manipulating the parser output data structures.

Usage example
-------------
All the methods defined in ``util`` module are under :staticscope:`static scope <http>`

The following example shows the usage of ``util`` functions:


.. code-block:: python

    # imports utility methods
    # -----------------------
    from genie.metaparser.util import keynames_exist, \
                                      keynames_convert, \
                                      reform_nestdict_from_keys

    dic = {'interface': 'loopback1', 
                    'address': {'ip': '1.1.10', 'mask': '24'}}

    # validate the mandatory keys are in dict

    keynames_to_check = ['interface', 'address.ip']
    assert keynames_exist(dic, keynames_to_check) == None
    
    # changing the keynames to agree with the schema
    
    names_mapping =  [('address.ip','ip_address'), ('interface','intf')]
    result = keynames_convert(dic, names_mapping)
    assert 'ip_address' in result['address']
    assert 'intf' in result
    
    # reforming a new dict contains only the desired keys
    
    keys = [['address','ip_address'], ['address','mask']]
    new_dict = reform_nestdict_from_keys(dic, keys)
    assert 'ip_address' in new_dict['address']
    assert 'mask' in new_dict['address']
    assert 'intf' not in new_dict

--------------------------------------------------------------------------------
