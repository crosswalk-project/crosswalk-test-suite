// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.basic;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;

public class XWalkViewWithOnHideOnShow extends XWalkActivity {
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.xwview_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can hide and show.(Also need to test it in Android TV)\n\n")
        .append("Test  Step:\n\n")
        .append("1. Play the video in the page, then click home key.\n")
        .append("2. Click the 'EmbeddedAPISamples' app again.\n\n")
        .append("Expected Result:\n\n")
        .append("1.Test passes if app video can be paused when clicking home key.")
        .append("2.Test passes if there is no short white screen displayed when clicking home key.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        // The web page below will display a video.
        // When home button is pressed, the activity will be in background, and the video will be paused.
        mXWalkView.load("https://www.w3.org/2010/05/video/mediaevents.html", null);
    }
}
