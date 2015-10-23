package org.xwalk.embedded.api.sample.extended;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;

public class XWalkViewWithFocusChanged  extends XWalkActivity implements MyXWalkView.FocusChangedListener {

    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_focus_changed);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onFocusChanged work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the msg 'onFocusChanged is invoked' and it's parameter list is shown\n\n")
                .append(" after user clicked the text field and XWalkView.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        MyXWalkView mXWalkView = (MyXWalkView) findViewById(R.id.focus_xwalk_view);
        mXWalkView.setFocuseChangedListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.focus_tip_label);
    }

    @Override
    public void informFocuseChanged(String msg){
        if(null != tv){
            tv.setText(msg);
        }
    }
}
