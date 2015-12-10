package org.xwalk.embedded.api.asyncsample.client;

import java.util.Map;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.app.Activity;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkWebResourceRequest;
import org.xwalk.core.XWalkWebResourceResponse;

public class XWalkViewWithOnReceivedResponseHeadersAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkView mXWalkView;
    private TextView mTextView;
    private XWalkInitializer mXWalkInitializer;

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
        setContentView(R.layout.activity_xwalk_view_with_on_received_response_headers_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
            .append("Verifies onReceivedResponseHeaders API can be invoked in XWalkResourceClient.\n\n")
            .append("Expected Result:\n\n")
            .append("Test passes if the Set-Cookie string shows");
        new AlertDialog.Builder(this)
            .setTitle("Info")
            .setMessage(mess.toString())
            .setPositiveButton("confirm", null)
            .show();

        mTextView = (TextView) findViewById(R.id.response_headers_label);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mXWalkView.setResourceClient(new XWalkResourceClient(mXWalkView) {

            @Override
            public void onReceivedResponseHeaders(XWalkView view,
                    XWalkWebResourceRequest request,
                    XWalkWebResourceResponse response) {
                // TODO Auto-generated method stub
                super.onReceivedResponseHeaders(view, request, response);
                if(response.getStatusCode() == 200) {
                    Map<String, String> headers = response.getResponseHeaders();
                    String cookies = headers.get("Set-Cookie");
                    if(cookies != null) {
                        mTextView.setText(cookies);
                    }
                }
            }
        });
        mXWalkView.load("http://m.baidu.cn", null);
    }
}
