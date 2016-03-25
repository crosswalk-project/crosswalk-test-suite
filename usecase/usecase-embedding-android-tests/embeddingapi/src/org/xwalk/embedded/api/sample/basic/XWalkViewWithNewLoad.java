package org.xwalk.embedded.api.sample.basic;

import java.util.HashMap;
import java.util.Map;

import android.app.AlertDialog;
import android.os.Bundle;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

public class XWalkViewWithNewLoad extends XWalkActivity {

    private XWalkView mXWalkView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_new_load);
    }

    @Override
    protected void onXWalkReady() {
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