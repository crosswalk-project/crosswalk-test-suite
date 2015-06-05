// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;


import org.xwalk.embedding.base.OnDocumentLoadedInFrameHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import org.xwalk.embedding.util.CommonResources;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkResourceClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testOnDocumentLoadedInFrame() throws Throwable {
        OnDocumentLoadedInFrameHelper mOnDocumentLoadedInFrameHelper = mTestHelperBridge.getOnDocumentLoadedInFrameHelper();
        String path = "/test.html";
        String pageContent = CommonResources.makeHtmlPageFrom("<title>Test</title>",
                "<div> The title is: Test </div>");
        final String url = addPageToTestServer(mWebServer, path, pageContent);

        loadUrlSync(url);
        assertEquals(1, mOnDocumentLoadedInFrameHelper.getFrameId());
        assertEquals(1, mOnDocumentLoadedInFrameHelper.getCallCount());
    }
}

