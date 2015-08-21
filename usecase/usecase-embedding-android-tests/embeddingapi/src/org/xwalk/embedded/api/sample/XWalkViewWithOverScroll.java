package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;

public class XWalkViewWithOverScroll extends XWalkActivity implements MyXWalkView.ScrollOverListener{

    private TextView tv;

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onOverScrolled work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'onOverScrolled is invoked. Parameter: ' \n\n" +
                        "is shown with parameter list after touching screen.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        MyXWalkView mXWalkView = (MyXWalkView) findViewById(R.id.scroll_xwalk_view);
        mXWalkView.setScrollOverListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.scroll_label);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_over_scroll);
    }

    @Override
    public void onScrollOver(String msg){
        if(null != tv) {
            tv.setText(msg);
        }
    }
}
