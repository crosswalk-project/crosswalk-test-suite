package org.xwalk.embedded.api.asyncsample;


import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;

public class ContactExtensionActivityAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private ExtensionContact mExtension;
    private XWalkView mXWalkView;
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
		// TODO Auto-generated method stub
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies extension can be supported .\n\n")
        .append("Test  Step:\n\n")
        .append("1. Input one contact name and contact phone number.\n\n")
        .append("2. Click Write Contact button\n\n")
        .append("3. Click Read Contact button\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the display of Write & Read contact contains 'passed' in green color.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.xwview_layout);
        mExtension = new ExtensionContact(ContactExtensionActivityAsync.this);
        
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mXWalkView.load("file:///android_asset/contact.html", null);
	}

}
