// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.basic;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.TextView;


public class WebViewWithLoadDataWithBaseURL extends Activity {
    private WebView mWebView;
    private Button loadLocalHtml;
    private Button loadLocalImage;
    private TextView invokedInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_loaddata);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can load local html or image.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click Load Local HTML button.\n")
        .append("2. Click Load Local Image button.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the view shows '百度' url and cat png respectively");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        mWebView = (WebView) findViewById(R.id.webview_loaddata);
        mWebView.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                // TODO Auto-generated method stub
                super.onPageFinished(view, url);
                invokedInfo.setText("load url is "+mWebView.getUrl());
            }
        });
        loadLocalHtml = (Button) findViewById(R.id.load_local_html);
        loadLocalImage = (Button) findViewById(R.id.load_local_image);

        final String data_html = "<a href ='http://www.baidu.com/'>百度</a>";
        final String data_image = "<img src ='cat.png'/>";
        final String encoding = "utf-8";
        final String mimeType = "text/html";
        final String baseUrl = "file:///android_asset/";
        loadLocalHtml.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mWebView.loadDataWithBaseURL(null, data_html, mimeType, encoding, null);
            }
        });

        loadLocalImage.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mWebView.loadDataWithBaseURL(baseUrl, data_image, mimeType, encoding, null);
            }
        });

    }
}