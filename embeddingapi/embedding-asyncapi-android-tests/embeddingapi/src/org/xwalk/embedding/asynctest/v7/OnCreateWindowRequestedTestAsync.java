// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.asynctest.v7;

import android.test.suitebuilder.annotation.SmallTest;
import android.util.Log;
import android.webkit.ValueCallback;

import org.chromium.base.test.util.Feature;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;
import org.xwalk.embedding.base.OnCreateWindowRequestedHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

/**
 * Test suite for OnCreateWindowRequested().
 */
public class OnCreateWindowRequestedTestAsync extends XWalkViewTestBase {
    private OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper;
    
    @Override
    public void setUp() throws Exception {
        super.setUp();

        mOnCreateWindowRequestedHelper = mTestHelperBridge.getOnCreateWindowRequestedHelper();
        XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, true);

        setUIClient(new XWalkUIClient(getXWalkView()){
            @Override
            public boolean onCreateWindowRequested(XWalkView view, InitiateBy initiator,
                    ValueCallback<XWalkView> callback) {
                Log.d("XWalkView", "onCreateWindowRequested: " + initiator);
                XWalkView newView = new XWalkView(getActivity(), getActivity());

                callback.onReceiveValue(newView);
                mOnCreateWindowRequestedHelper.notifyCalled(newView);
                return true;
            }

        });
    }

    @SmallTest
    @Feature({"OnCreateWindowRequested"})
    public void testOnCreateWindowRequestedByPreference() {
        try {
            String fileContent = getFileContent("create_window_1.html");
            int count = mOnCreateWindowRequestedHelper.getCallCount();

            loadDataAsync(null, fileContent, "text/html", false);
            clickOnElementId("new_window", null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertNotNull(mOnCreateWindowRequestedHelper.getXWalkView());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    @Feature({"OnCreateWindowRequested"})
    public void testOnCreateWindowRequestedByAPI() {
        try {
            String fileContent = getFileContent("create_window_1.html");
            int count = mOnCreateWindowRequestedHelper.getCallCount();

            setSupportMultipleWindows(false);
            setJavaScriptCanOpenWindowsAutomatically(false);
            loadDataAsync(null, fileContent, "text/html", false);
            clickOnElementId("new_window", null);
            assertNull(mOnCreateWindowRequestedHelper.getXWalkView());

            setSupportMultipleWindows(true);
            setJavaScriptCanOpenWindowsAutomatically(true);
            loadDataAsync(null, fileContent, "text/html", false);
            clickOnElementId("new_window", null);
            mOnCreateWindowRequestedHelper.waitForCallback(count);
            assertNotNull(mOnCreateWindowRequestedHelper.getXWalkView());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
