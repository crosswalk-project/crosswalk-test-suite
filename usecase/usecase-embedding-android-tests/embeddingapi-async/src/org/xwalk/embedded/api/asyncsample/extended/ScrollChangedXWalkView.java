package org.xwalk.embedded.api.asyncsample.extended;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;

import org.xwalk.core.XWalkView;

/**
 * Created by joey on 8/26/15.
 */
public class ScrollChangedXWalkView extends XWalkView {

    public final static String TAG = "ScrollChangedXWalkView";

    public ScrollChangedXWalkView(Context context) {
        super(context);
    }

    public ScrollChangedXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public ScrollChangedXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    private ScrollChangedListener mListener;

    public interface ScrollChangedListener{
        public void informScrollChanged(String msg);
    }

    public void setScrollChangedListener(ScrollChangedListener listener){
        this.mListener = listener;
    }

    @Override
    protected void onScrollChanged(int l, int t, int oldl, int oldt) {
        Log.i(TAG, "onScrollChanged is invoked, l:" + l + ", t:" + t + ", oldl:" + oldl + ", oldt:" + oldt);
        if(null != mListener) {
            mListener.informScrollChanged("onScrollChanged is invoked, l:" + l + ", t:" + t + ", oldl:" + oldl + ", oldt:" + oldt);
        }
        super.onScrollChanged(l, t, oldl, oldt);
    }
}
