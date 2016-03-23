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

public class XWalkViewWithSetBackgroundColor extends XWalkActivity {
    private XWalkView mXWalkView;
    private XWalkView mXWalkView2;

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

        LinearLayout parent = (LinearLayout) findViewById(R.id.container);

        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.MATCH_PARENT);
        params.weight = 1;

        mXWalkView = new XWalkView(this, this);
        parent.addView(mXWalkView, params);

        mXWalkView2 = new XWalkView(this, this);
        parent.addView(mXWalkView2, params);

        mXWalkView.setBackgroundColor(Color.RED);
        mXWalkView2.setBackgroundColor(Color.RED);
        mXWalkView.load("file:///android_asset/index4995_local_text.html", null);
        mXWalkView2.load("file:///android_asset/index4995_local_webgl.html", null);
    }

}
