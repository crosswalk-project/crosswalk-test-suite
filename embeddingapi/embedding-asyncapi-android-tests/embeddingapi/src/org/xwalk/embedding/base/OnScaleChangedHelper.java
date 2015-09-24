// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnScaleChangedHelper extends CallbackHelper {
    private float mPreviousScale;
    private float mCurrentScale;

    public void notifyCalled(float oldScale, float newScale) {
        mPreviousScale = oldScale;
        mCurrentScale = newScale;
        super.notifyCalled();
    }

    public float getOldScale() {
        return mPreviousScale;
    }

    public float getNewScale() {
        return mCurrentScale;
    }

    public float getLastScaleRatio() {
        assert getCallCount() > 0;
        return mCurrentScale / mPreviousScale;
    }
}
