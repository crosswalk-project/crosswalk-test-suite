// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.basic;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.widget.TextView;


public class WebViewWithPlayVideoActivity extends Activity {
    private WebView mWebView;
    private TextView caseDesc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_layout);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies Webview can play html5 video.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Play the video in the page, then click home key.\n")
        .append("2. Click the 'Usecase WebViewAPI' app again.\n\n")
        .append("Expected Result:\n\n")
        .append("1.Test passes if app video is still playing when come back.\n")
        .append("2.Test passes if there is no short white screen displayed when clicking home key.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        caseDesc = (TextView) findViewById(R.id.case_desc);
        caseDesc.setText(R.string.webview_with_playvideo_desc);
        mWebView = (WebView) findViewById(R.id.webview);
        mWebView.getSettings().setJavaScriptEnabled(true);
        mWebView.setWebChromeClient(new WebChromeClient());

        mWebView.loadUrl("http://www.iandevlin.com/html5/webvtt-example.html");
    }
}
