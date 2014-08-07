// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import org.chromium.base.test.util.Feature;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.ExtensionEcho;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.os.SystemClock;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class ExtensionEchoTest extends XWalkViewTestBase {
	private final static String PASS_STRING = "Pass";

    public ExtensionEchoTest() {
        super(MainActivity.class);
    }

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testOnMessage() throws Throwable {
        ExtensionEcho echo = new ExtensionEcho();
    
        loadAssetFileAndWaitForTitle("echo.html");
        assertEquals(PASS_STRING, getTitleOnUiThread());
    }

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testOnSyncMessage() throws Throwable {
        ExtensionEcho echo = new ExtensionEcho();

        loadAssetFile("echoSync.html");
        assertEquals(PASS_STRING, getTitleOnUiThread());
    }

    @SmallTest
    @Feature({"ExtensionEcho"})
    public void testMultiFrames() throws Throwable {
        ExtensionEcho echo = new ExtensionEcho();

        loadAssetFileAndWaitForTitle("framesEcho.html");
        assertEquals(PASS_STRING, getTitleOnUiThread());
    }
}
