Feature: Usecase WebAPI
 Scenario: Performance & Optimization/HrtimeAndroid Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/HrtimeAndroid/index.html"
     And I click "play"
    Then I should see "Waiting"
     And I wait 31 seconds
    Then I should see "Play"
     And I save "value1" from "playtime" area
    Then "value1" should be between "29000" to "31000"
