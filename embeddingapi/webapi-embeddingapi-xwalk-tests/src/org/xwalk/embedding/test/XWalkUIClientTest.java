// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.net.Uri;
import android.test.suitebuilder.annotation.SmallTest;
import android.webkit.ValueCallback;

@SuppressLint("NewApi")
public class XWalkUIClientTest extends XWalkViewTestBase {

    public XWalkUIClientTest() {
        super(MainActivity.class);
    }


    @SmallTest
    public void testOnRequestFocus() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onRequestFocus(mXWalkView);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnJavascriptCloseWindow() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onJavascriptCloseWindow(mXWalkView);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnFullscreenToggled() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onFullscreenToggled(mXWalkView, true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOpenFileChooser() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    ValueCallback<Uri> uploadFile = new ValueCallback<Uri>() {

                        @Override
                        public void onReceiveValue(Uri arg0) {

                        }

                    };
                    uiClient.openFileChooser(mXWalkView, uploadFile, "", "hello");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnScaleChanged() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onScaleChanged(mXWalkView, WAIT_TIMEOUT_SECONDS, NUM_NAVIGATIONS);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageStartedExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageFinishedExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnReceivedAppNameExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnReceivedIconExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnJsAlertExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnJsConfirmExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnJsPromptExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testTOnJavascriptModalDialog() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);

                    XWalkJavascriptResult result = new XWalkJavascriptResult() {

                        @Override
                        public void confirmWithResult(String arg0) {

                        }

                        @Override
                        public void confirm() {

                        }

                        @Override
                        public void cancel() {

                        }
                    };

                    uiClient.onJavascriptModalDialog(mXWalkView, XWalkUIClient.JavascriptMessageType.JAVASCRIPT_ALERT, "http://www.baidu.com/", "11", "22", result);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }catch (Throwable t)
        {
            assertTrue(false);
        }

    }
}
