// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v4;

import org.xwalk.core.XWalkPreferences;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkViewTest extends XWalkViewTestBase {

    @SmallTest
    public void testGetRemoteDebuggingUrl_enable() {
        try {
            String url = "file:///android_asset/index.html";
            loadUrlSync(url);
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
                }
            });
            String path = getRemoteDebuggingUrlOnUiThread();
            if(path != null && path.contains("devtools/page"))
            {
                assertTrue(true);
            } else {
                assertTrue(false);
            }
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetRemoteDebuggingUrl_disbale() {
        try {
            String url = "file:///android_asset/index.html";
            loadUrlSync(url);
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, false);
                }
            });
            String path = getRemoteDebuggingUrlOnUiThread();
            assertEquals("", path);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
