package org.xwalk.embedded.api.sample.extended;

import android.app.Activity;
import android.content.Context;
import android.util.AttributeSet;

import org.xwalk.core.XWalkView;

/**
 * Created by joey on 9/1/15.
 */
public class MessageInfoXWalkView extends XWalkView {
    public MessageInfoXWalkView(Context context) {
        super(context);
    }

    public MessageInfoXWalkView(Context context, Activity activity) {
        super(context, activity);
    }

    public MessageInfoXWalkView(Context context, AttributeSet attrs) {
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
}
