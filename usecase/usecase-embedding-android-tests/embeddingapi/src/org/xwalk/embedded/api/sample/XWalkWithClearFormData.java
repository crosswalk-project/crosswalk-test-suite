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
import android.widget.Button;

public class XWalkWithClearFormData extends XWalkActivity {
    private XWalkView mXWalkView;
    private Button clearFormData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.animatable_xwview_layout);
        clearFormData = (Button) findViewById(R.id.run_animation);
        clearFormData.setText("ClearFormData");
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
    }

    @Override
    protected void onXWalkReady() {
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

        clearFormData.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
            	mXWalkView.clearFormData();
            }
        });
        mXWalkView.load("file:///android_asset/datalist.html", null);
    }
}
