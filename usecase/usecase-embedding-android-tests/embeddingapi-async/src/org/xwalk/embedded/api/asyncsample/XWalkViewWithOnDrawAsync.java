package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

public class XWalkViewWithOnDrawAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkInitializer mXWalkInitializer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void onXWalkInitStarted() {

    }

    @Override
    public void onXWalkInitCancelled() {

    }

    @Override
    public void onXWalkInitFailed() {

    }

    @Override
    public void onXWalkInitCompleted() {

        setContentView(R.layout.activity_xwalk_view_with_on_draw_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onDraw work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the image of Android Robot is shown on right-top.");
        new  AlertDialog.Builder(this)
                .setTitle("Info" )
                .setMessage(mess.toString())
                .setPositiveButton("confirm" ,  null )
                .show();
    }
}
