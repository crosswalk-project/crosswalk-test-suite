// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import org.xwalk.core.XWalkNavigationHistory;
import org.xwalk.core.XWalkView;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class LoadTest extends XWalkViewTestBase {

    public LoadTest() {
        super(MainActivity.class);
    }

    @SmallTest
    public void testLoadUrl()
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
    public void testLoadAppFromManifest()
    {
        try {
            String path = "file:///android_asset/";
            String name = "manifest.json";
            String url = "file:///android_asset/index.html";
            loadFromManifestSync(path, name);
            assertEquals(url, getUrlOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testReload_ignoreCache() {
        try {
            String url = "file:///android_asset/p1bar.html";
            loadUrlSync(url);
            reloadSync(XWalkView.RELOAD_IGNORE_CACHE);
            assertEquals("Test", getTitleOnUiThread());
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
            String url = "file:///android_asset/p1bar.html";
            loadUrlSync(url);
            reloadSync(XWalkView.RELOAD_NORMAL);
            assertEquals("Test", getTitleOnUiThread());

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
            String originalUrl = "file:///android_asset/p2bar.html";
            String url = "file:///android_asset/p1bar.html";
            loadUrlSync(originalUrl);
            loadUrlSync(url);
            assertEquals(originalUrl, getOriginalUrlOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
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
            String url = "file:///android_asset/p2bar.html";
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
            clickOnElementId_changeTitle("AJAX_Read");
            assertEquals(changedTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
