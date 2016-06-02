// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.client;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup.LayoutParams;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

public class XWalkViewWithFindText extends XWalkActivity {
    private XWalkView mXWalkView;
    private LinearLayout mLinearLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mLinearLayout = new LinearLayout(this);
        mLinearLayout.setOrientation(LinearLayout.VERTICAL);
        mLinearLayout.setShowDividers(LinearLayout.SHOW_DIVIDER_MIDDLE);
        mLinearLayout.setLayoutParams(new LayoutParams(LayoutParams.WRAP_CONTENT,
                LayoutParams.WRAP_CONTENT));
        setContentView(mLinearLayout);
        
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies findAll, findNext and clearMatches of XWalkView can work.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Input the content that you want to find.\n")
        .append("2. Click 'Find All', 'Find Next', 'Find Previous', 'Clear Matches' to check the function.\n")
        .append("Expected Result:\n\n")
        .append("The content can be found on the page, the buttons can work normally");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        final EditText editText = new EditText(this);
        editText.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT, 100));
        mLinearLayout.addView(editText);

        LinearLayout row1 = new LinearLayout(this);
        row1.setOrientation(LinearLayout.HORIZONTAL);
        row1.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT));
        LinearLayout row2 = new LinearLayout(this);
        row2.setOrientation(LinearLayout.HORIZONTAL);
        row2.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT));

        mLinearLayout.addView(row1);
        mLinearLayout.addView(row2);

        Button findAllBtn = new Button(this);
        findAllBtn.setText("Find All");
        findAllBtn.setLayoutParams(new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));
        row1.addView(findAllBtn);

        Button clearBtn = new Button(this);
        clearBtn.setText("Clear Matches");
        clearBtn.setLayoutParams(new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));
        row1.addView(clearBtn);

        Button findNextBtn = new Button(this);
        findNextBtn.setText("Find Next");
        findNextBtn.setLayoutParams(new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));
        row2.addView(findNextBtn);

        Button findPreviousBtn = new Button(this);
        findPreviousBtn.setText("Find Previous");
        findPreviousBtn.setLayoutParams(new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));
        row2.addView(findPreviousBtn);



        findAllBtn.setOnClickListener(new OnClickListener(){
			@Override
			public void onClick(View v) {
				final String contentString = (editText.getText() == null ? "" : editText.getText().toString());
				mXWalkView.findAllAsync(contentString);
			}
        });
        findNextBtn.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				mXWalkView.findNext(true);
			}
		});
        findPreviousBtn.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				mXWalkView.findNext(false);
			}
		});
        clearBtn.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				mXWalkView.clearMatches();
			}
		});
        mXWalkView = new XWalkView(this);
        mXWalkView.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT,
                LayoutParams.MATCH_PARENT));
        mLinearLayout.addView(mXWalkView);
        mXWalkView.load("file:///android_asset/index4995_local_text.html", null);
    }
}
