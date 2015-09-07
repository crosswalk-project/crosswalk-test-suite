package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;

public class XWalkViewWithWindowsVisibilityChangedAsync extends Activity implements XWalkInitializer.XWalkInitListener, MessageInfoXWalkView.MessageListener{

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
            String combineMsg = tv.getText().toString();
            if (0 == combineMsg.length()){
                combineMsg = "onWindowVisibilityChanged is invoked, visibility:" + msg;
            }else{
                combineMsg += "->" + msg;
            }

            tv.setText(combineMsg);
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
        setContentView(R.layout.activity_xwalk_view_with_windows_visibility_changed_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onWindowVisibilityChanged work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'onWindowVisibilityChanged is invoked. Parameter: ' \n\n" +
                        "is shown with parameter list once user clicking the button to open a new Window, and clicking 'Return' button back to this Activity.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (MessageInfoXWalkView) findViewById(R.id.win_visibility_xwalk_view);
        mXWalkView.setMessageListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.windows_visibility_msg_label);
        tv.setTextColor(Color.GREEN);
        thisActivity = this;
        hb = (Button)findViewById(R.id.new_win_button);
        hb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(thisActivity, BlankWindowForVisibilityTesting.class);
                startActivity(intent);
            }
        });
    }
}
