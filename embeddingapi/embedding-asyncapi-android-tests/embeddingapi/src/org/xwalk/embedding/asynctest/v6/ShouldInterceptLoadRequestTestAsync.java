//Copyright (c) 2013 The Chromium Authors. All rights reserved.
//Copyright (c) 2014 Intel Corporation. All rights reserved.
//Use of this source code is governed by a BSD-style license that can be
//found in the LICENSE file.

package org.xwalk.embedding.asynctest.v6;

import android.test.suitebuilder.annotation.SmallTest;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.chromium.base.test.util.Feature;
import org.chromium.base.test.util.TestFileUtil;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnReceivedErrorHelper;

import org.xwalk.embedding.base.OnLoadStartedHelper;
import org.xwalk.embedding.base.ShouldInterceptLoadRequestHelper2;
import org.xwalk.embedding.base.AsynctestContentProvider;
import org.xwalk.embedding.base.TestXWalkResourceClientBase;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

/**
* Test case for XWalkResourceClient.shouldInterceptRequest callback
*
* Note the major part of this file is migrated from android_webview/.
*/
public class ShouldInterceptLoadRequestTestAsync extends XWalkViewTestBase {

 private TestXWalkResourceClientBase mTestXWalkResourceClient1;
 private ShouldInterceptLoadRequestHelper2 mShouldInterceptLoadRequestHelper2;
 private OnLoadStartedHelper mOnLoadStartedHelper;

 @Override
 protected void setUp() throws Exception {
     super.setUp();

     getInstrumentation().runOnMainSync(new Runnable() {
         @Override
         public void run() {
             mTestXWalkResourceClient1 = mTestXWalkResourceClient;
             mShouldInterceptLoadRequestHelper2 = mTestHelperBridge.getShouldInterceptLoadRequestHelper2();
             mOnLoadStartedHelper = mTestHelperBridge.getOnLoadStartedHelper();
         }
     });
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledWithCorrectUrl() throws Throwable {
     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);

     int callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     int onPageFinishedCallCount = mTestHelperBridge.getOnPageFinishedHelper().getCallCount();

     loadUrlAsync(aboutPageUrl);

     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount);
     assertEquals(1, mShouldInterceptLoadRequestHelper2.getUrls().size());
     assertEquals(aboutPageUrl,
             mShouldInterceptLoadRequestHelper2.getUrls().get(0));

