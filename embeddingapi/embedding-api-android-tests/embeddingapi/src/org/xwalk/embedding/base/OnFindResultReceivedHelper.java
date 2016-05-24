package org.xwalk.embedding.base;

import org.chromium.content.browser.test.util.CallbackHelper;

public class OnFindResultReceivedHelper extends CallbackHelper {
    private int mIndex;
    private int mMatches;
    private boolean mIsDone;

    public int getIndex() {
        assert getCallCount() > 0;
        return mIndex;
    }

    public int getMatches() {
        assert getCallCount() > 0;
        return mMatches;
    }

    public boolean isDone() {
        assert getCallCount() > 0;
        return mIsDone;
    }

    public void notifyCalled(int index, int matches, boolean isDone) {
        mIndex = index;
        mMatches = matches;
        mIsDone = isDone;
        notifyCalled();
    }
}
