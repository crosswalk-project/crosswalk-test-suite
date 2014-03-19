/*
Copyright (c) 2013 Samsung Electronics Co., Ltd.

Licensed under the Apache License, Version 2.0 (the License);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors:

*/

var TIMEOUT_ASYNC_TEST = 90000;
setup({timeout: TIMEOUT_ASYNC_TEST});

var PHONE_NUMBER = 911;

var FILTER_TYPE_1 = new tizen.AttributeFilter("type", "EXACTLY", "TEL");
var FILTER_TYPE_2 = new tizen.AttributeFilter("type", "EXACTLY", "XMPP");
var FILTER_TYPE_3 = new tizen.AttributeFilter("type", "EXACTLY", "SIP");

var FILTER_FEATURES_1 = new tizen.AttributeFilter("features", "EXACTLY", "CALL");
var FILTER_FEATURES_2 = new tizen.AttributeFilter("features", "EXACTLY", "VOICECALL");
var FILTER_FEATURES_3 = new tizen.AttributeFilter("features", "EXACTLY", "VIDEOCALL");
var FILTER_FEATURES_4 = new tizen.AttributeFilter("features", "EXACTLY", "EMERGENCYCALL");

var FILTER_RP_1 = new tizen.AttributeFilter("remoteParties.remoteParty", "EXACTLY", PHONE_NUMBER);
var FILTER_RP_2 = new tizen.AttributeFilter("remoteParties.personId", "EXACTLY", "100");

var FILTER_START_TIME = new tizen.AttributeFilter("startTime", "EXACTLY", new Date(2012, 11, 15));

var FILTER_DIRECTION_1 = new tizen.AttributeFilter("direction", "EXACTLY", "MISSEDNEW");
var FILTER_DIRECTION_2 = new tizen.AttributeFilter("direction", "EXACTLY", "DIALED");
var FILTER_DIRECTION_3 = new tizen.AttributeFilter("direction", "EXACTLY", "RECEIVED");
var FILTER_DIRECTION_4 = new tizen.AttributeFilter("direction", "EXACTLY", "MISSED");
var FILTER_DIRECTION_5 = new tizen.AttributeFilter("direction", "EXACTLY", "BLOCKED");
var FILTER_DIRECTION_6 = new tizen.AttributeFilter("direction", "EXACTLY", "REJECTED");

var FILTER_RANGE_1 = new tizen.AttributeRangeFilter("duration", "2", "10");
var FILTER_RANGE_2 = new tizen.AttributeRangeFilter("startTime", new Date(2012, 11, 15), new Date(2012, 12, 15));
var FILTER_RANGE_3 = new tizen.AttributeRangeFilter("remoteParties.remoteParty", null, PHONE_NUMBER);

var FILTER_COMPOSITE_1 = new tizen.CompositeFilter("INTERSECTION", [FILTER_TYPE_1, FILTER_RANGE_1]);
var FILTER_COMPOSITE_2 = new tizen.CompositeFilter("UNION", [FILTER_DIRECTION_2, FILTER_RANGE_2]);

var ARRAY_FILTER = [FILTER_TYPE_1, FILTER_TYPE_2, FILTER_TYPE_3, FILTER_FEATURES_1, FILTER_FEATURES_2, FILTER_FEATURES_3, FILTER_FEATURES_4,
    FILTER_RP_1, FILTER_RP_2, FILTER_START_TIME, FILTER_DIRECTION_1, FILTER_DIRECTION_2, FILTER_DIRECTION_3, FILTER_DIRECTION_4,
    FILTER_DIRECTION_5, FILTER_DIRECTION_6];

var ARRAY_FILTER_RANGE = [FILTER_RANGE_1, FILTER_RANGE_2, FILTER_RANGE_3];

var ARRAY_FILTER_COMPOSITE = [FILTER_COMPOSITE_1, FILTER_COMPOSITE_2];

var SORT_MODE = new tizen.SortMode("startTime", "ASC");
var OFFSET = 2;
var LIMIT = 4;

var TYPE_MISMATCH_ERR = 'TypeMismatchError';
var INVALID_VALUES_ERR = 'InvalidValuesError';
var NOT_FOUND_ERR = 'NotFoundError';
var NOT_SUPPORTED_ERR = 'NotSupportedError';
var IO_ERR = 'IOError';
var UNKNOWN_ERR = 'UnknownError';
var SECURITY_ERR = 'SecurityError';

var CALL_HISTORY_ENTRY_TYPE = ["TEL", "XMPP", "SIP"];
var CALL_HISTORY_ENTRY_FEATURES = ["CALL", "VOICECALL", "VIDEOCALL", "EMERGENCYCALL"];
var CALL_HISTORY_ENTRY_DIRECTION = ["DIALED", "RECEIVED", "MISSEDNEW", "MISSED", "BLOCKED", "REJECTED"];
