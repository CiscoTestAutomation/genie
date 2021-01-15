Usage
=====
This page contains all the documentation needed to use *Blitz*.


Prerequisites
-------------
* sourced pyATS virtual environment
* testbed yaml
* blitz yaml

*Blitz* is integerated in pyATS Once you have both the testbed yaml and
blitz yaml then all you need is a job file to run your tests.

.. code-block:: bash

    # Quick start Guide!
    # ------------------
    # 1. Create the blitz yaml
    # 2. Have a testbed
    # 3. Enjoy!

    # Integrated with pyATS jobs
    pyats run job <path_to_job_file> 

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