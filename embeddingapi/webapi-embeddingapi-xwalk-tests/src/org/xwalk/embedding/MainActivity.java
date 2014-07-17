// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding;


import org.xwalk.core.XWalkView;
import org.xwalk.embedding.test.R;

import android.app.Activity;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;

public class MainActivity extends Activity {

    protected XWalkView mXWalkView;

    public XWalkView getXWalkView()
    {
        return mXWalkView;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        this.requestWindowFeature(Window.FEATURE_NO_TITLE);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);

        setContentView(R.layout.xwview_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
    }

    /*
     * When the activity is paused, XWalkView.onHide() and XWalkView.pauseTimers() need to be called.
     */
    @Override
    public void onPause() {
        super.onPause();
        if (mXWalkView != null) {
            mXWalkView.onHide();
            mXWalkView.pauseTimers();
        }
    }

    /*
     * When the activity is resumed, XWalkView.onShow() and XWalkView.resumeTimers() need to be called.
     */
    @Override
    public void onResume() {
        super.onResume();
        if (mXWalkView != null) {
            mXWalkView.onShow();
            mXWalkView.resumeTimers();
        }
    }

    /*
     * Call onDestroy on XWalkView to release native resources when the activity is destroyed.
     */
    @Override
    public void onDestroy() {
        super.onDestroy();
        if (mXWalkView != null) {
            mXWalkView.onDestroy();
        }
    }

}
