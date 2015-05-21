// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;


import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.TimeUnit;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.OnLoadFinishedHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.os.SystemClock;
import android.test.suitebuilder.annotation.SmallTest;
import android.util.Pair;
import android.view.KeyEvent;

@SuppressLint("NewApi")
public class XWalkViewTest extends XWalkViewTestBase {

    @SmallTest
    public void testAddJavascriptInterface() {
        try {
            final String name = "add_js_interface.html";
            addJavascriptInterface();
            loadAssetFile(name);
            assertEquals(mExpectedStr, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testAddJavascriptInterfaceWithUrl() {
        try {
            final String url = "file:///android_asset/add_js_interface.html";
            addJavascriptInterface();
            loadUrlSync(url);
            assertEquals(mExpectedStr, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testAddJavascriptInterfaceWithAnnotation() {
        try {
            final String name = "index.html";
            final String xwalkStr = "\"xwalk\"";
            String result;
            addJavascriptInterface();
            loadAssetFile(name);
            result = executeJavaScriptAndWaitForResult("testInterface.getText()");
            assertEquals(xwalkStr, result);
            raisesExceptionAndSetTitle("testInterface.getTextWithoutAnnotation()");
            String title = getTitleOnUiThread();
            assertEquals(mExpectedStr, title);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
        }
    }

    @SmallTest
    public void testEvaluateJavascript() {
        try {
            String changedTitle = "testEvaluateJavascript_ChangeTitle";
            String url = "file:///android_asset/p1bar.html";
            loadUrlSync(url,null);
            executeJavaScriptAndWaitForResult("document.title='"+changedTitle+"';");
            assertEquals(changedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testClearCache() {
        try {
            final String pagePath = "/clear_cache_test.html";
            List<Pair<String, String>> headers = new ArrayList<Pair<String, String>>();
            // Set Cache-Control headers to cache this request. One century should be long enough.
            headers.add(Pair.create("Cache-Control", "max-age=3153600000"));
            headers.add(Pair.create("Last-Modified", "Tues, 12 September 2014 00:00:00 GMT"));
            final String pageUrl = mWebServer.setResponse(
                    pagePath, "<html><body>foo</body></html>", headers);

            // First load to populate cache.
            clearCacheOnUiThread(true);
            loadUrlSync(pageUrl);
            assertEquals(1, mWebServer.getRequestCount(pagePath));

            // Load about:blank so next load is not treated as reload by XWalkView and force
            // revalidate with the server.
            loadUrlSync("about:blank");

            // No clearCache call, so should be loaded from cache.
            loadUrlSync(pageUrl);
            assertEquals(1, mWebServer.getRequestCount(pagePath));

            // Same as above.
            loadUrlSync("about:blank");

            // Clear cache, so should hit server again.
            clearCacheOnUiThread(true);
            loadUrlSync(pageUrl);
            assertEquals(2, mWebServer.getRequestCount(pagePath));

            // Same as above.
            loadUrlSync("about:blank");

            // Do not clear cache, so should be loaded from cache.
            clearCacheOnUiThread(false);
            loadUrlSync(pageUrl);
            assertEquals(2, mWebServer.getRequestCount(pagePath));
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
    public void testSaveState() {
        try {
            final Bundle state = new Bundle();
            state.putByteArray("XWALKVIEW_STATE", "valid state".getBytes());
            boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mXWalkView.saveState(state);
                }
            });
            assertTrue(result);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testSaveRestoreStateWithTitle() throws Throwable {
        setServerResponseAndLoad(1);
        saveAndRestoreStateOnUiThread();
        assertTrue(pollOnUiThread(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return TITLES[0].equals(mRestoreXWalkView.getTitle());
            }
        }));
    }

    @SmallTest
    public void testSaveRestoreStateWithHistoryItemList() {
        try {
            setServerResponseAndLoad(NUM_NAVIGATIONS);
            saveAndRestoreStateOnUiThread();
            checkHistoryItemList(mRestoreXWalkView);
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testRestoreState_trueResult() {
        try {
            final Bundle state = new Bundle();
            state.putByteArray("XWALKVIEW_STATE", "valid state".getBytes());
            loadUrlSync("file:///android_asset/p1bar.html/");
            boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    mXWalkView.saveState(state);
                    return mRestoreXWalkView.restoreState(state);
                }
            });
            assertTrue(result);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testRestoreState_falseResult() {
        try {
            final Bundle state = new Bundle();
            state.putByteArray("XWALKVIEW_STATE", "invalid state".getBytes());
            loadUrlSync("file:///android_asset/p1bar.html/");
            boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mRestoreXWalkView.restoreState(state);
                }
            });
            assertFalse(result);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
     }

    @SmallTest
    public void testRestoreState_notLoadFirst() {
        try {
            final Bundle state = new Bundle();
            state.putByteArray("XWALKVIEW_STATE", "valid state".getBytes());
            boolean result = runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    mXWalkView.saveState(state);
                    return mRestoreXWalkView.restoreState(state);
                }
            });
            assertFalse(result);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetAPIVersion() {
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
    public void testGetXWalkVersion() {
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

    boolean haveLoadflag = false;
    @SmallTest
    public void testSetResourceClient_function() {
        try {
            haveLoadflag = false;
            final String url = "file:///android_asset/index.html";
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mRestoreXWalkView.setResourceClient(new XWalkResourceClient(mXWalkView) {
                        @Override
                        public void onLoadFinished(XWalkView view, String url) {
                            haveLoadflag = true;
                            mTestHelperBridge.onLoadFinished(url);
                        }
                    });
                }
            });
            OnLoadFinishedHelper mOnLoadFinishedHelper = mTestHelperBridge.getOnLoadFinishedHelper();
            int currentCallCount = mOnLoadFinishedHelper.getCallCount();
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mRestoreXWalkView.load(url, null);
                }
            });
            mOnLoadFinishedHelper.waitForCallback(currentCallCount);
            assertTrue(haveLoadflag);
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
    public void testSetUIClient_function() {
        try {
            haveLoadflag = false;
            final String url = "file:///android_asset/index.html";
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mRestoreXWalkView.setUIClient(new XWalkUIClient(mXWalkView) {
                        @Override
                        public void onPageLoadStopped(XWalkView view,
                                String url, LoadStatus status) {
                            haveLoadflag = true;
                            mTestHelperBridge.onPageFinished(url, status);
                        }
                    });
                }
            });
            CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            int currentCallCount = pageFinishedHelper.getCallCount();
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mRestoreXWalkView.load(url, null);
                }
            });
            pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                    TimeUnit.SECONDS);
            assertTrue(haveLoadflag);
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

    //need to be improved
    @SmallTest
    public void testPauseTimers_function() {
        try {
            String url = "file:///android_asset/pause_timers.html";
            addJavascriptInterface();
            loadUrlSync(url);
            SystemClock.sleep(2000);
            String date = new Date().toString();
            pauseTimers();
            SystemClock.sleep(2000);
            assertEquals(date, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testResumeTimers_function() {
        try {
            String url = "file:///android_asset/pause_timers.html";
            addJavascriptInterface();
            loadUrlSync(url);
            SystemClock.sleep(2000);
            pauseTimers();
            SystemClock.sleep(2000);
            resumeTimers();
            SystemClock.sleep(1000);
            String date = new Date().toString();
            assertEquals(date, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnDestroy_function() {
        try {
            String url = "file:///android_asset/pause_timers.html";
            addJavascriptInterface();
            loadUrlSync(url);
            SystemClock.sleep(2000);
            onDestroy();
            SystemClock.sleep(2000);
            assertNull(getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

}
