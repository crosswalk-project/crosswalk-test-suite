// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;


import java.io.ByteArrayInputStream;

import org.chromium.base.test.util.TestFileUtil;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnReceivedErrorHelper;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.embedding.base.OnLoadFinishedHelper;
import org.xwalk.embedding.base.OnLoadStartedHelper;
import org.xwalk.embedding.base.OnProgressChangedHelper;
import org.xwalk.embedding.base.ShouldInterceptLoadRequestHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.os.SystemClock;
import android.test.suitebuilder.annotation.SmallTest;
import android.webkit.WebResourceResponse;

public class XWalkResourceClientTest extends XWalkViewTestBase {



    @SmallTest
    public void testOnLoadStarted() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(getXWalkView());
                    mXWalkView.setResourceClient(client);
                    client.onLoadStarted(mXWalkView, "file:///android_asset/index.html");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnLoadStartedWithLocalUrl() {
        try {
            String url = "file:///android_asset/index.html";
            OnLoadStartedHelper mOnLoadStartedHelper = mTestHelperBridge.getOnLoadStartedHelper();
            int currentCallCount = mOnLoadStartedHelper.getCallCount();
            loadUrlAsync(url);
            mOnLoadStartedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnLoadStartedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnLoadStartedWithServer() {
        try {
            final String testHtml = "<html><head>Header</head><body>Body</body></html>";
            final String testPath = "/test.html";

            final String testUrl = mWebServer.setResponse(testPath, testHtml, null);

            OnLoadStartedHelper mOnLoadStartedHelper = mTestHelperBridge.getOnLoadStartedHelper();
            int currentCallCount = mOnLoadStartedHelper.getCallCount();
            loadUrlAsync(testUrl);
            mOnLoadStartedHelper.waitForCallback(currentCallCount);
            assertEquals(testUrl, mOnLoadStartedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnPageLoadStartedWithInvalidUrl() {
        try {
            String url = "file:///android_asset/invalid.html";
            OnLoadStartedHelper mOnLoadStartedHelper = mTestHelperBridge.getOnLoadStartedHelper();
            int currentCallCount = mOnLoadStartedHelper.getCallCount();
            loadUrlAsync(url);
            mOnLoadStartedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnLoadStartedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnLoadFinished() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkResourceClient client = new XWalkResourceClient(getXWalkView());
                    mXWalkView.setResourceClient(client);
                    client.onLoadFinished(mXWalkView, "http://www.baidu.com");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnLoadFinishedWithLocalUrl() {
        try {
            String url = "file:///android_asset/index.html";
            OnLoadFinishedHelper mOnLoadFinishedHelper = mTestHelperBridge.getOnLoadFinishedHelper();
            int currentCallCount = mOnLoadFinishedHelper.getCallCount();
            loadUrlAsync(url);
            mOnLoadFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(url, mOnLoadFinishedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnLoadFinishedPassesCorrectUrl() {
        try {
            OnLoadFinishedHelper mOnLoadFinishedHelper = mTestHelperBridge.getOnLoadFinishedHelper();
            String html = "<html><body>Simple page.</body></html>";
            int currentCallCount = mOnLoadFinishedHelper.getCallCount();
            loadDataAsync(null, html, "text/html", false);
            mOnLoadFinishedHelper.waitForCallback(currentCallCount);
            assertEquals("about:blank", mOnLoadFinishedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnLoadFinishedWithInvalidUrl() {
        try {
            OnLoadFinishedHelper mOnLoadFinishedHelper = mTestHelperBridge.getOnLoadFinishedHelper();
            String url = "file:///android_asset/non_existent";
            int currentCallCount = mOnLoadFinishedHelper.getCallCount();
            loadUrlAsync(url);
            mOnLoadFinishedHelper.waitForCallback(currentCallCount);
            SystemClock.sleep(1000);
            assertEquals(url, mOnLoadFinishedHelper.getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnPageFinishedNotCalledForValidSubresources() {
        try {
            OnLoadFinishedHelper mOnLoadFinishedHelper = mTestHelperBridge.getOnLoadFinishedHelper();
            final String testHtml = "<html><head>Header</head><body>Body</body></html>";
            final String testPath = "/test.html";
            final String syncPath = "/sync.html";
            final String testUrl = mWebServer.setResponse(testPath, testHtml, null);
            final String syncUrl = mWebServer.setResponse(syncPath, testHtml, null);
            assertEquals(0, mOnLoadFinishedHelper.getCallCount());
            final int pageWithSubresourcesCallCount = mOnLoadFinishedHelper.getCallCount();
            loadDataAsync("test.html", "<html><iframe src=\"" + testUrl + "\" /></html>", "text/html", false);
            mOnLoadFinishedHelper.waitForCallback(pageWithSubresourcesCallCount);
            final int synchronizationPageCallCount = mOnLoadFinishedHelper.getCallCount();
            loadUrlAsync(syncUrl);
            mOnLoadFinishedHelper.waitForCallback(synchronizationPageCallCount);
            assertEquals(syncUrl, mOnLoadFinishedHelper.getUrl());
            assertEquals(2, mOnLoadFinishedHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnLoadFinishedNotCalledForJavaScriptUrl() {
        try {
            OnLoadFinishedHelper mOnLoadFinishedHelper = mTestHelperBridge.getOnLoadFinishedHelper();
            String html = "<html><body>Simple page.</body></html>";
            int currentCallCount = mOnLoadFinishedHelper.getCallCount();
            assertEquals(0, currentCallCount);
            loadDataAsync(null, html, "text/html", false);
            loadUrlAsync("javascript: try { console.log('foo'); } catch(e) {};");

            mOnLoadFinishedHelper.waitForCallback(currentCallCount);
            assertEquals("about:blank", mOnLoadFinishedHelper.getUrl());
            assertEquals(1, mOnLoadFinishedHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnProgressChanged() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(getXWalkView());
                    mXWalkView.setResourceClient(client);
                    client.onProgressChanged(mXWalkView, NUM_NAVIGATIONS);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testOnProgressChanged_function() {
        try {
            OnProgressChangedHelper mOnProgressChangedHelper = mTestHelperBridge.getOnProgressChangedHelper();
            final int callCount = mOnProgressChangedHelper.getCallCount();
            final String testHtml = "<html><head>Header</head><body>Body</body></html>";
            final String testPath = "/test.html";
            final String testUrl = mWebServer.setResponse(testPath, testHtml, null);
            loadDataAsync("test.html", "<html><iframe src=\"" + testUrl + "\" /></html>", "text/html", false);
            mOnProgressChangedHelper.waitForCallback(callCount);
            assertTrue(mOnProgressChangedHelper.getProgress() > 0);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }  
    }

    @SmallTest
    public void testShouldInterceptLoadRequest() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkResourceClient client = new XWalkResourceClient(mXWalkView);
                    mXWalkView.setResourceClient(client);
                    client.shouldInterceptLoadRequest(mXWalkView, "http://www.baidu.com/");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestWithCorrectUrl() {
        try {
            final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            int onPageFinishedCallCount = mTestHelperBridge.getOnPageFinishedHelper().getCallCount();
            loadUrlAsync(aboutPageUrl);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
            assertEquals(1, mShouldInterceptLoadRequestHelper.getUrls().size());
            assertEquals(aboutPageUrl, mShouldInterceptLoadRequestHelper.getUrls().get(0));
            mTestHelperBridge.getOnPageFinishedHelper().waitForCallback(onPageFinishedCallCount);
            assertEquals(ABOUT_TITLE, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestOnInvalidData1() {
        try {
            String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            mShouldInterceptLoadRequestHelper.setReturnValue(new WebResourceResponse("text/html", "UTF-8", null));
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlAsync(aboutPageUrl);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestOnInvalidData2() {
        try {
            String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            mShouldInterceptLoadRequestHelper.setReturnValue(null);
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlAsync(aboutPageUrl);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestOnInvalidData3() {
        try {
            String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            mShouldInterceptLoadRequestHelper.setReturnValue(new WebResourceResponse(null, null, new ByteArrayInputStream(new byte[0])));
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlAsync(aboutPageUrl);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestOnInvalidData4() {
        try {
            String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            mShouldInterceptLoadRequestHelper.setReturnValue(new WebResourceResponse(null, null, null));
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlAsync(aboutPageUrl);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestOnEmptyStream() {
        try {
            final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            mShouldInterceptLoadRequestHelper.setReturnValue(
                    new WebResourceResponse("text/html", "UTF-8", new EmptyInputStream()));
            int shouldInterceptRequestCallCount = mShouldInterceptLoadRequestHelper.getCallCount();
            int onPageFinishedCallCount = mTestHelperBridge.getOnPageFinishedHelper().getCallCount();
    
            loadUrlAsync(aboutPageUrl);
    
            mShouldInterceptLoadRequestHelper.waitForCallback(shouldInterceptRequestCallCount);
            mTestHelperBridge.getOnPageFinishedHelper().waitForCallback(onPageFinishedCallCount);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestHttpStatusField() {
        try {
            final String syncGetUrl = mWebServer.getResponseUrl("/intercept_me");
            final String syncGetJs =
                "(function() {" +
                "  var xhr = new XMLHttpRequest();" +
                "  xhr.open('GET', '" + syncGetUrl + "', false);" +
                "  xhr.send(null);" +
                "  console.info('xhr.status = ' + xhr.status);" +
                "  return xhr.status;" +
                "})();";
            final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            loadUrlSync(aboutPageUrl);
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            mShouldInterceptLoadRequestHelper.setReturnValue(new WebResourceResponse("text/html", "UTF-8", null));
            assertEquals("404", executeJavaScriptAndWaitForResult(syncGetJs));
            mShouldInterceptLoadRequestHelper.setReturnValue(new WebResourceResponse("text/html", "UTF-8", new EmptyInputStream()));
            assertEquals("200", executeJavaScriptAndWaitForResult(syncGetJs));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestCanInterceptMainFrame() {
        try {
            final String expectedTitle = "testShouldInterceptLoadRequestCanInterceptMainFrame";
            final String expectedPage = "<html><head><title>" + expectedTitle + "</title></head><body>Body</body></html>";
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            mShouldInterceptLoadRequestHelper.setReturnValue(stringToWebResourceResponse(expectedPage));

            final String aboutPageUrl = addAboutPageToTestServer(mWebServer);

            loadUrlSync(aboutPageUrl);

            assertEquals(expectedTitle, getTitleOnUiThread());
            assertEquals(0, mWebServer.getRequestCount("/about.html"));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestDoesNotChangeReportedUrl() {
        try {
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            String expectedTitle = "some title";
            mShouldInterceptLoadRequestHelper.setReturnValue(stringToWebResourceResponse("<html><head><title>" + expectedTitle + "</title></head><body>Body</body></html>"));
            final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            loadUrlSync(aboutPageUrl);
            assertEquals(aboutPageUrl, mTestHelperBridge.getOnPageFinishedHelper().getUrl());
            assertEquals(aboutPageUrl, mTestHelperBridge.getOnPageStartedHelper().getUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestForImage() {
        try {
            final String imagePath = "/about.html";
            mWebServer.setResponseBase64(imagePath, CommonResources.FAVICON_DATA_BASE64, CommonResources.getImagePngHeaders(true));
            final String pageWithImage = addPageToTestServer(mWebServer, "/page_with_image.html",
                        CommonResources.getOnImageLoadedHtml(CommonResources.FAVICON_FILENAME));
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlSync(pageWithImage);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount, 2);
            assertEquals(2, mShouldInterceptLoadRequestHelper.getUrls().size());
            assertTrue(mShouldInterceptLoadRequestHelper.getUrls().get(1).endsWith(
                    CommonResources.FAVICON_FILENAME));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestForIframe() {
        try {
            final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
            final String pageWithIframe = addPageToTestServer(mWebServer, "/page_with_iframe.html",
                    CommonResources.makeHtmlPageFrom("", "<iframe src=\"" + aboutPageUrl + "\"/>"));
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            // These callbacks can race with favicon.ico callback.
            mShouldInterceptLoadRequestHelper.setUrlToWaitFor(aboutPageUrl);
            loadUrlSync(pageWithIframe);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount, 1);
            assertEquals(1, mShouldInterceptLoadRequestHelper.getUrls().size());
            assertEquals(aboutPageUrl, mShouldInterceptLoadRequestHelper.getUrls().get(0));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestForNonexistentFiles() {
        try {
            String url = "file:///somewhere/something";
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlSync(url);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
            assertEquals(url, mShouldInterceptLoadRequestHelper.getUrls().get(0));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestForExistingFiles() {
        try {
            final String tmpDir = getInstrumentation().getTargetContext().getCacheDir().getPath();
            final String fileName = tmpDir + "/testfile.html";
            final String title = "existing file title";
            TestFileUtil.deleteFile(fileName);  // Remove leftover file if any.
            TestFileUtil.createNewHtmlFile(fileName, title, "");
            final String existingFileUrl = "file://" + fileName;
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            int onPageFinishedCallCount = mTestHelperBridge.getOnPageFinishedHelper().getCallCount();
            loadUrlAsync(existingFileUrl);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
            assertEquals(existingFileUrl, mShouldInterceptLoadRequestHelper.getUrls().get(0));
    
            mTestHelperBridge.getOnPageFinishedHelper().waitForCallback(onPageFinishedCallCount);
            assertEquals(title, getTitleOnUiThread());
            assertEquals(onPageFinishedCallCount + 1,
                    mTestHelperBridge.getOnPageFinishedHelper().getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestExistingAsset_notCalled() {
        try {
            final String existingFileUrl = "file:///android_asset/index.html";
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlSync(existingFileUrl);
            assertTrue(mShouldInterceptLoadRequestHelper.getUrls().isEmpty());
            assertEquals(callCount, mShouldInterceptLoadRequestHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldInterceptLoadRequestForNonexistentAsset() {
        try {
            final String url = "file:///android_res/raw/no_file.html";
            ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper = mTestHelperBridge.getShouldInterceptLoadRequestHelper();
            int callCount = mShouldInterceptLoadRequestHelper.getCallCount();
            loadUrlAsync(url);
            mShouldInterceptLoadRequestHelper.waitForCallback(callCount);
            SystemClock.sleep(2000);
            assertEquals(url, mShouldInterceptLoadRequestHelper.getUrls().get(0));
            assertEquals(callCount + 1, mTestHelperBridge.getOnPageStartedHelper().getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedLoadError() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(mXWalkView);
                    mXWalkView.setResourceClient(client);
                    client.onReceivedLoadError(mXWalkView, NUM_NAVIGATIONS, null, "http://www.baidu.com/");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedLoadErrorOnInvalidUrl() {
        try {
            String url = "file:///android_asset/invalid.html";
            OnReceivedErrorHelper mOnReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
            int onReceivedErrorCallCount = mOnReceivedErrorHelper.getCallCount();
            loadUrlAsync(url);
            mOnReceivedErrorHelper.waitForCallback(onReceivedErrorCallCount);
            assertEquals(url, mOnReceivedErrorHelper.getFailingUrl());
            assertNotNull(mOnReceivedErrorHelper.getDescription());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedLoadErrorOnInvalidScheme() {
        try {
            String url = "foo://some/resource";
            OnReceivedErrorHelper mOnReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
            int onReceivedErrorCallCount = mOnReceivedErrorHelper.getCallCount();
            loadUrlAsync(url);
            mOnReceivedErrorHelper.waitForCallback(onReceivedErrorCallCount);
            assertEquals(XWalkResourceClient.ERROR_UNSUPPORTED_SCHEME,
                    mOnReceivedErrorHelper.getErrorCode());
            assertEquals(url, mOnReceivedErrorHelper.getFailingUrl());
            assertNotNull(mOnReceivedErrorHelper.getDescription());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
    
    @SmallTest
    public void testOnReceivedLoadErrorOnFailedSubresourceLoad() {
        try {
            TestCallbackHelperContainer.OnPageFinishedHelper onPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            OnReceivedErrorHelper mOnReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
            int currentCallCount = onPageFinishedHelper.getCallCount();
            loadDataAsync("<html><iframe src=\"http//invalid.url.co/\" /></html>", null, "text/html", false);
            onPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(0, mOnReceivedErrorHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedLoadErrorNonExistentAssetUrl() {
        try {
            final String url = "file:///android_asset/does_not_exist.html";
            OnReceivedErrorHelper mOnReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
            int onReceivedErrorCallCount = mOnReceivedErrorHelper.getCallCount();
            loadUrlAsync(url);
            mOnReceivedErrorHelper.waitForCallback(onReceivedErrorCallCount);
            assertEquals(XWalkResourceClient.ERROR_UNKNOWN, mOnReceivedErrorHelper.getErrorCode());
            assertEquals(url, mOnReceivedErrorHelper.getFailingUrl());
            assertNotNull(mOnReceivedErrorHelper.getDescription());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnReceivedLoadErrorOnLoadUrl() {
        try {
            TestCallbackHelperContainer.OnPageFinishedHelper onPageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
            OnReceivedErrorHelper mOnReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
            int currentCallCount = onPageFinishedHelper.getCallCount();
            loadUrlAsync("file:///android_asset/index.html");
            onPageFinishedHelper.waitForCallback(currentCallCount);
            assertEquals(0, mOnReceivedErrorHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

}
