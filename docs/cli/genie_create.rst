.. _cli_create:

pyATS Create
============

`pyats create` provide an easy way to create parsers, testbeds, and triggers.

.. note::
    pyats.contrib package needs to be installed for `pyats create` command. If not installed, please install by `pip install pyats.contrib`
    pyats.contrib GitHub : https://github.com/CiscoTestAutomation/pyats.contrib

To see what functionality `pyats create` offers, execute the following in your linux terminal:

.. code-block:: bash

    Usage:
      pyats create <subcommand> [options]

    Description:
      Creates script and library components automatically based on your input. These
      are helper functions intended to make your development life easier/reducing
      number of boilerplate to-dos.

    Subcommands:
      parser              create a new Genie parser from template
      project             create a new pyATS project from template
      testbed             create a testbed file automatically
      trigger             create a new Genie trigger from template

    General Options:
      -h, --help            Show help
      -v, --verbose         Give more output, additive up to 3 times.
      -q, --quiet           Give less output, additive up to 3 times, corresponding to WARNING, ERROR,
                            and CRITICAL logging levels

.. _cli_create_testbed:

pyATS Create Testbed
--------------------

`pyats create testbed` provide an easy way to create a testbed yaml file. It gives the ability to convert some sources containing device data into a testbed yaml that can be loaded directly. 

.. code-block:: bash

    Usage:
      pyats create testbed [source] [arguments]
    
    Testbed Options:
      [source]              Source of where to retrieve device data.
      --output OUTPUT       File location to output the created testbed yaml.
    
    General Options:
      -h, --help            Show help
      -v, --verbose         Give more output, additive up to 3 times.
      -q, --quiet           Give less output, additive up to 3 times, corresponding to WARNING, ERROR,
                            and CRITICAL logging levels

Generate from csv/excel file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following columns header to create a testbed yaml file from Excel/csv file:

+ **hostname** : *the host name of the device*
+ **ip** : *the ip address of the device, to specify a port, add the port number in the format of:* `ip:port`
+ **username** : *the username for logging into the device*
+ **password** : *the default password for logging into the device, user can leave this field blank for security reason, and Genie will prompt you to enter the password when you connect to the device*
+ **protocol** : *the protocol used to connected to the device i.e. ssh, telnet, etc..*
+ **os** : *the operating system for the device i.e. iosxr, iosxe, nxos, linux, etc..*
+ **enable_password** : *(Optional) to provide a different password for entering privileged EXEC mode with `enable` command*

All other columns not listed above will be added to the yaml as a `key: value` pair

**Example**

Here is an example excel file containing device data:

    .. figure:: Excel.png
        :alt: Sample Excel file

we can turn it into a testbed yaml file by running the following command:

.. code-block:: bash

    (venv)demo$ pyats create testbed file --path my_devices.xls --output yaml/my_testbed.yaml
    Testbed file generated:
    my_devices.xls -> yaml/my_testbed.yaml

This will give us the below yaml:

.. code-block:: yaml

    devices:
      R1:
        connections:
          cli:
          ip: 172.25.192.101
          port: 17013
          protocol: ssh
        credentials:
          default:
            password: cisco
            username: admin
          enable:
            password: cisco123
        os: iosxe
        type: iosxe
      R2:
        connections:
          cli:
            ip: 172.25.192.102
            port: 17015
            protocol: ssh
        credentials:
          default:
            password: cisco
            username: admin
          enable:
            password: cisco123
        os: iosxr
        type: iosxr
      R3:
        connections:
          cli:
            ip: 172.25.192.103
            port: 17019
            protocol: ssh
        credentials:
          default:
            password: cisco
            username: admin
          enable:
            password: cisco
        os: nxos
        type: nxos

.. tip::

    Add the `--encode-password` option to hide the password in the yaml as a secret string.
    However this is only for the purpose of obfuscation, the password is not cryptographically secure. Please refer to :pyats_secret_string:`Secret String <http>` for more detail.

