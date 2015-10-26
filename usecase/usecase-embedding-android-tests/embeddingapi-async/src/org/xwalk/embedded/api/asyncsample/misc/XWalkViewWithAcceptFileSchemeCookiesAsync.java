// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.asyncsample.misc;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkCookieManager;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

public class XWalkViewWithAcceptFileSchemeCookiesAsync extends Activity implements XWalkInitializer.XWalkInitListener {
	private static final String TAG = XWalkViewWithAcceptFileSchemeCookiesAsync.class.getSimpleName();
    private String url;
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;
    private XWalkCookieManager mCookieManager;
    private Button getCookie;
    private Button setAcceptFileSchemeCookiesTrue;
    private Button setAcceptFileSchemeCookiesFalse;
    private TextView CookieString;
    private String allCookies;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mXWalkInitializer = new XWalkInitializer(this, this);
        mXWalkInitializer.initAsync();
    }

    @Override
    public final void onXWalkInitStarted() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitCancelled() {
        // It's okay to do nothing
    }

    @Override
    public final void onXWalkInitFailed() {
        // Do crash or logging or anything else in order to let the tester know if this method get called
    }

    @Override
    public final void onXWalkInitCompleted() {
        setContentView(R.layout.cookiemanager_layout);
        LinearLayout layout = (LinearLayout)findViewById(R.id.set_cookie);
        layout.setVisibility(View.GONE);
        getCookie = (Button)findViewById(R.id.remove_session_cookie);
        setAcceptFileSchemeCookiesTrue = (Button)findViewById(R.id.remove_expired_cookie);
        setAcceptFileSchemeCookiesFalse = (Button)findViewById(R.id.remove_all_cookie);
        getCookie.setText("getCookie");
        setAcceptFileSchemeCookiesTrue.setText("setAcceptFileSchemeCookies True");
        setAcceptFileSchemeCookiesFalse.setText("setAcceptFileSchemeCookies False");
        CookieString = (TextView)findViewById(R.id.getcookie);

        mCookieManager = new XWalkCookieManager();
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkCookieManager can set AcceptFileSchemeCookies.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click getCookie button then no cookies show.\n")
        .append("2. Click setAcceptFileSchemeCookiesTrue button.\n")
        .append("3. Click getCookie button then cookie 'test123' shows.\n")
        .append("4. Click setAcceptFileSchemeCookiesFalse button.\n")
        .append("5. Click getCookie button then no cookies show\n");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mCookieManager.setAcceptCookie(true);
        Log.d(TAG, "mCookieManager.acceptCookie()="+mCookieManager.acceptCookie());
        mCookieManager.removeAllCookie();
        mCookieManager.flushCookieStore();
        Log.d(TAG, "mCookieManager.hasCookies()="+mCookieManager.hasCookies());

        String value = "test123";
        url = "file:///android_asset/cookie_test.html?value=" + value;

        getCookie.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
		        mXWalkView.load(url, null);
				allCookies = mCookieManager.getCookie(url);
				CookieString.setText(allCookies);
				Log.d(TAG, "mCookieManager allowFileSchemeCookies="+mCookieManager.allowFileSchemeCookies());
			}
		});

        setAcceptFileSchemeCookiesTrue.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
		        mCookieManager.setAcceptFileSchemeCookies(true);
			}
		});

        setAcceptFileSchemeCookiesFalse.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
		        mCookieManager.setAcceptFileSchemeCookies(false);
			}
		});
    }
}
