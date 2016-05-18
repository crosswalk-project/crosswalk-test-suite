// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageFinishedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnPageStartedHelper;
import org.chromium.content.browser.test.util.TestCallbackHelperContainer.OnReceivedErrorHelper;
import org.xwalk.core.ClientCertRequest;
import org.xwalk.core.XWalkUIClient.ConsoleMessageType;
import org.xwalk.core.XWalkUIClient.LoadStatus;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkWebResourceRequest;
import org.xwalk.core.XWalkWebResourceResponse;

import android.net.Uri;
import android.webkit.ValueCallback;
import android.webkit.WebResourceResponse;

public class TestHelperBridge {

    private LoadStatus mLoadStatus;
    private String mChangedTitle;
    private final OnPageStartedHelper mOnPageStartedHelper;
    private final OnPageFinishedHelper mOnPageFinishedHelper;
    private final OnTitleUpdatedHelper mOnTitleUpdatedHelper;
    private final OnEvaluateJavaScriptResultHelper mOnEvaluateJavaScriptResultHelper;
    private final OnJavascriptCloseWindowHelper mOnJavascriptCloseWindowHelper;
    private final OnScaleChangedHelper mOnScaleChangedHelper;
    private final OnRequestFocusHelper mOnRequestFocusHelper;
    private final OnCreateWindowRequestedHelper mOnCreateWindowRequestedHelper;
    private final OnIconAvailableHelper mOnIconAvailableHelper;
    private final OnReceivedIconHelper mOnReceivedIconHelper;
    private final OnReceivedErrorHelper mOnReceivedErrorHelper;
    private final OnReceivedSslHelper mOnReceivedSslHelper;
    private final OnLoadStartedHelper mOnLoadStartedHelper;
    private final OnLoadFinishedHelper mOnLoadFinishedHelper;
    private final OnProgressChangedHelper mOnProgressChangedHelper;
    private final ShouldInterceptLoadRequestHelper mShouldInterceptLoadRequestHelper;
    private final ShouldOverrideUrlLoadingHelper mShouldOverrideUrlLoadingHelper;
    private final OnFullscreenToggledHelper mOnFullscreenToggledHelper;
    private final OpenFileChooserHelper mOpenFileChooserHelper;
    private final OnConsoleMessageHelper mOnConsoleMessageHelper;
    private final OnDownloadStartHelper mOnDownloadStartHelper;
    private final OnDocumentLoadedInFrameHelper mOnDocumentLoadedInFrameHelper;
    private final OnReceivedClientCertRequestHelper mOnReceivedClientCertRequestHelper;
    private final OnReceivedHttpAuthRequestHelper mOnReceivedHttpAuthRequestHelper;
    private final OnJsAlertHelper mOnJsAlertHelper;
    private final OnJsConfirmHelper mOnJsConfirmHelper;
    private final OnJsPromptHelper mOnJsPromptHelper;
    private final OnReceivedResponseHeadersHelper mOnReceivedResponseHeadersHelper;
    private final ShouldInterceptLoadRequestHelper2 mShouldInterceptLoadRequestHelper2;

    TestHelperBridge() {
        mOnPageStartedHelper = new OnPageStartedHelper();
        mOnPageFinishedHelper = new OnPageFinishedHelper();
        mOnTitleUpdatedHelper = new OnTitleUpdatedHelper();
        mOnEvaluateJavaScriptResultHelper = new OnEvaluateJavaScriptResultHelper();
        mOnJavascriptCloseWindowHelper = new OnJavascriptCloseWindowHelper();
        mOnScaleChangedHelper = new OnScaleChangedHelper();
        mOnRequestFocusHelper = new OnRequestFocusHelper();
        mOnCreateWindowRequestedHelper = new OnCreateWindowRequestedHelper();
        mOnIconAvailableHelper = new OnIconAvailableHelper();
        mOnReceivedIconHelper = new OnReceivedIconHelper();
        mOnReceivedErrorHelper = new OnReceivedErrorHelper();
        mOnReceivedSslHelper = new OnReceivedSslHelper();
        mOnLoadStartedHelper = new OnLoadStartedHelper();
        mOnLoadFinishedHelper = new OnLoadFinishedHelper();
        mOnProgressChangedHelper = new OnProgressChangedHelper();
        mShouldInterceptLoadRequestHelper = new ShouldInterceptLoadRequestHelper();
        mShouldOverrideUrlLoadingHelper = new ShouldOverrideUrlLoadingHelper();
        mOnFullscreenToggledHelper = new OnFullscreenToggledHelper();
        mOpenFileChooserHelper = new OpenFileChooserHelper();
        mOnConsoleMessageHelper = new OnConsoleMessageHelper();
        mOnDownloadStartHelper = new OnDownloadStartHelper();
        mOnDocumentLoadedInFrameHelper = new OnDocumentLoadedInFrameHelper();
        mOnReceivedClientCertRequestHelper = new OnReceivedClientCertRequestHelper();
        mOnReceivedHttpAuthRequestHelper = new OnReceivedHttpAuthRequestHelper();
        mOnJsAlertHelper = new OnJsAlertHelper();
        mOnJsConfirmHelper = new OnJsConfirmHelper();
        mOnJsPromptHelper = new OnJsPromptHelper();
        mOnReceivedResponseHeadersHelper = new OnReceivedResponseHeadersHelper();
        mShouldInterceptLoadRequestHelper2 = new ShouldInterceptLoadRequestHelper2();
    }

