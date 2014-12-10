package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnLoadStartedHelper extends CallbackHelper {
    private String mUrl;

    public String getUrl() {
        assert getCallCount() > 0;
        return mUrl;
    }

    public void notifyCalled(String url) {
        mUrl = url;
        notifyCalled();
    }
}
