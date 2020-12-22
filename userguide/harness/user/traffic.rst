.. _traffic:

Traffic
=======

.. sidebar:: Quick References

    - :genietrafficgen:`genie.trafficgen <http>`
    - :ref:`statictgn <statictgn>`

Packets! As with any thorough testing, it's sometimes imperative to execute
tests with actual traffic flowing through devices. ``Genie`` can connect to
traffic generator (TGN) devices within a `testbed` topology.

The `genietrafficgen` package contains connection implementation classes for
traffic generator devices such as Ixia, Spirent etc.

This package can be used for connecting to traffic generator devices using
``Genie`` and execute common functions such as loading configuration,
starting/stopping traffic etc.

``Genie`` currently utilizes the following connection implementation libraries for
connecting to IXIA traffic generator devices:

    1. :genietrafficgen:`genie.trafficgen <http>`: Uses Ixia's Python-based :ixnetwork_pypi:`ixnetwork <http>` PyPI package
    2. :ref:`statictgn <statictgn>`: Leverages Cisco internal TCL-based TGN libraries (not available externally)

.. tip::
    We recommend using the genie.trafficgen package over the statictgn libraries.

.. note::
    Connection implementation library 'statictgn' will be deprecated soon.
