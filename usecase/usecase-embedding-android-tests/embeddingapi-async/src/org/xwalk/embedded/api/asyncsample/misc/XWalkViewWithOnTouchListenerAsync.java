// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.misc;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

import android.widget.TextView;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;


public class XWalkViewWithOnTouchListenerAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private TextView mTextView;
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
        setContentView(R.layout.activity_xwalk_view_with_on_touch_listener_async);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mTextView = (TextView) findViewById(R.id.message_tv);

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
