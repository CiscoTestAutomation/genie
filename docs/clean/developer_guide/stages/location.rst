Where does the code reside?
===========================

The first step to developing a clean stage is to determine the scope of the stage. Meaning will the stage work for all OS's and Platform's or will it be specific to one? The answer to the question is used to determine what file the clean stage belongs in:

    * | Common Clean Stages reside in the `stages/stages.py` file.
      | For example, the Common Clean Stages belong `here <https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/clean-pkg/src/genie/libs/clean/stages/stages.py>`_.

    * | OS-specific Clean Stages reside in the `stages/<os>/stages.py` file.
      | For example, the IOSXE specific Clean Stages belong `here <https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/clean-pkg/src/genie/libs/clean/stages/iosxe/stages.py>`_.

    * | Platform-specific Clean Stages reside in the `stages/<os>/<platform>/stages.py` file.
      | For example, the IOSXE CAT9K Clean Stages belong `here <https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/clean-pkg/src/genie/libs/clean/stages/iosxe/cat9k/stages.py>`_.

.. note::

    If the directory structure and/or the `stages.py` file does not already exist, create it following the below example but use your `<os>` and `<platform>`. The `<os>` and `<platform>` must align with the same from `unicon.plugins <https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/supported_platforms.html#>`_.

    .. code-block:: bash

        stages
        ├── __init__.py
        └── <os>
            ├── __init__.py
            ├── stages.py
            └── <platform>
                ├── __init__.py
                └── stages.py

    Copy/paste the following into each `__init__.py` file you create.

    .. code-block:: python

        try:
            from genie import abstract
            abstract.declare_token(__name__)
        except Exception as e:
            import warnings
            warnings.warn('Could not declare abstraction token: ' + str(e))
