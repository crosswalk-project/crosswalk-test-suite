// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageFinishedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageStartedHelper;

public class TestHelperBridge {

	private String mChangedTitle;
    private final OnPageStartedHelper mOnPageStartedHelper;
    private final OnPageFinishedHelper mOnPageFinishedHelper;
    private final OnTitleUpdatedHelper mOnTitleUpdatedHelper;
    private final OnEvaluateJavaScriptResultHelper mOnEvaluateJavaScriptResultHelper;
    private final OnJavascriptCloseWindowHelper mOnJavascriptCloseWindowHelper;
    private final OnScaleChangedHelper mOnScaleChangedHelper;
    private final OnRequestFocusHelper mOnRequestFocusHelper;
    private final OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper;
    private final OnIconAvailableHelper mOnIconAvailableHelper;
    private final OnReceivedIconHelper mOnReceivedIconHelper;

    TestHelperBridge() {
        mOnPageStartedHelper = new OnPageStartedHelper();
        mOnPageFinishedHelper = new OnPageFinishedHelper();
        mOnTitleUpdatedHelper = new OnTitleUpdatedHelper();
        mOnEvaluateJavaScriptResultHelper = new OnEvaluateJavaScriptResultHelper();
        mOnJavascriptCloseWindowHelper = new OnJavascriptCloseWindowHelper();
        mOnScaleChangedHelper = new OnScaleChangedHelper();
        mOnRequestFocusHelper = new OnRequestFocusHelper();
        mOnCreateWindowRequestedHelper = new OnCreateWindowRequestedHelper();
        mOnIconAvailableHelper = new OnIconAvailableHelper();
        mOnReceivedIconHelper = new OnReceivedIconHelper();
    }

    public OnPageFinishedHelper getOnPageFinishedHelper() {
        return mOnPageFinishedHelper;
    }
    
    public void onPageStarted(String url) {
        mOnPageStartedHelper.notifyCalled(url);
    }

    public void onPageFinished(String url) {
        mOnPageFinishedHelper.notifyCalled(url);
    }

    public OnTitleUpdatedHelper getOnTitleUpdatedHelper() {
        return mOnTitleUpdatedHelper;
    }

    public OnEvaluateJavaScriptResultHelper getOnEvaluateJavaScriptResultHelper() {
        return mOnEvaluateJavaScriptResultHelper;
    }

   public void onTitleChanged(String title) {
        mChangedTitle = title;
        mOnTitleUpdatedHelper.notifyCalled(title);
    }
   
    public String getChangedTitle() {
        return mChangedTitle;
    }

    public OnJavascriptCloseWindowHelper getOnJavascriptCloseWindowHelper() {
        return mOnJavascriptCloseWindowHelper;
    }

    public void onJavascriptCloseWindow() {
        mOnJavascriptCloseWindowHelper.notifyCalled(true);
    }

    public OnScaleChangedHelper getOnScaleChangedHelper() {
        return mOnScaleChangedHelper;
    }

    public void onScaleChanged(float scale) {
        mOnScaleChangedHelper.notifyCalled(scale);
    }

    public OnRequestFocusHelper getOnRequestFocusHelper() {
        return mOnRequestFocusHelper;
    }

    public void onRequestFocus() {
        mOnRequestFocusHelper.notifyCalled(true);
    }

    public OnCreateWindowRequestedHelper getOnCreateWindowRequestedHelper() {
        return mOnCreateWindowRequestedHelper;
    }

    public void onCreateWindowRequested() {
        mOnCreateWindowRequestedHelper.notifyCalled(true);
    }

    public OnIconAvailableHelper getOnIconAvailableHelper() {
        return mOnIconAvailableHelper;
    }

    public void onIconAvailable() {
        mOnIconAvailableHelper.notifyCalled(true);
    }

    public OnReceivedIconHelper getOnReceivedIconHelper() {
        return mOnReceivedIconHelper;
    }

    public void onReceivedIcon() {
        mOnReceivedIconHelper.notifyCalled(true);
    }
}
