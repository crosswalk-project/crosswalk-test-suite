package org.xwalk.embedded.api.sample;

import android.app.Activity;
import android.content.Context;
import android.content.res.AssetManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.util.Log;

import org.xwalk.core.XWalkView;

import java.io.IOException;

/**
 * Created by joey on 8/17/15.
 */
public class MyXWalkView extends XWalkView {

    public final static String TAG = "MyXWalkView";

    private ScrollOverListener mListener;

    public MyXWalkView(Context context) {
        super(context);
    }

    public MyXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public MyXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    public void dispatchDraw(Canvas canvas) {
        super.dispatchDraw(canvas);
        Log.i(TAG, "Overrided dispatchDraw");
        Paint mGridPaint = new Paint(Paint.LINEAR_TEXT_FLAG);

        AssetManager am = this.getContext().getAssets();

        try {
            Bitmap bm = BitmapFactory.decodeStream(am.open("ic_launcher.png"));
            canvas.drawBitmap(bm, 0, 0, mGridPaint);
        }catch (IOException e){
            Log.e(TAG, "the bitmap is not found!");
        }
    }

    @Override
    protected void onOverScrolled(int scrollX, int scrollY, boolean clampedX, boolean clampedY) {
        super.onOverScrolled(scrollX, scrollY, clampedX, clampedY);
        if(null != mListener){
            Log.i(TAG, "onOverScrolled is invoked. Parameter: scrollX=" + scrollX + "; scrollY=" + scrollY + "; clampedX=" + clampedX + "; clampedY=" + clampedY);
            mListener.onScrollOver("onOverScrolled is invoked. Parameter: scrollX=" + scrollX + "; scrollY=" + scrollY + "; clampedX=" + clampedX + "; clampedY=" + clampedY);
        }
    }

    public void setScrollOverListener(ScrollOverListener listener){
        this.mListener = listener;
    }

    public interface ScrollOverListener{

        public void onScrollOver(String msg);
    }
}
