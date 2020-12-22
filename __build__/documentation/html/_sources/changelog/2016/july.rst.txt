July 2016
=========

July 25
-------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 1.1.0                         |
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

 * New enhancement to :ref:`attribute_helper`. Replaces much of the boilerplate
   coding requirement for each `Feature`.
 * New addition to ``Genie``, :ref:`cli`. It deals with generating `Device`
   configuration, and automatically generates the unconfiguration.
 * :ref:`managedattribute` is another new addition which let's you finely
   control all aspect of class member variable. To list some of its
   features:

   1. Type checking
   2. Read-only mode
   3. Automatically document the attributes.
   4. Performs transformation on set/get/del.

 * New file structure to support abstract_ for `xbu_shared`.
 * `_finalize`, `_build_helper` and `_merge_level` are replaced by
   :ref:`attributehelper`.

.. _abstract: http://wwwin-pyats.cisco.com/cisco-shared/abstract/html/
.. _apidoc: http://wwwin-pyats.cisco.com/cisco-shared/genie/html/apidoc/decorator.html#genie.decorator.managedattribute
