name="webapi-service-tests"
version=$(grep main-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
sub_version=$(grep release-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
appname=$(echo $name|sed 's/-/_/g')

LIST="tct-canvas-html5-tests
tct-cors-w3c-tests
tct-csp-w3c-tests
tct-manual-w3c-tests
tct-navigationtiming-w3c-tests
tct-sessionhistory-html5-tests
tct-testconfig
tct-webgl-nonw3c-tests
tct-webmessaging-w3c-tests
tct-websocket-w3c-tests
tct-xmlhttprequest-w3c-tests
webapi-nacl-xwalk-tests
webapi-rawsockets-sysapps-tests
webapi-resourcetiming-w3c-tests"
