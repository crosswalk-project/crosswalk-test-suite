// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;

import java.util.concurrent.Callable;

import android.graphics.Color;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkViewTestAsync extends XWalkViewTestBase {

    @SmallTest
    public void testSetUserAgentString() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    mXWalkView.setUserAgentString(USER_AGENT);
                }
            });
            loadDataSync(null, EMPTY_PAGE, "text/html", false);
            String result = executeJavaScriptAndWaitForResult("navigator.userAgent;");
            assertEquals(EXPECTED_USER_AGENT, result);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetZOrderOnTop_True() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.setZOrderOnTop(true);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetZOrderOnTop_False() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                    mXWalkView.setZOrderOnTop(false);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    @SmallTest
    public void testSetBackgroundColor_Color() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setBackgroundColor(Color.RED);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testSetBackgroundColor_Value() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setBackgroundColor(Color.parseColor("#00FF00"));
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    @SmallTest
    public void testSetBackgroundColor_Transparent() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setBackgroundColor(0);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
    
    @SmallTest
    public void testSetXWalkViewTransparent() {
        try {
            getInstrumentation().runOnMainSync(new Runnable() {

                @Override
                public void run() {
                	mXWalkView.setZOrderOnTop(true);
                	mXWalkView.setBackgroundColor(0);
                }
            });
            assertTrue(true);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }

    @SmallTest
    public void testOnCanZoomInAndOut() {
        try {
        	final float mPageMinimumScale = 0.5f;
        	String url = "file:///android_asset/zoom.html";
        	assertFalse("Should not be able to zoom in", canZoomInOnUiThread());
        	loadUrlSync(url);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getScale();
                }
            });
            assertTrue("Should be able to zoom in", canZoomInOnUiThread());
            assertFalse("Should not be able to zoom out", canZoomOutOnUiThread());

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
			// TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
		}
    }
    
    @SmallTest
    public void testOnZoomByLimited() {
        try {
        	final float MAXIMUM_SCALE = 2.0f;
        	final float mPageMinimumScale = 0.5f;
        	String url = "file:///android_asset/zoom.html";
        	assertFalse("Should not be able to zoom in", canZoomInOnUiThread());
        	loadUrlSync(url);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getScale();
                }
            });
            
            zoomByOnUiThreadAndWait(4.0f);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return MAXIMUM_SCALE == mTestHelperBridge.getOnScaleChangedHelper().getScale();
                }
            });
            
            zoomByOnUiThreadAndWait(0.5f);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return MAXIMUM_SCALE * 0.5f == mTestHelperBridge.getOnScaleChangedHelper().getScale();
                }
            });

            zoomByOnUiThreadAndWait(0.01f);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getScale();
                }
            });
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
			// TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
		}
    }
    
    @SmallTest
    public void testOnZoomInAndOut() {
        try {
        	final float mPageMinimumScale = 0.5f;
        	String url = "file:///android_asset/zoom.html";
        	assertFalse("Should not be able to zoom in", canZoomInOnUiThread());
        	loadUrlSync(url);
            pollOnUiThread(new Callable<Boolean>() {
                @Override
                public Boolean call() throws Exception {
                    return mPageMinimumScale == mTestHelperBridge.getOnScaleChangedHelper().getScale();
                }
            });

            while (canZoomInOnUiThread()) {
                zoomInOnUiThreadAndWait();
            }
            assertTrue("Should be able to zoom out", canZoomOutOnUiThread());

            while (canZoomOutOnUiThread()) {
                zoomOutOnUiThreadAndWait();
            }
            assertTrue("Should be able to zoom in", canZoomInOnUiThread());
            
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
			// TODO: handle exception
            assertTrue(false);
            e.printStackTrace();
		}
    }

    @SmallTest
    public void testSetAcceptLanuages() throws Throwable {
        String result;
        final String script = "navigator.languages";
        final String[] languages = {"en;q=0.7", "zh-cn", "da,en-gb;q=0.8,en;q=0.7"};
        final String[] expectedLanguages = {"[\"en;q=0.7\"]", "[\"zh-cn\"]", "[\"da\",\"en-gb;q=0.8\",\"en;q=0.7\"]"};

        result = executeJavaScriptAndWaitForResult(script);
        assertNotNull(result);

        for (int i = 0; i < languages.length; i++) {
            setAcceptLanguages(languages[i]);
            result = executeJavaScriptAndWaitForResult(script);
            assertEquals(expectedLanguages[i], result);
        }
    }
}
