// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.os.Bundle;
import android.view.inputmethod.EditorInfo;
import android.view.inputmethod.InputConnection;
import android.view.inputmethod.InputConnectionWrapper;
import android.widget.LinearLayout;

public class XWalkWithInputConnection extends XWalkActivity {
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.container);        
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can use onCreateInputConnection method.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Input some words in baidu input box.\n")
        .append("2. Finally you just get 'HAHA'.\n\n")        
        .append("Expected Result:\n\n")
        .append("Test passes if you just get 'HAHA'.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        
        LinearLayout parent = (LinearLayout) findViewById(R.id.container);

        mXWalkView = new myXWalkView(this, this);
        parent.addView(mXWalkView);
        mXWalkView.load("http://www.baidu.com", null);
    }
    
    private class myXWalkView extends XWalkView {

        public myXWalkView(Context context, Activity activity) {
            super(context, activity);
            // TODO Auto-generated constructor stub
        }

        @Override
        public InputConnection onCreateInputConnection(EditorInfo ei) {
            // TODO Auto-generated method stub
            InputConnection inputConnection = super.onCreateInputConnection(ei);
            if (inputConnection != null) {
                return new LimitInputConnection(inputConnection, false);
            }
            return null;
        }
    }
    
    private class LimitInputConnection extends InputConnectionWrapper {
    
        public LimitInputConnection(InputConnection target, boolean mutable) {
            super(target, mutable);
            // TODO Auto-generated constructor stub
        }

        @Override
        public boolean commitText(CharSequence text, int newCursorPosition) {
            // TODO Auto-generated method stub
            return super.commitText("HAHA", 1);
        }
    }
}

