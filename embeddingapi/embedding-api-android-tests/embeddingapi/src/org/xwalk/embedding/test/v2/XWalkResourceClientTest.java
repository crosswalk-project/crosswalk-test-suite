// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v2;


import java.util.concurrent.Callable;

import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageStartedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnReceivedErrorHelper;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.embedding.base.ShouldOverrideUrlLoadingHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkResourceClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testShouldOverrideUrlLoading() {
        try {
            loadUrlSync("about:blank");
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(mXWalkView);
                    assertFalse(client.shouldOverrideUrlLoading(mXWalkView,"about:blank"));
                }
            });

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingNotCalledOnLoadData() {
        try {
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            loadDataSync(null, CommonResources.makeHtmlPageWithSimpleLinkTo(DATA_URL), "text/html", false);
            assertEquals(0, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingOnBackForwardNavigation() {
        try {
            final String url = "file:///android_asset/index.html";
            final String httpPath = "/test.html";
            final String httpPathOnServer = mWebServer.getResponseUrl(httpPath);
            addPageToTestServer(mWebServer, httpPath,
                    CommonResources.makeHtmlPageWithSimpleLinkTo(httpPathOnServer));
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            loadUrlSync(httpPathOnServer);
            loadUrlSync(url);
            assertEquals(2, mShouldOverrideUrlLoadingHelper.getCallCount());
            String oldTitle = getTitleOnUiThread();
            goBackSync(1);
            assertFalse(oldTitle.equals(getTitleOnUiThread()));
            assertEquals(3, mShouldOverrideUrlLoadingHelper.getCallCount());
            oldTitle = getTitleOnUiThread();
            goForwardSync(1);
            assertFalse(oldTitle.equals(getTitleOnUiThread()));
            assertEquals(4, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoading_OnPageStarted() {
        try {
            OnPageStartedHelper onPageStartedHelper = mTestHelperBridge.getOnPageStartedHelper();
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            loadDataSync(null,
                    CommonResources.makeHtmlPageWithSimpleLinkTo(DATA_URL), "text/html", false);
            final int shouldOverrideUrlLoadingCallCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            final int onPageStartedCallCount = onPageStartedHelper.getCallCount();
            mShouldOverrideUrlLoadingHelper.setShouldOverrideUrlLoadingReturnValue(true);
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(shouldOverrideUrlLoadingCallCount);
            assertEquals(onPageStartedCallCount, onPageStartedHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoading_OnReceivedError() {
        try {
            String url = "file:///android_asset/does_not_exist.html";
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            OnReceivedErrorHelper onReceivedErrorHelper = mTestHelperBridge.getOnReceivedErrorHelper();
            int onReceivedErrorCallCount = onReceivedErrorHelper.getCallCount();
            int shouldOverrideUrlLoadingCallCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            mShouldOverrideUrlLoadingHelper.setShouldOverrideUrlLoadingReturnValue(true);
            loadUrlSync(url);
            mShouldOverrideUrlLoadingHelper.waitForCallback(shouldOverrideUrlLoadingCallCount);
            assertEquals(onReceivedErrorCallCount, onReceivedErrorHelper.getCallCount());

            onReceivedErrorCallCount = onReceivedErrorHelper.getCallCount();
            shouldOverrideUrlLoadingCallCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            mShouldOverrideUrlLoadingHelper.setShouldOverrideUrlLoadingReturnValue(false);
            loadUrlSync(url);
            mShouldOverrideUrlLoadingHelper.waitForCallback(shouldOverrideUrlLoadingCallCount);
            assertNotSame(onReceivedErrorCallCount, onReceivedErrorHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingWhenLinkClicked() {
        try {
            loadDataSync(null, CommonResources.makeHtmlPageWithSimpleLinkTo(DATA_URL), "text/html", false);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            int callCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(callCount);
            assertEquals(1, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingWhenSelfLinkClicked() {
        try {
            final String httpPath = "/page_with_link_to_self.html";
            final String httpPathOnServer = mWebServer.getResponseUrl(httpPath);
            addPageToTestServer(mWebServer, httpPath,
                    CommonResources.makeHtmlPageWithSimpleLinkTo(httpPathOnServer));
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            loadUrlSync(httpPathOnServer);
            int callCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(callCount);
            assertEquals(httpPathOnServer,
                    mShouldOverrideUrlLoadingHelper.getShouldOverrideUrlLoadingUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingWhenNavigatingFromJavaScriptUsingAssign() {
        try {
            final String redirectTargetUrl = addPageToTestServer(mWebServer, REDIRECT_TARGET_PATH,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<div>This is the end of the redirect chain</div>"));
            loadDataSync(null,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<img onclick=\"location.href='" + redirectTargetUrl + "'\" class=\"big\" id=\"link\" />"), "text/html", false);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            int callCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(callCount);
            assertEquals(1, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingWhenNavigatingFromJavaScriptUsingReplace() {
        try {
            final String redirectTargetUrl = addPageToTestServer(mWebServer, REDIRECT_TARGET_PATH,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<div>This is the end of the redirect chain</div>"));
            loadDataSync(null,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<img onclick=\"location.replace('" + redirectTargetUrl + "');\" class=\"big\" id=\"link\" />"), "text/html", false);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            int callCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(callCount);
            assertEquals(1, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    
    public void testShouldOverrideUrlLoadingWithCorrectUrl() {
        try {
            final String redirectTargetUrl = addPageToTestServer(mWebServer, REDIRECT_TARGET_PATH,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<div>This is the end of the redirect chain</div>"));
            loadDataSync(null,
                    CommonResources.makeHtmlPageWithSimpleLinkTo(redirectTargetUrl), "text/html", false);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            int callCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(callCount);
            assertEquals(redirectTargetUrl,
                    mShouldOverrideUrlLoadingHelper.getShouldOverrideUrlLoadingUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingForDataUrl() {
        try {
            final String dataUrl =
                    "data:text/html;base64," +
                    "PGh0bWw+PGhlYWQ+PHRpdGxlPmRhdGFVcmxUZXN0QmFzZTY0PC90aXRsZT48" +
                    "L2hlYWQ+PC9odG1sPg==";
            loadDataSync(null, CommonResources.makeHtmlPageWithSimpleLinkTo(dataUrl), "text/html", false);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            int callCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(callCount);
            assertTrue("Expected URL that starts with 'data:' but got: <" + mShouldOverrideUrlLoadingHelper.getShouldOverrideUrlLoadingUrl() + "> instead.",
                    mShouldOverrideUrlLoadingHelper.getShouldOverrideUrlLoadingUrl().startsWith("data:"));
            assertEquals(1, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingForUnsupportedSchemes() {
        try {
            final String unsupportedSchemeUrl = "foobar://resource/1";
            loadDataSync(null,
                    CommonResources.makeHtmlPageWithSimpleLinkTo(unsupportedSchemeUrl), "text/html",
                            false);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            int callCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(callCount);
            assertEquals(unsupportedSchemeUrl,
                    mShouldOverrideUrlLoadingHelper.getShouldOverrideUrlLoadingUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingForPostNavigations() {
        try {
            final String redirectTargetUrl = addPageToTestServer(mWebServer, REDIRECT_TARGET_PATH,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<div>This is the end of the redirect chain</div>"));
            final String postLinkUrl = addPageToTestServer(mWebServer, "/page_with_post_link.html",
                    CommonResources.makeHtmlPageWithSimplePostFormTo(redirectTargetUrl));
            loadUrlSync(postLinkUrl);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            final int shouldOverrideUrlLoadingCallCount = mShouldOverrideUrlLoadingHelper.getCallCount();
    
            assertEquals(0, mWebServer.getRequestCount(REDIRECT_TARGET_PATH));
            clickOnElementId("link", null);

            // Wait for the target URL to be fetched from the server.
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mWebServer.getRequestCount(REDIRECT_TARGET_PATH) == 1;
                }
            });
            assertEquals(shouldOverrideUrlLoadingCallCount + 1, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingFor302AfterPostNavigations() {
        try {
            final String redirectTargetUrl = addPageToTestServer(mWebServer, REDIRECT_TARGET_PATH,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<div>This is the end of the redirect chain</div>"));
            final String postToGetRedirectUrl = mWebServer.setRedirect("/302.html", redirectTargetUrl);
            final String postLinkUrl = addPageToTestServer(mWebServer, "/page_with_post_link.html",
                    CommonResources.makeHtmlPageWithSimplePostFormTo(postToGetRedirectUrl));
            loadUrlSync(postLinkUrl);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            final int shouldOverrideUrlLoadingCallCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            mShouldOverrideUrlLoadingHelper.waitForCallback(shouldOverrideUrlLoadingCallCount);

            // Wait for the target URL to be fetched from the server.
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mWebServer.getRequestCount(REDIRECT_TARGET_PATH) == 1;
                }
            });
            assertEquals(redirectTargetUrl, mShouldOverrideUrlLoadingHelper.getShouldOverrideUrlLoadingUrl());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingForIframeHttpNavigations() {
        try {
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            final String iframeRedirectTargetUrl = addPageToTestServer(mWebServer, REDIRECT_TARGET_PATH,
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<div>This is the end of the redirect chain</div>"));
            final String iframeRedirectUrl = mWebServer.setRedirect("/302.html", iframeRedirectTargetUrl);
            final String pageWithIframeUrl = addPageToTestServer(mWebServer, "/iframe_intercept.html",
                    CommonResources.makeHtmlPageFrom("<title>" + TITLE + "</title> ", "<iframe src=\"" + iframeRedirectUrl + "\" />"));
            assertEquals(0, mWebServer.getRequestCount(REDIRECT_TARGET_PATH));
            loadUrlSync(pageWithIframeUrl);
            // Wait for the redirect target URL to be fetched from the server.
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mWebServer.getRequestCount(REDIRECT_TARGET_PATH) == 1;
                }
            });
            assertEquals(1, mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingNotCalledForAnchorNavigations() {
        try {
            final String anchorLinkPath = "/anchor_link.html";
            final String anchorLinkUrl = mWebServer.getResponseUrl(anchorLinkPath);
            addPageToTestServer(mWebServer, anchorLinkPath,
                    CommonResources.makeHtmlPageWithSimpleLinkTo(anchorLinkUrl + "#anchor"));
            loadUrlSync(anchorLinkUrl);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            final int shouldOverrideUrlLoadingCallCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            loadUrlSync("about:blank");
            assertEquals(shouldOverrideUrlLoadingCallCount,
                    mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    public void testShouldOverrideUrlLoadingNotCalledForAnchorNavigationsWithNonHierarchicalScheme() {
        try {
            final String anchorLinkPath = "/anchor_link.html";
            final String anchorLinkUrl = mWebServer.getResponseUrl(anchorLinkPath);
            addPageToTestServer(mWebServer, anchorLinkPath,
                    CommonResources.makeHtmlPageWithSimpleLinkTo(anchorLinkUrl + "#anchor"));
            loadDataSync(null, CommonResources.makeHtmlPageWithSimpleLinkTo("#anchor"), "text/html", false);
            ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper = mTestHelperBridge.getShouldOverrideUrlLoadingHelper();
            final int shouldOverrideUrlLoadingCallCount = mShouldOverrideUrlLoadingHelper.getCallCount();
            clickOnElementId("link", null);
            loadUrlSync("about:blank");
            assertEquals(shouldOverrideUrlLoadingCallCount,
                    mShouldOverrideUrlLoadingHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

}
