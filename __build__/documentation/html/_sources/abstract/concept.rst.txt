.. _abstraction_concepts:

Concept
=======

.. sidebar:: Helpful Reading

    - :pythonmodules:`Python Modules <http>`

    - :pythonpackages:`Python Packages <http>`

    - :pythonimportsystem:`Python Import System <http>`


``abstract`` package is built upon the principle of dynamically looking up and 
calling the right set of classes/functions/methods based on *requirements*. 
These requirements are defined in each **abstraction enabled package** in the 
form of **tokens**. 

.. _abstraction_pkg:

Abstraction-Enabled Package
---------------------------

An abstracton-enabled package is simply any regular Python package declared to
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
    abstract.declare_package(__name__)

    # Note
    # ----
    #
    #   - the above is equivalent to:
    #       from abstract import declare_package
    #       declare_package(__name__)
    #
    #   - __name__ is the name of this module

The call to ``abstract.declare_package(__name__)`` internally
flags the given module to be an abstraction package. This is a mandatory step
when creating a module to be abstraction-compatible, and does not change the 
behavior of how this package normally behaves.

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

Abstraction Tokens
------------------

An abstraction token is simply a child-module within an abstraction-enabled 
package. It is declared by calling ``abstract.declare_token()`` API. Similar to
the above, these are still... Python modules.

.. code-block:: python

    # Example
    # -------
    #
    #   abstraction-enabled package with tokens

    # assuming the following directory sturcture
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
    abstract.declare_token(__name__)

    # Note
    # ----
    #
    #   - the above is equivalent to:
    #       from abstract import declare_token
    #       declare_token(__name__)
    #
    #   - __name__ is the name of this module

    # keep in mind that this does not alter the nature of python modules
    # it can still be imported
    from my_package.token_one import my_class
    from my_package.token_two import token_two_one
    from my_package.token_two_one.token_two_one import my_other_class

Each abstraction token represents an alternate set of libraries, capable of 
handling the differences introduced/labelled by the **token** name. For example,
if a package contains token ``nxos``, it suggests that the libraries following
this token module is specific to Cisco NXOS. 

In addition, tokens may be chained/nested. This allows for library tiering. For
example, if token ``yang`` is declared under token ``nxos``, it suggests that
these libraries would be specific to Cisco NXOS's NETCONF/YANG implementation.

.. note::

    Tokens may carry arbitrary names. Use token naming wisely to depict 
    differences where you want to abstract your libraries. For more details, 
    refer to :ref:`abstraction_conventions`.

.. tip::
    
    Follow PEP8 - :modulenamingconvention:`module naming convention <http>`.


Abstraction Mechanism
---------------------

The ``abstract`` module works most of its magic at the Python ``import`` and
``getattr()`` level. It does so by dissecting each lookup into three distinct
parts: 

    - **relative path**: the primary lookup path that makes the most sense from
      a functional perspective. This is what the user references directly, eg: 
      ``my_library.routing.ospf``

    - **tokens**: the list of abstraction tokens currently known by the 
      abstraction engine. This portion is registered through the ``Lookup``
      object. Eg: ``iosxr``, ``fretta``, ``xml``.

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
    #    - iosxe
    #    - polaris_dev
    #    - yang
    os = 'iosxe'
    branch = 'polaris_dev'
    context = 'yang'

    # feed to to abstraction lookup engine.
    library = abstract.Lookup(os, branch, context)

    # the relative call to
    library.my_package.config.routing.ospf.Ospf()

    # could match, for example:
    #
    #    my_package.iosxe.config.polaris_dev.routing.ospf.yang.Ospf
    #         |       |      |       |          |     |     |    |
    #    abstraction  |   relative   |       relative |     |  class
    #      package    |     path     |         path   |   token
    #               token          token           relative
    #                                                path
    # which translates to:
    #   from my_package.iosxe.config.polaris_dev.routing.ospf.yang import Ospf
    #
    # where
    # -----
    #    relative path = config, routing, ospf
    #    tokens        = iosxe, polaris_dev, yang
    #    target        = Ospf()


.. _abstract_search_algorithm:

Search Algorithm
----------------

The search engine combines the user's **relative path** and currently known
**tokens** into possible **absolute paths** (python module names) and searches
through them. A match occurs when an implementation is found (ie the target 
exists at the candidate relative path). Otherwise, the next combination is 
tried. If no target is found, a ``LookupError`` would be thrown.

As the token names are not pre-defined, the search engine orders
all tokens in a pre-defined fashion:

    - token describes a set of *differences*
    - token positions are always fixed w.r.t. to its left (parent)
    - tokens on the right are more *specific* than tokens on the left
    - each token may only appear *once* in a combination
    - greedy match: more tokens matches is always better than less.

