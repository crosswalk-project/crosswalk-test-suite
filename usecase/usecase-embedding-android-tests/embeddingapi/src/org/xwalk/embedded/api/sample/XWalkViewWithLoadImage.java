// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.content.Intent;
import android.os.Bundle;

public class XWalkViewWithLoadImage extends XWalkActivity {
    private XWalkView mXWalkView;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		// TODO Auto-generated method stub
		super.onActivityResult(requestCode, resultCode, data);
		if (mXWalkView != null) mXWalkView.onActivityResult(requestCode, resultCode, data);
	}

	@Override
	protected void onXWalkReady() {
		// TODO Auto-generated method stub
        setContentView(R.layout.xwview_layout);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can load image.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load image from you upload.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mXWalkView.load("http://jquery.decadework.com/", null);
	}
    
}
