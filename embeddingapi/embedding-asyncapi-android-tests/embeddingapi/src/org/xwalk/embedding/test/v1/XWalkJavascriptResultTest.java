// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;


import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkJavascriptResultTest extends XWalkViewTestBase {

    @SmallTest
    public void testConfirmWithResult() {
        try {
            assertTrue(checkMethodInClass(XWalkJavascriptResult.class, "confirmWithResult"));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
     }

    @SmallTest
    public void testConfirm() {
        try {
            assertTrue(checkMethodInClass(XWalkJavascriptResult.class, "confirm"));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testCancel() {
        try {
            assertTrue(checkMethodInClass(XWalkJavascriptResult.class, "cancel"));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
