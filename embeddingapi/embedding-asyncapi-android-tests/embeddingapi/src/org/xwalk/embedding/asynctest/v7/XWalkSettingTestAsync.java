package org.xwalk.embedding.asynctest.v7;

import android.test.suitebuilder.annotation.MediumTest;
import android.test.suitebuilder.annotation.SmallTest;

import org.xwalk.core.XWalkSettings;
import org.xwalk.embedding.base.XWalkViewTestBase;

public class XWalkSettingTestAsync extends XWalkViewTestBase {

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

    // Test that the file URL access toggle does not affect assert URLs (file:///android_asset/)
    @SmallTest
    public void testAssetUrl() {
        try {
            // The expectedTitle should be kept same with the title of referenced page.
            final String expectedTitle = "Crosswalk Sample Application";
            final String assetURL = "file:///android_asset/index.html";
            // setAllowFileAccess default: ture
            loadUrlSync(assetURL);
            assertEquals(expectedTitle, getTitleOnUiThread());
            // setAllowFileAccess(false) will not affect assert URLs
            setAllowFileAccess(false);
            loadUrlSync(assetURL);
            assertEquals(expectedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    // Test that the file URL access toggle does not affect resource URLs (file:///android_res/).
    @SmallTest
    public void testResourceUrl() {
        try {
            // The expectedTitle should be kept same with the title of referenced page.
            final String expectedTitle = "Resource File";
            final String resoueceURL = "file:///android_res/raw/resource_file.html";
            // setAllowFileAccess default: ture
            loadUrlSync(resoueceURL);
            assertEquals(expectedTitle, getTitleOnUiThread());
            // setAllowFileAccess(false) will not affect resource URLs
            setAllowFileAccess(false);
            loadUrlSync(resoueceURL);
            assertEquals(expectedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testFileUrlAccessWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsFileUrlAccessTestHelper(
                            views.getView0(), views.getBridge0(), 0),
                    new XWalkSettingsFileUrlAccessTestHelper(
                            views.getView1(), views.getBridge1(), 1));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    // This test verifies that local image resources can be loaded from file:
    // URLs regardless of file access state.
    @SmallTest
    public void testFileAccessFromFilesImage() {
        try {
            final String testFile = "file:///sdcard/device_files/image_access.html";
            final String imageHeight = "145";
            setAllowUniversalAccessFromFileURLs(false);
            setAllowFileAccessFromFileURLs(false);
            loadUrlSync(testFile);
            assertEquals(imageHeight, getTitleOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
    

    @SmallTest
    public void testUniversalAccessFromFilesWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsUniversalAccessFromFilesTestHelper(
                            views.getView0(), views.getBridge0()),
                    new XWalkSettingsUniversalAccessFromFilesTestHelper(
                            views.getView1(), views.getBridge1()));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testFileAccessFromFilesIframeWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsFileAccessFromFilesIframeTestHelper(
                            views.getView0(), views.getBridge0()),
                    new XWalkSettingsFileAccessFromFilesIframeTestHelper(
                            views.getView1(), views.getBridge1()));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testFileAccessFromFilesXhrWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsFileAccessFromFilesXhrTestHelper(
                            views.getView0(), views.getBridge0()),
                    new XWalkSettingsFileAccessFromFilesXhrTestHelper(
                            views.getView1(), views.getBridge1()));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
