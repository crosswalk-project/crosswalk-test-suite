package org.xwalk.embedded.api.sample.extended;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;

/**
 * Created by joey on 9/1/15.
 */
public class WindowFocusChangedXwalkView extends MessageInfoXWalkView {

    public final static String TAG = "WindowFocusXwalkView";

    public WindowFocusChangedXwalkView(Context context) {
        super(context);
    }

    public WindowFocusChangedXwalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public WindowFocusChangedXwalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    public void onWindowFocusChanged(boolean hasWindowFocus) {
        super.onWindowFocusChanged(hasWindowFocus);
        Log.i(TAG, "============================onWindowFocusChanged is invoked, hasWindowFocus:" + hasWindowFocus);
        if(null != this.getMessageListener()) {
            this.getMessageListener().onMessageSent("onWindowFocusChanged is invoked, hasWindowFocus:" + hasWindowFocus);
        }
    }
}
