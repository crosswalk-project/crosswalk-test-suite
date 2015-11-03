// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.basic;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.TextView;

public class WebViewWithMultiInstanceOverlay extends Activity {
    private WebView mWebView;
    private WebView mWebView2;
    private Button mSwapButton;
    private TextView mOverlayLabel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_multi_instance_overlay);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies two WebViews filling in the same parent view can be displayed dynamically.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load 'sogou' and 'baidu' dynamically by swap button.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null)
        .show();

        FrameLayout parent = (FrameLayout) findViewById(R.id.overlay_container);

        FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT,
                FrameLayout.LayoutParams.MATCH_PARENT);

        mOverlayLabel = (TextView) findViewById(R.id.invoked_info);
        mSwapButton = (Button) findViewById(R.id.swap_button);
        mSwapButton.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                if (mWebView.getVisibility() == View.VISIBLE) {
                    mWebView.setVisibility(View.INVISIBLE);
                    mWebView2.setVisibility(View.VISIBLE);
                    mOverlayLabel.setText("sogou visibility: INVISIBLE; baidu visibility: VISIBLE");
                } else {
                    mWebView.setVisibility(View.VISIBLE);
                    mWebView2.setVisibility(View.INVISIBLE);
                    mOverlayLabel.setText("sogou visibility: VISIBLE; baidu visibility: INVISIBLE");
                }
            }
        });

        mWebView = new WebView(this);
        parent.addView(mWebView, params);
        mWebView.setVisibility(View.VISIBLE);

        mWebView2 = new WebView(this);
        parent.addView(mWebView2, params);
        mWebView2.setVisibility(View.INVISIBLE);

        mWebView.setWebViewClient(new WebViewClient() {

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                // TODO Auto-generated method stub
                view.loadUrl(url);
                return true;
            }
        });
        mWebView2.setWebViewClient(new WebViewClient() {

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                // TODO Auto-generated method stub
                view.loadUrl(url);
                return true;
            }
        });

        mWebView.loadUrl("http://www.sogou.com");
        mWebView2.loadUrl("http://www.baidu.com");

        mOverlayLabel.setText("sogou visibility: VISIBLE; baidu visibility: INVISIBLE");
    }

}