// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;


public class WebViewWithLayoutActivity extends Activity {
    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.webview_layout);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can load url.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load 'baidu' page.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mWebView = (WebView) findViewById(R.id.webview);
        mWebView.loadUrl("http://www.baidu.com/");
    }
}
