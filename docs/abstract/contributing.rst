.. _abstraction_contributing:

Adding and Modifying
====================

The primary benefit of using ``abstract`` module is its ease of use combined
with long-term scalability. With it, abstraction is no longer a day-one,
front-load investment, but rather a "create more specific implementations as
required" dynamic system. While a feature may exist under the token ``os="iosxe"``,
another implementation can be created at a later date to accommodate differences
in behaviour for specific platforms (eg. ``platform="cat9k"``) which exist under
the previous token.

.. warning::

    Tokens may *not* carry arbitrary names or values, and must adhere to a
    :ref:`specific hierarchy <token_order>`. They should match the values
    defined in the Unicon `PID tokens`_ file which is the source of truth for device
    definitions. If the token values for your particular device are not present
    please consider contributing a new definition to the file.

.. _PID tokens: https://github.com/CiscoTestAutomation/unicon.plugins/blob/master/src/unicon/plugins/pid_tokens.csv

.. tip::

    Before adding any new features makes sure to check the `Genie Feature Browser`_
    to ensure that it doesn't already exist, or if it already exists for another
    type of device.


.. _Genie Feature Browser: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/


Library Structure
-----------------

Always group methods and classes together using some form of system (such as
by functionality) into modules & submodules. This will add depth and structure
to your libraries, simplifying user's understanding & maintenance.

As abstracted packages and tokens are simply python packages and modules, the
standard python :pythonpackages:`Python Packages <http>` guidelines apply,
and your directory structure should naturally fall into place.


.. code-block:: text

    Library Structure
    -----------------

    library_root/
    ├── __init__.py                     # declare_package()
    ├── module.py                       # any default (no token) modules
    │
    ├── submodule/                      # and regular Python submodules.
    │   ├── __init__.py
    │   └── module.py
    │
    ├── <os>/                           # a token definition
    │   ├── __init__.py                 # declare_token(os='<some_os>')
    │   │
    │   ├── module.py                   # OS specific modules
    │   ├── submodule/                  # and submodules
    │   │   ├── __init__.py
    │   │   └── module.py
    │   │
    │   └── <platform>/                 # a token under another token
    │       ├── __init__.py             # declare_token(platform='<some_platform>')
    │       ├── module.py
    │       └── submodule/              # platform specific submodules for above OS
    │           ├── __init__.py
    │           └── module.py
    ...

.. code-block:: text

    Example Library
    ---------------

    The following is implemented:
        - generic reload, verify, configure ospf & interface
        - iosxr default reload, configure interface
        - iosxr/crs specific reload, configure interface

    example_abstracted_apis/
    ├── __init__.py                    # declare_package()
    |
    ├── reload.py
    ├── verify.py
    |
    ├── configure/
    │   ├── __init__.py
    │   ├── ospf.py
    │   └── interface.py
    |
    ├── iosxr/
    |   ├── __init__.py                # declare_token(os='iosxr')
    |   |
    |   ├── reload.py
    |   ├── configure/
    |   │   ├── __init__.py
    |   │   └── interface.py
    |   |
    |   └── asr9k/
    |       ├── __init__.py            # declare_token(platform='asr9k')
    |       ├── reload.py
    |       └── configure/
    |           ├── __init__.py
    |           └── interface.py
    ...

