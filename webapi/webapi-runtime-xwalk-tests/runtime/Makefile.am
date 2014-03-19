runtime_SCRIPTS = *
runtimedir = $(prefix)/opt/webapi-runtime-xwalk-tests/runtime
package_widgets_DATA = onLaunched.wgt onSuspend.wgt
package_widgetsdir = $(prefix)/opt/webapi-runtime-xwalk-tests/
EXTRA_DIST = $(runtime_SCRIPTS) $(package_widgets_DATA)

onLaunched.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

onSuspend.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .
