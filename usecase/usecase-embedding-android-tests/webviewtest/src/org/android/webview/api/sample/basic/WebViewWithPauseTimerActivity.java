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
import android.widget.ImageButton;
import android.widget.TextView;


public class WebViewWithPauseTimerActivity extends Activity {
    private ImageButton pauseTimerButton;
    private WebView mWebView;
    private boolean isPaused = false;
    private TextView invokedInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_pausetimer);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can pause and resume timer.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click pause button.\n\n")
        .append("2. Click resume button again.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if time paused and resumed.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        mWebView = (WebView) findViewById(R.id.webview_pausetimer);
        mWebView.getSettings().setJavaScriptEnabled(true);
        pauseTimerButton = (ImageButton) findViewById(R.id.pause_timer);
        pauseTimerButton.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                if (mWebView != null) {
                    if (!isPaused) {
                        //Pause js timer
                        mWebView.pauseTimers();
                        invokedInfo.setText("Timer is paused");
                        isPaused = true;
                        pauseTimerButton.setImageResource(android.R.drawable.ic_media_play);
                    } else {
                        mWebView.resumeTimers();
                        invokedInfo.setText("Timer is resumed");
                        isPaused = false;
                        pauseTimerButton.setImageResource(android.R.drawable.ic_media_pause);
                    }
                }
            }
        });

        mWebView.loadUrl("file:///android_asset/pause_timers.html");
    }
}