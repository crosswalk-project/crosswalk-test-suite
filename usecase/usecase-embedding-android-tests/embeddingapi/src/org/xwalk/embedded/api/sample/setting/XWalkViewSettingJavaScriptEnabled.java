package org.xwalk.embedded.api.sample.setting;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkSettings;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class XWalkViewSettingJavaScriptEnabled extends XWalkActivity {

    public final static String ENABLE_BT = "Enable JavaScript";
    public final static String DISABLE_BT = "Disable JavaScript";
    public final static String MESSAGE_TITLE = "JavaScript Enabled: ";

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;
    private XWalkSettings settings;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_setting_javascript_enabled);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check that XWalkView can enable/disable JavaScript execution.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if JavaScript can be enabled/disabled");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_al);
        settings = mXWalkView.getSettings();
        boolean defaultValue = settings.getJavaScriptEnabled();
        if (defaultValue) {
            mButton.setText(DISABLE_BT);
        }else{
            mButton.setText(ENABLE_BT);
        }
        mMessage.setText(MESSAGE_TITLE + defaultValue + "(Default)");
        mXWalkView.load("file:///android_asset/javascript_enabled.html", null);

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ENABLE_BT.equals(mButton.getText())) {
                    settings.setJavaScriptEnabled(true);
                    mButton.setText(DISABLE_BT);
                } else {
                    settings.setJavaScriptEnabled(false);
                    mButton.setText(ENABLE_BT);
                }
                mMessage.setText(MESSAGE_TITLE + settings.getJavaScriptEnabled());
                mXWalkView.load("file:///android_asset/javascript_enabled.html", null);

            }
        });
    }
}
