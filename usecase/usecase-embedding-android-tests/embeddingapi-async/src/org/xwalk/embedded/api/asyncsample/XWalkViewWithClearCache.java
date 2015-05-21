// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample;

import java.io.File;
import java.io.FileInputStream;
import java.text.DecimalFormat;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

public class XWalkViewWithClearCache extends Activity implements XWalkInitializer.XWalkInitListener {
	private static final String TAG = "XWalkViewWithClearCache";
	private static final String EXTRA_CACHE_PATH
				= "/data/data/org.xwalk.embedded.api.asyncsample/app_xwalkcore/Default/Cache";
    private XWalkView mXWalkView;
    private Button clearCacheButton;
    private TextView cacheSizeTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        XWalkInitializer.initAsync(this, this);
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
        setContentView(R.layout.clearcache_layout);
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can clear the cache.\n\n")
        .append("Expected Result:\n\n")
        .append("One way: browse some websites. Test passes if you click 'Clear Cache' button and cache size drop down to a much lower value\n\n")
        .append("Another way: browse some websites. Test passes if you exit and then go back, cache size drop down to a much lower value");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        cacheSizeTextView = (TextView) findViewById(R.id.text1);
        clearCacheButton = (Button) findViewById(R.id.clearcache_btn);
        clearCacheButton.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				if (mXWalkView != null) {
					mXWalkView.clearCache(true);
	    			cacheSizeTextView.setText("Cache Size: "+countCacheSize());
					Log.d(TAG, "ClickCacheClear: cache size: "+countCacheSize());
				}
			}
		});
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);        
        mXWalkView.setUIClient(new UIClient(mXWalkView));
        mXWalkView.load("http://www.baidu.com/", null);
    }
    
    class UIClient extends XWalkUIClient{

		public UIClient(XWalkView view) {
			super(view);
			// TODO Auto-generated constructor stub
		}

		@Override
		public void onPageLoadStopped(XWalkView view, String url,
				LoadStatus status) {
			// TODO Auto-generated method stub
			super.onPageLoadStopped(view, url, status);
			cacheSizeTextView.setText("Cache Size: "+countCacheSize());
	        Log.d(TAG, "PageLoadComplete: cache size: "+countCacheSize());
		}		
	}

	@Override
	protected void onResume() {
		// TODO Auto-generated method stub
		super.onResume();
		Log.d(TAG, "Restart(switch to frontend): cache size: "+countCacheSize());
	}

	@Override
	protected void onStop() {
		// TODO Auto-generated method stub
		super.onStop();
		if (mXWalkView != null) {
			mXWalkView.clearCache(true);
			Log.d(TAG, "Stop(switch to backend): cache size: "+countCacheSize());
		}
	}

	private static String countCacheSize(){
    	long blockSize = 0;
    	try {
        	File cacheDir = new File(EXTRA_CACHE_PATH);
        	if (cacheDir != null) {
    			if (cacheDir.isDirectory()) {
    				blockSize = getFileSizes(cacheDir);
    			} else {
    				blockSize = getFileSize(cacheDir);
    			}
    		}
		} catch (Exception e) {
			// TODO: handle exception
			Log.d(TAG, "count Cache Size error!");
		}
    	return FormetFileSize(blockSize);
    }
    
    private static long getFileSize(File f) throws Exception{
		// TODO Auto-generated method stub
    	long size = 0;
    	if (f.exists()) {
    	     FileInputStream fis = new FileInputStream(f);
    	     size = fis.available();
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
	
	private static String FormetFileSize(long fileS) {
		DecimalFormat df = new DecimalFormat("#.00");
		String fileSizeString = "";
		String wrongSize = "0B";
		if (fileS == 0) {
			return wrongSize;
		}
		if (fileS < 1024) {
			fileSizeString = df.format((double) fileS) + "B";
		}
		else if (fileS < 1048576){
			fileSizeString = df.format((double) fileS / 1024) + "KB";
		}
		else if (fileS < 1073741824){
			fileSizeString = df.format((double) fileS / 1048576) + "MB";
		}
		else{
			fileSizeString = df.format((double) fileS / 1073741824) + "GB";
		}
		return fileSizeString;
	}

}
