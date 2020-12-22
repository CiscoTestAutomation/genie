.. _abstraction_conventions:

Conventions
===========

The primary benefit of using ``abstract`` module is its ease of use combined
with long-term scalability. With it, abstraction is no longer a day-one, 
front-load investment, but rather an "add a token as you need" dynamic system.

In order to fully reap the benefits offered by abstraction and allowing for 
sharing between teams and projects, considering following the conventions
below during your coding.


Rules of Thumb
--------------

- when creating a new library, adding the :ref:`abstraction_pkg` declaration
  at the root ``__init__.py`` file is always a good habit to get into. There's
  no side effect and/or runtime costs.

- add your methods, modules as you see fit, but focus on on tackling one
  combination (tokenset) at a time (eg, start with writing libraries for your 
  uut:  iosxr/sunstone/latest)

- always create ``Lookup`` objects for each device as one of the first things in
  your script's CommonSetup section. This will ensure the rest of your script
  have proper access to abstracted packages & libraries.

- when needing to call/reference any library functions & classes, always do so
  through the ``Lookup`` object created above.

- when a new set of combination (tokensets) needs to be added, consider their
  relationships and group like-levels together.

  .. code-block:: text

      if you started with the following for iosxr/sunstone/latest
            /my_lib/__init__.py
            /my_lib/file.py

      and now needs to add iosxr/enxr, consider refactoring to:
            /my_lib/iosxr/sunstone/__init__.py
            /my_lib/iosxr/sunstone/file.py
            /my_lib/iosxr/enxr/__init__.py
            /my_lib/iosxr/enxr/file.py

      remember - a module is just a folder. You're merely shuffling files.

- create new tokens with meaningful names that reflects the set of differences
  it covers. Eg, os names, relese variants, branches, etc.

- use python inheritance between your various implementations for... a variety
  of OOP-related benefits.

- if your library requires a set of *defaults*, eg, fallback functions/classes
  when no tokens match, define them directly under the root package module. The
  engine will auto-fallback to it.

- consider sharing your code with the rest of the community.

- Follow PEP8 - :modulenamingconvention:`module naming convention <http>`.


Library Structure
-----------------

Always group methods and classes together using some form of system (such as
by funtionality) into modules & submodules. This will add depth and struture
to your libraries, simplifying user's understanding & maintenance.

As abstracted packages and tokens are simply python packages and modules, the
standard python :pythonpackages:`Python Packages <http>` guidelines apply,
and your directory structure should naturally fall into place.


.. code-block:: text

    Library Structure
    -----------------

    library_root/
    |-- __init__.py                     # declare_package()
    |
    |-- module.py                       # any default (no token) modules
    |-- submodule/                      # and submodules.
    |   |-- __init__.py
    |   `-- submodule_module.py
    |
    |-- token_module/                   # a new token
    |   |-- __init__.py                 # declare_token()
    |   |
    |   |-- module.py                   # token specific modules
    |   |-- submodule/                  # and submodules
    |   |   |-- __init__.py
    |   |   `-- submodule_module.py
    |   |
    |   `-- token_subtoken_module/      # a token under another token
    |       |-- __init__.py             # declare_token
    |       |-- module.py
    |       `-- submodule/              # ditto
    |           |-- __init__.py
    |           `-- submodule_module.py
    |
    ...

.. code-block:: text

    Example Library
    ---------------

    The following is implemented:
        - generic reload, verify, configure ospf & interface
        - iosxr default reload, configure interface
        - iosxr/crs specific reload, configure interface

    example_abstracted_module/
    |-- __init__.py
    |
    |-- reload.py
    |-- verify.py
    |
    |-- configure/
    |   |-- __init__.py
    |   |-- ospf.py
    |   `-- interface.py
    |
    |-- iosxr/
    |   |-- __init__.py
    |   |
    |   |-- reload.py
    |   |-- configure/
    |   |   |-- __init__.py
    |   |   `-- interface.py
    |   |
    |   `-- crs/
    |       |-- __init__.py
    |       |-- reload.py
    |       `-- configure/
    |           |-- __init__.py
    |           `-- interface.py
    |
    ...

