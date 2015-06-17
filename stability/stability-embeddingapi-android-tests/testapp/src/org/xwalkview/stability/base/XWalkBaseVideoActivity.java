// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalkview.stability.base;

import java.util.ArrayList;
import java.util.List;

import org.xwalk.core.XWalkActivity;
import org.xwalkview.stability.app.R;

import android.os.Bundle;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.CheckBox;
import android.widget.Toast;

public abstract class XWalkBaseVideoActivity extends XWalkActivity {
	protected List<CheckBox> checkBoxList = new ArrayList<CheckBox>();
	protected List<String> idList = new ArrayList<String>();

    protected Button mDetailInfoButton;
    protected StringBuffer message;
    protected TextView textDes;

    protected int url_index = 0;
    protected int view_num = 0;
    protected int count_num = 0;
    protected int change_num = 0;
    protected LinearLayout root;
    protected FrameLayout view_root;
    protected Button mAddViewsButton;
    protected Button mExitViewsButton;
    protected TextView textResultTextView;
    protected EditText views_num_text;

    //CheckBox for URL
    protected CheckBox cb_localvideo;

    CompoundButton.OnCheckedChangeListener listener = new CompoundButton.OnCheckedChangeListener() {  

        @Override  
        public void onCheckedChanged(CompoundButton buttonView,  
                boolean isChecked) {
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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.view_video);

        root = (LinearLayout) findViewById(R.id.view_video);
        view_root = (FrameLayout) findViewById(R.id.view_root);
        textDes = (TextView)findViewById(R.id.xwalk_des);
        textResultTextView = (TextView)findViewById(R.id.result_show);

        views_num_text = (EditText) findViewById(R.id.views_num);

        cb_localvideo = (CheckBox) findViewById(R.id.cb_localvideo);
        checkBoxList.add(cb_localvideo);


        for(CheckBox checkBox : checkBoxList) {
            checkBox.setOnCheckedChangeListener(listener);
        }

        mAddViewsButton = (Button) findViewById(R.id.run_add);
        mExitViewsButton = (Button) findViewById(R.id.run_exit);
    }

}
