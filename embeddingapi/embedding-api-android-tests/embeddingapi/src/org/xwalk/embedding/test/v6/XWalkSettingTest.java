package org.xwalk.embedding.test.v6;

import android.test.suitebuilder.annotation.MediumTest;

import org.xwalk.core.XWalkSettings;
import org.xwalk.embedding.base.XWalkViewTestBase;

/**
 * Created by joey on 11/27/15.
 */
public class XWalkSettingTest extends XWalkViewTestBase {

    private static final String USER_AGENT =
            "Chrome/44.0.2403.81 Crosswalk/15.44.376.0 Mobile Safari/537.36";
    private static final String LANGUAGE = "jp";

    private static final int FIXED_FONT_SIZE = 20;

    private static final int FONT_SIZE = 50;

    private static final int TEXT_ZOOM = 150;

    @Override
    public void setUp() throws Exception {
        super.setUp();
    }


    @MediumTest
    public void testUserAgentString() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                XWalkSettings settings = getXWalkView().getSettings();
                String defaultUserAgentString = settings.getUserAgentString();

                // Check that an attempt to set the default UA string to null or "" has no effect.
                settings.setUserAgentString(null);
                assertEquals(defaultUserAgentString, settings.getUserAgentString());
                settings.setUserAgentString("");
                assertEquals(defaultUserAgentString, settings.getUserAgentString());

                // Set a custom UA string, verify that it can be reset back to default.
                settings.setUserAgentString(USER_AGENT);
                assertEquals(USER_AGENT, settings.getUserAgentString());
                settings.setUserAgentString(null);
                assertEquals(defaultUserAgentString, settings.getUserAgentString());
            }
        });
    }

    @MediumTest
    public void testAcceptLanguages() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                XWalkSettings settings = getXWalkView().getSettings();
                String defaultLanguages = settings.getAcceptLanguages();

                // Set a custom UA string, verify that it can be reset back to default.
                settings.setAcceptLanguages(LANGUAGE);
                assertEquals(LANGUAGE, settings.getAcceptLanguages());
                settings.setAcceptLanguages(defaultLanguages);
                assertEquals(defaultLanguages, settings.getAcceptLanguages());
            }
        });
    }

    @MediumTest
    public void testDefaultFixedFontSize() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                XWalkSettings settings = getXWalkView().getSettings();
                int defaultFixedFontSize = settings.getDefaultFixedFontSize();

                // Set a custom FixedFontSize, verify that it can be reset back to default.
                settings.setDefaultFixedFontSize(FIXED_FONT_SIZE);
                assertTrue(FIXED_FONT_SIZE == settings.getDefaultFixedFontSize());
                settings.setDefaultFixedFontSize(defaultFixedFontSize);
                assertTrue(defaultFixedFontSize == settings.getDefaultFixedFontSize());
            }
        });
    }

    @MediumTest
    public void testDefaultFontSize() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                XWalkSettings settings = getXWalkView().getSettings();
                int defaultFontSize = settings.getDefaultFontSize();

                // Set a custom FontSize, verify that it can be reset back to default.
                settings.setDefaultFontSize(FONT_SIZE);
                assertTrue(FONT_SIZE == settings.getDefaultFontSize());
                settings.setDefaultFontSize(defaultFontSize);
                assertTrue(defaultFontSize == settings.getDefaultFontSize());
            }
        });
    }

    @MediumTest
    public void testTextZoom() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                XWalkSettings settings = getXWalkView().getSettings();
                int defaultFontSize = settings.getTextZoom();

                // Set a custom Text Zoom, verify that it can be reset back to default.
                settings.setTextZoom(TEXT_ZOOM);
                assertTrue(TEXT_ZOOM == settings.getTextZoom());
                settings.setTextZoom(defaultFontSize);
                assertTrue(defaultFontSize == settings.getTextZoom());
            }
        });
    }

    @MediumTest
    public void testInitialPageScale() throws Throwable {
        getInstrumentation().runOnMainSync(new Runnable() {
            @Override
            public void run() {
                XWalkSettings settings = getXWalkView().getSettings();

                // Set a 80% initial Page scale , verify no error happen once try to change the initial scale again.
                try{
                    float percent = 0.5f;
                    for(int i = 0; i < 5; i++) {
                        settings.setInitialPageScale(percent);
                        percent = percent + 0.1f;
                    }
                }catch (Exception e){
                    assertTrue(false);
                }
            }
        });
    }

}
