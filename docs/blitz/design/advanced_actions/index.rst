


Advanced Actions
===================


Up to this point of this tutorial, we were mainly talking about how to operate with *Blitz* and execute
different actions in a sequential manner. This means that upon running the *trigger_datafile*
actions are getting executed one after the other and each action should completely finish its job before
another action starts.

*Blitz* advanced actions are a form of action that will be introduced on top of a group actions
and modify implementation behaviour of said actions.
*Blitz* currently supports three advanced actions:

* :ref:`parallel<advanced>`: actions under this keyword will be executed concurrently.
* :ref:`loop<advanced>`: loop is a sequence of actions that is iterated until a certain terminating condition is reached.
* :ref:`run_condition<advanced>`: actions under this keyword will be executed after checking the truthness of a conditional statement.


.. toctree::
    :maxdepth: 4
    :hidden:

    advanced
