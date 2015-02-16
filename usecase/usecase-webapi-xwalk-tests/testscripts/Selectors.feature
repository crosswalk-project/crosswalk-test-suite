Feature: Usecase WebAPI
 Scenario: Performance & Optimization/Selectors Test
    When launch "usecase-webapi-xwalk-tests"
     And I go to "/samples/Selectors/index.html"
     And I press "querySelector"
    Then I should see "d1" area in "green" color
     And I press "querySelectorAll"
    Then I should see "d1" area in "green" color
    Then I should see "d2" area in "green" color
    Then I should see "d3" area in "green" color

