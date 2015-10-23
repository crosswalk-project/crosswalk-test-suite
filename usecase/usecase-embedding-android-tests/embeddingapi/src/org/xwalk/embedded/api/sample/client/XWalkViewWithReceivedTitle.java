package org.xwalk.embedded.api.sample.client;

import org.xwalk.embedded.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithReceivedTitle extends XWalkActivity{

    private XWalkView mXWalkView;

    private Activity thisActivity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_received_title);
    }

    @Override
    protected void onXWalkReady() {
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
                if(!TextUtils.isEmpty(title)) {
                    thisActivity.setTitle(title);
                }
            }
        });
    }
}
