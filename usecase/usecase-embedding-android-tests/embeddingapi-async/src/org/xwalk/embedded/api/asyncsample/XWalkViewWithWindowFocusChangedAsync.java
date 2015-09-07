package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;

public class XWalkViewWithWindowFocusChangedAsync extends Activity implements XWalkInitializer.XWalkInitListener, MessageInfoXWalkView.MessageListener{

    private XWalkInitializer mXWalkInitializer;

    private MessageInfoXWalkView mXWalkView;

    private TextView tv;

    private Button hb;

    private Activity thisActivity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void onMessageSent(String msg) {
        if(null != tv){
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
        setContentView(R.layout.activity_xwalk_view_with_window_focus_changed_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onWindowFocusChanged work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'onWindowFocusChanged is invoked. Parameter: ' \n\n" +
                        "is shown with parameter list once user clicking the button to pop-up a new dialog.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (MessageInfoXWalkView) findViewById(R.id.win_changed_xwalk_view);
        mXWalkView.setMessageListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.windows_focus_msg_label);
        tv.setTextColor(Color.GREEN);
        thisActivity = this;
        hb = (Button)findViewById(R.id.popup_button);
        hb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AlertDialog.Builder(thisActivity)
                        .setTitle("New Window")
                        .setMessage("New window is pop-up." +
                                "Check if the invoking message is shown")
                        .setPositiveButton("confirm", null)
                        .show();
            }
        });
    }
}
