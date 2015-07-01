// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.stability.app;

import org.xwalkview.stability.base.XWalkBaseNavigationActivity;
import android.text.TextUtils;
import android.view.Gravity;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

public class NavigationWebViewsActivity extends XWalkBaseNavigationActivity {
    private WebView webView;

    @Override
    protected void onXWalkReady() {
        setContentView(R.layout.view_maximum);
        textDes.setText("This sample demonstrates long time navigation with different web pages in WebView.");
        mAddViewsButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                int max_num = view_num;
                if(!TextUtils.isEmpty(views_num_text.getText())){
                    change_num = Integer.valueOf(views_num_text.getText().toString());
                    max_num = max_num + change_num;
                    int len = checkBoxList.size();
                    for(int i = view_num; i < max_num; i++) {
                        if (url_index >= len) {
                            url_index = 0;
                        }
                        webView = new WebView(NavigationWebViewsActivity.this);
                        webView.setId(i);
                        webView.setWebViewClient(new TestWebViewClientBase());
                        webView.getSettings().setJavaScriptEnabled(true);
                        webView.loadUrl(checkBoxList.get(url_index).getText().toString());
                        url_index++;

                        mAddViewsButton.setClickable(false);

                        FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(view_root.getWidth() - i * 10, view_root.getHeight() - i * 10);
                        params.gravity = Gravity.CENTER;
                        view_root.addView(webView, params);
                    }
                    view_num = view_num + change_num;
                }
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
        setContentView(root);
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
            String idStr = String.valueOf(view.getId());
            if(!idList.contains(idStr)){
                idList.add(idStr);
                count_num++;
                if(count_num == view_num) {
                    mAddViewsButton.setClickable(true);
                }
                textResultTextView.setText(String.valueOf(count_num));
            }
            super.onPageFinished(view, url);
        }
    }
}
