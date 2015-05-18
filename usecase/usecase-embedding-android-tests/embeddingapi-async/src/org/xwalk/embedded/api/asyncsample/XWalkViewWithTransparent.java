package org.xwalk.embedded.api.asyncsample;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;

public class XWalkViewWithTransparent extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;

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
        XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, false);
        
        setContentView(R.layout.xwview_transparent_layout);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Check XWalkView's transparent feature whether display the view under the webview.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if you can see button view & blue imageview");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview_transparent);
        mXWalkView.setZOrderOnTop(true);
        mXWalkView.setBackgroundColor(0);
        mXWalkView.load("http://www.baidu.com/", null);
    }

}
