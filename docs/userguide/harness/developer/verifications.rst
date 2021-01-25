.. _harness_verification:

Verifications
=============

<todo>

A verification is the execution of a command to retrieve the current state of a
device. The state can be retrieved with `cli`, `yang`, `xml` and so on or a mix of them. 

There are three types of verifications within Genie.

 .. figure:: VerificationSDK.png
    :align: center
    :alt: They can talk

Using Ops
---------

``Genie`` :ref:`Ops <ops_guide>` represents a device/feature operational state/data using
Python object. Each `feature` on a device is represented via a single `Ops`
object instance, where state/status information is stored as an object
attribute.

``Genie`` `Ops` objects are snapshot of a particular `Feature` on a `Device` at
a specific time. Hence `Ops`  objects are perfectly suited to be used as
comparable verification snapshot.

Now, let's see how to write one:

Step 0: Check if the ``Genie`` `Ops` class exists for the feature you want to
verify. If so, go to Step 2.

Step 1: Write an ops object for the feature you would like to verify. Once you are
finished, commit the ops object to ``Genie`` `Ops`

Step 2: Add your verification information to the `verification_datafile` as
shown below:

.. code-block:: yaml

    Verify_<feature name>:
        source:
            pkg: genie_libs.genie
            class: <your location, for example: ops.ospf.ospf.Ospf>
        exclude: [<list of generic keys to ignore in the comparison>]
        devices:
            uut:
                None
        iteration:
            attempt: 2
            interval: 10

.. note::

    Feel free to add more keys from the datafile schema.

Step 3: Ensure the `job` file is pointing to this verification
file via `verification_datafile` argument.

Step 4: To execute your verification, run your job via easypy with the
required arguments.

.. note::

     `testbed_file` is the only mandatory argument

Step 5: To add this verification to the ``Genie`` Master `verification_datafile`, 
please send an email to `asg-genie-support` for review. Once this verification is
reviewed and then added to the `verification_datafile`, other teams may easily use your 
new verification in their :ref:`verification datafile <verification_datafile>` via `extend`.

.. note::

    If you are unsure about extend, please refer to the datafile schema.

Using Template
--------------

Step 0: Do you have a parser? Great, that's all you need! If you don't have a
parser, simply write a new parser with :ref:`metaparser <metaparser>`.

Step 1: Add your verification information to the `verification_datafile` as
shown below:

.. code-block:: yaml

    Verify_<feature name>:
        exclude: [<list of generic keys to ignore in the comparison>]
        devices:
            uut:
                None
        cmd:
            pkg: genie_libs.parser
            class: <your parser location, for example: ops.ospf.ospf.Ospf>
        iteration:
            attempt: 2
            interval: 10

Step 2: Ensure the `job` file is pointing to this verification
file via the `verification_datafile` argument.

Step 3: To execute your verification, run your job via easypy with the
required arguments.

.. note::

    The only mandatory argument is the :ref:`testbed file <book_setup_testbed>`.
    

Step 4: To add this verification to the ``Genie`` Master `verification_datafile`, 
please send an email to `asg-genie-dev` for review. Once this verification is
reviewed and then added to the `verification_datafile`, other teams may easily use your 
new verification in their :ref:`verification datafile <verification_datafile>` via `extend`.

.. _harness_user_callable:

Using Callable
--------------

If the two previous sections did not meet your requirements, you
may write your own callable. However, we strongly encourage you to use the
previous sections to create your verifications as they provide users with 
multiple advantages, including: os agnostic, extensibility for different management interfaces
(Cli/Yang), among others.

Step 1: Write a callable which has `self` and `device` as its first and second
arguments. This callable needs to return a dictionary as it will be used as a
snapshot for verifications. 

.. note::

    if no comparison is needed, simply return an empty dictionary.

.. code-block::  python

    def a_callable(self, device, var1):
        device.parse('show clock')
        return {'value':var1}

Step 2: Add your callable information to the `verification_datafile` as shown
below.

