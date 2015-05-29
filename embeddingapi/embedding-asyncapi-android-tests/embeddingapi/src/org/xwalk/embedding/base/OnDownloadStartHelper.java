package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnDownloadStartHelper extends CallbackHelper {
    private String mUrl;
    private String mUserAgent;
    private String mContentDisposition;
    private String mMimeType;
    long mContentLength;

    public String getUrl() {
        assert getCallCount() > 0;
        return mUrl;
    }

    public String getUserAgent() {
        assert getCallCount() > 0;
        return mUserAgent;
    }

    public String getContentDisposition() {
        assert getCallCount() > 0;
        return mContentDisposition;
    }

    public String getMimeType() {
        assert getCallCount() > 0;
        return mMimeType;
    }

    public long getContentLength() {
        assert getCallCount() > 0;
        return mContentLength;
    }

    public void notifyCalled(String url, String userAgent, String contentDisposition,
            String mimeType, long contentLength) {
        mUrl = url;
        mUserAgent = userAgent;
        mContentDisposition = contentDisposition;
        mMimeType = mimeType;
        mContentLength = contentLength;
        notifyCalled();
    }
}
