Feature: Embedding api usecase tests
    Scenario: Long_Time_WebView_Swipe
        When I launch "stability-embeddingapi-android-tests" with "org.xwalkview.stability.app" and "SwipeWebViewsActivity" on android
         And I wait for 5 seconds
        Then I repeat fling to end and beginning vertically in 3600 seconds
