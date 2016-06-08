package org.xwalk.embedded.api.asyncsample.extended;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkDialogManager;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkUpdater;
import org.xwalk.core.XWalkUpdater.XWalkUpdateListener;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.asyncsample.R;

public class XWalkViewWithSharedDialogAsync extends Activity implements XWalkInitializer.XWalkInitListener, XWalkUpdateListener {

    private XWalkView mXWalkView;
    private TextView textView;
    private XWalkUpdater mXWalkUpdater;
    private XWalkInitializer mXWalkInitializer;
    private XWalkDialogManager mDialogManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();

        XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
        XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, true);

        setContentView(R.layout.version_layout);

        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        textView = (TextView) findViewById(R.id.text1);
        textView.setText("If shared mode startup dialog can be customized, " +
        		"the dialog with 'TestTitle' and 'TestMessage' is shown, " +
        		"and you can see the 'GET CROSSWALK' and 'CLOSE' button in the dialog");
    }

	@Override
	public void onXWalkInitCancelled() {
		finish();
	}

	@Override
	public void onXWalkInitCompleted() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
            .append("Verifies shared mode startup dialog can be customized.\n\n")
            .append("Expected Result:\n\n")
            .append("Test passes if the dialog with 'TestTitle' and 'TestMessage' is shown ")
            .append("and you can see the 'GET CROSSWALK' 'GET CROSSWALK' and 'CLOSE' button in the dialog");
        new  AlertDialog.Builder(this)
            .setTitle("Info")
            .setMessage(mess.toString())
            .setPositiveButton("confirm", null)
            .show();

        mXWalkView.load("file:///android_asset/sharedDialog.html", null);
		
	}

    @Override
    public void onXWalkInitFailed() {
        if (mXWalkUpdater == null) {
            AlertDialog dialog = new AlertDialog.Builder(this).create();
            dialog.setIcon(android.R.drawable.ic_dialog_alert);
            dialog.setTitle("TextTitle");
            dialog.setMessage("TextMessage");
            dialog.setButton(DialogInterface.BUTTON_NEGATIVE, "CLOSE", (DialogInterface.OnClickListener) null);
            dialog.setButton(DialogInterface.BUTTON_POSITIVE, "GET CROSSWALK", (DialogInterface.OnClickListener) null);

            mDialogManager = new XWalkDialogManager(this);
            mDialogManager.setAlertDialog(XWalkDialogManager.DIALOG_NOT_FOUND, dialog);
            mXWalkUpdater = new XWalkUpdater(this, this, mDialogManager);
        }
        mXWalkUpdater.updateXWalkRuntime();
    }

	@Override
	public void onXWalkInitStarted() {
		
	}

	@Override
	public void onXWalkUpdateCancelled() {
		finish();
	}
}
