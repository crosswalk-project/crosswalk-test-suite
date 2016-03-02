package org.xwalk.embedded.api.sample.misc;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.graphics.Color;
import android.net.http.SslError;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.webkit.ValueCallback;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithClearSslPreferences extends XWalkActivity {

    private XWalkView mXWalkView;

    private TextView tv;

    private Boolean mAllowSslError = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_clear_ssl_preferences);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies XWalkView API clearSslPreferences() works.\n\n")
                .append("Test  Step:\n\n")
                .append("1. Click 'Refresh' button to load 12306 website with ssl certificates.\n")
                .append("2. Message 'XWalkResourceClient.onReceivedSslError is invoked' will show.\n")
                .append("3. As we expect no ssl error, click 'Refresh' button again. onReceivedSslError() will not be triggered.\n")
                .append("4. This time we click 'clearSslPreferences' button to clear the SSL preferences table stored in response.\n")
                .append("5. Then we click 'Refresh' button again and we will get message 'XWalkResourceClient.onReceivedSslError is invoked' again.\n")
                .append("Expected Result:\n\n")
                .append("Test passes if this API can clear the SSL preferences table stored in response to proceeding with SSL certificate error.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        tv = (TextView)findViewById(R.id.client_sslerror_tip);
        tv.setTextColor(Color.GREEN);

        mXWalkView = (XWalkView) findViewById(R.id.client_sslerror_xwalk_view);
        mXWalkView.setResourceClient(new XWalkResourceClient(mXWalkView) {
            @Override
            public void onReceivedSslError(XWalkView view, ValueCallback<Boolean> callback, SslError error) {
                callback.onReceiveValue(mAllowSslError);
                tv.setText("XWalkResourceClient.onReceivedSslError is invoked. Event: " + error.toString());
            }
        });

        Button bt = (Button)findViewById(R.id.refresh_button);
        bt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mXWalkView.load("https://kyfw.12306.cn/otn/regist/init", null);
                tv.setText("onReceivedSslError() method is not triggered, ssl error is denied");
            }
        });

        Button clear = (Button)findViewById(R.id.clear_button);
        clear.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mXWalkView.clearSslPreferences();
            }
        });
    }
}
