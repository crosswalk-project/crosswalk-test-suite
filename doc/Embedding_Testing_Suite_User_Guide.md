# EmbeddingAPI Test Suite User Guide

Version 1.0, for Android 4.X

Copyright © 2014 Intel Corporation. All rights reserved. No portions of this document may be reproduced without the written permission of Intel Corporation.

Intel is a trademark of Intel Corporation in the U.S. and/or other countries.

Linux is a registered trademark of Linus Torvalds.

Tizen® is a registered trademark of The Linux Foundation.

ARM is a registered trademark of ARM Holdings Plc.

\*Other names and brands may be claimed as the property of others.

Any software source code reprinted in this document is furnished under a software license and may only be used or copied in accordance with the terms of that license.


## Introduction

This document provides the method to run EmbeddingAPI Test Suite on Android Platform.

## Preconditions

- Setup Ubuntu (12.04 64bit) Host for the Test Environments
- Ensure that you haveset up your host environment for Android compilation .
- Install testkit-lite on Host

## Run EmbeddingAPI test cases

EmbeddingAPI Test Suite is released as a ZIP file. Use this step to install it on the target device:

- Unzip the package on the test machine by running the following command:

$unzip -o webapi-embedding-xwalk-tests-<version\>.zip

- set up an Android device to the host with USB interface. 
- Install the package on the test machine by running the following command:

$cd opt

$cd webapi-embeddingapi-xwalk-tests

$./inst.sh –i

- Uninstall the package on the test machine:

If the console shows 'Failure [INSTALL\_FAILED\_ALREADY\_EXISTS]' when you install it, You need to uninstall it first. You can either uninstall it manually on the android device, or use the following command:

$./inst.sh –u

- Run test cases by running the following command on host:

$cp test.xml $My_Dir

$testkit-lite –f $My\_Dir/tests.xml --comm androidmobile -A -o "$My\_Dir/tests.result.xml"

## Appendix 1 Execution Result On The Console

