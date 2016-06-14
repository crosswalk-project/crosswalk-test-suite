// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashSet;
import java.util.Map;
import java.util.List;
import java.util.Set;
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicReference;

import junit.framework.Assert;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.chromium.content.browser.test.util.Criteria;
import org.chromium.content.browser.test.util.CriteriaHelper;
import org.chromium.net.test.util.TestWebServer;
import org.chromium.ui.gfx.DeviceDisplayInfo;
import org.xwalk.core.JavascriptInterface;
import org.xwalk.core.XWalkCookieManager;
import org.xwalk.core.XWalkDownloadListener;
import org.xwalk.core.XWalkFindListener;
import org.xwalk.core.XWalkNavigationHistory;
import org.xwalk.core.XWalkNavigationItem;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkSettings;
import org.xwalk.embedding.MainActivity;
import org.xwalk.core.XWalkWebResourceResponse;

import com.test.server.ActivityInstrumentationTestCase2;

import android.content.Context;
import android.content.res.AssetManager;
import android.os.Bundle;
import android.test.MoreAsserts;
import android.util.Log;
import android.util.Pair;
import android.graphics.Bitmap;
import android.net.http.SslCertificate;
import android.net.http.SslError;
import android.webkit.ValueCallback;
import android.webkit.WebResourceResponse;

public class XWalkViewTestBase extends ActivityInstrumentationTestCase2<MainActivity> {

    public XWalkViewTestBase(Class<MainActivity> activityClass) {
        super(activityClass);
    }

    protected static final int FIND_ALL = 3;
    protected static final int FIND = 2;

    protected final static String PASS_STRING = "Pass";

    protected static final String EMPTY_PAGE =
            "<!doctype html>" +
            "<title>Set User Agent String Test</title><p>Set User Agent String Test.</p>";

    protected static final String USER_AGENT =
            "Set User Agent String Test Mozilla/5.0 Apple Webkit Cosswalk Mobile Safari";

    protected static final String EXPECTED_USER_AGENT =
            "\"Set User Agent String Test Mozilla/5.0 Apple Webkit Cosswalk Mobile Safari\"";

    protected static final int NUM_OF_CONSOLE_CALL = 10;

    protected static final String REDIRECT_TARGET_PATH = "/redirect_target.html";
    protected static final String TITLE = "TITLE";
    protected final String mExpectedStr = "xwalk";
    protected final String mDefaultTitle = "Add JS Interface";
    protected static final String DATA_URL = "data:text/html,<div/>";

    protected final static int WAIT_TIMEOUT_SECONDS = 15;
    protected final static long WAIT_TIMEOUT_MS = 2000;
    private final static int CHECK_INTERVAL = 100;

    protected XWalkView mXWalkView;
    protected XWalkView mXWalkViewTexture;
    protected XWalkView mRestoreXWalkView;
    protected MainActivity mainActivity;
    protected TestWebServer mWebServer;
    protected TestWebServer mWebServerSsl;
    protected TestXWalkResourceClient mTestXWalkResourceClient;
    protected boolean mAllowSslError = true;
    protected XWalkCookieManager mCookieManager;
    protected final TestHelperBridge mTestHelperBridge = new TestHelperBridge();

    private String mUrls[]=new String[3];

    protected static final int NUM_NAVIGATIONS = 3;

    public static final String TITLES[] = {
        "page 1 title foo",
        "page 2 title bar",
        "page 3 title baz"
    };

    private static final String PATHS[] = {
        "/p1foo.html",
        "/p2bar.html",
        "/p3baz.html",
    };

    protected final String ALERT_TEXT = "Hello World!";
    protected final String PROMPT_TEXT = "How do you like your eggs in the morning?";
    protected final String PROMPT_DEFAULT = "Scrambled";
    protected final String PROMPT_RESULT = "I like mine with a kiss";
    final String CONFIRM_TEXT = "Would you like a cookie?";
    protected final AtomicBoolean callbackCalled = new AtomicBoolean(false);
    final CallbackHelper jsBeforeUnloadHelper = new CallbackHelper();
    boolean flagForConfirmCancelled = false;

