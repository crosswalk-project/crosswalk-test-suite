// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import org.chromium.base.test.util.Feature;
import org.xwalk.core.XWalkExtension;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkExtensionTest extends XWalkViewTestBase {

    public XWalkExtensionTest() {
        super(MainActivity.class);
    }


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
    public void testDestoryExtensionExist() {
        try {
            assertTrue(checkMethodInClass(XWalkExtension.class, "destoryExtension"));
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

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testOnMessage() throws Throwable {
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
                    xwalkExtension.onMessage(4, "Pass");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testOnSyncMessage() throws Throwable {
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
                    xwalkExtension.onSyncMessage(2, "Pass");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

}
