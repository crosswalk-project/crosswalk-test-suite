// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.setting;

import org.xwalk.embedded.api.asyncsample.R;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkSettings;
import org.xwalk.core.XWalkView;

import android.content.Context;
import android.graphics.Point;
import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.WindowManager;

public class XWalkViewSettingSetInitialPageScaleAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void onXWalkInitCancelled() {

    }

    @Override
    public void onXWalkInitStarted() {

    }

    @Override
    public void onXWalkInitFailed() {

    }

    @Override
    public void onXWalkInitCompleted() {
        setContentView(R.layout.xwview_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView Setting can setInitialPageScale.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Load the html page with whole blue background.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the blue background spans the entire screen size.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        WindowManager wm = (WindowManager) getSystemService(Context.WINDOW_SERVICE);
        Point screenSize = new Point();
        wm.getDefaultDisplay().getSize(screenSize);

        final String pageTemplate = "<html><head>"
                                + "<meta name='viewport' content='initial-scale=1.0' />"
                                + "</head><body style='margin:0; padding:0'>"
                                + "<div style='background:blue;width:" + screenSize.x
                                + "px;height:" + screenSize.y
                                + "px'>A big div</div>"
                                + "</body></html>";

        XWalkSettings settings = mXWalkView.getSettings();
        settings.setInitialPageScale(1.0f);
        mXWalkView.load(null, pageTemplate);
    }
}