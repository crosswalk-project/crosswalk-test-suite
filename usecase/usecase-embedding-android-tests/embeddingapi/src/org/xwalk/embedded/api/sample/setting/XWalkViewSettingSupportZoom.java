package org.xwalk.embedded.api.sample.setting;

import android.app.AlertDialog;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkSettings;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.FrameLayout;
import android.widget.LinearLayout;

import org.xwalk.embedded.api.sample.R;

public class XWalkViewSettingSupportZoom extends XWalkActivity {
    private Button mEnableBuiltInZoomButton;
    private Button mEnableSupportZoomButton;
    private Button mEnableDoubleTapZoomButton;
    private TextView mSupportZoomState;
    private XWalkSettings mXWalkSettings;
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.container);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Sets whether the XWalkView should support zooming using its on-screen zoom controls" +
                        "and gestures. The particular zoom mechanisms that should be used can be set with" +
                        "setBuiltInZoomControls(boolean). The default is true. \n\n")
                .append("Test  Step:\n\n")
                .append("1. Click 'Enable DoubleTapZoom' button.\n")
                .append("2. Click 'Enable SupportZoom' button.\n")
                .append("3. Click 'Enable BuiltInZoom' button.\n")
                .append("Expected Result:\n\n")
                .append("Test passes, if Zooming can be controlled.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        LinearLayout parent = (LinearLayout) findViewById(R.id.container);

        FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.FILL_PARENT,
                FrameLayout.LayoutParams.FILL_PARENT);
        FrameLayout.LayoutParams buttonParams = new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.FILL_PARENT,
                FrameLayout.LayoutParams.WRAP_CONTENT);

        mSupportZoomState = new TextView(this);
        parent.addView(mSupportZoomState, buttonParams);
        mSupportZoomState.setTextColor(Color.GREEN);

        mEnableSupportZoomButton = new Button(this);
        mEnableSupportZoomButton.setText("Enable SupportZoom");
        parent.addView(mEnableSupportZoomButton, buttonParams);
        mEnableSupportZoomButton.setOnClickListener(new OnClickListener() {
            public void onClick(View v) {
                if ("Enable SupportZoom".equals(mEnableSupportZoomButton.getText())) {
                    mEnableSupportZoomButton.setText("Disable SupportZoom");
                    setAndLoadForSupportZoom(true);
                } else {
                    mEnableSupportZoomButton.setText("Enable SupportZoom");
                    setAndLoadForSupportZoom(false);
                }
                setSupportZoomState();
            }
        });

        mEnableBuiltInZoomButton = new Button(this);
        mEnableBuiltInZoomButton.setText("Enable BuiltInZoom");
        parent.addView(mEnableBuiltInZoomButton, buttonParams);
        mEnableBuiltInZoomButton.setOnClickListener(new OnClickListener() {
            public void onClick(View v) {
                if ("Enable BuiltInZoom".equals(mEnableBuiltInZoomButton.getText())) {
                    mEnableBuiltInZoomButton.setText("Disable BuiltInZoom");
                    setAndLoadForBuiltInZoom(true);
                } else {
                    mEnableBuiltInZoomButton.setText("Enable BuiltInZoom");
                    setAndLoadForBuiltInZoom(false);
                }
                setSupportZoomState();
            }
        });

        mEnableDoubleTapZoomButton = new Button(this);
        mEnableDoubleTapZoomButton.setText("Enable DoubleTapZoom");
        parent.addView(mEnableDoubleTapZoomButton, buttonParams);
        mEnableDoubleTapZoomButton.setOnClickListener(new OnClickListener() {
            public void onClick(View v) {
                if ("Enable DoubleTapZoom".equals(mEnableDoubleTapZoomButton.getText())) {
                    mEnableDoubleTapZoomButton.setText("Disable DoubleTapZoom");
                    setAndLoadForDoubleTapZoom(true);
                } else {
                    mEnableDoubleTapZoomButton.setText("Enable DoubleTapZoom");
                    setAndLoadForDoubleTapZoom(false);
                }
                setSupportZoomState();
            }
        });

        mXWalkView = new XWalkView(this, this);
        parent.addView(mXWalkView, params);
        mXWalkSettings = mXWalkView.getSettings();
    }

    void setAndLoadForSupportZoom(boolean flag) {
        mXWalkSettings.setSupportZoom(flag);
        mXWalkView.load("file:///android_asset/builtinzoom.html", null);
    }

    void setAndLoadForBuiltInZoom(boolean flag) {
        mXWalkSettings.setBuiltInZoomControls(flag);
        mXWalkView.load("file:///android_asset/builtinzoom.html", null);
    }

    void setAndLoadForDoubleTapZoom(boolean flag) {
        // setUseWideViewPort() should be called at first.
        mXWalkSettings.setUseWideViewPort(flag);
        mXWalkSettings.setBuiltInZoomControls(flag);
        mXWalkView.load("file:///android_asset/doubletapzoom.html", null);
    }

    void setSupportZoomState() {
        String state = "SupportZoom: " + mXWalkSettings.supportZoom() +
                       "\nBuiltInZoomControls: " + mXWalkSettings.getBuiltInZoomControls() +
                       "\nUseWideViewPort: " + mXWalkSettings.getUseWideViewPort();
        mSupportZoomState.setText(state);
    }
}