    public WebResourceResponse shouldInterceptLoadRequest(String url) {
        WebResourceResponse response = mShouldInterceptLoadRequestHelper.getReturnValue(url);
        mShouldInterceptLoadRequestHelper.notifyCalled(url);
        return response;
    }

    public XWalkWebResourceResponse shouldInterceptLoadRequest2(String url) {
        XWalkWebResourceResponse response = mShouldInterceptLoadRequestHelper2.getReturnValue(url);
        mShouldInterceptLoadRequestHelper2.notifyCalled(url);
        return response;
    }

    public ShouldInterceptLoadRequestHelper getShouldInterceptLoadRequestHelper() {
        return mShouldInterceptLoadRequestHelper;
    }

    public ShouldInterceptLoadRequestHelper2 getShouldInterceptLoadRequestHelper2() {
        return mShouldInterceptLoadRequestHelper2;
    }

    public OnProgressChangedHelper getOnProgressChangedHelper() {
        return mOnProgressChangedHelper;
    }

    public void onProgressChanged(int progress) {
        mOnProgressChangedHelper.notifyCalled(progress);
    }

    public OnPageFinishedHelper getOnPageFinishedHelper() {
        return mOnPageFinishedHelper;
    }

    public OnPageStartedHelper getOnPageStartedHelper() {
        return mOnPageStartedHelper;
    }

    public void onPageStarted(String url) {
        mOnPageStartedHelper.notifyCalled(url);
    }

    public void onPageFinished(String url, LoadStatus status) {
        mLoadStatus = status;
        mOnPageFinishedHelper.notifyCalled(url);
    }

    public void onLoadStarted(String url) {
        mOnLoadStartedHelper.notifyCalled(url);
    }

    public void onLoadFinished(String url) {
        mOnLoadFinishedHelper.notifyCalled(url);
    }

    public OnLoadStartedHelper getOnLoadStartedHelper() {
        return mOnLoadStartedHelper;
    }

    public OnLoadFinishedHelper getOnLoadFinishedHelper() {
        return mOnLoadFinishedHelper;
    }

    public LoadStatus getLoadStatus() {
        return mLoadStatus;
    }

    public OnTitleUpdatedHelper getOnTitleUpdatedHelper() {
        return mOnTitleUpdatedHelper;
    }

    public OnEvaluateJavaScriptResultHelper getOnEvaluateJavaScriptResultHelper() {
        return mOnEvaluateJavaScriptResultHelper;
    }

   public void onTitleChanged(String title) {
        mChangedTitle = title;
        mOnTitleUpdatedHelper.notifyCalled(title);
    }

    public String getChangedTitle() {
        return mChangedTitle;
    }

    public OnJavascriptCloseWindowHelper getOnJavascriptCloseWindowHelper() {
        return mOnJavascriptCloseWindowHelper;
    }

    public void onJavascriptCloseWindow() {
        mOnJavascriptCloseWindowHelper.notifyCalled(true);
    }

    public OnScaleChangedHelper getOnScaleChangedHelper() {
        return mOnScaleChangedHelper;
    }

    public void onScaleChanged(float oldScale, float newScale) {
        mOnScaleChangedHelper.notifyCalled(oldScale, newScale);
    }

    public OnRequestFocusHelper getOnRequestFocusHelper() {
        return mOnRequestFocusHelper;
    }

    public void onRequestFocus() {
        mOnRequestFocusHelper.notifyCalled(true);
    }

    public OnCreateWindowRequestedHelper getOnCreateWindowRequestedHelper() {
        return mOnCreateWindowRequestedHelper;
    }

    public void onCreateWindowRequested() {
        mOnCreateWindowRequestedHelper.notifyCalled(true);
    }

    public OnIconAvailableHelper getOnIconAvailableHelper() {
        return mOnIconAvailableHelper;
    }

