.. _clean_doc_quick_start_getting_ready:

Getting Ready
=============

.. note::

    This page is the same as `Getting Ready` from the `Quick Start` section. You can skip this if you have already read it.

.. topic:: pyATS Clean requires the following inform to perform a clean:

    * `pyATS and Genie installed (latest version)`_
    * `Testbed YAML File`_
    * `Clean YAML File`_

pyATS and Genie installed (latest version)
------------------------------------------
The latest version will contain all the released features and will be the most stable.

Testbed YAML File
-----------------
For the purpose of this guide, the below testbed file will be used. For you to run the example, replace this
testbed file with one of your own and make any modifications that are highlighted throughout this guide. Also ensure you
replace `PE1` references with your own device.

For starters, we need to specify both `os` and `platform` for **each** device in the testbed. We also need to add the
`abstraction` block under the custom key to help pyATS Clean choose the correct stage implementations.

.. note::

    Refer to the :ref:`Supported Platforms and PowerCyclers <clean_doc_supported_os>` document to determine what the
    correct values for `os` and `platform` are.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 3-7

    devices:
        PE1:
            os: nxos
            platform: n9k
            custom:
                abstraction:
                    order: [os, platform]
            connections:
                cli:
                    protocol: telnet
                    ip: 127.0.0.1

Clean YAML File
---------------
To start, lets create an empty `yaml` file. This file can be named anything you like but for the purpose of this guide,
we will name it `clean.yaml`.

This file will contain all the information required to drive the clean. In the next sections we will focus on adding content
to this file.
