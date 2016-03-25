package org.xwalk.embedding.base;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;

import org.xwalk.core.XWalkView;


public class ScrollXWalkView extends XWalkView {

    public final static String TAG = "ScrollXWalkView";

    public ScrollXWalkView(Context context) {
        super(context);
    }

    public ScrollXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public ScrollXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    private OnMeasureListener mOnMeasureListener;

    public interface OnMeasureListener{
        public void informOnMeasure(String msg);
    }

    public void setOnMeasureListener(OnMeasureListener listener){
        this.mOnMeasureListener = listener;
    }

    private OverScrollModeListener mOverScrollModeListener;

    public interface OverScrollModeListener{
        public void informOverScrollMode(String msg);
    }

    public void setOverScrollModeListener(OverScrollModeListener listener){
        this.mOverScrollModeListener = listener;
    }

    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        // TODO Auto-generated method stub
        Log.i(TAG, "onMeasure is invoked, widthMeasureSpec:" + widthMeasureSpec + " heightMeasureSpec:" + heightMeasureSpec);
        if(null != mOnMeasureListener) {
            mOnMeasureListener.informOnMeasure("onMeasure is invoked");
        }
        super.onMeasure(widthMeasureSpec, heightMeasureSpec);
    }

    @Override
    public void setOverScrollMode(int overScrollMode) {
        // TODO Auto-generated method stub
        Log.i(TAG, "setOverScrollMode is invoked, overScrollMode is " + overScrollMode);
        if(null != mOverScrollModeListener) {
            mOverScrollModeListener.informOverScrollMode("setOverScrollMode is invoked");
        }
        super.setOverScrollMode(overScrollMode);
    }

}

