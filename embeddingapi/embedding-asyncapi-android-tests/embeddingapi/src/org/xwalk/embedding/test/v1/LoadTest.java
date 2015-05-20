// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageFinishedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageStartedHelper;
import org.xwalk.core.XWalkNavigationHistory;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkUIClient.LoadStatus;
import org.xwalk.embedding.base.OnTitleUpdatedHelper;
import org.xwalk.embedding.base.TestXWalkResourceClientBase;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.os.SystemClock;
import android.test.suitebuilder.annotation.SmallTest;

public class LoadTest extends XWalkViewTestBase {

    @SmallTest
    public void testLoad_html_content()
    {
        try {
            String filename = "index.html";
            String expectedLocalTitle = "Crosswalk Sample Application";
            String content = getFileContent(filename);
            loadUrlSync(filename, content);
            assertEquals(expectedLocalTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoad_xhtml_content()
    {
        try {
            String filename = "index.xhtml";
            String expectedLocalTitle = "Crosswalk Sample Application";
            String content = getFileContent(filename);
            loadUrlSync(filename, content);
            assertEquals(expectedLocalTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoad_html_url()
    {
        try {
            String url = "file:///android_asset/index.html";
            loadUrlSync(url);
            String title = "Crosswalk Sample Application";
            assertEquals(title, getTitleOnUiThread());
            assertEquals(url, getUrlOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoad_xhtml_url() {
        try {
            String url = "file:///android_asset/index.xhtml";
            loadUrlSync(url);
            String title = "Crosswalk Sample Application";
            assertEquals(title, getTitleOnUiThread());
            assertEquals(url, getUrlOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoadAppFromManifest()
    {
        try {
            String title = "Crosswalk Sample Application";
            String path = "file:///android_asset/";
            String name = "manifest.json";
            String url = "file:///android_asset/index.html";
            loadFromManifestSync(path, name);
            assertEquals(url, getUrlOnUiThread());
            assertEquals(title, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testReload_ignoreCache() {
        try {
            String title1 = "title1";
            String title2 = "title2";
            String html1 = "<html><head><title>" + title1 + "</title></head></html><body></body>";
            String html2 = "<html><head><title>" + title2 + "</title></head></html><body></body>";
            String url = mWebServer.setResponse("/reload.html", html1, null);
            loadUrlSync(url);
            mWebServer.setResponse("/reload.html", html2, null);
            reloadSync(XWalkView.RELOAD_IGNORE_CACHE);
            Thread.sleep(1000);
            assertEquals(title2, getTitleOnUiThread());
        } catch (InterruptedException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testReload_normal() {
        try {
            String title1 = "title1";
            String title2 = "title2";
            String html1 = "<html><head><title>" + title1 + "</title></head></html><body></body>";
            String html2 = "<html><head><title>" + title2 + "</title></head></html><body></body>";
            String url = mWebServer.setResponse("/reload.html", html1, null);
            loadUrlSync(url);
            mWebServer.setResponse("/reload.html", html2, null);
            reloadSync(XWalkView.RELOAD_NORMAL);
            Thread.sleep(1000);
            assertEquals(title2, getTitleOnUiThread());
        } catch (InterruptedException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testStopLoading() throws Throwable {
        try {
        String url = "file:///android_asset/p1bar.html";
        loadUrlSync(url);
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mXWalkView.stopLoading();
                }
            });
            assertTrue(true);
       } catch (Exception e) {
           assertTrue(false);
           e.printStackTrace();
       }
    }

    @SmallTest
    public void testGetUrl() {
        try {
            String url = "file:///android_asset/p1bar.html";
            loadUrlSync(url);
            assertEquals(url, getUrlOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetOriginalUrl() {
        try {
            String originalUrl = "file:///android_asset/redirect_url.html";
            String url = "file:///android_asset/p1bar.html";
            loadUrlSync(originalUrl);
            Thread.sleep(500);
            assertEquals(originalUrl, getOriginalUrlOnUiThread());
            assertEquals(url, getUrlOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetTitle_fileName() {
        try {
            final String name = "p1bar.html";
            loadAssetFile(name);
            String title = getTitleOnUiThread();
            assertEquals("Test", title);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetTitle_url() {
        try {
            loadUrlSync("file:///android_asset/p1bar.html");
            String title = getTitleOnUiThread();
            assertEquals("Test", title);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetNavigationHistory() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkNavigationHistory xnh = mXWalkView.getNavigationHistory();
                    assertNotNull(xnh);
                }
            });
        } catch (Exception e) {
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoadJs()
    {
        try {
            final String changedTitle = "testLoadJs_ChangeTitle";
            String url = "file:///android_asset/p1bar.html";
            String code = "javascript:document.title='"+changedTitle+"';";
            loadJavaScriptSync(url, code);
            assertEquals(changedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoadXHR()
    {
        final String changedTitle = "testLoadXHR_ChangeTitle";
        try {
            String url = "file:///android_asset/testXHR.html";
            loadUrlSync(url);
            CallbackHelper getTitleHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int currentCallCount = getTitleHelper.getCallCount();
            clickOnElementId("AJAX_Read",null);
            getTitleHelper.waitForCallback(currentCallCount);
            assertEquals(changedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoadInnerJs()
    {
        final String changedTitle = "testLoadExternalJs_ChangeTitle";
        try {
            final String url = "file:///android_asset/innerJs.html";
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mXWalkView.setResourceClient(new TestXWalkResourceClientBase(mTestHelperBridge,mXWalkView) {
                        @Override
                        public void onLoadFinished(XWalkView view, String url) {
                            view.load("javascript:functionInTest()", null);
                            mTestHelperBridge.onLoadFinished(url);
                        }
                    });
                }
            });
            loadUrlSync(url);
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int currentCallCount = mOnTitleUpdatedHelper.getCallCount();
            mOnTitleUpdatedHelper.waitForCallback(currentCallCount);
            assertEquals(changedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testLoadExternalJs()
    {
        final String changedTitle = "testLoadExternalJs_ChangeTitle";
        try {
            final String url = "file:///android_asset/externalJs.html";
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    mXWalkView.setResourceClient(new TestXWalkResourceClientBase(mTestHelperBridge,mXWalkView) {
                        @Override
                        public void onLoadFinished(XWalkView view, String url) {
                            view.load("javascript:functionInTest()", null);
                            mTestHelperBridge.onLoadFinished(url);
                        }
                    });
                }
            });
            loadUrlSync(url);
            OnTitleUpdatedHelper mOnTitleUpdatedHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
            int currentCallCount = mOnTitleUpdatedHelper.getCallCount();
            mOnTitleUpdatedHelper.waitForCallback(currentCallCount);
            assertEquals(changedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testStopLoading_function() {
        try {
            String url = "file:///android_asset/p1bar.html";
            OnPageStartedHelper mOnPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
            OnPageFinishedHelper mOnPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            int currentCallCount = mOnPageFinishedHelper.getCallCount();
            int startedCount = mOnPageStartedHelper.getCallCount();
            loadUrlAsync(url);
            mOnPageStartedHelper.waitForCallback(startedCount);
            stopLoading();
            mOnPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnPageFinishedHelper.getUrl());
            assertEquals(LoadStatus.CANCELLED, mTestHelperBridge.getLoadStatus());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}

