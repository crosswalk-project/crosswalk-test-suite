support_DATA = *.js
supportdir = $(prefix)/opt/tct-package-tizen-tests/package/support
package_manager_test_DATA = TCTPackageManagerTest1.1.1.wgt TCTPackageManagerTest2.2.2.wgt
package_manager_testdir = $(prefix)/opt/tct-package-tizen-tests/mediasrc
package_info_test_DATA = TCTPackageInfoTest.wgt
package_info_testdir = $(prefix)/opt/tct-package-tizen-tests/
EXTRA_DIST = $(support_DATA) $(package_manager_test_DATA) $(package_info_test_DATA)

TCTPackageManagerTest1.1.1.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

TCTPackageManagerTest2.2.2.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

TCTPackageInfoTest.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

