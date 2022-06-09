.. _abstraction_concepts:

Concept
=======

.. sidebar:: Helpful Reading

    - :pythonmodules:`Python Modules <http>`

    - :pythonpackages:`Python Packages <http>`

    - :pythonimportsystem:`Python Import System <http>`


The ``abstract`` package is built upon the principle of dynamically looking up
and calling the right set of classes/functions/methods based on *requirements*.
These requirements are defined in each **abstraction enabled package** in the
form of **tokens**, which are typically device information such as the OS and
platform.

.. _abstraction_pkg:

Abstraction-Enabled Package
---------------------------

An abstraction-enabled package is simply any regular Python package declared to
be abstraction-compatible using the ``abstract.declare_package()`` API. Beyond
that, an abstraction-enabled package behaves no differently than any other
standard Python modules.

.. code-block:: python

    # Example
    # -------
    #
    #   abstraction-enabled package example

    # assuming the following directory structure
    #   my_package/
    #   |
    #   |-- __init__.py
    #   |
    #   `-- <other files/dirs>

    # declare abstraction-package at the top of my_package/__init__.py
    from genie import abstract
    abstract.declare_package()

    # Note
    # ----
    #
    #   - the above is equivalent to:
    #       from abstract import declare_package
    #       declare_package()

The call to ``abstract.declare_package()`` internally flags the given module to
be an abstraction package. This is a mandatory step when creating a module to
be abstraction-compatible, and does not change the behavior of how this package
normally behaves.

``abstract.declare_package()`` can also take an optional list of tokens to
define the order in which these tokens are explored to find a particular
implementation. The default order when not specified is ``origin``, ``os``,
``platform``, ``model``, ``pid``, ``version``, ``revision``.


.. code-block:: python

    # Example
    # -------
    #
    #   an abstraction-enabled package is just like any other package

    # you can import it
    import my_package

    # you can import submodules/classes/functions from it
    from my_package import sub_module
    from my_package import your_class
    from my_package.sub_module import my_submodule_class


.. _abstraction_tokens:

Abstract Tokens
---------------

An abstract token is the device attribute for which a specific value would
require a unique set of tools/implementations. For example, the token `os`
could have two different values of `nxos` and `iosxr`, which have vastly
different libraries required to work with those two devices.

The tokens and values are defined in a tokenized folder within an
abstraction-enabled package with the ``abstract.declare_token(name=value)`` API.
All modules within this folder and subfolders become abstract modules associated
with that token value. Similar to above, these are still just Python modules and
can be imported as usual.

.. code-block:: python

    # Example
    # -------
    #
    #   abstraction-enabled package with tokens

    # assuming the following directory structure
    #   my_package/
    #   |
    #   |-- __init__.py
    #   |
    #   |-- token_one/
    #   |   `-- __init__.py
    #   |
    #   `-- token_two/
    #       |-- __init__.py
    #       |
    #       `-- token_two_one/
    #           `-- __init__.py

    # abstraction-token is declared at the top of
    #   - my_package/token_one/__init__.py
    #   - my_package/token_two/__init__.py
    #   - my_package/token_two_one/__init__.py
    from genie import abstract
    abstract.declare_token(os='iosxe')

    # Note
    # ----
    #
    #   - the above is equivalent to:
    #       from abstract import declare_token
    #       declare_token(os='iosxe')

    # keep in mind that this does not alter the nature of python modules
    # it can still be imported
    from my_package.token_one import my_class
    from my_package.token_two import token_two_one
    from my_package.token_two_one.token_two_one import my_other_class

Each abstract token value represents an alternate set of libraries, capable of
handling the differences introduced/labelled by the token value defined. For
example, if a package contains token value ``os=nxos``, it suggests that the
libraries following this token module is specific to Cisco NXOS.

In addition, token values may be chained/nested. This allows for library
tiering. For example, if token ``platform=n5k`` is declared under token value
``os=nxos``, it suggests that these libraries would be specific to the Cisco
Nexus 5000 Series.

Tokenized folders must only be nested according to the order of tokens given in
the abstract package definition (or the default, if no order is given). However,
not all tokens in the order need to have a value defined as long as the relative
order is maintained.

.. code-block:: text

    os = iosxe
        version > v2.0
            revision = 3

    This is a valid hierarchy of tokenized folders, despite missing values for
    origin, platform, model, and pid.

    version > v2.0
        os = iosxe

    This is invalid and will raise an exception since version is defined after
    os in the token order


.. note::

    Folder names may not exactly match the token value (for ``VersionRange``s
    this would be impossible). Take care when creating a new abstract folder to
    give it a name that best reflects the token value being declared. For more
    details, refer to :ref:`abstraction_conventions`.

.. tip::

    Follow PEP8 - :modulenamingconvention:`module naming convention <http>`.


Version Tokens
--------------

In addition to a static string value for abstract tokens, a version range can be
specified.

