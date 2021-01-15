Defining the Cleaner Class
==========================

The `cleaners` section in the Clean YAML file is where the cleaner module and class is defined.

For pyATS Clean, the cleaner module is `genie.libs.clean` and the cleaner class is `PyatsDeviceClean`. Add the highlighted
text below into your `Clean YAML`.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 1-5

    cleaners:
        # This means to use the cleaner class `PyatsDeviceClean`
        PyatsDeviceClean:
            # The module is where the cleaner class above can be found
            module: genie.libs.clean