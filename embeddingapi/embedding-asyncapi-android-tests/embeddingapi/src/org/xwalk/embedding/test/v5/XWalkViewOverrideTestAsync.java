// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;

import java.util.concurrent.Callable;

import android.graphics.Color;
import org.xwalk.embedding.base.OnDrawXWalkView;
import org.xwalk.embedding.base.OnCreateInputConnectionXWalkView;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkViewOverrideTestAsync extends XWalkViewTestBase {

    @SmallTest
    public void testOnDraw() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    OnDrawXWalkView mOnDrawXWalkView = new OnDrawXWalkView(mainActivity, mainActivity);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    @SmallTest
    public void testOnCreateInputConnectionXWalkView() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    OnCreateInputConnectionXWalkView mOnCreateInputConnectionXWalkView = new OnCreateInputConnectionXWalkView(mainActivity, mainActivity);                
                    mOnCreateInputConnectionXWalkView.load("http://www.baidu.com", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }    
}
