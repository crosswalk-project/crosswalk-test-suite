// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;

import org.xwalk.embedding.base.OnFullscreenToggledHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class FullScreenTest extends XWalkViewTestBase {

    @SmallTest
    public void testHasEnteredFullScreen() {
        try {
            final String name = "fullscreen_enter_exit.html";
            String fileContent = getFileContent(name);
            loadDataSync(name, fileContent, "text/html", false);
            assertFalse(hasEnteredFullScreenOnUiThread());
            OnFullscreenToggledHelper mOnFullscreenToggledHelper = mTestHelperBridge.getOnFullscreenToggledHelper();
            int count = mOnFullscreenToggledHelper.getCallCount();
            assertFalse(hasEnteredFullScreenOnUiThread());
            clickOnElementId("enter_fullscreen",null);
            mOnFullscreenToggledHelper.waitForCallback(count);
            Thread.sleep(2000);
            assertTrue(hasEnteredFullScreenOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testLeaveFullScreen() {
        try {
            final String name = "fullscreen_enter_exit.html";
            String fileContent = getFileContent(name);
            loadDataSync(name, fileContent, "text/html", false);
            assertFalse(hasEnteredFullScreenOnUiThread());
            OnFullscreenToggledHelper mOnFullscreenToggledHelper = mTestHelperBridge.getOnFullscreenToggledHelper();
            int count = mOnFullscreenToggledHelper.getCallCount();
            clickOnElementId("enter_fullscreen",null);
            mOnFullscreenToggledHelper.waitForCallback(count);
            Thread.sleep(2000);
            assertTrue(hasEnteredFullScreenOnUiThread());
            count = mOnFullscreenToggledHelper.getCallCount();
            leaveFullscreenOnUiThread();
            mOnFullscreenToggledHelper.waitForCallback(count);
            Thread.sleep(2000);
            assertFalse(hasEnteredFullScreenOnUiThread());
            count = mOnFullscreenToggledHelper.getCallCount();
            clickOnElementId("enter_fullscreen",null);
            mOnFullscreenToggledHelper.waitForCallback(count);
            Thread.sleep(2000);
            count = mOnFullscreenToggledHelper.getCallCount();
            clickOnElementId("exit_fullscreen",null);
            mOnFullscreenToggledHelper.waitForCallback(count);
            Thread.sleep(2000);
            assertFalse(hasEnteredFullScreenOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
