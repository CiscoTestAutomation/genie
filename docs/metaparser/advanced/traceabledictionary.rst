.. _TraceableDict:

Traceable Dictionary
====================

Introduction
------------
Visit :ref:`MetaParser_Key_Usage_Traceability` for the design motivation.

``tracabledict`` module located in ``metaparser`` package `util` directory 
(metaparser.util). This module provides dictionary (e.g.:: metaparser output) 
key-usage traceability.


TraceableDict Class
-------------------

``TraceableDict`` is a subclass of Python dict that provides functionality of 
key usage tracking. The class allows to convert the native ``dict`` into 
``TraceableDict`` data structure. All Python common  dictionary key usage 
functionalities, for example:
 - dict['xx']
 - dict.keys()
 - dict.items()
 - dict.values()
 - dict.get()
 - dict.copy()
 - dict.pop()
will be traced and saved into class variable - `tracer` for future access.

**class variable**:
    - tracer: class variable to hold dictionary name and its key 
      usage record, for example: {ShowVersion: {usage}, ShowBgp: {usage}}

**instance attributes**:
    - key_map: dict to store the current key name and its key path
    - dictname: dictionary identity.

**class functionalities**:
    - convert: class method to recursively convert Pyhton nested dict 
      into `TraceableDict`.
      For example:

      .. code-block:: python

          from genie.metaparser.util.traceabledict import TraceableDict
          d = {'a': {'aa': 'xxx'}}
          t = TraceableDict.convert(d, 'my_traced_dict')
          assert('TraceableDict'== t['a'].__class__.__name__)
          
          # access the key usage
          TraceableDict.tracer