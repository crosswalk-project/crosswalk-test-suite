package org.xwalk.embedded.api.sample.basic;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

public class XWalkViewGetCertificate extends XWalkActivity {
    private XWalkView xwalkview;
    private TextView textView;
    private Button button;

    @Override
    protected void onXWalkReady() {
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
    }
}
