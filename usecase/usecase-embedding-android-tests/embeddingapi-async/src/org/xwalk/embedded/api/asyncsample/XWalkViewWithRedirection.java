package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

public class XWalkViewWithRedirection extends Activity implements XWalkInitializer.XWalkInitListener {
	private static final String TAG = XWalkViewWithRedirection.class.getSimpleName();
	
    private XWalkView mXWalkView;
    private TextView LoadstoppedTimes;
    private int times_started = 0;
    private int times_stopped = 0;
    private int progress = 0;
	
	class UIClient extends XWalkUIClient{

		public UIClient(XWalkView view) {
			super(view);
			// TODO Auto-generated constructor stub
		}

		@Override
		public void onPageLoadStopped(XWalkView view, String url,
				LoadStatus status) {
			// TODO Auto-generated method stub
			super.onPageLoadStopped(view, url, status);
			Log.d(TAG, "onPageLoadStopped called");
			times_stopped++;
			updateLoadingState();
		}

		@Override
		public void onPageLoadStarted(XWalkView view, String url) {
			// TODO Auto-generated method stub
			super.onPageLoadStarted(view, url);
			Log.d(TAG, "onPageLoadStarted called");
			times_started++;
			updateLoadingState();
		}
		
	}
	
	class UIResourceClient extends XWalkResourceClient{

		public UIResourceClient(XWalkView view) {
			super(view);
			// TODO Auto-generated constructor stub
		}

		@Override
		public void onProgressChanged(XWalkView view, int progressInPercent) {
			// TODO Auto-generated method stub
			super.onProgressChanged(view, progressInPercent);
			Log.d(TAG, "Loading Progress:" + progressInPercent);
			progress = progressInPercent;
			updateLoadingState();
		}
		
	}

	private void updateLoadingState() {
		// TODO Auto-generated method stub
		String state = "onPageLoadStarted called: " + times_started +
				       "\nonPageLoadStopped called: " + times_stopped +
				       "\nonProgressChanged id: " + progress;
		LoadstoppedTimes.setText(state);
	}

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        XWalkInitializer.initAsync(this, this);
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
		// TODO Auto-generated method stub
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Load a page with redirection, track onPageLoadStopped, onPageLoadStarted, onProgressChanged called times.\n\n")
        .append("Test  Step:\n\n")
        .append("1. load the website http://www.cnn.com/ automatically.\n")
        .append("2. observe the onProgressChanged id until it is 100.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if onPageLoadStopped called shows 1 time");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
 
        setContentView(R.layout.version_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        LoadstoppedTimes = (TextView) findViewById(R.id.text1);

        mXWalkView.setUIClient(new UIClient(mXWalkView));
        mXWalkView.setResourceClient(new UIResourceClient(mXWalkView));
        mXWalkView.load("http://www.cnn.com/", null);
	}
}
