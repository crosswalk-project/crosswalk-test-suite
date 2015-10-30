Feature: Embedding api usecase tests
    Scenario: load app from manifest
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "basic.XWalkViewWithLoadAppFromManifest" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I register watcher "AlertOK" when "Javascript Alert" click "OK"
         And I force to run all watchers
         And I wait for 3 seconds
        Then I should see view "descriptionContains=Hello World."
         And I remove all watchers
