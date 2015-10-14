// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.widget.TextView;


public class XWalkViewWithOnUnhandledKeyEventAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private TextView mTextView;
    private XWalkInitializer mXWalkInitializer;
    private static final String TAG = XWalkViewWithOnUnhandledKeyEventAsync.class.getName();

    class UIClient extends XWalkUIClient {

        public UIClient(XWalkView xwalkView) {
            super(xwalkView);
        }

		@Override
		public void onUnhandledKeyEvent(XWalkView view, KeyEvent event) {
			// TODO Auto-generated method stub
			Log.d(TAG, "onUnhandledKeyEvent.");
			super.onUnhandledKeyEvent(view, event);
			mTextView.setText("onUnhandledKeyEvent is invoked. Event is " + event);
		}

		@Override
		public boolean shouldOverrideKeyEvent(XWalkView view, KeyEvent event) {
			// TODO Auto-generated method stub
			Log.d(TAG, "shouldOverrideKeyEvent.");
			return false;
		}        
    }

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
        setContentView(R.layout.activity_xwalk_view_with_on_unhandled_keyevent);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mTextView = (TextView) findViewById(R.id.unhandled_keyevent_label);    
    
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView UI Client can override 'onUnhandledKeyEvent' method.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Load baidu webpage.\n")
        .append("2. Input any words in the input field.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if text shows \"onUnhandledKeyEvent is invoked\".");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView.setUIClient(new UIClient(mXWalkView));
        mXWalkView.load("http://www.baidu.com/", null);
    }
}

