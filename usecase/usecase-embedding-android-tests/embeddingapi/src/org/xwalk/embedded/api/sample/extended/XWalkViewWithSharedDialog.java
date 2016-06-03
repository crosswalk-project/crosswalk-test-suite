package org.xwalk.embedded.api.sample.extended;

import android.app.AlertDialog;
import android.os.Bundle;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkDialogManager;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

public class XWalkViewWithSharedDialog extends XWalkActivity {

    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
        XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, true);

        setContentView(R.layout.xwview_layout);

        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        XWalkDialogManager dialogManager = getDialogManager();
        AlertDialog dialog = dialogManager.getAlertDialog(XWalkDialogManager.DIALOG_NOT_FOUND);
        dialog.setTitle("TestTitle");
        dialog.setMessage("TestMessage");
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
            .append("Verifies shared mode first startup dialog can be customized.\n\n")
            .append("Expected Result:\n\n")
            .append("Test passes if the dialog with 'TestTitle' and 'TestMessage' is shown ")
            .append("and you can get crosswalk lib from the link 'GET CROSSWALK' of the dialog")
            .append(" when the sample is in shared mode");
        new  AlertDialog.Builder(this)
            .setTitle("Info")
            .setMessage(mess.toString())
            .setPositiveButton("confirm", null)
            .show();

        mXWalkView.load("file:///android_asset/navigate.html", null);
    }
}
