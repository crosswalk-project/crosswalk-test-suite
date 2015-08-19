package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

public class XWalkViewWithDispatchDrawAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;

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

        setContentView(R.layout.activity_xwalk_view_with_dispatch_draw_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies XWalkView can disable back button.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if case can't backwards by pressing back key.");
        new  AlertDialog.Builder(this)
                .setTitle("Info" )
                .setMessage(mess.toString())
                .setPositiveButton("confirm" ,  null )
                .show();
        mXWalkView = (XWalkView) findViewById(R.id.dispatch_xwalk_view);
        mXWalkView.load("http://www.baidu.com/", null);
    }
}