Generate from multiple csv/excel files under a directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Having multiple csv/excel files? You can pass a directory as the input and another directory as the output, then it will create a testbed file for every excel in the provided directory.

.. code-block:: bash

    (venv)demo$ pyats create testbed file --path excels --output yamls -r
    Testbed file generated:
    excels/my_devices.xlsx -> yamls/my_devices.yaml
    excels/my_devices_2.xlsx -> yamls/my_devices_2.yaml
    excels/my_devices_test.csv -> yamls/my_devices_test.yaml
    excels/sub1/my_devices_csv.csv -> yamls/sub1/my_devices_csv.yaml
    excels/sub1/subsub1/my_devices_csv.csv -> yamls/sub1/subsub1 my_devices_csv.yaml 
    Errors:
    excels/my_devices_csv.csv has an error: Duplicate hostname "R2_xr" detected
    excels/my_devices_test_err.csv has an error: 'Every device must have a hostname'
    excels/my_devices_test_err.xlsx has an error: Error -3 while decompressing data: invalid code -- missing end-of-block
    Warnings:
    excels/not_excel.txt is not excel or csv
    excels/my_devices_csv.yaml is not excel or csv
    excels/sub1/not_sub_excel.txt is not excel or csv

.. note::
    The added `-r` option above will enable genie to look for excels in subdirectories.

Generate by entering device data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Don't have an excel sheet or a csv? Don't worry we got you covered! You can manually input the device data without providing the csv/excel file.
Just follow the prompt from the program to enter the data:

.. code-block:: bash

    (venv)demo$ pyats create testbed interactive --output yaml my_testbed.yaml --encode-password
    Start creating Testbed yaml file ...
    Do all of the devices have the same username? [y/n] y
    Common Username: admin
    Do all of the devices have the same default password? [y/n] y
    Common Default Password (leave blank if you want to enter on demand): 
    Do all of the devices have the same enable password? [y/n] n
    Device hostname: R1
        IP (ip, or ip:port): 172.15.192.101:17001
        Enable Password (leave blank if you want to enter on demand):
        Protocol (ssh, telnet, ...): ssh
        OS (iosxr, iosxe, ios, nxos, linux, ...): iosxe
    More devices to add ? [y/n] y
    Device hostname: R2
        IP (ip, or ip:port): 172.25.192.102:17002
        Enable Password (leave blank if you want to enter on demand):
        Protocol (ssh, telnet, ...): ssh
        OS (iosxr, iosxe, ios, nxos, linux, ...): iosxr
    More devices to add ? [y/n] n
    Testbed file generated:
    yaml/my_testbed.yaml

This will give us the below yaml (note the hidden password):

.. code-block:: yaml

    devices:
      R1:
        connections:
          cli:
            ip: 172.15.192.101
            port: 17001
            protocol: ssh
        credentials:
          default:
            password: ENC(w5PDosOUw5fDog==)
            username: admin
          enable:
            password: ENC(w5PDosOUw5fDosK-w4nDk8OHw4PDocOR)
        os: iosxe
        type: iosxe
      R2:
        connections:
          cli:
            ip: 172.25.192.102
            port: 17002
            protocol: ssh
        credentials:
          default:
            password: ENC(w5PDosOUw5fDog==)
            username: admin
          enable:
            password: ENC(w5PDosOUw5fDosK-w4nDk8OHw4PDocORw5PDl8Od)
        os: iosxr
        type: iosxr

Generate csv/excel template
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Too much work? You know can also generate a excel file template to fill in yourself:

Use the `--add-keys` option if you want to add more optional keys to your template.

.. code-block:: bash

    (venv)demo$ pyats create testbed template --output my_template.xlsx --add-keys alias type
    ... Template file generated: my_template.xlsx

Generate from Ansible inventory file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Having Ansible inventory file already and want to leverage it even with pyATS?
Yes! We offer the option to convert the Ansible inventory file to pyATS testbed yaml.

