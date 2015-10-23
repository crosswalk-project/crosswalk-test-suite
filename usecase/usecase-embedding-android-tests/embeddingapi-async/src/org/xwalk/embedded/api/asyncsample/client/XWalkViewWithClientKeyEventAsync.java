package org.xwalk.embedded.api.asyncsample.client;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.view.KeyEvent;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithClientKeyEventAsync extends Activity implements XWalkInitializer.XWalkInitListener {

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
        setContentView(R.layout.activity_xwalk_view_with_client_key_event_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies XWalkUIClient.shouldOverrideKeyEvent work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message 'XWalkUIClient.shouldOverrideKeyEvent is invoked'")
                .append(" is shown below with the KeyEvent parameter after clicking the Key.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (XWalkView) findViewById(R.id.client_keyevent_xwalk_view);
        mXWalkView.load("http://www.baidu.com", null);
        mXWalkView.setUIClient(new XWalkUIClient(mXWalkView) {
            @Override
            public boolean shouldOverrideKeyEvent(XWalkView view, KeyEvent event) {
                tv.setText("XWalkUIClient.shouldOverrideKeyEvent is invoked. Event: " + event.toString());
                return false;
            }
        });

        tv = (TextView)findViewById(R.id.client_keyevent_tip);
        tv.setTextColor(Color.GREEN);
    }
}
