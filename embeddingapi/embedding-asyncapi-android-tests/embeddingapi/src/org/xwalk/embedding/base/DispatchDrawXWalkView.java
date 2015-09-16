package org.xwalk.embedding.base;

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


public class DispatchDrawXWalkView extends XWalkView {

    public static String TAG = "DispatchDrawXWalkView";

    public DispatchDrawXWalkView(Context context) {
        super(context);
    }

    public DispatchDrawXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public DispatchDrawXWalkView(Context context, AttributeSet attrs) {
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
}