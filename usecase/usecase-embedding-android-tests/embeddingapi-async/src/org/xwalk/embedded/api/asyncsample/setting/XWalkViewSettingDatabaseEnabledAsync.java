package org.xwalk.embedded.api.asyncsample.setting;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class XWalkViewSettingDatabaseEnabledAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkInitializer mXWalkInitializer;

    public final static String ENABLE_BT = "Enable Database storage";
    public final static String DISABLE_BT = "Disable Database storage";
    public final static String MESSAGE_TITLE = "Database storage Enabled: ";


    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void onXWalkInitCancelled() {
        // TODO Auto-generated method stub
    }

    @Override
    public void onXWalkInitFailed() {
        // TODO Auto-generated method stub
    }

    @Override
    public void onXWalkInitStarted() {
        // TODO Auto-generated method stub
    }

    @Override
    public void onXWalkInitCompleted() {
        setContentView(R.layout.activity_xwalk_view_setting_database_enable_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can enable/disable Database storage.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if Database storage can be enabled/disabled");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_al);
        boolean defaultDatabase = mXWalkView.getSettings().getDatabaseEnabled();
        if (defaultDatabase) {
            mButton.setText(DISABLE_BT);
        }else{
            mButton.setText(ENABLE_BT);
        }
        mMessage.setText(MESSAGE_TITLE + defaultDatabase + "(Default)");
        mXWalkView.load("file:///android_asset/database_enable.html", null);

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ENABLE_BT.equals(mButton.getText())) {
                    mXWalkView.getSettings().setDatabaseEnabled(true);
                    mButton.setText(DISABLE_BT);
                } else {
                    mXWalkView.getSettings().setDatabaseEnabled(false);
                    mButton.setText(ENABLE_BT);
                }
                mMessage.setText(MESSAGE_TITLE + mXWalkView.getSettings().getDatabaseEnabled());
                mXWalkView.load("file:///android_asset/database_enable.html", null);
            }
        });
    }
}
