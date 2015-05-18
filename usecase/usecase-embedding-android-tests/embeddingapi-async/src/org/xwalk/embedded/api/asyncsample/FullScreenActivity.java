// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class FullScreenActivity extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        XWalkInitializer.initAsync(this, this);
    }

    @Override
    public final void onXWalkInitStarted() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitCancelled() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitFailed() {
        // Do crash or logging or anything else in order to let the tester know if this method get called
    }

    @Override
    public final void onXWalkInitCompleted() {
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