package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;

public class XWalkViewWithSetLayerTypeAsync extends Activity implements XWalkInitializer.XWalkInitListener, MessageInfoXWalkView.MessageListener{

    private XWalkInitializer mXWalkInitializer;

    private MessageInfoXWalkView mXWalkView;

    private TextView tv;

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
        setContentView(R.layout.activity_xwalk_view_with_set_layer_type_async);
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
}
