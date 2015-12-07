// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.client;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

public class XWalkViewWithOnJsAlertAsync extends Activity implements XWalkInitializer.XWalkInitListener {
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
        setContentView(R.layout.activity_xwalk_view_with_on_js_alert_async);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkUIClient API onJsAlert & onJsConfirm & onJsPrompt can work.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click 'Click Me'.\n")
        .append("2. Click 'Click Alert'.\n")
        .append("3. Click 'Click Confirm'.\n")
        .append("4. Click 'Click Prompt'.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if JS Dialog will show and message received.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView.setUIClient(new XWalkUIClient(mXWalkView) {

            @Override
            public boolean onJsAlert(XWalkView view, String url,
                    String message, XWalkJavascriptResult result) {
                // TODO Auto-generated method stub
                mMessage.setText("onJsAlert is invoked. Message is " + message);
                return super.onJsAlert(view, url, message, result);
            }

            @Override
            public boolean onJsConfirm(XWalkView view, String url,
                    String message, XWalkJavascriptResult result) {
                // TODO Auto-generated method stub
                mMessage.setText("onJsConfirm is invoked. Message is " + message);
                return super.onJsConfirm(view, url, message, result);
            }

            @Override
            public boolean onJsPrompt(XWalkView view, String url,
                    String message, String defaultValue,
                    XWalkJavascriptResult result) {
                // TODO Auto-generated method stub
                mMessage.setText("onJsPrompt is invoked. Message is " + message);
                return super.onJsPrompt(view, url, message, defaultValue, result);
            }
        });

        mXWalkView.load("file:///android_asset/js_modal_dialog.html", null);
    }
}