.. code-block:: bash

    (venv)demo$ pyats create testbed ansible --output testbed.yaml --inventory-name inventory.ini

.. tip::

    Add the `--encode-password` option to hide the password in the yaml as a secret string.
    However this is only for the purpose of obfuscation, the password is not cryptographically secure. Please refer to :pyats_secret_string:`Secret String <http>` for more detail.

Generate from Netbox
^^^^^^^^^^^^^^^^^^^^

You are managing network devices on Netbox and want to generate pyATS testbed yaml from the source of truth? Of course, you can! `pyats create testbed netbox` command can access to Netbox via REST API and retrieves device data and convert to testbed file.

.. code-block:: bash

    (venv)demo$ pyats create testbed netbox --output testbed.yaml --netbox-url=<netbox url> --user-token=<token>

.. tip::

    Add the `--encode-password` option to hide the password in the yaml as a secret string.
    However this is only for the purpose of obfuscation, the password is not cryptographically secure. Please refer to :pyats_secret_string:`Secret String <http>` for more detail.

Genie Create Parser
-------------------

This subcommand uses cookiecutter to generate a new Genie parser.
The generated folder contains a parser template and a parser unittest template

.. code-block:: text

    Usage:
      genie create parser [options]

    Description:
      create a Genie parser from cookiecutter template, located at:
          https://github.com/CiscoTestAutomation/genie-parser-template

    Parser Options:
      --parser_name PARSER_NAME
                            name of parser to be generated
      --os OS               Cisco OS for the parser

    General Options:
      -h, --help            Show help
      -v, --verbose         Give more output, additive up to 3 times.
      -q, --quiet           Give less output, additive up to 3 times, corresponding to WARNING, ERROR, and CRITICAL logging levels

By default, the command will prompt you for information it needs to generate
the parser from template. These prompts can be automated if you provide the
corresponding command line arguments.


Example
^^^^^^^

.. code-block:: text

    # Example
    # -------
    #
    #   creating a parser by entering everything through the prompts

    bash$ genie create parser
    Checking if cookiecutter is installed...
    Parser Name: my_parser
    Cisco OS for the parser [IOSXE/IOSXR/NXOS]: IOSXE
    Generating your project...

    # this will create a new folder with your provided parser name, containing
    # the template files

    bash $ tree my_parser/
    my_parser/
    ├── my_parser.py
    └── test_my_parser.py



genie create trigger
--------------------

Just like `genie create parser`, this subcommand uses cookiecutter to generate a new Genie trigger.
The generated folder contains a trigger template and a trigger datafile template

.. code-block:: text

    Usage:
      genie create trigger [options]

    Description:
      create a Genie trigger from cookiecutter template, located at:
          https://github.com/CiscoTestAutomation/genie-trigger-template

    Trigger Options:
      --trigger_name TRIGGER_NAME
                            name of trigger to be generated
      --action ACTION       action the trigger will perform
      --undo_action UNDO_ACTION
                            undo action the trigger will perform

    General Options:
      -h, --help            Show help
      -v, --verbose         Give more output, additive up to 3 times.
      -q, --quiet           Give less output, additive up to 3 times, corresponding to WARNING, ERROR, and CRITICAL logging levels

By default, the command will prompt you for information it needs to generate
the trigger from template. These prompts can be automated if you provide the
corresponding command line arguments.


Example
^^^^^^^

.. code-block:: text

    # Example
    # -------
    #
    #   creating a trigger by entering everything through the prompts

    bash$ pyats create trigger
    Checking if cookiecutter is installed...
    Trigger Name: my_trigger
    Action the trigger will perform (ex. Add): Shut
    Undo action the trigger will perform (ex. Remove): NoShut
    Generating your project...

    # this will create a new folder with your provided trigger name, containing
    # the template files

    bash $ tree my_trigger/
    my_trigger/
    ├── my_trigger.py
    └── my_trigger_datafile.yaml

