// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;

import org.xwalk.core.XWalkNavigationItem;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;


public class NavigationHistoryTest extends XWalkViewTestBase {

    @SmallTest
    public void testSize() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            goBackSync(1);
            assertEquals("2", getSizeOnUiThread());
        }catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testHasItemAt() {
         try {
           final String url1 = "about:blank";
           final String url2 = "file:///android_asset/manifest.json";
           loadUrlSync(url1);
           loadUrlSync(url2);
           goBackSync(1);
           assertEquals("true", hasItemAtOnUiThread());
         }catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetItemAt() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            goBackSync(1);
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    XWalkNavigationItem item = mXWalkView.getNavigationHistory().getItemAt(1);
                    assertNotNull(item);
                    assertEquals(url2, item.getUrl());
                }
            });
        }catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetCurrentItem_withBack() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            goBackSync(1);
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkNavigationItem item = mXWalkView.getNavigationHistory().getCurrentItem();
                    XWalkNavigationItem item1 = mXWalkView.getNavigationHistory().getItemAt(0);
                    assertEquals(item1.getUrl(), item.getUrl());
                }
            });
        }catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetCurrentItem_noBack() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkNavigationItem item = mXWalkView.getNavigationHistory().getCurrentItem();
                    assertEquals(url2, item.getUrl());
                }
            });
        }catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetCurrentIndex() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            final String url3 = "file:///android_asset/p1bar.html";
            loadUrlSync(url1);
            loadUrlSync(url2);
            loadUrlSync(url3);
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    int index = mXWalkView.getNavigationHistory().getCurrentIndex();
                    assertEquals(2, index);
                }
            });
        }catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testCanGoBack()
    {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            assertFalse(canGoBackOnUiThread());
            loadUrlSync(url1);
            assertFalse(canGoBackOnUiThread());
            loadUrlSync(url2);
            assertTrue(canGoBackOnUiThread());
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testCanGoForward() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            assertFalse(canGoForwardOnUiThread());
            loadUrlSync(url1);
            loadUrlSync(url2);
            getUrlOnUiThread();
            assertFalse(canGoForwardOnUiThread());
            goBackSync(1);
            assertTrue(canGoForwardOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testNavigate_backOneStep() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            goBackSync(1);
            assertEquals(url1, getUrlOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
     }

    @SmallTest
    public void testNavigate_forwardOneStep() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            goBackSync(1);
            goForwardSync(1);
            assertEquals(url2, getUrlOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testNavigate_backTwoStep() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            final String url3 = "file:///android_asset/p1bar.html";
            loadUrlSync(url1);
            loadUrlSync(url2);
            loadUrlSync(url3);
            goBackSync(2);
            assertEquals(url1, getUrlOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testNavigate_forwardTwoStep() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            final String url3 = "file:///android_asset/p1bar.html";
            loadUrlSync(url1);
            loadUrlSync(url2);
            loadUrlSync(url3);
            goBackSync(1);
            goBackSync(1);
            goForwardSync(2);
            assertEquals(url3,  getCurrentItemUrlOnUiThread());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }


    @SmallTest
    public void testClear() {
        try {
            final String url1 = "about:blank";
            final String url2 = "file:///android_asset/manifest.json";
            loadUrlSync(url1);
            loadUrlSync(url2);
            goBackSync(1);
            assertEquals(url1, getUrlOnUiThread());
            goForwardSync(1);

            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.getNavigationHistory().clear();
                    XWalkNavigationItem item = mXWalkView.getNavigationHistory().getCurrentItem();
                    int index = mXWalkView.getNavigationHistory().getCurrentIndex();
                    assertEquals(url2, item.getUrl());
                    assertEquals(0,index);
                }
            });
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
