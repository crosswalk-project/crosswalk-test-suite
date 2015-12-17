package org.xwalk.embedded.api.asyncsample.basic;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.os.Message;
import android.widget.ImageView;
import android.widget.Button;
import android.view.View;
import android.view.View.OnClickListener;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkUIClient;

public class XWalkViewWithGetFaviconAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;
    private ImageView mFavicon;
    private Button mGetFavicon;

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
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
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
        setContentView(R.layout.activity_xwalk_view_with_get_favicon_async);

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

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
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
