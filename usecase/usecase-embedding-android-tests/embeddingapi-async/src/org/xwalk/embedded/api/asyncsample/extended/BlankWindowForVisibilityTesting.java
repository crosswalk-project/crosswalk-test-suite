package org.xwalk.embedded.api.asyncsample.extended;

import org.xwalk.embedded.api.asyncsample.R;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class BlankWindowForVisibilityTesting extends Activity {

    private Activity thisActivity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_blank_window_for_visibility_testing);

        Button button = (Button)findViewById(R.id.return_button);
        thisActivity = this;
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                thisActivity.finish();
            }
        });
    }
}
