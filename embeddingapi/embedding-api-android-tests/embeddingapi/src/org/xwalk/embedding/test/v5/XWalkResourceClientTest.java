// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;

import org.xwalk.core.ClientCertRequest;
import org.xwalk.core.ClientCertRequestHandler;
import org.xwalk.embedding.base.OnDocumentLoadedInFrameHelper;
import org.xwalk.embedding.base.OnReceivedClientCertRequestHelper;
import org.xwalk.embedding.base.OnReceivedHttpAuthRequestHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.test.suitebuilder.annotation.MediumTest;
import android.test.suitebuilder.annotation.SmallTest;

public class XWalkResourceClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testAOnDocumentLoadedInFrame() throws Throwable {
        OnDocumentLoadedInFrameHelper mOnDocumentLoadedInFrameHelper = mTestHelperBridge.getOnDocumentLoadedInFrameHelper();
        String path = "/test.html";
        String pageContent = CommonResources.makeHtmlPageFrom("<title>Test</title>",
                "<div> The title is: Test </div>");
        final String url = addPageToTestServer(mWebServer, path, pageContent);

        loadUrlSync(url);
        assertTrue(mOnDocumentLoadedInFrameHelper.getFrameId() > 0);
        assertEquals(1, mOnDocumentLoadedInFrameHelper.getCallCount());
    }

    @MediumTest
    public void testClientCertRequest() throws Throwable {
        OnReceivedClientCertRequestHelper mOnReceivedClientCertRequestHelper = mTestHelperBridge.getOnReceivedClientCertRequestHelper();
        final String url = "https://egov.privasphere.com/";
        int onReceivedClientCertRequestCallCount = mOnReceivedClientCertRequestHelper.getCallCount();
        try {
            loadUrlAsync(url);
            mOnReceivedClientCertRequestHelper.waitForCallback(onReceivedClientCertRequestCallCount);
            ClientCertRequest request = mOnReceivedClientCertRequestHelper.getHandler();
            assertEquals(ClientCertRequestHandler.class.getName(), request.getClass().getName());
            // Following parameters just for host: "egov.privasphere.com".
            assertEquals("egov.privasphere.com", request.getHost());
            assertEquals(443, request.getPort());
            assertEquals("RSA", request.getKeyTypes()[0]);
            assertEquals("ECDSA", request.getKeyTypes()[1]);
            assertNull(request.getPrincipals());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnReceivedHttpAuthRequest() {
        OnReceivedHttpAuthRequestHelper mOnReceivedHttpAuthRequestHelper = mTestHelperBridge.getOnReceivedHttpAuthRequestHelper();
        String url = "http://httpbin.org/basic-auth/user/passwd";
        String host = "httpbin.org";
        int count = mOnReceivedHttpAuthRequestHelper.getCallCount();
        try {
            loadUrlAsync(url);
            mOnReceivedHttpAuthRequestHelper.waitForCallback(count);
            assertEquals(host, mOnReceivedHttpAuthRequestHelper.getHost());
        } catch (Exception e) {
            // TODO: handle exception
            assertTrue(false);
        }
    }
}