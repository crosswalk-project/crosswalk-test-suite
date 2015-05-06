// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.maximum.app;

import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;

public class AddSurfaceViewsActivity extends XWalkBaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mAddViewsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int add_num = 0;
                int max_num = view_num;
                if(!TextUtils.isEmpty(views_num_text.getText())){
                    add_num = Integer.valueOf(views_num_text.getText().toString());
                    max_num = max_num + add_num;
                }
                int len = checkBoxList.size();
                for(int i = view_num; i < max_num; i++) {
                    if (url_index >= len) {
                    	url_index = 0;
                    }
                    XWalkView mXWalkView = new XWalkView(AddSurfaceViewsActivity.this, AddSurfaceViewsActivity.this);
                    mXWalkView.setUIClient(new TestXWalkUIClientBase(mXWalkView));
                    mXWalkView.setX(i * 10);
                    mXWalkView.setY(380 + i * 10);
                    mXWalkView.load(checkBoxList.get(url_index).getText().toString(), null);
                    url_index++;
                    mAddViewsButton.setClickable(false);
                    view_root.addView(mXWalkView, 400, 400);
                }
                view_num = view_num + add_num;
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

    class TestXWalkUIClientBase extends XWalkUIClient {

        public TestXWalkUIClientBase(XWalkView arg0) {
            super(arg0);
        }

        @Override
        public void onPageLoadStopped(XWalkView view, String url, LoadStatus status) {
            count_num++;
            if(count_num == view_num) {
                mAddViewsButton.setClickable(true);
            }
            textResultTextView.setText(String.valueOf(count_num));
            super.onPageLoadStopped(view, url, status);
        }
    }
}
