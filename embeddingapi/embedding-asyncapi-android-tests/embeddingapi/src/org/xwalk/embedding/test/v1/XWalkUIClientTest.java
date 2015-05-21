// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;

import java.util.concurrent.TimeoutException;

import org.xwalk.core.XWalkUIClient;
import org.xwalk.embedding.base.ExtensionEcho;
import org.xwalk.embedding.base.OnFullscreenToggledHelper;
import org.xwalk.embedding.base.OnJavascriptCloseWindowHelper;
import org.xwalk.embedding.base.OnRequestFocusHelper;
import org.xwalk.embedding.base.OnScaleChangedHelper;
import org.xwalk.embedding.base.OpenFileChooserHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.net.Uri;
import android.test.suitebuilder.annotation.SmallTest;
import android.webkit.ValueCallback;

@SuppressLint("NewApi")
public class XWalkUIClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testOnRequestFocus() {
        try {
            final String url = "file:///android_asset/request_focus_main.html";
            OnRequestFocusHelper mOnRequestFocusHelper = mTestHelperBridge.getOnRequestFocusHelper();
            int count = mOnRequestFocusHelper.getCallCount();
            loadUrlSync(url);
            clickOnElementId("left_frame", "LeftFrame");
            mOnRequestFocusHelper.waitForCallback(count);
            assertTrue(mOnRequestFocusHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnJavascriptCloseWindow() {
        try {
            final String url = "window.close.html";
            OnJavascriptCloseWindowHelper mCloseWindowHelper = mTestHelperBridge.getOnJavascriptCloseWindowHelper();
            int count = mCloseWindowHelper.getCallCount();
            loadAssetFile(url);
            mCloseWindowHelper.waitForCallback(count);
            assertTrue(mCloseWindowHelper.getCalled());
        } catch (InterruptedException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (TimeoutException e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnFullscreenToggled() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    uiClient.onFullscreenToggled(mXWalkView, true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnFullscreenToggled_data() {
        try {
            final String name = "fullscreen_togged.html";
            String fileContent = getFileContent(name);
            OnFullscreenToggledHelper mOnFullscreenToggledHelper = mTestHelperBridge.getOnFullscreenToggledHelper();
            int count = mOnFullscreenToggledHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            clickOnElementId("fullscreen_toggled", null);
            mOnFullscreenToggledHelper.waitForCallback(count);
            assertTrue(mOnFullscreenToggledHelper.getEnterFullscreen());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnFullscreenToggled_url() {
        try {
            String url = "file:///android_asset/fullscreen_togged.html";
            OnFullscreenToggledHelper mOnFullscreenToggledHelper = mTestHelperBridge.getOnFullscreenToggledHelper();
            int count = mOnFullscreenToggledHelper.getCallCount();
            loadUrlSync(url);
            clickOnElementId("fullscreen_toggled", null);
            mOnFullscreenToggledHelper.waitForCallback(count);
            assertTrue(mOnFullscreenToggledHelper.getEnterFullscreen());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOpenFileChooser() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkUIClient uiClient = new XWalkUIClient(mXWalkView);
                    ValueCallback<Uri> uploadFile = new ValueCallback<Uri>() {

                        @Override
                        public void onReceiveValue(Uri arg0) {

                        }

                    };
                    uiClient.openFileChooser(mXWalkView, uploadFile, "", "hello");
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOpenFileChooser_data() {
        try {
            final String name = "file_chooser.html";
            String fileContent = getFileContent(name);
            OpenFileChooserHelper mOpenFileChooserHelper = mTestHelperBridge.getOpenFileChooserHelper();;
            int count = mOpenFileChooserHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            clickOnElementId("upload_input", null);
            mOpenFileChooserHelper.waitForCallback(count);
            assertNotNull(mOpenFileChooserHelper.getCallback());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOpenFileChooser_url() {
        try {
            String url = "file:///android_asset/file_chooser.html";
            OpenFileChooserHelper mOpenFileChooserHelper = mTestHelperBridge.getOpenFileChooserHelper();;
            int count = mOpenFileChooserHelper.getCallCount();
            loadUrlSync(url);
            clickOnElementId("upload_input", null);
            mOpenFileChooserHelper.waitForCallback(count);
            assertNotNull(mOpenFileChooserHelper.getCallback());
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnScaleChanged() {
        try {
            final String name = "scale_changed.html";
            String fileContent = getFileContent(name);
            OnScaleChangedHelper mOnScaleChangedHelper = mTestHelperBridge.getOnScaleChangedHelper();
            int count = mOnScaleChangedHelper.getCallCount();
            loadDataAsync(null, fileContent, "text/html", false);
            mOnScaleChangedHelper.waitForCallback(count);
            assertTrue(Float.compare(mOnScaleChangedHelper.getScale(), 0.0f) > 0);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnJavascriptModalDialog() {
        try {
            String EMPTY_PAGE = "<!doctype html>" +
                    "<title>Modal Dialog Test</title><p>Testcase.</p>";
            loadDataSync(null, EMPTY_PAGE, "text/html", false);
            executeJavaScriptAndWaitForResult("alert('" + ALERT_TEXT + "')");
            assertTrue(callbackCalled.get());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnPageFinished_write() {
        try {
            ExtensionEcho echo = new ExtensionEcho();
            loadUrlSync("file:///android_asset/framesEcho.html");
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
