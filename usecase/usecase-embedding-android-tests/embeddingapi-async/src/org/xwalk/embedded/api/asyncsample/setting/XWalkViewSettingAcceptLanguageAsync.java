package org.xwalk.embedded.api.asyncsample.setting;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.asyncsample.R;

public class XWalkViewSettingAcceptLanguageAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkInitializer mXWalkInitializer;

    public final static String DEFAULT_AL = "Set Default Language";

    public final static String ZHCN = "zh-cn";

    public final static String ALTER_AL = "Set Alternative Language";

    public final static String ENUS = "en-us";

    public final static String EN = "en";

    public final static String MESSAGE_TITLE = "Accept Language: ";

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;

    private String default_al = null;
    private String alternative_al = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void onXWalkInitCancelled() {

    }

    @Override
    public void onXWalkInitStarted() {

    }

    @Override
    public void onXWalkInitFailed() {

    }

    @Override
    public void onXWalkInitCompleted() {
        setContentView(R.layout.activity_xwalk_view_setting_accept_language_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can show web content with the changed language by switching the " +
                        "AcceptLanguage. \n\n")
                .append("Expected Result:\n\n")
                .append("Test passes, if the language of 'Huawei' page is changed when switching.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_al);
        mButton.setText(ALTER_AL);
        mXWalkView.load("http://www.huawei.com", null);

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (DEFAULT_AL.equals(mButton.getText())) {
                    mButton.setText(ALTER_AL);
                    mXWalkView.getSettings().setAcceptLanguages(default_al);
                    mMessage.setText(MESSAGE_TITLE + default_al);
                    mXWalkView.load("http://www.huawei.com", null);
                } else {
                    mButton.setText(DEFAULT_AL);
                    mXWalkView.getSettings().setAcceptLanguages(alternative_al);
                    mMessage.setText(MESSAGE_TITLE + alternative_al);
                    mXWalkView.load("http://www.huawei.com", null);
                }
            }
        });

        default_al  = mXWalkView.getSettings().getAcceptLanguages();
        mMessage.setText(MESSAGE_TITLE + default_al);
        if(default_al.startsWith(EN)){
            alternative_al = ZHCN;
        }else{
            alternative_al = ENUS;
        }
    }
}
