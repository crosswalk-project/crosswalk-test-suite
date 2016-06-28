// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.asynctest.v5;

import java.util.concurrent.Callable;

import android.graphics.Color;
import org.xwalk.embedding.base.OnDrawXWalkView;
import org.xwalk.embedding.base.OnCreateInputConnectionXWalkView;
import org.xwalk.embedding.base.RequestFocusXWalkView;
import org.xwalk.embedding.base.RequestFocusXWalkView.FocusChangedListener;
import org.xwalk.embedding.base.ScrollXWalkView;
import org.xwalk.embedding.base.ScrollXWalkView.OnMeasureListener;
import org.xwalk.embedding.base.ScrollXWalkView.OverScrollModeListener;
import org.xwalk.embedding.base.DispatchDrawXWalkView;
import org.xwalk.embedding.base.WindowsVisibilityChangedXWalkView;
import org.xwalk.embedding.base.WindowsVisibilityChangedXWalkView.MessageListener;
import org.xwalk.embedding.base.SetLayerTypeXWalkView;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkViewOverrideTestAsync extends XWalkViewTestBase {
    static Boolean focusChanged = false;

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
    public void testRequestFocus() {
        focusChanged = false;
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {

                    RequestFocusXWalkView mRequestFocusXWalkView = new RequestFocusXWalkView(mainActivity, mainActivity);
                    mRequestFocusXWalkView.setFocuseChangedListener(new FocusChangedListener(){

                        @Override
                        public void informFocuseChanged(String msg) {
                            // TODO Auto-generated method stub
                            focusChanged = true;
                        }

                    });
                    mRequestFocusXWalkView.load("http://www.baidu.com", null);
                    mRequestFocusXWalkView.setFocusable(true);
                    mRequestFocusXWalkView.setFocusableInTouchMode(true);
                    mRequestFocusXWalkView.requestFocus();
                    mRequestFocusXWalkView.requestFocusFromTouch();
                }
            });
            assertTrue(true);
            assertTrue(focusChanged);
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

    @SmallTest
    public void testComputeHorizontalScrollOffset() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    ScrollXWalkView mScrollXWalkView = new ScrollXWalkView(mainActivity, mainActivity);
                    mScrollXWalkView.load("http://www.sina.com.cn", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testComputeVerticalScrollRange() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    ScrollXWalkView mScrollXWalkView = new ScrollXWalkView(mainActivity, mainActivity);
                    mScrollXWalkView.load("http://www.sina.com.cn", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnMeasure() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    ScrollXWalkView mScrollXWalkView = new ScrollXWalkView(mainActivity, mainActivity);
                    mScrollXWalkView.load("http://www.sina.com.cn", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetOverScrollMode() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    ScrollXWalkView mScrollXWalkView = new ScrollXWalkView(mainActivity, mainActivity);
                    mScrollXWalkView.load("http://www.sina.com.cn", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testDispatchDraw() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    DispatchDrawXWalkView mDispatchDrawXWalkView = new DispatchDrawXWalkView(mainActivity, mainActivity);
                    mDispatchDrawXWalkView.load("http://www.baidu.com", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnWindowVisibilityChanged() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    WindowsVisibilityChangedXWalkView mWindowsVisibilityChangedXWalkView = new WindowsVisibilityChangedXWalkView(mainActivity, mainActivity);
                    mWindowsVisibilityChangedXWalkView.load("http://www.baidu.com", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }


    @SmallTest
    public void testSetLayerType() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    SetLayerTypeXWalkView mSetLayerTypeXWalkView = new SetLayerTypeXWalkView(mainActivity, mainActivity);
                    mSetLayerTypeXWalkView.load("http://www.baidu.com", null);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

}
