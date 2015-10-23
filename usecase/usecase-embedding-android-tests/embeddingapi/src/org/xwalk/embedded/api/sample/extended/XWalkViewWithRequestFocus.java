package org.xwalk.embedded.api.sample.extended;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;

public class XWalkViewWithRequestFocus extends XWalkActivity implements MessageInfoXWalkView.MessageListener{

    private MessageInfoXWalkView mXWalkView;

    private TextView tv;

    private Button hb;

    private EditText et;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_request_focus);
    }

    @Override
    public void onMessageSent(String msg) {
        if(null != tv){
            String combineMsg = tv.getText().toString();
            if (0 == combineMsg.length()){
                combineMsg = "requestFocus works. Focus Changed:" + msg;
            }else{
                combineMsg += "->" + msg;
            }
            tv.setText(combineMsg);
        }
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies requestFocus work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Pre-condition: The focus should be in the Baidu Search BOX before testing\n\n")
                .append("Test passes if the message \n\n" +
                        "'requestFocus works. Focus Changed: ...'. and " +
                        "the focus is changed between XWalkView and TextField " +
                        "once user clicking the button to switch focus.");
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
        et = (EditText)findViewById(R.id.edit_text);

        hb = (Button)findViewById(R.id.switch_focus_button);
        hb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(et.isFocused()) {
                    mXWalkView.requestFocus();
                }else{
                    et.requestFocus();
                    onMessageSent("EditText");
                }
            }
        });
    }
}
