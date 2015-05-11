// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.maximum.app;

import java.util.ArrayList;
import java.util.List;


import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TabHost;
import android.widget.TextView;
import android.widget.CheckBox;
import android.widget.Toast;

public class XWalkBaseTabActivity extends Activity implements
TabHost.TabContentFactory {
    protected List<CheckBox> checkBoxList = new ArrayList<CheckBox>();

    protected Button mDetailInfoButton;
    protected StringBuffer message;
    protected TextView textDes;

    protected int url_index = 0;
    protected int view_num = 0;
    protected int count_num = 0;
    protected int change_num = 0;
    protected RelativeLayout root;
    protected RelativeLayout view_root;
    protected Button mAddViewsButton;
    protected Button mExitViewsButton;
    protected TextView textResultTextView;
    protected EditText views_num_text;

    //CheckBox for URL
    protected CheckBox cb_yahoo;
    protected CheckBox cb_sina;
    protected CheckBox cb_qq;
    protected CheckBox cb_sohu;
    protected CheckBox cb_bing;
    protected CheckBox cb_w3;
    protected CheckBox cb_163;

    protected TabHost tabHost;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.view_tab_scroll);

        root = (RelativeLayout) findViewById(R.id.view_tab_scroll);
        view_root = (RelativeLayout) findViewById(R.id.view_root);
        textDes = (TextView)findViewById(R.id.xwalk_des);
        textDes.setText("This sample demonstrates the maximum of SurfaceViews could be opend.");

        textResultTextView = (TextView)findViewById(R.id.result_show);

        views_num_text = (EditText) findViewById(R.id.views_num);

        cb_yahoo = (CheckBox) findViewById(R.id.cb_yahoo);
        checkBoxList.add(cb_yahoo);
        cb_sina = (CheckBox) findViewById(R.id.cb_sina);
        checkBoxList.add(cb_sina);
        cb_qq = (CheckBox) findViewById(R.id.cb_qq);
        checkBoxList.add(cb_qq);
        cb_sohu = (CheckBox) findViewById(R.id.cb_sohu);
        checkBoxList.add(cb_sohu);
        cb_bing = (CheckBox) findViewById(R.id.cb_bing);
        checkBoxList.add(cb_bing);
        cb_w3 = (CheckBox) findViewById(R.id.cb_w3);
        checkBoxList.add(cb_w3);
        cb_163 = (CheckBox) findViewById(R.id.cb_163);
        checkBoxList.add(cb_163);

        for(CheckBox checkBox : checkBoxList) {
        	checkBox.setOnCheckedChangeListener(listener);
        }

        mAddViewsButton = (Button) findViewById(R.id.run_add);
        mExitViewsButton = (Button) findViewById(R.id.run_exit);

        // 从布局中获取TabHost并建立
        tabHost = (TabHost) findViewById(R.id.myTabHost);
        tabHost.setup();
    }

    @Override
    public View createTabContent(String tag)
    {
        final TextView tv = new TextView(this);
        tv.setText("Content for tab with tag " + tag);
        return tv;
    }

    protected void showDetailInfo(final Context context) {
        mDetailInfoButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new  AlertDialog.Builder(context)
                .setTitle("Info" )
                .setMessage(message.toString())
                .setPositiveButton("confirm" ,  null )
                .show();
            }
        });
    }

    CompoundButton.OnCheckedChangeListener listener = new CompoundButton.OnCheckedChangeListener() {

        @Override
        public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
            CheckBox box = (CheckBox) buttonView;  
            if(box.isChecked()) {
                checkBoxList.add(box);
            } else {
                if(checkBoxList.size() <= 1) {
                    Toast.makeText(getApplicationContext(),  
                            "At least one url checkbox should be Selected",
                            Toast.LENGTH_LONG).show();
                    box.setChecked(true);
                    return;
                }
                checkBoxList.remove(box);
            }

        }
    };
}
