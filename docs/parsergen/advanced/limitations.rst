Limitations
===========
``parsergen`` also has limitations that may prevent its deployment in some
parsing scenarios:

Currently, no support exists for the following:

 * Nontabular parser:

     * sectioning: (special parsing rules that apply only to a portion of the
       text to be parsed), define patterns for section entry/exit.  Allow sections
       within sections.

       * Indented blocks are not properly handled (for example, for XR
         ``show l2vpn forwarding private location 0/2/CPU0`` command).

     * Variable-length lists (these must be parsed manually), here is a :download:`workaround <non_tab_multi_example.txt>`.

     * Auto-regex-tag infix extension : Allow families of regex tags to be defined
       by extending the middle of the tag to allow section-specific parsing of text
       that contains repetitive input (such as interfaces in the command
       "show interface")

     * subroutining (defining and including sections that are common among multiple
       CLI commands).

     * side effects : pre-and-post regex tag side effects (for example, transform
       by removing capitalization from a parsed field).

     * conditionality : only parse a regex tag if a particular condition is met.
       Optionally declare a parsing error if the condition is not met.

     * create derived keys : use previously parsed values to create compound keys.

     * markup syntax allowing multiple patterns per regex tag to handle
       changing CLI output between releases.

 * Tabular parser:

    * The tabular parser's justification setting applies to all columns.
      Thus, it canot handle tabular output containing both left and right
      justified columns.

    * The tabular parser doesn't handle a mixture of left-justified and
      centered column titles without a workaround (adding extra preceding spaces
      to the centered column title to make it look like a left-justified title).

    * The tabular parser cannot handle rows that flow across several lines.