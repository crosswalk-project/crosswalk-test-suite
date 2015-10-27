Feature: Embedding api usecase tests
    Scenario: Multi_Tab_WebView_Image
        When I launch "stability-embeddingapi-android-tests" with "org.xwalkview.stability.app" and "TabImageWebViewsActivity" on android
         And I wait for 5 seconds
         And I click view "text=Add Views^^^className=android.widget.Button"
        Then I should see view "text=20^^^resourceId=org.xwalkview.stability.app:id/result_show" in 60 seconds
