package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnDocumentLoadedInFrameHelper extends CallbackHelper{

    private long mFrameId;

    public long getFrameId() {
        assert getCallCount() > 0;
        return mFrameId;
    }

    public void notifyCalled(long frameId) {
        mFrameId = frameId;
        notifyCalled();
    }    
}

