package org.xwalk.embedded.api.asyncsample.extended;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;

public class XWalkViewWithOverScrollByAsync extends Activity implements XWalkInitializer.XWalkInitListener, OverScrollXWalkView.ScrollOverListener {

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
        setContentView(R.layout.activity_xwalk_view_with_over_scroll_by_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies overScrollBy work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'overScrollBy is invoked. Parameter: ' \n\n" +
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
