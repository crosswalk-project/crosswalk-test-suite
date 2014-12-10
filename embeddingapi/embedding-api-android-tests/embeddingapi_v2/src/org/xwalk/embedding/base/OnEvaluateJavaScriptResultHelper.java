// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import java.util.concurrent.TimeoutException;
import org.chromium.content.browser.test.util.CallbackHelper;
import org.chromium.content.browser.test.util.Criteria;
import org.xwalk.core.XWalkView;

import android.webkit.ValueCallback;

public class OnEvaluateJavaScriptResultHelper extends CallbackHelper {
    private String mJsonResult;
    public void evaluateJavascript(XWalkView xWalkView, String code) {
        ValueCallback<String> callback = new ValueCallback<String>() {
                @Override
                public void onReceiveValue(String jsonResult) {
                    notifyCalled(jsonResult);
                }
            };
        xWalkView.evaluateJavascript(code, callback);
        mJsonResult = null;
    }

    public boolean hasValue() {
        return mJsonResult != null;
    }

    public boolean waitUntilHasValue() throws InterruptedException, TimeoutException {
        waitUntilCriteria(getHasValueCriteria());
        return hasValue();
    }

    public String getJsonResultAndClear() {
        assert hasValue();
        String result = mJsonResult;
        mJsonResult = null;
        return result;
    }

    public Criteria getHasValueCriteria() {
        return new Criteria() {
            @Override
            public boolean isSatisfied() {
                return hasValue();
            }
        };
    }

    public void notifyCalled(String jsonResult) {
        assert !hasValue();
        mJsonResult = jsonResult;
        notifyCalled();
    }
}