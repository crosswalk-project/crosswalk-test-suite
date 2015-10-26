// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.client;

import org.xwalk.embedded.api.asyncsample.R;

import org.xwalk.core.ClientCertRequest;
import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

public class XWalkViewWithOnReceivedLoadErrorAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private TextView mTextView;
    private XWalkInitializer mXWalkInitializer;
    private static final String TAG = XWalkViewWithOnReceivedLoadErrorAsync.class.getName();
    private static final String BAD_SSL_WEBSITE = "https://egov.privasphere.com/";

    class ResourceClient extends XWalkResourceClient {

        public ResourceClient(XWalkView xwalkView) {
            super(xwalkView);
        }

        public void onReceivedLoadError(XWalkView view, int errorCode, String description,
                String failingUrl) {
            Log.d(TAG, "Load Failed:" + description);
            super.onReceivedLoadError(view, errorCode, description, failingUrl);
            mTextView.setText(mTextView.getText().toString() + "Load Failed: " + description
            		+ "\n");
        }

        public void onReceivedClientCertRequest(XWalkView view,
                ClientCertRequest handler) {
            // TODO Auto-generated method stub
            Log.d(TAG, "ClientCert Request:" + handler);
            super.onReceivedClientCertRequest(view, handler);
            mTextView.setText(mTextView.getText().toString() + "ClientCert Request: " + handler
            		+ "\n");
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
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView change dialog of onReceivedLoadError to toast.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app get toast attention \"Bad SSL client authentication certificate\".");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.version_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mTextView = (TextView) findViewById(R.id.text1);
        mTextView.setText("XWalkView is handling a Bad SSL client certificate request. The load website is "
        		+ BAD_SSL_WEBSITE + "\n\n");

        mXWalkView.setResourceClient(new ResourceClient(mXWalkView));
        mXWalkView.load(BAD_SSL_WEBSITE, null);
    }
}
