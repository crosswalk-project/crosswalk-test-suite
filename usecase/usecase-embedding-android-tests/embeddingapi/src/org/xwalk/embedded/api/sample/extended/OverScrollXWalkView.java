package org.xwalk.embedded.api.sample.extended;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;

import org.xwalk.core.XWalkView;

/**
 * Created by joey on 8/25/15.
 */
public class OverScrollXWalkView extends XWalkView {

    public final static String TAG = "OverScrollXWalkView";

    public OverScrollXWalkView(Context context) {
        super(context);
    }

    public OverScrollXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public OverScrollXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    protected boolean overScrollBy(int deltaX, int deltaY, int scrollX, int scrollY, int scrollRangeX, int scrollRangeY, int maxOverScrollX, int maxOverScrollY, boolean isTouchEvent) {
        if (null != mListener) {
            mListener.onScrollOver("overScrollBy is invoked. Parameter: scrollX=" +
                    scrollX + "; scrollY=" + scrollY + "; deltaX=" + deltaX + "; deltaY=" + deltaY
                    + "; scrollRangeX=" + scrollRangeX + "; scrollRangeY=" + scrollRangeY
                    + "; maxOverScrollX=" + maxOverScrollX + "; maxOverScrollY=" + maxOverScrollY + "; isTouchEvent=" + isTouchEvent);
        }
        Log.i(TAG, "overScrollBy is invoked. Parameter: scrollX=" +
                scrollX + "; scrollY=" + scrollY + "; deltaX=" + deltaX + "; deltaY=" + deltaY
                + "; scrollRangeX=" + scrollRangeX + "; scrollRangeY=" + scrollRangeY
                + "; maxOverScrollX=" + maxOverScrollX + "; maxOverScrollY=" + maxOverScrollY + "; isTouchEvent=" + isTouchEvent);
        return super.overScrollBy(deltaX, deltaY, scrollX, scrollY, scrollRangeX, scrollRangeY, maxOverScrollX, maxOverScrollY, isTouchEvent);
    }

    private ScrollOverListener mListener;

    public interface ScrollOverListener{
        public void onScrollOver(String msg);
    }

    public void setScrollOverListener(ScrollOverListener listener){
        this.mListener = listener;
    }
}
