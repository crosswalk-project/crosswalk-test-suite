package org.xwalk.embedding.base;

import org.xwalk.core.XWalkView;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;
import android.view.View;


public class WindowsVisibilityChangedXWalkView extends XWalkView {

    public final static String TAG = "WinVisiChangedXWalkView";

    public WindowsVisibilityChangedXWalkView(Context context) {
        super(context);
    }

    public WindowsVisibilityChangedXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public WindowsVisibilityChangedXWalkView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    private MessageListener mListener;

    public interface MessageListener{
        public void onMessageSent(String msg);
    }

    public void setMessageListener(MessageListener listener){
        this.mListener = listener;
    }

    public MessageListener getMessageListener(){
        return this.mListener;
    }

    @Override
    protected void onWindowVisibilityChanged(int visibility) {
        super.onWindowVisibilityChanged(visibility);
        Log.i(TAG, "============================onWindowVisibilityChanged is invoked, visibility:" + visibility);
        if(null != this.getMessageListener()) {
            String visText = null;
            switch (visibility){
                case View.VISIBLE:
                    visText = "VISIBLE";
                    break;
                case View.INVISIBLE:
                    visText = "INVISIBLE";
                    break;
                case View.GONE:
                    visText = "GONE";
                    break;
            }
            this.getMessageListener().onMessageSent(visText);
        }
    }
}
