// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.asynctest.v6;

import org.xwalk.core.XWalkPreferences;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkPreferenceTestAsync extends XWalkViewTestBase {

    @SmallTest
    public void testSetThemeColor_enable() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.ENABLE_THEME_COLOR, true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetThemeColor_disbale() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.ENABLE_THEME_COLOR, false);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }


    @SmallTest
    public void testGetThemeColor() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {
                @Override
                public void run() {
                    assertTrue(XWalkPreferences.getBooleanValue(XWalkPreferences.ENABLE_THEME_COLOR));
                    XWalkPreferences.setValue(XWalkPreferences.ENABLE_THEME_COLOR, false);
                    assertFalse(XWalkPreferences.getBooleanValue(XWalkPreferences.ENABLE_THEME_COLOR));
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
