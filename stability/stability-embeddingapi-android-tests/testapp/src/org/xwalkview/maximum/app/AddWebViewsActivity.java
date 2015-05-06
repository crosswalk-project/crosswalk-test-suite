// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.maximum.app;


import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class AddWebViewsActivity extends XWalkBaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.view_maximum);

        mAddViewsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int max_num = view_num;
                if(!TextUtils.isEmpty(views_num_text.getText())){
                    change_num = Integer.valueOf(views_num_text.getText().toString());
                    max_num = max_num + change_num;
                }
                int len = checkBoxList.size();
                for(int i = view_num; i < max_num; i++) {
                	if (url_index >= len) {
                    	url_index = 0;
                    }
                    WebView webView = new WebView(AddWebViewsActivity.this);
                    webView.setWebViewClient(new TestWebViewClientBase());
                    webView.setX(i * 10);
                    webView.setY(380 + i * 10);
                    webView.getSettings().setJavaScriptEnabled(true);
                    webView.loadUrl(checkBoxList.get(url_index).getText().toString());
                    url_index++;

                    mAddViewsButton.setClickable(false);
                    view_root.addView(webView, 400, 400);
                }
                view_num = view_num + change_num;
            }
        });

        mExitViewsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                System.exit(0);
            }
        });
        setContentView(root);
    }

    class TestWebViewClientBase extends WebViewClient {
        @Override
        public void onPageFinished(WebView view, String url) {
            count_num++;
            if(count_num == view_num) {
                mAddViewsButton.setClickable(true);
            }
            textResultTextView.setText(String.valueOf(count_num));
            super.onPageFinished(view, url);
        }
    }
}
