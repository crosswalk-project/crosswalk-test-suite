package org.xwalk.embedding.base;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.xwalk.core.XWalkWebResourceResponse;

// Two new helper classes for testing new APIs.
public class ShouldInterceptLoadRequestHelper2 extends CallbackHelper {
    private List<String> mShouldInterceptRequestUrls = new ArrayList<String>();
    private ConcurrentHashMap<String, XWalkWebResourceResponse> mReturnValuesByUrls
        = new ConcurrentHashMap<String, XWalkWebResourceResponse>();
    // This is read from the IO thread, so needs to be marked volatile.
    private volatile XWalkWebResourceResponse mResourceResponseReturnValue = null;
    private String mUrlToWaitFor;

    public void setReturnValue(XWalkWebResourceResponse value) {
        mResourceResponseReturnValue = value;
    }

    public void setReturnValueForUrl(String url, XWalkWebResourceResponse value) {
        mReturnValuesByUrls.put(url, value);
    }

    public void setUrlToWaitFor(String url) {
        mUrlToWaitFor = url;
    }

    public List<String> getUrls() {
        assert getCallCount() > 0;
        return mShouldInterceptRequestUrls;
    }

    public XWalkWebResourceResponse getReturnValue(String url) {
        XWalkWebResourceResponse value = mReturnValuesByUrls.get(url);
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