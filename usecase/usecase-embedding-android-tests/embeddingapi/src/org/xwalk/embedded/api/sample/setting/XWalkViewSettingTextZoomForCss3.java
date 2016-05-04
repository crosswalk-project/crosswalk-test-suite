package org.xwalk.embedded.api.sample.setting;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.sample.R;

import android.content.Context;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.RelativeLayout;
import android.widget.Toast;

public class XWalkViewSettingTextZoomForCss3 extends XWalkActivity {

    private ViewGroup mContainerView;
    private View mWebView;
    private Button btn;

	@Override
	protected void onXWalkReady() {
		mWebView = new XWalkViewTest(this);
        mContainerView.addView(mWebView, RelativeLayout.LayoutParams.MATCH_PARENT,
                RelativeLayout.LayoutParams.MATCH_PARENT);
        loadView(R.id.action_swap_xwalkview);

        btn = (Button) findViewById(R.id.test);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int curZoom;
                int newZoom;
                if (mWebView instanceof XWalkView) {
                    curZoom = ((XWalkView) mWebView).getSettings().getTextZoom();
                } else {
                    curZoom = ((WebView) mWebView).getSettings().getTextZoom();
                }
                newZoom = curZoom == 100 ? 200 : 100;
                if (mWebView instanceof XWalkView) {
                    ((XWalkView) mWebView).getSettings().setTextZoom(newZoom);
                } else {
                    ((WebView) mWebView).getSettings().setTextZoom(newZoom);
                }
                btn.setText("Set TextZoom to " + String.valueOf(newZoom == 100 ? 200 : 100));
                Toast.makeText(XWalkViewSettingTextZoomForCss3.this, "Zoom set to " + newZoom + "%", Toast.LENGTH_LONG).show();
            }

        });
	}
    
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.zoom_css3columns_layout);
		mContainerView = (ViewGroup) findViewById(R.id.container);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        loadView(id);
        return super.onOptionsItemSelected(item);
    }

    private void loadView(int viewType) {
        mContainerView.removeAllViews();
        if (viewType == R.id.action_swap_xwalkview) {
            mWebView = new XWalkViewTest(this);
            setTitle("XWalkView");
        } else {
            mWebView = new WebViewTest(this);
            setTitle("WebView");
        }
        mContainerView.addView(mWebView, RelativeLayout.LayoutParams.MATCH_PARENT,
                RelativeLayout.LayoutParams.MATCH_PARENT);

    }

	public class WebViewTest extends WebView {

	    public WebViewTest(Context context) {
	        super(context);
	        loadUrl("file:///android_asset/text_zoom_css3.html");
	    }
	}

	public class XWalkViewTest extends XWalkView {

	    public XWalkViewTest(Context context) {
	        super(context);
	        load("file:///android_asset/text_zoom_css3.html", null);
	    }
	}
}
