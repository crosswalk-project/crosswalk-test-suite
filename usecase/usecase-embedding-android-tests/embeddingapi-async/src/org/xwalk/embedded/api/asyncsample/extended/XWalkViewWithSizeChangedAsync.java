package org.xwalk.embedded.api.asyncsample.extended;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

public class XWalkViewWithSizeChangedAsync extends Activity implements XWalkInitializer.XWalkInitListener, SizeChangedXWalkView.SizeChangedListener{

    private XWalkInitializer mXWalkInitializer;

    private SizeChangedXWalkView mXWalkView;

    private TextView tv;

    private Button hb;

    private final static String HB_BUTTON_TEXT = "Small View";
    private final static String FB_BUTTON_TEXT = "Big View";

    private final static int SMALL_VIEW_HEIGHT = 200;
    private final static int BIG_VIEW_HEIGHT = 600;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public void informSizeChanged(String msg) {
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
        setContentView(R.layout.activity_xwalk_view_with_size_changed_async);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onSizeChanged work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the message \n\n" +
                        "'onSizeChanged is invoked. Parameter: ' \n\n" +
                        "is shown with parameter list once user clicking the button to change the size of XWalkView.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (SizeChangedXWalkView) findViewById(R.id.size_changed_xwalk_view);
        mXWalkView.setSizeChangedListener(this);
        mXWalkView.load("http://www.baidu.com", null);
        tv = (TextView)findViewById(R.id.size_changed_tip_label);

        hb = (Button)findViewById(R.id.half_button);
        hb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (hb.getText().equals(HB_BUTTON_TEXT)) {
                    mXWalkView.getLayoutParams().height = SMALL_VIEW_HEIGHT;
                    hb.setText(FB_BUTTON_TEXT);
                    mXWalkView.requestLayout();
                } else {
                    mXWalkView.getLayoutParams().height = BIG_VIEW_HEIGHT;
                    hb.setText(HB_BUTTON_TEXT);
                    mXWalkView.requestLayout();
                }

            }
        });
    }
}
