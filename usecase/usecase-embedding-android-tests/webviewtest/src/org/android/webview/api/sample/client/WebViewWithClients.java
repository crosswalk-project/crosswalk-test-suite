// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.client;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.util.Log;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.EditText;


public class WebViewWithClients extends Activity{
    private static final String TAG = WebViewWithClients.class.getName();
    private WebView mWebView;
    private EditText mText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_clients);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView's WebViewClient & WebChromeClient override methods can be invoked.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if invoked methods will be shown when webview load a url.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null)
        .show();

        mWebView = (WebView) findViewById(R.id.webview);
        mText = (EditText) findViewById(R.id.text1);
        mWebView.setWebViewClient(new InVokedWebViewClient());
        mWebView.setWebChromeClient(new InVokedWebChromeClient());
        mWebView.loadUrl("http://www.sina.com.cn/");
    }

    class InVokedWebViewClient extends WebViewClient {

        @Override
        public void doUpdateVisitedHistory(WebView view, String url,
                boolean isReload) {
            // TODO Auto-generated method stub
            super.doUpdateVisitedHistory(view, url, isReload);
            Log.d(TAG, "doUpdateVisitedHistory is invoked");
            mText.append("doUpdateVisitedHistory is invoked. url is "+url+" isReload is "+isReload+"\n");
        }

        @Override
        public void onLoadResource(WebView view, String url) {
            // TODO Auto-generated method stub
            super.onLoadResource(view, url);
            Log.d(TAG, "onLoadResource is invoked");
            mText.append("onLoadResource is invoked. url is "+url+"\n");
        }

        @Override
        public void onPageFinished(WebView view, String url) {
            // TODO Auto-generated method stub
            super.onPageFinished(view, url);
            Log.d(TAG, "onPageFinished is invoked");
            mText.append("onPageFinished is invoked. url is "+url+"\n");
        }

        @Override
        public void onPageStarted(WebView view, String url, Bitmap favicon) {
            // TODO Auto-generated method stub
            super.onPageStarted(view, url, favicon);
            Log.d(TAG, "onPageStarted is invoked");
            mText.append("onPageStarted is invoked. url is "+url+"\n");
        }

        @Override
        public boolean shouldOverrideUrlLoading(WebView view, String url) {
            // TODO Auto-generated method stub
            Log.d(TAG, "shouldOverrideUrlLoading is invoked");
            mText.append("shouldOverrideUrlLoading is invoked. url is "+url+"\n");
            return super.shouldOverrideUrlLoading(view, url);
        }
    }

    class InVokedWebChromeClient extends WebChromeClient {

        @Override
        public void getVisitedHistory(ValueCallback<String[]> callback) {
            // TODO Auto-generated method stub
            super.getVisitedHistory(callback);
            Log.d(TAG, "getVisitedHistory is invoked");
            mText.append("getVisitedHistory is invoked.\n");
        }

        @Override
        public void onProgressChanged(WebView view, int newProgress) {
            // TODO Auto-generated method stub
            super.onProgressChanged(view, newProgress);
            Log.d(TAG, "onProgressChanged is invoked");
            mText.append("onProgressChanged is invoked. progress is "+newProgress+"\n");
        }

        @Override
        public void onReceivedTitle(WebView view, String title) {
            // TODO Auto-generated method stub
            super.onReceivedTitle(view, title);
            Log.d(TAG, "onReceivedTitle is invoked");
            mText.append("onReceivedTitle is invoked. title is "+title+"\n");
        }

        @Override
        public void onReceivedTouchIconUrl(WebView view, String url,
                boolean precomposed) {
            // TODO Auto-generated method stub
            super.onReceivedTouchIconUrl(view, url, precomposed);
            Log.d(TAG, "onReceivedTouchIconUrl is invoked");
            mText.append("onReceivedTouchIconUrl is invoked. url is "+url+"\n");
        }
    }
}