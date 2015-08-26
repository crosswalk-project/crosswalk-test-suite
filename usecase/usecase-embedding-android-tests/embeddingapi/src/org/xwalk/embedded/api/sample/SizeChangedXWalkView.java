package org.xwalk.embedded.api.sample;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;

import org.xwalk.core.XWalkView;

/**
 * Created by joey on 8/26/15.
 */
public class SizeChangedXWalkView extends XWalkView {

    public final static String TAG = "SizeChangedXWalkView";

    public SizeChangedXWalkView(Context context) {
        super(context);
    }

    public SizeChangedXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public SizeChangedXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    private SizeChangedListener mListener;

    public interface SizeChangedListener{
        public void informSizeChanged(String msg);
    }

    public void setSizeChangedListener(SizeChangedListener listener){
        this.mListener = listener;
    }

    @Override
    protected void onSizeChanged(int w, int h, int oldw, int oldh) {
        Log.i(TAG, "============================onSizeChanged is invoked, w:" + w + ", h:" + h + ", oldw:" + oldw + ", oldh:" + oldh);
        if(null != mListener) {
            mListener.informSizeChanged("onSizeChanged is invoked, w:" + w + ", h:" + h + ", oldw:" + oldw + ", oldh:" + oldh);
        }
        super.onSizeChanged(w, h, oldw, oldh);
    }
}
