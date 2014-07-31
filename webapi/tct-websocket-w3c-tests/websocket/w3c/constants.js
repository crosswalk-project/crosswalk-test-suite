//FIXME: 
var DOMAIN_FOR_WS_TESTS = '127.0.0.1';
var DOMAIN_FOR_WSS_TESTS = '127.0.0.1';

var PORT = "8081";
var PORT_SSL = "8443";

// logic for using wss URLs instead of ws
var SCHEME_AND_DOMAIN;
var SCHEME_DOMAIN_PORT;
if (location.search == '?wss') {
  SCHEME_AND_DOMAIN = 'wss://'+DOMAIN_FOR_WSS_TESTS;
  SCHEME_DOMAIN_PORT = SCHEME_AND_DOMAIN + ":" + PORT_SSL;
} else {
  SCHEME_AND_DOMAIN = 'ws://'+DOMAIN_FOR_WS_TESTS;
  SCHEME_DOMAIN_PORT = SCHEME_AND_DOMAIN + ":" + PORT;
}
