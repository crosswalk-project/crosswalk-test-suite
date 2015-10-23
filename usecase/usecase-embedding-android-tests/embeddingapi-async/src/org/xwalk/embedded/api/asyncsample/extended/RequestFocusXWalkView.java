package org.xwalk.embedded.api.asyncsample.extended;

import android.app.Activity;
import android.content.Context;
import android.graphics.Rect;
import android.util.AttributeSet;
import android.util.Log;

/**
 * Created by joey on 9/9/15.
 */
public class RequestFocusXWalkView extends MessageInfoXWalkView {

    public final static String TAG = "ReqFocusXWalkView";

    public RequestFocusXWalkView(Context context) {
        super(context);
    }

    public RequestFocusXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public RequestFocusXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    public boolean requestFocus(int direction, Rect previouslyFocusedRect) {
        Log.i(TAG, "============================requestFocus is invoked");
        boolean changed = super.requestFocus(direction, previouslyFocusedRect);
        Log.i(TAG, "============================changed: " + changed);
        getMessageListener().onMessageSent("RequestFocusXWalkView");
        return changed;
    }
}
