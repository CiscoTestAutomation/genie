.. _negative:

Negative testing
================

You can get a Passed result for an action that is expected to fail by setting the key; ``expected_failure: True``. 
Actions, [``configure``, ``execute``, ``parse``, ``learn``, ``api``, ``rest``, ``bash_console``] support this feature.

.. code-block:: YAML


    - configure:
        command: feature bgp
        device: PE1
        expected_failure: True
        timeout: 100


In above example The command supposedly doesnt exist on device PE1
so action should error out but since it was anticipated that the command wouldn't work.
The final results would be shown as passed.

