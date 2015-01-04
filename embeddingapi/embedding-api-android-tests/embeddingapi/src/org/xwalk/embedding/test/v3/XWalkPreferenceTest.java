// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v3;


import org.xwalk.core.XWalkPreferences;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkPreferenceTest extends XWalkViewTestBase {

    @SmallTest
    public void testSetValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    String value = "testSetValue_String";
                    XWalkPreferences.setValue(XWalkPreferences.ALLOW_UNIVERSAL_ACCESS_FROM_FILE, value);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.JAVASCRIPT_CAN_OPEN_WINDOW, true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetValue_int_SUPPORT_MULTIPLE_WINDOWS() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, 3);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetStringValue_String_ALLOW_UNIVERSAL_ACCESS_FROM_FILE() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    String value = "testSetValue_String";
                    XWalkPreferences.setValue(XWalkPreferences.ALLOW_UNIVERSAL_ACCESS_FROM_FILE, value);
                    assertEquals(value, XWalkPreferences.getStringValue(XWalkPreferences.ALLOW_UNIVERSAL_ACCESS_FROM_FILE));
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetBooleanValue_boolean_JAVASCRIPT_CAN_OPEN_WINDOW() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.JAVASCRIPT_CAN_OPEN_WINDOW, false);
                    assertEquals(false, XWalkPreferences.getBooleanValue(XWalkPreferences.JAVASCRIPT_CAN_OPEN_WINDOW));
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetIntegerValue_int_SUPPORT_MULTIPLE_WINDOWS() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, 3);
                    assertEquals(3, XWalkPreferences.getIntegerValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS));
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetValue_function() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.ALLOW_UNIVERSAL_ACCESS_FROM_FILE, true);
                    assertTrue(XWalkPreferences.getBooleanValue(XWalkPreferences.ALLOW_UNIVERSAL_ACCESS_FROM_FILE));
                    XWalkPreferences.setValue(XWalkPreferences.PROFILE_NAME, "PROFILE_NAME");
                    assertEquals("PROFILE_NAME", XWalkPreferences.getStringValue(XWalkPreferences.PROFILE_NAME));
                    XWalkPreferences.setValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS, false);
                    assertFalse(XWalkPreferences.getBooleanValue(XWalkPreferences.SUPPORT_MULTIPLE_WINDOWS));
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
