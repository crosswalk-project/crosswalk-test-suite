package org.xwalk.embedded.api.sample;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;
import android.view.View;

/**
 * Created by joey on 9/1/15.
 */
public class WindowsVisibilityChangedXWalkView extends MessageInfoXWalkView {

    public final static String TAG = "WinVisiChangedXWalkView";

    public WindowsVisibilityChangedXWalkView(Context context) {
        super(context);
    }

    public WindowsVisibilityChangedXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public WindowsVisibilityChangedXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    protected void onWindowVisibilityChanged(int visibility) {
        super.onWindowVisibilityChanged(visibility);
        Log.i(TAG, "============================onWindowVisibilityChanged is invoked, visibility:" + visibility);
        if(null != this.getMessageListener()) {
            String visText = null;
            switch (visibility){
                case View.VISIBLE:
                    visText = "VISIBLE";
                    break;
                case View.INVISIBLE:
                    visText = "INVISIBLE";
                    break;
                case View.GONE:
                    visText = "GONE";
                    break;
            }
            this.getMessageListener().onMessageSent(visText);
        }
    }
}
