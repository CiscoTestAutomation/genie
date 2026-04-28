.. _reply:

Replying to the prompt dialogue
=================================

When executing or configuring commands on some devices, it is possible that you receive
a prompt message that needs to be replied. In *Blitz*, you can handle these prompt messages
automatically by using the keyword `reply` in your action. In order to reply a message,
you need to know the regex pattern of the message that would show up in the console.

Below you can see an `example` of the action ``execute`` handling a prompt message.

.. code-block:: YAML

    # Looking for the parse_output variable in the action execute
    - apply_configuration:
        - execute:
            device: PE1
            command: write erase
            reply:
            - pattern: .*Do you wish to proceed anyway\? \(y/n\)\s*\[n\]
              action: sendline(y)
              loop_continue: True
              continue_timer: False