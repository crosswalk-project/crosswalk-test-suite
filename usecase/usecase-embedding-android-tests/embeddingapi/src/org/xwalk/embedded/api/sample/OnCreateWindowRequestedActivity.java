package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.os.Message;
import android.util.Log;
import android.webkit.ValueCallback;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkUIClient;

public class OnCreateWindowRequestedActivity extends XWalkActivity {
    private XWalkView mXWalkView;
    private TextView mTitleText1;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies onCreateWindowRequested method can be triggered when icon is available.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click the 'Create Window Self' button.\n")
        .append("2. Click the 'Create Window Parent' button.\n")
        .append("3. Click the 'Create Window Top' button.\n")
        .append("4. Click the 'Create Window Self' link.\n")
        .append("5. Click the 'Create Window Parent' link.\n")
        .append("6. Click the 'Create Window Top' link.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app show 'onCreateWindowRequested' after each one of the buttons or links is clicked.");
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
        mXWalkView.load("file:///android_asset/window_create_open.html", null);

    }

    class TestXWalkUIClientBase extends XWalkUIClient {

        public TestXWalkUIClientBase(XWalkView arg0) {
            super(arg0);
        }

        @Override
        public boolean onCreateWindowRequested(XWalkView view, InitiateBy initiator, ValueCallback<XWalkView> callback) {
            mTitleText1.setText("onCreateWindowRequested");
            return true;
        }
    }
}
