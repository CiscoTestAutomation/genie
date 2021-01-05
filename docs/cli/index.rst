.. _genie_cli:

Genie Command Line
==================

`genie` CLI is the network engineer's most valuable tool for network
automation! In this section we will take a look at how ``Genie`` CLI can help
expedite automation of your network.

``Genie`` CLI is a powerful linux-based command-line utility offering ``Genie``
Python functionality directly from a linux terminal. It requires no previous
knowledge of Python or network programming, making it a great way to start
getting acquainted with ``Genie``.

`genie` is the top-level command-line entry point for ``Genie``. All other
functions are loaded as subcommands of this command.

Ensure you have ``Genie`` installed prior to using `genie` CLI. Follow the steps
listed under :ref:`Genie Installation <installation>`

For a complete list of built-in functions avaialable within `genie` CLI,
execute the following in your linux terminal:

.. code-block:: bash

    (genie) bash-4.1$ genie --help
    Usage:
      genie <command> [options]

    Commands:
        create              Create Testbed, parser, triggers, ...
        diff                Command to diff two snapshots saved to file or directory
        dnac                Command to learn DNAC features and save to file
        learn               Command to learn device features and save to file
        parse               Command to parse show commands
        run                 Run Genie triggers & verifications in pyATS runtime environment
        shell               enter Python shell and load a Genie testbed file and/or Pickled file

    General Options:
      -h, --help            Show help

    Run 'genie <command> --help' for more information on a command.

Let's get into each of those!

.. toctree::
    :maxdepth: 1

    genie_parse
    genie_learn
    genie_diff
    genie_run
    genie_shell
    genie_dnac
    genie_create

.. sectionauthor:: Lubna Rasheed <lrasheed@cisco.com>
