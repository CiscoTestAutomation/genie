May 2017
========

May 23th
--------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 2.0.3                         |
+-------------------------------+-------------------------------+


Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

Also make sure you upgrade `genie_libs` to the latest version.

.. code-block:: bash

    cd $VIRTUAL_ENV/projects/genie_libs
    git pull origin master

Features:
^^^^^^^^^

Genie 2.0.2 fixes an issue with previous release for certain files.
Genie 2.0.3 fixes an issue with Yang connections.

For more information, make sure to go through the
genie_ documentation.

And make sure to visit our new ``Genie`` portal_.

May 15th
--------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 2.0.1                         |
+-------------------------------+-------------------------------+


Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

Also make sure you upgrade `genie_libs` to the latest version.

.. code-block:: bash

    cd $VIRTUAL_ENV/projects/genie_libs
    git pull origin master

Features:
^^^^^^^^^

Genie 2.0.1 introduces small enhancements/bug fixes to ``Genie``.

* Enhancement to Tftp for `Genie` harness.
* Enhancement to `Maker` to support regex in src and not in dest.
* Bug fix for `Diff` utils libraries.

For more information, make sure to go through the
genie_ documentation.

And make sure to visit our new ``Genie`` portal_.

May 8th
-------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 2.0.0                         |
+-------------------------------+-------------------------------+


Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

Also make sure you upgrade `genie_libs` to the latest version.

.. code-block:: bash

    cd $VIRTUAL_ENV/projects/genie_libs
    git pull origin master

Features:
^^^^^^^^^

Genie 2.0.0 introduces a brand new ``Genie`` Test Harness and several
exciting new features!

* ``Genie`` test harness introduces the concept of topology & configuration
  agnostic event driven testing to pyATS.
* ``Genie`` SDK provides triggers and verifications libraries.
* Agnostic based on OS, platform device, and management interfaces (CLI/Yang/...)
* Improved and enhanced ``Genie`` `Conf` and `Ops`.
* ``Genie`` SDK/Harness - the much-anticipated Python implementation of `BEST/PSAT-NG`_.

For more information, make sure to go through the
genie_ documentation.

And make sure to visit our new ``Genie`` portal_.

May 4th
-------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 1.2.5                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie

Also make sure you upgrade `genie_libs` to the latest version.

.. code-block:: bash

    cd $VIRTUAL_ENV/projects/genie_libs
    git pull origin master

Features:
^^^^^^^^^

* Fix genie scripts to be compatible with bitbucket design.

.. _portal: http://wwwin-genie.cisco.com/
.. _BEST/PSAT-NG: http://wwwin-best.cisco.com/
.. _genie: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/
