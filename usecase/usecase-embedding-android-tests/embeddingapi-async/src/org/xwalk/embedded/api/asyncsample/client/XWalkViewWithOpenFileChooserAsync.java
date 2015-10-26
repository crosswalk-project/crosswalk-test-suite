package org.xwalk.embedded.api.asyncsample.client;
import org.xwalk.embedded.api.asyncsample.R;

import java.io.FileNotFoundException;
import java.io.IOException;

import android.app.Activity;
import android.app.AlertDialog;
import org.xwalk.core.XWalkInitializer;
import org.xwalk.core.XWalkUIClient;
import org.xwalk.core.XWalkView;

import android.content.ContentResolver;
import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.webkit.ValueCallback;
import android.widget.ImageView;

public class XWalkViewWithOpenFileChooserAsync extends Activity implements XWalkInitializer.XWalkInitListener {
    private XWalkView mXWalkView;
    private XWalkInitializer mXWalkInitializer;
    private ImageView mImageView;
    private ValueCallback<Uri> mUploadMessage;

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
        setContentView(R.layout.openfile_layout);
        mXWalkView = (XWalkView) findViewById(R.id.xwalkview);
        mImageView = (ImageView) findViewById(R.id.imageview);

        StringBuffer mess = new StringBuffer();
        mess.append("Test Purpose: \n\n")
        .append("Verifies XWalkView can open local file.\n\n")
        .append("Test  Step:\n\n")
        .append("1. Click 'Choose File' button.\n")
        .append("2. Select system gallery app and choose one photo.\n")
        .append("Expected Result:\n\n")
        .append("Test passes if this photo shows on the green background region.");
        new  AlertDialog.Builder(this)
        .setTitle("Info" )
        .setMessage(mess.toString())
        .setPositiveButton("confirm" ,  null )
        .show();

        mXWalkView.setUIClient(new UIClient(mXWalkView));
        mXWalkView.load("file:///android_asset/open_file.html", null);
    }


    class UIClient extends XWalkUIClient {

        public UIClient(XWalkView xwalkView) {
            super(xwalkView);
        }

        public void openFileChooser(XWalkView view, ValueCallback<Uri> uploadFile,
                String acceptType, String capture) {
            super.openFileChooser(view, uploadFile, acceptType, capture);
            mUploadMessage = uploadFile;
        }
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent intent) {
        // TODO Auto-generated method stub
        if (mUploadMessage == null) return;
        Uri result = intent == null || resultCode != RESULT_OK ? null : intent.getData();
        mUploadMessage.onReceiveValue(result);
        mUploadMessage = null;

        Bitmap bm = null;
        ContentResolver resolver = getContentResolver();
        try {
            bm = MediaStore.Images.Media.getBitmap(resolver, result);
            mImageView.setImageBitmap(bm);
            bm = null;
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
