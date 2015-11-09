package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnReceivedHttpAuthRequestHelper extends CallbackHelper {
    private String mHost;

    public String getHost() {
        assert getCallCount() > 0;
        return mHost;
    }

    public void notifyCalled(String host) {
        mHost = host;
        notifyCalled();
    }
}
