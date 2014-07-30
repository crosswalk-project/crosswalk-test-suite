// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkJavascriptResultTest extends XWalkViewTestBase {

    public XWalkJavascriptResultTest() {
        super(MainActivity.class);
    }

    @SmallTest
    public void testConfirmWithResult() {
        try {
            final String url1 = "file:///android_asset/p1bar.html";
            final String url2 = "file:///android_asset/p2bar.html";

            getInstrumentation().runOnMainSync(new Runnable() {

                XWalkUIClient client = new XWalkUIClient(mXWalkView);
                XWalkJavascriptResult result = new XWalkJavascriptResult() {

                    @Override
                    public void confirmWithResult(String arg0) {

                    }
                    
                    @Override
                    public void confirm() {
                        mXWalkView.load(url2, null);
                    }
                    
                    @Override
                    public void cancel() {

                    }
                };

                @Override
                public void run() {
                    client.onJavascriptModalDialog(mXWalkView, XWalkUIClient.JavascriptMessageType.JAVASCRIPT_PROMPT, url1, "11", "22", result);

                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
     }


    @SmallTest
    public void testConfirm() {
        try {
            final String url1 = "file:///android_asset/p1bar.html";
            final String url2 = "file:///android_asset/p2bar.html";

            getInstrumentation().runOnMainSync(new Runnable() {

                XWalkUIClient client = new XWalkUIClient(mXWalkView);
                XWalkJavascriptResult result = new XWalkJavascriptResult() {

                    @Override
                    public void confirmWithResult(String arg0) {

                    }

                    @Override
                    public void confirm() {
                        mXWalkView.load(url2, null);
                    }
                    
                    @Override
                    public void cancel() {

                    }
                };

                @Override
                public void run() {
                    client.onJavascriptModalDialog(mXWalkView, XWalkUIClient.JavascriptMessageType.JAVASCRIPT_PROMPT, url1, "11", "22", result);
                    result.confirm();
                }
            });
            assertEquals(url2, getUrlOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testCancel() {
        try {
            final String url1 = "file:///android_asset/p1bar.html";
            final String url2 = "file:///android_asset/p2bar.html";

            getInstrumentation().runOnMainSync(new Runnable() {

                XWalkUIClient client = new XWalkUIClient(mXWalkView);
                XWalkJavascriptResult result = new XWalkJavascriptResult() {

                    @Override
                    public void confirmWithResult(String arg0) {

                    }

                    @Override
                    public void confirm() {

                    }

                    @Override
                    public void cancel() {
                        mXWalkView.load(url2, null);
                    }
                };

                @Override
                public void run() {
                    client.onJavascriptModalDialog(mXWalkView, XWalkUIClient.JavascriptMessageType.JAVASCRIPT_PROMPT, url1, "11", "22", result);
                    result.cancel();
                }
            });
            assertEquals(url2, getUrlOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
