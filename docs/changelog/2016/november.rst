November 2016
=============

November 29
-----------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 1.2.0                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install abstract
    pip install --upgrade genie

Also make sure you upgrade `xbu-shared` libraries to the latest version.

.. code-block:: bash

    cd $VIRTUAL_ENV/xbu_shared
    git pull origin master

Features:
^^^^^^^^^
*Ops, Ops, Ops*

 * `Ops` is now officially released!
 * `Ops` allows to retrieve the Operational state of the device.
 * `Ops` is tied with metaparser_ to retrieve the information from the device.
 * New `Maker` tool to simplify the process of mapping parsers output to a
   defined structure.
 * Each `Ops` object can be compared.
 * Supports connection pool to improve performance
 * And many more features. Read more about it in the Ops_ documentation.

 * Example of `Ops` library using Ydk_ is available under
   `xbu_shared/genie/ops/ospf/iosxe/yang/ospf.py`.
 * Full script example displaying `Conf` and `Ops` is available under the
   example directory.

 * Adition of the CliConfig_ concept for `Conf`.

xBU-Shared now houses 23 `Conf` libraries. Our sincere thanks to you and your
contributions.

.. _metaparser: http://wwwin-pyats.cisco.com/cisco-shared/metaparser/html/
.. _Ops: http://wwwin-pyats.cisco.com/cisco-shared/genie/html/Ops/index.html
.. _Ydk: https://github.com/CiscoDevNet/ydk-gen
.. _CliConfig: http://wwwin-pyats.cisco.com/cisco-shared/genie/html/Conf/developer/clibuilder.html#cliconfig
