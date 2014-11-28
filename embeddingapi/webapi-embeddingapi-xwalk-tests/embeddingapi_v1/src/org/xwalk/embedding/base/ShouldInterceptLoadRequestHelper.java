package org.xwalk.embedding.base;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

import org.chromium.content.browser.test.util.CallbackHelper;

import android.webkit.WebResourceResponse;

//Two new helper classes for testing new APIs.
public class ShouldInterceptLoadRequestHelper extends CallbackHelper {
    private List<String> mShouldInterceptRequestUrls = new ArrayList<String>();
    private ConcurrentHashMap<String, WebResourceResponse> mReturnValuesByUrls
        = new ConcurrentHashMap<String, WebResourceResponse>();
    // This is read from the IO thread, so needs to be marked volatile.
    private volatile WebResourceResponse mResourceResponseReturnValue = null;
    private String mUrlToWaitFor;

    public void setReturnValue(WebResourceResponse value) {
        mResourceResponseReturnValue = value;
    }

    public void setReturnValueForUrl(String url, WebResourceResponse value) {
        mReturnValuesByUrls.put(url, value);
    }

    public void setUrlToWaitFor(String url) {
        mUrlToWaitFor = url;
    }

    public List<String> getUrls() {
        assert getCallCount() > 0;
        return mShouldInterceptRequestUrls;
    }

    public WebResourceResponse getReturnValue(String url) {
        WebResourceResponse value = mReturnValuesByUrls.get(url);
        if (value != null) return value;
        return mResourceResponseReturnValue;
    }

    public void notifyCalled(String url) {
        if (mUrlToWaitFor == null || mUrlToWaitFor.equals(url)) {
            mShouldInterceptRequestUrls.add(url);
            notifyCalled();
        }
    }
}
