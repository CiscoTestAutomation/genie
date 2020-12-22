.. _harness_overview:

Harness Guide
=============

``Genie`` is the highly anticipated Python implementation of :best:`BEST <http>` that Cisco
engineers have been waiting for!

With the ``Genie`` test harness, the concept of event driven testing is
introduced into the pyATS framework. With event driven testing, script and
testcases are derived dynamically based on selected **triggers** and
**verification** from the ``Genie SDK`` pool.  

Using the ``Genie`` test harness, automation becomes focused primarily on developping targeted test 
scenarios where the action is handled in the **trigger** and what needs to be verified 
before and after the **trigger** in  **verification**.  

The following sections provide more details about how ``Genie`` test harness may be used by 
engineers. 

The user section explains how to use the ``Genie`` harness.
The developer section explains how to contribute new triggers and
verifications.

 .. toctree::
    :maxdepth: 3

    user/index
    developer/index
    genietelemetry/integration

.. sectionauthor:: Jean-Benoit Aubin <jeaubin@cisco.com>

