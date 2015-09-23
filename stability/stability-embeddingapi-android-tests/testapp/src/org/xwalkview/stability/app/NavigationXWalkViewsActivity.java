// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.stability.app;


import org.xwalk.core.XWalkNavigationHistory;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;
import org.xwalkview.stability.base.XWalkBaseNavigationActivity;
import org.xwalkview.stability.base.XWalkBaseUtil;

import android.text.TextUtils;
import android.view.Gravity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.FrameLayout;


public class NavigationXWalkViewsActivity extends XWalkBaseNavigationActivity {
    private XWalkView mXWalkView;

    @Override
    protected void onXWalkReady() {
        XWalkBaseUtil.createStorageFile(false);
        textDes.setText("This sample demonstrates long time navigation with different web pages in XWalkView.");

        mXWalkView = new XWalkView(NavigationXWalkViewsActivity.this, NavigationXWalkViewsActivity.this);
        mXWalkView.setUIClient(new TestXWalkUIClientBase(mXWalkView));  
        FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(view_root.getWidth(), 1000);
        params.gravity = Gravity.CENTER;
        mXWalkView.setLayoutParams(params);        
        view_root.addView(mXWalkView);
        
        if(!TextUtils.isEmpty(views_num_text.getText())){
            view_num = Integer.valueOf(views_num_text.getText().toString());
        }
        
        mAddViewsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mXWalkView.load(checkBoxList.get(url_index).getText().toString(), null);
                url_index++;
            }
        });
        mExitViewsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                System.exit(0);
            }
        });
        mPrevButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // Go backward
                if (mXWalkView != null &&
                        mXWalkView.getNavigationHistory().canGoBack()) {
                    mXWalkView.getNavigationHistory().navigate(
                            XWalkNavigationHistory.Direction.BACKWARD, 1);
                }
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
            }
        });

        if(hasPerform == false && isWindowReady == true) {
            mAddViewsButton.performClick();
            hasPerform = true;
        }
        isXwalkReady = true;
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if(hasFocus == true && isXwalkReady == true && hasPerform == false){
            mAddViewsButton.performClick();
            hasPerform = true;
        }
        isWindowReady = true;
    }

    class TestXWalkUIClientBase extends XWalkUIClient {

        public TestXWalkUIClientBase(XWalkView arg0) {
            super(arg0);
        }

        @Override
        public void onPageLoadStopped(XWalkView view, String url, LoadStatus status) {
            count_num++;
            textResultTextView.setText(String.valueOf(count_num));
            if (count_num < view_num) {
            	mAddViewsButton.performClick();
            }
            if (count_num == view_num) {
            	XWalkBaseUtil.createStorageFile(true);
            }
            super.onPageLoadStopped(view, url, status);
        }
    }
}
