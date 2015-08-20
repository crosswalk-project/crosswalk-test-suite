Feature: Embedding api usecase tests
    Scenario: echo extension
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.asyncsample" and "EchoExtensionActivityAsync" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
        Then I should see relative view "description=passed" on the "down" side of view "descriptionContains=From java sync:"
        Then I should see relative view "description=passed" on the "down" side of view "descriptionContains=From java async:"
         And I remove all watchers
