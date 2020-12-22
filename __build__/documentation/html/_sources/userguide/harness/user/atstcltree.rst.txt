.. _atstcltree:

Installing Cisco ATS TCL Tree
=============================


1. Follow the steps listed on this :atsinstall:`wiki page <http>` for installing
a Cisco ATS TCL tree from scratch.

.. note::
	* Follow steps for "TAR Ball Installation Steps"
	* Under Tarball, follow steps for "Standalone Installation"


2. Follow the steps listed on this :atsc3:`wiki page <http>` for upgrading your
newly installed Cisco ATS TCL tree to the C3 patch.

.. note::
	* Follow steps for "Tar Ball Tree Upgrade Process"


3. Create symbolic links for the following:

.. code-block:: bash

	cd $AUTOTEST
	ln -s install/atsc.csh atsc.csh
	ln -s install/atsc.sh atsc.sh
	ln -s install/env.csh env.csh
	ln -s install/env.sh env.sh


4. Get xBU-shared libraries:

.. code-block:: bash

	cd $AUTOTEST/lib
	cvs -d /auto/autons/CVSROOT co xBU-shared/pkgIndex.tcl
	cvs -d /auto/autons/CVSROOT co xBU-shared/caas-libs
	cvs -d /auto/autons/CVSROOT co xBU-shared/caas-pkgs
	cvs -d /auto/autons/CVSROOT co xBU-shared/ats-shared
	cvs -d /auto/autons/CVSROOT co xBU-shared/libs
	cd xBU-shared
	git clone asg-git-best@asg-git-host:/git/psat-ng.git


5. Get cisco-shared libraries:

.. code-block:: bash

	cd $AUTOTEST
	cvs -d /auto/autons/CVSROOT co cisco-shared/


6. Get ena-tests libraries:

.. code-block:: bash

	cd $AUTOTEST
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_db_lib.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_lib.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_cfg.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_tgn.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_triggers.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_verifications.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_verifications_cfg.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/psat/psat_xml_lib.tcl
	cvs -d /auto/autons/CVSROOT co  ena-tests/lib
	cvs -d /auto/autons/CVSROOT co  ena-tests/hfr-mpls/lib
	cvs -d /auto/autons/CVSROOT co  ena-tests/multicast/mrib
	cvs -d /auto/autons/CVSROOT co  ena-tests/multicast/lib
	cvs -d /auto/autons/CVSROOT co  ena-tests/template
	cvs -d /auto/autons/CVSROOT co  ena-tests/tools/instaGTO
	cvs -d /auto/autons/CVSROOT co  ena-tests/tools/mem-leak
	cvs -d /auto/autons/CVSROOT co  ena-tests/tools/mem-profile.lib
	cvs -d /auto/autons/CVSROOT co  ena-tests/tools/mem-profiler
	cvs -d /auto/autons/CVSROOT co  ena-tests/tools/TgnSsnLbl


7. Get ngxr-tests libraries:

.. code-block:: bash

	cd $AUTOTEST
	cvs -d /auto/autons/CVSROOT co  ngxr-tests/lib
	cd $AUTOTEST/ats_easy
	ln -s ../ngxr-tests ngxr-tests


8. Get regression libraries:

.. code-block:: bash

	cd $AUTOTEST
	cvs -d /auto/autons/CVSROOT co regression/lib/mid_range_routing/mrrUtils
	cvs -d /auto/autons/CVSROOT co regression/lib/contrib
	cd $AUTOTEST/local/lib
	ln -s ../../regression/lib/contrib/ contrib


9. Get contrib libraries:

.. code-block:: bash

	cd $AUTOTEST
	cvs -d /auto/autons/CVSROOT co  contrib/pkgIndex.tcl
	cvs -d /auto/autons/CVSROOT co  contrib/tbmap
	cvs -d /auto/autons/CVSROOT co  contrib/common


10. Get DC3 libraries:

.. code-block:: bash

	cd $AUTOTEST
	cvs -d /auto/autons/CVSROOT co  dc3/lib
	cd $AUTOTEST/lib
	ln -s ../dc3/lib dc3_utils
 
	# Go to the pkgIndex file
	cd $AUTOTEST/dc3/lib/
	vim pkgIndex.tcl

	# Edit the pkgIndex of dc3_utils to remove/comment out the following lines:
	# package ifneeded AgtClient 1.1 [list source [file join $dir agilent AgilentN2X AgtClient.tcl]]
	# package ifneeded AgtCommon 0.1 [list source [file join $dir agilent AgilentN2X AgtCommon.tcl]]
	# package ifneeded AgtScriptControl 1.0 [list source [file join $dir agilent AgilentN2X AgtScriptControl.tcl]]
	# package ifneeded AtoTest 0.1 [list source [file join $dir agilent AgilentN2X AtoTest.tcl]]
	# package ifneeded AgtTsu 15.14 [list source [file join $dir agilent AgtTsu AgtTsuLib.tcl]]

