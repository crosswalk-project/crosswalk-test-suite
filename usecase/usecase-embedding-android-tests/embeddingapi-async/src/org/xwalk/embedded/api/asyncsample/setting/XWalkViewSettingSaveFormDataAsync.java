package org.xwalk.embedded.api.asyncsample.setting;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkSettings;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class XWalkViewSettingSaveFormDataAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkInitializer mXWalkInitializer;

    public final static String ENABLE_BT = "Set SaveFormData(ture)";
    public final static String DISABLE_BT = "Set SaveFormData(false)";
    public final static String MESSAGE_TITLE = "Get SaveFormData: ";

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;
    private XWalkSettings settings;

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
        setContentView(R.layout.activity_xwalk_view_setting_save_form_data_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can set/get SaveFormData in XWalkSettings.\n\n")
                .append("Test Steps:\n\n")
                .append("1. Set SaveFormData to true if it's false.\n\n")
                .append("2. Input your name.\n\n")
                .append("3. Click submit button.\n\n")
                .append("4. Input first letter of your name or double click input area.\n\n")
                .append("5. Set SaveFormData to false.\n\n")
                .append("6. Input first letter of your name again or double click input area.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the saved form date does not auto complete(or popup) after set SaveFormData to false.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_al);
        settings = mXWalkView.getSettings();
        boolean defaultvalue = settings.getSaveFormData();
        if (defaultvalue) {
            mButton.setText(DISABLE_BT);
        }else{
            mButton.setText(ENABLE_BT);
        }
        mMessage.setText(MESSAGE_TITLE + defaultvalue + "(Default)");
        mXWalkView.load("file:///android_asset/save_form_data.html", null);

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ENABLE_BT.equals(mButton.getText())) {
                    settings.setSaveFormData(true);
                    mButton.setText(DISABLE_BT);
                } else {
                    settings.setSaveFormData(false);
                    mButton.setText(ENABLE_BT);
                }
                mMessage.setText(MESSAGE_TITLE + settings.getSaveFormData());
                mXWalkView.load("file:///android_asset/save_form_data.html", null);
            }
        });
    }
}
