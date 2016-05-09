package org.xwalk.embedded.api.asyncsample.basic;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.asyncsample.R;

public class XWalkViewGetCertificateAsync extends Activity implements XWalkInitializer.XWalkInitListener{
    private XWalkInitializer mXWalkInitializer;
    private XWalkView xwalkview;
    private TextView textView;
    private Button button;

    @Override
	public void onXWalkInitCompleted() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can get the content of certificate.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click 'XWalkView.getCertificate()' button when finish loading crosswalk home page.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if page shows the certificate content.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        setContentView(R.layout.activity_xwalk_view_get_certificate);
        xwalkview = (XWalkView) findViewById(R.id.xwalkview);
        textView = (TextView) findViewById(R.id.showCertificate);
        button = (Button) findViewById(R.id.getCertificate);
        button.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				textView.setText(xwalkview.getCertificate() == null ?
						"null" : xwalkview.getCertificate().toString());
			}
		});
    	xwalkview.load("https://crosswalk-project.org",null);
        
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

	@Override
	public void onXWalkInitCancelled() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void onXWalkInitFailed() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void onXWalkInitStarted() {
		// TODO Auto-generated method stub
		
	}
}
