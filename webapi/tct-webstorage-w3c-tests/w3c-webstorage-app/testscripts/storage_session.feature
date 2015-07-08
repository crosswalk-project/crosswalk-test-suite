Feature: w3c-webstorage
 Scenario: storage session
    When launch "w3c-webstorage-app"
    And I go to "webstorage/w3c/storage_session-manual.html"
    And I press "clear_button"
    And I reload
    And I wait 1 seconds
    Then I should see "You have viewed this page 1 time(s)."
    And quit "w3c-webstorage-app"
    When launch "w3c-webstorage-app"
    And I go to "webstorage/w3c/storage_session-manual.html"
    Then I should see "You have viewed this page 1 time(s)."
