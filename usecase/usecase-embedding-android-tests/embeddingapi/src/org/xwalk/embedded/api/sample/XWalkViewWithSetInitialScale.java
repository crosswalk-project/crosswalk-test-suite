// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.content.Context;
import android.graphics.Point;
import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.WindowManager;

public class XWalkViewWithSetInitialScale extends XWalkActivity {
	private final static String TAG = XWalkViewWithSetInitialScale.class.getName();
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.xwview_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can setInitialScale.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Load the html page with whole blue background.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the blue background spans the entire screen size.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

    	WindowManager wm = (WindowManager) getSystemService(Context.WINDOW_SERVICE);
    	Point screenSize = new Point();
    	wm.getDefaultDisplay().getSize(screenSize);
    	Log.d(TAG, "screenSize.x: " + screenSize.x + " screenSize.y: " + screenSize.y);
    	final String pageTemplate = "<html><head>"
    			                + "<meta name='viewport' content='initial-scale=1.0' />"
    			                + "</head><body style='margin:0; padding:0'>"
    			                + "<div style='background:blue;width:" + screenSize.x
    			                + "px;height:" + screenSize.y
    			                + "px'>A big div</div>"
    			                + "</body></html>";
    	mXWalkView.setInitialScale(100);
    	mXWalkView.load(null, pageTemplate);
    }
}