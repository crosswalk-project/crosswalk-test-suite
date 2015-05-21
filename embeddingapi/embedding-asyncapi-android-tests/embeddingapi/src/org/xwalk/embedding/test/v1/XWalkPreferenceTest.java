// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v1;


import org.xwalk.core.XWalkPreferences;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkPreferenceTest extends XWalkViewTestBase {

    @SmallTest
    public void testSetValue_false_REMOTE_DEBUGGING() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, false);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetValue_true_REMOTE_DEBUGGING() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testGetBooleanValue_false_REMOTE_DEBUGGING() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    boolean flag = XWalkPreferences.getBooleanValue(XWalkPreferences.REMOTE_DEBUGGING);
                    assertEquals(false, flag);
                }
            });

        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetBooleanValue_true_REMOTE_DEBUGGING() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
                    boolean flag = XWalkPreferences.getBooleanValue(XWalkPreferences.REMOTE_DEBUGGING);
                    assertEquals(true, flag);
                }
            });

        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
