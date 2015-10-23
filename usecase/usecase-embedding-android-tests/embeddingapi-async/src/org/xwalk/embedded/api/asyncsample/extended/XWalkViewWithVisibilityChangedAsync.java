package org.xwalk.embedded.api.asyncsample.extended;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;

public class XWalkViewWithVisibilityChangedAsync extends Activity implements XWalkInitializer.XWalkInitListener, VisibilityChangedXWalkView.VisibilityChangedListener{

    private XWalkInitializer mXWalkInitializer;

    private VisibilityChangedXWalkView mXWalkView;

    private TextView tv;

    private Button hb;

    private final static String HB_BUTTON_TEXT = "Show View";
    private final static String FB_BUTTON_TEXT = "Hide View";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void informVisibilityChanged(String msg) {
        if(null != tv){
            tv.setText(msg);
        }
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
        setContentView(R.layout.activity_xwalk_view_with_visibility_changed_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onVisibilityChanged work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'onVisibilityChanged is invoked. Parameter: ' \n\n" +
                        "is shown with parameter list once user clicking the button to show/hide the XWalkView.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (VisibilityChangedXWalkView) findViewById(R.id.visibility_changed_xwalk_view);
        mXWalkView.setSizeChangedListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.visibility_changed_tip_label);

        hb = (Button)findViewById(R.id.visibility_button);
        hb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(hb.getText().equals(HB_BUTTON_TEXT)){
                    hb.setText(FB_BUTTON_TEXT);
                    mXWalkView.setVisibility(View.VISIBLE);
                    mXWalkView.requestLayout();
                }else{
                    hb.setText(HB_BUTTON_TEXT);
                    mXWalkView.setVisibility(View.INVISIBLE);
                    mXWalkView.requestLayout();
                }
            }
        });
    }
}
