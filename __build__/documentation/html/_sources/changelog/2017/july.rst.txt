July 2017
=========

July 6th
--------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie``                     | 2.0.4                         |
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

* Genie now supports REST.
* Maker can now send kwargs to parser
* genie.infra has been renamed to genie.harness (Will affect existing Job file
  of Genie harness)
* Schema validation for datafiles
* Better error progration throughout Genie harness
* Genie Triggers and verification can be executed in pyATS Scripts, take a look
  inside the example_ page for our new examples.


For more information, make sure to go through the genie_ documentation.

And make sure to visit our new ``Genie`` portal_.

.. _example: http://wwwin-genie.cisco.com/cisco-shared/genie/latest/installation/example.html
.. _portal: http://wwwin-genie.cisco.com/
.. _genie: http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/
