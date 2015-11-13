// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.client;


import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebIconDatabase;
import android.webkit.WebView;
import android.widget.ImageView;
import android.widget.TextView;


public class WebViewWithOnReceivedIcon extends Activity{
    private WebView mWebView;
    private TextView invokedInfo;
    private ImageView mFavicon;
    private int count;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_on_received_icon);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebChromeClient onReceivedIcon API can be invoked.\n\n")
        .append("Expected Result:\n\n")
        .append("1. Test passes if app show 'onReceivedIcon' and the times.")
        .append("2. Test passes if app show the image of cat.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null)
        .show();

        mWebView = (WebView) findViewById(R.id.webview);
        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        mFavicon = (ImageView) findViewById(R.id.image_view);

        WebIconDatabase.getInstance().open(getDir("icons", MODE_PRIVATE).getPath());

        mWebView.setWebChromeClient(new InVokedWebChromeClient());
        mWebView.getSettings().setJavaScriptEnabled(true);
        mWebView.loadUrl("file:///android_asset/window_icon.html");
    }


    class InVokedWebChromeClient extends WebChromeClient {

        @Override
        public void onReceivedIcon(WebView view, Bitmap icon) {
            // TODO Auto-generated method stub
            super.onReceivedIcon(view, icon);
            count++;
            mFavicon.setImageBitmap(icon);
            invokedInfo.setText("onReceivedIcon is invoked " + count + " times");
        }
    }
}