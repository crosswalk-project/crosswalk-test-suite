package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;

public class XWalkViewWithSetLayerType extends XWalkActivity implements MessageInfoXWalkView.MessageListener{

    private MessageInfoXWalkView mXWalkView;

    private TextView tv;

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies setLayerType work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'DispatchDraw is completed without Hardware accelerated changed by setLayerType'");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (MessageInfoXWalkView) findViewById(R.id.layertype_xwalk_view);
        mXWalkView.setMessageListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.layertype_msg_label);
        tv.setTextColor(Color.GREEN);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_set_layer_type);
    }

    @Override
    public void onMessageSent(String msg) {
        if(null != tv){
            tv.setText(msg);
        }
    }

}