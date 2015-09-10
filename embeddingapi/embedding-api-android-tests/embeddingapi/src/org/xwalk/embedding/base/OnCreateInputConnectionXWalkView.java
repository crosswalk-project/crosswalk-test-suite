package org.xwalk.embedding.base;

import android.app.Activity;
import android.content.Context;

import android.view.inputmethod.EditorInfo;
import android.view.inputmethod.InputConnection;
import android.view.inputmethod.InputConnectionWrapper;

import org.xwalk.core.XWalkView;


public class OnCreateInputConnectionXWalkView extends XWalkView {

   public OnCreateInputConnectionXWalkView(Context context, Activity activity) {
        super(context, activity);
            // TODO Auto-generated constructor stub
    }

    @Override
    public InputConnection onCreateInputConnection(EditorInfo ei) {
        // TODO Auto-generated method stub
        InputConnection inputConnection = super.onCreateInputConnection(ei);
        if (inputConnection != null) {
            return new LimitInputConnection(inputConnection, false);
        }
        return null;
    }

    
    private class LimitInputConnection extends InputConnectionWrapper {
    
        public LimitInputConnection(InputConnection target, boolean mutable) {
            super(target, mutable);
            // TODO Auto-generated constructor stub
        }

        @Override
        public boolean commitText(CharSequence text, int newCursorPosition) {
            // TODO Auto-generated method stub
            return super.commitText("HAHA", 1);
        }
    }
}

