// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v7;


import org.xwalk.core.XWalkView;
import org.xwalk.embedding.base.OnFindResultReceivedHelper;
import java.util.concurrent.Callable;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkViewTestAsync extends XWalkViewTestBase {

    @Override
    public void setUp() throws Exception {
        super.setUp();
        setFindListener();
    }

    @SmallTest
    public void testFindAllAsync() {
        try {
            String fileContent = getFileContent("find.html");
            loadDataSync(null, fileContent, "text/html", false);
            OnFindResultReceivedHelper mOnFindResultReceivedHelper = mTestHelperBridge.getOnFindResultReceivedHelper();
            findAllSync(mOnFindResultReceivedHelper, FIND_ALL, "Find");
            assertEquals(0, mOnFindResultReceivedHelper.getIndex());
            assertEquals(3, mOnFindResultReceivedHelper.getMatches());
            assertTrue(mOnFindResultReceivedHelper.isDone());
        } catch (Exception e) {
            assertFalse(true);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testFindNext() {
        try {
            String fileContent = getFileContent("find.html");
            loadDataSync(null, fileContent, "text/html", false);
            OnFindResultReceivedHelper mOnFindResultReceivedHelper = mTestHelperBridge.getOnFindResultReceivedHelper();
            findAllSync(mOnFindResultReceivedHelper, FIND_ALL, "Find");
            findNextSync(mOnFindResultReceivedHelper, FIND, true);
            assertEquals(1, mOnFindResultReceivedHelper.getIndex());
            assertEquals(3, mOnFindResultReceivedHelper.getMatches());
            assertTrue(mOnFindResultReceivedHelper.isDone());
        } catch (Exception e) {
            assertFalse(true);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetContentHeightWithLocalUrl() {
        try {
            String url = "file:///android_asset/index.html";
            loadUrlSync(url);
            boolean result = pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mXWalkView.getContentHeight() != 0;
                }
            });
            assertTrue(result);
        } catch (Throwable e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testFindPrevious() {
        try {
            String fileContent = getFileContent("find.html");
            loadDataSync(null, fileContent, "text/html", false);
            OnFindResultReceivedHelper mOnFindResultReceivedHelper = mTestHelperBridge.getOnFindResultReceivedHelper();
            findAllSync(mOnFindResultReceivedHelper, FIND_ALL, "Find");
            findNextSync(mOnFindResultReceivedHelper, FIND, false);
            findNextSync(mOnFindResultReceivedHelper, FIND, false);
            assertEquals(1, mOnFindResultReceivedHelper.getIndex());
            assertEquals(3, mOnFindResultReceivedHelper.getMatches());
            assertTrue(mOnFindResultReceivedHelper.isDone());
        } catch (Exception e) {
            assertFalse(true);
            e.printStackTrace();
        }
    }

    public void testGetContentHeightWithRemoteUrl() {
        try {
            String url = "https://www.baidu.com";
            loadUrlSync(url);
            boolean result = pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mXWalkView.getContentHeight() != 0;
                }
            });
            assertTrue(result);
        } catch (Throwable e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testRemoveJavascriptInterface() {
        try {
            final String name = "add_js_interface.html";
            addJavascriptInterface();
            loadAssetFile(name);
            assertEquals(mExpectedStr, getTitleOnUiThread());
            removeJavascriptInterface();
            reloadSync(XWalkView.RELOAD_NORMAL);
            assertEquals(mDefaultTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testRemoveJavascriptInterfaceWithUrl() {
        try {
            final String url = "file:///android_asset/add_js_interface.html";
            addJavascriptInterface();
            loadUrlSync(url);
            assertEquals(mExpectedStr, getTitleOnUiThread());
            removeJavascriptInterface();
            reloadSync(XWalkView.RELOAD_NORMAL);
            assertEquals(mDefaultTitle, getTitleOnUiThread());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testRemoveJavascriptInterfaceWithAnnotation() {
        try {
            final String name = "index.html";
            final String xwalkStr = "\"xwalk\"";
            String result;
            addJavascriptInterface();
            loadAssetFile(name);

            result = executeJavaScriptAndWaitForResult("testInterface.getText()");
            assertEquals(xwalkStr, result);

            raisesExceptionAndSetTitle("testInterface.getTextWithoutAnnotation()");
            String title = getTitleOnUiThread();
            assertEquals(mExpectedStr, title);

            removeJavascriptInterface();
            reloadSync(XWalkView.RELOAD_NORMAL);

            result = executeJavaScriptAndWaitForResult("testInterface.getText()");
            assertEquals("null", result);

            raisesExceptionAndSetTitle("testInterface.getTextWithoutAnnotation()");
            title = getTitleOnUiThread();
            assertEquals("error", title);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetCompositingSurfaceTypeSurface() {
        try {
            assertEquals(SURFACE_VIEW, getBackendTypeOnUiThread(mXWalkView));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetCompositingSurfaceTypeTexture() {
        try {
            assertEquals(TEXTURE_VIEW, getBackendTypeOnUiThread(mXWalkViewTexture));
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
