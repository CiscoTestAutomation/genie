.. _subsections:

Subsections
===========

All :subsections:`Subsections <http>` are executed in the common setup and the common cleanup and
does not run between `Triggers`. As it is run only in common setup or common
cleanup, it allows ``Genie`` to perform certain tasks, such as take complete
snapshot of all the features configured on the device, backup configuration to
the cloud, restore configuration from the cloud, without impacting the execution
time.

More information can be found in the :ref:`user guide <Subsections>`.


Using Subsections
-----------------

Now, let's see how to create a `Subsection` `profile`.

Step 0: Write a new `Subsection` method or update an existing `Subsection`.

Step 1: Add your Subsection information to the `subsection_datafile` as shown
below.

.. note::

    Create a subsection_datafile as per the below schema that extends
    from the master one as illustrated below.

.. code-block:: yaml

    extends: # Use this field to extend an existing yaml subsection datafile,
             # allowing you to create an inheritance hierarchy.
             # Supports full path/names or name of file in the same dir.
             # ``Genie`` provides a Master set of subsection datafile for you to
             # extend from as a start. It is found at:
             # <$virtual_env>/projects/genie_libs/sdk/yaml/subsection_datafile.yaml

    setup:
        sections:
            # define a subsection with additional parameters
            <subsection name>:
                method: <your method location, for example: genie.subsection_1>
                parameters:
                     <key>: <value>
            # define a subsection without additional parameters
            <subsection name>:
                method: <your method location, for example: genie.subsection_2>
        order: [<list of existing subsections in a desired order>]

    cleanup:
        sections:
            # define a subsection with additional parameters
            <subsection name>:
                method: <your method location, for example: genie.subsection_1>
                parameters:
                     <key>: <value>
            # define a subsection without additional parameters
            <subsection name>:
                method: <your method location, for example: genie.subsection_2>
        order: [<list of existing subsections in a desired order>]

.. note::

    If you want to reuse some of the subsections, please define a unique
    subsection name, method with/without additional parameters.

    Defined subsection name will replace the subsection method name in the
    execution result/log.

.. note::

    Only the section defined in the order will be executed

.. note::

    Feel free to add more keys from the datafile schema.

Step 3: Ensure the `job` file is pointing to this file via the
`subsection_datafile` argument.

.. code-block:: text

    subsection_datafile="<path to your file created above>"

Step 4: To run `Subsections`, execute your job via easypy with the required
arguments.
