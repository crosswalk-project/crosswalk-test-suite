Feature: Usecase WebAPI
 Scenario: Performance & Optimization/HrtimeAndroid Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/HrtimeAndroid/index.html"
     And I click "play"
    Then I should see "Waiting"
     And I wait 31 seconds
    Then I should see "Play"
    Then I should see between "29000" and "31000" in "playtime" area

