package org.xwalk.embedded.api.asyncsample.basic;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;

public class XWalkViewWithTransparentAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, true);
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

        setContentView(R.layout.xwview_layout);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Check XWalkView's transparent feature.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if you can see transparent webpage BAIDU");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        mXWalkView.setBackgroundColor(Color.TRANSPARENT);
        mXWalkView.load("http://www.baidu.com/", null);
    }

}
