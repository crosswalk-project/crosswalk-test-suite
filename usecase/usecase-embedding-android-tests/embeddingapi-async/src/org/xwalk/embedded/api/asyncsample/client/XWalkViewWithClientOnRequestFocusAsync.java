package org.xwalk.embedded.api.asyncsample.client;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithClientOnRequestFocusAsync extends Activity implements XWalkInitializer.XWalkInitListener{

    private XWalkInitializer mXWalkInitializer;

    private XWalkView mXWalkView;

    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

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
        setContentView(R.layout.activity_xwalk_view_with_client_on_request_focus_async);
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
