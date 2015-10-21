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
import android.widget.LinearLayout;
import android.widget.TextView;


public class WebViewWithMultiInstanceActivity extends Activity {
    private WebView mWebView1;
    private WebView mWebView2;
    private TextView invokedInfo;
    private String loadUrl;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_container);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can create multi instance.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load 'sogou.com' and 'baidu.com'.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm", null)
        .show();

        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        LinearLayout parent = (LinearLayout) findViewById(R.id.container);

        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.MATCH_PARENT);
        params.weight = 1;

        mWebView1 = new WebView(this);
        parent.addView(mWebView1, params);

        mWebView2 = new WebView(this);
        parent.addView(mWebView2, params);

        mWebView1.loadUrl("http://m.sogou.com", null);
        mWebView2.loadUrl("http://m.baidu.com", null);
        mWebView1.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                // TODO Auto-generated method stub
                super.onPageFinished(view, url);
                loadUrl = "webview1 url is "+mWebView1.getUrl() + "; webview2 url is "+mWebView2.getUrl();
                invokedInfo.setText(loadUrl);
            }
        });
        mWebView2.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                // TODO Auto-generated method stub
                super.onPageFinished(view, url);
                loadUrl = "webview1 url is "+mWebView1.getUrl() + "; webview2 url is "+mWebView2.getUrl();
                invokedInfo.setText(loadUrl);
            }
        });
    }
}