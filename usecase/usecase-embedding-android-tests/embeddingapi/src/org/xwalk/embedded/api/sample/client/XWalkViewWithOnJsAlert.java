// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.client;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

public class XWalkViewWithOnJsAlert extends XWalkActivity {
    private XWalkView mXWalkView;
    private TextView mMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_on_js_alert);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
    }

    @Override
    protected void onXWalkReady() {
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
