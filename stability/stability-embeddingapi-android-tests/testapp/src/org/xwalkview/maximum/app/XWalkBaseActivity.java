// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.maximum.app;

import org.xwalk.core.XWalkView;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class XWalkBaseActivity extends Activity {
    protected XWalkView mXWalkView;
    protected Button mDetailInfoButton;
    protected StringBuffer message;
    protected TextView textDes;

    protected int view_num = 0;
    protected int count_num = 0;
    protected int change_num = 0;
    protected RelativeLayout root;
    protected RelativeLayout view_root;
    protected Button mAddViewsButton;
    protected Button mDestoryViewsButton;
    protected Button mExitViewsButton;
    protected TextView textResultTextView;
    protected EditText views_num_text;
    
    protected void showDetailInfo(final Context context) {
        mDetailInfoButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new  AlertDialog.Builder(context)
                .setTitle("Info" )
                .setMessage(message.toString())
                .setPositiveButton("confirm" ,  null )
                .show();
            }
        });
    }

}
