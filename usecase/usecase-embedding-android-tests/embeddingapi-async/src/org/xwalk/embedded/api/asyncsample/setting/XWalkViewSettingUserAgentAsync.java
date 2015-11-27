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

public class XWalkViewSettingUserAgentAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    public final static String CHROME_AGENT_TEXT = "Set Chrome UserAgent";

    public final static String CHROME_USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36";

    public final static String DEFAULT_AGENT_TEXT = "Set Default UserAgent";

    public final static String MESSAGE_TITLE = "UserAgent: ";

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;

    private String default_useragent = "";
    private XWalkInitializer mXWalkInitializer;

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
        setContentView(R.layout.activity_xwalk_view_setting_user_agent_async);

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_user_agent);
        mButton.setText(CHROME_AGENT_TEXT);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can show different web content by switching the " +
                        "userAgent default UserAgent and the Mozila5.0 (Chrome 41). \n\n")
                .append("Expected Result:\n\n")
                .append("Test passes, if the 'Baidu' page is different when switching.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView.load("http://www.baidu.com", null);

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (CHROME_AGENT_TEXT.equals(mButton.getText())) {
                    mButton.setText(DEFAULT_AGENT_TEXT);
                    mXWalkView.getSettings().setUserAgentString(CHROME_USER_AGENT);
                    mMessage.setText(MESSAGE_TITLE + CHROME_USER_AGENT);
                    mXWalkView.load("http://www.baidu.com", null);
                } else {
                    mButton.setText(CHROME_AGENT_TEXT);
                    mXWalkView.getSettings().setUserAgentString(default_useragent);
                    mMessage.setText(MESSAGE_TITLE + default_useragent);
                    mXWalkView.load("http://www.baidu.com", null);
                }
            }
        });

        default_useragent  = mXWalkView.getSettings().getUserAgentString();
        mMessage.setText(MESSAGE_TITLE + default_useragent);
    }
}
