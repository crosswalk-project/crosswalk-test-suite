Feature: Embedding api usecase tests
    Scenario: Check xwalk pause & resume js time
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.asyncsample" and "PauseTimersActivity" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
         And I click view "resourceId=org.xwalk.embedded.api.asyncsample:id/pause"
         And I save relative view "className=android.view.View" on the "down" side of view "description=A script on this page starts this clock:" to object "clock_time"
         And I save object "clock_time" info "contentDescription" to temp "clock_pause"
         And I wait for 3 seconds
         And I save object "clock_time" info "contentDescription" to temp "clock_after_pause"
        Then The saved info "clock_pause" is equal to "clock_after_pause"
         And I click view "resourceId=org.xwalk.embedded.api.asyncsample:id/pause"
         And I wait for 3 seconds
         And I save object "clock_time" info "contentDescription" to temp "clock_onresume"
        Then The saved info "clock_after_pause" is unequal to "clock_onresume"
         And I remove all watchers
