// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;

import org.xwalk.core.XWalkResourceClient;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkResourceClientTest extends XWalkViewTestBase {


    public XWalkResourceClientTest() {
        super(MainActivity.class);
    }


    @SmallTest
    public void testOnLoadStarted() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(getXWalkView());
                    mXWalkView.setResourceClient(client);
                    client.onLoadStarted(mXWalkView, "http://www.baidu.com");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
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
            e.printStackTrace();
            assertTrue(false);
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
            e.printStackTrace();
            assertTrue(false);
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
            e.printStackTrace();
            assertTrue(false);
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
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testShouldOverrideUrlLoading() {
        try {
            loadUrlSync("about:blank");
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(mXWalkView);
                    assertFalse(client.shouldOverrideUrlLoading(mXWalkView,"about:blank"));
                }
            });

        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
