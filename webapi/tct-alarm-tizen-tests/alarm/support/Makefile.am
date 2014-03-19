support_SCRIPTS = *
supportdir = $(prefix)/opt/tct-alarm-tizen-tests/alarm/support
package_widgets_DATA = UnitTest-AlarmTest1.wgt
package_widgetsdir = $(prefix)/opt/tct-alarm-tizen-tests/
EXTRA_DIST = $(support_DATA) $(package_widgets_DATA)

UnitTest-AlarmTest1.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .