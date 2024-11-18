API Guidelines and good practices
=================================

Genie Apis comes with a guideline. This guideline is there to make the apis
easy to use and consistent.

:apis:`Website with all existing apis<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`

All these apis are open-source. Ready for you to contribute!

Functions
---------

Functions are really useful when you need to do a task over and over. For
example, if you want to get the Ip address of different interfaces in a
device, you can create a function that does that for you:

.. code:: python

   def get_address(dev, interface):
       out = dev.parse("show ip interface brief {interface}".format(interface=interface))
       return out['interface'][interface]['ip_address']

There you go, now every time you need the ip address of an interface you
can re-use this function whenever you want. It would be nice if everyone
could use this function when developing network automation and although you who
created this function know what is its purpose, other Genie users may not.
That’s why we should always write good self-explanatory names for
functions. For example, a nice name for below function would be:

.. code:: python

   def get_interface_ip_address(dev, interface):
       out = dev.parse("show ip interface brief {interface}".format(interface=interface))
       return out['interface'][interface]['ip_address']

**Way better right**? Now only reading the function name I have an idea what
is the function purpose. Here are some recommendations when writing function
names for Genie. In Genie we have three types of functions, get, verify
and configure.

Get functions
-------------

A get function always returns values. These values may be a number, a
string, or even a list. A get function starts with `get_`.

.. code:: python

   def get_netmask()
   def get_mac()

But those are bad ‘get’ function names because they don’t say anything
about the function purpose. **Good names** would be:

.. code:: python

   def get_interface_netmask()
   def get_interface_mac_address()

Verify functions
----------------

This function verifies a value on a configuration and returns True or
False. A verify function starts with `verify_` or `is_`.

.. code:: python

   def is_in_running_config()
   def verify_in_show_interfaces()

But again, those are not nice names for functions because we don’t know
exactly what they are doing. **Good names** for those would be:

.. code:: python

   def is_interface_present_running_config()
   def verify_interface_description_in_show_interfaces()

Also we can write functions to check if an output is as expected. For
example:

.. code:: python

   def verify_interface_status_in_state(interface, state):
       # Here we use keyword 'state'
       status = get_interface_status(interface)
       # State could be 'up' or 'down'
       if state == status:
           return True
       else:
           return False

   def verify_address_family_of_interface(interface, expected_address_family):
       # In this case we use keyword 'expected_' for the address_family we are expecting
       address_family = get_address_family_of_interface(interface)
       if address_family == expected_address_family:
           return True
       else:
           return False

Configure functions
-------------------

A configure function applies a configuration to a device. Method name
should describe what it is configuring. For example:

.. code:: python

   def shutdown_interface()
   def configure_vrf_on_interface()

Arguments
---------

We've discussed on how to write meaningful function names and now every Genie
user is using your functions. We also need consistent argument name; otherwise
using different functions will get confusing.

.. code:: python

   def get_interface_ip_address(device, interface):
       out = dev.parse("show ip interface brief {interface}".format(interface=interface))
       return out['interface'][interface]['ip_address']

There you go, everytime Genie users want to use that function, they will
know exactly which arguments to pass. When choosing arguments names,
it’s a good practice to write names that everyone will know what is the
purpose of an argument. Here are some suggestions for common argument
names used in Genie:

-  device: Device object. Always the first argument
-  interface: Name of an interface. Ex: GigabitEthernet.1
-  neighbor_interface: Neighbor interface name (in case function needs
   both interface and neighbor_interface)
-  bgp_as: AS router number
-  neighbor_as: AS router number of a neighbor (in case function needs
   both bgp_as and neighbor_as)
-  uut_address: Address of unit under test
-  neighbor_address: Address of a neighbor
-  vrf: Name of a VRF
-  vrf_neighbor: Name of a VRF of a neighbor (in case function needs both
   vrf and vrf_neighbor)
