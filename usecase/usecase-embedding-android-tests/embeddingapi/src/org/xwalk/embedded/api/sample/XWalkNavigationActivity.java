// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkNavigationHistory;
import org.xwalk.core.XWalkNavigationItem;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageButton;
import android.widget.TextView;

public class XWalkNavigationActivity extends XWalkActivity {
    private XWalkView mXWalkView;
    private ImageButton mNextButton;
    private ImageButton mPrevButton;

    String url, originalUrl, title;
    TextView text1, text2, text3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    private void showNavigationItemInfo(XWalkNavigationItem navigationItem){
        url = navigationItem.getUrl();
        originalUrl = navigationItem.getOriginalUrl();
        title = navigationItem.getTitle();

        text1.setText(title);
        text2.setText(url);
        text3.setText(originalUrl);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can forward and backward history.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Search some in baidu page, and click some some searched links.\n")
        .append("2. Click the go backward button and then cilck go forward button.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app history can go backward and go forward.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
 
        setContentView(R.layout.navigation_layout);
        mPrevButton = (ImageButton) findViewById(R.id.prev);
        mNextButton = (ImageButton) findViewById(R.id.next);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        text1 = (TextView) super.findViewById(R.id.text1);
        text2 = (TextView) super.findViewById(R.id.text2);
        text3 = (TextView) super.findViewById(R.id.text3);

        mPrevButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // Go backward
                if (mXWalkView != null &&
                        mXWalkView.getNavigationHistory().canGoBack()) {
                    mXWalkView.getNavigationHistory().navigate(
                            XWalkNavigationHistory.Direction.BACKWARD, 1);
                }
                XWalkNavigationItem navigationItem = mXWalkView.getNavigationHistory().getCurrentItem();
                showNavigationItemInfo(navigationItem);
            }
        });

        mNextButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // Go forward
                if (mXWalkView != null &&
                        mXWalkView.getNavigationHistory().canGoForward()) {
                    mXWalkView.getNavigationHistory().navigate(
                            XWalkNavigationHistory.Direction.FORWARD, 1);
                }
                XWalkNavigationItem navigationItem = mXWalkView.getNavigationHistory().getCurrentItem();
                showNavigationItemInfo(navigationItem);
            }
        });

        mXWalkView.load("http://www.baidu.com/", null);
    }
}