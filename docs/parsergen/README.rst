.. automodule:: parsergen

Introduction
============

``Parsergen`` is capable of parsing both tabular and non-tabular "show"
command output once the user properly teaches it how. It is also capable of parsing
a mixture of tabular and non-tabular show command output.

* In the case of tabular parsing, the user needs to provide the column titles in order to allow the table to be automatically parsed, check :ref:`tabular parsing<oper_fill_tabular>` for details.


* In the case of non-tabular parsing, the user can provide parsing instructions to ``parsergen`` by using a convenient human-readable :ref:`core_markup` that ``parsergen`` uses to synthesize the `regular expressions<re>` it needs to parse the data check :ref:`non-tabular parsing<non_tabular_parsing>` for details.

.. note:: The user also has the option to create their own `regular expression<re>` 
    input manually rather than using the markup syntax (see `extend` for details).

