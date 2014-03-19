support_DATA = *.js
supportdir = $(prefix)/opt/tct-application-tizen-tests/application/support
application_widgets_DATA = TCTAppControl.wgt TCTAppControlMock.wgt
application_widgetsdir = $(prefix)/opt/tct-application-tizen-tests/
package_widgets_DATA = TCTAppInfoEventTest1.wgt TCTAppInfoEventTest2.wgt
package_widgetsdir = $(prefix)/opt/tct-application-tizen-tests/mediasrc

EXTRA_DIST = $(support_DATA) $(application_widgets_DATA) $(package_widgets_DATA)

TCTAppInfoEventTest1.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

TCTAppInfoEventTest2.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

TCTAppControl.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .

TCTAppControlMock.wgt:
	cd $(basename $@); zip -rq ../$(notdir $@) .
