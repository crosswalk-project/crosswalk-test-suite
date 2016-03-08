package org.xwalk.embedded.api.asyncsample.basic;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.ClientCertRequest;
import org.xwalk.core.XWalkResourceClient;
import org.xwalk.core.XWalkView;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

public class XWalkViewWithClearClientCertPreferencesAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private TextView mClientCertRequest;
    private XWalkInitializer mXWalkInitializer;
    private static final String BAD_SSL_WEBSITE = "https://egov.privasphere.com/";

    class ResourceClient extends XWalkResourceClient {

        public ResourceClient(XWalkView xwalkView) {
            super(xwalkView);
        }

        public void onReceivedClientCertRequest(XWalkView view,
                ClientCertRequest handler) {
            // TODO Auto-generated method stub
            mClientCertRequest.setText("ClientCert Request: " + handler + "\n");
            handler.cancel();
        }
    }


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
        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can clear client certificate preferences.\n\n")
        .append("Test Step:\n\n")
        .append("1. Load the url defautly and ClientCertRequest info will show.\n")
        .append("2. Click 'Reload' button and the info will disapper.\n")
        .append("3. Click 'Clear ClientCert Preferences' button.\n")
        .append("4. Click 'Reload' button and the info will show again.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if XWalkView can clear client certificate preferences.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        setContentView(R.layout.activity_xwalk_view_with_clear_clientcert_preferences_async);
        mXWalkView = (XWalkView) findViewById(R.id.xwalk_view);
        mClientCertRequest = (TextView) findViewById(R.id.client_request);

        mXWalkView.setResourceClient(new ResourceClient(mXWalkView));
        mXWalkView.load(BAD_SSL_WEBSITE, null);

        Button clear = (Button) findViewById(R.id.clear_button);
        clear.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mXWalkView.clearClientCertPreferences(null);
            }
        });

        Button reload = (Button) findViewById(R.id.reload_button);
        reload.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                mClientCertRequest.setText("");
                mXWalkView.load(BAD_SSL_WEBSITE, null);
            }
        });
    }
}