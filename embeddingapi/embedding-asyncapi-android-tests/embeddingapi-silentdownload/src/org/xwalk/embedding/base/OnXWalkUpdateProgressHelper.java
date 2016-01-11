package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;


public class OnXWalkUpdateProgressHelper extends CallbackHelper {
    private String mMessage;
    private int mProgress;

    public String getMessage() {
        assert getCallCount() > 0;
        return mMessage;
    }

    public void notifyCalled(String message, int progress) {
        mMessage = message;
        mProgress = progress;
        notifyCalled();
    }
    
    public int getProgress() {
        return mProgress;
    }
}
