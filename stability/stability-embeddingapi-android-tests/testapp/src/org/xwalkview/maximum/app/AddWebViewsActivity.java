// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.maximum.app;

import org.xwalk.views_maximum_test.R;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class AddWebViewsActivity extends XWalkBaseActivity {

    TextView textResultTextView;
    EditText views_num_text;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.view_maximum);
        
        root = (RelativeLayout) findViewById(R.id.view_maximum);
        view_root = (RelativeLayout) findViewById(R.id.view_root);
        textDes = (TextView)findViewById(R.id.xwalk_des);
        textDes.setText("This sample demonstrates the maximum of WebViews could be opend.");

        textResultTextView = (TextView)findViewById(R.id.result_show);
        textResultTextView.setX(0);
        textResultTextView.setY(160);
        textResultTextView.setText("0");

        views_num_text = (EditText) findViewById(R.id.views_num);
        views_num_text.setX(0);
        views_num_text.setY(220);
        views_num_text.setText("1");

        LinearLayout btnLay = (LinearLayout) findViewById(R.id.btns_lay);
        btnLay.setX(100);
        btnLay.setY(200);

        mAddViewsButton = (Button) findViewById(R.id.run_add);
        mExitViewsButton = (Button) findViewById(R.id.run_exit);
        mDestoryViewsButton = (Button) findViewById(R.id.run_destory);

        mAddViewsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int max_num = view_num;
                if(!TextUtils.isEmpty(views_num_text.getText())){
                    change_num = Integer.valueOf(views_num_text.getText().toString());
                    max_num = max_num + change_num;
                }
                for(int i = view_num; i < max_num; i++) {
                    WebView webView = new WebView(AddWebViewsActivity.this);
                    webView.setWebViewClient(new TestWebViewClientBase());
                    webView.setX(i * 10);
                    webView.setY(300 + i * 10);
                    webView.getSettings().setJavaScriptEnabled(true);
                    webView.loadUrl("https://www.yahoo.com/");
                    mAddViewsButton.setClickable(false);
                    mDestoryViewsButton.setClickable(false);
                    view_root.addView(webView, 400, 400);
                }
                view_num = view_num + change_num;
            }
        });

        mDestoryViewsButton.setOnClickListener(new View.OnClickListener() {
            
            @Override
            public void onClick(View arg0) {
                int min_num = 0;
                if(!TextUtils.isEmpty(views_num_text.getText())){
                    change_num = Integer.valueOf(views_num_text.getText().toString());
                    min_num = view_num - change_num;
                }
                if(view_num >= change_num) {
                    for(int i = view_num - 1; i >= min_num; i--) {
                        view_root.removeViewAt(i);
                        count_num--;
                    }
                    view_num = view_num - change_num;
                }
                textResultTextView.setText(String.valueOf(count_num));
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
                mDestoryViewsButton.setClickable(true);
            }
            textResultTextView.setText(String.valueOf(count_num));
            super.onPageFinished(view, url);
        }
    }
}
