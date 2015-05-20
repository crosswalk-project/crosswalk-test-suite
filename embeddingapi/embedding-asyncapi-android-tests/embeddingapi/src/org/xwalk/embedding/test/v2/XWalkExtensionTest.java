// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v2;


import java.util.concurrent.TimeUnit;

import org.chromium.base.test.util.Feature;
import org.xwalk.core.XWalkExtension;
import org.xwalk.embedding.base.ExtensionEcho;
import org.xwalk.embedding.base.ExtensionEcho_broadcast;
import org.xwalk.embedding.base.OnTitleUpdatedHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkExtensionTest extends XWalkViewTestBase {

    @SmallTest
    public void testXWalkExtension() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkExtension xWalkExtension = new XWalkExtension("xwalkExtension", "xwalkExtension") {

                        @Override
                        public String onSyncMessage(int arg0, String arg1) {
                            return null;
                        }

                        @Override
                        public void onMessage(int arg0, String arg1) {

                        }
                    };
                    assertTrue(true);
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testXWalkExtension_StringArray() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkExtension xwalkExtension = new XWalkExtension("xwalkExtension", "xwalkExtension", new String[]{"111","222"}) {
                        @Override
                        public void onMessage(int arg0, String arg1) {

                        }

                        @Override
                        public String onSyncMessage(int arg0, String arg1) {

                            return null;
                        }
                    };
                    assertTrue(true);
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testXWalkExtension_emptyArray() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkExtension xwalkExtension = new XWalkExtension("xwalkExtension", "xwalkExtension", new String[]{}) {

                        @Override
                        public void onMessage(int arg0, String arg1) {

                        }

                        @Override
                        public String onSyncMessage(int arg0, String arg1) {
                            return null;
                        }
                    };
                    assertTrue(true);
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testPostMessage() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkExtension xWalkExtension = new XWalkExtension("xwalkExtension", "xwalkExtension") {

                        @Override
                        public void onMessage(int arg0, String arg1) {

                        }

                        @Override
                        public String onSyncMessage(int arg0, String arg1) {

                            return null;
                        }
                    };
                    xWalkExtension.postMessage(0, "test");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testPostMessage_nullString() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkExtension xwalkExtension = new XWalkExtension("xwalkExtension", "xwalkExtension") {

                        @Override
                        public void onMessage(int arg0, String arg1) {

                        }

                        @Override
                        public String onSyncMessage(int arg0, String arg1) {

                            return null;
                        }
                    };
                    xwalkExtension.postMessage(1, null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    public void testPostMessage_function() {
        try {
            ExtensionEcho echo = new ExtensionEcho();
            loadAssetFileAndWaitForTitle("echo.html");
            assertEquals(PASS_STRING, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testBroadcastMessage() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkExtension xwalkExtension = new XWalkExtension("xwalkExtension", "xwalkExtension") {
                        @Override
                        public void onMessage(int arg0, String arg1) {

                        }

                        @Override
                        public String onSyncMessage(int arg0, String arg1) {

                            return null;
                        }
                    };
                    xwalkExtension.broadcastMessage("Message");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testBroadcastMessage_nullString() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkExtension xwalkExtension= new XWalkExtension("xwalkExtension", "xwalkExtension") {

                        @Override
                        public void onMessage(int arg0, String arg1) {

                        }

                        @Override
                        public String onSyncMessage(int arg0, String arg1) {

                            return null;
                        }
                    };
                    xwalkExtension.broadcastMessage(null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    public void testBroadcastMessage_function() {
        try {
            ExtensionEcho_broadcast echo = new ExtensionEcho_broadcast();
            loadAssetFileAndWaitForTitle("echo.html");
            assertEquals(PASS_STRING, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testOnMessage() {
        try {
            ExtensionEcho echo = new ExtensionEcho();
            loadAssetFileAndWaitForTitle("echo.html");
            assertEquals(PASS_STRING, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testOnSyncMessage() {
    	try {
    	    ExtensionEcho echo = new ExtensionEcho();
            loadAssetFile("echoSync.html");
            assertEquals(PASS_STRING, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testOnSyncMessage_MultiFrames() {
        try {
            ExtensionEcho echo = new ExtensionEcho();
            String fileName = "framesEcho.html";
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int currentCallCount = mOnTitleUpdatedHelper.getCallCount();
            String fileContent = getFileContent(fileName);
            loadDataAsync(fileName, fileContent, "text/html", false);
            mOnTitleUpdatedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                    TimeUnit.SECONDS);
            assertEquals(PASS_STRING, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}

