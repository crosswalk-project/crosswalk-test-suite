// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import org.xwalk.embedding.base.OnXWalkInitFailedHelper;

public class TestHelperBridge {

    private final OnXWalkInitFailedHelper mOnXWalkInitFailedHelper;
    private final OnXWalkUpdateStartedHelper mOnXWalkUpdateStartedHelper;
    private final OnXWalkUpdateProgressHelper mOnXWalkUpdateProgressHelper;
    private final OnXWalkUpdateCompletedHelper mOnXWalkUpdateCompletedHelper;
    private final OnXWalkInitCompletedHelper mOnXWalkInitCompletedHelper;


    public TestHelperBridge() {
        mOnXWalkInitFailedHelper = new OnXWalkInitFailedHelper();
        mOnXWalkUpdateStartedHelper = new OnXWalkUpdateStartedHelper();
        mOnXWalkUpdateProgressHelper = new OnXWalkUpdateProgressHelper();
        mOnXWalkUpdateCompletedHelper = new OnXWalkUpdateCompletedHelper();
        mOnXWalkInitCompletedHelper = new OnXWalkInitCompletedHelper();
    }
    
    public OnXWalkInitFailedHelper getOnXWalkInitFailedHelper() {
        return mOnXWalkInitFailedHelper;
    }
    
    public boolean onXWalkInitFailed(String message) {
        mOnXWalkInitFailedHelper.notifyCalled(message);
        return true;
    }
   
    public OnXWalkUpdateStartedHelper getOnXWalkUpdateStartedHelper() {
        return mOnXWalkUpdateStartedHelper;
    }
    
    public boolean onXWalkUpdateStarted(String message) {
        mOnXWalkUpdateStartedHelper.notifyCalled(message);
        return true;
    }

    public OnXWalkUpdateProgressHelper getOnXWalkUpdateProgressHelper() {
        return mOnXWalkUpdateProgressHelper;
    }
    
    public boolean onXWalkUpdateProgress(String message, int progress) {
        mOnXWalkUpdateProgressHelper.notifyCalled(message, progress);
        return true;
    }
    
    public OnXWalkUpdateCompletedHelper getOnXWalkUpdateCompletedHelper() {
        return mOnXWalkUpdateCompletedHelper;
    }
    
    public boolean onXWalkUpdateCompleted(String message) {
        mOnXWalkUpdateCompletedHelper.notifyCalled(message);
        return true;
    }   
    
    public OnXWalkInitCompletedHelper getOnXWalkInitCompletedHelper() {
        return mOnXWalkInitCompletedHelper;
    }
    
    public boolean onXWalkInitCompleted(String message) {
        mOnXWalkInitCompletedHelper.notifyCalled(message);
        return true;
    }    
}
