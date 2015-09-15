package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithClientOnRequestFocus extends XWalkActivity {

    private XWalkView mXWalkView;

    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_client_on_request_focus);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies XWalkUIClient.onRequestFocus work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message 'XWalkUIClient.onRequestFocus is invoked'")
                .append(" is shown below after clicking the HTML link to load another page in XWalkView.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (XWalkView) findViewById(R.id.client_focus_xwalk_view);
        mXWalkView.load("file:///android_asset/frames/frameMain.html", null);
        mXWalkView.setUIClient(new XWalkUIClient(mXWalkView) {
            @Override
            public void onRequestFocus(XWalkView view) {
                tv.setText("XWalkUIClient.onRequestFocus is invoked");
                super.onRequestFocus(view);
            }
        });

        tv = (TextView)findViewById(R.id.client_focus_tip);
        tv.setTextColor(Color.GREEN);
    }
}
