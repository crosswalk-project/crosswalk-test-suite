Feature: Usecase WebAPI
 Scenario: Performance & Optimization/Usertiming Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/Usertiming/index.html"
     And I press "compute"
    Then I should see "Infinity" in "result" area
    Then I should see "ms" in "start" area
    Then I should see "ms" in "duration" area