.. code-block:: text

    Given tokens: a, b, c and d, the preferred token combination would be:

        a b c d
        a b c
        a b
        a
        (no tokens)

These combinations are then *multiplexed* to user's **relative path** into 
potential **absolute paths** to search for, using the following rules:
    
    - absolute paths must always start with the abstracted package name.

    - the order of relative path sections (words divided by ``.``) must be
      preserved.

    - the order of token combinations must be preserved.

    - tokens may take place before and after each relative path section, and may
      appear in multiples together. (eg, ``library.iosxr.google.latest.mpls``)

    - the last resort option is to try with "no token", eg, matching the 
      relative path directly.

Combining the above rules, the ideal solution would be a multi-combinatory 
mathematical function, whose search complexity is ... *(insert math here)* ... 
exponential. 

.. code-block:: text
    
    Given Package: my_pkg
    Relative Path: X, Y
    Tokens: a, b
    Target: MyClass()

    We could have the following mathmatical combinational possibilities:

        1. my_pkg.a.X.b.Y.MyClass()
        2. my_pkg.a.X.Y.b.MyClass()
        3. my_pkg.X.a.Y.b.MyClass()
        4. my_pkg.X.a.b.Y.MyClass()
        5. my_pkg.X.Y.a.b.MyClass()
        6. my_pkg.a.X.Y.MyClass()
        7. my_pkg.X.a.Y.MyClass()
        8. my_pkg.X.Y.a.MyClass()
        9. my_pkg.X.Y.MyClass()

    And that's just with two tokens and two path sections!

The actual implementation internally is much simpler. When an an abstracted
package is defined/declared and the lookup object is created, the package and 
all of its child modules are *recursively imported*. This allows the abstraction
engine to build an internal table of relative paths, their available token 
combinations learnt from the import and its corresponding module. This reduced
**relative path + tokens** relationship effectively simplies the above
brute-force search algorithm into an ``O(n)`` lookup, where ``n`` is the number 
of tokens.

.. code-block:: text

    Pseudo Lookup Table
    ===================

    Relative Path            Tokens Combos           Corresponding Module
    -------------            -------------           --------------------
         X.Y                      a, b                     X.a.Y.b
         X.Y                      a                        X.a.Y
         X.Y                      None                     X.Y

    (shown in order of preference, from top down)

This algorithm limits to only dealing with what's been defined in the user 
library, instead of going through all possible permutations of **relative path**
and **tokens**. The system assumes that it is unlikely for users to make
redundant declarations, such as defining both ``from X.a.Y.b import target`` and 
``from X.a.b.Y import target`` within the same library.

.. note:: 
    
    The learning process safeguards against these redundant scenarios.


.. _token_builder:

Token Builder
-------------

The token builder is a simple function that implements the token permutation 
portion of the :ref:`abstract_search_algorithm`. The default token builder is
available as ``abstract.magic.default_builder()``.

.. csv-table:: default_builder Argument List
    :header: "Argument", "Description"

    ``tokens``, "list of tokens to permute"
    ``mandatory``, "list of tokens that must be used"

.. code-block:: python

    # Example
    # -------
    #
    #   pseudo code demonstrating the behavior of default token builder

    from abstract.magic import default_builder

    # without any mandatory tokens
    default_builder(tokens = ['nxos', 'n7k', 'c7003', 'yang', 'R8_1'])
    # [('nxos', 'n7k', 'c7003', 'yang', 'R8_1'), 
    #  ('nxos', 'n7k', 'c7003', 'yang'), 
    #  ('nxos', 'n7k', 'c7003'), 
    #  ('nxos', 'n7k'), 
    #  ('nxos',), 
    #  ()]

    # a mandatory token is one that MUST be used in the search
    default_builder(tokens = ['nxos', 'n7k', 'c7003', 'yang', 'R8_1'], 
                    mandatory = ['yang'])
    # [('nxos', 'n7k', 'c7003', 'yang', 'R8_1'), 
    #  ('nxos', 'n7k', 'c7003', 'yang'), 
    #  ('nxos', 'n7k', 'yang'),
    #  ('nxos', 'yang'),
    #  ('yang',)]

In essence, the "tokens" input parameter to the builder is a reflection of
the actual, longest possible chain of tokens under any given relative path. If
no target is found at this token/relative path combination, the next, reduced 
set of tokens is tried. This reduction mechanism always reduces from the right.

Use the ``mandatory`` input argument when you absolutely require some tokens to
be present in any token permutations during abstraction. This can be useful when
you do not want the system to automatically fallback using the above logic and 
remove it. This ensures the proper "set" of libraries is picked.
