// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.misc;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebHistoryItem;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageButton;
import android.widget.TextView;

public class WebViewWithNavigation extends Activity {
    private WebView mWebView;
    private ImageButton mNextButton;
    private ImageButton mPrevButton;

    String url, originalUrl, title;
    TextView text1, text2, text3;

    private void showNavigationItemInfo(WebHistoryItem navigationItem){
        url = navigationItem.getUrl();
        originalUrl = navigationItem.getOriginalUrl();
        title = navigationItem.getTitle();

        text1.setText(title);
        text2.setText(url);
        text3.setText(originalUrl);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_navigation);
        mWebView = (WebView) findViewById(R.id.webview_navigation);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can forward and backward history.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Search some in baidu page, and click some some searched links.\n")
        .append("2. Click the go backward button and then cilck go forward button.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app history can go backward and go forward.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mPrevButton = (ImageButton) findViewById(R.id.prev);
        mNextButton = (ImageButton) findViewById(R.id.next);

        text1 = (TextView) super.findViewById(R.id.text1);
        text2 = (TextView) super.findViewById(R.id.text2);
        text3 = (TextView) super.findViewById(R.id.text3);

        mPrevButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // Go backward
                if (mWebView != null &&
                        mWebView.canGoBack()) {
                    mWebView.goBack();
                }
                WebHistoryItem navigationItem = mWebView.copyBackForwardList().getCurrentItem();
                showNavigationItemInfo(navigationItem);
            }
        });

        mNextButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // Go forward
                if (mWebView != null &&
                        mWebView.canGoForward()) {
                    mWebView.goForward();
                }
                WebHistoryItem navigationItem = mWebView.copyBackForwardList().getCurrentItem();
                showNavigationItemInfo(navigationItem);
            }
        });

        mWebView.setWebViewClient(new WebViewClient() {

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                // TODO Auto-generated method stub
                view.loadUrl(url);
                return true;
            }
        });
        mWebView.loadUrl("http://www.baidu.com/", null);
    }
}
