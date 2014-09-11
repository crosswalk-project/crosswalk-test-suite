// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding;


import org.xwalk.core.XWalkView;
import org.xwalk.embedding.test.R;

import android.app.Activity;
import android.os.Bundle;

public class MainActivity extends Activity {

    protected XWalkView mXWalkView;

    public XWalkView getXWalkView()
    {
        return mXWalkView;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.xwview_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
    }
}
