package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnProgressChangedHelper extends CallbackHelper {
    private int mProgress;

    public int getProgress() {
        assert getCallCount() > 0;
        return mProgress;
    }

    public void notifyCalled(int progress) {
        mProgress = progress;
        notifyCalled();
    }
}
