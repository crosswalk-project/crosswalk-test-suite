// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.stability.app;

import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;
import org.xwalkview.stability.base.XWalkBaseVideoActivity;
import android.text.TextUtils;
import android.view.Gravity;
import android.view.View;
import android.widget.FrameLayout;

public class VideoXWalkViewsActivity extends XWalkBaseVideoActivity {

    @Override
    protected void onXWalkReady() {
        textDes.setText("This sample demonstrates the feasibility to create and destroy many XWalkViews at same time to load webpages with playing video.");
        XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, true);
        mAddViewsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int add_num = 0;
                int max_num = view_num;
                if(!TextUtils.isEmpty(views_num_text.getText())){
                    add_num = Integer.valueOf(views_num_text.getText().toString());
                    max_num = max_num + add_num;
                    int len = checkBoxList.size();
                    for(int i = view_num; i < max_num; i++) {
                        if (url_index >= len) {
                            url_index = 0;
                        }
                        XWalkView mXWalkView = new XWalkView(VideoXWalkViewsActivity.this, VideoXWalkViewsActivity.this);
                        mXWalkView.setId(i);
                        mXWalkView.setUIClient(new TestXWalkUIClientBase(mXWalkView));
                        mXWalkView.load(checkBoxList.get(url_index).getText().toString(), null);
                        url_index++;
                        mAddViewsButton.setClickable(false);

                        FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(view_root.getWidth() - i * 10, view_root.getHeight() - i * 10);
                        params.gravity = Gravity.CENTER;
                        mXWalkView.setLayoutParams(params);
                        view_root.addView(mXWalkView);
                    }
                    view_num = view_num + add_num;
                }
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
            String idStr = String.valueOf(view.getId());
            if(!idList.contains(idStr)){
                idList.add(idStr);
                count_num++;
                if(count_num == view_num) {
                    mAddViewsButton.setClickable(true);
                }
                textResultTextView.setText(String.valueOf(count_num));
            }
            super.onPageLoadStopped(view, url, status);
        }
    }
}
