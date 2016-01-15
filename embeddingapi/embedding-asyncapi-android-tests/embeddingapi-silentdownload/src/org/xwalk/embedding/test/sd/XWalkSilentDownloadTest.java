package org.xwalk.embedding.test.sd;

import org.xwalk.embedding.base.OnXWalkInitFailedHelper;
import org.xwalk.embedding.base.OnXWalkUpdateProgressHelper;
import org.xwalk.embedding.base.OnXWalkUpdateStartedHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.test.suitebuilder.annotation.SmallTest;

public class XWalkSilentDownloadTest extends XWalkViewTestBase {

    @SmallTest
    public void testXWalkSilentDownload() {
        OnXWalkInitFailedHelper mOnXWalkInitFailedHelper = mTestHelperBridge.getOnXWalkInitFailedHelper();
        OnXWalkUpdateStartedHelper mOnXWalkUpdateStartedHelper = mTestHelperBridge.getOnXWalkUpdateStartedHelper();
        OnXWalkUpdateProgressHelper mOnXWalkUpdateProgressHelper = mTestHelperBridge.getOnXWalkUpdateProgressHelper();
        try {
            assertEquals(1, mOnXWalkInitFailedHelper.getCallCount());
            assertEquals("initFailed", mOnXWalkInitFailedHelper.getMessage());
            assertEquals(1, mOnXWalkUpdateStartedHelper.getCallCount());
            assertEquals("updateStarted", mOnXWalkUpdateStartedHelper.getMessage());
            Thread.sleep(10000);
            int progress = mOnXWalkUpdateProgressHelper.getProgress();
            assertTrue(progress >= 1);
            assertEquals("updateProgress", mOnXWalkUpdateProgressHelper.getMessage());
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            assertFalse(true);
        }
    }
}
