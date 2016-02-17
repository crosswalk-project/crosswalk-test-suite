Feature: Embedding api usecase tests
    Scenario: Multi_XWalkView_Image
        When I launch "stability-embeddingapi-android-tests" with "org.xwalkview.stability.app" and "ImageXWalkViewsActivity" on android
         And I wait for 5 seconds
         And I click view "resourceId=org.xwalkview.stability.app:id/views_num"
         And I edit view "resourceId=org.xwalkview.stability.app:id/views_num" to input "10"
         And I press "back" hardware key
         And I click view "text=Add Views^^^className=android.widget.Button"
        Then I should see view "text=10^^^resourceId=org.xwalkview.stability.app:id/result_show" in 120 seconds
