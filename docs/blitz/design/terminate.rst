.. _terminate:

Script termination on failure
===============================

By default blitz actions and sections continue to work even after a failure. However, users can manually adjust their
testscripts so the script stop upon failure. Below example shows how to achieve that.

.. code-block:: YAML

    - test_sections:
        - apply_configuration:
            - continue: False
            - configure:
                command: router bgp 6500
                device: PE2
        - confirm_actions:
            - execute:
                continue: False
                command: show interface
                device: PE2
            - execute:
                command: show module
                device: P2

In the section apply_configuration in action level ``- continue: False`` is set, so if the result of the section is
a failure the script stops the run of the rest of the sections in the testscript.

In the section confirm_actions, in the first action ``execute`` a keyword ``continue`` is added with value ``False``.
That would send the signal that upon failure of an action the rest of the actions in that section should not be running.

.. note::

    Due to limitation on some of the pyATS libraries that Blitz uses, currently it is not possible to set ``continue: False`` under parallel keyword and terminate 
    the section upon failure.