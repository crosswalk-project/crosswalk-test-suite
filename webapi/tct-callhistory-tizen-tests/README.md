## Introduction

This test suite is for testing Tizen Callhistory API, which covers the following specifications:
* https://developer.tizen.org/help/topic/org.tizen.web.device.apireference/tizen/callhistory.html

## Pre-conditions

* 11 cases below need an existence call history:
    CallHistoryEntryArraySuccessCallback_onsuccess.html
    CallHistoryEntry.html
    CallHistory_find.html
    CallHistoryChangeCallback_onremoved.html
    CallHistory_remove.html
    CallHistory_remove_findBySortMode.html
    CallHistory_removeBatch.html
    CallHistory_removeBatch_with_errorCallback.html
    CallHistory_removeBatch_with_successCallback.html
    CallHistory_removeAll_with_successCallback.html

* 5 cases below need at least 3 existence call history:
    CallHistory_find_limit_2.html
    CallHistory_removeBatch_errorCallback_null.html
    CallHistory_removeBatch_errorCallback_undefined
    CallHistory_removeBatch_successCallback_null.html
    CallHistory_removeBatch_successCallback_undefined

* 2 cases below need a PHONE NUMBER ADDRESSING call history
    CallHistory_removeBatch_findByType.html
    CallHistoryEntry_type_TEL.html

* 1 case below need at least one MISSED call which was seen:
    CallHistoryEntry_direction_MISSED.html

* 3 cases below need at least one MISSED call which is not seen:
    CallHistoryEntry_direction_MISSEDNEW.html
    CallHistoryEntry_direction_attribute.html
    CallHistoryChangeCallback_onchanged.html

* 1 case below need make an VOICE ONLY CALL call:
    CallHistoryEntry_features_VOICECALL.html

* 1 case below need RECEIVED call:
    CallHistoryEntry_direction_RECEIVED.html

* 2 cases below need REJECTED call:
    CallHistoryEntry_direction_REJECTED.html
    CallHistory_removeBatch_findByDirection.html

* 1 case below need DIALED call:
    CallHistoryEntry_direction_DIALED.html

## Authors:

* Guan,JingX <jingx.guan@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
