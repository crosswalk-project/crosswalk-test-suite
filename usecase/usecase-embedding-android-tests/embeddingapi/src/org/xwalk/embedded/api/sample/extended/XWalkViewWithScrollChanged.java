package org.xwalk.embedded.api.sample.extended;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

public class XWalkViewWithScrollChanged extends XWalkActivity implements ScrollChangedXWalkView.ScrollChangedListener{

    private TextView tv;

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onScrollChanged work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the the message\n\n" +
                        "'onScrollChanged is invoked' and it's parameter list is shown after you scroll the page");

        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        tv = (TextView)findViewById(R.id.scroll_changed_label);

        XWalkView view = (XWalkView)findViewById(R.id.scroll_changed_xwalk_view);
        ScrollChangedXWalkView mScrollChangedXWalkView = (ScrollChangedXWalkView)view;
        mScrollChangedXWalkView.setScrollChangedListener(this);
        view.load("http://www.baidu.com", null);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_scroll_changed);
    }

    @Override
    public void informScrollChanged(String msg) {
        if(null != tv){
            tv.setText(msg);
        }
    }
}
