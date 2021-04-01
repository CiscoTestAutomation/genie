
Useful tips and tricks in Blitz
=================================

.. note::

    1- The name of the device that the action is being executed on will be saved automatically upon
    execution of the action and stay usable till the end of that action life-cycle. You can use that
    name as a variable using ``%VARIABLES{device.name}`` for various purposes in your action.

    2- Task id and transcript name also can be accessed by using ``%VARIABLES{task.id}``, ``%VARIABLES{transcript.name}``.

    3- The result of a section (whether it is passed, failed etc.) will be saved automatically into a variable
    same as the section name. You can use that name using ``%VARIABLES{<section_name>}``.

    4- Also in your YAML file, it is possible to have access the section's uid simply by using ``%VARIABLES{section.uid}``.

    5- Job file related values, such as job file path or job file name can be accessed by using ``%VARIABLES{runtime.job.file}``
    and ``%VARIABLES{runtime.job.name}``. Any other job file related value can be accessed in similar fashion
    ``%VARIABLES{runtime.job.<value>``

.. note::

    ```&&``` and ``and`` have different functionalities. ``&&`` is only useful to check if the result of an action is within a range of number
    ``and`` as well as ``or`` should be used to write conditional statements.
