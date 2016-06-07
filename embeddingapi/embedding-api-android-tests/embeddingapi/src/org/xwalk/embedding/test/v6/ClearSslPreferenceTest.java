// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v6;

import org.xwalk.embedding.base.OnReceivedSslHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;


@SuppressLint("NewApi")
public class ClearSslPreferenceTest extends XWalkViewTestBase {

    @SmallTest
    // If the user allows the ssl error, the same ssl error will not trigger
    // the onReceivedSslError callback; If the user denies it, the same ssl
    // error will still trigger the onReceivedSslError callback.
    public void testSslPreferences() throws Throwable {
        final String pagePath = "/hello.html";
        final String pageUrl =
                mWebServerSsl.setResponse(pagePath, "<html><body>hello world</body></html>", null);
        final OnReceivedSslHelper onReceivedSslErrorHelper =
                mTestHelperBridge.getOnReceivedSslHelper();
        int onSslErrorCallCount = onReceivedSslErrorHelper.getCallCount();

        loadUrlSync(pageUrl);

        assertEquals(onSslErrorCallCount + 1, onReceivedSslErrorHelper.getCallCount());
        assertEquals(1, mWebServerSsl.getRequestCount(pagePath));

        // Now load the page again. This time, we expect no ssl error, because
        // user's decision should be remembered.
        onSslErrorCallCount = onReceivedSslErrorHelper.getCallCount();
        loadUrlSync(pageUrl);
        assertEquals(onSslErrorCallCount, onReceivedSslErrorHelper.getCallCount());

        // Now clear the ssl preferences then load the same url again. Expect to see
        // onReceivedSslError getting called again.
        clearSslPreferences();
        onSslErrorCallCount = onReceivedSslErrorHelper.getCallCount();
        loadUrlSync(pageUrl);
        assertEquals(onSslErrorCallCount + 1, onReceivedSslErrorHelper.getCallCount());

        // Now clear the stored decisions and tell the client to deny ssl errors.
        clearSslPreferences();
        setAllowSslError(false);
        onSslErrorCallCount = onReceivedSslErrorHelper.getCallCount();
        loadUrlSync(pageUrl);
        assertEquals(onSslErrorCallCount + 1, onReceivedSslErrorHelper.getCallCount());

        // Now load the same page again. This time, we still expect onReceivedSslError,
        // because we only remember user's decision if it is "allow".
        onSslErrorCallCount = onReceivedSslErrorHelper.getCallCount();
        loadUrlSync(pageUrl);
        assertEquals(onSslErrorCallCount + 1, onReceivedSslErrorHelper.getCallCount());
    }
}
