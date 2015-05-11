// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.maximum.app;

import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.TabHost.TabContentFactory;
import android.widget.TabHost.TabSpec;

public class TabTextureViewsActivity extends XWalkBaseTabActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, true);

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
                    String name = "Tab " + (i + 1);
                    TabSpec tab1 = tabHost.newTabSpec(name);
                    tab1.setIndicator(name);

                    tab1.setContent(new TabContentFactory(){

                        @Override
                        public View createTabContent(String tag) {
                            XWalkView mXWalkView = new XWalkView(TabTextureViewsActivity.this, TabTextureViewsActivity.this);
                            mXWalkView.setUIClient(new TestXWalkUIClientBase(mXWalkView));
                            mXWalkView.load(checkBoxList.get(url_index).getText().toString(), null);
                            return mXWalkView;
                        }
                    });
                    tabHost.addTab(tab1);
                    tabHost.setCurrentTab(i);
                    tabHost.performClick();
                    url_index++;
                    mAddViewsButton.setClickable(false);
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
