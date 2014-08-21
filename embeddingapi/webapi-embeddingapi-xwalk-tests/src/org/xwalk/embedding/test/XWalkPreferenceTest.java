// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test;


import org.xwalk.core.XWalkPreferences;
import org.xwalk.embedding.MainActivity;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkPreferenceTest extends XWalkViewTestBase {

    public XWalkPreferenceTest() {
        super(MainActivity.class);
    }

     
    @SmallTest
    public void testSetValue_falseParam() {
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
    public void testSetValue_trueParam() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetValue_falseParam() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    boolean flag = XWalkPreferences.getValue(XWalkPreferences.REMOTE_DEBUGGING);
                    assertEquals(false, flag);
                }
            });

        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testGetValue_trueParam() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run()  {
                    XWalkPreferences.setValue(XWalkPreferences.REMOTE_DEBUGGING, true);
                    boolean flag = XWalkPreferences.getValue(XWalkPreferences.REMOTE_DEBUGGING);
                    assertEquals(true, flag);
                }
            });

        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

}
