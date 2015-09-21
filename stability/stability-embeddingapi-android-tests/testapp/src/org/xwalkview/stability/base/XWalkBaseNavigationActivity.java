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
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.CheckBox;
import android.widget.Toast;


public abstract class XWalkBaseNavigationActivity extends XWalkActivity {
    protected boolean isXwalkReady = false;
    protected boolean isWindowReady = false;
    protected boolean hasPerform = false;

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
    protected CheckBox home_sina;
    protected CheckBox news_sina;
    protected CheckBox finance_sina;
    protected CheckBox tech_sina;
    protected CheckBox sports_sina;
    protected CheckBox ent_sina;
    protected CheckBox auto_sina;
    protected CheckBox blog_sina;
    protected CheckBox games_sina;
    protected CheckBox video_sina;
    protected CheckBox home_jd;
    protected CheckBox fashion_jd;
    protected CheckBox beautysale_jd;
    protected CheckBox chaoshi_jd;
    protected CheckBox sports_jd;
    protected CheckBox hk_jd;
    protected CheckBox red_jd;
    protected CheckBox jr_jd;
    protected CheckBox baby_jd;
    protected CheckBox book_jd;   
    protected ImageButton mPrevButton;
    protected ImageButton mNextButton;

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
        setContentView(R.layout.view_navigation);

        root = (LinearLayout) findViewById(R.id.view_navigation);
        view_root = (FrameLayout) findViewById(R.id.view_root);
        textDes = (TextView)findViewById(R.id.xwalk_des);
        textResultTextView = (TextView)findViewById(R.id.result_show);

        views_num_text = (EditText) findViewById(R.id.views_num);

        home_sina = (CheckBox) findViewById(R.id.home_sina);
        checkBoxList.add(home_sina);
        news_sina = (CheckBox) findViewById(R.id.news_sina);
        checkBoxList.add(news_sina);
        finance_sina = (CheckBox) findViewById(R.id.finance_sina);
        checkBoxList.add(finance_sina);
        tech_sina = (CheckBox) findViewById(R.id.tech_sina);
        checkBoxList.add(tech_sina);
        sports_sina = (CheckBox) findViewById(R.id.sports_sina);
        checkBoxList.add(sports_sina);
        ent_sina = (CheckBox) findViewById(R.id.ent_sina);
        checkBoxList.add(ent_sina);
        auto_sina = (CheckBox) findViewById(R.id.auto_sina);
        checkBoxList.add(auto_sina);
        blog_sina = (CheckBox) findViewById(R.id.blog_sina);
        checkBoxList.add(blog_sina);
        games_sina = (CheckBox) findViewById(R.id.games_sina);
        checkBoxList.add(games_sina);
        video_sina = (CheckBox) findViewById(R.id.video_sina);
        checkBoxList.add(video_sina);
        home_jd = (CheckBox) findViewById(R.id.home_jd);
        checkBoxList.add(home_jd);
        fashion_jd = (CheckBox) findViewById(R.id.fashion_jd);
        checkBoxList.add(fashion_jd);
        beautysale_jd = (CheckBox) findViewById(R.id.beautysale_jd);
        checkBoxList.add(beautysale_jd);
        chaoshi_jd = (CheckBox) findViewById(R.id.chaoshi_jd);
        checkBoxList.add(chaoshi_jd);
        sports_jd = (CheckBox) findViewById(R.id.sports_jd);
        checkBoxList.add(sports_jd);
        hk_jd = (CheckBox) findViewById(R.id.hk_jd);
        checkBoxList.add(hk_jd);
        red_jd = (CheckBox) findViewById(R.id.red_jd);
        checkBoxList.add(red_jd);
        jr_jd = (CheckBox) findViewById(R.id.jr_jd);
        checkBoxList.add(jr_jd);
        baby_jd = (CheckBox) findViewById(R.id.baby_jd);
        checkBoxList.add(baby_jd);
        book_jd = (CheckBox) findViewById(R.id.book_jd);
        checkBoxList.add(book_jd);         

        for(CheckBox checkBox : checkBoxList) {
            checkBox.setOnCheckedChangeListener(listener);
        }

        mAddViewsButton = (Button) findViewById(R.id.run_add);
        mExitViewsButton = (Button) findViewById(R.id.run_exit);
        mPrevButton = (ImageButton) findViewById(R.id.prev);
        mNextButton = (ImageButton) findViewById(R.id.next);
    }

}
