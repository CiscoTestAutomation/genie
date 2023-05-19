.. _abstraction_concepts:

Concept
=======

.. sidebar:: Helpful Reading

    - :pythonmodules:`Python Modules <http>`

    - :pythonpackages:`Python Packages <http>`

    - :pythonimportsystem:`Python Import System <http>`


``abstract`` package is built upon the principle of dynamically looking up and
calling the right set of classes/functions/methods based on *requirements*.
These requirements are defined in the form of **tokens**, which describe the
types of device that a specific implementation supports.

.. _abstraction_pkg:

Abstraction-Enabled Package
---------------------------

An abstraction-enabled package is simply any regular Python package declared to
be abstraction-compatible using the ``abstract.declare_package()`` API.

.. code-block:: python

    # Example
    # -------
    #   abstraction-enabled package example

    # assuming the following directory structure
    #   mypackage/
    #   ├── __init__.py
    #   └── <other files/dir>

    # declare abstraction-package at the top of my_package/__init__.py
    from genie import abstract
    abstract.declare_package()

Beyond that, an abstraction-enabled package behaves no differently than any other
standard Python module.

.. code-block:: python

    # Example
    # -------
    #   an abstraction-enabled package is just like any other package

    # you can import it
    import my_package

    # you can import submodules/classes/functions from it
    from my_package import sub_module
    from my_package import your_class
    from my_package.sub_module import my_submodule_class


.. _abstraction_tokens:

Abstraction Tokens
------------------

An abstraction token is a device description attached to a child-module within
an abstraction-enabled package. It is declared by calling
``abstract.declare_token(<attribute>=<value>)`` API, which is how we define what
kind of device this child-module is meant to support. Similar to the above,
these are still regular Python modules and can be imported and used
as such.

.. code-block:: text

    # Example
    # -------
    #   abstraction-enabled package with tokens

    # assuming the following directory structure
    #   mypackage/
    #   ├── __init__.py
    #   ├── nxos/
    #   │   └── __init__.py
    #   └── iosxe/
    #       ├── __init__.py
    #       └── cat9k/
    #           └── __init__.py


Abstraction tokens are declared at the top of the ``__init__.py`` file


.. code-block:: python

    #   - my_package/nxos/__init__.py
    from genie import abstract
    abstract.declare_token(os='nxos')


.. code-block:: python

    #   - my_package/iosxe/__init__.py
    from genie import abstract
    abstract.declare_token(os='iosxe')

.. code-block:: python

    #   - my_package/iosxe/cat9k/__init__.py
    from genie import abstract
    abstract.declare_token(platform='cat9k')

Keep in mind that this does not alter the nature of python modules, they
can still be imported as usual

.. code-block:: python

    from my_package.nxos import my_class
    from my_package.iosxe import my_class
    from my_package.iosxe.cat9k import my_class

Each abstraction token represents an alternate set of libraries, capable of
handling the differences introduced/labelled by the **token** value. For example,
if a package contains token ``os='nxos'``, it suggests that the libraries following
this token module is specific to Cisco NXOS.

.. _token_order:

In addition, tokens may be nested. For example, if the token ``platform='n7k'``
is declared under token ``os='nxos'``, it suggests that these libraries would be
specific to Cisco Nexus 7000 Series Switches. There is a specific order of device
attributes for tokens, which **must** be followed while nesting:

.. code-block:: markdown

    - os
    - platform
    - model
    - pid
    - version
    - revision

.. warning::

    Tokens may *not* carry arbitrary names or values. They should match the values
    defined in the Unicon `PID tokens`_ file which is the source of truth for device
    definitions. If the token values for your particular device are not present
    please consider contributing a new definition to the file.

.. _PID tokens: https://github.com/CiscoTestAutomation/unicon.plugins/blob/master/src/unicon/plugins/pid_tokens.csv


Abstraction Mechanism
---------------------

Retrieving features with abstraction will attempt to find the most number of
token matches to return an implementation for that feature. An implementation
matching both OS and platform would be returned instead of just the
implementation matching OS, as the first would be more specific for the given
device.


Examples
########

Parser code exists in a directory structure like so:

.. code-block:: text

    parser/
    ├── __init__.py
    └── iosxe/
        ├── __init__.py
        ├── show_feature.py
        └── cat9k/
            ├── __init__.py
            ├── show_feature.py
            └── c9300/
                ├── __init__.py
                └── show_feature.py

Each level of ``show_feature.py`` has an implementation for the `show feature`
parser, but only ``parser/iosxe/show_feature.py`` and
``parser/iosxe/cat9k/show_feature.py`` have implementations for the `show other feature`
parser. Note that the `c9700` folder does **not** exist.

.. list-table:: Show Feature Parser
    :header-rows: 1
    :align: center

    * - Parser Path
      - show feature
      - show other feature
    * - iosxe
      - ✔️
      - ✔️
    * - iosxe/cat9k
      - ✔️
      - ✔️
    * - iosxe/cat9k/c9300
      - ✔️
      - ❌
    * - iosxe/cat9k/c9700
      - ❌
      - ❌

