// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

public class XWalkVersionAndAPIVersion extends XWalkActivity {
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can get API version and xwalk version.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app show API version and xwalk version.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        setContentView(R.layout.version_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        String apiVersion = mXWalkView.getAPIVersion();
        String xwalkVersion = mXWalkView.getXWalkVersion();
        TextView text1 = (TextView) super.findViewById(R.id.text1);
        text1.setText("API Version: " + apiVersion + "; XWalk Version: " + xwalkVersion);
        mXWalkView.load("", "");
    }
}