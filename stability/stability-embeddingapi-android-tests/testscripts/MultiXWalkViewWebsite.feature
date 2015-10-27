Feature: Embedding api usecase tests
    Scenario: Multi_XWalkView_Website
        When I launch "stability-embeddingapi-android-tests" with "org.xwalkview.stability.app" and "AddXWalkViewsActivity" on android
         And I wait for 5 seconds
         And I edit view "resourceId=org.xwalkview.stability.app:id/views_num" to input "20"
         And I press "back" hardware key
         And I click view "text=Add Views^^^className=android.widget.Button"
        Then I should see view "text=20^^^resourceId=org.xwalkview.stability.app:id/result_show" in 60 seconds
