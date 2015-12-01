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

public class XWalkViewSettingTextZoomAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    public final static String ZOOM_100 = "Zoom 100";

    public final static String ZOOM_200 = "Zoom 200";

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;

    public final static String MESSAGE_TITLE = "TextSize Percent: ";

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
        setContentView(R.layout.activity_xwalk_view_setting_text_zoom_async);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_text_zoom);
        mButton.setText(ZOOM_100);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can set the text zoom of the page in percent." +
                        "The default is 100.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes, if you click 'Zoom 200', text will be zoomed bigger.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView.load("file:///android_asset/text_zoom.html", null);
        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ZOOM_100.equals(mButton.getText())) {
                    mButton.setText(ZOOM_200);
                    mXWalkView.getSettings().setTextZoom(100);
                    mMessage.setText(MESSAGE_TITLE + mXWalkView.getSettings().getTextZoom());
                    mXWalkView.load("file:///android_asset/text_zoom.html", null);
                } else {
                    mButton.setText(ZOOM_100);
                    mXWalkView.getSettings().setTextZoom(200);
                    mMessage.setText(MESSAGE_TITLE + mXWalkView.getSettings().getTextZoom());
                    mXWalkView.load("file:///android_asset/text_zoom.html", null);
                }
            }
        });

        mMessage.setText(MESSAGE_TITLE + mXWalkView.getSettings().getTextZoom());
    }
}
