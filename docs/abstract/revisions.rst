Revisions
=========

Purpose
^^^^^^^

As CLI parsers and APIs continue to evolve, updates may introduce breaking
changes that result in errors within previously functional jobs. To address this
issue, we have implemented a revision system that allows us to update parsers
and APIs, without changing the existing implementations.

To use these revisions, we now generate a `<job_name>.abstract` YAML file each
time a pyATS job is run that can be loaded back into a job to ensure parity on
rerun. This file contains a comprehensive collection of all parsers, APIs, ops,
and other elements used throughout the job, allowing for seamless integration
of new parser/api/ops developments without disrupting existing job workflows.

Usage
^^^^^

When new jobs are initiated, the most recent revision of the relevant
parser/api/ops will be automatically identified and used. These functions are
then saved to a file, which can be conveniently loaded as needed for future use.

Saving
^^^^^^

At the completion of each job, abstract revisions are automatically saved to the
`<job_name>.abstract` file within the corresponding run info folder. This
file can be utilized during future runs to ensure that the same parser/api/ops
versions are utilized for consistency across all devices.

Loading
^^^^^^^

There are two options for loading the `<job_name>.abstract` file. Placing
the file in the same folder as the job file will automatically load it.
Alternatively, the `--abstract-revisions` argument can be used to indicate the
file path if it is stored elsewhere.

.. code-block:: sh

    pyats run job <job_file> --abstract-revisions <revisions-file>


Legacy
^^^^^^

New jobs will automatically leverage the most recent parser/api/ops revision,
which is typically suitable for most use cases. However, in certain situations,
reverting back to the initial parser/api/ops implementation may be necessary.
This can be achieved by passing in the `--abstract-legacy` argument.

.. code-block:: sh

    pyats run job <job_file> --abstract-legacy

The `<job_name>.abstract` can also specify that a job should always use the
earliest revision of any feature as long as it contains the line:

.. code-block:: text

    default_revision: earliest

For large collections of jobs, the `pyats migrate abstract`_ command has an
added option to generate `<job_name>.abstract` files with this line for every
discovered job

.. _pyats migrate abstract: https://pubhub.devnetcloud.com/media/pyats/docs/cli/pyats_migrate.html

Creating a Revision
^^^^^^^^^^^^^^^^^^^

To create a revision for a parser/api/ops, a new revision folder must be
established within the existing OS folder, following the naming convention
`rv<Revision Number>`.

.. code-block:: text

    genieparser/
    └── src/
        └── genie/
            └── libs/
                └── parser/
                    └── <OS>/
                        ├── rv1/
                        ├── rv2/
                        └── rv3/

Within the revision folder, two steps must be taken:

1) Create a new `__init__.py` file with the following contents:
    ```python
    from genie import abstract
    abstract.declare_token(revision='<Revision Number>')
    ```
   The `<revision number>` should match the number used in the folder name (for
   instance, `rv1` would use `'1'` as the revision number).

2) Create a new file with the same name as the file of the feature you are
   revising. For example, if the `"show platform"` command is to be revised,
   create a `show_platform.py` in the revision folder.

3) Once the new file has been created, open it and create the revised version
   of whatever feature you would like with **the exact function/class name**.
   IE, if you were to create a revision for the `show platform` parser, you
   would create a new class `ShowPlatform` and the accompanying schema.

As an example, assume the first revision is being created for the IOSXE version
of the `"show platform"` command, the resulting file structure would resemble:

.. code-block:: text

    genieparser/
    └── src/
        └── genie/
            └── libs/
                └── parser/
                    └── iosxe/
                        └── rv1/
                            ├── __init__.py
                            └── show_platform.py

Any changes made in `iosxe/rv1/show_platform.py` will then be used instead of
the original `iosxe/show_platform.py` file.