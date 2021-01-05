March 2017
==========

March 31
--------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 1.2.4                         |
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

* Fix issue with the integration with unicon

March 21
--------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 1.2.3                         |
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

* Fix issue with Config and __lt__ where it was causing issue for unconfiguring 
  certain objects
* Enhancement to Maker for Ops to treat callable for attributes.

