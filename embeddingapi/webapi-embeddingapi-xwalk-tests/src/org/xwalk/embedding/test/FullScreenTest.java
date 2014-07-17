// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;

import org.xwalk.core.XWalkUIClient;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class FullScreenTest extends XWalkViewTestBase {


    public FullScreenTest() {
        super(MainActivity.class);
    }

    /**
     * fail
     */
    @SmallTest
    public void testHasEnteredFullScreen() {
        try {
            loadUrlSync("file:///android_asset/p1bar.html");
            assertEquals(true, hasEnteredFullScreenOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testHasEnteredFullScreen2() {
        try {
            XWalkUIClient client = new XWalkUIClient(mXWalkView);
            client.onFullscreenToggled(mXWalkView, true);
            loadUrlSync("file:///android_asset/p1bar.html");
            assertEquals(true, hasEnteredFullScreenOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testLeaveFullScreen() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mXWalkView.leaveFullscreen();
                }
            });
            assertEquals(false, hasEnteredFullScreenOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
