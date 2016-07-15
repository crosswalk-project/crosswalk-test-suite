// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.asynctest.v6;


import java.util.ArrayList;
import java.util.List;

import org.xwalk.core.XWalkWebResourceRequest;
import org.xwalk.core.XWalkWebResourceResponse;
import org.xwalk.embedding.base.OnReceivedResponseHeadersHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.test.suitebuilder.annotation.SmallTest;
import android.util.Pair;

public class XWalkResourceClientTestAsync extends XWalkViewTestBase {

    @SmallTest
    public void testForMainResource() {
        try {
            OnReceivedResponseHeadersHelper mOnReceivedResponseHeadersHelper = mTestHelperBridge.getOnReceivedResponseHeadersHelper();
            List<Pair<String, String>> headers = new ArrayList<Pair<String, String>>();
            headers.add(Pair.create("Content-Type", "text/html; charset=utf-8"));
            headers.add(Pair.create("Coalesce", ""));
            headers.add(Pair.create("Coalesce", "a"));
            headers.add(Pair.create("Coalesce", ""));
            headers.add(Pair.create("Coalesce", "a"));
            final String url = mWebServer.setResponseWithNotFoundStatus("/404.html", headers);
            loadUrlSync(url);

            XWalkWebResourceRequest request = mOnReceivedResponseHeadersHelper.getRequest();
            assertNotNull(request);
            assertEquals("GET", request.getMethod());
            assertNotNull(request.getRequestHeaders());
            assertFalse(request.getRequestHeaders().isEmpty());
            assertTrue(request.isForMainFrame());
            assertFalse(request.hasGesture());
            XWalkWebResourceResponse response = mOnReceivedResponseHeadersHelper.getResponse();
            assertEquals(404, response.getStatusCode());
            assertEquals("Not Found", response.getReasonPhrase());
            assertEquals("text/html", response.getMimeType());
            assertNotNull(response.getResponseHeaders());
            assertTrue(response.getResponseHeaders().containsKey("Content-Type"));
            assertEquals("text/html; charset=utf-8", response.getResponseHeaders().get("Content-Type"));
            assertTrue(response.getResponseHeaders().containsKey("Coalesce"));
            assertEquals("a, a", response.getResponseHeaders().get("Coalesce"));
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            assertFalse(true);
        }
    }

    @SmallTest
    public void testForSubresource() {
        try {
            OnReceivedResponseHeadersHelper mOnReceivedResponseHeadersHelper = mTestHelperBridge.getOnReceivedResponseHeadersHelper();
            List<Pair<String, String>> headers = new ArrayList<Pair<String, String>>();
            headers.add(Pair.create("Content-Type", "text/html; charset=utf-8"));
            final String imageUrl = mWebServer.setResponseWithNotFoundStatus("/404.png", headers);
            final String pageHtml = CommonResources.makeHtmlPageFrom(
                    "", "<img src='" + imageUrl + "' class='img.big' />");
            final String pageUrl = mWebServer.setResponse("/page.html", pageHtml, null);
            loadUrlSync(pageUrl);

            XWalkWebResourceRequest request = mOnReceivedResponseHeadersHelper.getRequest();
            assertNotNull(request);
            assertEquals("GET", request.getMethod());
            assertNotNull(request.getRequestHeaders());
            assertFalse(request.getRequestHeaders().isEmpty());
            assertFalse(request.isForMainFrame());
            assertFalse(request.hasGesture());
            XWalkWebResourceResponse response = mOnReceivedResponseHeadersHelper.getResponse();
            assertEquals(404, response.getStatusCode());
            assertEquals("Not Found", response.getReasonPhrase());
            assertEquals("text/html", response.getMimeType());
            assertNotNull(response.getResponseHeaders());
            assertTrue(response.getResponseHeaders().containsKey("Content-Type"));
            assertEquals("text/html; charset=utf-8", response.getResponseHeaders().get("Content-Type"));
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            assertFalse(true);
        }
    }

    @SmallTest
    public void testAfterRedirect() {
        try {
            OnReceivedResponseHeadersHelper mOnReceivedResponseHeadersHelper = mTestHelperBridge.getOnReceivedResponseHeadersHelper();
            List<Pair<String, String>> headers = new ArrayList<Pair<String, String>>();
            headers.add(Pair.create("Content-Type", "text/html; charset=utf-8"));
            final String secondUrl = mWebServer.setResponseWithNotFoundStatus("/404.html", headers);
            final String firstUrl = mWebServer.setRedirect("/302.html", secondUrl);

            loadUrlSync(firstUrl);
            XWalkWebResourceRequest request = mOnReceivedResponseHeadersHelper.getRequest();
            assertNotNull(request);
            assertEquals("GET", request.getMethod());
            assertNotNull(request.getRequestHeaders());
            assertFalse(request.getRequestHeaders().isEmpty());
            assertTrue(request.isForMainFrame());
            assertFalse(request.hasGesture());
            XWalkWebResourceResponse response = mOnReceivedResponseHeadersHelper.getResponse();
            assertEquals(404, response.getStatusCode());
            assertEquals("Not Found", response.getReasonPhrase());
            assertEquals("text/html", response.getMimeType());
            assertNotNull(response.getResponseHeaders());
            assertTrue(response.getResponseHeaders().containsKey("Content-Type"));
            assertEquals("text/html; charset=utf-8", response.getResponseHeaders().get("Content-Type"));
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            assertFalse(true);
        }
    }
}