.. code-block:: yaml

    Verify_<whatever you want>:
        source:
            class: <your location, for example: my.callable.function>
        exclude: [<list of generic keys to ignore in the comparison>]
        devices:
            uut:
                None
        parameters:
            var1: 9
        iteration:
            attempt: 2
            interval: 10

.. note::

    If needed, abstraction can be added with the `pkg` key.

Step 3: Ensure the `job` file is pointing to this verification
file via `verification_datafile` argument.

Step 4: To execute your verification, run your job via easypy with the
required arguments.

.. note::

    The only mandatory argument is the :ref:`testbed file <book_setup_testbed>`.

Step 5: If you now have a callable which you think should be a part of the ``Genie`` master
`verification_datafile`, please feel free to send an email to `asg-genie-dev` for
review.


Using Parameters
----------------

Step 0: Do you have a parser? Great, that's all you need! If you don't have a
parser, simply write a new parser with :ref:`metaparser <metaparser>`.

Step 1: Add your verification information to the `verification_datafile` as
shown below:

.. code-block:: yaml

    Verify_<feature name>:
        exclude: [<list of generic keys to ignore in the comparison>]
        devices:
            uut:
                None
        cmd:
            pkg: genie_libs.parser
            class: <your parser location, for example: ops.ospf.ospf.Ospf>
        iteration:
            attempt: 2
            interval: 10
        parameters:
            <key>: <value>

.. note::

    If you want to pass parameters to verification, please use key `parameters`
    and follow by your parameters.

Step 2: Ensure the `job` file is pointing to this verification
file via the `verification_datafile` argument.

Step 3: To execute your verification, run your job via easypy with the
required arguments.

.. note::

    The only mandatory argument is the :ref:`testbed file <book_setup_testbed>`.

Step 5: If you now have a callable which you think should be a part of the ``Genie`` master
`verification_datafile`, please feel free to send an email to `asg-genie-dev` for
review.

Using Processors
----------------

``Genie`` verifications are fully customizable with the help of pyats
pre/post/exception :processors:`Processors <http>` and :ref:`abstraction <abstract>`.

Step 0: You got a processor? Great, that is all you need! If you don't have a
processor, simply write a new pre/post/exception :processors:`Processors <http>`.

Step 1: Add your processors information to the `verification_datafile` as
shown below.

.. code-block:: yaml

    Verify_<feature name>:
        source:
            pkg: genie_libs.genie
            class: <your location, for example: ops.ospf.ospf.Ospf>
        exclude: [<list of generic keys to ignore in the comparison>]
        devices:
            uut:
                None
        iteration:
            attempt: 2
            interval: 10
        processors:
            pre:
                <your pre processor name>:
                    pkg: <your abstraction package, for example: genie_libs>
                    method: <your location, for example: sdk.libs.prepostprocessor.sleep_processor>
                    parameters:
                        <your parameters variable name>: <your parameters value>
            post:
                <your post processor name>:
                    pkg: <your abstraction package, for example: genie_libs>
                    method: <your location, for example: sdk.libs.prepostprocessor.sleep_processor>
                    parameters:
                        <your parameters variable name>: <your parameters value>
            exception:
                <your exception processor name>:
                    pkg: <your abstraction package, for example: genie_libs>
                    method: <your location, for example: sdk.libs.prepostprocessor.sleep_processor>
                    parameters:
                        <your parameters variable name>: <your parameters value>

.. note::

    If needed, abstraction can be added via the `pkg` key.
    If needed, extra parameters can be added via the `parameters` key.

Step 3: Ensure the `job` file is pointing to this verification
file via `verification_datafile` argument.

Step 4: To execute your verification, run your job via easypy with the
required arguments.

.. note::

    The only mandatory argument is the :ref:`testbed file <book_setup_testbed>`.

Step 5: You have a processor which you think should be part of ``Genie`` master
`verification_datafile` ?  Feel free to send an email to `asg-genie-dev` for
review to add this processor to the ``Genie`` Master `verification_datafile`.

