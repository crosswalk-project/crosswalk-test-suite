package org.xwalk.embedded.api.asyncsample.extended;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

public class XWalkViewWithScrollChangedAsync extends Activity implements XWalkInitializer.XWalkInitListener, ScrollChangedXWalkView.ScrollChangedListener {

    private XWalkInitializer mXWalkInitializer;

    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void informScrollChanged(String msg) {
        if(null != tv) {
            tv.setText(msg);
        }
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
        setContentView(R.layout.activity_xwalk_view_with_scroll_changed_async);
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
        tv = (TextView)findViewById(R.id.scroll_changed_label);

        XWalkView view = (XWalkView)findViewById(R.id.scroll_changed_xwalk_view);
        ScrollChangedXWalkView mScrollChangedXWalkView = (ScrollChangedXWalkView)view;
        mScrollChangedXWalkView.setScrollChangedListener(this);
        view.load("http://www.baidu.com", null);
    }
}
