package org.xwalk.embedded.api.sample.extended;

import android.app.AlertDialog;
import android.os.Bundle;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkDialogManager;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

public class XWalkViewWithSharedDialog extends XWalkActivity {

    private XWalkView mXWalkView;
    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
        XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, true);

        setContentView(R.layout.version_layout);

        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        textView = (TextView) findViewById(R.id.text1);
        textView.setText("If shared mode startup dialog can be customized, " +
        		"the dialog with 'TestTitle' and 'TestMessage' is shown, " +
        		"and you can see the 'GET CROSSWALK' and 'CLOSE' button in the dialog");

        XWalkDialogManager dialogManager = getDialogManager();
        AlertDialog dialog = dialogManager.getAlertDialog(XWalkDialogManager.DIALOG_NOT_FOUND);
        dialog.setTitle("TestTitle");
        dialog.setMessage("TestMessage");
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
            .append("Verifies shared mode startup dialog can be customized.\n\n")
            .append("Expected Result:\n\n")
            .append("Test passes if the dialog with 'TestTitle' and 'TestMessage' is shown ")
            .append("and you can see the 'GET CROSSWALK' and 'CLOSE' button in the dialog");
        new  AlertDialog.Builder(this)
            .setTitle("Info")
            .setMessage(mess.toString())
            .setPositiveButton("confirm", null)
            .show();
        mXWalkView.load("file:///android_asset/sharedDialog.html", null);
    }
}
