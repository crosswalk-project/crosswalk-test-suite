package org.xwalk.embedding.test.v7;

import android.test.suitebuilder.annotation.MediumTest;
import android.test.suitebuilder.annotation.SmallTest;

import org.xwalk.core.XWalkSettings;
import org.xwalk.embedding.base.XWalkViewTestBase;

public class XWalkSettingTest extends XWalkViewTestBase {

    @SmallTest
    public void testLoadWithOverviewModeWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView0(), views.getBridge0(), false),
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView1(), views.getBridge1(), false));

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testLoadWithOverviewModeViewportTagWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView0(), views.getBridge0(), true),
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView1(), views.getBridge1(), true));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @MediumTest
    public void testCacheMode() {
        try {
            final String htmlPath = "/testCacheMode.html";
            final String url = mWebServer.setResponse(htmlPath, "response", null);
            final String htmlNotInCachePath = "/testCacheMode-not-in-cache.html";
            final String urlNotInCache = mWebServer.setResponse(htmlNotInCachePath, "", null);

            clearCacheOnUiThread(true);
            assertEquals(XWalkSettings.LOAD_DEFAULT, getCacheMode());

            setCacheMode(XWalkSettings.LOAD_CACHE_ELSE_NETWORK);
            loadUrlSync(url);
            assertEquals(1, mWebServer.getRequestCount(htmlPath));
            loadUrlSync(url);
            assertEquals(1, mWebServer.getRequestCount(htmlPath));

            setCacheMode(XWalkSettings.LOAD_NO_CACHE);
            loadUrlSync(url);
            assertEquals(2, mWebServer.getRequestCount(htmlPath));
            loadUrlSync(url);
            assertEquals(3, mWebServer.getRequestCount(htmlPath));

            setCacheMode(XWalkSettings.LOAD_CACHE_ONLY);
            loadUrlSync(url);
            assertEquals(3, mWebServer.getRequestCount(htmlPath));
            loadUrlSync(url);
            assertEquals(3, mWebServer.getRequestCount(htmlPath));

            loadUrlSyncAndExpectError(urlNotInCache);
            assertEquals(0, mWebServer.getRequestCount(htmlNotInCachePath));

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @MediumTest
    public void testCacheModeWithBlockedNetworkLoads() {
        try {
            final String htmlPath = "/testCacheModeWithBlockedNetworkLoads.html";
            final String url = mWebServer.setResponse(htmlPath, "response", null);

            clearCacheOnUiThread(true);
            assertEquals(XWalkSettings.LOAD_DEFAULT, getCacheMode());

            setBlockNetworkLoads(true);
            loadUrlSyncAndExpectError(url);
            assertEquals(0, mWebServer.getRequestCount(htmlPath));

            setCacheMode(XWalkSettings.LOAD_CACHE_ELSE_NETWORK);
            loadUrlSyncAndExpectError(url);
            assertEquals(0, mWebServer.getRequestCount(htmlPath));

            setCacheMode(XWalkSettings.LOAD_NO_CACHE);
            loadUrlSyncAndExpectError(url);
            assertEquals(0, mWebServer.getRequestCount(htmlPath));

            setCacheMode(XWalkSettings.LOAD_CACHE_ONLY);
            loadUrlSyncAndExpectError(url);
            assertEquals(0, mWebServer.getRequestCount(htmlPath));

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
