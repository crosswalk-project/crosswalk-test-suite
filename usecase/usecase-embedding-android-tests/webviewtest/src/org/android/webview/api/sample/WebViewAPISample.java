// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.android.webview.api.sample;

import java.util.ArrayList;
import java.util.List;

import android.app.ListActivity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.MenuItem;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ListView;
import android.widget.TextView;

public class WebViewAPISample extends ListActivity {

    public final static String TAG = "WebViewAPISample";

    public final static String LEVEL_BOUND = "LEVEL_BOUND";

    public final static String ORDER_BOUND = "ORDER_BOUND";

    private static int level = 0;

    private String title;

    private static int order = 0;

    private String[][] TITLES = {{"Usecase WebViewAPI"}, {"WebView", "WebView-Extended", "WebChromeClient & WebViewClient", "Misc"}};

    private String[] CATEGORIES = {"WebView.Basic", "WebView.Extended", "WebView.WebChromeClient.WebViewClient", "WebView.Misc"};

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Bundle bundle = this.getIntent().getExtras();
        if(null != bundle) {
            int tmp_level = bundle.getInt(LEVEL_BOUND);
            if (tmp_level >= 0) {
                level = tmp_level;
            }
            int tmp_order = bundle.getInt(ORDER_BOUND);
            if (tmp_order >= 0) {
                order = tmp_order;
            }
        }
        if (level == 1) {
            getActionBar().setDisplayHomeAsUpEnabled(true);
        } else {
            getActionBar().setDisplayHomeAsUpEnabled(false);
        }
        this.setTitle(TITLES[level][order]);
        setListAdapter(new SampleAdapter(level, order));
    }

    @Override
    public void onPause() {
        super.onPause();
    }

    @Override
    public void onResume() {
        super.onResume();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }

    @Override
    protected void onListItemClick(ListView lv, View v, int pos, long id) {
        SampleInfo info = (SampleInfo) getListAdapter().getItem(pos);
        startActivity(info.intent);
    }

    static class SampleInfo {
        String name;
        Intent intent;

        SampleInfo(String name, Intent intent) {
            this.name = name;
            this.intent = intent;
        }
    }

    class SampleAdapter extends BaseAdapter {
        private ArrayList<SampleInfo> mItems;

        private void addItems(ResolveInfo info, PackageManager pm){
            final CharSequence labelSeq = info.loadLabel(pm);
            String label = labelSeq != null ? labelSeq.toString() : info.activityInfo.name;

            Intent target = new Intent();
            target.setClassName(info.activityInfo.applicationInfo.packageName,
                    info.activityInfo.name);
            SampleInfo sample = new SampleInfo(label, target);
            mItems.add(sample);
        }

        public SampleAdapter(int level, int order){
            mItems = new ArrayList<SampleInfo>();
            if(level == 0){
                for(int i = 0; i < TITLES[1].length; i++) {
                    Intent target = new Intent();
                    target.setClassName("org.android.webview.api.sample",
                            "org.android.webview.api.sample.WebViewAPISample");
                    Bundle bundle = new Bundle();
                    bundle.putInt(LEVEL_BOUND, 1);
                    bundle.putInt(ORDER_BOUND, i);

                    target.putExtras(bundle);
                    SampleInfo sample = new SampleInfo(TITLES[1][i], target);
                    mItems.add(sample);
                }
            }else{
                Intent intent = new Intent(Intent.ACTION_MAIN, null);
                intent.setPackage(getPackageName());
                intent.addCategory(CATEGORIES[order]);

                Log.i(TAG, "___________________Create new Adapter__________");

                PackageManager pm = getPackageManager();
                List<ResolveInfo> infos = pm.queryIntentActivities(intent, 0);
                for (int i = 0; i < infos.size(); i++) {
                    final ResolveInfo info = infos.get(i);
                    addItems(info, pm);
                }
            }
        }

        @Override
        public int getCount() {
            return mItems.size();
        }

        @Override
        public Object getItem(int position) {
            return mItems.get(position);
        }

        @Override
        public long getItemId(int position) {
            return position;
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            if (convertView == null) {
                convertView = getLayoutInflater().inflate(android.R.layout.simple_list_item_1,
                        parent, false);
                convertView.setTag(convertView.findViewById(android.R.id.text1));
            }
            TextView tv = (TextView) convertView.getTag();
            SampleInfo info = mItems.get(position);
            tv.setText(info.name);
            return convertView;
        }
    }

    @Override
    public void onBackPressed() {
        // TODO Auto-generated method stub
        level = 0;
        order = 0;
        super.onBackPressed();
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // TODO Auto-generated method stub
        switch (item.getItemId()) {
        case android.R.id.home:
            Intent target = new Intent();
            target.setClassName("org.android.webview.api.sample",
                            "org.android.webview.api.sample.WebViewAPISample");
            Bundle bundle = new Bundle();
            bundle.putInt(LEVEL_BOUND, 0);
            bundle.putInt(ORDER_BOUND, 0);
            target.putExtras(bundle);
            startActivity(target);
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
