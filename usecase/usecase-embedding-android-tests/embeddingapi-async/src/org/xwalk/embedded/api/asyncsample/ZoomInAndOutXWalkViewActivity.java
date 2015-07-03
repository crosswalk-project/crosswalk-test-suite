// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;


import org.xwalk.core.XWalkView;
import android.app.AlertDialog;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.TextView;
import android.os.Bundle;

public class ZoomInAndOutXWalkViewActivity extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;
    private Button zoomInBtn;
    private Button zoomOutBtn;
    private SeekBar zoomSeekBar;
    private TextView canZoomText;
    private static final String ZOOMRANGE = "Set zoom range: 0.5~2.0\n";
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
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
        setContentView(R.layout.zoom_layout);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can zoom.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click Zoom In or Zoom Out Button.\n\n")
        .append("2. Change Zoom Seek bar value.\n\n")    
        .append("Expected Result:\n\n")
        .append("Test passes if the load page can be zoomed and limited.\n\n")
        .append("Test passes if textview 'can zoom in or can zoom out' can change accordingly.");        
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        zoomInBtn = (Button) findViewById(R.id.zoomin_btn);
        zoomOutBtn = (Button) findViewById(R.id.zoomout_btn);
        canZoomText = (TextView) findViewById(R.id.zommtv);
        canZoomText.setText(ZOOMRANGE + "Can zoom in: " + mXWalkView.canZoomIn() + 
				" Can zoom out: " + mXWalkView.canZoomOut());
        zoomSeekBar = (SeekBar) findViewById(R.id.zoombar);
        
        zoomInBtn.setOnClickListener(new OnClickListener() {
			
		@Override
		public void onClick(View v) {
			// TODO Auto-generated method stub
			mXWalkView.zoomIn();
			canZoomText.setText(ZOOMRANGE + "Can zoom in: " + mXWalkView.canZoomIn() + 
					" Can zoom out: " + mXWalkView.canZoomOut());
		}
	});
        zoomOutBtn.setOnClickListener(new OnClickListener() {
			
		@Override
		public void onClick(View v) {
			// TODO Auto-generated method stub
			mXWalkView.zoomOut();
			canZoomText.setText(ZOOMRANGE + "Can zoom in: " + mXWalkView.canZoomIn() + 
					" Can zoom out: " + mXWalkView.canZoomOut());
		}
	});
        zoomSeekBar.setOnSeekBarChangeListener(new OnSeekBarChangeListener() {
			
		@Override
		public void onStopTrackingTouch(SeekBar seekBar) {
			// TODO Auto-generated method stub
				
		}
			
		@Override
		public void onStartTrackingTouch(SeekBar seekBar) {
			// TODO Auto-generated method stub
				
		}
			
		@Override
		public void onProgressChanged(SeekBar seekBar, int progress,
				boolean fromUser) {
			// TODO Auto-generated method stub
			if (progress==0) {
				progress=1;
			}
			mXWalkView.zoomBy((float) (progress/10.0));
			canZoomText.setText(ZOOMRANGE + "Can zoom in: " + mXWalkView.canZoomIn() + 
					" Can zoom out: " + mXWalkView.canZoomOut());
		}
	});

        mXWalkView.load("file:///android_asset/zoom.html", null);
    }
}
