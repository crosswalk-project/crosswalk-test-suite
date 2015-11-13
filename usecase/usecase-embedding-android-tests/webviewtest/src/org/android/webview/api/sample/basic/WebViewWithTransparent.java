// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.basic;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;


public class WebViewWithTransparent extends Activity {
    private WebView mWebView;
    private TextView mCaseDesc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_layout);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView's transparent feature.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load transparent baidu page.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mCaseDesc = (TextView) findViewById(R.id.case_desc);
        mCaseDesc.setText(getText(R.string.webview_with_transparent_desc));
        mWebView = (WebView) findViewById(R.id.webview);
        mWebView.setBackgroundColor(Color.TRANSPARENT);
        mWebView.setWebViewClient(new WebViewClient() {

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                // TODO Auto-generated method stub
                view.loadUrl(url);
                return true;
            }

        });
        mWebView.loadUrl("http://m.baidu.com/");
    }
}
