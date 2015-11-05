package org.xwalk.embedded.api.asyncsample.client;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkHttpAuthHandler;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

public class XWalkViewWithOnReceivedHttpAuthRequestAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkInitializer mXWalkInitializer;
    private XWalkView mXWalkView;
    private TextView mTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public final void onXWalkInitStarted() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitCancelled() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitFailed() {
        // Do crash or logging or anything else in order to let the tester know if this method get called
    }

    @Override
    public final void onXWalkInitCompleted() {
        setContentView(R.layout.activity_xwalk_view_with_on_received_httpauth_request_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
            .append("Verifies OnReceivedHttpAuthRequest API can be invoked in XWalkResourceClient.\n\n")
            .append("Expected Result:\n\n")
            .append("Test passes if the host name will be shown and it is 'httpbin.org'");
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
                mTextView.setText(host);
            }
        });
    }
}
