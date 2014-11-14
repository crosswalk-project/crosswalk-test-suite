// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnScaleChangedHelper extends CallbackHelper {
    private float mScale;

    public float getScale() {
        assert getCallCount() > 0;
        return mScale;
    }

    public void notifyCalled(float scale) {
        mScale = scale;
        notifyCalled();
    }
}
