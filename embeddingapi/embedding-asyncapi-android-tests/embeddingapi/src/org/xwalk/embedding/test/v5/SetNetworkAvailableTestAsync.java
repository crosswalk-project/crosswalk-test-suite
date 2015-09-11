// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;


import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;


@SuppressLint("NewApi")
public class SetNetworkAvailableTestAsync extends XWalkViewTestBase {

    @SmallTest
    public void testSetNetworkAvailable() throws Throwable {

        final String code = "navigator.onLine";
        loadAssetFile("navigator.online.html");
        String title = getTitleOnUiThread();

        if ("true".equals(title)) {
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    // Forcing to trigger 'offline' event.
                	mXWalkView.setNetworkAvailable(false);
                }
            });

            /**
             * Expectations:
             * 1. navigator.onLine is false;
             * 2. window.onoffline event is fired.
             */
            assertEquals("false", executeJavaScriptAndWaitForResult(code));
            assertEquals("offline:false", getTitleOnUiThread());

            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    // Forcing to trigger 'online' event.
                	mXWalkView.setNetworkAvailable(true);
                }
            });

            /**
             * Expectations:
             * 1. navigator.onLine is true;
             * 2. window.ononline event is fired.
             */
            assertEquals("true", executeJavaScriptAndWaitForResult(code));
            assertEquals("online:true", getTitleOnUiThread());
        }

        if ("false".equals(title)) {
             getInstrumentation().runOnMainSync(new Runnable() {
                 @Override
                 public void run() {
                     // Forcing to trigger 'online' event.
                	 mXWalkView.setNetworkAvailable(true);
                 }
             });

            /**
             * Expectations:
             * 1. navigator.onLine is true;
             * 2. window.ononline event is fired.
             */
            assertEquals("true", executeJavaScriptAndWaitForResult(code));
            assertEquals("online:true", getTitleOnUiThread());

            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    // Forcing to trigger 'offline' event.
                	mXWalkView.setNetworkAvailable(false);
                }
            });

            /**
             * Expectations:
             * 1. navigator.onLine is false;
             * 2. window.onoffline event is fired.
             */
            assertEquals("false", executeJavaScriptAndWaitForResult(code));
            assertEquals("offline:false", getTitleOnUiThread());
        }
    }
    
}