     mTestHelperBridge.getOnPageFinishedHelper().waitForCallback(onPageFinishedCallCount);
     assertEquals(CommonResources.ABOUT_TITLE, getTitleOnUiThread());
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testOnLoadResourceCalledWithCorrectUrl() throws Throwable {
     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
     int callCount = mOnLoadStartedHelper.getCallCount();

     loadUrlAsync(aboutPageUrl);

     mOnLoadStartedHelper.waitForCallback(callCount);
     assertEquals(aboutPageUrl, mOnLoadStartedHelper.getUrl());
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testDoesNotCrashOnInvalidData() throws Throwable {
     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);

     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse("text/html", "UTF-8", null));
     int callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     loadUrlAsync(aboutPageUrl);
     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount);

     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse(
                     null, null, new ByteArrayInputStream(new byte[0])));
     callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     loadUrlAsync(aboutPageUrl);
     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount);

     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse(null, null, null));
     callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     loadUrlAsync(aboutPageUrl);
     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount);
 }

 private static class EmptyInputStream extends InputStream {
     @Override
     public int available() {
         return 0;
     }

     @Override
     public int read() throws IOException {
         return -1;
     }

     @Override
     public int read(byte b[]) throws IOException {
         return -1;
     }

     @Override
     public int read(byte b[], int off, int len) throws IOException {
         return -1;
     }

     @Override
     public long skip(long n) throws IOException {
         if (n < 0)
             throw new IOException("skipping negative number of bytes");
         return 0;
     }
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testDoesNotCrashOnEmptyStream() throws Throwable {
     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);

     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse(
                     "text/html", "UTF-8", new EmptyInputStream()));
     int shouldInterceptRequestCallCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     int onPageFinishedCallCount = mTestHelperBridge.getOnPageFinishedHelper().getCallCount();

     loadUrlAsync(aboutPageUrl);

     mShouldInterceptLoadRequestHelper2.waitForCallback(shouldInterceptRequestCallCount);
     mTestHelperBridge.getOnPageFinishedHelper().waitForCallback(onPageFinishedCallCount);
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testHttpStatusField() throws Throwable {
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

     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse(
                     "text/html", "UTF-8", null));
     assertEquals("404", executeJavaScriptAndWaitForResult(syncGetJs));

     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse(
                     "text/html", "UTF-8", new EmptyInputStream()));
     assertEquals("200", executeJavaScriptAndWaitForResult(syncGetJs));
 }


 private String makePageWithTitle(String title) {
     return CommonResources.makeHtmlPageFrom("<title>" + title + "</title>",
             "<div> The title is: " + title + " </div>");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCanInterceptMainFrame() throws Throwable {
     final String expectedTitle = "testShouldInterceptLoadRequestCanInterceptMainFrame";
     final String expectedPage = makePageWithTitle(expectedTitle);

     mShouldInterceptLoadRequestHelper2.setReturnValue(
             stringToWebResourceResponse2(expectedPage));

     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);

     loadUrlSync(aboutPageUrl);

     assertEquals(expectedTitle, getTitleOnUiThread());
     assertEquals(0, mWebServer.getRequestCount("/" + CommonResources.ABOUT_FILENAME));
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testDoesNotChangeReportedUrl() throws Throwable {
     mShouldInterceptLoadRequestHelper2.setReturnValue(
             stringToWebResourceResponse2(makePageWithTitle("some title")));

     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);

     loadUrlSync(aboutPageUrl);

     assertEquals(aboutPageUrl, mTestHelperBridge.getOnPageFinishedHelper().getUrl());
     assertEquals(aboutPageUrl, mTestHelperBridge.getOnPageStartedHelper().getUrl());
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testNullInputStreamCausesErrorForMainFrame() throws Throwable {
     final OnReceivedErrorHelper onReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse("text/html", "UTF-8", null));

     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
     final int callCount = onReceivedErrorHelper.getCallCount();
     loadUrlAsync(aboutPageUrl);
     onReceivedErrorHelper.waitForCallback(callCount);
     assertEquals(0, mWebServer.getRequestCount("/" + CommonResources.ABOUT_FILENAME));
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForImage() throws Throwable {
     final String imagePath = "/" + CommonResources.FAVICON_FILENAME;
     mWebServer.setResponseBase64(imagePath,
             CommonResources.FAVICON_DATA_BASE64, CommonResources.getImagePngHeaders(true));
     final String pageWithImage =
         addPageToTestServer(mWebServer, "/page_with_image.html",
                 CommonResources.getOnImageLoadedHtml(CommonResources.FAVICON_FILENAME));

     int callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     loadUrlSync(pageWithImage);
     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount, 2);

     assertEquals(2, mShouldInterceptLoadRequestHelper2.getUrls().size());
     assertTrue(mShouldInterceptLoadRequestHelper2.getUrls().get(1).endsWith(
             CommonResources.FAVICON_FILENAME));
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testOnReceivedErrorCallback() throws Throwable {
     final OnReceivedErrorHelper onReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
     mShouldInterceptLoadRequestHelper2.setReturnValue(
             mTestXWalkResourceClient1.createXWalkWebResourceResponse(null, null, null));
     int onReceivedErrorHelperCallCount = onReceivedErrorHelper.getCallCount();
     loadUrlSync("foo://bar");
     onReceivedErrorHelper.waitForCallback(onReceivedErrorHelperCallCount, 1);
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testNoOnReceivedErrorCallback() throws Throwable {
     final String imagePath = "/" + CommonResources.FAVICON_FILENAME;
     final String imageUrl = mWebServer.setResponseBase64(imagePath,
             CommonResources.FAVICON_DATA_BASE64, CommonResources.getImagePngHeaders(true));
     final String pageWithImage =
             addPageToTestServer(mWebServer, "/page_with_image.html",
                     CommonResources.getOnImageLoadedHtml(CommonResources.FAVICON_FILENAME));
     final OnReceivedErrorHelper onReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
     mShouldInterceptLoadRequestHelper2.setReturnValueForUrl(
             imageUrl,
             mTestXWalkResourceClient1.createXWalkWebResourceResponse(null, null, null));
     int onReceivedErrorHelperCallCount = onReceivedErrorHelper.getCallCount();
     loadUrlSync(pageWithImage);
     assertEquals(onReceivedErrorHelperCallCount, onReceivedErrorHelper.getCallCount());
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForIframe() throws Throwable {
     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
     final String pageWithIframe = addPageToTestServer(mWebServer, "/page_with_iframe.html",
             CommonResources.makeHtmlPageFrom("",
                 "<iframe src=\"" + aboutPageUrl + "\"/>"));

     int callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     // These callbacks can race with favicon.ico callback.
     mShouldInterceptLoadRequestHelper2.setUrlToWaitFor(aboutPageUrl);
     loadUrlSync(pageWithIframe);

     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount, 1);
     assertEquals(1, mShouldInterceptLoadRequestHelper2.getUrls().size());
     assertEquals(aboutPageUrl, mShouldInterceptLoadRequestHelper2.getUrls().get(0));
 }

 private void calledForUrlTemplate(final String url) throws Exception {
     int callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     int onPageStartedCallCount = mTestHelperBridge.getOnPageStartedHelper().getCallCount();
     loadUrlAsync(url);
     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount);
     assertEquals(url, mShouldInterceptLoadRequestHelper2.getUrls().get(0));

     mTestHelperBridge.getOnPageStartedHelper().waitForCallback(onPageStartedCallCount);
     assertEquals(onPageStartedCallCount + 1,
             mTestHelperBridge.getOnPageStartedHelper().getCallCount());
 }

 private void notCalledForUrlTemplate(final String url) throws Exception {
     int callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     loadUrlSync(url);
     // The intercepting must happen before onPageFinished. Since the IPC messages from the
     // renderer should be delivered in order waiting for onPageFinished is sufficient to
     // 'flush' any pending interception messages.
     assertEquals(callCount, mShouldInterceptLoadRequestHelper2.getCallCount());
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForUnsupportedSchemes() throws Throwable {
     calledForUrlTemplate("foobar://resource/1");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForNonexistentFiles() throws Throwable {
     calledForUrlTemplate("file:///somewhere/something");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForExistingFiles() throws Throwable {
     final String tmpDir = getInstrumentation().getTargetContext().getCacheDir().getPath();
     final String fileName = tmpDir + "/testfile.html";
     final String title = "existing file title";
     TestFileUtil.deleteFile(fileName);  // Remove leftover file if any.
     TestFileUtil.createNewHtmlFile(fileName, title, "");
     final String existingFileUrl = "file://" + fileName;

     int callCount = mShouldInterceptLoadRequestHelper2.getCallCount();
     int onPageFinishedCallCount = mTestHelperBridge.getOnPageFinishedHelper().getCallCount();
     loadUrlAsync(existingFileUrl);
     mShouldInterceptLoadRequestHelper2.waitForCallback(callCount);
     assertEquals(existingFileUrl, mShouldInterceptLoadRequestHelper2.getUrls().get(0));

     mTestHelperBridge.getOnPageFinishedHelper().waitForCallback(onPageFinishedCallCount);
     assertEquals(title, getTitleOnUiThread());
     assertEquals(onPageFinishedCallCount + 1,
             mTestHelperBridge.getOnPageFinishedHelper().getCallCount());
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testNotCalledForExistingResource() throws Throwable {
     notCalledForUrlTemplate("file:///android_res/raw/resource_file.html");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForNonexistentResource() throws Throwable {
     calledForUrlTemplate("file:///android_res/raw/no_file.html");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testNotCalledForExistingAsset() throws Throwable {
     notCalledForUrlTemplate("file:///android_asset/index.html");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForNonexistentAsset() throws Throwable {
     calledForUrlTemplate("file:///android_res/raw/no_file.html");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testNotCalledForExistingContentUrl() throws Throwable {
     final String contentResourceName = "target";
     final String existingContentUrl = AsynctestContentProvider.createContentUrl(contentResourceName);
     AsynctestContentProvider.resetResourceRequestCount(
             getInstrumentation().getTargetContext(), contentResourceName);

     notCalledForUrlTemplate(existingContentUrl);

     int contentRequestCount = AsynctestContentProvider.getResourceRequestCount(
             getInstrumentation().getTargetContext(), contentResourceName);
     assertEquals(1, contentRequestCount);
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testCalledForNonexistentContentUrl() throws Throwable {
     calledForUrlTemplate("content://org.xwalk.core.test.NoSuchProvider/foo");
 }

 @SmallTest
 @Feature({"ShouldInterceptLoadRequest"})
 public void testOnPageStartedOnlyOnMainFrame() throws Throwable {
     final String aboutPageUrl = addAboutPageToTestServer(mWebServer);
     final String pageWithIframe = addPageToTestServer(mWebServer, "/page_with_iframe.html",
             CommonResources.makeHtmlPageFrom("",
                 "<iframe src=\"" + aboutPageUrl + "\"/>"));
     int onPageStartedCallCount = mTestHelperBridge.getOnPageStartedHelper().getCallCount();

     loadUrlSync(pageWithIframe);

     mTestHelperBridge.getOnPageStartedHelper().waitForCallback(onPageStartedCallCount);
     assertEquals(onPageStartedCallCount + 1,
             mTestHelperBridge.getOnPageStartedHelper().getCallCount());
 }
}