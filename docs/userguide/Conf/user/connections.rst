Connections
===========

In this section, users will learn how to connect to the `device`.

Single Connection
-----------------

Connection to a device is the same as pyATS. You can find some example below.

Let's begin with a simple example:

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect()

Once connected, Genie infrastructure is ready to use the `device`.

As no `via` was provided in this example, the device will use the `console` connection
to connect through `a` and `b` (optional).

Users may also connect to `device` by using a `via` argument:

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect(via='vty1')

Now, it use the vty1 to connect to the `device`.

Finally, users may use the `alias` argument to connect to the `device`.
When no `alias` is provided the `default` alias is used. However, a specific
alias may be given, if the user so chooses.

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect(via='vty1', alias='vty')
    >>> device.mapping['cli'] = 'vty'

We have strategically added a `mapping` attribute to the `device`. Using the `mapping`
attribute, ``Genie`` knows what the user has defined as the alias. Now, for every `cli` command
for this `device`, it will use the `vty` connection.

The same concept is applied for `Yang`, except in these circumstances, the
mapping should use the keyword `yang` instead of `vty`, `rest` for REST and
`xml` for xml connection.

.. code-block:: python

    >>> device
    <Device object 'P1' at 0xf71a5f8c>
    >>> device.connect(via='netconf', alias='nc')
    >>> device.mapping['yang'] = 'nc'

.. note::

    To learn more about pyATS Connection and how to use different connection mechanisms
    (Yang, Rest,...) please visit the pyATS :connection:`connection <http>` documentation.

Connection Pool
---------------

Users can send multiple commands simultaneously  to a `device`
using a connection pool. However, for `conf`, applying multiple commands at the same to a
`device` is disastrous. For this reason, even if a user creates a
connection pool, only a single command will be sent to the `device` at one time.


.. code-block:: python

   >>> device.start_pool(alias='vty',
                         via='vty1',
                         size=pool_num)
   # Same as above, we need to tell the infrastructure which
   # alias to use for cli commands.
   >>> dev.mapping['cli'] = 'vty'

Once again, ``Genie`` will use the `mapping` attribute to know what connection to use.

The same concept may be applied for `Yang`


