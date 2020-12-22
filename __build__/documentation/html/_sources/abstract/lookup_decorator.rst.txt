.. _abstract_lookup_decorator:

Lookup Decorator
================

``LookupDecorator`` is a feature extension to :ref:`abstract_lookup_cls`. 
Whereas the ``Lookup`` class allows users to write **different** classes,
functions and variables in tokenized modules and dynamically reference them, the 
lookup decorator operates at the class method level, allowing users to write
a **single class** with different method implementations per each token variance
combination.

.. code-block:: text

                                                    .--> TokenX.Y class method
                                                   /
    UserScript -> import cls -> call cls method --+----> TokenX class method   
                                                   \
                                                    `--> Default (no token)
                                                           class method

.. code-block:: python

    # Example
    # -------
    #
    #  a simple lookup decorator example

    # my_library/config.py
    # --------------------

    # import the decorator
    # (note the lowercase 'lookup')
    from abstract import lookup

    # define a class using the decorator on its methods
    class ConfigureRouting(object)
        def __init__(self, os):
            self.os = os

        # apply the decorator on methods to be abstracted
        @lookup('os')
        def apply_config(self):
            # ... insert generic/non-os specific code here


    # my_library/nxos/config.py
    # -------------------------
    from ..config import ConfigureRouting as BaseConfigRouting

    # inherit the parent class
    class ConfigureRouting(BaseConfigRouting):

        # define the same method specific to this token
        def apply_config(self):
            # ... insert nxos specific code here

The main benefit of using ``LookupDecorator`` is that it allows the user to 
perform standard python ``import`` and deal with only one class instance. 
During runtime, the engine looks up the class's attributes and forms a list of
tokens based on these values, and replaces the decorated methods during with a 
"more" appropriate one from a tokenized search
(see :ref:`abstract_search_algorithm`).

.. code-block:: python
    
    # Example
    # -------
    #
    #   using the above code

    # import the main entry class directly
    from my_library.config import ConfigureRouting

    # use it as you would naturally
    obj = ConfigureRouting(os = 'nxos')

    # when a decorated method is called, the lookup occurs and the 
    # most appriorate method from one of its subclasses is called instead.
    result = obj.apply_config()
    # lookup information
    # ------------------
    #   attributes to read: os
    #   attribute value: os = 'nxos'
    # 
    # thus, the search result equivalence is:
    #   from my_library.nxos.config import ConfigureRouting
    #   result = ConfigureRouting.apply_config(obj)


Usages
------

To use ``LookupDecorator``, start with writing your abstraction-enabled library
as you normally would. When arriving at defining classes that requires methods
level abstraction, simply apply the decorator onto each method that needs to be
abstracted. Behaviors:

- Lookup decorator can be imported as ``lookup`` (note the lowercase), or as
  ``decorator.LookupDecorator``. They are exactly the same, but some may prefer
  one name over the other.

  .. code-block:: python

      from abstract import lookup
      from abstract.decorator import LookupDecorator

- The usage of lookup decorator does not mandate a top-level 
  :ref:`abstraction_pkg` declaration. It only requires :ref:`abstraction_tokens`
  definitions under the module where the lookup decorator is used.

  .. code-block:: text

      Example:
        if LookupDecorator is used in on class X under module A.B, 
        tokens should be defined as child modules under A.B.

- Lookup decorator takes in a list of **attributes names** as arguments. During
  runtime, the engine will lookup the given class instance for these attributes
  to be used as tokens. This mechanism is called an *attribute getter*. The 
  default attribute getter looks up both the class instance and 
  ``instance.device`` (if exists) for the named attribute. 

  .. code-block:: python

      class MyClass(object):

          @lookup('attr_1', 'attr_2')
          def some_func(self):
              # ...

      # equivalent to
      #     obj = MyClass()
      #     token_1 = getattr(obj, 'attr_1', getattr(obj.device, 'attr_1'))
      #     token_2 = getattr(obj, 'attr_2', getattr(obj.device, 'attr_2'))

- The search for matching token combinations always begins at this class's 
  module declaration level onwards. It will match for the same **relative path**
  as the current module, and the same class name (or names in nested class defs)
  and target method.

  .. code-block:: text

      Example:
        a search originating from: moduleX.moduleY.classA.classB.some_func()
        may match: moduleX.moduleY.tokenJ.tokenK.classA.classB.some_func()

- the default *attribute getter* can be replaced by providing a new function
  through ``attr_getter`` argument. The provided function must take in two 
  arguments: ``obj`` and ``attr`` for both the object under scrutiny and the
  attribute to lookup

.. code-block:: python

    # Examples
    # --------
    #
    #   lookup decorator usage

    # assuming we had a lookup-decorator enabled library
    # my_library.my_module.ConfigureOspf

    # import it regularly
    from my_library.my_module import ConfigureOspf

    # instaciate it naturally
    # (in this case our class requires argument 'os' and mgmt_context)
    routing = ConfigureOspf(os = 'iosxr', mgmt_context = 'yang')

    # if we call a decorated method, say, apply_configuration
    # eg, code snippet:
    #       @lookup('os', 'mgmt_context')
    #       def apply_configuration(self):
    #           # ... code

    routing.apply_configuration()
    # the engine translates this to:
    #    token_os = routing.os = 'iosxr'
    #    token_mgmt_context = routing.mgmt_context = 'yang'
    # and the resulting lookup equivalent could be:
    #    from my_library.my_module.iosxr.yang import ConfigureOspf
    #    result = ConfigureOspf.apply_configuration(routing)
    
    # note
    # ----
    #   after lookup is performed, notice that the found target class's method
    #   is called directly with the original class instance as first argument.
    #   This is a python property: class methods can be treated as "functions"
    #   if you pass in a "similar" class instance as the first argument.
    #   See: https://docs.python.org/3.4/tutorial/classes.html#method-objects

.. csv-table:: LookupDecorator Class Argument List
    :header: "Argument", "Description"

    ``*attrs``, "list of attributes to be used read as input tokens for lookup"
    ``attr_getter``, "class instance attribute getter (optional)"
    ``builder``, "token permutation builder (optional)"
    ``**builder_kwargs``, "any keyword arguments/values to be passed to the
    builder (optional)"

Lookup From Device Decorator
============================

``LookupDecorator.from_device`` is a feature extension to ``LookupDecorator``.
The lookup.from_device decorator operates at the runtime, allowing users to
write a **single class** with different method implementations and dynamically
based on the token variance combination from device's custom abstraction or
pre-defined at class method level.

.. code-block:: python

    # Example
    # -------
    #
    #  a simple lookup.from_device decorator example

    # my_library/config.py
    # --------------------

    # import the decorator
    # (note the lowercase 'lookup')
    from abstract import lookup

    # define a class using the decorator on its methods
    class ConfigureRouting(object)
        def __init__(self, os):
            self.os = os

        # apply the decorator on methods to be abstracted dynamically based on
        # custom abstraction data
        @lookup.from_device
        def apply_config(self):
            # ... insert generic/non-os specific code here

        # apply the decorator on methods to be abstracted dynamically based on
        # custom abstraction data or fallback to token 'os'
        @lookup.from_device('os')
        def check_config(self):
            # ... insert generic/non-os specific code here
