package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;

public class XWalkViewWithNetworkAvailable extends XWalkActivity {

    private XWalkView mXWalkView;

    private Button hb;


    private final static String ON_BUTTON_TEXT = "Network On";
    private final static String OFF_BUTTON_TEXT = "Network Off";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_network_available);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies setNetworkAvailable work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the Javascript alert dialog will be shown by clicking button to switch Network on/off");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (XWalkView) findViewById(R.id.onoff_xwalk_view);
        mXWalkView.load("file:///android_asset/onlineoffline.html", null);

        hb = (Button)findViewById(R.id.switch_on_off_button);
        hb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(hb.getText().equals(ON_BUTTON_TEXT)){
                    mXWalkView.setNetworkAvailable(true);
                    hb.setText(OFF_BUTTON_TEXT);
                }else{
                    mXWalkView.setNetworkAvailable(false);
                    hb.setText(ON_BUTTON_TEXT);
                }
            }
        });
    }
}
