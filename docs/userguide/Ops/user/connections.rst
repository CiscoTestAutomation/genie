.. _Oconnection:

Connections
===========

This section will teach users how to connect to their `device` whichever way they want.

Single Connection
-----------------

In this scenario, users want to connect to their `device` using the
`console` or the `vty`.

Let's begin with the simplest case:

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect()

The `device` is connected and ready to be used by the ``Genie`` infrastructure. As
no `via` was provided, it will try to connect to the default connection, which
generally uses the `console` connection.

Another possibility is using `via` argument.

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect(via='vty1')

Now, it will use the vty1 to connect to the `device`.

Another option is to use the `alias` argument. When no `alias` is provided,
it uses the `default` alias. However, users can provide a specific `alias`.

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect(via='vty1', alias='vty')

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect(via='netconf', alias='nc')
    >>> device.connect(via='vty1', alias='vty')
    >>> device.mapping['yang'] = 'nc'
    >>> device.mapping['cli'] = 'vty1'

We have added a `mapping` attribute to the `device`. This attribute allows
``Genie`` to determine which user-defined `alias`. Now, every `cli` command
used for this `device`, will use the `vty` connection. The same concept may be
applied for `Yang`, except the mapping should use the keyword `yang` instead.

If the more than one connection was made to the device with different alias,
then you will need to use mapping. However if only 1 connection is made to the
device, then it will automatically use this connection.

.. hint::

    Confused about the `alias` concept ? Make sure you are familiar with the
    concept of pyATS :connection:`connection <http>`.

.. _user_ops_connection_pool:

Pool Connection
---------------

A pool connection can be used to connect to the `device`, which allows to
send multiple commands at the same time to the `device`. This improve the
performance of learning the feature.

.. code-block:: python

   >>> device.start_pool(alias='vty',
                         via='vty1',
                         size='<any number which is supported by your device>')

Once this the pool is started, then passing this `device` to an `Ops` object
will send all the commands in parallel. This works for all connection type
which support multiple connections to the device.

If more than one connection was made to the device with different alias, then
you will need to use mapping. Mapping allow to let ``Genie`` know which
connection for sending the cli commands. However if only 1 connection is made
to the device, then it will automatically use this connection.

.. code-block:: python

    def.mapping['cli'] = 'vty'
