// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.basic;

import org.android.webview.api.sample.R;

import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.TextView;


public class WebViewWithAnimatableActivity extends Activity {
    private final static float ANIMATION_FACTOR = 0.6F;
    private WebView mWebView;
    private Button runAnimationButton;
    private TextView invokedInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_animatable);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can be scaled.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click Run Animation button.\n")
        .append("2. Click Run Animation button again.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the view is scaled down or scaled up after the Run Animation button is clicked.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        runAnimationButton = (Button) findViewById(R.id.run_animation);
        runAnimationButton.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                startAnimation();
            }
        });

        mWebView = (WebView) findViewById(R.id.webview_animatable);
        mWebView.loadUrl("http://www.baidu.com/");
    }

    private void startAnimation() {
        AnimatorSet combo = new AnimatorSet();

        float targetAlpha = mWebView.getAlpha() == 1.f ? ANIMATION_FACTOR : 1.f;
        float targetScaleFactor = mWebView.getScaleX() == 1.f ? ANIMATION_FACTOR : 1.f;

        ObjectAnimator fade = ObjectAnimator.ofFloat(mWebView,
                "alpha", mWebView.getAlpha(), targetAlpha);
        ObjectAnimator scaleX = ObjectAnimator.ofFloat(mWebView,
                "scaleX", mWebView.getScaleX(), targetScaleFactor);
        ObjectAnimator scaleY = ObjectAnimator.ofFloat(mWebView,
                "scaleY", mWebView.getScaleY(), targetScaleFactor);

        invokedInfo.setText("WebView alpha changed from "+mWebView.getAlpha()+" to "+targetAlpha+
                            "; scaleX changed from "+mWebView.getScaleX()+" to "+targetScaleFactor+
                            "; scaleY changed from "+mWebView.getScaleY()+" to "+targetScaleFactor);

        combo.setDuration(400);
        combo.playTogether(fade, scaleX, scaleY);
        combo.start();
    }
}