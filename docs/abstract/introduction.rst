Introduction
============

In software engineering and computer science, **abstraction** is a technique for
managing complexity of computer systems. It works by establishing a level of
complexity on which a person interacts with the system, suppressing the more
complex details below the current level. The programmer works with an
idealized interface (usually well defined) and can add additional levels of
functionality that would otherwise be too complex to handle. (:wikipedia:`Wikipedia <http>`)

As Python is a :dynamicallytyped:`dynamically typed <http>`,
:objectoriented:`object-oriented <http>` programming language, function/code
and data abstraction can be achieved easily through
:ducktyping:`duck typing <http>` and :inheritance:`inheritance <http>`:
defining classes/objects that behaves similarly in a given context, and hiding
details of implementation under its methods and properties.

    *If it flies like a duck & quacks like a duck, it's a duck!*

.. code-block:: python

    # Example
    # -------
    #
    #   duck typing and inheritance

    class Mallard(object):
        def quack(self):
            raise NotImplementedError

        def fly(self):
            raise NotImplementedError

    class Duck(Mallard):
        def quack(self):
            print("Quack, quack!");

        def fly(self):
            print("Flap, Flap!");

    class Person(Mallard):
        def quack(self):
            print("I'm Quackin'!");

        def fly(self):
            print("I'm Flyin'!");

    for mallard in [Duck(), Person()]:
        mallard.fly()
        mallard.quack()


The above stipulates how classes can be defined to behave similarly (eg, through
similar interfaces and subclassing). This is the underlying principle for Genie
Libraries (ie. parsers and APIs). However, it doesn't solve how the system
should pick the *correct class* during runtime.


Our Solution
------------

The ``abstract`` package is intended solve the above issue by **standardizing the
abstraction decision making process**. Through the use of abstraction tokens
gathered from devices & lookup algorithms, the package empowers users to write
agnostic libraries and scripts capable of handling a variety of differences between
os/platform/model, etc.

.. figure:: abstract.png
    :align: center

