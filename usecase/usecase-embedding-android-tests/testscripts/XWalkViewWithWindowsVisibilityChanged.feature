Feature: Embedding api usecase tests
    Scenario: get API version and xwalk version
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "extended.XWalkViewWithWindowsVisibilityChanged" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
         And I click view "text=Open a new Window"
         And I click view "text=Return"
        Then I should see view "textContains=GONE->VISIBLE"
         And I remove all watchers
