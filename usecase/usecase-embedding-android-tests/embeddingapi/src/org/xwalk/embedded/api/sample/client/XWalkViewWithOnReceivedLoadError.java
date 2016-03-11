// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.client;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.ClientCertRequest;
import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;


public class XWalkViewWithOnReceivedLoadError extends XWalkActivity {
    private XWalkView mXWalkView;
    private TextView mTextView;
    private static final String TAG = XWalkViewWithOnReceivedLoadError.class.getName();
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
            String request = "ClientCert Request Host: " + handler.getHost() + "\n"
                           + "ClientCert Request Port: " + handler.getPort() + "\n"
                           + "ClientCert Request KeyTypes: " + handler.getKeyTypes()[0] + " " + handler.getKeyTypes()[1] + "\n"
                           + "ClientCert Request Principals: " + handler.getPrincipals() + "\n";
            mTextView.setText(mTextView.getText().toString() + request);
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.version_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mTextView = (TextView) findViewById(R.id.text1);
        mTextView.setTextColor(Color.GREEN);
        mTextView.setText("XWalkView is handling a Bad SSL client certificate request. The load website is "
        		+ BAD_SSL_WEBSITE + "\n\n");
    }

    @Override
    protected void onXWalkReady() {
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

        mXWalkView.setResourceClient(new ResourceClient(mXWalkView));
        mXWalkView.load(BAD_SSL_WEBSITE, null);
    }
}