.. code-block:: python

    from genie import abstract
    abstract.declare_token(version=abstract.VersionRange(min='v7.3', max='v8.2.1')
    # Or
    abstract.declare_token(version=abstract.VersionRange(min='v2')

Both ``min`` and ``max`` are optional arguments, with unbounded defaults. This
means that tokens can be defined with overlapping ranges (ie. multiple ranges
with unbounded maximums). In this case, the tokens are sorted during a lookup
such that the ranges with the greatest values are searched first, giving
preference to "later" versions.


Abstraction Mechanism
---------------------

The ``abstract`` module works most of its magic at the Python ``import`` and
``getattr()`` level. It does so by dissecting each lookup into three distinct
parts:

    - **relative path**: the primary lookup path that makes the most sense from
      a functional perspective. This is what the user references directly, eg:
      ``my_library.routing.ospf``

    - **tokens**: the list of abstraction token values currently known by the
      abstraction engine. This portion is registered through the ``Lookup``
      object. Eg: ``os=iosxe``, ``platform=cat9k``, ``model=c9600``.

    - **target**: the module/class/function/variable user is looking for.

During runtime, the lookup engine dynamically pieces together the above
information into a list of possible candidate **absolute paths** (direct mapping
to python import statements). As the list of tokens is arbitrary, this candidate
list is built following the :ref:`abstract_search_algorithm`.

.. code-block:: python

    # Example
    # -------
    #
    #   relative path & absolute path explained

    # Given the following tokens:
    tokens = {
        'os': 'iosxe',
        'platform': 'cat9k',
        'model': 'c9600'
    }

    # feed to to abstraction lookup engine.
    import my_package
    library = abstract.Lookup(tokens, package=my_package)

    # the relative call to
    library.config.routing.ospf.Ospf()

    # could match, for example:
    #
    #    my_package.iosxe.config.cat9k.routing.ospf.c9600.Ospf
    #         |       |      |     |      |     |     |    |
    #    abstraction  |   relative |   relative |     |  class
    #      package    |     path   |     path   |  tokenized
    #                 |         tokenized       |   folder
    #              tokenized     folder      relative
    #               folder                     path
    #
    # which translates to:
    #   from my_package.iosxe.config.cat9k.routing.ospf.c9600 import Ospf
    #
    # where
    # -----
    #    relative path = config, routing, ospf
    #    tokens        = os=iosxe, platform=cat9k, model=c9600
    #    target        = Ospf()


.. _abstract_search_algorithm:

Search Algorithm
----------------

The first time a lookup is performed on an abstract package, every token
definition and module is discovered and stored in a tree structure, with each
**relative path** to a module branching into multiple possible implementations
based on the token values.

The lookup will then traverse the tree with the given token values
in the order defined by the package, and return the stored implementation with
the best fit for token values. There may not be an implementation that matches
all the given token values, so the lookup will "fall back" along the search path
until an implementation is found, which best matches the given token values.

There are cases where multiple matches are possible. Token values can be given
as lists, which will attempt to match each value in the list sequentially. The
lookup works as a depth-first traversal. This means that the second value of a
list will only be considered if there is no valid implementation in the
tokenized folder matching the first value and all of the child tokenized folders
as well.

The other way multiple matches can be found is with overlapping version ranges.
If multiple tokenized folders have overlapping version ranges as their defined
token value, lookup will consider them in the order of "latest" to "earliest".

.. code-block:: text

    Given the token values
        token_one = one_one
        token_two = [two_one, two_three]
        token_three = v4

    And the abstract package structure
        one_one                 (token_one = one_one)
            two_one             (token_two = two_one)
                v5              (token_three > v5)
            two_two             (token_two = two_two)
                v1              (token_three > v1)
            two_three           (token_two = two_three)
                v1              (token_three > v1)
                v2              (token_three > v2)
        one_two                 (token_one = one_two)
            two_one             (token_two = two_one)
                v1              (token_three > v1)


    The order of consideration for implementations within tokenized folders
    would be
    one_one.two_one
    one_one.two_three.v2
    one_one.two_three.v1
    one_one.two_three
    one_one


JSON Integration
----------------

Most usage of the abstract lookup will not be done explicitly with a ``Lookup``
object. Instead, certain packages have an associated pre-generated JSON file
which links each abstracted feature (classes or functions) in the package with
matching token values. The contents of the JSON file are loaded into a tree
structure the same way discovered modules are. The only difference is that the
lookup will start with the name of a class or function or an associated command
instead of the **relative path** to a module.


.. _token_retrieval:

Getting Tokens
--------------

Tokens can be given as a dict, but are most useful when related to a particular
device. ``Lookup.from_device(device, package=abstract_package)`` will use the
tokens defined in ``abstract_package`` to retrieve attributes from devices for
performing lookups.

.. note::

    :ref:`Integration with Topology  <abstract_topology>`


