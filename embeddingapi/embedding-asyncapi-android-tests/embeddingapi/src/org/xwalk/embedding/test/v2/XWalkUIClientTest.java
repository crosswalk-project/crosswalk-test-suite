// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v2;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageFinishedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageStartedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnReceivedErrorHelper;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkUIClient.LoadStatus;
import org.xwalk.embedding.base.OnTitleUpdatedHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;
import android.view.KeyEvent;

@SuppressLint("NewApi")
public class XWalkUIClientTest extends XWalkViewTestBase {

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

    @SmallTest
    public void testOnReceivedTitleWithWriteContent() {
        try {
            String testUrl = "file:///android_asset/writeContent.html";
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int onReceivedTitleCallCount = mOnTitleUpdatedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnTitleUpdatedHelper.waitForCallback(onReceivedTitleCallCount);
            assertEquals("Test", mOnTitleUpdatedHelper.getTitle());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedTitleWithWithWriteIfrme() {
        try {
            String testUrl = "file:///android_asset/writeIfrme.html";
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int onReceivedTitleCallCount = mOnTitleUpdatedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnTitleUpdatedHelper.waitForCallback(onReceivedTitleCallCount);
            assertEquals("Test", mOnTitleUpdatedHelper.getTitle());
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
                    uiClient.onPageLoadStarted(mXWalkView, "file:///android_asset/p1bar.html");
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
    public void testOnPageLoadStartedWithLocalUrl() {
        try {
            String url = "file:///android_asset/index.html";
            OnPageStartedHelper mOnPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
            int currentCallCount = mOnPageStartedHelper.getCallCount();
            loadUrlAsync(url);
            mOnPageStartedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnPageStartedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnPageLoadStartedWithServer() {
        try {
            final String testHtml = "<html><head>Header</head><body>Body</body></html>";
            final String testPath = "/test.html";
            final String testUrl = mWebServer.setResponse(testPath, testHtml, null);
            OnPageStartedHelper mOnPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
            int currentCallCount = mOnPageStartedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnPageStartedHelper.waitForCallback(currentCallCount);
            assertEquals(testUrl, mOnPageStartedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageLoadStartedWithWriteContent() {
        try {
            String testUrl = "file:///android_asset/writeContent.html";
            OnPageStartedHelper mOnPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
            int currentCallCount = mOnPageStartedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnPageStartedHelper.waitForCallback(currentCallCount);
            assertEquals(testUrl, mOnPageStartedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnPageLoadStartedWithWithWriteIfrme() {
        try {
            String testUrl = "file:///android_asset/writeIfrme.html";
            OnPageStartedHelper mOnPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
            int currentCallCount = mOnPageStartedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnPageStartedHelper.waitForCallback(currentCallCount);
            assertEquals(testUrl, mOnPageStartedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnPageLoadStartedWithInvalidUrl() {
        try {
            String url = "http://this.url.is.invalid/";
            OnPageStartedHelper mOnPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
            int currentCallCount = mOnPageStartedHelper.getCallCount();
            loadUrlAsync(url);
            mOnPageStartedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnPageStartedHelper.getUrl());
        } catch (Exception e) {
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
                    uiClient.onPageLoadStopped(mXWalkView, "file:///android_asset/p1bar.html", LoadStatus.CANCELLED);
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
    public void testOnPageLoadStoppedWithLocalUrl() {
        try {
            String url = "file:///android_asset/index.html";
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            loadUrlAsync(url);
            mOnPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.FINISHED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnPageLoadStoppedWithWriteContent() {
        try {
            String url = "file:///android_asset/writeContent.html";
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            loadUrlAsync(url);
            mOnPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.FINISHED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnPageLoadStoppedWithWriteIfrme() {
        try {
            String url = "file:///android_asset/writeIfrme.html";
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            loadUrlAsync(url);
            mOnPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.FINISHED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnPageLoadStoppedWithServer() {
        try {
            final String testHtml = "<html><head>Header</head><body>Body</body></html>";
            final String testPath = "/test.html";
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            final String testUrl = mWebServer.setResponse(testPath, testHtml, null);
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(testUrl, mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.FINISHED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    public void testOnPageLoadStoppedWithData() {
        try {
            final String name = "index.html";
            String fileContent = getFileContent(name);
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            loadDataAsync(null, fileContent, "text/html", false);
            mOnPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals("about:blank", mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.FINISHED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    public void testOnPageLoadStoppedWithInvalidUrl() {
        try {
            String url = "http://localhost/non_existent";
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            OnReceivedErrorHelper mOnReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            int onReceivedErrorCallCount = mOnReceivedErrorHelper.getCallCount();
            assertEquals(0, mOnReceivedErrorHelper.getCallCount());
            loadUrlAsync(url);
    
            mOnReceivedErrorHelper.waitForCallback(onReceivedErrorCallCount,
                                                   1, WAIT_TIMEOUT_MS,
                                                   TimeUnit.MILLISECONDS);
            mOnPageFinishedHelper.waitForCallback(currentCallCount,
                                                  1, WAIT_TIMEOUT_MS,
                                                  TimeUnit.MILLISECONDS);
            assertEquals(1, mOnReceivedErrorHelper.getCallCount());
            assertEquals(url, mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.FAILED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    public void testOnPageLoadStoppedWithStopLoading() {
        try {
            final String testHtml = "<html><head>Header</head><body>Body</body></html>";
            final String testPath = "/test.html";
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            OnPageStartedHelper mOnPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
    
            final String testUrl = mWebServer.setResponse(testPath, testHtml, null);
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            int startedCount = mOnPageStartedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnPageStartedHelper.waitForCallback(startedCount);
            stopLoading();
            mOnPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(testUrl, mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.CANCELLED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
