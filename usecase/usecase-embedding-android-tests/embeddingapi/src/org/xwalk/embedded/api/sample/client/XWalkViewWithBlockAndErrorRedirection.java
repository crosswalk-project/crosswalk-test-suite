package org.xwalk.embedded.api.sample.client;

import org.xwalk.embedded.api.sample.R;

import java.io.InputStream;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

import android.os.Bundle;
import android.app.AlertDialog;
import android.util.Log;
import android.webkit.WebResourceResponse;


public class XWalkViewWithBlockAndErrorRedirection extends XWalkActivity{
    private XWalkView mXWalkView;
    private static final String TAG = XWalkViewWithBlockAndErrorRedirection.class.getName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.xwview_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
    }

    class ResourceClient extends XWalkResourceClient {

        public ResourceClient(XWalkView xwalkView) {
            super(xwalkView);
        }

        public void onLoadStarted(XWalkView view, String url) {
            super.onLoadStarted(view, url);
            Log.d(TAG, "Load Started:" + url);
        }

        public void onLoadFinished(XWalkView view, String url) {
            super.onLoadFinished(view, url);
            Log.d(TAG, "Load Finished:" + url);
        }

        public void onProgressChanged(XWalkView view, int progressInPercent) {
            super.onProgressChanged(view, progressInPercent);
            Log.d(TAG, "Loading Progress:" + progressInPercent);
        }

        public WebResourceResponse shouldInterceptLoadRequest(XWalkView view, String url) {
            Log.d(TAG, "Intercept load request: " + url);
            if (url.endsWith("cat")) {
			try {
				InputStream is = getApplicationContext().getResources().getAssets().open("cat.png");
				WebResourceResponse response = new WebResourceResponse("image/gif", "utf-8", is);
				return response;
			} catch (Exception e) {
				// TODO: handle exception
				Log.d(TAG, "Intercept Error: "+ e.toString());
			}
		}
            return super.shouldInterceptLoadRequest(view, url);
        }

        public void onReceivedLoadError(XWalkView view, int errorCode, String description,
                String failingUrl) {
            Log.d(TAG, "Load Failed:" + errorCode + description);
            mXWalkView.load("http://www.baidu.com/", null);
        }
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can block response.\n\n")
	    .append("Verifies XWalkView can redirect to default page when load error page.\n\n")
        .append("Expected Result:\n\n")
        .append("1. Test passes if click first link to show a cat image.\n\n")
        .append("2. Test passes if click second link to show baidu homepage.\n\n");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, true);
        XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
        XWalkPreferences.setValue(XWalkPreferences.JAVASCRIPT_CAN_OPEN_WINDOW, true);

        mXWalkView.setResourceClient(new ResourceClient(mXWalkView));
        mXWalkView.load("file:///android_asset/block_redirect_url.html", null);
    }
}
