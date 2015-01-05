package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnFullscreenToggledHelper extends CallbackHelper {
    private boolean mEnterFullscreen = false;

    public boolean getEnterFullscreen() {
        assert getCallCount() > 0;
        return mEnterFullscreen;
    }

    public void notifyCalled(boolean enterFullscreen) {
        mEnterFullscreen = enterFullscreen;
        notifyCalled();
    }
}
