package org.xwalk.embedding.asynctest.v7;

import android.test.suitebuilder.annotation.SmallTest;
import org.xwalk.embedding.base.XWalkViewTestBase;

public class XWalkSettingTestAsync extends XWalkViewTestBase {

    @Override
    public void setUp() throws Exception {
        super.setUp();
    }


    @SmallTest
    public void testLoadWithOverviewModeWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView0(), views.getBridge0(), false),
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView1(), views.getBridge1(), false));

        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }

    @SmallTest
    public void testLoadWithOverviewModeViewportTagWithTwoViews() {
        try {
            ViewPair views = createViews();
            runPerViewSettingsTest(
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView0(), views.getBridge0(), true),
                    new XWalkSettingsLoadWithOverviewModeTestHelper(
                            views.getView1(), views.getBridge1(), true));
        } catch (Exception e) {
            assertTrue(false);
            e.printStackTrace();
        } catch (Throwable e) {
            assertTrue(false);
            e.printStackTrace();
        }
    }
}
