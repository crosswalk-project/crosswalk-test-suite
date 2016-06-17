// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.asynctest.v6;

import org.xwalk.embedding.base.OnJsAlertHelper;
import org.xwalk.embedding.base.OnJsConfirmHelper;
import org.xwalk.embedding.base.OnJsPromptHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkUIClientTestAsync extends XWalkViewTestBase {

    @SmallTest
    public void testOnJsAlert() {
        OnJsAlertHelper mOnJsAlertHelper = mTestHelperBridge.getOnJsAlertHelper();
        try {
            final String url = "file:///android_asset/js_modal_dialog.html";
            loadUrlSync(url);
            int count = mOnJsAlertHelper.getCallCount();
            clickOnElementId("js_alert", null);
            mOnJsAlertHelper.waitForCallback(count);
            assertEquals(1, mOnJsAlertHelper.getCallCount());
            assertEquals("alert", mOnJsAlertHelper.getMessage());
        } catch (Exception e) {
            // TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnJsConfirm() {
        OnJsConfirmHelper mOnJsConfirmHelper = mTestHelperBridge.getOnJsConfirmHelper();
        try {
            final String url = "file:///android_asset/js_modal_dialog.html";
            loadUrlSync(url);
            int count = mOnJsConfirmHelper.getCallCount();
            clickOnElementId("js_confirm", null);
            mOnJsConfirmHelper.waitForCallback(count);
            assertEquals(1, mOnJsConfirmHelper.getCallCount());
            assertEquals("confirm", mOnJsConfirmHelper.getMessage());
        } catch (Exception e) {
            // TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnJsPrompt() {
        OnJsPromptHelper mOnJsPromptHelper = mTestHelperBridge.getOnJsPromptHelper();
        try {
            final String url = "file:///android_asset/js_modal_dialog.html";
            loadUrlSync(url);
            int count = mOnJsPromptHelper.getCallCount();
            clickOnElementId("js_prompt", null);
            mOnJsPromptHelper.waitForCallback(count);
            assertEquals(1, mOnJsPromptHelper.getCallCount());
            assertEquals("prompt", mOnJsPromptHelper.getMessage());
        } catch (Exception e) {
            // TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
        }
    }
}