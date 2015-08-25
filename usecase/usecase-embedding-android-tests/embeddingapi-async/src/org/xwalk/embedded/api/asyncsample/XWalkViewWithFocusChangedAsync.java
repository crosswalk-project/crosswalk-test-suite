package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;


import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

public class XWalkViewWithFocusChangedAsync extends Activity implements XWalkInitializer.XWalkInitListener, MyXWalkView.FocusChangedListener {

    private XWalkInitializer mXWalkInitializer;

    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void onXWalkInitStarted() {

    }

    @Override
    public void onXWalkInitCancelled() {

    }

    @Override
    public void onXWalkInitFailed() {

    }

    @Override
    public void onXWalkInitCompleted() {
        setContentView(R.layout.activity_xwalk_view_with_focus_changed_async);
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
