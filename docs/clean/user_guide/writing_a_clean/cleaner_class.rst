Adding the Cleaner Class
========================

pyATS must know where the python code for the clean exists. The `cleaners` section in the ``Clean YAML`` is where the
cleaner module and class is defined.

Cleaner Class for pyATS Clean
-----------------------------

For pyATS Clean, the cleaner module is `genie.libs.clean` and the cleaner class is `PyatsDeviceClean`. Add the highlighted
text below into your ``Clean YAML``.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 1-5

    cleaners:
        # This means to use the cleaner class `PyatsDeviceClean`
        PyatsDeviceClean:
            # The module is where the cleaner class above can be found
            module: genie.libs.clean

.. _clean_doc_combining_cleaners:

Combining a different clean with pyATS Clean
--------------------------------------------

The `cleaners` section in the ``Clean YAML`` supports multiple cleaners. For example, if pyATS Clean does not
support a platform that Uniclean does, you can use both of them at the same time.

.. note::

    Uniclean is end-of-life and end-of-support.

    Combining a different clean with pyATS Clean should only be used as a temporary work-around until pyATS Clean has
    support.

    Please :ref:`contact the development team <clean_doc_support>` and/or contribute following the
    :ref:`Developer Guide <clean_doc_developer_guide>` to fill these feature gaps.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 7-10

    cleaners:
        # This means to use the cleaner class `PyatsDeviceClean`
        PyatsDeviceClean:
            # The module is where the cleaner class above can be found
            module: genie.libs.clean

        # This is the uniclean cleaner class
        DeviceClean:
            # This is the uniclean module
            module: Uniclean.uniclean