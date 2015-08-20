Feature: Embedding api usecase tests
    Scenario: extension can be supported with additional permissions
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "ContactExtensionActivity" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
         And I edit index 0 EditText to input "jacky"
         And I edit index 1 EditText to input "10010"
         And I click view "description=Write Contact"
         And I wait for 1 seconds
         And I click view "description=Read Contact"
         And I wait for 1 seconds
        Then I should see view "description=passed"
         And I remove all watchers
