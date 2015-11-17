// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.client;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;


public class WebViewWithShouldOverrideUrlLoading extends Activity{
    private WebView mWebView;
    private TextView mCaseDesc;
    private TextView invokedInfo;
    private int count;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_layout);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebChromeClient onCreateWindow API can be invoked.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click the 'Create Window on blank' button.\n")
        .append("2. Click the 'Create Window on blank' link.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app show 'onCreateWindowRequested' and the correct triggered times.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null)
        .show();

        mWebView = (WebView) findViewById(R.id.webview);
        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        mCaseDesc = (TextView) findViewById(R.id.case_desc);
        mCaseDesc.setText(getText(R.string.webview_with_should_override_url_loading_desc));

        mWebView.setWebViewClient(new InVokedWebViewClient());
        mWebView.getSettings().setJavaScriptEnabled(true);
        mWebView.loadUrl("file:///android_asset/navigate.html");
    }


    class InVokedWebViewClient extends WebViewClient {

        @Override
        public boolean shouldOverrideUrlLoading(WebView view, String url) {
            // TODO Auto-generated method stub
            count++;
            invokedInfo.setText("shouldOverrideUrlLoading is invoked "+ count + " times.\nThe url is " + url);
            return super.shouldOverrideUrlLoading(view, url);
        }
    }
}