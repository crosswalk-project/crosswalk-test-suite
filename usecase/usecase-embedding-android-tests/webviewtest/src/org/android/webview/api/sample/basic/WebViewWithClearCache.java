// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.basic;

import java.io.File;
import java.text.DecimalFormat;

import org.android.webview.api.sample.R;

import android.app.Activity;
import android.app.AlertDialog;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.TextView;


public class WebViewWithClearCache extends Activity {
    private static final String TAG = "ClearCache";
    private WebView mWebView;
    private TextView invokedInfo;
    private Button clearCacheBtn;
    private File mCacheDir;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_clear_cache);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can clear the cache.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Load the webpage and cache size will show when loading finished.\n")
        .append("2. Click the 'Clear Cache' button.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the cache size drops down a lot.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mCacheDir = this.getCacheDir();

        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        clearCacheBtn = (Button) findViewById(R.id.clear_cache_btn);
        clearCacheBtn.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                if (mWebView != null) {
                    mWebView.clearCache(true);
                    invokedInfo.setText("Cache Size: " + countCacheSize(mCacheDir));
                }
            }
        });

        mWebView = (WebView) findViewById(R.id.webview);
        mWebView.getSettings().setAppCacheEnabled(true);
        mWebView.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                // TODO Auto-generated method stub
                super.onPageFinished(view, url);
                invokedInfo.setText("Cache Size: " + countCacheSize(mCacheDir));
            }
        });
        mWebView.loadUrl("http://www.baidu.com/");
    }

    private static String countCacheSize(File path){
        long blockSize = 0;
        try {
            if (path != null) {
                if (path.isDirectory()) {
                    blockSize = getFileSizes(path);
                } else {
                    blockSize = getFileSize(path);
                }
            }
        } catch (Exception e) {
            // TODO: handle exception
            Log.d(TAG, "count Cache Size error!");
        }
        return readableFileSize(blockSize);
    }

    private static long getFileSize(File f) throws Exception{
        // TODO Auto-generated method stub
        long size = 0;
        if (f.exists() && f.isFile()) {
             size = f.length();
        }
        return size;
    }

    private static long getFileSizes(File f) throws Exception{
        long size = 0;
        File flist[] = f.listFiles();
        for (int i = 0; i < flist.length; i++){
            if (flist[i].isDirectory()){
                size = size + getFileSizes(flist[i]);
            }
            else{
                size = size + getFileSize(flist[i]);
            }
        }
        return size;
    }

    private static String readableFileSize(long size) {
        if(size <= 0) return "0";
        final String[] units = new String[] { "B", "KB", "MB", "GB", "TB" };
        int digitGroups = (int) (Math.log10(size)/Math.log10(1024));
        return new DecimalFormat("#,##0.#").format(size/Math.pow(1024, digitGroups)) + " " + units[digitGroups];
    }
}
