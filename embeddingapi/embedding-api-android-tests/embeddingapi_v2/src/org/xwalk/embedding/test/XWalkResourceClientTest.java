// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import java.util.concurrent.Callable;

import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageStartedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnReceivedErrorHelper;
import org.chromium.net.test.util.TestWebServer;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.embedding.base.ShouldOverrideUrlLoadingHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkResourceClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testShouldOverrideUrlLoading() {
        try {
            loadUrlSync("about:blank");
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkResourceClient client = new XWalkResourceClient(mXWalkView);
                    assertFalse(client.shouldOverrideUrlLoading(mXWalkView,"about:blank"));
                }
            });

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

}
