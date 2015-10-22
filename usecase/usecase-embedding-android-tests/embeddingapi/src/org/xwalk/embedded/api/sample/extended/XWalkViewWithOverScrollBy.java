package org.xwalk.embedded.api.sample.extended;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

public class XWalkViewWithOverScrollBy extends XWalkActivity implements OverScrollXWalkView.ScrollOverListener {

    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_over_scroll_by);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies overScrollBy work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'onOverScrolled is invoked. Parameter: ' \n\n" +
                        "is shown with parameter list after touching screen.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        OverScrollXWalkView mXWalkView = (OverScrollXWalkView) findViewById(R.id.scroll_by_xwalk_view);
        mXWalkView.setScrollOverListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.scroll_by_label);
    }

    @Override
    public void onScrollOver(String msg){
        if(null != tv) {
            tv.setText(msg);
        }
    }
}
