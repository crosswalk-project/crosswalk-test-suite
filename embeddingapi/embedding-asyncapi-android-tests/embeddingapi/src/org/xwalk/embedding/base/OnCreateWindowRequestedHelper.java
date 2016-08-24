package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;
import org.xwalk.core.XWalkView;

public class OnCreateWindowRequestedHelper extends CallbackHelper {
    private boolean mCalled = false;
    private XWalkView mXWalkView;

    public boolean getCalled() {
        assert getCallCount() > 0;
        return mCalled;
    }

    public void notifyCalled(boolean called) {
        mCalled = called;
        notifyCalled();
    }
    
    public XWalkView getXWalkView() {
        assert getCallCount() > 0;
        return mXWalkView;
    }

    public void notifyCalled(XWalkView view) {
        mXWalkView = view;
        notifyCalled();
    }
}
