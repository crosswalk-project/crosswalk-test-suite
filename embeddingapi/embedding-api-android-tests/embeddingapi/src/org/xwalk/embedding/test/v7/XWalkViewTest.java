// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v7;


import org.xwalk.embedding.base.OnFindResultReceivedHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkViewTest extends XWalkViewTestBase {

    @Override
    public void setUp() throws Exception {
        super.setUp();
        setFindListener();
    }

    @SmallTest
    public void testFindAllAsync() {
        try {
            String fileContent = getFileContent("find.html");
			loadDataSync(null, fileContent, "text/html", false);
			OnFindResultReceivedHelper mOnFindResultReceivedHelper = mTestHelperBridge.getOnFindResultReceivedHelper();
	        findAllSync(mOnFindResultReceivedHelper, FIND_ALL, "Find");
	        assertEquals(0, mOnFindResultReceivedHelper.getIndex());
	        assertEquals(3, mOnFindResultReceivedHelper.getMatches());
	        assertTrue(mOnFindResultReceivedHelper.isDone());
		} catch (Exception e) {
			assertFalse(true);
			e.printStackTrace();
		}
    }

    @SmallTest
    public void testFindNext() {
        try {
            String fileContent = getFileContent("find.html");
            loadDataSync(null, fileContent, "text/html", false);
        	OnFindResultReceivedHelper mOnFindResultReceivedHelper = mTestHelperBridge.getOnFindResultReceivedHelper();
        	findAllSync(mOnFindResultReceivedHelper, FIND_ALL, "Find");
        	findNextSync(mOnFindResultReceivedHelper, FIND, true);
            assertEquals(1, mOnFindResultReceivedHelper.getIndex());
            assertEquals(3, mOnFindResultReceivedHelper.getMatches());
            assertTrue(mOnFindResultReceivedHelper.isDone());
		} catch (Exception e) {
			assertFalse(true);
			e.printStackTrace();
		}
    }

    @SmallTest
    public void testFindPrevious() {
        try {
            String fileContent = getFileContent("find.html");
            loadDataSync(null, fileContent, "text/html", false);
        	OnFindResultReceivedHelper mOnFindResultReceivedHelper = mTestHelperBridge.getOnFindResultReceivedHelper();
        	findAllSync(mOnFindResultReceivedHelper, FIND_ALL, "Find");
        	findNextSync(mOnFindResultReceivedHelper, FIND, false);
        	findNextSync(mOnFindResultReceivedHelper, FIND, false);
            assertEquals(1, mOnFindResultReceivedHelper.getIndex());
            assertEquals(3, mOnFindResultReceivedHelper.getMatches());
            assertTrue(mOnFindResultReceivedHelper.isDone());
		} catch (Exception e) {
			assertFalse(true);
			e.printStackTrace();
		}
    }
}
