package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnReceivedSslHelper extends CallbackHelper {
    private boolean mCalled = false;

    public boolean getCalled() {
        assert getCallCount() > 0;
        return mCalled;
    }

    public void notifyCalled(boolean called) {
        mCalled = called;
        notifyCalled();
    }
}
