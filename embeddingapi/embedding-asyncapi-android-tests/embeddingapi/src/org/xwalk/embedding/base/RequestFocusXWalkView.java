package org.xwalk.embedding.base;

import android.app.Activity;
import android.content.Context;
import android.graphics.Rect;
import android.util.AttributeSet;
import android.util.Log;

import org.xwalk.core.XWalkView;


public class RequestFocusXWalkView extends XWalkView {

    public final static String TAG = "RequestFocusXWalkView";

    private FocusChangedListener mFocusChangedListener;

    public RequestFocusXWalkView(Context context) {
        super(context);
    }

    public RequestFocusXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public RequestFocusXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }


    public void setFocuseChangedListener(FocusChangedListener listener){
        this.mFocusChangedListener = listener;
    }

    public interface FocusChangedListener{

        public void informFocuseChanged(String msg);

    }

    @Override
    protected void onFocusChanged(boolean focused, int direction, Rect previouslyFocusedRect) {
        super.onFocusChanged(focused, direction, previouslyFocusedRect);
        Log.i(TAG, "onFocusChanged is invoked, focused:"
                + focused + "; direction:" + direction
                + ": previouslyFocusedRect: " + previouslyFocusedRect);
        if(null != mFocusChangedListener) {
            mFocusChangedListener.informFocuseChanged("onFocusChanged is invoked, focused:"
                    + focused + "; direction:" + direction
                    + ": previouslyFocusedRect: " + previouslyFocusedRect);
        }
    }
}

