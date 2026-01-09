Exploratory Testing in Script Generation
==========================================

While building automation scripts, you'll want to explore device behavior and try
experimental actions without polluting your final testcase. LAMP's test sections let
you separate exploratory actions from production code.

The Challenge
-------------

When generating testcases interactively, you might execute several commands to
understand device responses, try different configuration approaches, test edge
cases, or debug unexpected behavior.

Without proper separation, all experimental actions end up in your saved testcase,
making it difficult to read, maintain, and larger than necessary.

The Solution: Test Sections
---------------------------

Use the ``test_section`` command to create isolated sections that can be easily removed:

.. code-block:: console

    (lamp-dev1) test_section exploratory
    (lamp-dev1) execute show version
    (lamp-dev1) execute show interfaces
    (lamp-dev1) execute show ip route | include 1.1.1.1
    (lamp-dev1) remove -n exploratory

**Workflow**

1. Create a new test section: ``test_section exploratory``
2. Execute exploratory actions: Run any commands you want to test
3. Remove the section: ``remove -n exploratory`` deletes all actions
4. Continue with production actions: Your testcase stays clean

Practical Example
-----------------

You're building a configuration testcase but need to verify device behavior first:

.. code-block:: console

    # Start main test section
    (lamp) test_section main
    (lamp-dev1) configure interface Ethernet0/0 + ip address 10.0.0.1 255.255.255.0

    # Explore impact
    (lamp-dev1) test_section exploratory
    (lamp-dev1) execute show ip interface brief
    (lamp-dev1) execute show ip route
    (lamp-dev1) parse show interfaces Ethernet0/0

    # Remove exploratory section
    (lamp-dev1) remove -n exploratory

    # Continue with production actions
    (lamp-dev1) configure interface Ethernet0/0 + ip ospf 1 area 0
    (lamp-dev1) sleep 30
    (lamp-dev1) execute -i show ip ospf neighbor

When you save, only the ``main`` section is included.

Creating Aliases for Quick Exploration
---------------------------------------

Define aliases to streamline the workflow:

.. code-block:: console

    (lamp) alias create explore test_section exploratory
    (lamp) alias create cleanup remove -n exploratory

Your workflow becomes:

.. code-block:: console

    (lamp) explore
    # ... exploratory actions ...
    (lamp) cleanup

Much faster with less typing!

Summary
-------

The ``test_section`` command enables a clean, iterative workflow:

    1. Build production logic in named sections
    2. Create exploratory sections for testing and debugging
    3. Remove exploratory sections before saving
    4. Save clean, focused testcases

This keeps your automation scripts maintainable and prevents experimental code from
polluting your production testcases.
