package org.xwalk.embedding.base;

import java.util.concurrent.atomic.AtomicBoolean;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.xwalk.core.XWalkJavascriptResult;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Message;
import android.webkit.ValueCallback;

public class TestXWalkUIClientBase extends XWalkUIClient {
    TestHelperBridge mInnerContentsClient;

    protected final String ALERT_TEXT = "Hello World!";
    final String CONFIRM_TEXT = "Would you like a cookie?";
    boolean flagForConfirmCancelled = false;
    protected final String PROMPT_TEXT = "How do you like your eggs in the morning?";
    protected final String PROMPT_DEFAULT = "Scrambled";
    protected final String PROMPT_RESULT = "I like mine with a kiss";
    final CallbackHelper jsBeforeUnloadHelper = new CallbackHelper();
    AtomicBoolean mInnerCallbackCalled;

    public TestXWalkUIClientBase(TestHelperBridge client, XWalkView mXWalkView, AtomicBoolean callbackCalled) {
        super(mXWalkView);
        mInnerContentsClient = client;
        mInnerCallbackCalled = callbackCalled;
    }

    @Override
    public void onPageLoadStarted(XWalkView view, String url) {
        mInnerContentsClient.onPageStarted(url);
    }

    @Override
    public void onPageLoadStopped(XWalkView view, String url, LoadStatus status) {
        mInnerContentsClient.onPageFinished(url, status);
    }

    @Override
    public void onReceivedTitle(XWalkView view, String title) {
        mInnerContentsClient.onTitleChanged(title);
    }

    @Override
    public void onJavascriptCloseWindow(XWalkView view) {
        mInnerContentsClient.onJavascriptCloseWindow();
    }

    @Override
    public void onScaleChanged(XWalkView view, float oldScale,
            float newScale) {
        mInnerContentsClient.onScaleChanged(oldScale, newScale);
    }

    @Override
    public void onRequestFocus(XWalkView view) {
        mInnerContentsClient.onRequestFocus();
    }

    @Override
    public boolean onCreateWindowRequested(XWalkView view,
            InitiateBy initiator, ValueCallback<XWalkView> callback) {
        mInnerContentsClient.onCreateWindowRequested();
        return true;
    }

    @Override
    public void onIconAvailable(XWalkView view, String url,
            Message startDownload) {
        startDownload.sendToTarget();
        mInnerContentsClient.onIconAvailable();
    }

    @Override
    public void onReceivedIcon(XWalkView view, String url, Bitmap icon) {
        mInnerContentsClient.onReceivedIcon();
    }

    @Override
    public void onFullscreenToggled(XWalkView view, boolean enterFullscreen) {
        mInnerContentsClient.onFullscreenToggled(enterFullscreen);
    }

    @Override
    public void openFileChooser(XWalkView view,
            ValueCallback<Uri> uploadFile, String acceptType, String capture) {
        mInnerContentsClient.openFileChooser(uploadFile);
    }

    @Override
    public boolean onJavascriptModalDialog(XWalkView view, JavascriptMessageType type,
            String url, String message, String defaultValue, XWalkJavascriptResult result) {
        switch(type) {
            case JAVASCRIPT_ALERT:
                 onJsAlert(view, url, message, result);
                 break;
            case JAVASCRIPT_CONFIRM:
                 onJsConfirm(view, url, message, result);
                 break;
            case JAVASCRIPT_PROMPT:
                 onJsPrompt(view, url, message, defaultValue, result);
                 break;
            case JAVASCRIPT_BEFOREUNLOAD:
                // Reuse onJsConfirm to show the dialog.
                onJsConfirm(view, url, message, result);
                break;
            default:
                break;
        }
        return false;
    }

    @Override
    public boolean onConsoleMessage(XWalkView view, String message,
            int lineNumber, String sourceId, ConsoleMessageType messageType) {
        return mInnerContentsClient.onConsoleMessage(message,lineNumber,sourceId, messageType);
    }

    @Override
    public boolean onJsAlert(XWalkView view,
            String url, String message, XWalkJavascriptResult result) {
        return mInnerContentsClient.onJsAlert(message);
    }

    @Override
    public boolean onJsConfirm(XWalkView view,
            String url, String message, XWalkJavascriptResult result) {
        return mInnerContentsClient.onJsConfirm(message);
    }

    @Override
    public boolean onJsPrompt(XWalkView view,
            String url, String message, String defaultValue,
            XWalkJavascriptResult result) {
        return mInnerContentsClient.onJsPrompt(message);
    }
}