The result will show on the console. You can copy it to a document and view the summary information. According to the summary information as follows, we can get more detailed information from the files in 
/opt/testkit/lite/2014-10-17-10:50:14.910225/.

    [ analysis test xml file: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.xml ]
    
    [ testing xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1.xml by <set> ]
    [ this might take some time, please wait ]
    [ total set number is: 10 ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_1.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_1.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_2.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_2.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_3.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_3.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_4.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_4.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_5.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_5.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_6.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_6.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_7.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_7.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_8.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_8.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_9.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_9.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_10.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/ww42_tests.auto.suite_1_set_10.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    
    [ test complete at time: 2014-10-17_10_50_20 ]
    [ start merging test result xml files, this might take some time, please wait ]
    [ merge result files into /opt/testkit/lite/2014-10-17-10:50:14.910225/tests.result.xml ]
    [ test summary ]
      [ total case number: 0 ]
    [Warning: found 0 case from the result files, if it's not right, please check the test xml files, or the filter values ]
    [ generate result xml: /opt/testkit/lite/2014-10-17-10:50:14.910225/tests.result.xml ]
    [ merge complete, write to the result file, this might take some time, please wait ]
    [ copy result xml to output file: /home/archermind/result.xml ]
    [ all tasks for testkit lite are accomplished, goodbye ]
    archermind@rdjdz110017:~/zyy/work/ww42/crosswalk-test-suite/embeddingapi/webapi-embeddingapi-xwalk-tests/opt/webapi-embeddingapi-xwalk-tests$ testkit-lite -f ~/zyy/work/ww42/tests.xml --comm androidmobile -k "androidunit" -A -o "/home/archermind/result.xml"
    [ analysis test xml file: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.xml ]
    
    [ testing xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1.xml by <set> ]
    [ this might take some time, please wait ]
    [ total set number is: 10 ]
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_1.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_1.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.LoadTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testGetNavigationHistory...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetOriginalUrl...(FAIL)
    [message]
    execute case: webapi-embeddingapi-xwalk-tests # testGetTitle_fileName...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetTitle_url...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetUrl...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testLoadAppFromManifest...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testLoadJs...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testLoadUrl...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testLoadXHR...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testReload_ignoreCache...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testReload_normal...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testStopLoading...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_2.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_2.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.NavigationHistoryTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testCanGoBack...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testCanGoForward...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testClear...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetCurrentIndex...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetCurrentItem_noBack...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetCurrentItem_withBack...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetItemAt...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testHasItemAt...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testNavigate_backOneStep...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testNavigate_backTwoStep...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testNavigate_forwardOneStep...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testNavigate_forwardTwoStep...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSize...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_3.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_3.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.XWalkNavigationItemTest ]
    execute case: webapi-embeddingapi-xwalk-tests # test_navigationItem_getOriginalUrl...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # test_navigationItem_getTitle...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # test_navigationItem_getUrl...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_4.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_4.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.XWalkViewTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testAddJavascriptInterface...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testAddJavascriptInterfaceWithAnnotation...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testClearCache...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testEvaluateJavascript...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetAPIVersion...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetXWalkVersion...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnActivityResult...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnDestroy...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnHide...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnKeyDown...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnKeyUp...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnNewIntent...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnShow...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testPauseTimers...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testRestoreState_falseResult...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testRestoreState_notLoadFirst...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testRestoreState_trueResult...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testResumeTimers...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSaveState...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSaveState_loadUrl...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSetResourceClient...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSetUIClient...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_5.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_5.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.XWalkUIClientTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testOnFullscreenToggled...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnJavascriptCloseWindow...(FAIL)
    [message]
    execute case: webapi-embeddingapi-xwalk-tests # testOnJavascriptModalDialog...(FAIL)
    [message]
    execute case: webapi-embeddingapi-xwalk-tests # testOnPageLoadStarted...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnPageStarted_nullUrl...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnPageStopped...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnPageStopped_nullUrl...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnReceivedTitle_Callback...(FAIL)
    [message]
    execute case: webapi-embeddingapi-xwalk-tests # testOnReceivedTitle_TitleChanged...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnReceivedTitle_WithData...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnReceivedTitle_WithUrl...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnRequestFocus...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnScaleChanged...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnUnhandledKeyEvent...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOpenFileChooser...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testShouldOverrideKeyEvent...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_6.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_6.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.XWalkResourceClientTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testOnLoadFinished...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnLoadStarted...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnProgressChanged...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnReceivedLoadError...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testShouldInterceptLoadRequest...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testShouldOverrideUrlLoading...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_7.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_7.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.XWalkPreferenceTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testGetBooleanValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetBooleanValue_false_REMOTE_DEBUGGING...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetBooleanValue_true_REMOTE_DEBUGGING...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetIntegerValue_int_SUPPORT_MULTIPLE_WINDOWS...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testGetStringValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSetValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSetValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSetValue_false_REMOTE_DEBUGGING...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSetValue_int_SUPPORT_MULTIPLE_WINDOWS...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testSetValue_true_REMOTE_DEBUGGING...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_8.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_8.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.XWalkJavascriptResultTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testCancel...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testConfirm...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testConfirmWithResult...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_9.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_9.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.FullScreenTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testHasEnteredFullScreen...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testLeaveFullScreen...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ run set: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_10.xml ]
    [ split xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/ww42_tests.auto.suite_1_set_10.xml by <case> ]
    [ this might take some time, please wait ]
    [ preparing for startup options ]
    [ android unit test, entry: org.xwalk.embedding.test.XWalkExtensionTest ]
    execute case: webapi-embeddingapi-xwalk-tests # testBroadcastMessage...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testBroadcastMessage_nullString...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnMessage...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnSyncMessage...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testOnSyncMessage_MultiFrames...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testPostMessage...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testPostMessage_nullString...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testXWalkExtension...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testXWalkExtension_StringArray...(PASS)
    execute case: webapi-embeddingapi-xwalk-tests # testXWalkExtension_emptyArray...(PASS)
    [ cases result saved to resultfile ]
    
    
    [ test complete at time: 2014-10-17_10_52_57 ]
    [ start merging test result xml files, this might take some time, please wait ]
    [ merge result files into /opt/testkit/lite/2014-10-17-10:51:29.223649/tests.result.xml ]
    [ test summary ]
      [ total case number: 97 ]
      [ pass rate: 95.88% ]
      [ PASS case number: 93 ]
      [ FAIL case number: 4 ]
      [ BLOCK case number: 0 ]
      [ N/A case number: 0 ]
    [ generate result xml: /opt/testkit/lite/2014-10-17-10:51:29.223649/tests.result.xml ]
    [ merge complete, write to the result file, this might take some time, please wait ]
    [ copy result xml to output file: /home/archermind/result.xml ]
    [ all tasks for testkit lite are accomplished, goodbye ]



## Appendix 2 Result Details In The 'tests.result.xml'

    <?xml version="1.0" encoding="UTF-8"?>
            <?xml-stylesheet type="text/xsl" href="testresult.xsl"?>
    <test_definition><environment build_id="" device_id="MedfieldF4FE9D99" device_model="" device_name="N/A" host="Linux-3.8.0-29-generic-i686-with-Ubuntu-12.04-precise" lite_version="3.1.9" manufacturer="" resolution="N/A" screen_size="N/A"><other /></environment>
    <summary test_plan_name="Empty test_plan_name"><start_at>2014-10-17_10_51_29</start_at><end_at>2014-10-17_10_52_57</end_at></summary>
      <suite category="Android embedding APIs" name="webapi-embeddingapi-xwalk-tests">
        <set name="LoadTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.LoadTest"><testcase id="testGetNavigationHistory" purpose="testGetNavigationHistory" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:37</start><end>2014-10-17 10:51:37</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetOriginalUrl" purpose="testGetOriginalUrl" result="FAIL"><result_info><actual_result>FAIL</actual_result><start>2014-10-17 10:51:38</start><end>2014-10-17 10:51:38</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetTitle_fileName" purpose="testGetTitle_fileName" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:38</start><end>2014-10-17 10:51:38</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetTitle_url" purpose="testGetTitle_url" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:38</start><end>2014-10-17 10:51:38</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetUrl" purpose="testGetUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:39</start><end>2014-10-17 10:51:39</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testLoadAppFromManifest" purpose="testLoadAppFromManifest" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:39</start><end>2014-10-17 10:51:39</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testLoadJs" purpose="testLoadJs" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:39</start><end>2014-10-17 10:51:39</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testLoadUrl" purpose="testLoadUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:39</start><end>2014-10-17 10:51:39</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testLoadXHR" purpose="testLoadXHR" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:40</start><end>2014-10-17 10:51:40</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testReload_ignoreCache" purpose="testReload_ignoreCache" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:41</start><end>2014-10-17 10:51:41</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testReload_normal" purpose="testReload_normal" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:43</start><end>2014-10-17 10:51:43</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testStopLoading" purpose="testStopLoading" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:43</start><end>2014-10-17 10:51:43</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="NavigationHistoryTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.NavigationHistoryTest"><testcase id="testCanGoBack" purpose="testCanGoBack" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:46</start><end>2014-10-17 10:51:46</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testCanGoForward" purpose="testCanGoForward" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:46</start><end>2014-10-17 10:51:46</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testClear" purpose="testClear" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:46</start><end>2014-10-17 10:51:46</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetCurrentIndex" purpose="testGetCurrentIndex" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:47</start><end>2014-10-17 10:51:47</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetCurrentItem_noBack" purpose="testGetCurrentItem_noBack" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:47</start><end>2014-10-17 10:51:47</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetCurrentItem_withBack" purpose="testGetCurrentItem_withBack" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:47</start><end>2014-10-17 10:51:47</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetItemAt" purpose="testGetItemAt" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:47</start><end>2014-10-17 10:51:47</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testHasItemAt" purpose="testHasItemAt" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:48</start><end>2014-10-17 10:51:48</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testNavigate_backOneStep" purpose="testNavigate_backOneStep" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:48</start><end>2014-10-17 10:51:48</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testNavigate_backTwoStep" purpose="testNavigate_backTwoStep" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:48</start><end>2014-10-17 10:51:48</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testNavigate_forwardOneStep" purpose="testNavigate_forwardOneStep" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:49</start><end>2014-10-17 10:51:49</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testNavigate_forwardTwoStep" purpose="testNavigate_forwardTwoStep" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:49</start><end>2014-10-17 10:51:49</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSize" purpose="testSize" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:49</start><end>2014-10-17 10:51:49</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="XWalkNavigationItemTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.XWalkNavigationItemTest"><testcase id="test_navigationItem_getOriginalUrl" purpose="test_navigationItem_getOriginalUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:52</start><end>2014-10-17 10:51:52</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="test_navigationItem_getTitle" purpose="test_navigationItem_getTitle" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:52</start><end>2014-10-17 10:51:52</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="test_navigationItem_getUrl" purpose="test_navigationItem_getUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:53</start><end>2014-10-17 10:51:53</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="XWalkViewTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.XWalkViewTest"><testcase id="testAddJavascriptInterface" purpose="testAddJavascriptInterface" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:55</start><end>2014-10-17 10:51:55</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testAddJavascriptInterfaceWithAnnotation" purpose="testAddJavascriptInterfaceWithAnnotation" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:56</start><end>2014-10-17 10:51:56</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testClearCache" purpose="testClearCache" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:56</start><end>2014-10-17 10:51:56</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testEvaluateJavascript" purpose="testEvaluateJavascript" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:57</start><end>2014-10-17 10:51:57</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetAPIVersion" purpose="testGetAPIVersion" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:57</start><end>2014-10-17 10:51:57</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetXWalkVersion" purpose="testGetXWalkVersion" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:57</start><end>2014-10-17 10:51:57</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnActivityResult" purpose="testOnActivityResult" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:57</start><end>2014-10-17 10:51:57</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnDestroy" purpose="testOnDestroy" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:58</start><end>2014-10-17 10:51:58</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnHide" purpose="testOnHide" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:58</start><end>2014-10-17 10:51:58</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnKeyDown" purpose="testOnKeyDown" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:58</start><end>2014-10-17 10:51:58</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnKeyUp" purpose="testOnKeyUp" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:58</start><end>2014-10-17 10:51:58</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnNewIntent" purpose="testOnNewIntent" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:58</start><end>2014-10-17 10:51:58</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnShow" purpose="testOnShow" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:59</start><end>2014-10-17 10:51:59</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testPauseTimers" purpose="testPauseTimers" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:59</start><end>2014-10-17 10:51:59</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testRestoreState_falseResult" purpose="testRestoreState_falseResult" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:51:59</start><end>2014-10-17 10:51:59</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testRestoreState_notLoadFirst" purpose="testRestoreState_notLoadFirst" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:00</start><end>2014-10-17 10:52:00</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testRestoreState_trueResult" purpose="testRestoreState_trueResult" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:00</start><end>2014-10-17 10:52:00</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testResumeTimers" purpose="testResumeTimers" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:00</start><end>2014-10-17 10:52:00</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSaveState" purpose="testSaveState" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:00</start><end>2014-10-17 10:52:00</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSaveState_loadUrl" purpose="testSaveState_loadUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:01</start><end>2014-10-17 10:52:01</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSetResourceClient" purpose="testSetResourceClient" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:01</start><end>2014-10-17 10:52:01</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSetUIClient" purpose="testSetUIClient" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:01</start><end>2014-10-17 10:52:01</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="XWalkUIClientTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.XWalkUIClientTest"><testcase id="testOnFullscreenToggled" purpose="testOnFullscreenToggled" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:04</start><end>2014-10-17 10:52:04</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnJavascriptCloseWindow" purpose="testOnJavascriptCloseWindow" result="FAIL"><result_info><actual_result>FAIL</actual_result><start>2014-10-17 10:52:09</start><end>2014-10-17 10:52:09</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnJavascriptModalDialog" purpose="testOnJavascriptModalDialog" result="FAIL"><result_info><actual_result>FAIL</actual_result><start>2014-10-17 10:52:25</start><end>2014-10-17 10:52:25</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnPageLoadStarted" purpose="testOnPageLoadStarted" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:25</start><end>2014-10-17 10:52:25</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnPageStarted_nullUrl" purpose="testOnPageStarted_nullUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:25</start><end>2014-10-17 10:52:25</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnPageStopped" purpose="testOnPageStopped" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:25</start><end>2014-10-17 10:52:25</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnPageStopped_nullUrl" purpose="testOnPageStopped_nullUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:26</start><end>2014-10-17 10:52:26</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnReceivedTitle_Callback" purpose="testOnReceivedTitle_Callback" result="FAIL"><result_info><actual_result>FAIL</actual_result><start>2014-10-17 10:52:31</start><end>2014-10-17 10:52:31</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnReceivedTitle_TitleChanged" purpose="testOnReceivedTitle_TitleChanged" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:31</start><end>2014-10-17 10:52:31</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnReceivedTitle_WithData" purpose="testOnReceivedTitle_WithData" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:32</start><end>2014-10-17 10:52:32</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnReceivedTitle_WithUrl" purpose="testOnReceivedTitle_WithUrl" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:32</start><end>2014-10-17 10:52:32</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnRequestFocus" purpose="testOnRequestFocus" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:32</start><end>2014-10-17 10:52:32</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnScaleChanged" purpose="testOnScaleChanged" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:33</start><end>2014-10-17 10:52:33</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnUnhandledKeyEvent" purpose="testOnUnhandledKeyEvent" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:33</start><end>2014-10-17 10:52:33</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOpenFileChooser" purpose="testOpenFileChooser" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:33</start><end>2014-10-17 10:52:33</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testShouldOverrideKeyEvent" purpose="testShouldOverrideKeyEvent" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:33</start><end>2014-10-17 10:52:33</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="XWalkResourceClientTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.XWalkResourceClientTest"><testcase id="testOnLoadFinished" purpose="testOnLoadFinished" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:36</start><end>2014-10-17 10:52:36</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnLoadStarted" purpose="testOnLoadStarted" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:37</start><end>2014-10-17 10:52:37</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnProgressChanged" purpose="testOnProgressChanged" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:37</start><end>2014-10-17 10:52:37</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnReceivedLoadError" purpose="testOnReceivedLoadError" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:37</start><end>2014-10-17 10:52:37</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testShouldInterceptLoadRequest" purpose="testShouldInterceptLoadRequest" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:37</start><end>2014-10-17 10:52:37</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testShouldOverrideUrlLoading" purpose="testShouldOverrideUrlLoading" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:38</start><end>2014-10-17 10:52:38</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="XWalkPreferenceTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.XWalkPreferenceTest"><testcase id="testGetBooleanValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW" purpose="testGetBooleanValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:41</start><end>2014-10-17 10:52:41</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetBooleanValue_false_REMOTE_DEBUGGING" purpose="testGetBooleanValue_false_REMOTE_DEBUGGING" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:41</start><end>2014-10-17 10:52:41</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetBooleanValue_true_REMOTE_DEBUGGING" purpose="testGetBooleanValue_true_REMOTE_DEBUGGING" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:41</start><end>2014-10-17 10:52:41</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetIntegerValue_int_SUPPORT_MULTIPLE_WINDOWS" purpose="testGetIntegerValue_int_SUPPORT_MULTIPLE_WINDOWS" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:41</start><end>2014-10-17 10:52:41</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testGetStringValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE" purpose="testGetStringValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:42</start><end>2014-10-17 10:52:42</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSetValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE" purpose="testSetValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:42</start><end>2014-10-17 10:52:42</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSetValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW" purpose="testSetValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:42</start><end>2014-10-17 10:52:42</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSetValue_false_REMOTE_DEBUGGING" purpose="testSetValue_false_REMOTE_DEBUGGING" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:42</start><end>2014-10-17 10:52:42</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSetValue_int_SUPPORT_MULTIPLE_WINDOWS" purpose="testSetValue_int_SUPPORT_MULTIPLE_WINDOWS" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:43</start><end>2014-10-17 10:52:43</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testSetValue_true_REMOTE_DEBUGGING" purpose="testSetValue_true_REMOTE_DEBUGGING" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:43</start><end>2014-10-17 10:52:43</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="XWalkJavascriptResultTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.XWalkJavascriptResultTest"><testcase id="testCancel" purpose="testCancel" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:46</start><end>2014-10-17 10:52:46</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testConfirm" purpose="testConfirm" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:46</start><end>2014-10-17 10:52:46</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testConfirmWithResult" purpose="testConfirmWithResult" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:47</start><end>2014-10-17 10:52:47</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="FullScreenTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.FullScreenTest"><testcase id="testHasEnteredFullScreen" purpose="testHasEnteredFullScreen" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:50</start><end>2014-10-17 10:52:50</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testLeaveFullScreen" purpose="testLeaveFullScreen" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:50</start><end>2014-10-17 10:52:50</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
        <set name="XWalkExtensionTest" set_debug_msg="result.dlog" test_set_src="org.xwalk.embedding.test.XWalkExtensionTest"><testcase id="testBroadcastMessage" purpose="testBroadcastMessage" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:54</start><end>2014-10-17 10:52:54</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testBroadcastMessage_nullString" purpose="testBroadcastMessage_nullString" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:54</start><end>2014-10-17 10:52:54</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnMessage" purpose="testOnMessage" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:55</start><end>2014-10-17 10:52:55</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnSyncMessage" purpose="testOnSyncMessage" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:55</start><end>2014-10-17 10:52:55</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testOnSyncMessage_MultiFrames" purpose="testOnSyncMessage_MultiFrames" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:55</start><end>2014-10-17 10:52:55</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testPostMessage" purpose="testPostMessage" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:56</start><end>2014-10-17 10:52:56</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testPostMessage_nullString" purpose="testPostMessage_nullString" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:56</start><end>2014-10-17 10:52:56</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testXWalkExtension" purpose="testXWalkExtension" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:56</start><end>2014-10-17 10:52:56</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testXWalkExtension_StringArray" purpose="testXWalkExtension_StringArray" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:56</start><end>2014-10-17 10:52:56</end><stdout>[message]</stdout><stderr /></result_info></testcase><testcase id="testXWalkExtension_emptyArray" purpose="testXWalkExtension_emptyArray" result="PASS"><result_info><actual_result>PASS</actual_result><start>2014-10-17 10:52:57</start><end>2014-10-17 10:52:57</end><stdout>[message]</stdout><stderr /></result_info></testcase></set>
      </suite>
    </test_definition>
