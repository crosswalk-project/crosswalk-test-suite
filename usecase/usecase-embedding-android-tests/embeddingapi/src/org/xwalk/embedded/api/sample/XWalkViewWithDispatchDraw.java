package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.os.Bundle;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

public class XWalkViewWithDispatchDraw extends XWalkActivity {

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies dispatchDraw work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the image of Android Robot is shown on left-top.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        XWalkView mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mXWalkView.load("http://www.baidu.com", null);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_dispatch_draw);
    }
}
