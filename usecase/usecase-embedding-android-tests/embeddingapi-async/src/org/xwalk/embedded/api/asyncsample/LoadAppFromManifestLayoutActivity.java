// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample;

import java.io.IOException;
import java.io.InputStream;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.content.res.AssetManager;
import android.os.Bundle;

public class LoadAppFromManifestLayoutActivity extends Activity implements XWalkInitializer.XWalkInitListener {

    private String getAssetsFileContent(AssetManager assetManager, String fileName)
            throws IOException {
        String result = "";
        InputStream inputStream = null;
        try {
            inputStream = assetManager.open(fileName);
            int size = inputStream.available();
            byte[] buffer = new byte[size];
            inputStream.read(buffer);
            result = new String(buffer);
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
        }
        return result;
    }

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
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can load app from manifest.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if app show 'Hello World'.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();
        setContentView(R.layout.xwview_layout);
        XWalkView xwalkView = (XWalkView) findViewById(R.id.xwalkview);
        String manifestContent = "";
        try {
            manifestContent = getAssetsFileContent(this.getAssets(), "manifest.json");
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        // The manifest, please refer to the link:
        // https://crosswalk-project.org/#wiki/Crosswalk-manifest 
        xwalkView.loadAppFromManifest("file:///android_asset/", manifestContent);
    }
}
