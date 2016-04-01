Feature: Usecase WebAPI
 Scenario: Networking & Storage/SessionHistory Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/SessionHistory/index.html"
    Then I should see "10" in "sessionID" area
     And I click "sback"
    Then I should see "9" in "sessionID" area
     And I click "sback"
    Then I should see "8" in "sessionID" area
     And I click "sback"
    Then I should see "7" in "sessionID" area
     And I click "sforward"
    Then I should see "8" in "sessionID" area
     And I click "sforward"
    Then I should see "9" in "sessionID" area
     And I click "sforward"
    Then I should see "10" in "sessionID" area
