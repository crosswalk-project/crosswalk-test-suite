// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.misc;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.widget.TextView;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;


public class XWalkViewWithOnTouchListener extends XWalkActivity {
    private XWalkView mXWalkView;
    private TextView mTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_on_touch_listener);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mTextView = (TextView) findViewById(R.id.message_tv);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView API OnTouchListener can work.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the message 'onTouchEvent is invoked; Action is UP/DOWN/MOVE' shows");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView.load("http://www.baidu.com/", null);
        mXWalkView.setOnTouchListener(new OnTouchListener() {

            @Override
            public boolean onTouch(View v, MotionEvent event) {
                // TODO Auto-generated method stub
                int action = event.getActionMasked();
                switch (action) {
                case MotionEvent.ACTION_DOWN:
                    mTextView.setText("onTouchEvent is invoked. Action is DOWN");
                    break;
                case MotionEvent.ACTION_MOVE:
                    mTextView.setText("onTouchEvent is invoked. Action is MOVE");
                   break;
                case MotionEvent.ACTION_UP:
                    mTextView.setText("onTouchEvent is invoked. Action is UP");
                    break;
                case MotionEvent.ACTION_CANCEL:
                    mTextView.setText("onTouchEvent is invoked. Action is CANCEL");
                    break;
                case MotionEvent.ACTION_OUTSIDE:
                    mTextView.setText("onTouchEvent is invoked. Action is OUTSIDE");
                    break;
                }
                return false;
            }
        });
    }
}
