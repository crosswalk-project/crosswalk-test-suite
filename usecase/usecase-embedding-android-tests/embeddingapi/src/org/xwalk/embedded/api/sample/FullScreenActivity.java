// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class FullScreenActivity extends XWalkActivity {
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can enter and exit fullscreen.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the page view enter and exit fullscreen correctly.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm", null)
        .show();
        setContentView(R.layout.xwview_fullscreen);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview_fullscreen);
        Button leaveFullScreenBtn = (Button) findViewById(R.id.leave_fullscreen);
        leaveFullScreenBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View arg0) {
                mXWalkView.leaveFullscreen();
            }
        });
        mXWalkView.load("file:///android_asset/fullscreen_enter_exit.html", null);
    }
}