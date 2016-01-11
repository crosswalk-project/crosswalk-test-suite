package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnXWalkInitCompletedHelper extends CallbackHelper {
    private String mMessage;

    public String getMessage() {
        assert getCallCount() > 0;
        return mMessage;
    }

    public void notifyCalled(String message) {
        mMessage = message;
        notifyCalled();
    }
}
