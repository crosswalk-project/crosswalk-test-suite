package org.xwalk.embedded.api.sample;

import android.app.AlertDialog;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;

import org.xwalk.core.XWalkActivity;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class XWalkViewWithConsoleLog extends XWalkActivity {

    private XWalkView mXWalkView;

    private EditText et;

    private final static SimpleDateFormat FORMAT = new SimpleDateFormat("MM-dd hh:mm:ss.SSS");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xwalk_view_with_console_log);
    }

    @Override
    protected void onXWalkReady() {
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
                .append("Verifies onConsoleMessage work in XWalkView.\n\n")
                .append("Expected Result:\n\n")
                .append("Test passes if the console message \n\n" +
                        "printed by Javascript will be shown by clicking HTML form button");
        new  AlertDialog.Builder(this)
                .setTitle("Info")
                .setMessage(mess.toString())
                .setPositiveButton("confirm", null)
                .show();
        mXWalkView = (XWalkView) findViewById(R.id.console_xwalk_view);
        mXWalkView.load("file:///android_asset/jsconsole_demo.html", null);
        mXWalkView.setUIClient(new XWalkUIClient(mXWalkView) {
            @Override
            public boolean onConsoleMessage(XWalkView view, String message, int lineNumber,
                                            String sourceId, ConsoleMessageType messageType) {
                Log.i("WebViewActivity", "----------------------------------------------"
                        + message + " -- From line "
                        + lineNumber + " of "
                        + sourceId);
                Calendar cal = Calendar.getInstance();
                et.append(FORMAT.format(cal.getTime()));
                et.append("\t");
                et.append(message);
                et.append(" -- From line ");
                et.append(Integer.toString(lineNumber));
                et.append(" of ");
                et.append(sourceId);
                et.append("\n");
                return super.onConsoleMessage(view, message, lineNumber, sourceId, messageType);
            }
        });
        et = (EditText)findViewById(R.id.console_log_text);
        et.setBackgroundColor(Color.GRAY);
        et.setTextColor(Color.GREEN);
    }
}
