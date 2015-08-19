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

    public static String TAG = "MyXWalkView";

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
}
