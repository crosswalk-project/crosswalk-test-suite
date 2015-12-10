package org.xwalk.embedded.api.sample.client;

import java.util.Map;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkWebResourceRequest;
import org.xwalk.core.XWalkWebResourceResponse;

public class XWalkViewWithOnReceivedResponseHeaders extends XWalkActivity{

    private XWalkView mXWalkView;
    private TextView mTextView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_on_received_response_headers);
    }

    @Override
    protected void onXWalkReady() {
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
