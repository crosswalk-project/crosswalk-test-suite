package org.xwalk.embedded.api.sample.extended;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

public class XWalkViewWithComputeScroll extends XWalkActivity {

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button mButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_compute_scroll);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mMessage = (TextView) findViewById(R.id.message_tv);
        mButton = (Button) findViewById(R.id.switch_user_agent);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can compute horizontal and vertical scroll offset and range.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes, if 'computeVerticalScrollOffset' value + 'computeVerticalScrollExtent' value = 'computeVerticalScrollRange' value when you scroll down webpage to the end then click 'Compute' button");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView.load("http://m.baidu.com/news", null);
        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mMessage.setText("computeHorizontalScrollOffset: " + mXWalkView.computeHorizontalScrollOffset() +
                        " computeHorizontalScrollRange: " + mXWalkView.computeHorizontalScrollRange() +
                        " computeVerticalScrollOffset:  " + mXWalkView.computeVerticalScrollOffset() +
                        " computeVerticalScrollRange: " + mXWalkView.computeVerticalScrollRange() +
                        " computeVerticalScrollExtent: " + mXWalkView.computeVerticalScrollExtent());
            }
        });
    }
}
