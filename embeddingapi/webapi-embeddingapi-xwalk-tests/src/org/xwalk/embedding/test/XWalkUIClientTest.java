// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;

import java.util.concurrent.TimeoutException;

import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkUIClient.LoadStatus;
import org.xwalk.embedding.base.OnCreateWindowRequestedHelper;
import org.xwalk.embedding.base.OnIconAvailableHelper;
import org.xwalk.embedding.base.OnJavascriptCloseWindowHelper;
import org.xwalk.embedding.base.OnReceivedIconHelper;
import org.xwalk.embedding.base.OnRequestFocusHelper;
import org.xwalk.embedding.base.OnScaleChangedHelper;
import org.xwalk.embedding.base.OnTitleUpdatedHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.annotation.SuppressLint;
import android.net.Uri;
import android.test.suitebuilder.annotation.SmallTest;
import android.view.KeyEvent;
import android.webkit.ValueCallback;

@SuppressLint("NewApi")
public class XWalkUIClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testOnRequestFocus() {
        try {
            final String url = "file:///android_asset/request_focus_main.html";
            OnRequestFocusHelper mOnRequestFocusHelper = mTestHelperBridge.getOnRequestFocusHelper();
            int count = mOnRequestFocusHelper.getCallCount();
            loadUrlSync(url);
            clickOnElementId("left_frame", "LeftFrame");
            mOnRequestFocusHelper.waitForCallback(count);
            assertTrue(mOnRequestFocusHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnCreateWindowRequested_open_self() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_open_self",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnCreateWindowRequested_open_parent() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_open_parent",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnCreateWindowRequested_open_top() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_open_top",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnCreateWindowRequested_navigate_self() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_a_self",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnCreateWindowRequested_navigate_parent() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_a_parent",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnCreateWindowRequested_navigate_top() {
        try {
            final String url = "file:///android_asset/window_create_open.html";
            loadUrlSync(url);
            OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
            int count = mOnCreateWindowRequestedHelper.getCallCount();
            clickOnElementId("create_window_a_top",null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertTrue(mOnCreateWindowRequestedHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnIconAvailable() {
        try {
            final String url = "file:///android_asset/window_icon.html";
            OnIconAvailableHelper mOnIconAvailableHelper = mTestHelperBridge.getOnIconAvailableHelper();
            int count = mOnIconAvailableHelper.getCallCount();
            loadUrlSync(url);
            mOnIconAvailableHelper.waitForCallback(count);
            assertTrue(mOnIconAvailableHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedIcon() {
        try {
            final String url = "file:///android_asset/window_icon.html";
            OnReceivedIconHelper mOnReceivedIconHelper = mTestHelperBridge.getOnReceivedIconHelper();
            int count = mOnReceivedIconHelper.getCallCount();
            loadUrlSync(url);
            mOnReceivedIconHelper.waitForCallback(count);
            assertTrue(mOnReceivedIconHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnJavascriptCloseWindow() {
        try {
            final String url = "window.close.html";
            OnJavascriptCloseWindowHelper mCloseWindowHelper = mTestHelperBridge.getOnJavascriptCloseWindowHelper();
            int count = mCloseWindowHelper.getCallCount();
            loadAssetFile(url);
            mCloseWindowHelper.waitForCallback(count);
            assertTrue(mCloseWindowHelper.getCalled());
        } catch (InterruptedException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (TimeoutException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
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
            final String name = "scale_changed.html";
            String fileContent = getFileContent(name);
            OnScaleChangedHelper mOnScaleChangedHelper = mTestHelperBridge.getOnScaleChangedHelper();
            int count = mOnScaleChangedHelper.getCallCount();
            loadDataAsync(null, fileContent, "text/html", false);
            mOnScaleChangedHelper.waitForCallback(count);
            assertTrue(Float.compare(mOnScaleChangedHelper.getScale(), 0.0f) > 0);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnJavascriptModalDialog() {
        try {
            String EMPTY_PAGE = "<!doctype html>" +
                    "<title>Modal Dialog Test</title><p>Testcase.</p>";
            loadDataSync(null, EMPTY_PAGE, "text/html", false);
            executeJavaScriptAndWaitForResult("alert('" + ALERT_TEXT + "')");
            assertTrue(callbackCalled.get());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnReceivedTitle_WithUrl() {
        try {
            String path = "/test.html";
            String pageContent = CommonResources.makeHtmlPageFrom("<title>Test</title>",
                    "<div> The title is: Test </div>");
            String url = addPageToTestServer(mWebServer, path, pageContent);
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int onReceivedTitleCallCount = mOnTitleUpdatedHelper.getCallCount();
            loadUrlAsync(url);
            mOnTitleUpdatedHelper.waitForCallback(onReceivedTitleCallCount);
            assertEquals("Test", mOnTitleUpdatedHelper.getTitle());
        } catch (InterruptedException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (TimeoutException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnReceivedTitle_Callback() {
        try {
            String path = "/test.html";
            String pageContent = CommonResources.makeHtmlPageFrom("<title>Test</title>",
                    "<div> The title is: Test </div>");
            String url = addPageToTestServer(mWebServer, path, pageContent);
            loadUrlSync(url);
            loadUrlSync("file:///android_asset/index.html");
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int onReceivedTitleCallCount = mOnTitleUpdatedHelper.getCallCount();
            goBackSync(1);
            mOnTitleUpdatedHelper.waitForCallback(onReceivedTitleCallCount);
            assertEquals("Test",mOnTitleUpdatedHelper.getTitle());
        } catch (InterruptedException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (TimeoutException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedTitle_TitleChanged() {
        try {
            final String url1 = "file:///android_asset/p1bar.html";
            final String url2 = "file:///android_asset/index.html";
            loadUrlSync(url1);
            loadUrlSync(url2);
            goBackSync(1);
            assertEquals("Test", getTitleOnUiThread());
        }catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnReceivedTitle_WithData() {
        try {
            final String name = "index.html";
            final String fileContent = getFileContent(name);
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int onReceivedTitleCallCount = mOnTitleUpdatedHelper.getCallCount();
            loadDataSync(name, fileContent, "text/html", false);
            mOnTitleUpdatedHelper.waitForCallback(onReceivedTitleCallCount);
            assertNotNull(mOnTitleUpdatedHelper.getTitle());
        } catch (InterruptedException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (TimeoutException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
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
    public void testOnPageLoadStarted() {
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
            assertTrue(false);
            e.printStackTrace();
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
}
