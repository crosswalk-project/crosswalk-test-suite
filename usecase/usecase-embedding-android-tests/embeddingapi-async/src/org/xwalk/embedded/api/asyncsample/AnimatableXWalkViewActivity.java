// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkPreferences;

import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.Button;
import android.view.View;

/**
 * Sample code to show how to use ANIMATED_XWALK_VIEW preference key to create
 * animated XWalkView and apply alpha animation or scale animation on it.
 */
public class AnimatableXWalkViewActivity extends Activity implements XWalkInitializer.XWalkInitListener {
    private final static float ANIMATION_FACTOR = 0.6f;
    private Button mRunAnimationButton;
    private XWalkView mXWalkView;

    private void startAnimation() {
        AnimatorSet combo = new AnimatorSet();

        float targetAlpha = mXWalkView.getAlpha() == 1.f ? ANIMATION_FACTOR : 1.f;
        float targetScaleFactor = mXWalkView.getScaleX() == 1.f ? ANIMATION_FACTOR : 1.f;

        ObjectAnimator fade = ObjectAnimator.ofFloat(mXWalkView,
                "alpha", mXWalkView.getAlpha(), targetAlpha);
        ObjectAnimator scaleX = ObjectAnimator.ofFloat(mXWalkView,
                "scaleX", mXWalkView.getScaleX(), targetScaleFactor);
        ObjectAnimator scaleY = ObjectAnimator.ofFloat(mXWalkView,
                "scaleY", mXWalkView.getScaleY(), targetScaleFactor);

        combo.setDuration(400);
        combo.playTogether(fade, scaleX, scaleY);
        combo.start();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        XWalkInitializer.initAsync(this, this);
    }

    @Override
    public final void onXWalkInitStarted() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitCancelled() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitFailed() {
        // Do crash or logging or anything else in order to let the tester know if this method get called
    }

    @Override
    public final void onXWalkInitCompleted() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies Animatable XWalkView can be scaled.\n\n")
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

        // ANIMATABLE_XWALK_VIEW preference key MUST be set before XWalkView creation.
        XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, true);

        setContentView(R.layout.animatable_xwview_layout);

        mRunAnimationButton = (Button) findViewById(R.id.run_animation);
        mRunAnimationButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startAnimation();
            }
        });

        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mXWalkView.load("http://www.baidu.com", null);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();

        // Reset the preference for animatable XWalkView.
        if (mXWalkView != null) {
            XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, false);
        }
    }

}
