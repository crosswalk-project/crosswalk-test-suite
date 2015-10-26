package org.xwalk.embedded.api.asyncsample.client;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.text.TextUtils;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithReceivedTitleAsync extends Activity implements XWalkInitializer.XWalkInitListener{

    private XWalkInitializer mXWalkInitializer;

    private XWalkView mXWalkView;

    private Activity thisActivity;

    @Override
    public void onXWalkInitCancelled() {

    }

    @Override
    public void onXWalkInitStarted() {

    }

    @Override
    public void onXWalkInitFailed() {

    }

    @Override
    public void onXWalkInitCompleted() {
        setContentView(R.layout.activity_xwalk_view_with_received_title_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onReceivedTitle work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the Activity Title will be changed by submitting HTML form");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (XWalkView) findViewById(R.id.console_xwalk_view);
        mXWalkView.load("file:///android_asset/title_change.html", null);
        thisActivity = this;
        mXWalkView.setUIClient(new XWalkUIClient(mXWalkView) {
            @Override
            public void onReceivedTitle(XWalkView view, String title) {
                super.onReceivedTitle(view, title);
                if (!TextUtils.isEmpty(title)) {
                    thisActivity.setTitle(title);
                }
            }
        });
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }
}
