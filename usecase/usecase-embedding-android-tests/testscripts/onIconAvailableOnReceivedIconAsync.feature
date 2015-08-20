Feature: Embedding api usecase tests
    Scenario: load icon when it's available
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.asyncsample" and "OnIconAvailableOnReceivedIconActivityAsync" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
        Then I should see view "text=onIconAvailable 2 times"
        Then I should see view "text=onReceivedIcon 2 times"
        Then I should see view "resourceId=org.xwalk.embedded.api.asyncsample:id/imageView1"
        Then I should see view "resourceId=org.xwalk.embedded.api.asyncsample:id/imageView2"
         And I remove all watchers
