package org.xwalk.embedded.api.sample.extended;

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
 * Created by joey on 8/19/15.
 */
public class OnDrawXWalkView extends XWalkView {

    public static String TAG = "OnDrawXWalkView";

    public OnDrawXWalkView(Context context) {
        super(context);
        this.setWillNotDraw(false);
    }

    public OnDrawXWalkView(Context context, Activity activity) {
        super(context, activity);
        this.setWillNotDraw(false);
    }

    public OnDrawXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
        this.setWillNotDraw(false);
    }

    @Override
    public void onDraw(Canvas canvas){
        Paint mGridPaint = new Paint(Paint.LINEAR_TEXT_FLAG);

        AssetManager am = this.getContext().getAssets();

        try {
            Bitmap bm = BitmapFactory.decodeStream(am.open("ic_launcher.png"));
            Log.i(TAG, "Screen Width: " + getWidth() + ", Bitmap Width: " + bm.getWidth());
            Log.i(TAG, "Canvas Height: " + canvas.getHeight() + ", Bitmap Height: " + bm.getHeight());
            Bitmap background = Bitmap.createBitmap(canvas.getWidth(), canvas.getHeight() - bm.getHeight(), Bitmap.Config.ARGB_8888);
            canvas.drawBitmap(bm, getWidth() - bm.getWidth(), 0, mGridPaint);
        } catch (IOException e) {
            Log.e(TAG, "the bitmap is not found!");
        }
    }
}
