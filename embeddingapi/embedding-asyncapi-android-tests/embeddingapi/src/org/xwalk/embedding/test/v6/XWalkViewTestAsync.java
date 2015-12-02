// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v6;


import java.util.Locale;

import android.graphics.Point;

import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.content.Context;
import android.test.suitebuilder.annotation.SmallTest;
import android.test.suitebuilder.annotation.MediumTest;
import android.view.WindowManager;
import android.util.Pair;

@SuppressLint("NewApi")
public class XWalkViewTestAsync extends XWalkViewTestBase {

    @SmallTest
    public void testUserAgent() throws Throwable {
        final String USER_AGENT = "Chrome/44.0.2403.81 Crosswalk/15.44.376.0 Mobile Safari/537.36";
        final String defaultUserAgentString = getUserAgent();

        // Check that an attempt to set the default UA string to null or "" has no effect.
        setUserAgent(null);
        assertEquals(defaultUserAgentString, getUserAgent());
        setUserAgent("");
        assertEquals(defaultUserAgentString, getUserAgent());

        // Set a custom UA string, verify that it can be reset back to default.
        setUserAgent(USER_AGENT);
        assertEquals(USER_AGENT, getUserAgent());
        setUserAgent(null);
        assertEquals(defaultUserAgentString, getUserAgent());
    }

    // @MediumTest
    // public void testUserAgentWithTestServer() throws Throwable {
    //     final String customUserAgentString = "testUserAgentWithTestServerUserAgent";

    //     String fileName = null;
    //     try {
    //         final String httpPath = "/testUserAgentWithTestServer.html";
    //         final String url = mWebServer.setResponse(httpPath, "foo", null);

    //         setUserAgent(customUserAgentString);
    //         loadUrlSync(url);

    //         assertEquals(1, mWebServer.getRequestCount(httpPath));
    //         HttpRequest request = mWebServer.getLastRequest(httpPath);
    //         Header[] matchingHeaders  = request.getHeaders("User-Agent");
    //         assertEquals(1, matchingHeaders.length);

    //         Header header = matchingHeaders[0];
    //         assertEquals(customUserAgentString, header.getValue());
    //         assertEquals(customUserAgentString, getUserAgent());
    //     } finally {
    //     }
    // }

    @SmallTest
    public void testSetInitialScale1() throws Throwable {

        final String pageTemplate = "<html><head>"
                + "<meta name='viewport' content='initial-scale=%d' />"
                + "</head><body>"
                + "<div style='width:10000px;height:200px'>A big div</div>"
                + "</body></html>";
        final int initialScale4 = 4;
        final int initialScale1 = 1;
        final String pageScale4 = String.format((Locale) null, pageTemplate, initialScale4);
        final String page = String.format((Locale) null, pageTemplate, initialScale1);
        final double dipScale = getDipScale();

        // Page scale updates are asynchronous. There is an issue that we can't
        // reliably check, whether the scale as NOT changed (i.e. remains to be 1.0).
        // So we first change the scale to some non-default value, and then wait
        // until it gets back to 1.0.
        int onScaleChangedCallCount = mTestHelperBridge.getOnScaleChangedHelper().getCallCount();
        loadDataSync(null, pageScale4, "text/html", false);
        mTestHelperBridge.getOnScaleChangedHelper().waitForCallback(onScaleChangedCallCount);
        assertEquals(4.0f, getScaleFactor());

        // The following call to set initial scale will be ignored. However, a temporary
        // page scale change may occur, and this makes the usual onScaleChanged-based workflow
        // flaky. So instead, we are just polling the scale until it becomes 1.0.
        setInitialScale(50);
        loadDataSync(null, page, "text/html", false);
        ensureScaleBecomes(1.0f);
    }

    @SmallTest
    public void testSetInitialScale2() throws Throwable {

        WindowManager wm = (WindowManager) getInstrumentation().getTargetContext()
                .getSystemService(Context.WINDOW_SERVICE);
        Point screenSize = new Point();
        wm.getDefaultDisplay().getSize(screenSize);
        // Make sure after 50% scale, page width still larger than screen.
        int height = screenSize.y * 2 + 1;
        int width = screenSize.x * 2 + 1;
        final String page = "<html><body>"
                + "<p style='height:" + height + "px;width:" + width + "px'>"
                + "testSetInitialScale</p></body></html>";
        final float defaultScaleFactor = 0;
        final float defaultScale = 0.5f;

        assertEquals(defaultScaleFactor, getScaleFactor(), .01f);
        loadDataSync(null, page, "text/html", false);
        assertEquals(defaultScaleFactor, getScaleFactor(), .01f);

        int onScaleChangedCallCount = mTestHelperBridge.getOnScaleChangedHelper().getCallCount();
        setInitialScale(50);
        loadDataSync(null, page, "text/html", false);
        mTestHelperBridge.getOnScaleChangedHelper().waitForCallback(onScaleChangedCallCount);
        assertEquals(0.5f, getPixelScale(), .01f);

        onScaleChangedCallCount = mTestHelperBridge.getOnScaleChangedHelper().getCallCount();
        setInitialScale(500);
        loadDataSync(null, page, "text/html", false);
        mTestHelperBridge.getOnScaleChangedHelper().waitForCallback(onScaleChangedCallCount);
        assertEquals(5.0f, getPixelScale(), .01f);

        onScaleChangedCallCount = mTestHelperBridge.getOnScaleChangedHelper().getCallCount();
        // default min-scale will be used.
        setInitialScale(0);
        loadDataSync(null, page, "text/html", false);
        mTestHelperBridge.getOnScaleChangedHelper().waitForCallback(onScaleChangedCallCount);
        assertEquals(defaultScale, getPixelScale(), .01f);
    }
}
