package org.xwalk.embedded.api.sample.setting;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class XWalkViewSettingDomStorageEnabled extends XWalkActivity {

    public final static String ENABLE_BT = "Enable DOM Storage";
    public final static String DISABLE_BT = "Disable DOM Storage";
    public final static String MESSAGE_TITLE = "DOM Storage Enabled: ";

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_setting_dom_storage_enable);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can enable/disable DOM storage API.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if Dom storage can be enabled/disabled");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_al);
        boolean defaultStorage = mXWalkView.getSettings().getDomStorageEnabled();
        if (defaultStorage) {
            mButton.setText(DISABLE_BT);
        }else{
            mButton.setText(ENABLE_BT);
        }
        mMessage.setText(MESSAGE_TITLE + defaultStorage + "(Default)");
        mXWalkView.load("file:///android_asset/dom_storage_enable.html", null);

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ENABLE_BT.equals(mButton.getText())) {
                    mXWalkView.getSettings().setDomStorageEnabled(true);
                    mButton.setText(DISABLE_BT);
                } else {
                    mXWalkView.getSettings().setDomStorageEnabled(false);
                    mButton.setText(ENABLE_BT);
                }
                mMessage.setText(MESSAGE_TITLE + mXWalkView.getSettings().getDomStorageEnabled());
                mXWalkView.load("file:///android_asset/dom_storage_enable.html", null);

            }
        });
    }
}
