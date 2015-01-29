package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.xwalk.core.XWalkUIClient.ConsoleMessageType;

public class OnConsoleMessageHelper extends CallbackHelper {
    private String mMessage;
    private ConsoleMessageType mMessageType;

    public String getMessage() {
        return mMessage;
    }

    public ConsoleMessageType getMessageType() {
        return mMessageType;
    }

    public void notifyCalled(String message,
        int lineNumber, String sourceId, ConsoleMessageType messageType) {
        mMessage = message;
        mMessageType = messageType;
        notifyCalled();
    }
}
