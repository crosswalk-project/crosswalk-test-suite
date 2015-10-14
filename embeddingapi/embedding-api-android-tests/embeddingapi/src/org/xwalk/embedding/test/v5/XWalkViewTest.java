// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.concurrent.Callable;

import android.graphics.Color;
import android.graphics.Point;

import org.apache.http.Header;
import org.apache.http.HttpRequest;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.content.Context;
import android.test.suitebuilder.annotation.SmallTest;
import android.test.suitebuilder.annotation.MediumTest;
import android.util.Pair;
import android.view.WindowManager;

@SuppressLint("NewApi")
public class XWalkViewTest extends XWalkViewTestBase {

    @SmallTest
    public void testSetUserAgentString() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    mXWalkView.setUserAgentString(USER_AGENT);
                }
            });
            loadDataSync(null, EMPTY_PAGE, "text/html", false);
            String result = executeJavaScriptAndWaitForResult("navigator.userAgent;");
            assertEquals(EXPECTED_USER_AGENT, result);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    
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
    
    @MediumTest
    public void testUserAgentWithTestServer() throws Throwable {
        final String customUserAgentString = "testUserAgentWithTestServerUserAgent";

        String fileName = null;
        try {
            final String httpPath = "/testUserAgentWithTestServer.html";
            final String url = mWebServer.setResponse(httpPath, "foo", null);

            setUserAgent(customUserAgentString);
            loadUrlSync(url);

            assertEquals(1, mWebServer.getRequestCount(httpPath));
            HttpRequest request = mWebServer.getLastRequest(httpPath);
            Header[] matchingHeaders  = request.getHeaders("User-Agent");
            assertEquals(1, matchingHeaders.length);

            Header header = matchingHeaders[0];
            assertEquals(customUserAgentString, header.getValue());
            assertEquals(customUserAgentString, getUserAgent());
        } finally {
        }
    }    

    @SmallTest
    public void testSetZOrderOnTop_True() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.setZOrderOnTop(true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetZOrderOnTop_False() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.setZOrderOnTop(false);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    @SmallTest
    public void testSetBackgroundColor_Color() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setBackgroundColor(Color.RED);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetBackgroundColor_Value() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setBackgroundColor(Color.parseColor("#00FF00"));
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    @SmallTest
    public void testSetBackgroundColor_Transparent() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setBackgroundColor(0);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    @SmallTest
    public void testSetXWalkViewTransparent() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setZOrderOnTop(true);
                	mXWalkView.setBackgroundColor(0);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnCanZoomInAndOut() {
        try {
        	final float mPageMinimumScale = 0.5f;
        	String url = "file:///android_asset/zoom.html";
        	assertFalse("Should not be able to zoom in", canZoomInOnUiThread());
        	loadUrlSync(url);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getNewScale();
                }
            });
            assertTrue("Should be able to zoom in", canZoomInOnUiThread());
            assertFalse("Should not be able to zoom out", canZoomOutOnUiThread());

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
			// TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
		}
    }
    
    @SmallTest
    public void testOnZoomByLimited() {
        try {
        	final float MAXIMUM_SCALE = 2.0f;
        	final float mPageMinimumScale = 0.5f;
        	String url = "file:///android_asset/zoom.html";
        	assertFalse("Should not be able to zoom in", canZoomInOnUiThread());
        	loadUrlSync(url);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getNewScale();
                }
            });
            
            zoomByOnUiThreadAndWait(4.0f);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return MAXIMUM_SCALE == mTestHelperBridge.getOnScaleChangedHelper().getNewScale();
                }
            });
            
            zoomByOnUiThreadAndWait(0.5f);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return MAXIMUM_SCALE * 0.5f == mTestHelperBridge.getOnScaleChangedHelper().getNewScale();
                }
            });

            zoomByOnUiThreadAndWait(0.01f);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getNewScale();
                }
            });
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
			// TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
		}
    }
    
    @SmallTest
    public void testOnZoomInAndOut() {
        try {
        	final float mPageMinimumScale = 0.5f;
        	String url = "file:///android_asset/zoom.html";
        	assertFalse("Should not be able to zoom in", canZoomInOnUiThread());
        	loadUrlSync(url);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getNewScale();
                }
            });

            while (canZoomInOnUiThread()) {
                zoomInOnUiThreadAndWait();
            }
            assertTrue("Should be able to zoom out", canZoomOutOnUiThread());

            while (canZoomOutOnUiThread()) {
                zoomOutOnUiThreadAndWait();
            }
            assertTrue("Should be able to zoom in", canZoomInOnUiThread());
            
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
			// TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
		}
    }

    @SmallTest
    public void testSetAcceptLanuages() throws Throwable {
        String result;
        final String script = "navigator.languages";
        final String[] languages = {"en;q=0.7", "zh-cn", "da,en-gb;q=0.8,en;q=0.7"};
        final String[] expectedLanguages = {"[\"en;q=0.7\"]", "[\"zh-cn\"]", "[\"da\",\"en-gb;q=0.8\",\"en;q=0.7\"]"};

        result = executeJavaScriptAndWaitForResult(script);
        assertNotNull(result);

        for (int i = 0; i < languages.length; i++) {
            setAcceptLanguages(languages[i]);
            result = executeJavaScriptAndWaitForResult(script);
            assertEquals(expectedLanguages[i], result);
        }
    }
    
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
    
    @SmallTest
    public void testClearCacheForSingleFile() throws Throwable {
        final String pagePath = "/clear_cache_test.html";
        final String otherPagePath = "/clear_other_cache_test.html";
        List<Pair<String, String>> headers = new ArrayList<Pair<String, String>>();
        // Set Cache-Control headers to cache this request. One century should be long enough.
        headers.add(Pair.create("Cache-Control", "max-age=3153600000"));
        headers.add(Pair.create("Last-Modified", "Mon, 12 May 2014 00:00:00 GMT"));
        final String pageUrl = mWebServer.setResponse(
                pagePath, "<html><body>foo</body></html>", headers);
        final String otherPageUrl = mWebServer.setResponse(
                otherPagePath, "<html><body>foo</body></html>", headers);

        // First load to populate cache.
        clearSingleCacheOnUiThread(pageUrl);
        loadUrlSync(pageUrl);
        assertEquals(1, mWebServer.getRequestCount(pagePath));

        // Load about:blank so next load is not treated as reload by XWalkView and force
        // revalidate with the server.
        loadUrlSync("about:blank");

        // No clearCache call, so should be loaded from cache.
        loadUrlSync(pageUrl);
        assertEquals(1, mWebServer.getRequestCount(pagePath));

        loadUrlSync(otherPageUrl);
        assertEquals(1, mWebServer.getRequestCount(otherPagePath));

        // Same as above.
        loadUrlSync("about:blank");

        // Clear cache, so should hit server again.
        clearSingleCacheOnUiThread(pageUrl);
        loadUrlSync(pageUrl);
        assertEquals(2, mWebServer.getRequestCount(pagePath));

        // otherPageUrl was not cleared, so should be loaded from cache.
        loadUrlSync(otherPageUrl);
        assertEquals(1, mWebServer.getRequestCount(otherPagePath));

        // Same as above.
        loadUrlSync("about:blank");

        // Do not clear cache, so should be loaded from cache.
        clearCacheOnUiThread(false);
        loadUrlSync(pageUrl);
        assertEquals(2, mWebServer.getRequestCount(pagePath));
    }        
}
