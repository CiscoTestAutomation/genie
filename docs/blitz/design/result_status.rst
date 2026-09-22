.. _result_status:

Changing the result status
=================================

The user can now change the result status to failed, passed, aborted, blocked, skipped, errored
or passx when the step is passed. This feature is supported by all the actions.
In the example below, result_status is changed to ``passx``.

.. code-block:: YAML

    - execute: # ACTION
        # (Either device hostname or device alias)
        device: R1
        # Send show version to the device
        command: show version
        # To Change the result status
        result_status: passx

In the example below, if include or exclude conditions are met, their results will be
changed to ``failed``.

Example with include and exclude:

.. code-block:: YAML

    - execute: # ACTION
        # (Either device hostname or device alias)
        device: R1
        # Send show version to the device
        command: show version
        # To Change the result status
        result_status: failed
        # Can have as many items under include or exclude that you want
        include:
            - 'CSR1000V'
        exclude:
            - 'Should not be in the output'

