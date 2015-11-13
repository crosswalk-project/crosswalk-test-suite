// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample.client;


import java.io.FileNotFoundException;
import java.io.IOException;

import org.android.webview.api.sample.R;

import android.annotation.TargetApi;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.ContentResolver;
import android.content.Intent;
import android.graphics.Bitmap;

import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.MediaStore;

import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageView;
import android.widget.TextView;


public class WebViewWithOnShowFileChooser extends Activity {
    private WebView mWebView;
    private TextView invokedInfo;
    private ImageView mImageView;
    public static final int INPUT_FILE_REQUEST_CODE = 1;

    private ValueCallback<Uri[]> mFilePathCallback;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_with_webview_onshow_file_chooser);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies WebView can show a file chooser and this feature needs API 21+.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click the 'Choose File' button.\n")
        .append("2. Select system gallery app and choose one photo.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if the photo shows on the blue background region.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        invokedInfo = (TextView) findViewById(R.id.invoked_info);
        mImageView = (ImageView) findViewById(R.id.image_view);
        mWebView = (WebView) findViewById(R.id.webview);

        setUpWebViewDefaults(mWebView);

        mWebView.setWebChromeClient(new InVokedWebChromeClient());
        mWebView.loadUrl("file:///android_asset/open_file.html");
    }

    class InVokedWebChromeClient extends WebChromeClient {

        @Override
        public boolean onShowFileChooser(WebView webView,
                ValueCallback<Uri[]> filePathCallback,
                FileChooserParams fileChooserParams) {
            // TODO Auto-generated method stub
            invokedInfo.setText("onShowFileChooser is invoked.");

            if(mFilePathCallback != null) {
                mFilePathCallback.onReceiveValue(null);
            }
            mFilePathCallback = filePathCallback;

            Intent contentSelectionIntent = new Intent(Intent.ACTION_GET_CONTENT);
            contentSelectionIntent.addCategory(Intent.CATEGORY_OPENABLE);
            contentSelectionIntent.setType("image/*");

            Intent chooserIntent = new Intent(Intent.ACTION_CHOOSER);
            chooserIntent.putExtra(Intent.EXTRA_INTENT, contentSelectionIntent);
            chooserIntent.putExtra(Intent.EXTRA_TITLE, "Image Chooser");

            startActivityForResult(chooserIntent, INPUT_FILE_REQUEST_CODE);

            return true;
        }
    }

    @TargetApi(Build.VERSION_CODES.HONEYCOMB)
    private void setUpWebViewDefaults(WebView webView) {
        WebSettings settings = webView.getSettings();

        // Enable Javascript
        settings.setJavaScriptEnabled(true);

        // Use WideViewport and Zoom out if there is no viewport defined
        settings.setUseWideViewPort(true);
        settings.setLoadWithOverviewMode(true);

        // We set the WebViewClient to ensure links are consumed by the WebView rather
        // than passed to a browser if it can
        mWebView.setWebViewClient(new WebViewClient());
    }

    @Override
    public void onActivityResult (int requestCode, int resultCode, Intent data) {
        if(requestCode != INPUT_FILE_REQUEST_CODE || mFilePathCallback == null) {
            super.onActivityResult(requestCode, resultCode, data);
            return;
        }

        Uri[] results = null;

        // Check that the response is a good one
        if(resultCode == Activity.RESULT_OK) {
            String dataString = data.getDataString();
            if (dataString != null) {
                results = new Uri[]{Uri.parse(dataString)};
            }
        }

        mFilePathCallback.onReceiveValue(results);
        mFilePathCallback = null;

        Bitmap bm = null;
        ContentResolver resolver = getContentResolver();
        try {
            bm = MediaStore.Images.Media.getBitmap(resolver, results[0]);
            mImageView.setImageBitmap(bm);
            bm = null;
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
