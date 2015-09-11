Feature: Embedding api usecase tests
    Scenario: get API version and xwalk version
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.asyncsample" and "XWalkVersionAndAPIVersionAsync" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
        Then I should see view "textContains=API Version: 5.0; XWalk Version: 1"
         And I remove all watchers
