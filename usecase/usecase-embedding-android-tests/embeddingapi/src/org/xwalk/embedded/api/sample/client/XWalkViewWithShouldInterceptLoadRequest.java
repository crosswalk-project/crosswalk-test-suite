package org.xwalk.embedded.api.sample.client;

import org.xwalk.embedded.api.sample.R;

import java.io.InputStream;
import java.util.Map;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkWebResourceRequest;
import org.xwalk.core.XWalkWebResourceResponse;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.app.AlertDialog;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;


public class XWalkViewWithShouldInterceptLoadRequest extends XWalkActivity{
    private static final String BUNDLE_KEY = XWalkViewWithShouldInterceptLoadRequest.class.getSimpleName();
    private XWalkView mXWalkView;
    private TextView textView;
    private Handler handler = new Handler() {

        @Override
        public void handleMessage(Message msg) {
            // TODO Auto-generated method stub
            switch(msg.what) {
            case 0:
                String req = msg.getData().getString(BUNDLE_KEY);
                textView.setText(req);
                break;
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_should_intercept_load_request);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        textView = (TextView) findViewById(R.id.request);
    }

    class ResourceClient extends XWalkResourceClient {

        public ResourceClient(XWalkView xwalkView) {
            super(xwalkView);
        }

        @Override
        public XWalkWebResourceResponse createXWalkWebResourceResponse(
                String mimeType, String encoding, InputStream data,
                int statusCode, String reasonPhrase,
                Map<String, String> responseHeaders) {
            // TODO Auto-generated method stub
            return super.createXWalkWebResourceResponse(mimeType, encoding, data,
                    statusCode, reasonPhrase, responseHeaders);
        }


        @Override
        public XWalkWebResourceResponse createXWalkWebResourceResponse(
                String mimeType, String encoding, InputStream data) {
            // TODO Auto-generated method stub
            return super.createXWalkWebResourceResponse(mimeType, encoding, data);
        }


        @Override
        public XWalkWebResourceResponse shouldInterceptLoadRequest(
                XWalkView view, XWalkWebResourceRequest request) {
            // TODO Auto-generated method stub
            String req = "Request url: " + request.getUrl().getPath() +
                         " Request isMainFrame: " + request.isForMainFrame() +
                         " Request hasUserGesture: " + request.hasGesture() +
                         " Request method: " + request.getMethod() +
                         " Request headers: " + request.getRequestHeaders().toString();
            Message msg = handler.obtainMessage();
            msg.what = 0;
            Bundle bundle = new Bundle();
            bundle.putString(BUNDLE_KEY, req);
            msg.setData(bundle);
            handler.sendMessage(msg);

            if (request.getUrl().getPath().endsWith("cat")) {
                try {
                    InputStream is = getApplicationContext().getResources().getAssets().open("cat.png");
                    return createXWalkWebResourceResponse("image/gif", "utf-8", is);
                } catch (Exception e) {
                    // TODO: handle exception
                    e.printStackTrace();
                }
            }
            return super.shouldInterceptLoadRequest(view, request);
        }
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkResourceClient api shouldInterceptLoadRequest works\n\n")
	    .append("Verifies shouldInterceptLoadRequest can get request params and return an artificial response.\n\n")
        .append("Expected Result:\n\n")
        .append("1. Test passes if a cat image shows.\n\n")
        .append("2. Test passes if request params show.\n\n");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView.setResourceClient(new ResourceClient(mXWalkView));
        Button btn = (Button) findViewById(R.id.visit);
        btn.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mXWalkView.load("http://www.baidu.com/cat", null);
            }
        });
    }
}