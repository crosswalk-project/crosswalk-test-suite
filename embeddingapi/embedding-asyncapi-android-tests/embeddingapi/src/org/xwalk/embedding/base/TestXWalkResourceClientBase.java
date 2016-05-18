package org.xwalk.embedding.base;

import org.xwalk.core.ClientCertRequest;
import org.xwalk.core.XWalkHttpAuthHandler;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkWebResourceRequest;
import org.xwalk.core.XWalkWebResourceResponse;

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
    public XWalkWebResourceResponse shouldInterceptLoadRequest(XWalkView view,
            XWalkWebResourceRequest request) {
        return mInnerContentsClient.shouldInterceptLoadRequest2(request.getUrl().toString());
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

    @Override
    public void onDocumentLoadedInFrame(XWalkView view, long frameId) {
        mInnerContentsClient.onDocumentLoadedInFrame(frameId);
    }

    @Override
    public void onReceivedClientCertRequest(XWalkView view,
            ClientCertRequest handler) {
        mInnerContentsClient.onReceivedClientCertRequest(view, handler);
    }

    @Override
    public void onReceivedHttpAuthRequest(XWalkView view,
            XWalkHttpAuthHandler handler, String host, String realm) {
        mInnerContentsClient.onReceivedHttpAuthRequest(host);
    }

    @Override
    public void onReceivedResponseHeaders(XWalkView view,
            XWalkWebResourceRequest request,
            XWalkWebResourceResponse response) {
        mInnerContentsClient.onReceivedResponseHeaders(view, request, response);
    }
}
