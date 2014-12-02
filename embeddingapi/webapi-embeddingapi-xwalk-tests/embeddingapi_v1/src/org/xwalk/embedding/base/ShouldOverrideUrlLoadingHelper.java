package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class ShouldOverrideUrlLoadingHelper extends CallbackHelper {
    private String mShouldOverrideUrlLoadingUrl;
    private String mPreviousShouldOverrideUrlLoadingUrl;
    private boolean mShouldOverrideUrlLoadingReturnValue = false;

    void setShouldOverrideUrlLoadingUrl(String url) {
        mShouldOverrideUrlLoadingUrl = url;
    }

    void setPreviousShouldOverrideUrlLoadingUrl(String url) {
        mPreviousShouldOverrideUrlLoadingUrl = url;
    }

    public void setShouldOverrideUrlLoadingReturnValue(boolean value) {
        mShouldOverrideUrlLoadingReturnValue = value;
    }

    public String getShouldOverrideUrlLoadingUrl() {
        assert getCallCount() > 0;
        return mShouldOverrideUrlLoadingUrl;
    }

    public String getPreviousShouldOverrideUrlLoadingUrl() {
        assert getCallCount() > 1;
        return mPreviousShouldOverrideUrlLoadingUrl;
    }

    public boolean getShouldOverrideUrlLoadingReturnValue() {
        return mShouldOverrideUrlLoadingReturnValue;
    }

    public void notifyCalled(String url) {
        mPreviousShouldOverrideUrlLoadingUrl = mShouldOverrideUrlLoadingUrl;
        mShouldOverrideUrlLoadingUrl = url;
        notifyCalled();
    }
}