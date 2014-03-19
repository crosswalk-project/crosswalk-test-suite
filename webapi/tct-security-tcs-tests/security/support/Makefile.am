support_SCRIPTS = *
supportdir = $(prefix)/opt/tct-security-tcs-tests/security/support
package_widgets_DATA = sharedDirTestApp.wgt
package_widgetsdir = $(prefix)/opt/tct-security-tcs-tests/
EXTRA_DIST = $(support_SCRIPTS) $(package_widgets_DATA)

sharedDirTestApp.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

