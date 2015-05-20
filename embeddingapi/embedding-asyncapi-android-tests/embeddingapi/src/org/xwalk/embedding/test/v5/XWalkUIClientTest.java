// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;

import org.xwalk.embedding.base.OnConsoleMessageHelper;
import org.xwalk.embedding.base.XWalkViewTestBase;

import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkUIClientTest extends XWalkViewTestBase {

    @SmallTest
    public void testOnConsoleMessageDebug() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doDebug();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("debug", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageError() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doError();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("error", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageInfo() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doInfo();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("info", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageLog() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doLog();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("log", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageWarn() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doWarn();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("warn", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageDir() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doDir();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("dir", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageDirxml() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doDirxml();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("dirxml", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageTable() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doTable();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("table", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageClear() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doClear();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("clear", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageTrace() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doTrace();");
            mOnConsoleMessageHelper.waitForCallback(count);
            assertEquals(1, mOnConsoleMessageHelper.getCallCount());
            assertEquals("trace", mOnConsoleMessageHelper.getMessage());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testOnConsoleMessageAll() {
        try {
            String fileContent = getFileContent("console_message.html");
            OnConsoleMessageHelper mOnConsoleMessageHelper = mTestHelperBridge.getOnConsoleMessageHelper();
            int count = mOnConsoleMessageHelper.getCallCount();
            loadDataSync(null, fileContent, "text/html", false);
            executeJavaScriptAndWaitForResult("doAll();");
            mOnConsoleMessageHelper.waitForCallback(count,NUM_OF_CONSOLE_CALL);
            assertEquals(NUM_OF_CONSOLE_CALL, mOnConsoleMessageHelper.getCallCount());
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
