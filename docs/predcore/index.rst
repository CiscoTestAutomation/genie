.. _predcore:
Predicates
==========

A predicate is a simple truth checker object inheriting from `Predicate`.

The following :voD:`VoD <http>` gives a quick introduction to predicate-based
testing.

When a `Predicate` is tested for truth, a user-defined checking behavior is
automatically invoked.  Thus, complex testing may be wrapped up into a simple
truth test.


Let's illustrate the concept of a `Predicate` by creating a new predicate class
that accepts a number when it is constructed.  The predicate only tests
`True` when that number is even::

        from genie.predcore import Predicate

        class IsEvenPredicate(Predicate):
            ''' Predicate that tests True if the input value is even '''

            def __init__(self, value):
                self._value = value

            def dump(self):
                return "IsEvenPredicate({})".format(self._value)

            def test(self):
                return (self._value % 2 == 0)

        numsToList = [1, 6, 8, 9]
        for num in numsToList:
            pred = IsEvenPredicate(num)
            print ("          Testing {}".format(pred.dump()))
            if pred :
                print ("{} is even.".format(num))

        IsEvenPredicate(8).assert_test()
        IsEvenPredicate(9).assert_test()

        IsEvenPredicate(8)()
        IsEvenPredicate(9)()


This example produces the following output (notice the
`assert_test <Predicate.assert_test>` silently passes when the number being
tested is even but raises a signal when the number is odd)::

                  Testing IsEvenPredicate(1)
                  Testing IsEvenPredicate(6)
        6 is even.
                  Testing IsEvenPredicate(8)
        8 is even.
                  Testing IsEvenPredicate(9)


        (signal gets raised)
        genie.predcore.PredicateTestedFalseSignal: IsEvenPredicate(9)

        True
        False


A `Predicate` is a class that has the following properties:

    #. It has a `test <Predicate.test>` method that executes a test and returns `True` or `False`.  This method is overloaded and typically runs CLI commands on a device,  determining the truth value to return based on the device's response.

    #. Whenever an object inheriting from `Predicate` is tested for truth (for example, in an `if` statement), its `test <Predicate.test>` method is automatically called.

    #. It has an `assert_test <Predicate.assert_test>` method that is used to ensure a predicate tests `True` (if it doesn't, a signal is raised).

    #. It has an optional `dump <Predicate.dump>` method that, if overloaded, provides a powerful way to pass relevant information when the predicate does not test to the expected value.

    #. It can be called in order to perform its truth test, returning either `True` or `False`.  This makes `Predicate` interoperable with commands such as `threading.Condition.wait_for` or `asyncio.wait_for`.



Let's see a more device-centric example.  Assume we have an
`InterfaceUpPredicate` class that has its `test <Predicate.test>` method
overloaded to run a `show interface` command on a device, parse the result,
and determine if the requested interface is operationally and administratively
up::

        if_name = 'GigabitEthernet0/0'

        check_pred = InterfaceUpPredicate(
                        device         = my_device,
                        interface_name = if_name)

        if check_pred:
            print("Interface is up.")
        else:
            print("Interface is down.")


Predicates that contain other Predicates
----------------------------------------

Let's say that we want to validate that a series of interfaces are up by doing
only a single truth test.

This can be done using `AndPredicate`, which is a predicate that accepts a
series of user-defined objects that are able to be tested for truth.  These
objects don't have to be `Predicates <Predicate>`, but in this example they
will be.

Every time this predicate is tested for truth, all contained objects are
scheduled for re-testing.  If any object in the series tests `False`, then the
predicate itself tests `False` and the remaining objects remain un-tested.

Let's assume that `InterfaceUpPredicate` can accept an interface object
that knows its attached device and interface name::

        all_interfaces_up_pred = AndPredicate(
                InterfaceUpPredicate (interface_object = interface_1),
                InterfaceUpPredicate (interface_object = interface_2),
                InterfaceUpPredicate (interface_object = interface_3),
            )

        if all_interfaces_up_pred:
            print ("All interfaces are up.")
        else:
            print ("Not all interfaces are up.")


Timed Looping Predicates
------------------------

