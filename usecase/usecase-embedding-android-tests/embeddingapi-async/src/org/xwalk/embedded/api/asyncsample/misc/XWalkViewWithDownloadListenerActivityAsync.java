// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.misc;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkDownloadListener;

import android.os.Bundle;
import org.xwalk.core.XWalkView;
import android.app.AlertDialog;
import android.widget.TextView;

public class XWalkViewWithDownloadListenerActivityAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;
    private TextView downloadText;

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
        setContentView(R.layout.version_layout);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can set & get UserAgentString, meaningwhile set DownloadListener & override onDownloadStart.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Load the Baidu page and show the set UserAgentString.\n\n")
        .append("2. Click baidu website bottom ShouJiBaidu link or any other download link.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if UserAgentString & download link info shows.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        downloadText = (TextView) findViewById(R.id.text1);
        mXWalkView.setUserAgentString("Chrome/44.0.2403.81 Crosswalk/15.44.376.0 Mobile Safari/537.36");
        downloadText.setText("getUserAgentString: " + mXWalkView.getUserAgentString() + "\n");
        mXWalkView.setDownloadListener(new XWalkDownloadListener(getApplicationContext()) {

			@Override
			public void onDownloadStart(String url, String userAgent,
			                String contentDisposition, String mimetype, long contentLength) {
				// TODO Auto-generated method stub
				// You can realize your down here.
				downloadText.setText(downloadText.getText() +
				                    "url: " + url + "\n" +
				                    "userAgent: " + userAgent + "\n" +
				                    "contentDisposition: " + contentDisposition + "\n" +
				                    "mimeType: " + mimetype + "\n" +
				                    "contentLength: " + contentLength);
			}
		});
        mXWalkView.load("http://m.baidu.com/", null);
    }

}
