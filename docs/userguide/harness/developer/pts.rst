PTS
===

`PTS` creates ``Genie``:ref:`Ops <ops_guide>` objects to learn which configurations
have been applied to a device. The ops objects are snapshots of the
operational state of devices in the topology. `PTS` executes multiple commands
(via cli/yang/xml) to collection a feature's state and operational information.

This concept may sound similar to a `Verification`, however, `PTS` is only
executed in the common setup and the common cleanup; it does not run between
`Triggers`. As `PTS` runs only twice, it allows ``Genie`` `harness` to take a
complete snapshot of all the features configured on the device, without
impacting the execution time. 

Another advantage of `PTS` is the `pts_golden_config` feature. This feature
allows ``Genie`` to verify that the operational state of the configuration
applied to the device, precisely matches a previously created verified
snapshot. This ensures the same operational state for every run with the same
configuration.  Users can find more information about `pts_golden_config`
feature in the :ref:`user guide <PTS>`.

Using Ops
---------

``Genie`` :ref:`Ops <ops_guide>` objects are a snapshot of a particular
`Feature` on a `Device` at a specific time. Hence `Ops`  objects are  suited perfectly
to be used as a comparable `PTS` `profile`.

Now, let's see how to create a `PTS` `profile`.

Step 0: Check if the ``Genie`` `Ops` class exists for the feature you want to
run `PTS` on. If so, go to Step 2.

Step 1: Write a new `Ops` object or update an existing `Ops` object for the
feature you would like to `profile`. Once this is done, commit the `Ops` object to 
``Genie`` `Ops`.

Step 2: Add your PTS information to the `pts_datafile` as shown below:

.. code-block:: yaml

    <feature_name>:
        source:
            pkg: genie_libs.genie
            class: <your location, for example: ops.ospf.ospf.Ospf>
        exclude: [<list of generic keys to ignore in the comparison>]
        devices:
            uut:
                None

.. note::

    More keys from the datafile schema can be added

Step 3: Ensure the `job` file is pointing to this file via the `pts_datafile`
argument.

Step 4: To run `PTS`, execute your job via easypy with the required arguments.

.. note::

    The only mandatory argument is the :ref:`testbed file <book_setup_testbed>`.