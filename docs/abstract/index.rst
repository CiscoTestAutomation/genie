.. _abstract:
Library Abstraction
===================

The Genie Abstraction package (or simply ``genie.abstract``) enables users
to build os/platform/release/feature/etc and reference them dynamically in their
scripts without hard-coded imports.

For more details, refer to :pyats:`pyATS <http>`.


.. tip::

    It is **strongly** recommended that all scripts to be written using this
    abstraction package. This will vastly reduce future maintenance work if the
    script is to be re-used. Wanna know why? Read on...

.. important::

    The abstraction package is undergoing a revision to more consistently
    organize features around device definitions. See the command `pyats migrate abstract`_
    to check your environment and ensure it will continue to be compatible. The
    source of truth for device definitions will be the `PID tokens`_ file in
    Unicon, so please ensure that your devices are present and represented
    accurately.

.. _pyats migrate abstract: https://pubhub.devnetcloud.com/media/pyats/docs/cli/pyats_migrate.html
.. _PID tokens: https://github.com/CiscoTestAutomation/unicon.plugins/blob/master/src/unicon/plugins/pid_tokens.csv

.. toctree::
   :maxdepth: 2

   introduction
   concept
   lookup_class
   lookup_decorator
   conventions
   apidoc

