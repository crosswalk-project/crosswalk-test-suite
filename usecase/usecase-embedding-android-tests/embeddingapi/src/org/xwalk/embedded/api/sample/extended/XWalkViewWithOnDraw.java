package org.xwalk.embedded.api.sample.extended;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

public class XWalkViewWithOnDraw extends XWalkActivity {

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onDraw work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the image of Android Robot is shown on right-top.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_on_draw);
    }
}
