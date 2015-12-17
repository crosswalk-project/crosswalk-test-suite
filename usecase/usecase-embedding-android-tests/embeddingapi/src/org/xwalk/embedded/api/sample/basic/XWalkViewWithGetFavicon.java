package org.xwalk.embedded.api.sample.basic;

import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.os.Message;
import android.widget.ImageView;
import android.widget.Button;
import android.view.View;
import android.view.View.OnClickListener;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkUIClient;

public class XWalkViewWithGetFavicon extends XWalkActivity {
    private XWalkView mXWalkView;
    private ImageView mFavicon;
    private Button mGetFavicon;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_get_favicon);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
    }

    class TestXWalkUIClientBase extends XWalkUIClient {

        public TestXWalkUIClientBase(XWalkView arg0) {
            super(arg0);
        }

        @Override
        public void onIconAvailable(XWalkView view, String url, Message msg) {
            msg.sendToTarget();
        }
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can get favicon from the html.\n\n")
        .append("Expected Result:\n\n")
        .append("1. Click the button 'Get Favicon'.\n")
        .append("2. Test passes if image of cat shows.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView.setUIClient(new TestXWalkUIClientBase(mXWalkView));

        mFavicon = (ImageView) findViewById(R.id.imageview);
        mGetFavicon = (Button) findViewById(R.id.get_favicon_btn);
        mGetFavicon.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                if (mXWalkView.getFavicon() != null) {
                    mFavicon.setImageBitmap(mXWalkView.getFavicon());
                }
            }
        });
        mXWalkView.load("file:///android_asset/favicon.html", null);
    }
}
