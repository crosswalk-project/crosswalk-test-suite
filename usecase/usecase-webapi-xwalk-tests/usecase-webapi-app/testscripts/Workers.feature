Feature: Usecase WebAPI
 Scenario: Performance & Optimization/Workers Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/Workers/index.html"
     And I press "start"
    Then I should see "5000050000" in "outPut" area