-  address_family: Address family, such as ipv4 or ipv6
-  address_family_neighbor: Address family of a neighbor(in case function
   needs both address_family and address_family_neighbor)
-  ip_address: Any ip address, such as an interface address
-  netmask: Netmask address
-  mac_address: MAC address
-  state: When checking is an output is in a state
-  expected\_ : For verify functions when we need to check if an output is
   as expected. Examples: (expected_vrf, expected_address_family)


Arguments good practices
------------------------

It’s not a good practice and it’s not recommended to set default values
like this:

.. code:: python

   def some_function(interfaces_list=[], interfaces_dict={})

Intead, we can default values as None and then check in function:

.. code:: python

   def some_function(interfaces_list=None, interfaces_dict=None):
       
       if interfaces_list is None:
           interfaces_list=[]
       if interfaces_dict is None:
           interfaces_dict={}

The reason is a new list/dict is created once when the function is
defined, and the same list is used in each successive call, which can
break everything.

Docstring
---------

Now we know how to create nice names for functions and arguments. But what
if I need to add an argument that is not in that list? How can we make
use everyone will know what exactly value we should pass? The answer is
docstring. **A docstring describes the function and arguments purpose, what
the function returns and exception it may raise**. Docstring recommendation
for Genis APIs follows the following structure:

.. code:: python

   def some_function(arg1, arg2...):
       ''' What does this function do?

           Args:
               arg1 ('type?'): What is this argument for?
               arg2 ('type?'): What about this one?
           Returns:
               Does it return a list? A number? A string?
               list: What is this list?
           Raises:
               Does this function raise an exception?
       '''

That been said, let’s improve our ‘get_interface_ip_address’ to support
docstring:

.. code:: python

   def get_interface_ip_address(device, interface):
       ''' Get Ip address of an interface

           Args:
               device ('obj'): Device object
               interface ('str'): Interface name
           Returns:
               str: Address of interface
           Raises:
               N/A
       '''
       out = dev.parse("show ip interface brief {interface}".format(interface=interface))
       return out['interface'][interface]['ip_address']

Beautiful right? Now it’s even easier to understand the purpose of our
function and everyone can re-use your beautiful function.

General good practices and recommendations

When writing a new API it is recommended following these good practices
for every function

Show and configure commands
---------------------------

It is highly encouraged to use keys and Python .format() for commands.
Such as:

.. code:: python

   device.parse("show ip interface brief {interface}".format(interface=interface))

   device.configure("interface {interface}\n"
                    "shutdown".format(interface=interface))

When writing multi-lines commands, it is more readable if we break in
multiple lines:

.. code:: python

   device.configure('command 1\ncommand 2\n command 3')

   device.configure('command 1\n'
                    'command 2\n'
                    'command 3')

Log messages We encourage the user to write log messages describing what
is going on your function. That is useful when we need to check errors.
You can use python ‘logging’ module. Let’s improve our function to use
logs

.. code:: python

   import logging

   log = logging.getLogger(__name__)

   def get_interface_ip_address(device, interface):
       ''' Get Ip address of an interface
           Args:
               device ('obj'): Device object
               interface ('str'): Interface name
           Returns:
               str: Address of interface
           Raises:
               N/A
       '''
       log.info('Getting ip address of interface {interface}'.format(interface=interface))
       out = dev.parse("show ip interface brief {interface}".format(interface=interface))    
       ip_address = out['interface'][interface]['ip_address']

       log.info('Found IP address {ip_address}'.format(ip_address=ip_address))

       return out['interface'][interface]['ip_address']

Exceptions
----------

Sometime our function will break and most of the time that happens because
of exceptions. An exception is an error that happens during the
execution of a program. When that error occurs, Python generates an
exception that can be handled, which avoids your program to crash.

When we are executing a parser command, most of the times it will raise
SchemaEmptyParserError, so we need to ‘capture’ it and handle it. Let’s
improve our function to handle exceptions:

