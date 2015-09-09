package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;

public class XWalkViewWithLongClickAsync extends Activity implements XWalkInitializer.XWalkInitListener, MessageInfoXWalkView.MessageListener {

    private XWalkInitializer mXWalkInitializer;

    private MessageInfoXWalkView mXWalkView;

    private TextView listener_tv;

    private TextView perform_tv;

    private Button hb;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void onMessageSent(String msg) {
        if(null != perform_tv){
            perform_tv.setText(msg);
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
        setContentView(R.layout.activity_xwalk_view_with_long_click_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies OnLongClickListener and performLongClick work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes \n\n" +
                        "1\\ if the invoking message is shown once user clicking the button to execute 'performLongClick'.\n\n" +
                        "2\\ if the OnLongClickListener is triggered once the user long click on the XWalkView");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        listener_tv = (TextView)findViewById(R.id.listener_msg_label);
        listener_tv.setTextColor(Color.GREEN);

        perform_tv = (TextView)findViewById(R.id.perform_msg_label);
        perform_tv.setTextColor(Color.GREEN);

        mXWalkView = (MessageInfoXWalkView) findViewById(R.id.win_changed_xwalk_view);
        mXWalkView.setMessageListener(this);

        mXWalkView.setOnLongClickListener(new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View v) {
                listener_tv.setText("OnLongClickListener is triggered. view:" + v.getClass());
                return false;
            }
        });
        mXWalkView.load("http://www.baidu.com", null);

        hb = (Button)findViewById(R.id.invoke_button);
        hb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mXWalkView.performLongClick();
            }
        });

        Button clearBt = (Button)findViewById(R.id.clear_button);
        clearBt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                listener_tv.setText("");
                perform_tv.setText("");
            }
        });
    }
}
