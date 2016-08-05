// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import android.app.Activity;
import android.test.ActivityInstrumentationTestCase2;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.FrameLayout;

import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.TimeUnit;

import org.chromium.content.browser.ContentViewCore;
import org.chromium.content.browser.test.util.CallbackHelper;
import org.chromium.content.browser.test.util.Criteria;
import org.chromium.content.browser.test.util.CriteriaHelper;
import org.xwalk.core.internal.XWalkResourceClientInternal;
import org.xwalk.core.internal.XWalkUIClientInternal;
import org.xwalk.core.internal.XWalkViewInternal;
import org.xwalk.core.internal.XWalkWebChromeClient;
import static org.chromium.base.test.util.ScalableTimeout.scaleTimeout;

public class XWalkViewInternalTestBase
       extends ActivityInstrumentationTestCase2<XWalkViewInternalTestRunnerActivity> {
    protected final static int WAIT_TIMEOUT_SECONDS = 15;
    private static final long WAIT_TIMEOUT_MS = scaleTimeout(15000);
    private static final int CHECK_INTERVAL = 100;
    private final static String TAG = "XWalkViewInternalTestBase";
    private XWalkViewInternal mXWalkViewInternal;
    final TestHelperBridge mTestHelperBridge = new TestHelperBridge();

    class TestXWalkUIClientInternalBase extends XWalkUIClientInternal {
        TestHelperBridge mInnerContentsClient;
        public TestXWalkUIClientInternalBase(TestHelperBridge client) {
            super(getXWalkView());
            mInnerContentsClient = client;
        }

        @Override
        public void onPageLoadStarted(XWalkViewInternal view, String url) {
            mInnerContentsClient.onPageStarted(url);
        }

        @Override
        public void onPageLoadStopped(XWalkViewInternal view, String url, LoadStatusInternal status) {
            mInnerContentsClient.onPageFinished(url);
        }

        @Override
        public void onReceivedTitle(XWalkViewInternal view, String title) {
            mInnerContentsClient.onTitleChanged(title);
        }
    }

    class TestXWalkUIClientInternal extends TestXWalkUIClientInternalBase {
        public TestXWalkUIClientInternal() {
            super(mTestHelperBridge);
        }
    }

    class TestXWalkResourceClientBase extends XWalkResourceClientInternal {
        TestHelperBridge mInnerContentsClient;
        public TestXWalkResourceClientBase(TestHelperBridge client) {
            super(mXWalkViewInternal);
            mInnerContentsClient = client;
        }

        @Override
        public void onLoadStarted(XWalkViewInternal view, String url) {
            mInnerContentsClient.onLoadStarted(url);
        }

        @Override
        public void onReceivedLoadError(XWalkViewInternal view, int errorCode,
                String description, String failingUrl) {
            mInnerContentsClient.onReceivedLoadError(errorCode, description, failingUrl);
        }

    }

    class TestXWalkResourceClient extends TestXWalkResourceClientBase {
        public TestXWalkResourceClient() {
            super(mTestHelperBridge);
        }
    }

    class TestXWalkWebChromeClientBase extends XWalkWebChromeClient {
        private CallbackHelper mOnShowCustomViewCallbackHelper = new CallbackHelper();
        private CallbackHelper mOnHideCustomViewCallbackHelper = new CallbackHelper();

        private Activity mActivity = getActivity();
        private View mCustomView;
        private XWalkWebChromeClient.CustomViewCallback mExitCallback;

        public TestXWalkWebChromeClientBase() {
            super(mXWalkViewInternal);
        }

        @Override
        public void onShowCustomView(View view, XWalkWebChromeClient.CustomViewCallback callback) {
            mCustomView = view;
            mExitCallback = callback;
            mActivity.getWindow().setFlags(
                    WindowManager.LayoutParams.FLAG_FULLSCREEN,
                    WindowManager.LayoutParams.FLAG_FULLSCREEN);

            mActivity.getWindow().addContentView(view,
                    new FrameLayout.LayoutParams(
                            ViewGroup.LayoutParams.MATCH_PARENT,
                            ViewGroup.LayoutParams.MATCH_PARENT,
                            Gravity.CENTER));
            mOnShowCustomViewCallbackHelper.notifyCalled();
        }

        @Override
        public void onHideCustomView() {
            mActivity.getWindow().clearFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);
            mOnHideCustomViewCallbackHelper.notifyCalled();
        }

        public XWalkWebChromeClient.CustomViewCallback getExitCallback() {
            return mExitCallback;
        }

        public View getCustomView() {
            return mCustomView;
        }

        public boolean wasCustomViewShownCalled() {
            return mOnShowCustomViewCallbackHelper.getCallCount() > 0;
        }

        public void waitForCustomViewShown() throws TimeoutException, InterruptedException {
            mOnShowCustomViewCallbackHelper.waitForCallback(0, 1, WAIT_TIMEOUT_SECONDS, TimeUnit.SECONDS);
        }

        public void waitForCustomViewHidden() throws InterruptedException, TimeoutException {
            mOnHideCustomViewCallbackHelper.waitForCallback(0, 1, WAIT_TIMEOUT_SECONDS, TimeUnit.SECONDS);
        }
    }

    void setUIClient(final XWalkUIClientInternal client) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                getXWalkView().setUIClient(client);
            }
        });
    }

    void setResourceClient(final XWalkResourceClientInternal client) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                getXWalkView().setResourceClient(client);
            }
        });
    }

    void setXWalkWebChromeClient(final TestXWalkWebChromeClientBase client) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkViewInternal.setXWalkWebChromeClient(client);
            }
        });
    }

    public XWalkViewInternalTestBase() {
        super(XWalkViewInternalTestRunnerActivity.class);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        // Must call getActivity() here but not in main thread.
        final Activity activity = getActivity();
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkViewInternal = new XWalkViewInternal(activity, activity);
                mXWalkViewInternal.setUIClient(new TestXWalkUIClientInternal());
                mXWalkViewInternal.setResourceClient(new TestXWalkResourceClient());
            }
        });
    }

    protected void pollOnUiThread(final Callable<Boolean> callable) throws Exception {
        poll(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return runTestOnUiThreadAndGetResult(callable);
            }
        });
    }

    protected void loadUrlSync(final String url) throws Exception {
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        loadUrlAsync(url);

        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void loadUrlAsync(final String url) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkViewInternal.load(url, null);
            }
        });
    }

    protected void loadDataAsync(final String url, final String data, final String mimeType,
             final boolean isBase64Encoded) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkViewInternal.load(url, data);
            }
        });
    }

    protected <R> R runTestOnUiThreadAndGetResult(Callable<R> callable)
            throws Exception {
        FutureTask<R> task = new FutureTask<R>(callable);
        getInstrumentation().waitForIdleSync();
        getInstrumentation().runOnMainSync(task);
        return task.get();
    }

    protected XWalkViewInternal getXWalkView() {
        return mXWalkViewInternal;
    }

    protected ContentViewCore getContentViewCore() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<ContentViewCore>() {
            @Override
            public ContentViewCore call() throws Exception {
                return mXWalkViewInternal.getXWalkContentForTest();
            }
        });
    }

    protected void poll(final Callable<Boolean> callable) throws Exception {
        CriteriaHelper.pollForCriteria(new Criteria() {
            @Override
            public boolean isSatisfied() {
                try {
                    return callable.call();
                } catch (Throwable e) {
                    Log.e(TAG, "Exception while polling.", e);
                    return false;
                }
            }
        }, WAIT_TIMEOUT_MS, CHECK_INTERVAL);
    }
}

