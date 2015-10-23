package org.xwalk.embedded.api.sample.extended;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.view.View;

import org.xwalk.core.XWalkView;

/**
 * Created by joey on 8/26/15.
 */
public class VisibilityChangedXWalkView extends XWalkView {

    public final static String TAG = "VisibilityChangedXWalkView";

    public VisibilityChangedXWalkView(Context context) {
        super(context);
    }

    public VisibilityChangedXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public VisibilityChangedXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    private VisibilityChangedListener mListener;

    public interface VisibilityChangedListener{
        public void informVisibilityChanged(String msg);
    }

    public void setSizeChangedListener(VisibilityChangedListener listener){
        this.mListener = listener;
    }

    @Override
    protected void onVisibilityChanged(View changedView, int visibility) {
        if(null != mListener){
            String vis_str = "UNKNOWN";
            switch (visibility){
                case View.INVISIBLE:
                    vis_str = "INVISIBLE";
                    break;
                case View.VISIBLE:
                    vis_str = "VISIBLE";
                    break;
                case View.GONE:
                    vis_str = "GONE";
                    break;
            }
            mListener.informVisibilityChanged("onVisibilityChanged is invoked. View: " + changedView.getClass() + "; Visibility:" + vis_str);
        }
        super.onVisibilityChanged(changedView, visibility);
    }
}
