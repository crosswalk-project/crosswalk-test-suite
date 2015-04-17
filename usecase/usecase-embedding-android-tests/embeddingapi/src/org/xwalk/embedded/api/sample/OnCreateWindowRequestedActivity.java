package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.os.Bundle;
import android.webkit.ValueCallback;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkUIClient;

public class OnCreateWindowRequestedActivity extends XWalkActivity {
    private XWalkView mXWalkView;
    private TextView mTitleText1;
    private TextView mTitleText2;
    private int count;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState);
    }

    class TestXWalkUIClientBase extends XWalkUIClient {

        public TestXWalkUIClientBase(XWalkView arg0) {
            super(arg0);
        }

        @Override
        public boolean onCreateWindowRequested(XWalkView view, InitiateBy initiator, ValueCallback<XWalkView> callback) {
            count++;
            mTitleText1.setText("onCreateWindowRequested");
            mTitleText2.setText(count + " times");
            return super.onCreateWindowRequested(view, initiator, callback);
        }
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies onCreateWindowRequested method can be triggered when icon is available.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click the 'Create Window on blank' button.\n")
        .append("2. Click the 'Create Window on blank' link.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app show 'onCreateWindowRequested' and the correct triggered times after each one of the buttons or links is clicked.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.embedding_main);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview_embedding);
        mXWalkView.setUIClient(new TestXWalkUIClientBase(mXWalkView));

        XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, true);
        XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
        XWalkPreferences.setValue(XWalkPreferences.JAVASCRIPT_CAN_OPEN_WINDOW, true);

        mTitleText1 = (TextView) findViewById(R.id.titletext1);
        mTitleText2 = (TextView) findViewById(R.id.titletext2);
        mXWalkView.load("file:///android_asset/window_create_open.html", null);
    }
}
