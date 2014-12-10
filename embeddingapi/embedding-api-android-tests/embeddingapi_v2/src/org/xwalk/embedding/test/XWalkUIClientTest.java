// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;

import java.util.concurrent.TimeoutException;

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
}
