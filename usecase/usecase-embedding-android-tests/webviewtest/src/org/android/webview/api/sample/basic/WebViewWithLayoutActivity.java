// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.basic;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;


public class WebViewWithLayoutActivity extends Activity {
    private WebView mWebView;
    private TextView invokedInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_layout);

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

        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        mWebView = (WebView) findViewById(R.id.webview);
        mWebView.loadUrl("http://www.baidu.com/");
        mWebView.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                // TODO Auto-generated method stub
                super.onPageFinished(view, url);
                invokedInfo.setText("load url is "+mWebView.getUrl());
            }
        });
    }
}
