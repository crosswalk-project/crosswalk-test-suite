package org.xwalk.embedded.api.sample.extended;

import org.xwalk.embedded.api.sample.R;
import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

public class XWalkViewWithOnTouchEvent extends XWalkActivity implements MyXWalkView.TouchEventListener {

    private TextView tv;

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onTouchEvent work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the the message\n\n" +
                        "'onTouchEvent is invoked; Action is UP/DOWN/MOVE' ");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        tv = (TextView)findViewById(R.id.touch_event_label);

        XWalkView view = (XWalkView)findViewById(R.id.touch_event_xwalk_view);
        MyXWalkView mMyXWalkView = (MyXWalkView)view;
        mMyXWalkView.setTouchEventListener(this);
        view.load("http://www.baidu.com", null);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_on_touch_event);
    }

    @Override
    public void onTouchEventInvoked(String msg){
        if(null != tv) {
            tv.setText(msg);
        }
    }
}
