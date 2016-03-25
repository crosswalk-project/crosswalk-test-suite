package org.xwalk.embedded.api.sample.client;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkHttpAuthHandler;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithOnReceivedHttpAuthRequest extends XWalkActivity{

    private XWalkView mXWalkView;
    private TextView mTextView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_on_received_httpauth_request);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
            .append("Verifies OnReceivedHttpAuthRequest API can be invoked in XWalkResourceClient.\n\n")
            .append("Expected Result:\n\n")
            .append("Test passes if the host name and isFirstAttempt will be shown and it is 'httpbin.org' and 'true'");
        new AlertDialog.Builder(this)
            .setTitle("Info")
            .setMessage(mess.toString())
            .setPositiveButton("confirm", null)
            .show();

        mTextView = (TextView) findViewById(R.id.httpauth_request_label);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mXWalkView.load("http://httpbin.org/basic-auth/user/passwd", null);
        mXWalkView.setResourceClient(new XWalkResourceClient(mXWalkView) {

            @Override
            public void onReceivedHttpAuthRequest(XWalkView view,
                    XWalkHttpAuthHandler handler, String host, String realm) {
                // TODO Auto-generated method stub
                super.onReceivedHttpAuthRequest(view, handler, host, realm);
                String isFirst = " isFirstAttempt is ";
                if (handler != null) {
                    isFirst += handler.isFirstAttempt();
                }
                mTextView.setText(host + isFirst);
            }
        });
    }
}
