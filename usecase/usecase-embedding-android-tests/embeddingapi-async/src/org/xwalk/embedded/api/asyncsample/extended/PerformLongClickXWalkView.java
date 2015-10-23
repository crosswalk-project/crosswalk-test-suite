package org.xwalk.embedded.api.asyncsample.extended;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;

/**
 * Created by joey on 9/9/15.
 */
public class PerformLongClickXWalkView extends MessageInfoXWalkView {

    public final static String TAG = "LongClickXWalkView";

    public PerformLongClickXWalkView(Context context) {
        super(context);
    }

    public PerformLongClickXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public PerformLongClickXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    public boolean performLongClick() {
        Log.i(TAG, "performLongClick is invoked");
        getMessageListener().onMessageSent("performLongClick is invoked. Class: " + this.getClass());
        return super.performLongClick();
    }
}
