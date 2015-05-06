package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;

public class XWalkViewFromXWalkActivity extends XWalkActivity {
	private XWalkView mXWalkView;

	@Override
	protected void onXWalkReady() {
		// TODO Auto-generated method stub       
        setContentView(R.layout.xwview_layout);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("XWalkActivity is a new API of the Embedding API. So just inherit from it like XWalkViewShellActivity, you can use XWalkView.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app load 'baidu.com' page.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mXWalkView.load("http://www.baidu.com/", null);
	}

}
