// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.client;

import org.xwalk.embedded.api.sample.R;

import org.xwalk.core.ClientCertRequest;
import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.webkit.ValueCallback;
import android.webkit.WebResourceResponse;
import android.widget.EditText;

public class XWalkViewWithResourceAndUIClient extends XWalkActivity {
    private XWalkView mXWalkView;
    private EditText mText;
    private static final String TAG = XWalkViewWithResourceAndUIClient.class.getName();

    class ResourceClient extends XWalkResourceClient {

        public ResourceClient(XWalkView xwalkView) {
            super(xwalkView);
        }

        public void onLoadStarted(XWalkView view, String url) {
            super.onLoadStarted(view, url);
            Log.d(TAG, "Load Started:" + url);
            mText.append("Load Started: " + url + "\n");
        }

        public void onLoadFinished(XWalkView view, String url) {
            super.onLoadFinished(view, url);
            Log.d(TAG, "Load Finished:" + url);
            mText.append("Load Finished: " + url + "\n");
        }

        public void onProgressChanged(XWalkView view, int progressInPercent) {
            super.onProgressChanged(view, progressInPercent);
            Log.d(TAG, "Loading Progress:" + progressInPercent);
            mText.append("Loading Progress: " + progressInPercent + "\n");
        }

        public WebResourceResponse shouldInterceptLoadRequest(XWalkView view, String url) {
            Log.d(TAG, "Intercept load request");
            return super.shouldInterceptLoadRequest(view, url);
        }

        public void onReceivedLoadError(XWalkView view, int errorCode, String description,
                String failingUrl) {
            Log.d(TAG, "Load Failed:" + description);
            super.onReceivedLoadError(view, errorCode, description, failingUrl);
            mText.append("Load Failed: " + description + "\n");
        }

        public void onDocumentLoadedInFrame(XWalkView view, long frameId) {
        // TODO Auto-generated method stub
            super.onDocumentLoadedInFrame(view, frameId);
            Log.d(TAG, "onDocumentLoadedInFrame frameId: " + frameId);
            mText.append("onDocumentLoadedInFrame frameId: " + frameId + "\n");
        }

        public void doUpdateVisitedHistory(XWalkView view, String url,
                boolean isReload) {
            // TODO Auto-generated method stub
            Log.d(TAG, "doUpdateVisitedHistory url: " + url + "isReload: "+isReload);
            super.doUpdateVisitedHistory(view, url, isReload);
            mText.append("doUpdateVisitedHistory url: " + url + " isReload: " + isReload + "\n");
        }
    }

    class UIClient extends XWalkUIClient {

        public UIClient(XWalkView xwalkView) {
            super(xwalkView);
        }

        public void onJavascriptCloseWindow(XWalkView view) {
            super.onJavascriptCloseWindow(view);
            Log.d(TAG, "Window closed.");
        }

        public boolean onJavascriptModalDialog(XWalkView view, JavascriptMessageType type,
                String url,
                String message, String defaultValue, XWalkJavascriptResult result) {
            Log.d(TAG, "Show JS dialog.");
            return super.onJavascriptModalDialog(view, type, url, message, defaultValue, result);
        }

        public void onFullscreenToggled(XWalkView view, boolean enterFullscreen) {
            super.onFullscreenToggled(view, enterFullscreen);
            if (enterFullscreen) {
                Log.d(TAG, "Entered fullscreen.");
            } else {
                Log.d(TAG, "Exited fullscreen.");
            }
        }

        public void openFileChooser(XWalkView view, ValueCallback<Uri> uploadFile,
                String acceptType, String capture) {
            super.openFileChooser(view, uploadFile, acceptType, capture);
            Log.d(TAG, "Opened file chooser.");
        }

        public void onScaleChanged(XWalkView view, float oldScale, float newScale) {
            super.onScaleChanged(view, oldScale, newScale);
            Log.d(TAG, "Scale changed.");
            mText.append("Scale changed from " + oldScale + " to " + newScale + "\n");
        }

        @Override
        public void onPageLoadStarted(XWalkView view, String url) {
            // TODO Auto-generated method stub
            super.onPageLoadStarted(view, url);
            Log.d(TAG, "Page Load Started. url: " + url);
            mText.append("Page Load Started. url: " + url + "\n");
        }

        @Override
        public void onPageLoadStopped(XWalkView view, String url,
                LoadStatus status) {
            // TODO Auto-generated method stub
            super.onPageLoadStopped(view, url, status);
            Log.d(TAG, "Page Load Stopped. url: " + url + " status: " + status);
            mText.append("Page Load Stopped. url: " + url + " status: " + status + "\n");
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.client_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mText = (EditText) findViewById(R.id.text1);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can set resource client and UI client.\n\n")
        .append("Expected Result:\n\n")
        .append("Test passes if resource and UI client methods triggered when xwalk load a url.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView.setResourceClient(new ResourceClient(mXWalkView));
        mXWalkView.setUIClient(new UIClient(mXWalkView));
        mXWalkView.load("http://www.baidu.com/", null);
    }
}
