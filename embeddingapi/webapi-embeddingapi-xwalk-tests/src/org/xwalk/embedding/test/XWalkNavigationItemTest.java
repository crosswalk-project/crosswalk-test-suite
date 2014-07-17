// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkNavigationItemTest extends XWalkViewTestBase {

    public XWalkNavigationItemTest() {
        super(MainActivity.class);
    }

    @SmallTest
    public void testGetNavigationItemUrl() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            String url = getNavigationUrlOnUiThread();
            assertEquals(url2, url);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetNavigationItemOriginalUrl() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            final String url3 = "file:///android_asset/p1bar.html";
            loadUrlSync(url1);
            loadUrlSync(url2);
            loadUrlSync(url3);
            goBackSync(2);
            String url = getNavigationOriginalUrlOnUiThread();
            assertEquals(url3, url);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        } catch (Throwable e) {
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetNavigationItemTitle() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            final String url3 = "file:///android_asset/p1bar.html";
            loadUrlSync(url1);
            loadUrlSync(url2);
            loadUrlSync(url3);
            String title = getNavigationTitleOnUiThread();
            assertEquals("Test", title);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        } catch (Throwable e) {
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetFaviconExist() {
        try {
            assertTrue(false);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        } 
    }
}
