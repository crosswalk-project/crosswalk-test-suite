// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;


import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkDownloadListener;

import android.os.Bundle;
import org.xwalk.core.XWalkView;
import android.app.AlertDialog;
import android.widget.TextView;

public class XWalkViewWithDownloadListenerActivity extends XWalkActivity {
    private XWalkView mXWalkView;
    private TextView downloadText;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.version_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);                
    }
        
    @Override
    protected void onXWalkReady() {

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can set & get UserAgentString, meaningwhile set DownloadListener & override onDownloadStart.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Load the Baidu page and show the set UserAgentString.\n\n") 
        .append("2. Click baidu website bottom ShouJiBaidu link or any other download link.\n\n") 
        .append("Expected Result:\n\n")
        .append("Test passes if UserAgentString & download link info shows.");     
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
                
        downloadText = (TextView) findViewById(R.id.text1);
        
        mXWalkView.setUserAgentString("Chrome/44.0.2403.81 Crosswalk/15.44.376.0 Mobile Safari/537.36");
        downloadText.setText("getUserAgentString: " + mXWalkView.getUserAgentString() + "\n");       
        mXWalkView.setDownloadListener(new XWalkDownloadListener(getApplicationContext()) {
			
			@Override
			public void onDownloadStart(String url, String userAgent,
			                String contentDisposition, String mimetype, long contentLength) {
				// TODO Auto-generated method stub
				// You can realize your down here.
				downloadText.setText(downloadText.getText() + 
				                    "url: " + url + "\n" + 
				                    "userAgent: " + userAgent + "\n" + 
				                    "contentDisposition: " + contentDisposition + "\n" + 
				                    "mimeType: " + mimetype + "\n" + 
				                    "contentLength: " + contentLength);
			}
		});
        mXWalkView.load("http://m.baidu.com/", null);
    }

}
