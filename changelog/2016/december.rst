December 2016
=============

December 9 
----------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 1.2.2                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

Also make sure you upgrade `xbu-shared` libraries to the latest version.

.. code-block:: bash

    cd $VIRTUAL_ENV/xbu_shared
    git pull origin master

Features:
^^^^^^^^^

 * Modification to IPv4InterfaceCache_ and IPv6InterfaceCache_. It now returns
   a range_ instead of an iterator. Examples in the above link on how to use it
   and in the Genie example script.
 * Enhancement to diff_ to make it easier
   to use.
 * Enhancement to `conf` on managing which object contains a `Feature`
   depending where it is added.
 * Bug fix

.. _IPv4InterfaceCache: http://wwwin-pyats.cisco.com/cisco-shared/genie/html/apidoc/genie.conf.base.utils.html#genie.conf.base.utils.IPv4InterfaceRange
.. _IPv6InterfaceCache: http://wwwin-pyats.cisco.com/cisco-shared/genie/html/apidoc/genie.conf.base.utils.html#genie.conf.base.utils.IPv6InterfaceCache
.. _range: https://docs.python.org/3.4/library/functions.html#func-range
.. _diff: http://wwwin-pyats.cisco.com/cisco-shared/genie/html/Ops/user/ops.html#extra-features
