// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import java.io.ByteArrayInputStream;

import org.chromium.base.test.util.TestFileUtil;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnReceivedErrorHelper;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.embedding.base.OnLoadFinishedHelper;
import org.xwalk.embedding.base.OnLoadStartedHelper;
import org.xwalk.embedding.base.OnProgressChangedHelper;
import org.xwalk.embedding.base.ShouldInterceptLoadRequestHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.test.suitebuilder.annotation.SmallTest;
import android.webkit.WebResourceResponse;

public class XWalkResourceClientTest extends XWalkViewTestBase {



    @SmallTest
    public void testOnLoadStarted() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(getXWalkView());
                    mXWalkView.setResourceClient(client);
                    client.onLoadStarted(mXWalkView, "file:///android_asset/index.html");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnLoadFinished() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkResourceClient client = new XWalkResourceClient(getXWalkView());
                    mXWalkView.setResourceClient(client);
                    client.onLoadFinished(mXWalkView, "http://www.baidu.com");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnProgressChanged() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(getXWalkView());
                    mXWalkView.setResourceClient(client);
                    client.onProgressChanged(mXWalkView, NUM_NAVIGATIONS);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testShouldInterceptLoadRequest() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkResourceClient client = new XWalkResourceClient(mXWalkView);
                    mXWalkView.setResourceClient(client);
                    client.shouldInterceptLoadRequest(mXWalkView, "http://www.baidu.com/");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedLoadError() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(mXWalkView);
                    mXWalkView.setResourceClient(client);
                    client.onReceivedLoadError(mXWalkView, NUM_NAVIGATIONS, null, "http://www.baidu.com/");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
