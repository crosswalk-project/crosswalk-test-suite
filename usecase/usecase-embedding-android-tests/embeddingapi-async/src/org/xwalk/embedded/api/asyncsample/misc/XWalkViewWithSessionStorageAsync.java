// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.misc;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class XWalkViewWithSessionStorageAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private Button mRestoreBtn;
    private Bundle mStoredBundle;
    private XWalkInitializer mXWalkInitializer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
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
        setContentView(R.layout.activity_xwalk_view_with_session_storage_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can restore html5 sessionStorage value when screen rotates.\n\n")
        .append("Test  Step:\n")
        .append("1. Turn on android system auto rotate setting.\n")
        .append("2. Load the page and you get 'myname: null'.\n")
        .append("3. Rotate the screen and click the button.\n")
        .append("4. The 'myname: ' value should be changed to 'jack'.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if sessionStorage value changed to 'jack' when screen rotates.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mRestoreBtn = (Button) findViewById(R.id.restore_btn);
        mRestoreBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (mXWalkView != null) {
                    mXWalkView.restoreState(mStoredBundle);
                }
            }
        });
        mXWalkView.load("file:///android_asset/session_storage_test.html", null);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        // TODO Auto-generated method stub
        super.onRestoreInstanceState(savedInstanceState);
        mStoredBundle = savedInstanceState;
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        // TODO Auto-generated method stub
        super.onSaveInstanceState(outState);
        if (mXWalkView != null) {
            mXWalkView.saveState(outState);
        }
    }
}