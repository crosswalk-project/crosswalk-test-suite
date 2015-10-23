// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedded.api.sample.misc;

import org.xwalk.embedded.api.sample.R;

import java.util.Date;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkCookieManager;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class XWalkViewWithCookieManagerTest extends XWalkActivity {
    private static final String TAG = XWalkViewWithCookieManagerTest.class.getSimpleName();
    final String url = "http://www.baidu.com";
    final String cookie1 = "cookie1=peter";
    final String cookie2 = "cookie2=sue";
    final String cookie3 = "cookie3=marc";
    final String cookieTitle = "All cookies list as below: \n\n";
    private Integer cookie_count = 1;

    private XWalkView mXWalkView;
    private XWalkCookieManager mCookieManager;
    private EditText cookieName;
    private EditText cookieExpiredTime;
    private Button addCookie;
    private Button removeSessionCookie;
    private Button removeExpiredCookie;
    private Button removeAllCookie;
    private TextView getCookieString;
    private String allCookies;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.cookiemanager_layout);
        addCookie = (Button)findViewById(R.id.add_cookie);
        cookieName = (EditText)findViewById(R.id.cookie_name);
        cookieExpiredTime = (EditText)findViewById(R.id.cookie_time);
        removeSessionCookie = (Button)findViewById(R.id.remove_session_cookie);
        removeExpiredCookie = (Button)findViewById(R.id.remove_expired_cookie);
        removeAllCookie = (Button)findViewById(R.id.remove_all_cookie);
        getCookieString = (TextView)findViewById(R.id.getcookie);

        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mCookieManager = new XWalkCookieManager();
    }

    @Override
    protected void onXWalkReady() {

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkCookieManager apis can work.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Load page and show there are three cookies.\n")
        .append("2. Click removeSessionCookie button then cookie1 is disappeared.\n")
        .append("3. Wait 10 seconds and click removeExpiredCookie button then cookie2 is disappeared.\n")
        .append("4. Click removeAllCookie button then all cookies are disappeared.\n\n")
        .append("Notice:\n\n")
        .append("You can also set your own cookie and expired time.\n");
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

        SetXWalkCookie();
        allCookies = mCookieManager.getCookie(url);
        getCookieString.setText(cookieTitle+allCookies.replaceAll("; ", "\n"));

        addCookie.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                String cookie_name = cookieName.getText().toString().trim();
                if (cookie_name.length() > 0) {
                    cookie_name = "cookie_set"+cookie_count+"="+cookie_name;
                    String expiration = cookieExpiredTime.getText().toString().trim();
                    if (expiration.length() > 0) {
                        Date date = new Date();
                        date.setTime(date.getTime() + Integer.parseInt(expiration)*1000);
                        String value = cookie_name + "; expires=" + date.toGMTString();
                        // Expires in 3s.
                        mCookieManager.setCookie(url, value);
                    } else {
                        mCookieManager.setCookie(url, cookie_name);
                    }
                    allCookies = mCookieManager.getCookie(url);
                    getCookieString.setText(allCookies!=null ? cookieTitle+allCookies.replaceAll("; ", "\n") : allCookies);
                    cookie_count ++;
                }else {
                    Toast.makeText(getApplicationContext(), "please input cookie name!", Toast.LENGTH_SHORT).show();
                }
            }
        });

        removeSessionCookie.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mCookieManager.removeSessionCookie();
                allCookies = mCookieManager.getCookie(url);
                getCookieString.setText(allCookies!=null ? cookieTitle+allCookies.replaceAll("; ", "\n") : allCookies);
            }
        });

        removeExpiredCookie.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                 mCookieManager.removeExpiredCookie();
                 allCookies = mCookieManager.getCookie(url);
                 getCookieString.setText(allCookies!=null ? cookieTitle+allCookies.replaceAll("; ", "\n") : allCookies);
            }
        });

        removeAllCookie.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mCookieManager.removeAllCookie();
                allCookies = mCookieManager.getCookie(url);
                getCookieString.setText(allCookies);
            }
        });

        mXWalkView.load(url, null);
    }

    private void SetXWalkCookie() {
        // Session cookie.
        mCookieManager.setCookie(url, cookie1);

        long expiration = 10000;
        Date date = new Date();
        date.setTime(date.getTime() + expiration);
        String value2 = cookie2 + "; expires=" + date.toGMTString();
        // Expires in 10s.
        mCookieManager.setCookie(url, value2);

        date = new Date();
        date.setTime(date.getTime() + 1000 * 600);
        String value3 = cookie3 + "; expires=" + date.toGMTString();
        // Expires in 10min.
        mCookieManager.setCookie(url, value3);
    }
}
