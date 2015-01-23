// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageButton;

public class PauseTimersActivity extends XWalkActivity {
    private XWalkView mXWalkView;
    private ImageButton mButton;
    private boolean isPaused;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can pause timers.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click pause button.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app pause time.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        setContentView(R.layout.pause_timers_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        isPaused = false;
        mButton = (ImageButton) findViewById(R.id.pause);
        mButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                if (mXWalkView != null) {
                    if (!isPaused) {
                        // Pause JS timer
                        mXWalkView.pauseTimers();
                        isPaused = true;
                        mButton.setImageResource(android.R.drawable.ic_media_play);
                    } else {
                        // Resume JS timer
                        mXWalkView.resumeTimers();
                        isPaused = false;
                        mButton.setImageResource(android.R.drawable.ic_media_pause);
                    }
                }
            }
        });
        mXWalkView.load("file:///android_asset/pause_timers.html", null);
    }
}
