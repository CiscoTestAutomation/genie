
Verifying actions output
==========================


As it was mentioned when introducing different actions, users can query
output of an action, and verify if the output is as expected. Various forms 
of querying and verification is provided. For instance you can see:

* if a key/value pair does exist in the JSON output of an action.
* if an element or a string pattern does exist in the List output of an action.
* if output of an api is True/False
* if numerical output of an action is equal, greater (greate equal) or smaller (smaller equal) then a certain value.
* if numerical output of an action is within a specific range.

Keywords ``include`` and ``exclude`` can be used to apply a query for verification. ``include`` would 
make sure that you are query is validated and true. On the other hand ``exclude`` is useful for negative testing and
make sure a certain query is not applicable on an action output.


.. code-block:: YAML


    # Description: This would check whether the output of the parser (JSON) contains a key
    # "WebUI" in it and also no value for "platform" is provided in the JSON output.

    - apply_configuration:
              - parse:
                  command: show version
                  device: PE2
                  include:

                    # we want to se if the result of this query
                    # is not a empty dictionary
                    - contains('WebUI', regex=True)
                  exclude:

                    # The output of the query is 'VIRTUAL XE'
                    # but we hope that the key 'platform' has no value
                    # or does not exist within the dictionary by using
                    # the exclude keyword
                    - get_values('platform')

Different mechanisms is used depending the type the action output.
Supported types are ``JSON``, ``List``, ``Boolean`` and ``Numerical``. 
Example for how to verify the actions output is provided :ref:`here<types>`.


Following you can see the list of supported data types:

.. toctree::
    :maxdepth: 4
 
    types