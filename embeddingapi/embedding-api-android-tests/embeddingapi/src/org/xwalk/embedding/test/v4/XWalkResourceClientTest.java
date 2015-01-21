// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v4;

import org.xwalk.embedding.base.OnReceivedSslHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.test.suitebuilder.annotation.SmallTest;

public class XWalkResourceClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testOnReceivedSslError() {
        try {
            String url = "https://kyfw.12306.cn/otn/regist/init";
            OnReceivedSslHelper mOnReceivedSslHelper = mTestHelperBridge.getOnReceivedSslHelper();
            int count = mOnReceivedSslHelper.getCallCount();
            loadUrlAsync(url);
            mOnReceivedSslHelper.waitForCallback(count);
            assertTrue(mOnReceivedSslHelper.getCalled());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
