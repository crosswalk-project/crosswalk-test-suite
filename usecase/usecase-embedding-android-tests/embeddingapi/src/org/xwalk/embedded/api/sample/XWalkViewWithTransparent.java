package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;

public class XWalkViewWithTransparent extends XWalkActivity{
    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected void onXWalkReady() {
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
