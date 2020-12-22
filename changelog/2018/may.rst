May 2018
========

May 31st
--------

+-------------------------------+-------------------------------+
| Module                        | Versions                      |
+===============================+===============================+
| ``Genie.ops``                 | 3.0.1                         |
+-------------------------------+-------------------------------+
| ``Genie.conf``                | 3.0.1                         |
+-------------------------------+-------------------------------+
| ``Genie.utils``               | 3.0.1                         |
+-------------------------------+-------------------------------+
| ``Genie.harness``             | 3.0.3                         |
+-------------------------------+-------------------------------+
| ``Genie.examples``            | 3.0.1                         |
+-------------------------------+-------------------------------+

Upgrade Instruction
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade genie.conf
    pip install --upgrade genie.ops
    pip install --upgrade genie.utils
    pip install --upgrade genie.harness
    pip install --upgrade genie.examples

Features:
^^^^^^^^^

* Fix for running the same processor with different arguments
* Timeout fix
    * No more negative number
    * Always run for up to maxtime
* `common_setup` and `common_cleanup` can now have processors added dynamically with the subsection datafile
* `Trigger` section can now have processors added dynamically with the trigger datafile
* Fix bug with adding the same processor with the different arguments
* Enhancement for `Maker`, can now provide `attributes` longer than the smallest dest of the ops.
* Removal of interfaces.find_links, as interfaces only have 1 link. (Following pyATS model)

* Datafiles are now smart. Trigger, verification, subsection and PTS datafile will find their corresponding files if not provided. 
* Robot keyword changed: 
    * Compare profile "later" with "current" on devices "R1;R2"
* Triggers and verification will only execute the one requested with uids or groups, old behavior was to run all triggers in datafile, unless uids/groups provided.
