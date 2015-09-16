Feature: Embedding api usecase tests
    Scenario: Check XWalkCookieManager can setAcceptFileSchemeCookies & allowFileSchemeCookies
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.asyncsample" and "AcceptFileSchemeCookiesActivityAsync" on android
         And I register watcher "ClearInfoWindow" when "Info" click "confirm"
         And I force to run all watchers
         And I wait for 3 seconds
         And I click view "text=getCookie"
         Then I should not see view "textContains=test123"
         And I click view "text=setAcceptFileSchemeCookies True"
         And I click view "text=getCookie"
         And I click view "text=getCookie"
         Then I should see view "textContains=test123"
         And I click view "text=setAcceptFileSchemeCookies False"
         And I click view "text=getCookie"
         Then I should not see view "textContains=test123"
         And I remove all watchers
