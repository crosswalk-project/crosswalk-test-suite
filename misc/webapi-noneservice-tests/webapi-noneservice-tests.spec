name="webapi-noneservice-tests"
version=$(grep main-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
sub_version=$(grep release-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
appname=$(echo $name|sed 's/-/_/g')

LIST=`find $(dirname $0)/../../../crosswalk-test-suite/webapi/ -maxdepth 1 -type d |awk '/-tests$/'`

BLACK="webapi-style-css3-tests
webapi-ambientlight-w3c-tests
webapi-imports-w3c-tests
webapi-deviceadaptation-css3-tests
webapi-htmltemplates-html5-tests
webapi-runtime-xwalk-tests
webapi-shadowdom-w3c-tests
webapi-taskscheduler-sysapps-tests
webapi-cssfilter-w3c-tests
webapi-locale-xwalk-tests
webapi-speechapi-xwalk-tests
webapi-vehicleinfo-xwalk-tests
webapi-nacl-xwalk-tests
webapi-audiosystem-xwalk-tests
webapi-sso-xwalk-tests
webapi-mediarenderer-xwalk-tests
webapi-nfc-w3c-tests
tct-batterystatus-w3c-tests
tct-capability-tests
tct-security-tcs-tests
tct-wgtapi01-w3c-tests
tct-wgtapi02-w3c-tests
tct-widget01-w3c-tests
tct-widget02-w3c-tests
tct-widgetpolicy-w3c-tests
tct-alarm-tizen-tests
tct-appcontrol-tizen-tests
tct-application-tizen-tests
tct-bluetooth-tizen-tests
tct-bookmark-tizen-tests
tct-calendar-tizen-tests
tct-callhistory-tizen-tests
tct-contact-tizen-tests
tct-content-tizen-tests
tct-datacontrol-tizen-tests
tct-datasync-tizen-tests
tct-download-tizen-tests
tct-messageport-tizen-tests
tct-messaging-email-tizen-tests
tct-messaging-mms-tizen-tests
tct-messaging-sms-tizen-tests
tct-namespace-tizen-tests
tct-networkbearerselection-tizen-tests
tct-nfc-tizen-tests
tct-notification-tizen-tests
tct-package-tizen-tests
tct-power-tizen-tests
tct-privilege-tizen-tests
tct-push-tizen-tests
tct-secureelement-tizen-tests
tct-systeminfo-tizen-tests
tct-systemsetting-tizen-tests
tct-time-tizen-tests
tct-tizen-tizen-tests
tct-websetting-tizen-tests
tct-getcapabilities
tct-testconfig"

for list in $LIST;do
    suite_name=`echo $list |awk -F "/" '{print $NF}'`
    grep \<testcase $list/tests.xml > /dev/null 2>&1
    if [ $? -eq 1 ];then
        LIST=`echo "$LIST" | sed "/$suite_name/d"`
    fi
done

for black in $BLACK;do
    LIST=`echo "$LIST" | sed "/$black/d"`
done
