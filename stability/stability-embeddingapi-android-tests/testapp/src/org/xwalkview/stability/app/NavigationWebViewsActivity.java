// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.stability.app;

import org.xwalkview.stability.base.XWalkBaseNavigationActivity;
import org.xwalkview.stability.base.XWalkBaseUtil;
import android.text.TextUtils;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class NavigationWebViewsActivity extends XWalkBaseNavigationActivity {
    private WebView webView;

    @Override
    protected void onXWalkReady() {
        XWalkBaseUtil.createStorageFile(false);
        textDes.setText("This sample demonstrates long time navigation with different web pages in WebView.");
        
        webView = new WebView(NavigationWebViewsActivity.this);
        webView.setWebViewClient(new TestWebViewClientBase());
        webView.getSettings().setJavaScriptEnabled(true);        
        view_root.addView(webView);
        
        if(!TextUtils.isEmpty(views_num_text.getText())){
            view_num = Integer.valueOf(views_num_text.getText().toString());
        }
        
        mAddViewsButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                webView.loadUrl(checkBoxList.get(url_index).getText().toString());
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
                if (webView != null &&
                        webView.canGoBack()) {
                    webView.goBack();
                }
            }
        });
        mNextButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // Go forward
                if (webView != null &&
                        webView.canGoForward()) {
                    webView.goForward();
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

    class TestWebViewClientBase extends WebViewClient {
        @Override
        public void onPageFinished(WebView view, String url) {
            count_num++;
            textResultTextView.setText(String.valueOf(count_num));

            if (count_num < view_num) {
            	mAddViewsButton.performClick();
            }
            if (count_num == view_num) {
            	XWalkBaseUtil.createStorageFile(true);
            }
            super.onPageFinished(view, url);
        }
    }
}
