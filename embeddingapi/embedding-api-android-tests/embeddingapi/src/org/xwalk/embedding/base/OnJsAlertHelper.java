// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Copyright (c) 2013 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnJsAlertHelper extends CallbackHelper {
    private String mMessage;

    public String getMessage() {
        assert getCallCount() > 0;
        return mMessage;
    }

    public void notifyCalled(String message) {
        mMessage = message;
        notifyCalled();
    }
}
