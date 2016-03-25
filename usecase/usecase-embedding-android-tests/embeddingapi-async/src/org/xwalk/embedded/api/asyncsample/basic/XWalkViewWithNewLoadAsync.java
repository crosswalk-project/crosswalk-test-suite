package org.xwalk.embedded.api.asyncsample.basic;

import java.util.HashMap;
import java.util.Map;

import android.app.AlertDialog;
import android.os.Bundle;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.asyncsample.R;

public class XWalkViewWithNewLoadAsync extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;

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
        setContentView(R.layout.activity_xwalk_view_with_new_load_async);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check XWalkView's new interface: load URL with specified HTTP headers. \n\n")
                .append("Expected Result:\n\n")
                .append("Test passes, if the language of 'Huawei' page is loaded in Chinese.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);

        Map<String,String> extraHeaders = new HashMap<String, String>();
        extraHeaders.put("Accept-Encoding", "utf-8");
        extraHeaders.put("Accept-Language", "zh-cn");
        extraHeaders.put("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36");
        extraHeaders.put("Referer", "http://www.google.com");
        mXWalkView.load("http://www.huawei.com", null, extraHeaders);
    }
}