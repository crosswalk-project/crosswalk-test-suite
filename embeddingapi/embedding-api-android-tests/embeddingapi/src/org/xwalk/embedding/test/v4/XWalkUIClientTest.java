// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v4;

import org.xwalk.embedding.base.OnCreateWindowRequestedHelper;
import org.xwalk.embedding.base.OnIconAvailableHelper;
import org.xwalk.embedding.base.OnReceivedIconHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkUIClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testOnCreateWindowRequested_open_blank() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_open_blank",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnCreateWindowRequested_navigate_blank() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_a_blank",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnIconAvailable() {
        try {
            final String url = "file:///android_asset/window_icon.html";
            OnIconAvailableHelper mOnIconAvailableHelper = mTestHelperBridge.getOnIconAvailableHelper();
            int count = mOnIconAvailableHelper.getCallCount();
            loadUrlSync(url);
            mOnIconAvailableHelper.waitForCallback(count);
            assertTrue(mOnIconAvailableHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedIcon() {
        try {
            final String url = "file:///android_asset/window_icon.html";
            OnReceivedIconHelper mOnReceivedIconHelper = mTestHelperBridge.getOnReceivedIconHelper();
            int count = mOnReceivedIconHelper.getCallCount();
            loadUrlSync(url);
            mOnReceivedIconHelper.waitForCallback(count);
            assertTrue(mOnReceivedIconHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
