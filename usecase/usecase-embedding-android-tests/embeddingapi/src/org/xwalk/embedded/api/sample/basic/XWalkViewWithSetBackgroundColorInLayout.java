// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.basic;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.LinearLayout;

public class XWalkViewWithSetBackgroundColorInLayout extends XWalkActivity {
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.container);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can set background color without delay.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load the red without flicker.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.xwview_backgroundcolor_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mXWalkView.load("file:///android_asset/index4995_local_text.html", null);
    }

}
