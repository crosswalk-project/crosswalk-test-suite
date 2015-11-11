// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.client;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;


public class XWalkViewWithOnJavascriptCloseWindowAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;
    private TextView mMessage;

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
        setContentView(R.layout.activity_xwalk_view_with_on_javascript_close_window_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkUIClient API onJavascriptCloseWindow method can work.\n\n")
        .append("Test  Step:\n")
        .append("1. Click 'Open Popup Window' link.\n")
        .append("2. The Popup Window shows.\n")
        .append("3. Then click 'Close the Popup Window' link.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the xwalkview testcase window closed.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);

        mXWalkView.setUIClient(new XWalkUIClient(mXWalkView) {

            @Override
            public void onJavascriptCloseWindow(XWalkView view) {
                // TODO Auto-generated method stub
                super.onJavascriptCloseWindow(view);
                mMessage.setText("onJavascriptCloseWindow is invoked");
            }
        });

        mXWalkView.load("file:///android_asset/window_close_js.html", null);
    }
}
