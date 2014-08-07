// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;

import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkUIClient.LoadStatus;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.net.Uri;
import android.test.suitebuilder.annotation.SmallTest;
import android.view.KeyEvent;
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
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onPageStarted"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageFinishedExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onPageFinished"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnReceivedAppNameExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onReceivedAppName"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnReceivedIconExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onReceivedIcon"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnJsAlertExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onJsAlert"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnJsConfirmExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onJsConfirm"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnJsPromptExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onJsPrompt"));
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


    @SmallTest
    public void testGetDefaultVideoPosterExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "getDefaultVideoPoster"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetVideoLoadingProgressViewExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "getVideoLoadingProgressView"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnCreateWindowExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onCreateWindow"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnReceivedTitle() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onReceivedTitle(mXWalkView, "title");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnReceivedTouchIconUrlExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onReceivedTouchIconUrl"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testShouldOverrideKeyEvent() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.shouldOverrideKeyEvent(mXWalkView, new KeyEvent(0, 65));
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnUnhandledKeyEvent() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onUnhandledKeyEvent(mXWalkView, new KeyEvent(0,65));
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageStarted() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onPageLoadStarted(mXWalkView, "file:///android_asset/p2bar.html");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageStarted_nullUrl() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onPageLoadStarted(mXWalkView, null);
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
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.shouldOverrideKeyEvent(mXWalkView, new KeyEvent(0, 65));
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnCreateWindowRequestExist() {
        try {
            assertTrue(checkMethodInClass(XWalkUIClient.class, "onCreateWindowRequest"));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }


    @SmallTest
    public void testOnPageStopped() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onPageLoadStopped(mXWalkView, "file:///android_asset/p2bar.html", LoadStatus.CANCELLED);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageStopped_nullUrl() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onPageLoadStopped(mXWalkView, null, LoadStatus.CANCELLED);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageStopped_nullView() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onPageLoadStopped(null, null, LoadStatus.CANCELLED);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
