// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.basic;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

import org.xwalk.core.XWalkActivity;
import android.content.res.AssetManager;
import android.net.Uri;
import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.webkit.WebResourceResponse;
import android.widget.RelativeLayout;
import android.widget.TextView;

import java.io.IOException;
import java.io.InputStream;

public class XWalkViewWithIframes extends XWalkActivity {
    private final String TAG = "poc";

    private final static boolean IS_TEXTURE_VIEW_ENABLED = true;

    private final static String TARGET_URL = "http://localhost/parent.html";

    private final static int HOW_MANY = 3;

    private final static int WIDTH = 500;
    private final static int HEIGHT = 500;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Having debugger doesn't have an effect on the behaviour
        XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);

        XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, IS_TEXTURE_VIEW_ENABLED);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can be reliable with iframes.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if iframes will load the document which is defined in its src attribute.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        RelativeLayout root = new RelativeLayout(this);
        TextView text = new TextView(this);
        text.setText("This sample demonstrates intercepting http requests with shouldInterceptLoadRequest() is reliable in combination with iframes. Iframe will load the document which is defined in its src attribute.");
        root.addView(text);

        loadXWalkViews(root);
        setContentView(root);
    }

    private void loadXWalkViews(RelativeLayout root) {
        for (int i = 0; i < HOW_MANY; i++) {
            XWalkView xWalkView = new XWalkView(this, this);
            xWalkView.setResourceClient(initResourceClient(xWalkView));
            xWalkView.setX(getX(i));
            xWalkView.setY(200+getY(i));
            xWalkView.load(TARGET_URL, null);

            root.addView(xWalkView, WIDTH, HEIGHT);
        }
    }

    private int getY(int i) {
        return (i % 5) * 100;
    }

    private int getX(int i) {
        return i * 25;
    }

    private XWalkResourceClient initResourceClient(XWalkView xWalkView) {
        return new XWalkResourceClient(xWalkView) {
            @Override
            public WebResourceResponse shouldInterceptLoadRequest(XWalkView view, String uriString) {
                try {
                    Uri uri = Uri.parse(uriString);

                    if (isLocalhostRequest(uri)) {
                        Log.d(TAG, "Will intercept request " + uri.getPath());
                        InputStream data = getAssetFile(uri.getPath().substring(1)); // strip leading slah

                        if (data == null) {
                            Log.wtf(TAG, "No content for intercepted request: " + uriString);
                        }

                        return new WebResourceResponse("text/html", "UTF-8", data);
                    }
                } catch (Throwable thw) {
                    Log.wtf(TAG, "Exception trying to get resource for intercepted request: "
                            + uriString, thw);
                }

                Log.d(TAG, "Did not intercept request");
                return null;
            }

        };
    }
    private InputStream getAssetFile(String path) {
        InputStream data;
        AssetManager assetManager = getApplicationContext().getAssets();

        try {
            Log.d(TAG, "Open asset " + path);
            data = assetManager.open(path);
        } catch (IOException e) {
            data = null;
        }

        return data;
    }

    public boolean isLocalhostRequest(Uri uri) {
        return uri.getScheme().equals("http") && uri.getHost().equals("localhost");
    }

}