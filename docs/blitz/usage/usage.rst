Usage
=====
Now that you have your Trigger Yaml file ready with your *Blitz* testcase(s), let's get it running. You need the following:

Prerequisites
-------------
* sourced pyATS virtual environment
* testbed yaml
* `trigger yaml <https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writetrigger/writetrigger.html#create-a-new-trigger-datafile>`_

*Blitz* is integerated in pyATS. Once you have both the testbed yaml and
blitz yaml then you can run your tests either using a job file or with executing a single cli command.

.. code-block:: bash

    # Quick start Guide!
    # ------------------
    # 1. Create the blitz yaml
    # 2. Have a testbed
    # 3. Enjoy!

    # Integrated with pyATS jobs
    pyats run job <path_to_job_file> 
    # Integerated using only a single command line
    pyats run genie --trigger-datafile <path_to_blitz_datafile> --trigger-uids 'test1' --testbed-file testbed.yaml

.. code-block:: python


  # Example of a Job file
  # ----------------------

  import os
  from genie.harness.main import gRun
  from pyats.datastructures.logic import And, Not, Or
  

  def main():
  
      gRun(
          trigger_datafile=<path_to_blitz_datafile>,
          trigger_uids = ['test1', 'test2'],  # name of the tests you wish to run
          testbed=<path_to_testbed>,
      )


Blitz Schema Validation
-----------------------
Under Construction