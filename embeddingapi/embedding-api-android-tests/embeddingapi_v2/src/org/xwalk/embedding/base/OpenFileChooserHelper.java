package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

import android.net.Uri;
import android.webkit.ValueCallback;

public class OpenFileChooserHelper extends CallbackHelper{
    private ValueCallback<Uri> mCallback;

    public ValueCallback<Uri> getCallback() {
        assert getCallCount() > 0;
        return mCallback;
    }

    public void notifyCalled(ValueCallback<Uri> callback) {
        mCallback = callback;
        notifyCalled();
    }
}
