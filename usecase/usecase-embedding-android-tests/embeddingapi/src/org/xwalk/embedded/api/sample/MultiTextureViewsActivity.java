package org.xwalk.embedded.api.sample;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkPreferences;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.RelativeLayout;

public class MultiTextureViewsActivity extends XWalkActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    private void resizeLoop(final RelativeLayout views) {
        views.postDelayed(new Runnable() {
            @Override
            public void run() {
                resize(views, 400, 400);
                views.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        resize(views, 200, 200);
                        resizeLoop(views);
                    }
                }, 2000);
            }
        }, 2000);
    }

    private void resize(RelativeLayout views, int width, int height) {
        for (int i = 0; i < views.getChildCount(); i++) {
            View child = views.getChildAt(i);
            child.setLayoutParams(new RelativeLayout.LayoutParams(width, height));
        }
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies Multiple TextureViews can be shown in order.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Rotate the device screen 90 degrees.\n")
        .append("2. Restore the device screen.\n\n")
        .append("Expected Result:\n\n")
        .append("1. Test passes if the sort order of A, B, C views are the same with the  sort order of D, E, F views which are correct and created by WebView at first.\n")
        .append("2. Test passes if the sort order of A, B, C views are the same with the  sort order of D, E, F views which are correct and created by WebView when rotating the device screen 90 degrees.\n")
        .append("3. Test passes if the sort order of A, B, C views are the same with the  sort order of D, E, F views which are correct and created by WebView when restoring the device screen.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        XWalkPreferences.setValue(XWalkPreferences.ANIMATABLE_XWALK_VIEW, true);

        RelativeLayout root = new RelativeLayout(this);

        for (int i = 0; i < 3; i++) {
            XWalkView xWalkView = new XWalkView(this, this);
            xWalkView.setX(i * 100);
            xWalkView.setY(i * 100);
            xWalkView.load(null, String.format("<html><head><meta name='viewport' content='width=device-width'/></head>"
                    + "<body style='background-color: %s;'><h1>%s</h1></body></html>", i % 2 == 0 ? "white" : "grey", i == 0 ? "A" : i == 1 ?  "B" : "C"));
            root.addView(xWalkView, 200, 200);
        }

        for (int i = 3; i < 6; i++) {
            WebView webView = new WebView(this);
            webView.setX(i * 100);
            webView.setY(i * 100);
            webView.loadData(String.format("<html><body style='background-color: %s'><h1>%s</h1></body></html>",
                    i % 2 == 0 ? "white" : "grey", i == 3 ? "D" : i == 4 ?  "E" : "F"), "text/html", "utf-8");
            root.addView(webView, 200, 200);
        }

        setContentView(root);
        resizeLoop(root);
    }
}
