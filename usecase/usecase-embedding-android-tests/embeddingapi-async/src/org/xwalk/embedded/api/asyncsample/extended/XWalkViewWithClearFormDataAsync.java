// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.extended;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class XWalkViewWithClearFormDataAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private Button clearFormData;
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
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can clear form data.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Input a 'h' on the edit text.\n\n")
        .append("2. Then the pull-down list will show.\n\n")
        .append("3. Click the 'clearFormData' button.\n\n")
        .append("4. Then the pull-down list will disappear.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the pull-down list will disappear.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.animatable_xwview_layout);
        clearFormData = (Button) findViewById(R.id.run_animation);
        clearFormData.setText("ClearFormData");
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        clearFormData.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
            	mXWalkView.clearFormData();
            }
        });
        mXWalkView.load("file:///android_asset/datalist.html", null);
    }
}