.. note::

    A reminder of purpose of the different levels of ``show_feature.py``

      - Generic implementations for any IOSXE device.
      - More specific implementations for the Catalyst 9000 Platform.
      - Even more specific implementations for only the Catalyst 9300 model.

We have two devices,

- ``Device_A`` which can be defined by the tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``.
- ``Device_B`` which can be defined by the tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9700'``.

Note the different models of the two devices.

Example 1
^^^^^^^^^

.. tabs::

    .. tab:: 1

        We want to parse `show feature` with ``Device_A``.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``

    .. tab:: 2

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!

    .. tab:: 3

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``. An implementation
        of the `show feature` parser exists here.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> `show feature` parser exists!

    .. tab:: 4

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``. An implementation
        of the `show feature` parser exists here. This implementation is returned.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> `show feature` parser exists!
        - Return found parser

Example 2
^^^^^^^^^

.. tabs::

    .. tab:: 1

        We want to parse `show feature` with ``Device_B``.

        - ``Device_B`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9700'``

    .. tab:: 2

        We want to parse `show feature` with ``Device_B``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9700/show_feature.py``.

        - ``Device_B`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9700'``
        - ``parser/iosxe/cat9k/c9700/show_feature.py`` -> File does not exist!

    .. tab:: 3

        We want to parse `show feature` with ``Device_B``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9700/show_feature.py``. This file does
        not exist so the abstraction mechanism falls back to the next best match,
        ``parser/iosxe/cat9k/show_feature.py``.

        - ``Device_B`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9700'``
        - ``parser/iosxe/cat9k/c9700/show_feature.py`` -> File does not exist! -> Fallback!
        - ``parser/iosxe/cat9k/show_feature.py`` -> File exists!

    .. tab:: 4

        We want to parse `show feature` with ``Device_B``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9700/show_feature.py``. This file does
        not exist so the abstraction mechanism falls back to the next best match,
        ``parser/iosxe/cat9k/show_feature.py``. An implementation of the
        `show feature` parser exists here.

        - ``Device_B`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9700'``
        - ``parser/iosxe/cat9k/c9700/show_feature.py`` -> File does not exist! -> Fallback!
        - ``parser/iosxe/cat9k/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/show_feature.py`` -> `show feature` parser exists!

    .. tab:: 5

        We want to parse `show feature` with ``Device_B``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9700/show_feature.py``. This file does
        not exist so the abstraction mechanism falls back to the next best match,
        ``parser/iosxe/cat9k/show_feature.py``. An implementation of the
        `show feature` parser exists here. This implementation is returned.

        - ``Device_B`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9700'``
        - ``parser/iosxe/cat9k/c9700/show_feature.py`` -> File does not exist! -> Fallback!
        - ``parser/iosxe/cat9k/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/show_feature.py`` -> `show feature` parser exists!
        - Return found parser

Example 3
^^^^^^^^^

.. tabs::

    .. tab:: 1

        We want to parse `show other feature` with ``Device_A``.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``

    .. tab:: 2

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!

    .. tab:: 3

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``. This file exists
        but does not have an implementation of the `show other feature` parser
        that we want.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> `show other feature` parser does not exist!

    .. tab:: 4

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``. This file exists
        but does not have an implementation of the `show other feature` parser
        that we want. The abstraction mechanism falls back to the next best match
        which is ``parser/iosxe/cat9k/show_feature.py``.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> `show other feature` parser does not exist! -> Fallback!
        - ``parser/iosxe/cat9k/show_feature.py`` -> File exists!

    .. tab:: 5

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``. This file exists
        but does not have an implementation of the `show other feature` parser
        that we want. The abstraction mechanism falls back to the next best match
        which is ``parser/iosxe/cat9k/show_feature.py``. An implementation of the
        `show other feature` parser exists here.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> `show other feature` parser does not exist! -> Fallback!
        - ``parser/iosxe/cat9k/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/show_feature.py`` -> `show other feature` parser exists!

    .. tab:: 6

        We want to parse `show feature` with ``Device_A``. The abstraction
        mechanism will find the file that matches the most number of tokens,
        which is ``parser/iosxe/cat9k/c9300/show_feature.py``. This file exists
        but does not have an implementation of the `show other feature` parser
        that we want. The abstraction mechanism falls back to the next best match
        which is ``parser/iosxe/cat9k/show_feature.py``. An implementation of the
        `show other feature` parser exists here. This implementation is returned.

        - ``Device_A`` tokens ``os='iosxe'``, ``platform='cat9k'``, ``model='c9300'``
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/c9300/show_feature.py`` -> `show other feature` parser does not exist! -> Fallback!
        - ``parser/iosxe/cat9k/show_feature.py`` -> File exists!
        - ``parser/iosxe/cat9k/show_feature.py`` -> `show other feature` parser exists!
        - Return found parser

