package org.xwalk.embedded.api.sample.database;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkView;
import org.xwalk.core.XWalkViewDatabase;


import org.xwalk.embedded.api.sample.R;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class XWalkViewDatabaseWithClearFormData  extends XWalkActivity {

    private XWalkView mXWalkView;
    private TextView mMessage;
    private Button hasFormData;
    private Button clearFormData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_formdatabase_clearformdata);
        mMessage = (TextView) findViewById(R.id.message_tv);
        hasFormData = (Button) findViewById(R.id.hasformdata);
        hasFormData.setText("HasFormData");
        clearFormData = (Button) findViewById(R.id.clearformdata);
        clearFormData.setText("ClearFormData");
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Check if clearFormData() of XWalkViewDatabase can remove form data from XWalkView's store, and hasFormData() get whether there is any saved data.\n\n")
                .append("Test Steps:\n\n")
                .append("1. Input your name, and click submit button.\n\n")
                .append("2. Click hasFormData button.\n\n")
                .append("3. Click clearFormData button.\n\n")
                .append("4. Click hasFormData button.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the saved form date can be cleared.");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();


        hasFormData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkFormData();
            }
        });

        clearFormData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                XWalkViewDatabase.clearFormData();
                if(!checkFormData()) {
                    mMessage.setText("Form data success to clear");
                } else {
                    mMessage.setText("Form data fail to clear");
                }

            }
        });

        mXWalkView.load("file:///android_asset/form_database.html", null);

    }

    protected boolean checkFormData(){
        if (XWalkViewDatabase.hasFormData()) {
            mMessage.setText("There is saved form data.");
            return true;
        } else {
            mMessage.setText("There is no saved form data.");
            return false;
        }
    }

}
