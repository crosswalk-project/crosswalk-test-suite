// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;

public class XWalkPreferencesActivity extends XWalkActivity {
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can set style value.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load 'baidu.com' page.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        setContentView(R.layout.xwview_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        // Enable remote debugging.
        // You can debug the web content via PC chrome.
        XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
        XWalkPreferences.setValue(XWalkPreferences.JAVASCRIPT_CAN_OPEN_WINDOW, true);
        XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, 3);
        XWalkPreferences.setValue(XWalkPreferences.ALLOW_UNIVERSAL_ACCESS_FROM_FILE, "testSetValue_String");
        XWalkPreferences.getBooleanValue(XWalkPreferences.REMOTE_DEBUGGING);
        XWalkPreferences.getBooleanValue(XWalkPreferences.JAVASCRIPT_CAN_OPEN_WINDOW);
        XWalkPreferences.getIntegerValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS);
        XWalkPreferences.getStringValue(XWalkPreferences.ALLOW_UNIVERSAL_ACCESS_FROM_FILE);
        mXWalkView.load("http://www.baidu.com/", null);
    }
}
