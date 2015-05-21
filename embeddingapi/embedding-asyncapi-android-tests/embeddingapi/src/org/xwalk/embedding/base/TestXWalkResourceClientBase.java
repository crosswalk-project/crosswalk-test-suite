package org.xwalk.embedding.base;

import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

import android.net.http.SslError;
import android.webkit.ValueCallback;
import android.webkit.WebResourceResponse;

public class TestXWalkResourceClientBase extends XWalkResourceClient{
    TestHelperBridge mInnerContentsClient;
    public TestXWalkResourceClientBase(TestHelperBridge client, XWalkView mXWalkView) {
        super(mXWalkView);
        mInnerContentsClient = client;
    }

    @Override
    public void onLoadStarted(XWalkView view, String url) {
        mInnerContentsClient.onLoadStarted(url);
    }

    @Override
    public void onLoadFinished(XWalkView view, String url) {
        mInnerContentsClient.onLoadFinished(url);
    }

    @Override
    public void onProgressChanged(XWalkView view, int progressInPercent) {
        mInnerContentsClient.onProgressChanged(progressInPercent);
    }

    @Override
    public void onReceivedLoadError(XWalkView view, int errorCode,
            String description, String failingUrl) {
        mInnerContentsClient.onReceivedLoadError(errorCode, description, failingUrl);
    }

    @Override
    public WebResourceResponse shouldInterceptLoadRequest(XWalkView view,
            String url) {
        return mInnerContentsClient.shouldInterceptLoadRequest(url);
    }

    @Override
    public boolean shouldOverrideUrlLoading(XWalkView view, String url) {
        return mInnerContentsClient.shouldOverrideUrlLoading(url);
    }

    @Override
    public void onReceivedSslError(XWalkView view,
            ValueCallback<Boolean> callback, SslError error) {
        mInnerContentsClient.onReceivedSsl();
    }
}
