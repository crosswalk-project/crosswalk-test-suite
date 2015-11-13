/// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.client;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.os.Message;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.widget.TextView;


public class WebViewWithOnCreateWindow extends Activity{
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
        mCaseDesc.setText(getText(R.string.webview_with_on_create_window_desc));

        mWebView.setWebChromeClient(new InVokedWebChromeClient());
        mWebView.getSettings().setJavaScriptEnabled(true);
        mWebView.getSettings().setSupportMultipleWindows(true);
        mWebView.getSettings().setJavaScriptCanOpenWindowsAutomatically(true);
        mWebView.loadUrl("file:///android_asset/window_create_open.html");
    }


    class InVokedWebChromeClient extends WebChromeClient {

        @Override
        public boolean onCreateWindow(WebView view, boolean isDialog,
                boolean isUserGesture, Message resultMsg) {
            // TODO Auto-generated method stub
            count++;
            invokedInfo.setText("onCreateWindow is invoked " + count + " times");
            return false;
        }
    }

}