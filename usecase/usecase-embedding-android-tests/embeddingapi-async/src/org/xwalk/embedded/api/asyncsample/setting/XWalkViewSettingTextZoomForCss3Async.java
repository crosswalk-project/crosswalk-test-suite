package org.xwalk.embedded.api.asyncsample.setting;

import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkView;
import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

public class XWalkViewSettingTextZoomForCss3Async extends Activity implements XWalkInitializer.XWalkInitListener {

    private XWalkInitializer mXWalkInitializer;
    private ViewGroup mContainerView;
    private View mWebView;
    private TextView mMessage;
    private Button btn;
    public final static String MESSAGE_TITLE = "TextSize Percent: ";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
        
		setContentView(R.layout.zoom_css3columns_layout);
		mContainerView = (ViewGroup) findViewById(R.id.container);
        mMessage = (TextView) findViewById(R.id.message_tv);
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
            mMessage.setText(MESSAGE_TITLE + ((XWalkView) mWebView).getSettings().getTextZoom());
        } else {
            mWebView = new WebViewTest(this);
            setTitle("WebView");
            mMessage.setText(MESSAGE_TITLE + ((WebView) mWebView).getSettings().getTextZoom());
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

	@Override
	public void onXWalkInitCancelled() {
		
	}

	@Override
	public void onXWalkInitCompleted() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if XWalkView can set the text zoom for css3 like Webview.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes, if you click 'Set TextZoom to 200', text will be zoomed bigger, click the " +
                		"menu key to switch to 'Load WebView', the behavior should be the same with 'Load XWalkView'");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();

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
                    mMessage.setText(MESSAGE_TITLE + ((XWalkView) mWebView).getSettings().getTextZoom());
                } else {
                    ((WebView) mWebView).getSettings().setTextZoom(newZoom);
                    mMessage.setText(MESSAGE_TITLE + ((WebView) mWebView).getSettings().getTextZoom());
                }
                btn.setText("Set TextZoom to " + String.valueOf(newZoom == 100 ? 200 : 100));
                Toast.makeText(XWalkViewSettingTextZoomForCss3Async.this, "Zoom set to " + newZoom + "%", Toast.LENGTH_LONG).show();
            }

        });
	}

	@Override
	public void onXWalkInitFailed() {
		
	}

	@Override
	public void onXWalkInitStarted() {
		
	}
}
