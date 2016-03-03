// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.misc;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.view.View;

public class XWalkViewWithThemeColorAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;

    private TextView themeValue;

@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public final void onXWalkInitStarted() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitCancelled() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitFailed() {
        // Do crash or logging or anything else in order to let the tester know if this method get called
    }

    @Override
    public final void onXWalkInitCompleted() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can work with theme-color meta tag by setting XWalkPreferences.ENABLE_THEME_COLOR. Notice this feature only works on Android Lollipop or later.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Default XWalkPreferences theme-color is enabled, just load the page.\n")
        .append("2. Click android recent-apps button to see our app status.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if recent app list can show red toolbar XWalkView.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.activity_xwalk_view_with_theme_color_async);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);

        mXWalkView.load("file:///android_asset/red_toolbar_theme.html", null);

        Button bt = (Button)findViewById(R.id.refresh_button);
        themeValue= (TextView)findViewById(R.id.theme_colcr_preference);
        bt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Boolean value = XWalkPreferences.getBooleanValue(XWalkPreferences.ENABLE_THEME_COLOR);
                themeValue.setText("XWalkPreferences.ENABLE_THEME_COLOR is " + value);
            }
        });
    }
}
