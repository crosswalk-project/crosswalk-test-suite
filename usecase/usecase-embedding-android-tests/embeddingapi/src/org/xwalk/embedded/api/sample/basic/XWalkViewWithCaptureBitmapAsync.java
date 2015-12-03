// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.basic;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkGetBitmapCallback;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.ImageView;


public class XWalkViewWithCaptureBitmapAsync extends XWalkActivity {
    private XWalkView mXWalkView;
    private ImageView mImageView;
    private Button mCaptureButton;
    private XWalkGetBitmapCallback mXWalkGetBitmapCallback;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_capture_bitmap_async);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can capture the visible content of web page.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click 'Capture Bitmap' button when finish loading baidu home page.\n")
        .append("2. The captured bitmap will show on the bottom.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if captured bitmap shows.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mImageView = (ImageView) findViewById(R.id.imageview);
        mCaptureButton = (Button) findViewById(R.id.capture_btn);

        mXWalkView.load("http://www.baidu.com", null);
        mCaptureButton.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                if (mXWalkView == null) return;
                mXWalkGetBitmapCallback = new XWalkGetBitmapCallbackImpl();
                mXWalkView.captureBitmapAsync(mXWalkGetBitmapCallback);
            }
        });
    }

    class XWalkGetBitmapCallbackImpl extends XWalkGetBitmapCallback{

        public XWalkGetBitmapCallbackImpl() {
            super();
        }

        @Override
        public void onFinishGetBitmap(Bitmap bitmap, int response) {
            if (response == 0) {
                mImageView.setImageBitmap(bitmap);
                bitmap = null;
            }
        }
    }
}
