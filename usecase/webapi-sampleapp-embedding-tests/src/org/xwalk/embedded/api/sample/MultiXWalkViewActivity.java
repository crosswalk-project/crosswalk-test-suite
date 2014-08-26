// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.LinearLayout;

public class MultiXWalkViewActivity extends XWalkBaseActivity {

    private XWalkView mXWalkView2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can create multi instance.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load 'intel.com' and 'baidu.com'.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        
        setContentView(R.layout.container);
        LinearLayout parent = (LinearLayout) findViewById(R.id.container);

        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.MATCH_PARENT);
        params.weight = 1;

        mXWalkView = new XWalkView(this, this);
        parent.addView(mXWalkView, params);

        mXWalkView2 = new XWalkView(this, this);
        parent.addView(mXWalkView2, params);

        mXWalkView.load("http://www.intel.com", null);
        mXWalkView2.load("http://www.baidu.com", null);
    }

    @Override
    public void onPause() {
        super.onPause();
        if (mXWalkView2 != null) {
            mXWalkView2.onHide();
            mXWalkView2.pauseTimers();
        }
    }

    @Override
    public void onResume() {
        super.onResume();
        if (mXWalkView2 != null) {
            mXWalkView2.onShow();
            mXWalkView2.resumeTimers();
        }
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        if (mXWalkView2 != null) {
            mXWalkView2.onDestroy();
        }
    }
}