    public void onIconAvailable() {
        mOnIconAvailableHelper.notifyCalled(true);
    }

    public OnReceivedIconHelper getOnReceivedIconHelper() {
        return mOnReceivedIconHelper;
    }

    public void onReceivedIcon() {
        mOnReceivedIconHelper.notifyCalled(true);
    }

    public OnReceivedErrorHelper getOnReceivedErrorHelper() {
        return mOnReceivedErrorHelper;
    }

    public void onReceivedLoadError(int errorCode, String description, String failingUrl) {
        mOnReceivedErrorHelper.notifyCalled(errorCode, description, failingUrl);
    }

    public OnReceivedSslHelper getOnReceivedSslHelper() {
        return mOnReceivedSslHelper;
    }

    public void onReceivedSsl() {
        mOnReceivedSslHelper.notifyCalled(true);
    }

    public ShouldOverrideUrlLoadingHelper getShouldOverrideUrlLoadingHelper() {
        return mShouldOverrideUrlLoadingHelper;
    }

    public boolean shouldOverrideUrlLoading(String url) {
        boolean returnValue = mShouldOverrideUrlLoadingHelper.getShouldOverrideUrlLoadingReturnValue();
        mShouldOverrideUrlLoadingHelper.notifyCalled(url);
        return returnValue;
    }

    public OnFullscreenToggledHelper getOnFullscreenToggledHelper() {
        return mOnFullscreenToggledHelper;
    }

    public void onFullscreenToggled(boolean enterFullscreen) {
        mOnFullscreenToggledHelper.notifyCalled(enterFullscreen);
    }

    public OpenFileChooserHelper getOpenFileChooserHelper() {
        return mOpenFileChooserHelper;
    }

    public void openFileChooser(ValueCallback<Uri> uploadFile) {
        mOpenFileChooserHelper.notifyCalled(uploadFile);
    }

    public OnConsoleMessageHelper getOnConsoleMessageHelper() {
        return mOnConsoleMessageHelper;
    }

    public boolean onConsoleMessage(String message, int lineNumber,
            String sourceId, ConsoleMessageType messageType) {
        mOnConsoleMessageHelper.notifyCalled(message, lineNumber, sourceId, messageType);
        return true;
    }

    public OnDownloadStartHelper getOnDownloadStartHelper() {
        return mOnDownloadStartHelper;
    }

    public void onDownloadStart(String url, String userAgent,
            String contentDisposition, String mimetype, long contentLength) {
        mOnDownloadStartHelper.notifyCalled(url, userAgent, contentDisposition,
                mimetype, contentLength);
    }

    public void onDocumentLoadedInFrame(long frameId) {
        mOnDocumentLoadedInFrameHelper.notifyCalled(frameId);
    }

    public OnDocumentLoadedInFrameHelper getOnDocumentLoadedInFrameHelper() {
        return mOnDocumentLoadedInFrameHelper;
    }

    public OnReceivedClientCertRequestHelper getOnReceivedClientCertRequestHelper() {
        return mOnReceivedClientCertRequestHelper;
    }

    public void onReceivedClientCertRequest(XWalkView view, ClientCertRequest handler) {
        mOnReceivedClientCertRequestHelper.notifyCalled(handler);
    }
    public OnReceivedHttpAuthRequestHelper getOnReceivedHttpAuthRequestHelper() {
        return mOnReceivedHttpAuthRequestHelper;
    }

    public void onReceivedHttpAuthRequest(String host) {
        mOnReceivedHttpAuthRequestHelper.notifyCalled(host);
    }

    public OnJsAlertHelper getOnJsAlertHelper() {
        return mOnJsAlertHelper;
    }

    public OnJsConfirmHelper getOnJsConfirmHelper() {
        return mOnJsConfirmHelper;
    }

    public OnJsPromptHelper getOnJsPromptHelper() {
        return mOnJsPromptHelper;
    }

    public boolean onJsAlert(String message) {
        mOnJsAlertHelper.notifyCalled(message);
        return true;
    }

    public boolean onJsConfirm(String message) {
        mOnJsConfirmHelper.notifyCalled(message);
        return true;
    }

    public boolean onJsPrompt(String message) {
        mOnJsPromptHelper.notifyCalled(message);
        return true;
    }

    public OnReceivedResponseHeadersHelper getOnReceivedResponseHeadersHelper() {
        return mOnReceivedResponseHeadersHelper;
    }

    public void onReceivedResponseHeaders(XWalkView view,
                    XWalkWebResourceRequest request,
                    XWalkWebResourceResponse response) {
        mOnReceivedResponseHeadersHelper.notifyCalled(request, response);
    }
}
