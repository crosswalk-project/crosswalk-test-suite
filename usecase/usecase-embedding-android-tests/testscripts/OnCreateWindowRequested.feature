Feature: Embedding api usecase tests
    Scenario: create new window
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "client.XWalkViewWithOnCreateWindowRequested" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
         And I click view "className=android.widget.Button^^^description=Create Window on blank"
         And I click view "className=android.view.View^^^description=Create Window on blank"
        Then I should see view "text=2 times"
         And I click view "className=android.widget.Button^^^description=Create Window on blank"
         And I click view "className=android.view.View^^^description=Create Window on blank"
        Then I should see view "text=4 times"
         And I remove all watchers
