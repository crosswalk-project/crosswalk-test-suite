// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import java.util.concurrent.Callable;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.test.suitebuilder.annotation.SmallTest;
import android.view.KeyEvent;
import android.webkit.ValueCallback;

@SuppressLint("NewApi")
public class XWalkViewTest extends XWalkViewTestBase {


    public XWalkViewTest() {
        super(MainActivity.class);
    }

    @SmallTest
    public void testAddJavascriptInterface() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    mXWalkView.addJavascriptInterface(new TestJavascriptInterface(), "testInterface");

                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testEvaluateJavascript() {
        try {
            final String name = "p1bar.html";
            final String code = "document.title=\"xwalk\"";
            loadAssetFile(name);
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.evaluateJavascript(code, new ValueCallback<String>() {

                        @Override
                        public void onReceiveValue(String arg0) {

                        }
                    });
                }
            });
            assertTrue(true);
       } catch (Exception e) {
           e.printStackTrace();
           assertTrue(false);
       }
    }
    
    @SmallTest
    public void testClearCache() throws Throwable {

        try {
            String url = "file:///android_asset/p1bar.html/";
            loadUrlSync(url);
            clearCacheOnUiThread(false);
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testClearCache2() throws Throwable {

        try {
            String url = "file:///android_asset/p1bar.html";
            loadUrlSync(url);
            clearCacheOnUiThread(true);
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testPauseTimers() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.pauseTimers();
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testResumeTimers() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    mXWalkView.pauseTimers();
                    mXWalkView.resumeTimers();
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnHide() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.onHide();
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnShow() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.onShow();
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnDestroy() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.onDestroy();
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnActivityResult() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.onActivityResult(WAIT_TIMEOUT_SECONDS, NUM_NAVIGATIONS, null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnNewIntent() {
        try {
            getInstrumentation().runOnMainSync(new Runnable()  {

                @Override
                public void run()  {
                    Intent intent = new Intent();
                    intent.setClassName("org.xwalk.embedding", MainActivity.class.getName());
                    mXWalkView.onNewIntent(intent);

                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSaveState() throws Throwable {
        final Bundle state = new Bundle();
        state.putByteArray("XWALKVIEW_STATE", "valid state".getBytes());
        boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return mXWalkView.saveState(state);
            }
        });
        assertTrue(result);
    }

    @SmallTest
    public void testSaveState2() throws Throwable {
        setServerResponseAndLoad(NUM_NAVIGATIONS);
        saveAndRestoreStateOnUiThread();
        checkHistoryItemList();
    }

    @SmallTest
    public void testRestoreStateTrue() throws Throwable {
        try {
            final Bundle state = new Bundle();
            state.putByteArray("XWALKVIEW_STATE", "valid state".getBytes());
            loadUrlSync("file:///android_asset/p1bar.html/");
            boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    mXWalkView.saveState(state);
                    return mXWalkView.restoreState(state);
                }
            });
            assertTrue(result);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testRestoreStateFalse() throws Throwable {
        try {
            final Bundle state = new Bundle();
            state.putByteArray("XWALKVIEW_STATE", "valid state".getBytes());
            loadUrlSync("file:///android_asset/p1bar.html/");
            boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mXWalkView.restoreState(state);
                }
            });
            assertFalse(result);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
     }

    @SmallTest
    public void testRestoreStateFalse2() throws Throwable {
        try {
            final Bundle state = new Bundle();
            state.putByteArray("XWALKVIEW_STATE", "valid state".getBytes());
            boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    mXWalkView.saveState(state);
                    return mXWalkView.restoreState(state);
                }
            });
            assertFalse(result);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetAPIVersion() throws Throwable {
        try {
            String version = getAPIVersionOnUiThread();
            Pattern pattern = Pattern.compile("^[0-9]+(.[0-9]+)$");
            Matcher matcher = pattern.matcher(version);
            assertTrue("The API version is invalid.", matcher.find());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
     }

    @SmallTest
    public void testGetXWalkVersion() throws Throwable {
        try {
            String version = getXWalkVersionOnUiThread();
            Pattern pattern = Pattern.compile("\\d+\\.\\d+\\.\\d+\\.\\d+");
            Matcher matcher = pattern.matcher(version);
            assertTrue("The Crosswalk version is invalid.", matcher.find());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testSetResourceClient() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.setResourceClient(new XWalkResourceClient(mXWalkView));
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetUIClient() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    mXWalkView.setUIClient(new XWalkUIClient(mXWalkView));
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnKeyUp() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    mXWalkView.onKeyUp(0, null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnKeyDown() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.onKeyDown(65, new KeyEvent(0, 65));

                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