    public XWalkViewTestBase() {
        super(MainActivity.class);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        mainActivity = (MainActivity) getActivity();
        mWebServer = TestWebServer.start();
        mWebServerSsl = TestWebServer.startSsl();
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mRestoreXWalkView = new XWalkView(getActivity(), getActivity());
                mXWalkView = mainActivity.getXWalkView();
                mXWalkViewTexture = mainActivity.getXWalkViewTexture();
                mXWalkView.setUIClient(new TestXWalkUIClient());
                mTestXWalkResourceClient = new TestXWalkResourceClient();
                mXWalkView.setResourceClient(mTestXWalkResourceClient);
            }
        });
    }

    protected void loadUrlAsync(final String url) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.load(url, null);
            }
        });
    }

    protected void loadUrlAsync(final String url,final String content) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.load(url, content);
            }
        });
    }

    protected void loadDataAsync(final String url, final String data, final String mimeType,
            final boolean isBase64Encoded) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.load(url, data);
            }
        });
    }

    protected String getTitleOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getTitle();
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

    protected String getFileContent(String fileName) {
        try {
            Context context = getInstrumentation().getContext();
            InputStream inputStream = context.getAssets().open(fileName);
            int size = inputStream.available();
            byte buffer[] = new byte[size];
            inputStream.read(buffer);
            inputStream.close();

            String fileContent = new String(buffer);
            return fileContent;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    protected XWalkView getXWalkView() {
        return mXWalkView;
    }


    protected boolean canGoBackOnUiThread() throws Throwable {
        return runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() {
                return mXWalkView.getNavigationHistory().canGoBack();
            }
        });
    }

    protected boolean hasEnteredFullScreenOnUiThread() throws Throwable {
        return runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() {
                return mXWalkView.hasEnteredFullscreen();
            }
        });
    }

    protected void leaveFullscreenOnUiThread() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.leaveFullscreen();
            }
        });
    }

    protected boolean canGoForwardOnUiThread() throws Throwable {
        return runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() {
                return mXWalkView.getNavigationHistory().canGoForward();
            }
        });
    }

    protected XWalkNavigationItem getCurrentItemOnUiThread() throws Throwable {
        return runTestOnUiThreadAndGetResult(new Callable<XWalkNavigationItem>() {
            @Override
            public XWalkNavigationItem call() {
                return mXWalkView.getNavigationHistory().getCurrentItem();
            }
        });
    }

    protected String executeJavaScriptAndWaitForResult(final String code) throws Exception {
        final OnEvaluateJavaScriptResultHelper helper = mTestHelperBridge.getOnEvaluateJavaScriptResultHelper();
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                helper.evaluateJavascript(mXWalkView, code);
            }
        });
        helper.waitUntilHasValue();
        Assert.assertTrue("Failed to retrieve JavaScript evaluation results.", helper.hasValue());
        return helper.getJsonResultAndClear();
    }

    protected String getUrlOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getUrl();
            }
        });
    }

    protected String getRemoteDebuggingUrlOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                if(mXWalkView.getRemoteDebuggingUrl() == null)
                {
                    return "";
                }
                return mXWalkView.getRemoteDebuggingUrl().getPath();
            }
        });
    }

    protected String getCurrentItemUrlOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getNavigationHistory().getCurrentItem().getUrl();
            }
        });
    }

    protected String getNavigationUrlOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {

                return mXWalkView.getNavigationHistory().getCurrentItem().getUrl();
            }
        });
    }

    protected String getNavigationOriginalUrlOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {

                return mXWalkView.getNavigationHistory().getCurrentItem().getOriginalUrl();
            }
        });
    }

    protected String getNavigationTitleOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getNavigationHistory().getCurrentItem().getTitle();
            }
        });
    }

    protected String getSizeOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return String.valueOf(mXWalkView.getNavigationHistory().size());
            }
        });
    }

    protected String hasItemAtOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return String.valueOf(mXWalkView.getNavigationHistory().hasItemAt(1));
            }
        });
    }

    protected String getOriginalUrlOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getOriginalUrl();
            }
        });
    }

    protected void clearCacheOnUiThread(final boolean includeDiskFiles) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.clearCache(includeDiskFiles);
            }
        });
    }

    protected String getAPIVersionOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getAPIVersion();
            }
        });
    }

    protected String getXWalkVersionOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getXWalkVersion();
            }
        });
    }

    private String getAssetsFileContent(AssetManager assetManager, String fileName)
            throws IOException {
        String result = "";
        InputStream inputStream = null;
        try {
            inputStream = assetManager.open(fileName);
            int size = inputStream.available();
            byte[] buffer = new byte[size];
            inputStream.read(buffer);
            result = new String(buffer);
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
        }
        return result;
    }

    public class PerformExecute implements Runnable
    {
        protected StringBuffer urlBuf;
        public PerformExecute(StringBuffer url) {
            urlBuf = url;
        }
        @Override
        public void run() {


        }
    }

    public static class EmptyInputStream extends InputStream {
        @Override
        public int available() {
            return 0;
        }

        @Override
        public int read() throws IOException {
            return -1;
        }

        @Override
        public int read(byte b[]) throws IOException {
            return -1;
        }

        @Override
        public int read(byte b[], int off, int len) throws IOException {
            return -1;
        }

        @Override
        public long skip(long n) throws IOException {
            if (n < 0)
                throw new IOException("skipping negative number of bytes");
            return 0;
        }
    }

    class TestXWalkFindListener extends XWalkFindListener {
        @Override
        public void onFindResultReceived(int activeMatchOrdinal, int numberOfMatches,
                boolean isDoneCounting) {
            mTestHelperBridge.onFindResultReceived(activeMatchOrdinal, numberOfMatches,
    	        isDoneCounting);
    	}
    }

    protected void setFindListener() {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                getXWalkView().setFindListener(new TestXWalkFindListener());
            }
        });
    }

    protected void goBackSync(final int n) throws Throwable {
        runTestWaitPageFinished(new Runnable(){
            @Override
            public void run() {
                getInstrumentation().runOnMainSync(new Runnable() {
                    @Override
                    public void run() {
                        mXWalkView.getNavigationHistory().navigate(
                            XWalkNavigationHistory.Direction.BACKWARD, n);
                    }
                });
            }
        });
    }

    protected void goForwardSync(final int n) throws Throwable {
        runTestWaitPageFinished(new Runnable(){
            @Override
            public void run() {
                getInstrumentation().runOnMainSync(new Runnable() {
                    @Override
                    public void run() {
                        mXWalkView.getNavigationHistory().navigate(
                            XWalkNavigationHistory.Direction.FORWARD, n);
                    }
                });
            }
        });
    }

    protected void setServerResponseAndLoad(int upto) throws Throwable {
        for (int i = 0; i < upto; ++i) {
            String html = "<html><head><title>" + TITLES[i] + "</title></head></html>";
            mUrls[i] = mWebServer.setResponse(PATHS[i], html, null);
            loadUrlSync(mUrls[i]);
        }
    }

    protected void saveAndRestoreStateOnUiThread() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                Bundle bundle = new Bundle();
                mXWalkView.saveState(bundle);
                mRestoreXWalkView.restoreState(bundle);
            }
        });
    }

    protected boolean pollOnUiThread(final Callable<Boolean> callable) throws Exception {
        return CriteriaHelper.pollForCriteria(new Criteria() {
            @Override
            public boolean isSatisfied() {
                try {
                    return runTestOnUiThreadAndGetResult(callable);
                } catch (Throwable e) {
                    return false;
                }
            }
        });
    }

    protected void checkHistoryItemList(XWalkView restoreXWalkView) throws Throwable {
        XWalkNavigationHistory history = getNavigationHistoryOnUiThread(restoreXWalkView);
        assertEquals(NUM_NAVIGATIONS, history.size());
        assertEquals(NUM_NAVIGATIONS - 1, history.getCurrentIndex());

        for (int i = 0; i < NUM_NAVIGATIONS; ++i) {
            assertEquals(mUrls[i], history.getItemAt(i).getUrl());
            assertEquals(TITLES[i], history.getItemAt(i).getTitle());
        }
    }

    private XWalkNavigationHistory getNavigationHistoryOnUiThread(
            final XWalkView content) throws Throwable{
        return runTestOnUiThreadAndGetResult(new Callable<XWalkNavigationHistory>() {
            @Override
            public XWalkNavigationHistory call() throws Exception {
                return content.getNavigationHistory();
            }
        });
    }

    @Override
    protected void tearDown() throws Exception {
        if (mWebServer != null) {
            mWebServer.shutdown();
        }
        if (mWebServerSsl != null) {
            mWebServerSsl.shutdown();
        }
        if(mainActivity != null)
        {
            mainActivity.finish();
        }
        super.tearDown();
    }

    public class TestJavascriptInterface {
        @JavascriptInterface
        public String getTextWithoutAnnotation() {
            return mExpectedStr;
        }

        @JavascriptInterface
        public String getText() {
            return mExpectedStr;
        }

        @JavascriptInterface
        public String getDateText() {
            return new Date().toString();
        }
    }

    protected void addJavascriptInterface() {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                getXWalkView().addJavascriptInterface(new TestJavascriptInterface(),
                        "testInterface");
            }
        });
    }

    protected void removeJavascriptInterface() {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                getXWalkView().removeJavascriptInterface("testInterface");
            }
        });
    }

    protected void raisesExceptionAndSetTitle(String script) throws Throwable {
        executeJavaScriptAndWaitForResult("try { var title = " +
                                          script + ";" +
                                          "  document.title = title;" +
                                          "} catch (exception) {" +
                                          "  document.title = \"error\";" +
                                          "}");
    }

    public class TestXWalkUIClient extends TestXWalkUIClientBase {
        public TestXWalkUIClient() {
            super(mTestHelperBridge, mXWalkView, callbackCalled);
        }
    }

    class TestXWalkResourceClient extends TestXWalkResourceClientBase {
        public TestXWalkResourceClient() {
            super(mTestHelperBridge,mXWalkView);
        }

        @Override
        public void onReceivedSslError(XWalkView view,
                ValueCallback<Boolean> callback, SslError error) {
            if(error.getUrl().endsWith("html")){
                callback.onReceiveValue(mAllowSslError);
                mTestHelperBridge.onReceivedSsl();
            }
        }
    }

    protected void loadUrlSync(final String url) throws Exception {
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        loadUrlAsync(url);
        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void loadUrlSync(final String url, final String content) throws Exception {
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        loadUrlAsync(url, content);
        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void loadJavaScriptSync(final String url, final String code) throws Exception {
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        loadUrlAsync(url);
        loadUrlAsync(code);
        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void loadFromManifestSync(final String path, final String name) throws Exception {
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        loadFromManifestAsync(path, name);
        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void loadFromManifestAsync(final String path, final String name) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                String manifestContent = "";
                try {
                    manifestContent = getAssetsFileContent(mainActivity.getAssets(), name);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                mXWalkView.loadAppFromManifest(path, manifestContent);
            }
        });
    }

    protected void loadAssetFile(String fileName) throws Exception {
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        String fileContent = getFileContent(fileName);
        loadDataAsync(fileName, fileContent, "text/html", false);

        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void runTestWaitPageFinished(Runnable runnable) throws Exception{
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        runnable.run();
        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void reloadSync(final int mode) throws Exception {
        runTestWaitPageFinished(new Runnable(){
            @Override
            public void run() {
                getInstrumentation().runOnMainSync(new Runnable() {
                    @Override
                    public void run() {
                        mXWalkView.reload(mode);
                    }
                });
            }
        });
    }

    protected void loadDataSync(final String url, final String data, final String mimeType,
            final boolean isBase64Encoded) throws Exception {
        CallbackHelper pageFinishedHelper = mTestHelperBridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        loadDataAsync(url, data, mimeType, isBase64Encoded);
        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    public void loadAssetFileAndWaitForTitle(String fileName) throws Exception {
        CallbackHelper getTitleHelper = mTestHelperBridge.getOnTitleUpdatedHelper();
        int currentCallCount = getTitleHelper.getCallCount();
        String fileContent = getFileContent(fileName);

        loadDataSync(fileName, fileContent, "text/html", false);

        getTitleHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    public boolean checkMethodInClass(Class<?> clazz, String methodName){
        Method[] methods = clazz.getMethods();
        for(Method method : methods)
        {
            if(method.getName().equals(methodName)){
                return true;
            }
        }
        Method[] methods2 = clazz.getDeclaredMethods();
        for(Method method : methods2)
        {
            if(method.getName().equals(methodName)){
                return true;
            }
        }
        return false;
    }

    public void clickOnElementId_evaluateJavascript(final String id) throws Exception {
        Assert.assertTrue(CriteriaHelper.pollForCriteria(new Criteria() {
            @Override
            public boolean isSatisfied() {
                try {
                    String idIsNotNull = executeJavaScriptAndWaitForResult(
                        "document.getElementById('" + id + "') != null");
                    return idIsNotNull.equals("true");
                } catch (Throwable t) {
                    t.printStackTrace();
                    Assert.fail("Failed to check if DOM is loaded: " + t.toString());
                    return false;
                }
            }
        }, WAIT_TIMEOUT_MS, CHECK_INTERVAL));
        try {
            executeJavaScriptAndWaitForResult(
                    "var evObj = document.createEvent('Events'); " +
                    "evObj.initEvent('click', true, false); " +
                    "document.getElementById('" + id + "').dispatchEvent(evObj);" +
                    "console.log('element with id [" + id + "] clicked');");
          } catch (Throwable t) {
              t.printStackTrace();
          }
    }

    public void clickOnElementId(final String id, String frameName) throws Exception {
        String str;
        if (frameName != null) {
            str = "top.window." + frameName + ".document.getElementById('" + id + "')";
        } else {
            str = "document.getElementById('" + id + "')";
        }
        final String script1 = str + " != null";
        final String script2 = str + ".dispatchEvent(evObj);";
        Assert.assertTrue(CriteriaHelper.pollForCriteria(new Criteria() {
            @Override
            public boolean isSatisfied() {
                try {
                    String idIsNotNull = executeJavaScriptAndWaitForResult(script1);
                    return idIsNotNull.equals("true");
                } catch (Throwable t) {
                    t.printStackTrace();
                    Assert.fail("Failed to check if DOM is loaded: " + t.toString());
                    return false;
                }
            }
        }, WAIT_TIMEOUT_MS, CHECK_INTERVAL));

        try {
          loadJavaScriptUrl("javascript:var evObj = document.createEvent('Events'); " +
          "evObj.initEvent('click', true, false); " +
          script2 +
          "console.log('element with id [" + id + "] clicked');");
        } catch (Throwable t) {
            t.printStackTrace();
        }
    }

    protected String addPageToTestServer(TestWebServer webServer, String httpPath, String html) {
        List<Pair<String, String>> headers = new ArrayList<Pair<String, String>>();
        headers.add(Pair.create("Content-Type", "text/html"));
        headers.add(Pair.create("Cache-Control", "no-store"));
        return webServer.setResponse(httpPath, html, headers);
    }

    protected void stopLoading() throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.stopLoading();
            }
        });
    }

    protected void pauseTimers() throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.pauseTimers();
            }
        });
    }

    protected void resumeTimers() throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.resumeTimers();
            }
        });
    }

    protected void onHide() throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.onHide();
            }
        });
    }

    protected void onShow() throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.onShow();
            }
        });
    }

    protected void onDestroy() throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.onDestroy();
            }
        });
    }

    protected void setDownloadListener() {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.setDownloadListener(new XWalkDownloadListener(getActivity()) {

                    @Override
                    public void onDownloadStart(String url, String userAgent,
                            String contentDisposition, String mimetype, long contentLength) {
                        // TODO Auto-generated method stub
                        mTestHelperBridge.onDownloadStart(url, userAgent, contentDisposition,
                                mimetype, contentLength);
                    }
                });
            }
        });
    }

    protected boolean canZoomInOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return mXWalkView.canZoomIn();
            }
        });
    }

    protected boolean canZoomOutOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return mXWalkView.canZoomOut();
            }
        });
    }

    protected void zoomInOnUiThreadAndWait() throws Throwable {
        final double dipScale = DeviceDisplayInfo.create(getActivity()).getDIPScale() ;
        final float previousScale = mTestHelperBridge.getOnScaleChangedHelper().getNewScale() * (float)dipScale;
        assertTrue(runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return mXWalkView.zoomIn();
            }
        }));
        // The zoom level is updated asynchronously.
        pollOnUiThread(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return previousScale != mTestHelperBridge.getOnScaleChangedHelper().getNewScale() * (float)dipScale;
            }
        });
    }

    protected void zoomOutOnUiThreadAndWait() throws Throwable {
        final double dipScale = DeviceDisplayInfo.create(getActivity()).getDIPScale() ;
        final float previousScale = mTestHelperBridge.getOnScaleChangedHelper().getNewScale() * (float)dipScale;
        assertTrue(runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return mXWalkView.zoomOut();
            }
        }));
        // The zoom level is updated asynchronously.
        pollOnUiThread(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return previousScale != mTestHelperBridge.getOnScaleChangedHelper().getNewScale() * (float)dipScale;
            }
        });
    }

    protected void zoomByOnUiThreadAndWait(final float delta) throws Throwable {
        final double dipScale = DeviceDisplayInfo.create(getActivity()).getDIPScale() ;
        final float previousScale = mTestHelperBridge.getOnScaleChangedHelper().getNewScale() * (float)dipScale;
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.zoomBy(delta);
            }
        });
        // The zoom level is updated asynchronously.
        pollOnUiThread(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return previousScale != mTestHelperBridge.getOnScaleChangedHelper().getNewScale() * (float)dipScale;
            }
        });
    }

    protected void setAcceptLanguages(final String languages) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.setAcceptLanguages(languages);
            }
        });
    }

    protected void setUserAgent(final String userAgent) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.setUserAgentString(userAgent);
            }
        });
    }

    protected String getUserAgent() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return mXWalkView.getUserAgentString();
            }
        });
    }

    protected void setCookie(final String name, final String value) throws Exception {
        String jsCommand = "javascript:void((function(){" +
                "var expirationDate = new Date();" +
                "expirationDate.setDate(expirationDate.getDate() + 5);" +
                "document.cookie='" + name + "=" + value +
                        "; expires=' + expirationDate.toUTCString();" +
                "})())";
        loadJavaScriptUrl(jsCommand);
    }

    protected void waitForCookie(final String url) throws InterruptedException {
        assertTrue(CriteriaHelper.pollForCriteria(new Criteria() {
            @Override
            public boolean isSatisfied() {
                return mCookieManager.getCookie(url) != null;
            }
        }, 6000, 50));
    }

    protected void validateCookies(String responseCookie, String... expectedCookieNames) {
        String[] cookies = responseCookie.split(";");
        Set<String> foundCookieNames = new HashSet<String>();
        for (String cookie : cookies) {
            foundCookieNames.add(cookie.substring(0, cookie.indexOf("=")).trim());
        }
        MoreAsserts.assertEquals(
                foundCookieNames, new HashSet<String>(Arrays.asList(expectedCookieNames)));
    }

    protected String makeExpiringCookie(String cookie, int secondsTillExpiry) {
        return makeExpiringCookieMs(cookie, secondsTillExpiry * 1000);
    }

    @SuppressWarnings("deprecation")
    protected String makeExpiringCookieMs(String cookie, int millisecondsTillExpiry) {
        Date date = new Date();
        date.setTime(date.getTime() + millisecondsTillExpiry);
        return cookie + "; expires=" + date.toGMTString();
    }

    protected boolean fileURLCanSetCookie(String suffix) throws Throwable {
        String value = "value" + suffix;
        String url = "file:///android_asset/cookie_test.html?value=" + value;
        loadUrlSync(url);
        String cookie = mCookieManager.getCookie(url);
        return cookie != null && cookie.contains("test=" + value);
    }

    public static final String ABOUT_TITLE = "About the Google";

    protected String addAboutPageToTestServer(TestWebServer webServer) {
        return addPageToTestServer(webServer, "/" + "about.html", "<html><head><title>" + ABOUT_TITLE + "</title></head></html>");
    }

    protected WebResourceResponse stringToWebResourceResponse(String input) throws Throwable {
        final String mimeType = "text/html";
        final String encoding = "UTF-8";

        return new WebResourceResponse(
                mimeType, encoding, new ByteArrayInputStream(input.getBytes(encoding)));
    }

    protected void loadJavaScriptUrl(final String url) throws Exception {
        if (!url.startsWith("javascript:")) {
            Log.w("Test", "loadJavascriptUrl only accepts javascript: url");
            return;
        }
        loadUrlAsync(url);
    }

    protected void setInitialScale(final int scaleInPercent) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.setInitialScale(scaleInPercent);
            }
        });
    }

    protected double getDipScale() {
        return DeviceDisplayInfo.create(mXWalkView.getContext()).getDIPScale();
    }

    protected float getScaleFactor() {
        return getPixelScale() / (float) getDipScale();
    }

    public float getPixelScale() {
        return mTestHelperBridge.getOnScaleChangedHelper().getNewScale();
    }

    protected void ensureScaleBecomes(final float targetScale) throws Throwable {
        pollOnUiThread(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return targetScale == getScaleFactor();
            }
        });
    }

    protected void clearSingleCacheOnUiThread(final String url) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.clearCacheForSingleFile(url);
            }
        });
    }

    protected XWalkSettings getXWalkSettingsOnUiThreadByXWalkView(
            final XWalkView view) throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<XWalkSettings>() {
            @Override
            public XWalkSettings call() throws Exception {
                return view.getSettings();
            }
        });
    }

    protected Bitmap getFaviconOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<Bitmap>() {
            @Override
            public Bitmap call() throws Exception {
                return mXWalkView.getFavicon();
            }
        });
    }

    protected void setAllowSslError(boolean allow) {
        mAllowSslError = allow;
    }

    protected void clearSslPreferences() throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.clearSslPreferences();
            }
        });
    }

    protected XWalkWebResourceResponse stringToWebResourceResponse2(String input) throws Throwable {
        final String mimeType = "text/html";
        final String encoding = "UTF-8";

        return mTestXWalkResourceClient.createXWalkWebResourceResponse(
                mimeType, encoding, new ByteArrayInputStream(input.getBytes(encoding)));
    }

    protected void loadUrlWithHeaders(final String url, final Map<String, String> headers) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.load(url, null, headers);
            }
        });
    }

    protected SslCertificate getCertificateOnUiThread() throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<SslCertificate>() {
            @Override
            public SslCertificate call() throws Exception {
                return mXWalkView.getCertificate();
            }
        });
    }


    protected void findAllAsync(final String text) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.findAllAsync(text);
            }
        });
    }

    protected void findAllSync(CallbackHelper mOnFindResultReceivedHelper, int count, final String text) throws InterruptedException, TimeoutException {
    	int currentCallCount = mOnFindResultReceivedHelper.getCallCount();
    	findAllAsync(text);
        mOnFindResultReceivedHelper.waitForCallback(currentCallCount, count);
    }

    protected void findNextAsync(final boolean forward) {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                mXWalkView.findNext(forward);
            }
        });
    }


    protected void runPerViewSettingsTest(XWalkSettingsTestHelper<?> helper0,
            XWalkSettingsTestHelper<?> helper1) throws Throwable {
        helper0.ensureSettingHasInitialValue();
        helper1.ensureSettingHasInitialValue();
        helper1.setAlteredSettingValue();
        helper0.ensureSettingHasInitialValue();
        helper1.ensureSettingHasAlteredValue();

        helper1.setInitialSettingValue();
        helper0.ensureSettingHasInitialValue();
        helper1.ensureSettingHasInitialValue();

        helper0.setAlteredSettingValue();
        helper0.ensureSettingHasAlteredValue();
        helper1.ensureSettingHasInitialValue();

        helper0.setInitialSettingValue();
        helper0.ensureSettingHasInitialValue();
        helper1.ensureSettingHasInitialValue();

        helper0.setAlteredSettingValue();
        helper0.ensureSettingHasAlteredValue();
        helper1.ensureSettingHasInitialValue();

        helper1.setAlteredSettingValue();
        helper0.ensureSettingHasAlteredValue();
        helper1.ensureSettingHasAlteredValue();

        helper0.setInitialSettingValue();
        helper0.ensureSettingHasInitialValue();
        helper1.ensureSettingHasAlteredValue();

        helper1.setInitialSettingValue();
        helper0.ensureSettingHasInitialValue();
        helper1.ensureSettingHasInitialValue();
    }

    protected XWalkView createXWalkViewContainerOnMainSync(
            final Context context,
            final XWalkUIClient uiClient,
            final XWalkResourceClient resourceClient) throws Exception {
        final AtomicReference<XWalkView> xWalkViewContainer =
                new AtomicReference<XWalkView>();
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                xWalkViewContainer.set(new XWalkView(context, getActivity()));
                getActivity().addView(xWalkViewContainer.get());
                xWalkViewContainer.get().setUIClient(uiClient);
                xWalkViewContainer.get().setResourceClient(resourceClient);
            }
        });

        return xWalkViewContainer.get();
    }

    public static class ViewPair {
        private final XWalkView view0;
        private final TestHelperBridge bridge0;
        private final XWalkView view1;
        private final TestHelperBridge bridge1;

        ViewPair(XWalkView view0, TestHelperBridge bridge0,
                XWalkView view1, TestHelperBridge bridge1) {
            this.view0 = view0;
            this.bridge0 = bridge0;
            this.view1 = view1;
            this.bridge1 = bridge1;
        }

        public XWalkView getView0() {
            return view0;
        }

        public TestHelperBridge getBridge0() {
            return bridge0;
        }

        public XWalkView getView1() {
            return view1;
        }

        public TestHelperBridge getBridge1() {
            return bridge1;
        }
    }

    protected ViewPair createViews() throws Throwable {
        TestHelperBridge helperBridge0 = new TestHelperBridge();
        TestHelperBridge helperBridge1 = new TestHelperBridge();
        TestXWalkUIClientBase uiClient0 = new TestXWalkUIClientBase(helperBridge0, mXWalkView, callbackCalled);
        TestXWalkUIClientBase uiClient1 = new TestXWalkUIClientBase(helperBridge1, mXWalkView, callbackCalled);
        TestXWalkResourceClientBase  resourceClient0=
                new TestXWalkResourceClientBase(helperBridge0, mXWalkView);
        TestXWalkResourceClientBase resourceClient1 =
                new TestXWalkResourceClientBase(helperBridge1, mXWalkView);
        ViewPair viewPair =
                createViewsOnMainSync(helperBridge0, helperBridge1, uiClient0, uiClient1,
                        resourceClient0, resourceClient1, getActivity());

        return viewPair;
    }

    protected ViewPair createViewsOnMainSync(final TestHelperBridge helperBridge0,
                                             final TestHelperBridge helperBridge1,
                                             final XWalkUIClient uiClient0,
                                             final XWalkUIClient uiClient1,
                                             final XWalkResourceClient resourceClient0,
                                             final XWalkResourceClient resourceClient1,
                                             final Context context) throws Throwable {
        final XWalkView walkView0 = createXWalkViewContainerOnMainSync(context,
                uiClient0, resourceClient0);
        final XWalkView walkView1 = createXWalkViewContainerOnMainSync(context,
                uiClient1, resourceClient1);
        final AtomicReference<ViewPair> viewPair = new AtomicReference<ViewPair>();

        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                viewPair.set(new ViewPair(walkView0, helperBridge0, walkView1, helperBridge1));
            }
        });

        return viewPair.get();
    }

    protected void loadDataAsyncWithXWalkView(final String data,
            final XWalkView view) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                view.load(null, data);
            }
        });
    }


    protected void findNextSync(CallbackHelper mOnFindResultReceivedHelper, int count, final boolean bool) throws InterruptedException, TimeoutException {
    	int currentCallCount = mOnFindResultReceivedHelper.getCallCount();
    	findNextAsync(bool);
        mOnFindResultReceivedHelper.waitForCallback(currentCallCount, count);
    }

    protected void loadDataSyncWithXWalkView(final String data,
            final XWalkView view, final TestHelperBridge bridge) throws Exception {
        CallbackHelper pageFinishedHelper = bridge.getOnPageFinishedHelper();
        int currentCallCount = pageFinishedHelper.getCallCount();
        loadDataAsyncWithXWalkView(data, view);
        pageFinishedHelper.waitForCallback(currentCallCount, 1, WAIT_TIMEOUT_SECONDS,
                TimeUnit.SECONDS);
    }

    protected void setUseWideViewPortOnUiThreadByXWalkView(final boolean value,
            final XWalkView view) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                view.getSettings().setUseWideViewPort(value);
            }
        });
    }

    abstract class XWalkSettingsTestHelper<T> {
        protected final XWalkView mXWalkViewForHelper;
        protected final XWalkSettings mXWalkSettingsForHelper;

        XWalkSettingsTestHelper(XWalkView view) throws Throwable {
            mXWalkViewForHelper = view;
            mXWalkSettingsForHelper = getXWalkSettingsOnUiThreadByXWalkView(view);
        }

        void ensureSettingHasAlteredValue() throws Throwable {
            ensureSettingHasValue(getAlteredValue());
        }

        void ensureSettingHasInitialValue() throws Throwable {
            ensureSettingHasValue(getInitialValue());
        }

        void setAlteredSettingValue() throws Throwable {
            setCurrentValue(getAlteredValue());
        }

        void setInitialSettingValue() throws Throwable {
            setCurrentValue(getInitialValue());
        }

        protected abstract T getAlteredValue();

        protected abstract T getInitialValue();

        protected abstract T getCurrentValue();

        protected abstract void setCurrentValue(T value) throws Throwable;

        protected abstract void doEnsureSettingHasValue(T value) throws Throwable;

        private void ensureSettingHasValue(T value) throws Throwable {
            assertEquals(value, getCurrentValue());
            doEnsureSettingHasValue(value);
        }
    }

    private static final boolean ENABLED = true;	
    private static final boolean DISABLED = false;


    private float getScaleFactorByXWalkViewAndHelperBridge(final XWalkView view,
            final TestHelperBridge bridge) {
        final float newScale = bridge.getOnScaleChangedHelper().getNewScale();
        // If new scale is 0.0f, it means the page does not zoom,
        // return the default scale factior: 1.0f.
        if (Float.compare(newScale, 0.0f) == 0) return 1.0f;
        return newScale / (float) DeviceDisplayInfo.create(view.getContext()).getDIPScale();
    }

    protected void setLoadWithOverviewModeOnUiThreadByXWalkView(
            final boolean value, final XWalkView view) throws Exception {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                view.getSettings().setLoadWithOverviewMode(value);
            }
        });
    }

    protected boolean getLoadWithOverviewModeOnUiThreadByXWalkView(
            final XWalkView view) throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
                return view.getSettings().getLoadWithOverviewMode();
            }
        });
    }

    public class XWalkSettingsLoadWithOverviewModeTestHelper extends XWalkSettingsTestHelper<Boolean> {
        private static final float DEFAULT_PAGE_SCALE = 1.0f;
        private final boolean mWithViewPortTag;
        private boolean mExpectScaleChange;
        private int mOnScaleChangedCallCount;
        XWalkView mView;
        TestHelperBridge mBridge;

        public XWalkSettingsLoadWithOverviewModeTestHelper(
                XWalkView view,
                TestHelperBridge bridge,
                boolean withViewPortTag) throws Throwable {
            super(view);
            mView = view;
            mBridge = bridge;
            mWithViewPortTag = withViewPortTag;
            setUseWideViewPortOnUiThreadByXWalkView(true, view);
        }

        @Override
        protected Boolean getAlteredValue() {
            return ENABLED;
        }

        @Override
        protected Boolean getInitialValue() {
            return DISABLED;
        }

        @Override
        protected Boolean getCurrentValue() {
            try {
                return getLoadWithOverviewModeOnUiThreadByXWalkView(mView);
            } catch (Exception e) {
                return false;
            }
        }

        @Override
        protected void setCurrentValue(Boolean value) {
            try {
                mExpectScaleChange = getLoadWithOverviewModeOnUiThreadByXWalkView(mView) != value;
                if (mExpectScaleChange)
                    mOnScaleChangedCallCount = mBridge.getOnScaleChangedHelper().getCallCount();
                setLoadWithOverviewModeOnUiThreadByXWalkView(value, mView);
            } catch (Exception e) {
            }
        }

        @Override
        protected void doEnsureSettingHasValue(Boolean value) throws Throwable {
            loadDataSyncWithXWalkView(getData(), mView, mBridge);
            if (mExpectScaleChange) {
                mBridge.getOnScaleChangedHelper().waitForCallback(mOnScaleChangedCallCount);
                mExpectScaleChange = false;
            }

            float currentScale = getScaleFactorByXWalkViewAndHelperBridge(mView, mBridge);
            if (value) {
                assertTrue("Expected: " + currentScale + " < " + DEFAULT_PAGE_SCALE,
                        currentScale < DEFAULT_PAGE_SCALE);
            } else {
                assertEquals(DEFAULT_PAGE_SCALE, currentScale);
            }
        }

        private String getData() {
            return "<html><head>"
                    + (mWithViewPortTag ? "<meta name='viewport' content='width=3000' />" : "")
                    + "</head>"
                    + "<body></body></html>";
        }
    }

    public static final String SURFACE_VIEW = "SurfaceView";
    public static final String TEXTURE_VIEW = "TextureView";

    protected String getBackendTypeOnUiThread(final XWalkView view) throws Exception {
        return runTestOnUiThreadAndGetResult(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return view.getCompositingSurfaceType();
            }
        });
    }
}
