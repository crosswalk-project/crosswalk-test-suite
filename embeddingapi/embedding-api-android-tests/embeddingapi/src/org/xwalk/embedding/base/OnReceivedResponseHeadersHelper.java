// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.xwalk.core.XWalkWebResourceRequest;
import org.xwalk.core.XWalkWebResourceResponse;

public class OnReceivedResponseHeadersHelper extends CallbackHelper {
    private XWalkWebResourceRequest mRequest;
    private XWalkWebResourceResponse mResponse;

    public void notifyCalled(XWalkWebResourceRequest request, XWalkWebResourceResponse response) {
        mRequest = request;
        mResponse = response;
        notifyCalled();
    }
    public XWalkWebResourceRequest getRequest() {
        assert getCallCount() > 0;
        return mRequest;
    }
    public XWalkWebResourceResponse getResponse() {
        assert getCallCount() > 0;
        return mResponse;
    }
}
