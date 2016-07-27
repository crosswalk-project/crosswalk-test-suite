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

public class XWalkViewSettingJavaScriptCanOpenWindowsAutomatically extends XWalkActivity {

    public final static String ENABLE_BT = "Enable JavaScriptCanOpenWindowsAutomatically";
    public final static String DISABLE_BT = "Disable JavaScriptCanOpenWindowsAutomatically";
    public final static String MESSAGE_TITLE = "JavaScriptCanOpenWindowsAutomatically Enabled: ";

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;
    private XWalkSettings settings;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_setting_javascript_open_windows_automatically);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
            .append("Check that XWalkView can enable/disable JavaScript open windows automatically.\n\n")
            .append("Expected Result:\n\n")
            .append("Test passes if XWalkView can enable/disable JavaScript open windows automatically during window.open().");
        new  AlertDialog.Builder(this)
                        .setTitle("Info")
                        .setMessage(mess.toString())
                        .setPositiveButton("confirm", null)
                        .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_al);
        settings = mXWalkView.getSettings();
        boolean defaultValue = settings.getJavaScriptCanOpenWindowsAutomatically();
        if (defaultValue) {
            mButton.setText(DISABLE_BT);
        }else{
            mButton.setText(ENABLE_BT);
        }
        mMessage.setText(MESSAGE_TITLE + defaultValue + "(Default)");
        mXWalkView.load("file:///android_asset/window_open_automatically.html", null);

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ENABLE_BT.equals(mButton.getText())) {
                    settings.setJavaScriptCanOpenWindowsAutomatically(true);
                    mButton.setText(DISABLE_BT);
                } else {
                    settings.setJavaScriptCanOpenWindowsAutomatically(false);
                    mButton.setText(ENABLE_BT);
                }
                mMessage.setText(MESSAGE_TITLE + settings.getJavaScriptCanOpenWindowsAutomatically());
                mXWalkView.load("file:///android_asset/window_open_automatically.html", null);

            }
        });
    }
}