Predicates that periodically test a series of objects for truth are particularly
useful when doing initial test setup.  :mod:`predcore` provides several such
pre-requisite classes.

Prerequisite
------------

When a `Prerequisite` object is tested for truth, it periodically checks a
series of user-defined contained objects for truth until either they all test
`True` or a timeout is hit.  These objects are typically
`Predicates <Predicate>` but could be any object able to be tested for truth.

Every time a `Prerequisite` is tested for truth, all contained objects are
re-tested.


The following snippet illustrates how a `Prerequisite` can be created and
checked::

        check_pred = InterfaceUpPredicate(
                        device         = my_device,
                        interface_name = if_name)

        interfaceIsUpPred = Prerequisite(check_pred, timeout=30)

        if interfaceIsUpPred:
            print("Interface came up within 30 seconds.")
        else:
            print("Interface did not come up within 30 seconds.")


The `assert_test <Predicate.assert_test>` method is most commonly used to check
a pre-requisite.  If the pre-requisite fails then an exception is raised that
carries with it debug information describing the failure reason::

        try:
            interfaceIsUpPred.assert_test()
        except PredicateTestedFalseSignal as e:
            log.error(e)
            print("Interface did not come up within 30 seconds."


PrerequisiteWhile
-----------------
This is a looping predicate that ensures a series of user-defined objects all
continue to test `True` for a minimum length of time.


The following snippet shows how the `PrerequisiteWhile` class may be used
to ensure an interface stays up for a minimum length of time. Notice the
`assert_test <Predicate.assert_test>` method also accepts a user-defined
failure string that is contained by the exception produced should the assertion
fail.  ::

        check_pred = InterfaceUpPredicate(
                        device         = my_device,
                        interface_name = if_name)

        interfaceStaysUpPred = PrerequisiteWhile(check_pred, timeout=30)
        try:
            interfaceStaysUpPred.assert_test(
                "Interface did not stay up for 30 seconds.")
        except PredicateTestedFalseSignal as e:
            log.error(e)

Finally, here's an example of a test that ensures a series of interfaces stay up
for a minimum length of time.  If the test fails, the interface that did not
stay up is included in the signal and is logged to facilitate debugging::

        interfaceStaysUpPred = PrerequisiteWhile(
                InterfaceUpPredicate (interface_object = interface_1),
                InterfaceUpPredicate (interface_object = interface_2),
                InterfaceUpPredicate (interface_object = interface_3),
                timeout=30)

        try:
            interfaceStaysUpPred.assert_test(
                "Interfaces did not stay up for 30 seconds.")
        except PredicateTestedFalseSignal as e:
            log.error(e)




API Reference
-------------

Base Class for Truth Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: genie.predcore::Predicate
    :members: test, dump, assert_test, last_result

.. autoclass:: genie.predcore::PredicateTestedFalseSignal

Classes for Looped / Timed Predicate Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: genie.predcore::Prerequisite
    :members: time_remaining, assert_test


.. autoclass:: genie.predcore::PrerequisiteWhile
    :members: time_remaining, assert_test

Classes for Logical Predicate Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: genie.predcore::AndPredicate
    :members: last_passed, last_failed, last_untested, assert_test

.. autoclass:: genie.predcore::OrPredicate
    :members: last_passed, last_failed, last_untested, assert_test

.. autoclass:: genie.predcore::NotPredicate
    :members: assert_test

List and Dictionary Comparison Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: genie.predcore::ListEqualPredicate
    :members: assert_test

.. autoclass:: genie.predcore::DictEqualPredicate
    :members: assert_test

.. autoclass:: genie.predcore::IsSequenceEqualDiffPredicate
    :members: assert_test


Generic Function Call Response Checking Class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: genie.predcore::FunctionCallEqualsPredicate
    :members: assert_test



Other Predicate Classes
^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: genie.predcore::InPredicate
    :members: assert_test

.. autoclass:: genie.predcore::InRangePredicate
    :members: assert_test

.. autoclass:: genie.predcore::IsSubsetPredicate
    :members: assert_test

.. autoclass:: genie.predcore::IsSupersetPredicate
    :members: assert_test


.. sectionauthor:: Myles Dear <mdear@cisco.com>
