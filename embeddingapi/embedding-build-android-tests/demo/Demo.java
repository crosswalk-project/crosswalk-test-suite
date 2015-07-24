package {pkg_name};

import org.xwalk.core.XWalkView;

import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnKeyListener; 
import android.app.Activity;
import android.os.Bundle;

public class {app_name} extends Activity {
  private XWalkView mXWalkView;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    mXWalkView = (XWalkView) findViewById(R.id.activity_main);
    mXWalkView.load("http://crosswalk-project.org/", null);
  }
}
