// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.FrameLayout;

public class XWalkWithSaveState extends XWalkActivity {
    private XWalkView xWalkView;
    private Button button_one;
    private Button button_two;
    private Button button_three;
    private FrameLayout mFrameLayout;
    private Bundle bundle;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.savestate_layout);        
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can saveState & restoreState bundle.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click saveInstance button when finish loading baidu home page.\n")
        .append("2. Click load_other button and meituan homepage shows.\n")
        .append("3. Click restoreInstance button and wait page changing to first one.\n\n")  
        .append("Expected Result:\n\n")
        .append("Test passes if app show baidu home page.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        
        button_one = (Button) findViewById(R.id.button_one);
        button_two = (Button) findViewById(R.id.button_two);
        button_three = (Button) findViewById(R.id.button_three);
        mFrameLayout = (FrameLayout) findViewById(R.id.frameLayout);
        
        bundle = new Bundle();
        xWalkView = new XWalkView(this,this);
        xWalkView.load("http://www.baidu.com", null);
        button_one.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                xWalkView.saveState(bundle);
            }
        });
        button_two.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                xWalkView.load("http://i.meituan.com", null);
            }
        });
        button_three.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                xWalkView.restoreState(bundle);
            }
        });
        mFrameLayout.addView(xWalkView);
    }
}
