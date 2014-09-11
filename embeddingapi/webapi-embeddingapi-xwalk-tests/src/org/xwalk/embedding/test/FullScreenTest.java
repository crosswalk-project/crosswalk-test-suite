// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;

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
            clickOnElementId("enter_fullscreen",null);
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
            clickOnElementId("enter_fullscreen",null);
            assertTrue(hasEnteredFullScreenOnUiThread());
            leaveFullscreenOnUiThread();
            assertFalse(hasEnteredFullScreenOnUiThread());
            clickOnElementId("enter_fullscreen",null);
            clickOnElementId("exit_fullscreen",null);
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
