package org.xwalk.embedding.base;

import org.xwalk.embedding.MainActivity;

import android.test.ActivityInstrumentationTestCase2;


public class XWalkViewTestBase extends ActivityInstrumentationTestCase2<MainActivity> {
    
    protected MainActivity mainActivity;
    protected TestHelperBridge mTestHelperBridge;    

    public XWalkViewTestBase() {
        super(MainActivity.class);
        // TODO Auto-generated constructor stub
    }

    @Override
    protected void setUp() throws Exception {
        // TODO Auto-generated method stub
        super.setUp();
        mainActivity = (MainActivity) getActivity();
        mTestHelperBridge = mainActivity.getTestHelperBridge();
    }

    @Override
    protected void tearDown() throws Exception {
        // TODO Auto-generated method stub
        if(mainActivity != null)
        {
            mainActivity.finish();
        }        
        super.tearDown();
    }

}
