.. _contribute_to_parser_build:

Contribute in parsers build
===========================

To contribute in the parsers build, you need to activate the developer mode. You
will need to follow the below steps in order to do so.

.. code-block:: text

	pip uninstall genie.libs.parser
	git clone parser module (GitHub/BitBucket)
	cd $VIRTUALENV/pypi/genieparser/
	make package

	# Now you build your parser under the corresponding OS as per the hierarchy
	# below.

	# Done with the developer mode and already committed your parser?
	cd $VIRTUALENV/pypi/genieparser/
	make undevelop

	# Install parser module as a user again
	pip install genie.libs.parser

.. note::

    There is no manadate to switch back to user mode, if you would like to remain
    in developer mode, it's fine. Just make sure you won't accidently push a code
    breakage to the official branch.

Parser file hierarchy
---------------------

.. code-block:: text

    parser
     |-- __init__.py
     |-- iosxe
     |   `-- __init__.py
     |-- iosxr
     |   `-- __init__.py
     |-- nxos
     |   |-- __init__.py
     |   `-- show_version.py
     `-- template
         `-- template.py

    where the top level is broken down further into OS-specific directories,
    and optionally, have a template directory for demonstrating other developers
    what to do.

   /parser
       The parser file system root.The parser file categories have been 
       organized based on OS/platform types.

   /parser/__init__.py
       Place to declare the abstraction-enabled package. 

   /parser/nxos
       NXOS platform-specific parsers. 

   /parser/nxos/__init__.py
       Place to declare the abstraction token (nxos) in the abstraction-enabled 
       package.

   /parser/nxos/show_version.py
       As an example, show_version.py aims to guide developers on writing their 
       first parsers.

   /parser/iosxe
       IOSXE platform-specific parsers. This directory holds all iosxe 
       parser files.

   /parser/iosxe/__init__.py
       Place to declare the abstraction token (iosxe) in the abstraction-enabled 
       package.

   /parser/iosxr
       IOSXR platform-specific parsers. This directory holds all iosxr 
       parser files.

   /parser/iosxr/__init__.py
       Place to declare the abstraction token (iosxr) in the abstraction-enabled 
       package.
       
   /parser/template
       Parser template folder - all template files can be found inside of 
       this directory.

   /parser/template/template.py
       Parser template file - the template doc defines the common 
       format/structure/guidelines which helps to guide developers to 
       complete their parser development.

Parser file naming convention guidelines:
-----------------------------------------
   **Recommendation #1:** Parser file contains at least one parser class which 
   includes actual parsing mechanisms (cli, xml, yang) implementation. 
   All relevant parser classes (name with same starting words) should be 
   sit in the same file. For instance, parser class ShowXxx, ShowXxxYyy, 
   and ShowXxxYyyZzz should be implemented in file: show_xxx.py.
   
   **Recommendation #2:** Parser module (parser file) name should be the first 
   two words of the corresponding cli command or equivalent. 
   For example: show_interface.py. If the first two words contain strong 
   ambiguity (e.g.: show ip), extend the next word (e.g.: show_ip_ospf.py) to 
   clarify the parser purpose.
   
   **Recommendation #3:** Each parser class within the parser module must 
   inherit from ``MetaParser`` class. We strongly recommend to name the class 
   using the full cli command or equivalent to represent the actual parser 
   (e.g.: ShowIpOspfInterface).
   
   **Recommendation #4:** For variable phrases within the parser class name 
   (e.g.: show interface Eth3/4), use _WORD_ to present the phrase 
   (e.g.: ShowInterface_WORD\_).

Parser development review criteria
----------------------------------

It is expected that all parser code get reviewed by developers' local team 
before submitting to official ``Cisco-shared`` in order to reduce overall 
traffic & comments.

Developer is expected to raise a pull request on
:codereview:`code review <http>` so Genie developers review before
committing to the community parser repository.

Submit the parser source code (new code, new folder, fixing, enhancement, etc), 
diff using ``diff -u 20``  as part of the pull request.

.. note::
    
    It is strongly recommended to submit unit tests associated with the parser 
    implementation.