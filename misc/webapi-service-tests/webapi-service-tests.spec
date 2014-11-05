name="webapi-service-tests"
version=$(grep main-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
sub_version=$(grep release-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
appname=$(echo $name|sed 's/-/_/g')

LIST="webapi-resourcetiming-w3c-tests
webapi-rawsockets-sysapps-tests
tct-xmlhttprequest-w3c-tests
tct-websocket-w3c-tests
tct-webmessaging-w3c-tests
tct-webgl-nonw3c-tests
tct-sessionhistory-html5-tests
tct-navigationtiming-w3c-tests
tct-csp-w3c-tests
tct-cors-w3c-tests"
