Parsing Both Tabular and Non-Tabular Output
===========================================
For CLI command outputs that have both tabular and non-tabular components,
it is possible to use both kinds of parsers.  Please refer to the following
:ref:`example<core_example>`.

Putting It All Together
=======================
Please see the following downloadable file for instructions
on how to run a sample pyATS job that does the following:

1. Connects to a router in your testbed
2. Runs a "show interface" command
3. Parses output using conventional cAAs/TCL parser
4. Runs the same "show interface" command again
5. Parses output using parsergen
6. Compares the results of each parser.
7. Runs a parse/compare operation against a small set of selected keys.
8. Runs a "show arp" command
9. Parses the output using parsergen

:download:`readme_file <readme.txt>`


Standalone Parsing
==================
It is also possible to run ``parsergen`` in standalone mode.
In this model, all interactions with the device under test and the tcl
interpreter are "mocked", meaning that while the parser thinks it is
talking to a real device and a real TCL interpreter, it is really talking
to mocks that are under the user's complete control.  The advantage is that a
parser can be tested with a variety of different kinds of inputs in an
incredibly swift manner because there is no requirement to have a real
device up and running.

Here's an example of running the non-tabular parser in standalone mode:
:download:`nontabular_parser_xrvr.py <nontabular_parser_xrvr.txt>`.

Here's an example of running the tabular parser in standalone mode:
:download:`tabular_parser_subclass.py <tabular_parser_subclass.txt>`.