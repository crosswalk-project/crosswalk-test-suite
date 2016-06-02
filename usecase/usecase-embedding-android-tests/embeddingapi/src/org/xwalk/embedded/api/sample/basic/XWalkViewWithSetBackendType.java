package org.xwalk.embedded.api.sample.basic;

import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

public class XWalkViewWithSetBackendType extends XWalkActivity {
    private XWalkView mXWalkView1, mXWalkView2;
    private Button mRunAnimationButton1, mRunAnimationButton2;

    private final static float ANIMATION_FACTOR = 0.6f;

    private void startAnimation( XWalkView xwalkview) {
        AnimatorSet combo = new AnimatorSet();

        float targetAlpha = xwalkview.getAlpha() == 1.f ? ANIMATION_FACTOR : 1.f;
        float targetScaleFactor = xwalkview.getScaleX() == 1.f ? ANIMATION_FACTOR : 1.f;

        ObjectAnimator fade = ObjectAnimator.ofFloat(xwalkview,
                "alpha", xwalkview.getAlpha(), targetAlpha);
        ObjectAnimator scaleX = ObjectAnimator.ofFloat(xwalkview,
                "scaleX", xwalkview.getScaleX(), targetScaleFactor);
        ObjectAnimator scaleY = ObjectAnimator.ofFloat(xwalkview,
                "scaleY", xwalkview.getScaleY(), targetScaleFactor);

        combo.setDuration(400);
        combo.playTogether(fade, scaleX, scaleY);
        combo.start();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_animation);

    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView BackendType can be set in layout xml\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click the 'ANIMATION1' button.\n")
        .append("2. Click the 'ANIMATION2' button.\n\n")
        .append("Expected Result:\n\n")
        .append("1.Test passes if the baidu page hide.")
        .append("2.Test passes if the sogou page change in scale.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView1 = (XWalkView) findViewById(R.id.xwalkview1);
        mXWalkView2 = (XWalkView) findViewById(R.id.xwalkview2);

        mRunAnimationButton1 = (Button) findViewById(R.id.run_animation1);
        mRunAnimationButton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startAnimation(mXWalkView1);
            }
        });

        mRunAnimationButton2 = (Button) findViewById(R.id.run_animation2);
        mRunAnimationButton2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startAnimation(mXWalkView2);
            }
        });

        mXWalkView1.load("http://www.baidu.com", null);
        mXWalkView2.load("http://www.sogou.com", null);

    }
}