.. code:: python

       
       from genie.metaparser.util.exceptions import SchemaEmptyParserError

       def get_interface_ip_address(device, interface):
       ''' Get Ip address of an interface
           Args:
               device ('obj'): Device object
               interface ('str'): Interface name
           Returns:
               str: Address of interface
           Raises:
               N/A
       '''
       log.info('Getting ip address of interface {interface}'.format(interface=interface))
       try:
           out = dev.parse("show ip interface brief {interface}".format(interface=interface))    
       except SchemaEmptyParserError:
           # If not output from the device, then its all good.
           # No ip address
           log.info('Could not find IP address')
           return None
       ip_address = out['interface'][interface]['ip_address']

       log.info('Found IP address {ip_address}'.format(ip_address=ip_address))

In ‘get\_’ functions, when SchemaEmptyParserError is raised, we capture it
and return a value. So for example, if the function was supposed to return
a list, we return an empty list. If it was supposed to return a python
dictionary, we return an empty dictionary and so forth so on.

For configuring commands in ‘config’ functions it will usually raise a
SubCommandFailure. In this case, we capture it and raise a
SubCommandFailure with a message describing what happened. For example:

.. code:: python

   from unicon.core.errors import SubCommandFailure
   try:
       device.configure("interface {interface}\n"
                         "shutdown".format(interface=interface))
   except SubCommandFailure:
       raise SubCommandFailure('Could not shutdown interface {interface}'.format(interface=interface))

For verify functions, we can capture exceptions and return True/False. For
example:

.. code:: python

   from unicon.core.errors import SubCommandFailure

   def verify_interface_config_is_rejected(device, interface):    
       try:
           device.configure("int {interface}".format(interface=interface))
       except SubCommandFailure as e:
           return True

       return False

Using timeout
-------------

Sometimes after a configure command, we want to check if the result is
as expected, but these changes can take a couple of seconds or even
minutes to happen. In this case, we suggest using genie Timeout class.
Here is how we use it.

.. code:: python

   from genie.utils.timeout import Timeout

   # Using function right after interface shutdown
   def is_interface_down_state(interace, max_time=60, check_interval=15):
       timeout = Timeout(max_time, check_interval)
       while timeout.iterate():
           state = get_interface_state()
           if state == 'down':
               return True

           timeout.sleep()
       return False

Here function will check every 15 seconds (check_interval) for 60 seconds
(max_time) the state of the interface. It’s recommended to set default
values for max_time and check_interval.

Accessing dictionaries
-----------------------

It’s highly encouraged to use dict function ‘.get()’ when accessing python
dictionaries fields. This avoids your function to break when a key is
missing in the dictionary. Here is an example improving our
get_interface_ip_address function"

.. code:: python

   from genie.metaparser.util.exceptions import SchemaEmptyParserError

   def get_interface_ip_address(device, interface):
       ''' Get Ip address of an interface
           Args:
               device ('obj'): Device object
               interface ('str'): Interface name
           Returns:
               str: Address of interface
           Raises:
               N/A
       '''
       log.info('Getting ip address of interface {interface}'.format(interface=interface))
       try:
           out = dev.parse("show ip interface brief {interface}".format(interface=interface))    
       except SchemaEmptyParserError:
           # If not output from the device, then its all good.
           # No ip address
           log.info('Could not find IP address')
           return None
       # Here .get will get interface key. If dictionary does not have interface, it will return a empty dictionary
       ip_address = out['interface'].get(interface, {}).get('ip_address', None)

       log.info('Found IP address {ip_address}'.format(ip_address=ip_address))

Avoiding name conflicts
--------------------

Sometimes when writing a function with a beautiful name, it is recommended
to check if there is another function with that same name, even in other
libs. For example:

.. code:: python

   # Conflict
   from vrf.retrieve import get_something
   from bgp.retrieve import get_something

By keeping your function name specific, this should not happen.

Calling other APIs
----------------

If you need to use another API within one you are writing it is
highly encouraged to use only keyword arguments due to OS abstraction.
